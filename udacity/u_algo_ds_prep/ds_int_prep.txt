udacity  data science interview
hours: 1 1 2 2 2 2 2 2 2  = 16
expected = 32
//////////////////////////////////////////////////////
//  check naive bayes  ML algo
//  design a plagiarism detection system : cosine similarity tf-idf method
//
//
//////////////////////////////////////////////////////


lesson 1 Intro

4 types of DS 

* the data analyst  (basics)
* the data engineer (good with software, build pipes, data platform)
* the machine learning engineer ( in companies where data is their product,) mach learning is intense,  programming is intense 
* the data science generalist  ( for many companies )  company which cares about their data but is not a data company. (do analysis touch production code, visuzalize data, etc) Exp. with messy, real-life datasets. 

Do be confident.  Show you are a problem solver 


lesson 2 data analysis interbiew practice 

    quiz describe your latest data project
        prepare a SOAR on your latest DS project(s)
            business question about project goals
            dataset questions
                how many features had, how bit is dataset
            type of methods used
                which models used
                did you have problems with overfitting

    interviewer checks
        how the problem is exposed and explained.
             separate biz questions, from tech data, from model consideration


    !NB quiz probabilities 
        !NB proba problems are important  in interviews. 

    !NB quiz SQL  question, easy, no joins   select top(3) * from .. where crit1>val order by crit 2 desc

    !NB guiz general programming  show i,j for biggest elemenet difference in array
         general programming questions always come up.
    def find_max_dist(x):
    #check for args (i.e.  empty array)
    max_i = 0
    max_j = 1
    max = x[1] - x[0]
    for j in range(len(x)):
        for i in range(j):
            if  x[j] - x[i] > max:
                max = x[j] - x[i]
                max_j = j
                max_i = i
    return (max_j, max_i)           
            
    O(N^2)

    do a func test graphically 
    i.e.
    x = [4,3,2,1]

    max = -1
  
   unoptimized solution to the problems are OK in a DS interview but invest in algos

   !NB quiz  design an email spam classification  solution. Q: which features to use:
        
        email fields:
        sender addresses, ip address, subject lie, time-date body, attachments recipients, RE/FW

            in subject and body, have text. 
            is sender  (known/unknown to address-book,  is in spam list), if addresses (spamlist)
            white list of known addresses, 
            within unknowns addresses spoofing  (from=text1, in raw email from=text2)
            known email provider 

            ip address (in spam list of ip addresses, map to a country : my countries vs other countries, prevalence of spammers in that country (! also avoid bias) )

            this is a binary classification problem
                for large data set problem  one approach is naive Bayes ( a very simple algo)
                mb support vector machines
                    pros non-linear kernels
                    cons  slower to train on datasets (take a lot of memory, but fast on predict)
                    in this problem retraining is frequent
                standard logistic regression  would do the job (probability of spam 0<p<1 )

         reviewer asks machine learning questions as they are big part of DS (i.e. design a system)
            checks if a candidate can come up  with good features for the problem presented (data acumen)
            reviewer tests about ML algos pros/cons to test a knowledge of an ML algo       
            ! do not mention algorithm you are not familiar about it. otherwise next questions will
            follow. the algo portion of the machine learning question is usually a test

            if you used the algo in you project you should be really familiar with how the algo works.

    general review:  Charlee was a great interviewee
          she could have worked more:  be more familiar with a machine learning algorithms!
          be more slower in visual testing of a coding question


    lesson 3 machine learning engineer  interview overview
        cs fundamentals

        
        design plagiarism detection

        data modeling
        applying ML algos and libs
        software engineering aand system design

        quizes 
            1. proba: bayes rule problem . OK

            2. design a plagiarism detection system
                analyze similarity between 2 sets of documents
                    => NB! use cosine similarity, tf-idf method on all docs in order
                        to vectorize each of documents .  high similarity = plagiarism
                        tf-idf count # of words and generate frequency of each word,
                        higher frequencies = higher cosine similarity
                        each el in vector is a frequency of a particular word
                        further: n-grams = series of words which appear multiple times
                        check frequencies of same n-grams
                        further: nlp processing -> find very similar sentence structure

                review: plagiarism is unsupervized learning,  mentioned specialized text analysis techniques

            3. image categorization    
                image 1920 x 1080  RGB  channels  1 M images
                classify: cat, dog, human, none
                how to speed up the ML algo?   
                    NB!  perform a transform on data before feed. e.g. fourier transform to
                    which looks at freqs of color patterns -> reducing dimensionality of data
                    having a smaller feature space without loosing too much of info.
                    impact on model performance?  pix by pix -> patterns (loss of info happening)
                    other ways to improve peroformance? 
                        hardware implement multi-threaded parallel processing 
                    q? where FFT can not be applied.  FFT works well on audio and video, capturing wavelenghts and transfer into frequencies. 
                    for survey FFT is not good as this data is not expressed in wavelengths. 

                review:   image classification is classic ML task.   lorenzo came with FFT, other is PCA. lorenzo said FFT can be used in audio, video domains

            4. describe your ML project. (this is an open ended project)
                can you describe your email project?   i work on music acompannement app. 
                training:  took a son, added noise. then choped to make prediction on a short piece . did FFT, peak analysis
                what ML alo you used? tried several:   RandomForests accu good but slow,  used SVM less accu, but preds are fast. 

                => do projects that interest you. this shows in the interview how passionaate your are about the machine learning. 
 
            5.  explain how SVM works 
                    what is a parameter function that SVM tries to optimize (minimize or maximize) ?
                     a: draw a boundary bands where a number of misclassifications should be minimized
                     distance between a border and each class should be about the same i.e.  a border is equally distant from both classes
                     Points near boundary are called support vectors?
                        what are domains where SVM is useful? 
                            when is data is well clustred i.e. boundaries are clear. 
                        tweak an SVM kernel from linear to radial

                review: SVMs are widely used for classification tasks.  The param tries to optimize the
                separation between two classes . when classes are intermingled  change kernel.

        gen review:
            liked that candidate takes an explanatory approach. every piece of info is written on the board. this is helpful as an interviewer feels connected. interviee can ask questions, i.e. he might be a good team player.
            Squeeze info  on a project you worked on. Helps to impresss people, how passionate you are about ML.



    lesson 13  interview fails 
             Mile Wales:  tic-tac-toe function . concentrate on a a func which does mvp


             Siya Raj Purohit
                unqualified for a tech screening interview. do not stresss about bad interview

            Lyla Fujiwara
                tech intervies are stressfuls, can last several hours. I wasnt supposed to be in interview.   i.e. be motivated when you apply to be in the context of the company.
                apply to the job you really want to do. 
                

