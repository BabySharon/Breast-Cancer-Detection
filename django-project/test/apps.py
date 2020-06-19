from django.apps import AppConfig
import torch
import numpy as np
import matplotlib.pyplot as plt
import torch
import time
import numpy as np
from torch import nn, optim
import torch.nn.functional as F
from torchvision import datasets, transforms, models
import torchvision
from collections import OrderedDict
from torch.autograd import Variable
from PIL import Image
from torch.optim import lr_scheduler
import copy
import json
import os
from os.path import exists



class TestConfig(AppConfig):
   
    name = 'test'
    idx_to_class={}
    
    def load_checkpoint(filepath):
        checkpoint = torch.load(filepath,map_location=lambda storage, loc: storage)
        model = models.resnet152()
        
        # Our input_size matches the in_features of pretrained model
        input_size = 2048
        output_size = 2
        
        classifier = nn.Sequential(OrderedDict([
                            ('fc1', nn.Linear(2048, 512)),
                            ('relu', nn.ReLU()),
                            #('dropout1', nn.Dropout(p=0.2)),
                            ('fc2', nn.Linear(512, 2)),
                            ('output', nn.LogSoftmax(dim=1))
                            ]))

    # Replacing the pretrained model classifier with our classifier
        model.fc = classifier
        
        
        model.load_state_dict(checkpoint['state_dict'])
        
        return model, checkpoint['class_to_idx']

    # Get index to class mapping



    def process_image(image):
    #Scales, crops, and normalizes a PIL image for a PyTorch model,
    #returns an Numpy array
    
    
        # Process a PIL image for use in a PyTorch model

        size = 256, 256
        image.thumbnail(size, Image.ANTIALIAS)#img resize
        image = image.crop((128 - 112, 128 - 112, 128 + 112, 128 + 112))
        npImage = np.array(image)#creating nd array/ndimensional array
        npImage = npImage/255.#normalising to 0 to 1 scale
            
        imgA = npImage[:,:,0]#x,y,rgb pixel
        imgB = npImage[:,:,1]
        imgC = npImage[:,:,2]
        
        imgA = (imgA - 0.485)/(0.229) #normalisation values standard, from imagenet
        imgB = (imgB - 0.456)/(0.224)
        imgC = (imgC - 0.406)/(0.225)
            
        npImage[:,:,0] = imgA
        npImage[:,:,1] = imgB
        npImage[:,:,2] = imgC
        
        npImage = np.transpose(npImage, (2,0,1))
        
        return npImage

        
    def predict(image_path, model, topk=2):
    #Predict the class (or classes) of an image using a trained deep learning model.
    
    
        # Implement the code to predict the class from an image file
        
        image = torch.FloatTensor([TestConfig.process_image(Image.open(image_path))])
        model.eval()
        output = model.forward(Variable(image))
        pobabilities = torch.exp(output).data.numpy()[0]
        

        top_idx = np.argsort(pobabilities)[-topk:][::-1] 
        top_class = [TestConfig.idx_to_class[x] for x in top_idx]
        top_probability = pobabilities[top_idx]

        return top_probability, top_class


    # Display an image along with the top 2 classes
    def view_classify(img, probabilities, classes, mapper):
        #Function for viewing an image and it's predicted classes.
            print(img)
            img_filename = img #.split('/')[-2]
            # img = Image.open('media\\images\\' +img)

            fig, (ax1, ax2) = plt.subplots(figsize=(6,10), ncols=1, nrows=2)
            # cancer_type = mapper[img_filename]
            
            # ax1.set_title(cancer_type)
            # ax1.imshow(img)
            # ax1.axis('off')
            
            y_pos = np.arange(len(probabilities))
            ax2.barh(y_pos, probabilities)
            ax2.set_yticks(y_pos)
            ax2.set_yticklabels([mapper[x] for x in classes])
            ax2.invert_yaxis()
           

            
            plt.show()              
