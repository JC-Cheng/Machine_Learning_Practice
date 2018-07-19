import pandas as pd

class Market:
    
    def __init__(self, begin_price=None, end_price=None, begin_price_hedge=None, end_price_hedge=None):
        
        self.begin_px = begin_price
        self.end_px = end_price
        
        self.begin_px_hedge = begin_price_hedge
        self.end_px_hedge = end_price_hedge
        
        if isinstance(self.begin_px, pd.DataFrame) and isinstance(self.end_px, pd.DataFrame):
            self.ret = (self.end_px - self.begin_px) / self.begin_px
        else:
            self.ret = None

        if isinstance(self.begin_px_hedge, pd.Series) and isinstance(self.end_px_hedge, pd.Series):
            self.ret_hedge = (self.end_px_hedge - self.begin_px_hedge) / self.begin_px_hedge
        else:
            self.ret_hedge = None
        
    def get_returns(self, date):
        if date in self.ret.index:
            return self.ret.loc[date, :], self.ret_hedge.loc[date]
        else:
            return pd.Series(0, index=self.ret.columns), 0
    
    def get_begin_price(self, date):
        if date in self.begin_px.index:
            return self.begin_px.loc[date, :], self.begin_px_hedge.loc[date]
        else:
            return pd.Series(0, index=self.begin_px.columns), 0
    
    def get_end_price(self, date):
        return self.end_px.loc[date, :], self.end_px_hedge.loc[date]