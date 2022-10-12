from flask import Flask, flash, request, redirect, url_for, render_template
from flask import session

import os
from werkzeug.utils import secure_filename

import numpy as np
from keras_preprocessing.image import load_img
from keras.models import load_model


 
app = Flask(__name__)
 
UPLOAD_FOLDER = 'static/uploads/'
 
app.secret_key = "secret key"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
#app.config['MAX_CONTENT_LENGTH'] = 5 * 224 * 224
 
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])


 
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
     
a= """ It is considered a chronic form of eczema, Benign keratosis appears on the body where there is a lot of oil-producing (sebaceous) glands like the upper back, nose, and scalp  
"""
b=""" Melanoma occurs when something goes wrong in the melanin-producing cells (melanocytes) that give color to your skin."""

c=""" Melanocytic Nevi is usually a non-cancerous disorder of pigment-producing skin cells and is commonly called birthmarks or moles."""
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/index.html')
def index():
    return render_template('index.html')
 
@app.route('/', methods=['POST'])
def upload_image():
    
    
    
    
    if 'file' not in request.files:
        flash('No file part')
        return redirect(request.url)
    file = request.files['file']
    if file.filename == '':
        flash('No image selected for uploading')
        return redirect(request.url)
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        image_path=os.path.join(app.config['UPLOAD_FOLDER'], filename)
        #print('upload_image filename: ' + filename)
        flash('Image successfully uploaded and displayed below')
        model2 = load_model(r'C:\Users\DjS\Downloads\84_3_class.h5')
        image = load_img(image_path, target_size=(224, 224))
        img = np.array(image)
        img = img / 255.0
        img = img.reshape(1,224,224,3)
        label = model2.predict(img)
        maximum=max(label[0])
        label1=list(label[0])
        label2=label1.index(maximum)
        label3=['Benign keratosis','Melanoma','Melanocytic Nevi']
        ans=label3[label2]
        session['ans']=ans
        if label2==0:
            
            return render_template('index.html', prediction=ans,filename=filename)
        if label2==1:
            
            return render_template('index.html', prediction=ans,filename=filename)

        if label2==2:
            return render_template('index.html', prediction=ans,filename=filename)
    else:
        flash('Allowed image types are - png, jpg, jpeg, gif')
        return redirect(request.url)
    
         
@app.route('/display/<filename>')
def display_image(filename):
    #print('display_image filename: ' + filename)
    return redirect(url_for('static', filename='uploads/' + filename), code=301) 


@app.route('/first')
def first():
    ans1=session['ans']
    
    if ans1=='Benign keratosis':
        return render_template('first.html',prediction=ans1,prediction1=a) 
    if ans1=='Melanoma':
        return render_template('first.html',prediction=ans1,prediction2=b) 
    if ans1=='Melanocytic Nevi':
        return render_template('first.html',prediction=ans1,prediction3=c) 



 
if __name__ == "__main__":
    app.run(debug=True)

