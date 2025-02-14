from Config import Config
import pymysql

def get_db_connection():
    db = pymysql.connect(
        host = Config.host,
        user = Config.user,
        password = Config.password,
        database = Config.database
    )
    return db
INSERT_JOBS_QUERY = """
            INSERT INTO jobs (title, description, skills_req, date_posted, link)
            values(%s,%s,%s,%s,%s)
"""
def add_jobs(title, description, skills_req, date_posted,link):
    db = get_db_connection()
    cursor = db.cursor()#Here the cursor is made
    #Now executing the above command with the recieved arguments from admin
    cursor.execute(INSERT_JOBS_QUERY,(title,description,skills_req,date_posted, link))

    db.commit()
    cursor.close()
    db.close()

