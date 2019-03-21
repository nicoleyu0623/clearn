from pprint import pprint as pp
import csv
from datetime import datetime
import statistics as s

class BabyPandas:
    def __init__(self,filename, hasHeader):
        self._filename = filename
        self._header = self._load_header(hasheader=hasHeader)
        self._data = self.load_data(hasheader=hasHeader)
        self._hasheader = len(self._header) > 0

    def _getcolindex(self,column):
        # case column param is numeric
        if isinstance(column, int) and column >= 0:
            if len(self._header) > 0 and column < len(self._header):
                return column
            else:
                if column < len(self._data[0]):
                    return column
        #case column param is str
        if isinstance(column, str):
            try:
                idx = self._header.index(column)
                return idx
            except  (ValueError, TypeError):
                print("Exception column {0} not found in header!".format(column))
                return 0.99 #invalid type for indexing

    def _load_header(self, hasheader, separator=','):
        cols = []
        if hasheader:
                with open(self._filename, mode="rt", encoding='utf-8') as f:
                    chars = [ line.split('\n')[0] for line in f.readlines()[0] ]
                gchars = ''.join(chars)
                cols = gchars.split(separator)
        return cols


    def load_data(self, hasheader):
        f = open(self._filename, mode="rt")
        data = csv.reader(f)
        ldata = list(data)
        f.close()

        if hasheader:
            return ldata[1:]
        else:
            return ldata



    def info_columns(self):
        if len(self._header) > 0:
            #lbl_cols = [ "col="+x for x in self._header ]
            print(self._header)
        else:
            print("column names are unavailable")

    def head(self, n=5):
        self.info_columns()
        pp(self._data[:n])

    def tail(self,n=2):
        self.info_columns()
        lst_idx = len(self._data) -1
        lst_idx_n = lst_idx-n
        pp(self._data[lst_idx_n:lst_idx])

    def shape(self):
        nrow = len(self._data)
        ncol = len(self._data[0])
        dims = (nrow, ncol)
        print(dims)

    def info(self):
        self.info_columns()
        types = [ type(x) for x in self._data[0] ]
        print(types)


    def apply(self, column, func, needParam=False, param="%Y-%m-%d"):
        idx = self._getcolindex(column)
        if needParam:
            g = lambda x,f,p:f(x,p)
        else:
            g = lambda x,f:f(x)
        #i = 0
        for row in self._data:
            if needParam:
                row[idx] = g(row[idx],func,param)
            else:
                row[idx] = g(row[idx], func)
            #print("db ",i)
            #i +=1

    def apply_ymd(self, column, dtattribute):
            if dtattribute not in ['year', 'month', 'day']:
                print("dtattribute expected to be year month or day")
                return None
            idx = self._getcolindex(column)
            for row in self._data:
                if dtattribute == 'year':
                    row[idx] = row[idx].year
                if dtattribute == 'month':
                    row[idx] = row[idx].month
                if dtattribute == 'day':
                    row[idx] = row[idx].day



    def get_column(self, column):
        idx = self._getcolindex(column)
        return [ r[idx] for r in self._data ]

    def new_column(self, newname, listcolumn):
        if len(self._header) > 0:
            self._header = self._header + [newname]
        i=0
        for row in self._data:
            self._data[i] = row + [listcolumn[i]]
            i += 1

    def subset(self, column, criteria):

        filtered =[]
        for row in self._data:
            if row[self._getcolindex(column)] == criteria:
                filtered.append(row)
        return filtered

    def summary(self, columns):
        col_indices = columns
        col_names = [ str(c) for c in columns]
        if self._hasheader:
            col_indices = [ self._getcolindex(c) for c in columns ]

        summ = {}
        col_stats ={}
        i = 0
        for col_idx in col_indices:
            col_data = self.get_column(col_idx)
            col_stats['sum'] = sum(col_data)
            col_stats['mean'] = s.mean(col_data)
            col_stats['median']= s.median(col_data)
            #col_stats['mode'] = s.mode(col_data)
            col_stats['min']  = min(col_data)
            col_stats['max'] = max(col_data)
            summ[col_names[i]] = col_stats
            i += 1
        pp(summ)





def devtesting():
    bp = BabyPandas("la_weather.csv", hasHeader=True)
    #bp = BabyPandas("crime_rates.csv", hasHeader=False)

    #pp(bp._data)
    #pp(bp._header)
    #bp.head(n=3)
    #bp.tail(n=2)
    bp.shape()
    #bp.info()
    bp.apply(0, int,needParam=False)
    #bp.head(n=5)
    #pp(bp.get_column(0))
    bp.new_column('copyDay', bp.get_column(0))
    bp.head(n=5)

    dbp = BabyPandas("datetest.csv", hasHeader=True)
    #dbp.head()
    dbp.apply(2,datetime.strptime,needParam=True, param='%Y-%m-%d')
    dbp.head()

    subset = bp.subset('Type of Weather', 'Sunny')
    pp(subset[:3])
    print('last test')
    bp.summary(['Day', 'copyDay'])


def explore_music():
    bp = BabyPandas("music_data.csv",hasHeader=True)
    #bp.head(n=2)
    bp.apply('Date', datetime.strptime,needParam=True, param="%Y-%m-%d")
    #bp.head(n=5)
    bp.new_column('Year', bp.get_column('Date'))
    #bp.head(n=3)
    bp.apply_ymd('Year','year')
    bp.head(n=3)
    music17 = bp.subset('Year', 2017)
    pp(music17[-4:-1])



def main():
    #devtesting()
    explore_music()



if __name__ == '__main__':
    main()
    #unittest.main()