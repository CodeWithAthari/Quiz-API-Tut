from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import create_engine, Column, String, Integer, Text,select

host = "localhost"
user = "root"
password = ""
database = "Quiz_Database"

engine = create_engine(url="mysql+pymysql://{0}:{1}@{2}/{3}".format(
    user, password, host, database
))
Base = declarative_base()


class QuizCategories(Base):
    __tablename__ = "quiz_categories"
    id = Column(Integer, primary_key=True, autoincrement=True)
    category_name = Column(String(255))


class Quizes(Base):
    __tablename__ = "quiz_quizes"
    id = Column(Integer, primary_key=True, autoincrement=True)
    category_id = Column(Integer, nullable=False)
    quiz_title = Column(String(255), nullable=False)
    option_a = Column(String(255), nullable=False)
    option_b = Column(String(255), nullable=False)
    option_c = Column(String(255), nullable=False)
    option_d = Column(String(255), nullable=False)
    correct_option = Column(String(255), nullable=False)


Base.metadata.create_all(engine)


def insert_cat(category_name):
    Session = sessionmaker(bind=engine)
    session = Session()
    table = QuizCategories(category_name=category_name)
    session.add(table)
    session.commit()
    session.close()
    print("Category Inserted => ", category_name)


def insert_quiz(category_id, quiz_title, option_a, option_b, option_c, option_d, correct_option):
    Session = sessionmaker(bind=engine)
    session = Session()
    table = Quizes(category_id=category_id, quiz_title=quiz_title, option_a=option_a, option_b=option_b,
                   option_c=option_c
                   , option_d=option_d, correct_option=correct_option)
    session.add(table)
    session.commit()
    session.close()
    print("Quiz Inserted For Cat Id => ", category_id)


def get_categories():
    Session = sessionmaker(bind=engine)
    session = Session()
    rows= session.query(QuizCategories).all()
    lst = []
    for row in rows:
        result = row.__dict__
        result.pop("_sa_instance_state",None)
        lst.append(result)
    session.close()
    return lst


def get_quiz_by_cat(category_id):
    Session = sessionmaker(bind=engine)
    session = Session()
    rows= session.query(Quizes).where(Quizes.category_id == category_id).all()
    session.close()
    if not rows:
        return None
    lst = []
    for row in rows:
        result = row.__dict__
        result.pop("_sa_instance_state",None)
        lst.append(result)
    return lst


if __name__ == "__main__":
    # print(get_quiz_by_cat(3))
    insert_quiz(2, "Who was Sheikhspeare?", "Poet", "Actor", "Comedian", "Teacher", "Poet")
    pass
    # insert_cat("Physics")
