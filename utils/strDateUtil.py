from datetime import date

def strToDate(str_date):
    return date.fromisoformat(str_date)

def dateToStr(date_datetime):
    type(date_datetime)
    return date_datetime.strftime('%Y-%m-%d')