from django import forms
from bootstrap_datepicker_plus import DateTimePickerInput
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Row, Column, Submit, Reset, HTML

from apps.trade import models


class JournalForm(forms.ModelForm):
    class Meta:
        model = models.Journal
        fields = "__all__"
        widgets = {
            'entry_time':  DateTimePickerInput(format='%d/%m/%Y'),
            'closed_time': DateTimePickerInput(format='%d/%m/%Y'),
        }

    def __init__(self, *args, **kwargs):
        super(JournalForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Save', css_class='btn btn-outline-primary'))
        self.helper.add_input(Reset('reset', 'Cancel', css_class='btn btn-outline-warning'))
        self.helper.layout = Layout(
            Row(
                Column(
                    Row(Column('symbol_name')),
                    Row(Column('upcoming_event')),
                    css_class='col-sm-4'
                ),
                Column('pre_analysis', css_class='col-sm-8 '),
            ),
            Row(
                Column('trade_note', css_class='col-sm-12')
            ),
            Row(
                Column('htf_image', HTML("""{% if form.htf_image.value %}<img class="img-responsive" src="{{ MEDIA_URL }}{{ form.htf_image.value }}">{% endif %}""", )),
                # Column('htf_image', css_class='col-sm-4'),
                Column('ttf_image', css_class='col-sm-4'),
                Column('ltf_image', css_class='col-sm-4'),
            ),
            Row(
                Column('entry_time'),
                Column('entry_type', css_class='col-sm-3'), Column('entry_price', css_class='col-sm-3'),
                Column('entry_sl', css_class='col-sm-3'), Column('entry_tp', css_class='col-sm-3')
            ),
            Row(
                Column('during_trade_analysis')
            ),
            Row(
                Column('closed_price'), Column('closed_time'), Column('trade_image', css_class='col-sm-8')
            ),
            Row(
                Column('post_analysis')
            )
        )
