from django import forms


class ContactForm(forms.Form):

    subject = forms.CharField(
            required = True,
            label = '',
            widget = forms.TextInput(
                    attrs = {
                            "placeholder": "Enter subject",

                    },
            )
    )
    message = forms.CharField(
            label = '',
            required = True,
            help_text = None,
            widget = forms.Textarea(

                    attrs = {
                            "placeholder": "Enter message",

                    },
            )
    )

    def clean_subject(self):
        return self.cleaned_data['subject']

    def clean_message(self):
        return self.cleaned_data['message']
