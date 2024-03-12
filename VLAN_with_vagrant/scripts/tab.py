from tabulate import tabulate
from datetime import datetime

current_datetime = datetime.now()
formatted_datetime = current_datetime.strftime('%Y-%m-%d %H:%M')
print(formatted_datetime)

mytab = [('1', 'John Smith', 'This is a rather long description that might look better if it is wrapped a bit')]
header = ("Issue Id", "Author", "Description")
cw=[None, None, 30]

print(tabulate( mytab, headers=header, maxcolwidths=cw, tablefmt="grid" ))
