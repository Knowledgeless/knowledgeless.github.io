from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(
        label='Your Name',
        max_length=30,
        widget=forms.TextInput(attrs={'placeholder': 'Your Name'})
    )
    email = forms.EmailField(
        label='Your Email',
        max_length=254,
        widget=forms.EmailInput(attrs={'placeholder': 'Email'})
    )
    message = forms.CharField(
        label='Your Message',
        max_length=2000,
        widget=forms.Textarea(attrs={'placeholder': 'Write your message here'}),
        help_text=''
    )
    source = forms.CharField(
        max_length=50,
        widget=forms.HiddenInput(),
        initial='Contact Form'  # You can set an initial value if needed
    )

    def clean(self):
        cleaned_data = super(ContactForm, self).clean()
        name = cleaned_data.get('name')
        email = cleaned_data.get('email')
        message = cleaned_data.get('message')
        if not name and not email and not message:
            raise forms.ValidationError('You have to write something!')