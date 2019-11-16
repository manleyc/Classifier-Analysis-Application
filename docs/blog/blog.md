# Blog: Classifier Analysis Application

**Cian Manley**

[markdown](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet)

## 27th of November 2018

I had my first meeting with Mark Roantree in order to layout a plan for the project. For the first version I have decided to create a desktop application of in order to implement the main functionality of the program. Also the different classification algorithm I intent to use are:

- Naive Bayes
- Decision Trees
- K-Nearest Neighbours
- Support Vector Diagrams

These algorithms will be made into different python modules. This will be for the first version of the application. 

By the end of the week, I aim to finish up on the Functional Specification and begin programming. I will be aiming to be able to import the datasets from the desktop app first. Once that is completed I will be able to move on to the implementation of the different algorithms.

## 30th of October 2018

Functional specification has now been completed. From here, I will be moving on to the beginning of the coding. I will be aiming to have a functional desktop application with 2 of the algorithms implemented into it. The first two algorithms I will be using is Naive Bayes and K-Nearest neighbours. 

Throughout this process, I will be getting different types of data sets from a number of different sources. This is to allow continuous testing. 

## 31st of January 2019

After a break for exams, I'm now starting back on work for the project. Today I had a meeting with Mark to go over everything that I have done to date. Now that a skeleton has been create to upload a csv file to and I can start by processing the the datasets passed through the GUI. I have created this shell using PyQt Designer. This is only part of the first version of the program in order to progress into developing the backend.

I'll be moving onto developing a plan for importing the dataset now. Some of the  questions I will be looking at are how the training/testing split will be approached, whether or not I will ask the user for the column names or not and which of the columns will be the feature columns. 

I'm aiming to have built the generic logic for processing any CSV file passed through and to get the first prediction algorithm (Naive Bayes) implemented. I will also be identify my datasets for test purposes from now on also. These will be taken from Kaggle.

## 4th of February 2019

Making progress on the UI at the moment in order to make it as easy to navigate as possible. Once the UI is finished I will begin testing. This is to ensure everything used in the UI is being used and once that is all check I will begin the writing the logic for processing the inputted file. This will be done by asking the user what the columns are and the featured columns.

## 15th of February 2019

From today on, I'm managing my algorithms through the use of jupyter notebooks in order to test them. I will be firstly implementing a Naive Bayes and Support Vector Machines. I will pass my test datasets through these notebooks in order to get a standard score to compare it against my actual program. It will also be used to further develop the modules in order to get a higher accuracy by implementing different techniques.

## 24th of February 2019

Now I have a implemented that when the user enters there csv file it searches for headings in the dataset and displays them to the right of the program. Now that this has been implemented, I started to program the naive bayes module in order to run once asked. For the moment I will be focusing on getting the Naive Bayes implementation sorted then will be moving on to making sure that there are headings involved in the csv file if not the user will be given the option to split them in another form.

I've began documenting the explaination of Naive Bayes into Jupyter notebooks. This is going to be used in order to test my datasets and see how they are passed through the program before implementing them into the actual program. Once the code has been test I will begin to transfer it over to the module. I will also be moving on to K-Nearest Neighbours after this.

At the moment the code is a bit messy but once the Shell has been fully developed, my aim will be to tidy it will commenting on what is happening throughout it.

## 11th of March

Naive Bayes is now processing but will need to implement normalization in order to get a more accurate score for certain datasets. This is to to rescale the data to any specific *x* value to be between *0 ≤ x ≥ 1*. The formula used for normalization is: 


Once this has been implemented it will make the training less sensitive to the scale of the feature columns. I'm going to see how normalization will have an impact on project. Once this has been done, I will then look into standardization. This is different as the values will be scaled from *0 - a standardized score*. This can be done by getting using the below formula:


I'm looking to give the user an option to whether they want their data standarized or normalized. Some users might even already have their data set up like this, so it would be a good idea to maybe have the option of not doing this also. Once both of been looked at I should be able to see what the best solution will be.

##7th of April 2019

Coming close to the deadline now! It's been a few weeks since my last blog post, took the foot of the pedal for a bit which was a mistake. Anyway, Over the past few weeks I've made progression on Web based site for the classifier kit. I haven't made as much progress as I had of hoped too as I'm only as far as taking in the different parameters for each of the classifiers.

//Insert picture of classifier settings page

I have basic connection between the backend and the frontend at the moment where it is taking in the uploaded csv file and is returning that the backend is receiving it. It at this point in time I'm hoping to get the reports printing by the end of the week but it will be a heavy workload to accomplish as I haven't touched the results page yet. Functionality is looking like an out of reach dream at the moment but if I persist I may be able to add more once I'm finished this MVP. As I still have a basic version for desktop I don't see that as being my MVP project unless I decide to drop the Web based version and focus on developing that. 

Over the next few days, I will be aiming to finish a basic web based platform with all classifiers running without any extra parameters. Then the additional factors will be included in with space between then and the deadline. I will be meeting with Mark this week to discuss the end game of the project and how to make the most of my last few weeks of work.

##23rd of April 2019 

Over the Easter break, I was focusing more on getting my study prepared for the upcoming exam season and to give my self a bit of breathing room to do some finishing up on my project. 

Over the next few days, I will be aiming to have the results showing for each of the classifiers selected. In order to do this I will have to be able to send the different configs plus csv file to the REST Api backend in order to run the chosen classifiers and getting an accuracy result back. Once I have results printing for each of these classifiers I will be looking at adding a bit more information to the overall results page to give a clearer presentation of these results.

*Extra Functionality:* I will look into adding in a helper popup to help guide some users through the program.

##3rd of May 2019

Big issue came up. I wasn't able to connect my backend to a my frontend. Due to this I've decided to change the structure and not use react for the front end and only use javascript, css and HTML. It has been a smooth transfer, however, I've become a bit undecisive on whether or not I am going to save the files locally or to a database. If I was to save it to a database I would be using SQLite as Flask has a supported library called Flask-SQLAlchemy which adds the basic support for SQLAlchemy. For the moment I've decided to progress with just saving it to a Folder. 

I've aimed to have the database implemented for Sunday. This should be easy enough as the setup is very basic. I don't see too many more errors arising between now and completing the assignment. My final MVP should be finished by this time next week. 

##19th of May 2019

Finally it has come to an end. The final implementation of the program works alot better than expected. Through the implementation of the database it opened my eyes to alot more future work for this project. What a journey this was from start to finish. Project DONE!