from sqlalchemy import Column, Integer, String
from sqlalchemy.ext import declarative
 
 
Base = declarative.declarative_base()
 
 
class Jobs(Base):
    __tablename__ = "Jobs";
 
    JobID = Column(String(255), primary_key=True)
    NumServer = Column(Integer)
 
    def __init__(self,JobID,NumServer=None):
        self.JobID = JobID
        self.NumServer = NumServer

    def __json__(self):
        return dict(
            JobID = self.JobID,
            NumServer = self.NumServer,
        )

