from Project import Project
from datetime import datetime
'''
for i in range(11):
    s = 
p[{0}].time = ""
p[{0}].important = 
p[{0}].timeend=
p[{0}].problem = ""
p[{0}].place = ""
p[{0}].title = ""
p[{0}].name = ""
p[{0}].bullet = []
p[{0}].tech = []
        .format(i)
    print(s)
word_should_use = ["Address","Lead","Conduct","Improve","Increase/Reduce","Develop","Design","Initiate"]

Learn,Participate,Assist,Observe,Work,Edit


'''
p = [Project() for i in range(11)]
p[0].time = "Sep 2017 – Dec 2017"
p[0].important = 1
p[0].timeend = datetime(2017, 12, 15)
p[0].problem = "2048 Game"
p[0].place = ""
p[0].title = "Course Project"
p[0].name = "AI 2048"
p[0].tech = ["Python", "TensorFlow", "Keras", "Machine Learning", "Deep Learning"]
p[0].bullet.append(
    "Built AI Solver to automatically play Game 2048 using Python and JavaScript, achieving successful rate with 98\%")
p[0].bullet.append(
    "Constructed deep reinforcement learning with three layers deep Q-Network to play 2048, using Keras and Tensorflow framework.")
p[0].bullet.append(
    "Implemented new heurist function in ExpectiMax algorithm to improve 5\% in success rate.")

p[1].time = ""
p[1].important = 3
p[1].timeend = datetime(2017, 12, 15)
p[1].problem = "Real-time Embedded System Kernel"
p[1].place = ""
p[1].title = "Course Project"
p[1].name = "Real-time Embedded System Kernel"
p[1].tech = ["C", "Embedded System", "Assembly",
             "Linux", "multi-thread", "Raspberry Pi"]
p[1].bullet.append(
    "Implemented rate-monotonic scheduling and real-time synchronization with  the priority ceiling protocol to accomplish a multi-thread real-time kernel.")
p[1].bullet.append(
    "Built Loadable Kernel Modules for PWM and Motor Encoder to use PID control algorithm to control motor velocity on embedded Linux.")

p[1].bullet.append(
    "Developed embedded peripheral device' I2C and UART drivers,enabling Raspberry Pi to detect clapper with sound sensor using C and Assembly.")


p[2].time = "Oct 2017 – Dec 2017"
p[2].important = 2
p[2].timeend = datetime(2017, 12, 1)
p[2].problem = "Knowing computer system"
p[2].place = ""
p[2].title = "Course Project"
p[2].name = "Introduction to Computer System Project"
p[2].tech = ["C", "Network", "HTTP", "Shell", "Linux"]
p[2].bullet.append(
    "Developed dynamic storage allocator in C using explicit, segregated lists and improved space utilization by reduce header in the allocator block.")
p[2].bullet.append("Designed a web proxy supporting HTTP/1.0 requests and implemented multi-thread to deal with multiple concurrent connections and added LRU cache to reduce the response time")
p[2].bullet.append(
    "Implemented a Linux shell to support signal handling, job control and I/O redirection")

p[3].time = "May 2017 – Jul 2017"
p[3].important = 1
p[3].timeend = datetime(2017, 7, 1)
p[3].problem = ""
p[3].place = ""
p[3].title = "Team Project"
p[3].name = "University Chatbot"
p[3].tech = ["Python", "SQL Server", "C#", "Web scrapy", "NLP", "QA"]
p[3].bullet.append(
    "Designed a chatbot to answer question related to my university via Microsoft Bot Framework in C\#.")
p[3].bullet.append(
    "Developed a Python web crawler to extract information from websites and utilized SQL sever to manage them.")
p[3].bullet.append(
    "Using natural language processing to analyse key words in the question and improved answers correctness, achieving top 32 out of 1000 in Beauty of Programming competition.")


p[4].time = "Apr - June 2016"
p[4].important = 3
p[4].timeend = datetime(2016, 6, 1)
p[4].problem = ""
p[4].place = ""
p[4].title = "Team member of three"
p[4].name = "Finding relationship of academic entities service "
p[4].tech = ["Java", "Tomcat", "json", "RESTful"]
p[4].bullet.append(
    "Designed a RESTful service endpoint to find relationship between different academic entities in Microsoft Academic Graph.")
p[4].bullet.append(
    "Deployed a Java Tomcat web server on the Azure and extracted information JSON array received from Academic Knowledge API.")

p[5].time = "Jan - Jun 2017"
p[5].important = 2
p[5].timeend = datetime(2017, 8, 1)
p[5].problem = ""
p[5].place = ""
p[5].title = "Course Project"
p[5].name = "Personal Time Management Software"
p[5].tech = ["Python", "Google API",
             "Data visualization", "Panads", "SQLite", "OOP"]
p[5].bullet.append(
    "Designed a Python software to combine To-Do list and Calendar using Object Oriented Programming, supporting Google Calendar synchronization.")
p[5].bullet.append(
    "Developed weekly summary website to visualize time utilization with Pandas, SQLite, Bokeh.")

p[6].time = "May 2015 - May 2016"
p[6].important = 3
p[6].timeend = datetime(2016, 6, 1)
p[6].problem = ""
p[6].place = ""
p[6].title = "Group leader of  five"
p[6].name = "Android application to detect and train attention based on EEG signal"
p[6].tech = ["Android", "R"]


p[7].time = ""
p[7].important = 1
p[7].timeend = 1
p[7].problem = ""
p[7].place = ""
p[7].title = ""
p[7].name = "Stock"
p[7].tech = []


p[8].time = ""
p[8].important = 1
p[8].timeend = 1
p[8].problem = ""
p[8].place = ""
p[8].title = ""
p[8].name = "Intel"
p[8].tech = []


p[9].time = "March - May 2016"
p[9].important = 1
p[9].timeend = 1
p[9].problem = ""
p[9].place = ""
p[9].title = ""
p[9].name = "A Central Processing Unit (CPU) Basing On Verilog HDL"
p[9].tech = ["Verilog", "FPGA"]
p[9].bullet.append(
    "Designed and simulated CPU micro-operation with eight basic modules in Verilog.")
p[9].bullet.append(
    "Implemented 15 operation instructions, supporting basic calculator function and received the highest score in the class.")
