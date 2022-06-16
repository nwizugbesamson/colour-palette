from cv2 import kmeans
from flask import Blueprint, render_template, redirect, request, url_for, abort
from project.forms import UploadForm
from werkzeug.utils import secure_filename
import numpy as np
import cv2 as cv
from sklearn.cluster import KMeans

# CREATE BLUEPRINT OBJECT
main = Blueprint(name="main", import_name=__name__, static_folder="static", template_folder="templates")


# READ THE IMAGE USING CV2
def read_image(upload_file):
    npimg = np.fromfile(upload_file, np.uint8)
    upload_file = cv.imdecode(npimg, cv.IMREAD_COLOR)
    upload_file = cv.cvtColor(upload_file, cv.COLOR_BGR2RGB)
    return upload_file


def calculate_max_colour_freq(upload_file):
    upload_file = upload_file.reshape(-1, 3)
    high_freq, counts = np.unique(upload_file, axis=0, return_counts=True)
    most_freq_color = high_freq[np.argmax(counts)]
    most_freq_color = tuple(most_freq_color)
    return most_freq_color


def calculate_clusters(upload_file):
    upload_file = upload_file.reshape(-1, 3)
    clt = KMeans(n_clusters=5)
    clt.fit(upload_file)
    top_5 = clt.cluster_centers_
    top_5 = list(map(tuple, top_5))
    return top_5


@main.route('/', methods=["GET", "POST"])
def home_page():
    form = UploadForm()
    if form.validate_on_submit():
        upload_file = form.upload_file.data
        file_name = secure_filename(upload_file.filename)
        upload_file = read_image(upload_file)
        max_freq = calculate_max_colour_freq(upload_file)
        top_colors = calculate_clusters(upload_file)
        print(max_freq)
        print(top_colors)
        return render_template("index.html", max_freq=max_freq, top_colors=top_colors)
    return render_template("index.html", form=form)
