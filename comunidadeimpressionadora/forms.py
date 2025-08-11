from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from flask_login import current_user
from flask_wtf.file import FileAllowed, FileField
from comunidadeimpressionadora.models import Usuario


class FormCriarConta(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    senha = PasswordField('Password', validators=[DataRequired(), Length(6, 20)])
    confirmacao_senha = PasswordField('Password Confirmation', validators=[DataRequired(), EqualTo('senha')])
    botao_submit_criarconta = SubmitField('Create Account')

    def validate_email(self, email):
        usuario = Usuario.query.filter_by(email=email.data).first()
        if usuario:
            raise ValidationError('Email already exists, please register a new email or sign in.')


class FormLogin(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    senha = PasswordField('Senha', validators=[DataRequired(), Length(6, 20)])
    botao_submit_login = SubmitField('Log in')
    lembrar_dados = BooleanField('Remember me')

class FormEditarPerfil(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    foto_perfil = FileField('Choose a New Profile Picture', validators=[FileAllowed(['jpg', 'png'])])
    curso_exel = BooleanField('Exel')
    curso_vba = BooleanField('VBA')
    curso_python = BooleanField('Python')
    curso_sql = BooleanField('SQL')
    curso_ppt = BooleanField('Power Point')
    curso_powerbi = BooleanField('PowerBI')
    botao_submit_editarperfil = SubmitField('Update Profile')

    def validate_email(self, email):
        if current_user.email != email.data:
            usuario = Usuario.query.filter_by(email=email.data).first()
            if usuario:
                raise ValidationError('User already exists, log in or register a new email.')

class FormCriarPost(FlaskForm):
    titulo = StringField('Post Title', validators=[DataRequired(), Length(2, 140)])
    corpo = TextAreaField('Write here', validators=[DataRequired()])
    botao_submit = SubmitField('Create Post')