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
