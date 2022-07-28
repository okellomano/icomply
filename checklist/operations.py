from django.db.models import Sum
from .models import Checklist, UserChecklistEntries


def calculate_scores(score_entries=None):
    '''Calculating the user score. '''
    user_score_total = 0
    for score_id in score_entries:
        checklist_item = Checklist.objects.get(id=score_id)
        user_score_total = user_score_total + checklist_item.value

    summation = Checklist.objects.aggregate(Sum('value'))
    total_available_score = summation['value__sum']

    percent = round((user_score_total / total_available_score) * 100)

    return {'percent': percent, 'user_score_total': user_score_total, 'total_available_score': total_available_score}


def get_compliance_tier(percent=None):
    '''Get and returns the percentage score. '''
    if percent > 90:
        tier_level = 'Tier 1'
    elif percent > 80:
        tier_level = 'Tier 2'
    elif percent > 70:
        tier_level = 'Tier 3'
    elif percent > 50:
        tier_level = 'Tier 4'
    else:
        tier_level = 'Non-compliant'

    return tier_level


def save_user_entries(user=None, entries=None):
    '''Save user results to the database. '''

    for entry_id in entries:
        try:
            checklist_item = Checklist.objects.get(id=entry_id)
        except:
            pass
        else:
            scores = calculate_scores(entries)

            percentage = scores['percent']
            user_score = scores['user_score_total']
            total_values = scores['total_available_score']

            tier_level = get_compliance_tier(percentage)

            user_entry = UserChecklistEntries()

            user_entry.user = user
            user_entry.percent_s = percentage
            user_entry.tier = tier_level
            user_entry.user_score = user_score
            user_entry.total_values = total_values
            user_entry.checklist = checklist_item

            user_entry.save()


def get_user_scores_for_specific_checklist(user=None, checklist_id=None):
    entries = UserChecklistEntries.objects.filter(user=user, checklist_id=checklist_id).values_list('checklist_id', flat=True)
    scores_entries = []
    for entry in entries:
        scores_entries.append(entry)

    scores = calculate_scores(score_entries=scores_entries)
    return scores


