from tests.test_web import tests
import time
import json
import matplotlib.pyplot as plt
import pandas as pd
import plotly.express as px

class visualize():

    def gatherData():
        test = tests()
        setUp = test.setUp()
        startTimeDev = time.time()
        dev = test.test_developerButton()
        endTimeDev = time.time()
        finalTimeDev = endTimeDev - startTimeDev
        startTimeQa = time.time()
        qa = test.test_qaButton()
        endTimeQa = time.time()
        finalTimeQa = endTimeQa - startTimeQa
        startTimeMa = time.time()
        manage = test.test_managementButton()
        endTimeMa = time.time()
        finalTimeMa = endTimeMa - startTimeMa
        startTimeCon = time.time()
        con = test.test_contact()
        endTimeCon = time.time()
        finalTimeCon = endTimeCon - startTimeCon
        startTimePro = time.time()
        pro = test.test_products()
        endTimePro = time.time()
        finalTimePro = endTimePro - startTimePro

        timedata = {
            'developperTest' : [finalTimeDev],
            'qaButtonTest' : [finalTimeQa],
            'managementTest' : [finalTimeMa],
            'contactTest' : [finalTimeCon],
            'productTest' : [finalTimePro]
        }

        with open('time.json', 'w') as timeFile:
            json.dump(timedata, timeFile, indent=4)

        df = pd.read_json('time.json')
        print(df)

        fig = px.bar(data_frame=df)
        fig.show()

if __name__ == '__main__':
    visualize.gatherData()