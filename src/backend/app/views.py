from app import app
from app import db
from flask import make_response, request, render_template, redirect, flash, url_for, send_file
from app.classifications.nBayes import nbayes
from app.classifications.dTree import dtree
from app.classifications.knn import kNeigh
from app.classifications.svm import svm
from app.classifications.processing import addHeaders
from werkzeug.utils import secure_filename
from app.forms import ConfigForm, MetricForm
from app.models import Filestorage
import pygal
from io import BytesIO, StringIO
import pandas as pd

def allowed_file(filename):
    return '.' in filename and \
        filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/upload', methods=['GET', 'POST'])
def upload():
    form = ConfigForm()
    Mform = MetricForm()
    
    return render_template("upload.html", form=form, Mform=Mform)

@app.route('/form', methods=['GET', 'POST'])
def form():
    form = MetricForm()
    Cform = ConfigForm()

    db.session.query(Filestorage).delete()
    db.session.commit()
    db.create_all()

    file = request.files['inputFile']
    filename = file.filename
    csv_file = pd.read_csv(file)

    if Cform.header_check.data == 'No':
        csv_file = addHeaders(csv_file)
        headers = list(csv_file)
    else:
        headers = list(csv_file)

    csv = csv_file.to_csv(index=False)
    csv_encode = csv.encode('utf-8')

    newFile = Filestorage(name=file.filename, data=csv_encode)
    db.session.add(newFile)
    db.session.commit()

    file_data = Filestorage.query.filter_by(id=1).first()

    choices = [(headers[i], headers[i]) for i in range(len(headers))]

    form.selectedAtt.choices = choices
    form.targetAtt.choices = choices

    if request.method == 'POST' and form.validate_on_submit():
        return render_template('result.html')
    else:
        return render_template('form.html', form=form, headers=headers)

def sortClassifers(targetAtt, chosenAtt, csv_file, split):
    Mform = MetricForm()

    results = []

    if Mform.nbCheck.data == True:
        nb_result = nbayes(csv_file, chosenAtt, targetAtt, split)
        nb_dict = {}
        nb_dict["Classifier_Used"] = "Naive Bayes"
        nb_dict["Result"] = round(nb_result*100, 4)
        results.append(nb_dict)

    if Mform.svmCheck.data == True:
        svm_result = svm(csv_file, chosenAtt, targetAtt, split)
        svm_dict = {}
        svm_dict["Classifier_Used"] = "Support Vector Machines"
        svm_dict["Result"] = round(svm_result*100, 4)
        results.append(svm_dict)

    if Mform.dtCheck.data == True:
        metric = Mform.dtMetric.data
        dt_result = dtree(csv_file, chosenAtt, targetAtt, metric, split)
        dt_dict = {}
        dt_dict["Classifier_Used"] = "Decision Tree"
        dt_dict["Result"] = round(dt_result*100, 4)
        results.append(dt_dict)

    if Mform.knnCheck.data == True:
        kmetric = Mform.knnMetric.data
        k = Mform.kValue.data
        knn_result = kNeigh(csv_file, chosenAtt, targetAtt, k, kmetric, split)
        knn_dict = {}
        knn_dict["Classifier_Used"] = "K-Nearest Neighbours"
        knn_dict["Result"] = round(knn_result*100, 2)
        results.append(knn_dict)


    return results

@app.route('/result', methods=['GET', 'POST'])
def result():
    form = MetricForm()
    Mform = ConfigForm()
    graph = pygal.Bar()

    targetAtt = form.targetAtt.data
    selectedAtt = form.selectedAtt.data

    split = form.split.data
 
    file_data = Filestorage.query.filter_by(id=1).first()
    csv_file = pd.read_csv(BytesIO(file_data.data))

    results = sortClassifers(targetAtt, selectedAtt, csv_file, split)

    label = []
    data = []
    for result in results:
        label.append(result['Classifier_Used'])
        data.append(result['Result'])

    graph.title = 'Accuracy Results'
    graph.x_labels = label
    graph.add('Results', data)
    graph_data = graph.render_data_uri()

    return render_template('result.html', results=results, form=form, Mform=Mform, graph_data=graph_data)

@app.route('/about')
def about():
    return render_template('about.html')