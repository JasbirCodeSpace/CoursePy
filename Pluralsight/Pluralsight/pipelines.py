# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import sqlite3

class PluralsightPipeline:
    db_file = "pluralsight.db"
    db_table = "pluralsight"

    def __init__(self):
        self.create_connection()
        self.create_table()

    def create_connection(self):
        self.conn = sqlite3.connect(self.db_file)
        self.curr = self.conn.cursor()
    
    def create_table(self):
        self.curr.execute(""" DROP TABLE IF EXISTS %s """ % self.db_table)
        self.curr.execute(""" CREATE TABLE %s (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            category TEXT,
            author TEXT,
            difficulty TEXT,
            duration TEXT,
            link TEXT) """ % self.db_table)
        self.conn.commit()
    
    def insert_row(self, item):
        self.curr.execute(""" INSERT INTO %s (name,category,author,difficulty,duration,link)
        VALUES(?,?,?,?,?,?)""" % self.db_table, (
            item['name'],
            item['category'],
            item['author'],
            item['difficulty'],
            item['duration'],
            item['link']
        ))
        self.conn.commit()


    def process_item(self, item, spider):
        self.insert_row(item)
        return item
