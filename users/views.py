from allauth.account.views import SignupView


class AccountSignupView(SignupView):
    template_name = 'signup.html'
