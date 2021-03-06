---
layout: post
permalink: /outline/
title: outline
titleheader: Course Outline
nav: true
toc: true
toc_label: "Contents"
toc_icon: "list-ol"
toc_sticky: true
description: Course information, topics, schedule and policies.
showtitle: true
date: 2021-07-05
---

# Course ECE657A  - DKMA - Data and Knowledge Modelling and Analysis


| **Offered:** Spring 2021                                     | **Instructor:** Prof. Mark Crowley                                        |
| :----------------------------------------------------------: | :----------------------------------------------------------:              |
| [Website]( https://compthinking.github.io/DKMA/)             | [Bookable Meetings](https://doodle.com/mm/markcrowley/bookable-1on1-657a) |
| [Piazza](https://piazza.com/uwaterloo.ca/summer2021/ece657a) | [YouTube](https://www.youtube.com/channel/UC7vU2kP8oNwvr0GuAqoxYGA)       |
| [Weekly Calendar](/DKMA/calendar/)                           |                                                                           |

### Course Description

Engineers encounter data in many of their tasks, whether the sources of this data may be from experiments, databases, computer files or the Internet.  There is a dire need for effective methods to model and analyze the data and extract useful knowledge from it and to know how to act on it. In this course you will learn the fundamental tools for assessing, preparing and analyzing data. You will learn to design a data and analysis pipeline to move from raw data to task solution. You will learn to implement a variety of analytical and machine learning algorithms to including supervised, unsupervised and other learning approaches. Students will gain practical experience with coding and analysis through assignments. Research students will have opportunity to connect course material to their research as a project instead of some of the assignments. 

### Recommended background:

- *Data Structures and Algorithms, Basic Programming Skills (Python especially) and Basic Knowledge of Probability and Statistics Theory*

## Course Staff

| **Instructor:** Prof. Mark Crowley                           | TA: Milad Sikaroudi                        | Fatemeh Tavakoli                           |
| ------------------------------------------------------------ | ------------------------------------------ | ------------------------------------------ |
| **Contact: **mcrowley@uwaterloo.ca (but for better results, use piazza or book a meeting)) | **Contact:** msikaroudi@uwaterloo.ca       | **Contact:** fatemeh.tavakoli@uwaterloo.ca |
| **Office Hour:** [Bookable Meetings](https://doodle.com/mm/markcrowley/bookable-1on1-657a) | **Office Hour:** Wednesday<br />at 8:00 am |                                            |

## Learning Outcomes

The [Course Design and Learning Outcomes](/DKMA/outcomes) describe the design philosophy of this course which guide the topics and assessments below.

## Major Topics:

These topics are an outline, and each year some subset of non-core topics will be skipped due to time constraints and in order to benefit students through deeper focus. When tests are planned to assess knowledge of the material the mandatory core topics will be highlighted to students so they know which will be tested. **(s)** indicates self-study, pre-recorded video content.

1. Understanding and Preparing Data
   1. Data types, sources, nature, scales, representations and distributions
   2. Preparation of Data: missing data, smoothing, transformation and normalization
   3. Summarizing Data: mean, variance, skew, PCC, cross correlation
   4. (s) Comparison Measures between datasets
   5. (s) Experimental Methodology, statistical tests and validation metrics
2. Fundamentals of Estimation and Learning
   1. (s) Background  Review of Probability and Statistics: Random Variables, Conditional Probability, Bayes Rule, Entropy, KL-Divergence, Hypothesis Testing
   2. Parameter Estimation, statistical approaches, MLE, MAP, EM, density estimation
   3. Classification Preview: Naive Bayes Algorithm
3. Classification I :
   1. Distance based - k-Nearest Neighbours (kNN) Algorithm
   2. Decision Tree based, Ensemble Methods including Random Forests, XG-Boost, Mondrian Forests
4. Representation Learning I
   1. (s) Feature extraction : PCA, LDA, ISOMAP, LLE
   2. (s) Dimensionality Reduction and Manifold Learning
   3. `(topic dropped)` *Vector Embeddings : TF-IDF, Word2Vec, BERT*
5. Classification II : 
   1. Support Vector Machines (SVM)
   2. Kernel Methods and Latent Models
6. Semi-/Self-/Unsuprevised Learning
   1. Clustering: Partition, Hierarchical, Model and Density based.
   2. (s) Clustering evaluation measures
   3. k-Means Algorithm, DBScan Algorithm
   4. Anomaly Detection: Classification, Outlier, Density, and Isolation based
7. Deep Learning
   1. Fundamentals of Neural Networks
   3. Types of Deep Learning : CNN, RNN
   4. Classification III : Data, Image and Timeseries classification using Deep Learning
   2. Effective Deep Learning Training Methods: Attention, Regularization, Optimizers
   5. Reusing Information: Resnet, Inception
   6. Representation Learning II: Autoencoders and Variational Autoencoders
8. Additional Learning Topics (if time allows)
   1. **Transfer Learning** (likely)
   2. *Active Learning*
   3. *Incremental/Online Learning*
   4. *Reinforcement Learning* (unlikely)



## Timing of Assessments, Lectures and Interaction

- **Assessments:** No more than one Test or Assignment will be due on any given week.
- *Pre-Recorded Content:* Some weeks there will be pre-recorded lecture content available, the total content (live-recorded, or pre-recorded self-study) per week will be maintained around the same level, around 3-4 hours of content per week.
    - See [DKMA youtube channel](https://www.youtube.com/channel/UC7vU2kP8oNwvr0GuAqoxYGA)
- **Weekly Live Sessions:** There will be 2-3 hrs of weekly live sessions from course staff (instructor and/or TAs) which will include
  - Live lecture reviews (hosted and recorded on "Bongo" within LEARN) reviewing or going deeper into core, high level topics
  - Recordings of these will be avilable on LEARN via the `Content/Virtual Classroom` link and in each week's content 
  - Help sessions (unrecorded) to discuss content, answer questions and build class community

#### Planned Weekly Schedule:
- ***Class Lecture/Discussion -*** **Mondays 11:30 am- 12:50 pm** - The *weekly lecture* slot on Mondays will be used for discussion of the self-study material from the previous week, additional questions and exercises and general discussion.
- ***Bookable 1-on-1 Meetings -***  **Thursdays 11:30am - 1:00pm** 
  - These are regular, one-on-one (or a small group) meeting slots with the professor, [bookable via doodle](https://doodle.com/mm/markcrowley/bookable-1on1-657a) a few days ahead of time.
  - [Doodle Bookable Calendar](https://doodle.com/mm/markcrowley/bookable-1on1-657a)
- **TA office hours** - to be determined (some times on Tuesday-Thursdays)

## Assessment:

The goal of this course is to help students learn how to **analyse and prepare** data, **describe and apply** theoretical concepts in Data Science and Machine Learning, **design** data processing pipelines and **implement** important machine learning algorithms on a range of datasets and tasks. This course will be a success if students can use these skills in their future endeavours, research and employment. To assess this, students will complete assignments that require all of these skills on real datasets and they will also complete small tests focussing on the theoretical and design aspects of these skills.

### Weighting of Assessments

- **65% Assignments** (three or four assignments, done in pairs or alone):
  - Assignments will arise from the major component topics of the course, some will buid on previous assignment outcomes.
  - Possibility to have later assignments as Kaggle-style competitive submissions (note: vast majority of grade will be based on performance and correcteness rather than based on competitive performance)
  - Assignments will involve multiple skills:
    - mathematical analysis of data and results
    - logical design and clear description of a expeirmental methodology
    - programming various algorithms for processing, training and analysis of data to achieve given tasks (Programming will be in Python using libraries such as sci-kit learn and tensor flow)
  - Late Assignments: 
    - Assignment due dates will be at midnight on the designated date.
    - Late assignments will have the following penalties from the assigned grade: 
      - 6 hours (0%)
      - 6-24 hours (5%)
      - 24-48 hours (10%)
      - \>48 hours (100%)
    - If you know *ahead of time* that you will not be able to make the deadline do to *serious* health or personal issues contact the professor to ask for an exception.
- **35% Tests**  
    - Three tests on different parts of the course.
    - These will be done alone and time-limited. 
    - We will use online timed question banks and take-home files submitted to Crowdmark.
    - For each test, questions will be on content up to that point on concepts, theory and design.
      - **Test Weighting**: Test 1 (10%), Test 2 (10%), Test 3 (15%)
    
    

## Getting Help:

- **Discussion board:** 
  - *Piazza* will be the main place for detailed discussion and questions. Students can post anonymously (from students only), post a collaborative answer and course staff can confirm these, post their own or run Live Q&A events.
  - Go there there and sign up with your UWaterloo email now!
- **Pre-recorded Video Lectures:** These will be made available on the [course youtube channel](https://www.youtube.com/channel/UC7vU2kP8oNwvr0GuAqoxYGA), and links from whithin Learn
- **LEARN Website:** The main course content, announcements, grade stracking and materials will be made availble on Learn. All registered students should see this in their LEARN courses.
- **Email the Teaching Assistant and Instructor:** Office Hours will be arranged once term starts as needed.
- **AccessAbility Services :** http://uwaterloo.ca/accessability-services 
  - If you need any accommodation, assistance with exams, learning environment, assignments, talk to this office and they can help you set it up as securely and anonymously as possible.

### Discussion Group Protocols

- Posts on Piazza can be public or anonymous to your classmates, but they will *never* be anonymous to the TAs and Instructor. 
- Be kind. Assume the best, not the worst. Think before you hit enter.
- Posts which are considered offensive, abusive, bullying, discriminatory to any group or person, will be made private or deleted and followed up with private discussion.
- If you feel there is inappropriate, hurtful behaviour occurring on the discussion forum, please notify the professor, TAs or department staff as you feel appropriate. 
- If you really can't get in touch with anyone and it is an emergency you can contact Prof. Crowley directory via Microsoft Teams messaging (please don't abuse this though :- )

## Resources:
There is no required textbook. But most of the course is based on the following books and will be useful to take a look at them.

1. Arxiv Tutorials - links will be provided to a number of detailed tutorials on some course topics.
1. K. Murphy. “Machine Learning: A Probabilistic Perspective”. MIT Press, 2012.
1. I. Goodfellow, Y. Bengio and A. Courville. “Deep Learning”. MIT Press, 2016.
	- Online for free at [http://www.deeplearningbook.org*](http://www.deeplearningbook.org). The first half covers many of     basics of this course, while the second half focusses on Deep Learning only.
1. R. O. Duda, P. E. Hart and D. G. Stork. Pattern Classification (2nd ed.), John Wiley and Sons, 2001.

Papers and electronic references will be made available on the course website which is on LEARN (go to http://learn.uwaterloo.ca to log in).

## Recipe for success: 

Ask questions.  Connect with your classmates. Do the assignments. ***Ask questions.*** 
Most of all, *have fun*.

## Wellness Support and Contact Information.

University can be a challenging environment and it is normal to need support from time-to-time. Campus Wellness services are available to students through counselling and health services. If you are struggling or need someone to talk to you, please reach out. 

To book an appointment or learn more about the services, call 519-888-4567 x 32655 or explore [www.uwaterloo.ca/campus-wellness](http://www.uwaterloo.ca/campus-wellness). 

If you're experiencing a crisis and feel unable to cope and Campus Wellness is closed, contact any of these after-hours supports: EmpowerMe (1-833-628-5589), Good2Talk (1-866-925-5454) or Here 24/7 (1-844-437-3247). They are available at any time of the day or night to help.

## Policy and Rules

### Fair Contingencies for Emergency Remote Teaching

We are facing unusual and challenging times. To provide contingency for unforeseen circumstances, the instructor reserves the right to *modify* course topics and/or assessments and/or weight and/or deadlines *with due notice to students*. In the event of further challenges, the instructor will work with the Department/Faculty to find reasonable and fair solutions that respect rights and workloads of students, staff, and faculty.

### Online Academic Integrity

In order to maintain a culture of academic integrity, members of the University of Waterloo community are expected to promote honesty, trust, fairness, respect and responsibility. [Check www.uwaterloo.ca/academicintegrity/ for more information.]

All students are expected to work individually, or in pairs as described for assignments, and submit their own original work. Under Policy 71, the instructor may have follow-up conversations with individual students to ensure that the work submitted was completed on their own. Any follow up will be conducted remotely (e.g., MS Teams, Skype, phone), as the University of Waterloo has suspended all in-person meetings until further notice.

### Grievance:

A student who believes that a decision affecting some aspect of his/her university life has been unfair or unreasonable may have grounds for initiating a grievance. Read Policy 70, Student Petitions and Grievances, Section 4, http://www.adm.uwaterloo.ca/infosec/Policies/policy70.htm. When in doubt please be certain to contact the department's administrative assistant who will provide further assistance. 


### Discipline:

A student is expected to know what constitutes academic integrity to avoid committing academic offenses and to take responsibility for his/her actions. A student who is unsure whether an action constitutes an offense, or who needs help in learning how to avoid offenses (e.g., plagiarism, cheating) or about "rules" for group work/collaboration should seek guidance from the course professor, academic advisor, or the undergraduate associate dean. For information on categories of offenses and types of penalties, students should refer to Policy 71, Student Discipline, http://www.adm.uwaterloo.ca/infosec/Policies/policy71.htm. For typical penalties check Guidelines for the Assessment of Penalties, http://www.adm.uwaterloo.ca/infosec/guidelines/penaltyguidelines.htm.

Plagiarism-detection software may be used on any submitted work.

### Appeals:

A decision made or penalty imposed under Policy 70, Student Petitions and Grievances (other than a petition) or Policy 71, Student Discipline may be appealed if there is a ground. A student who believes he/she has a ground for an appeal should refer to Policy 72, Student Appeals, http://www.adm.uwaterloo.ca/infosec/Policies/policy72.htm.

### Note for students with disabilities:

The Office for Persons with Disabilities (OPD), located in Needles Hall, Room 1132, collaborates with all academic departments to arrange appropriate accommodations for students with disabilities without compromising the academic integrity of the curriculum. If you require academic accommodations to lessen the impact of your disability, please register with the OPD at the beginning of each academic term.

