from flask import Flask,render_template,request

app = Flask(__name__)

# initial the publishList, publishList contains all the publish message
publishList = {}

# initial the subList for user1 and user2, will store the sub topic for user1 and user2
subList = {}
subList["user1"] = []
subList["user2"] = []

# create Mesaage class, have two elements : topic and message
class Message:
    def __init__(self,topic,message):
        self.topic = ""
        self.message = ""

# define the beginning of the html page
@app.route('/')
def Home():
    return render_template('index.html',user1=subList["user1"],user2=subList["user2"],publishList=publishList)

# define the html page that when user click the any submit button and information post
@app.route('/',methods=['POST'])
def getPostByOne():

    # if one of the submit button click and some information post
    if request.method == "POST":

    # USER 1:
        # if the button is submit for usr1 and message and the message textarea and topic selection is not empty
        # then add the topic and message into publishList and return the new html page with new information
        if request.form['submit'] == 'Submit':
            if request.form['topic']!="" and request.form['message']!="":
                topic = request.form['topic']
                message = request.form['message']
                if(topic in publishList):
                    publishList[topic].append(message)
                else:
                    publishList[topic] = [message]
                return render_template('index.html',user1=subList["user1"],user2=subList["user2"],publishList=publishList)
            else:
                return render_template('index.html',user1=subList["user1"],user2=subList["user2"],publishList=publishList)

        # if the button is Sub for user 1 ,then the topic of selection will add to the user1's subList and return
        # the new html page with new information
        elif request.form['submit'] == 'Sub':
            topic = request.form['subTopic']
            if(topic not in subList["user1"]):
                subList["user1"].append(topic)
            return render_template('index.html',user1=subList["user1"],user2=subList["user2"],publishList=publishList)

    # USER 2:
        # if the button is submit for usr2 and message and the message textarea and topic selection is not empty
        # then add the topic and message into publishList and return the new html page with new information

        elif request.form['submit'] == 'Submit2':
            if request.form['topic2']!="" and request.form['message2']!="":
                topic = request.form['topic2']
                message = request.form['message2']
                if(topic in publishList):
                    publishList[topic].append(message)
                else:
                    publishList[topic] = [message]
                return render_template('index.html',user1=subList["user1"],user2=subList["user2"],publishList=publishList)
            else:
                return render_template('index.html',user1=subList["user1"],user2=subList["user2"],publishList=publishList)
                
        # if the button is Sub for user 2 ,then the topic of selection will add to the user2's subList and return
        # the new html page with new information
        elif request.form['submit'] == 'Sub2':
            topic = request.form['subTopic2']
            if(topic not in subList["user2"]):
                subList["user2"].append(topic)
            return render_template('index.html',user1=subList["user1"],user2=subList["user2"],publishList=publishList)

if __name__ == "__main__":
    app.debug = True
    app.run(host='0.0.0.0')
