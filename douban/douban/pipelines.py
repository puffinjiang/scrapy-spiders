# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import psycopg2

from douban.settings import DB_HOST, DB_NAME, DB_PASSWORD, DB_PORT, DB_USER

# class DoubanPipeline:
#     def process_item(self, item, spider):
#         return item


class PostgresqlPipeline:
    def __init__(self):
        self.conn = psycopg2.connect(
            dbname=DB_NAME, user=DB_USER, password=DB_PASSWORD, host=DB_HOST, port=DB_PORT)
        self.cur = self.conn.cursor()

        sql = """
        CREATE TABLE IF NOT EXISTS douban_popular_books(
            id serial PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            author VARCHAR(255),
            title VARCHAR,
            cover VARCHAR,
            create_at TIMESTAMP NOT NULL DEFAULT NOW(),
            update_at TIMESTAMP NOT NULL DEFAULT NOW()
            )
        """
        self.cur.execute(sql)

    def process_item(self, item, spider):
        print("item is: {}", item)
        self.cur.execute("""insert into douban_popular_books (name, author,cover, title) values (%s,%s,%s, %s)""",
                         (item["name"], item["author"], item["cover"], item["title"]))
        self.conn.commit()

    def close_spider(self, spider):
        self.cur.close()
        self.conn.close()
