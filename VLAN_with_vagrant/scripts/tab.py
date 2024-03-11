from tabulate import tabulate

mytab = [('1', 'John Smith', 'This is a rather long description that might look better if it is wrapped a bit')]
header = ("Issue Id", "Author", "Description")
cw=[None, None, 30]

print(tabulate( mytab, headers=header, maxcolwidths=cw, tablefmt="grid" ))