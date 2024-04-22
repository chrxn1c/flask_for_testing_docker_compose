import redis
import psycopg2


redis_host = 'redis'
redis_port = 6379
redis_db = 0
redis_client = redis.StrictRedis(host=redis_host, port=redis_port, db=redis_db)


pg_host = 'db'
pg_port = 5432
pg_db = 'my_db'
pg_user = 'app_user'
pg_password = 'password'
conn = psycopg2.connect(host=pg_host, port=pg_port,
database=pg_db, user=pg_user, password=pg_password)
cursor = conn.cursor()


redis_key = 'example_key'
redis_value = 'example_value'
redis_client.set(redis_key, redis_value)


value_from_redis = redis_client.get(redis_key)
print(f'Data from Redis: {value_from_redis.decode()}')


create_table_query = '''
CREATE TABLE IF NOT EXISTS example_table (
    id SERIAL PRIMARY KEY,
    data TEXT
);
'''
cursor.execute(create_table_query)

create_table_query = '''
    INSERT INTO example_table VALUES (
    1,
    'text'
);
'''