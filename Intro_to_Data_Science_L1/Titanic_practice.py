import numpy
from pandas import DataFrame, Series
import pandas

def simple_heuristic(file_path, rule):
    '''
    In this exercise, we will perform some rudimentary practices similar to those of
    an actual data scientist.
    
    Part of a data scientist's job is to use her or his intuition and insight to
    write algorithms and heuristics. A data scientist also creates mathematical models 
    to make predictions based on some attributes from the data that they are examining.

    We would like for you to take your knowledge and intuition about the Titanic
    and its passengers' attributes to predict whether or not the passengers survived
    or perished. You can read more about the Titanic and specifics about this dataset at:
    http://en.wikipedia.org/wiki/RMS_Titanic
    http://www.kaggle.com/c/titanic-gettingStarted
        
    In this exercise and the following ones, you are given a list of Titantic passengers
    and their associated information. More information about the data can be seen at the 
    link below:
    http://www.kaggle.com/c/titanic-gettingStarted/data. 

    For this exercise, you need to write a simple heuristic that will use
    the passengers' gender to predict if that person survived the Titanic disaster.
    
    You prediction should be 78% accurate or higher.
        
    Here's a simple heuristic to start off:
        1) If the passenger is female, your heuristic should assume that the
        passenger survived.
        2) If the passenger is male, you heuristic should
        assume that the passenger did not survive.
       
    Here's a more complex algorithm, predict the passenger survived if:
        1) If the passenger is female or
        2) If his/her socioeconomic status is high AND if the passenger is under 18
    
    Then let's try some customized heuristics:
    Passengers would survive if:
        1) If the passenger is female and in high socioeconomic status and has at most 5 (sum of) sibsp & Parch
        2) If the passenger is female and in low/mid socioeconomic status
        3) If his/her socioeconomic status is high AND if the passenger is under 18
    
    You can access the gender of a passenger via passenger['Sex'].
    If the passenger is male, passenger['Sex'] will return a string "male".
    If the passenger is female, passenger['Sex'] will return a string "female".
    Otherwise, your algorithm should predict that the passenger perished in the disaster.

    Write your prediction back into the "predictions" dictionary. The
    key of the dictionary should be the passenger's id (which can be accessed
    via passenger["PassengerId"]) and the associated value should be 1 if the
    passenger survied or 0 otherwise.

    For example, if a passenger is predicted to have survived:
    passenger_id = passenger['PassengerId']
    predictions[passenger_id] = 1

    And if a passenger is predicted to have perished in the disaster:
    passenger_id = passenger['PassengerId']
    predictions[passenger_id] = 0
    
    You can also look at the Titantic data that you will be working with
    at the link below:
    https://www.dropbox.com/s/r5f9aos8p9ri9sa/titanic_data.csv
    '''

    predictions = {}
    df = pandas.read_csv(file_path)
    #print df
    for passenger_index, passenger in df.iterrows():
        passenger_id = passenger['PassengerId']
        
        #why we need passenger_index: to iterate among the df.iterrows.
        #an alternative:
        #for passenger in df.iterrows():
        #    passenger_id = passenger[1]['PassengerId']; #here [1] means the row axis. [0] for column axis
        
        # Your code here:
        # For example, let's assume that if the passenger
        # is a male, then the passenger survived.
        #     if passenger['Sex'] == 'male':
        #         predictions[passenger_id] = 1
        
        #-------------------------------------------
        #prediction heuristics:
        if (rule == 'simple'):
            if (passenger['Sex'] == 'male'):
                predictions[passenger_id] = 0;
            else:
                predictions[passenger_id] = 1;
            
        elif (rule == 'slight_complex'):
            if ((passenger['Sex'] == 'female') or ((passenger['Pclass']) == 1 and passenger['Age'] < 18)):
                predictions[passenger_id] = 1;
            else:
                predictions[passenger_id] = 0;
        elif (rule == 'custom'):
            if (passenger['Sex']=='female' and passenger['Pclass']==3):
                if (passenger['SibSp']+passenger['Parch']<=4):
                    predictions[passenger_id] = 1;
                else:
                    predictions[passenger_id] = 0;
            elif (passenger['Sex']=='female' and passenger['Pclass']!=3):
                predictions[passenger_id] = 1;
            elif (passenger['Pclass'] == 1 and passenger['Age'] < 18):
                predictions[passenger_id] = 1;
            else:
                predictions[passenger_id] = 0;
        #-------------------------------------------
        
    
    return predictions

def calculate_correctness(test_path,prediction):
    
    correct_count = 0;
    df_test = pandas.read_csv(test_path)
    #compare the predictions with the 'Survived' column to see the prediction result;
    for passenger in df_test.iterrows():
        passenger_id = passenger[1]['PassengerId'];
        if (prediction[passenger_id]==passenger[1]['Survived']):
            correct_count=correct_count+1;
    
    correctness = float(correct_count)/float(len(df_test['PassengerId']));
    print len(df_test['PassengerId']),correctness;
    
    return correctness;

if __name__ == '__main__':
    file_path_train = r"E:\Programming\Eclipse\Workspace\Kaggle_Titanic\data\train.csv";
    file_path_test = r"E:\Programming\Eclipse\Workspace\Kaggle_Titanic\data\test.csv";
    
    #training heuristic rule type:
    #'simple' for the simplest rule set (1st rule in Intro to Data Science)
    #'slight_comple' for the 2nd rule in Intro to Data Science
    rule_type = 'slight_complex';
    
    #make prediction
    prediction_result=simple_heuristic(file_path_train, rule_type);
    
    #calculate the correctness of the prediction:
    correctness = calculate_correctness(file_path_train, prediction_result);
    
    print ("correctness is: %r%%" %(correctness*100));
