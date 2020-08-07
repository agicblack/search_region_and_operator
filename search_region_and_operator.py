import pandas as pd


class search_region_and_operator():
    def __init__(self):
        self.ros_sviaz = self.get_rossviaz()

    def get_rossviaz(self):
        ros_sviaz = pd.read_csv('https://rossvyaz.gov.ru/data/DEF-9xx.csv', dtype={'АВС/ DEF': str, 'От': str,
                                                                                   'До': str}, sep=';')
        ros_sviaz['От'] = '7' + ros_sviaz['АВС/ DEF'] + ros_sviaz['От']
        ros_sviaz['До'] = '7' + ros_sviaz['АВС/ DEF'] + ros_sviaz['До']
        ros_sviaz = ros_sviaz.astype({'От': 'int64', 'До': 'int64'})
        return ros_sviaz

    def search_region_and_operator(self, num):
        region = None
        operator = None
        try:
            num = int(num)
            tmp = self.ros_sviaz[(self.ros_sviaz['От'] < num) & (self.ros_sviaz['До'] > num)]
            if len(tmp) > 0:
                region = list(tmp['Регион'])[0]
                operator = list(tmp['Оператор'])[0]
        except:
            pass
        return operator, region
search_numb = search_region_and_operator()
#print(search_numb.search_region_and_operator(79119279008))