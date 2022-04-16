
import pandas
from src.config import engine, DATABASE_URL
from src.models import Restaurant


file = "restaurantes.csv"



# https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_sql.html

_csv = pandas.read_csv(file)
_csv.to_sql(name=Restaurant.__tablename__, con=engine,if_exists='append', index= False)
