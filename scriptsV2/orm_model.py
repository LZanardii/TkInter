import sqlalchemy as db
import sqlalchemy.orm as orm

engine = db.create_engine('sqlite:///orm.db')
conn = engine.connect()
engine.echo=True

Base = orm.declarative_base()

# Definição da tabela principal


class Student(Base):
    __tablename__ = 'student'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    lastname = db.Column(db.String(50))
    sex = db.Column(db.String(1))
    age = db.Column(db.SmallInteger)

    def __str__(self):
        text = f'Student: {self.name} {self.lastname} ({self.sex})\n  '
        text += '\n  '.join([str(i) for i in self.addresses])
        return text.strip()


# Definição da tabela secundária
class Address(Base):
    __tablename__ = 'address'

    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey('student.id'))
    address = db.Column(db.String(100))
    email = db.Column(db.String(100))

    def __str__(self):
        return f'Address: {self.address} E-mail: {self.email}'


# Relacionamentos entre as tabelas
Student.addresses = orm.relationship('Address', back_populates='student')
# Student.addresses = orm.relationship('Address', back_populates='student', lazy='joined')
# Student.addresses = orm.relationship('Address', back_populates='student', cascade='all, delete')

Address.student = orm.relationship('Student', back_populates='addresses')

Base.metadata.create_all(engine)
