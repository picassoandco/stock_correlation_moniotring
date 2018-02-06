import win32com.client

excel = win32com.client.Dispatch("Excel.Application")
excel.Visible = True
wb = excel.Workbooks.Open('C:\\Users\\MINJUN KWAK\\Documents\\github\\stock_correlation_moniotring\\last price_v2_20180123.xlsm')
ws = wb.CORR
print(ws.Cells(1,1).Value)
excel.Quit()