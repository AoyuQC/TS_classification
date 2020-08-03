
import matplotlib.pyplot as plt
import xlrd
xl = xlrd.open_workbook('/Users/getong/Desktop/25-37.xlsx')
table = xl.sheets()[0]
row = table.row_values(1)
col = table.col_values(0)
accx = table.col_values(5,0)
accy = table.col_values(9,0)
accz = table.col_values(19,0)
plt.title('Result Analysis')
plt.plot(accx,color="green",label="accx")
plt.plot(accy,color="yellow",label="accy")
plt.plot(accz,color="red",label="accz")
plt.legend()
plt.show()
