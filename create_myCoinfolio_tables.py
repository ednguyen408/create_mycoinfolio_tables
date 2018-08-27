import logging
import logging.handlers
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

#so I can use all the postgres vendor specific datatypes with sqlalchemy
from sqlalchemy.dialects.postgresql import *

### setup logging ###
    
logger = logging.getLogger('alchemy')
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s %(levelname)5s %(name)7s %(thread)d - %(message)s')
stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)
logger.addHandler(stream_handler)


db_string = f"postgresql://postgres:postgres@127.0.0.1:5432/mycoinfolio"
db = create_engine(db_string)
Session = sessionmaker(db)
base = declarative_base()


class coinfolioTable(base):
    __tablename__ = 'coinfolio'
    coin_id = Column(INTEGER, primary_key=True)
    cm_id = Column(VARCHAR (40))
    name = Column(VARCHAR (40))
    symbol = Column(VARCHAR (5))
    rank = Column(INTEGER)
    price_usd = Column(REAL)
    volume_usd_24h = Column(REAL)
    market_cap_usd = Column(REAL)
    available_supply = Column(REAL)
    total_supply = Column(REAL)
    max_supply = Column(REAL)
    percent_change_1h = Column(REAL)
    percent_change_24h = Column(REAL)
    percent_change_7d = Column(REAL)
    last_updated = Column(TIMESTAMP)
        
class userTable(base):
    __tablename__ = 'user'
    user_id = Column(INTEGER, primary_key=True)
    username = Column(VARCHAR (200)) 
    password = Column(VARCHAR (200)) 
    email = Column(VARCHAR (200)) 
    active = Column(BOOLEAN)
    initial_investment = Column(REAL)
    joined_date = Column(TIMESTAMP)
    last_login = Column(TIMESTAMP) 

class globalTable(base):
    __tablename__ = 'global'
    global_id = Column(INTEGER, primary_key=True)
    total_market_cap_usd = Column(REAL)
    total_24h_volume_usd = Column(REAL)
    bitcoin_percentage_of_market_cap = Column(REAL)
    active_currencies = Column(INTEGER)
    active_markets = Column(INTEGER)
    last_updated = Column(TIMESTAMP)  

#class live_coinsTable(base):
    #__tablename__ = 'live_coins'
    #cm_id = Column(VARCHAR (40))
    #name = Column(VARCHAR (40))
    #symbol = Column(VARCHAR (5))
    #rank = Column(INTEGER)
    #price_usd = Column(REAL)
    #volume_usd_24h = Column(REAL)
    #market_cap_usd = Column(REAL)
    #available_supply = Column(REAL)
    #total_supply = Column(REAL)
    #max_supply = Column(REAL)
    #percent_change_1h = Column(REAL)
    #percent_change_24h = Column(REAL)
    #percent_change_7d = Column(REAL)
    #last_updated = Column(TIMESTAMP)
    
#class live_globalTable(base):
    #__tablename__ = 'live_global' 
    #total_market_cap_usd = Column(REAL)
    #total_24h_volume_usd = Column(REAL)
    #bitcoin_percentage_of_market_cap = Column(REAL)
    #active_currencies = Column(INTEGER)
    #active_markets = Column(INTEGER)
    #last_updated = Column(TIMESTAMP)
    
#class user_coinsTable(base):
    #__tablename__ = 'user_coins'
    #user_id = Column(INTEGER)
    #coin = Column(VARCHAR (40))
    #symbol = Column(VARCHAR (5))
    #quantity = Column(REAL)
    #cost_usd = Column(REAL)
    #price_usd = Column(REAL)
    #portfolio_value = Column(REAL)
    #profit_usd = Column(REAL)
    #profit_percent = Column(REAL)
    #allocation_percent = Column(REAL)
    #percent_change_24h = Column(REAL)
    #percent_change_7d = Column(REAL)
    #last_updated = Column(TIMESTAMP) 
    

#class alertsTable(base):
    #__tablename__ = 'alerts'
    #user_id = Column(INTEGER)
    #item = Column(VARCHAR (30)) 
    #attribute = Column(VARCHAR (50)) 
    #operator = Column(VARCHAR (5)) 
    #value = Column(REAL)
    #title = Column(VARCHAR (200))
    #created = Column(TIMESTAMP)
    #last_triggered = Column(TIMESTAMP)
    #notification_enabled = Column(VARCHAR (10))
    #notification_sent = Column(TIMESTAMP) 
    
    
def main():
    '''
    This program uses schalchemys ORM approach to create the tables for myCoinfolio
    Database is postgres 9.6
    '''
    
    try:
        logger.info(f'Creating Tables now')
        base.metadata.create_all(db)
    except Exception as e:
        logger.error(f'{e}') 

if __name__ == '__main__':
    main() 