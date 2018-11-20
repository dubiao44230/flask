import pymysql
from DBUtils.PooledDB import PooledDB
POOL = PooledDB(
    creator=pymysql,  # 使用链接数据库的模块
    maxconnections=6,  # 连接池允许的最大连接数，0和None表示不限制连接数
    mincached=2,  # 初始化时，链接池中至少创建的空闲的链接，0表示不创建
    maxcached=5,  # 链接池中最多闲置的链接，0和None不限制
    maxshared=3,  # 链接池中最多共享的链接数量，0和None表示全部共享。PS: 无用，因为pymysql和MySQLdb等模块的 threadsafety都为1，所有值无论设置为多少，_maxcached永远为0，所以永远是所有链接都共享。
    blocking=True,  # 连接池中如果没有可用连接后，是否阻塞等待。True，等待；False，不等待然后报错
    maxusage=None,  # 一个链接最多被重复使用的次数，None表示无限制
    setsession=[],  # 开始会话前执行的命令列表。如：["set datestyle to ...", "set time zone ..."]
    ping=0,
    # ping MySQL服务端，检查是否服务可用。
    # 如：0 = None = never,   从不
    # 1 = default = whenever it is requested,  任何一个被要求的时候
    # 2 = when a cursor is created,   当创建游标的时候
    # 4 = when a query is executed,   当一个查询被执行的时候
    # 7 = always
    host='127.0.0.1',
    port=3306,
    user='root',
    password='',
    database='day113',
    charset='utf8'
)


def get_conn():
    conn = POOL.connection()
    cursor = conn.cursor(pymysql.cursors.DictCursor)   # 以字典的形式输出

    return conn, cursor


def reset_conn(conn, cursor):
    cursor.close()
    conn.close()


def fetch_all(sql, args):

    conn, cursor = get_conn()
    cursor.execute(sql, args)
    result = cursor.fetchall()
    reset_conn(conn, cursor)

    return result


def fetch_one(sql, args):
    conn, cursor = get_conn()
    cursor.execute(sql, args)
    result = cursor.fetchone()
    reset_conn(conn, cursor)

    return result


def insert_one(sql, args):
    conn, cursor = get_conn()
    cursor.execute(sql, args)
    conn.commit()
    reset_conn(conn, cursor)

ret = fetch_all("select * from user", ())   # [{'id': 1, 'name': 'alex'}, {'id': 2, 'name': 'eeee'}]

ret2 = fetch_one("select name from user where id=%s", (1,))  # {'name': 'alex'}

ret3 = insert_one("insert into user(id, name) values (%s, %s)",(4,"ffffff"))
print(ret)
print(ret2)


















