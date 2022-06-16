from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed, FileRequired
from wtforms import  SubmitField

# using flask uploads package
# images = UploadSet('images', IMAGES)

class UploadForm(FlaskForm):

    upload_file = FileField(
        label="Select an image", 
        validators=[FileRequired(message="upload a file"),
         FileAllowed(upload_set=['jpg', 'png'], message='Images only!')]
         )
    submit = SubmitField("upload")