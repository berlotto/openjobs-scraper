# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import rethinkdb as r
try:
    from settings import RDB_HOST, RDB_PORT, RDB_DATABASE
except:
    RDB_HOST = "localhost"
    RDB_PORT = 28015
    RDB_DATABASE = "vagascrawler"
table_name = "vagas"

r.connect(RDB_HOST, RDB_PORT).repl()
# Cria o banco de dados
r.db_create(RDB_DATABASE).run()
# Cria a tabela
r.db(RDB_DATABASE).table_create(table_name).run()
r.db(RDB_DATABASE).table(table_name).index_create("body").run()
r.db(RDB_DATABASE).table(table_name).index_create("datetime").run()
r.db(RDB_DATABASE).table(table_name).index_create("cidade").run()
r.db(RDB_DATABASE).table(table_name).index_create("categoria").run()
r.db(RDB_DATABASE).table(table_name).index_create("titulo").run()
