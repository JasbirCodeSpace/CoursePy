# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import sqlite3
import urllib.parse as urlparse

class UdemyCouponsPipeline:
	def __init__(self):
		self.create_connection()
		self.create_table()

	def create_connection(self):
		self.conn = sqlite3.connect("udemycoupons")
		self.cur = self.conn.cursor()

	def create_table(self):
		self.cur.execute("""drop table if exists udemy_coupons""")
		self.cur.execute("""create table udemy_coupons(
			name text PRIMARY KEY,
			tags text NOT NULL,
			link NOT NULL,
			code text)""")

	def close_connection(self):
		self.conn.close()

	def insert_db(self,item):
		self.cur.execute("""insert into udemy_coupons values(?,?,?,?)""",(
			item['name'],
			"&".join(item['tags']),
			item['link'],
			item['code']))
		self.conn.commit()

	def process_item(self, item, spider):
		self.insert_db(item)
		return item
