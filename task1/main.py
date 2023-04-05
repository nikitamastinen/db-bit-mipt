import json

from bson import json_util
from pymongo import MongoClient, ASCENDING
import csv


def read_data():
    with open('data/titanic.csv', 'r') as data:
        result = []
        for i in csv.DictReader(data):
            result.append(i)
        return result


class Homework:
    def __init__(self):
        client: MongoClient = MongoClient('0.0.0.0', 27017)
        self.instance_ = client['task1']
        self.instance_.people.delete_many({})
        print(self.instance_)

    def load_dataset(self):
        self.instance_.people.insert_many(read_data())

    def create_queries(self):
        self.instance_.people.insert_one(
            {
                'Survived': '0',
                'Pclass': '3',
                'Name': 'Miss. Bur',
                'Sex': 'female',
                'Age': '48',
                'Siblings/Spouses Aboard': '0',
                'Parents/Children Aboard': '1',
                'Fare': '17'
            })
        self.instance_.people.insert_one([
            {
                'Survived': '0',
                'Pclass': '1',
                'Name': 'Miss. Bur',
                'Sex': 'female',
                'Age': '47',
                'Siblings/Spouses Aboard': '0',
                'Parents/Children Aboard': '5',
                'Fare': '1.7'
            },
            {
                'Survived': '1',
                'Pclass': '3',
                'Name': 'Miss. Bur',
                'Sex': 'female',
                'Age': '100',
                'Siblings/Spouses Aboard': '0',
                'Parents/Children Aboard': '1',
                'Fare': '1'
            }
        ])

    def find_queries(self):
        r = self.instance_.people.find_one({'Survived': '0'})
        print(r)

        r = self.instance_.people.find({'Age': {'$eq': '22'}})
        print(json.dumps(json.loads(json_util.dumps(r)), indent=2))

    def update_queries(self):
        self.instance_.people.update_one({'name': 'Mr. Owen Harris Braund'}, {'$set': {'Age': '105'}})

    def delete_queries(self):
        self.instance_.people.delete_one({'name': 'Mr. Anders Johan Andersson'})

    def index_performance_queries(self):
        no_index_stats = self.instance_.people.find({'Age': {'$gt': '24'}}).explain()
        print(no_index_stats)

        self.instance_.people.create_index([('Age', ASCENDING)])

        no_index_stats = self.instance_.people.find({'Age': {'$gt': '24'}}).explain()
        print(no_index_stats)

        # executionTimeMillisEstimate': 3 after vs executionTimeMillisEstimate': 0 before

def main():
    homework = Homework()
    homework.load_dataset()
    homework.find_queries()
    homework.update_queries()
    homework.index_performance_queries()


if __name__ == '__main__':
    main()
