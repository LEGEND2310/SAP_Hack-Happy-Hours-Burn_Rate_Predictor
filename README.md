# SAP_Hack-Happy-Hours-Burn_Rate_Predicto

This project is being submitted by the team Tech_Enthus consisting of:
1) Deepak Kumar Jha ([LEGEND2310](https://github.com/LEGEND2310))
2) Sankalp Verma ([KillaShank](https://github.com/KillaShank))
3) Swattik Maiti ([PerciValXIII](https://github.com/PerciValXIII))
4) Shubhankar Shankar ([shubhankarshankar](https://github.com/shubhankarshankar))

This is in lieu of the submission to be given for the hackathon conducted by SAP Labs on the HackerEarth platform.

Happy Hours is an online web application that can manage the well-being status of the employees in a company through an interactive dashboard provided to the Human Resources department and also the Upper Management of the company.
The web app can clearly demonstrate the status of the employees working there and how are they feeling with the amount of work put on them.
In addition to this, the web app can identify a person's personality over 4 different axes by analyzing their publicly available social media posts.
This can provide a deeper insight as to how well will they be able to cope with pressure.

## About the Files

This repository has the following main folders:

1) [Frontend](https://github.com/LEGEND2310/SAP_Hack-Happy-Hours-Burn_Rate_Predictor/tree/main/Frontend):
   This folder contains all the files for the frontend and static files.
2) [ML alogs and API](https://github.com/LEGEND2310/SAP_Hack-Happy-Hours-Burn_Rate_Predictor/tree/main/ML%20alogs%20and%20API):
    This folder consists of all the Machine Learning and Deep Learning Models along with their Flask APIs:
    1) [Burnrate API](https://github.com/LEGEND2310/SAP_Hack-Happy-Hours-Burn_Rate_Predictor/tree/main/ML%20alogs%20and%20API/Burnrate%20API):
      The model used to predict burnout rate in employees using basic information.
    2) [Personality prediction API](https://github.com/LEGEND2310/SAP_Hack-Happy-Hours-Burn_Rate_Predictor/tree/main/ML%20alogs%20and%20API/Personality%20prediction%20API):
      The model used to predict the personality of an individual using thier usual social media posts.


## Running the Application

To run, clone the repository using the follwowing command in git bash:

```
git clone https://github.com/LEGEND2310/SAP_Hack-Happy-Hours-Burn_Rate_Predictor.git
```

Navigate to frontend folder and run home.html.

To run the ML and DL models, you will additionally have to install some python packages are required given in the requirements.txt file using:

```
pip install -r requirements.txt
```

To run the flask file as local host use the command
```
python app.py
```

## The Machine Learning and Deep Learning Models

This Model implements 2 main models. One Machine Learing model to predict the burnout rate of an employee given the basic information of the employee from a HR database.
The Model implemented is a Linear Regression Model. It uses the following flow:

![linar reg flow](https://user-images.githubusercontent.com/47575172/115266986-50376880-a156-11eb-9474-f849e89dd1e4.png)

Our application also uses a Deep Learning model to perdict a person's personality.
Personality is divided into 4 different axes of perosanilities.
We have made 4 models with 4 different weights and biases for each of the personality traits using posts made by the user.
The model architecture can be visualised as:

![model0](https://user-images.githubusercontent.com/47575172/115267890-524df700-a157-11eb-955e-42ab985bf5e1.png)

## Screenshots from the application


![1 (1)](https://user-images.githubusercontent.com/47575172/115268757-3c8d0180-a158-11eb-9aeb-034c1a9309bf.PNG)

![2 (1)](https://user-images.githubusercontent.com/47575172/115268838-50386800-a158-11eb-9bff-5a788e0e01b3.PNG)