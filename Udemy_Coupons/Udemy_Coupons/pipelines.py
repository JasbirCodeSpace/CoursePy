# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import sqlite3
import urllib.parse as urlparse

class UdemyCouponsPipeline:
	dbFile = 'udemycoupons'
	dbTable = 'udemy_coupons'
	def __init__(self):
		self.create_connection()
		self.create_table()

	def create_connection(self):
		self.conn = sqlite3.connect(self.dbFile)
		self.cur = self.conn.cursor()

	def create_table(self):
		self.cur.execute("""DROP TABLE IF EXISTS %s """ % self.dbTable)
		self.cur.execute("""CREATE TABLE %s (
			site text,
			name text PRIMARY KEY,
			tags text,
			link text,
			code text)""" % self.dbTable)
		self.conn.commit()

	def insert_db(self,item):
		self.cur.execute("""INSERT INTO %s VALUES(?,?,?,?,?)""" % self.dbTable,(
			item['site'],
			item['name'],
			"&".join(item['tags']),
			item['link'],
			item['code']))
		self.conn.commit()

	def process_item(self, item, spider):
		self.insert_db(item)
		return item
