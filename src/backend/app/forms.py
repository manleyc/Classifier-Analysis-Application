from wtforms import RadioField, IntegerField, SelectMultipleField, BooleanField, SelectField
from wtforms.validators import InputRequired
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms.widgets import ListWidget, CheckboxInput

class MultiCheckboxField(SelectMultipleField):
    widget = ListWidget(prefix_label=False)
    option_widget = CheckboxInput()

class ConfigForm(FlaskForm):
    file = FileField(validators=[FileRequired(), FileAllowed(['csv'], 'CSV Only!')])
    header_check = RadioField('headers', choices = [('Yes', 'Yes'), ('No', 'No')], default='Yes')

class MetricForm(FlaskForm):
	selectedAtt = SelectMultipleField('selectAtt', choices=[])
	targetAtt = SelectField('targetAtt', choices=[])
	nbCheck = BooleanField('Naive Bayes', default=False)
	dtCheck = BooleanField('Decision Tree', default=False)
	knnCheck = BooleanField('K-Nearest Neighbours', default=False)
	svmCheck = BooleanField('Support Vector Machine', default=False)
	knnMetric = RadioField('Distance Method', choices = [('Manhattan', 'Manhattan'), ('Euclidean', 'Euclidean')], default='Manhattan')
	kValue = IntegerField('K-Value', default = 1)
	split = IntegerField('Train-Test Split', default = 20)
	dtMetric = RadioField('Distance Method', choices = [('Entropy', 'Entropy'), ('Gini', 'Gini Index')], default='Entropy')
	