articol = "Compania Municipală Termoenergetica Bucureşti anunţă, luni, că în următoarele zile se vor face lucrări de remediere a unor avarii pe conductele reţelei termice, în mai multe zone din Capitală. Potrivit sursei citate, intervenţiile au durate diferite de realizare, în funcţie de complexitatea fiecărei lucrări. Sunt afectaţi locuitorii din aproximativ 250 de blocuri."
articol_x = articol[(len(articol)//2):]
articol_y = articol[:(len(articol)//2)]
articol_y_modificat = articol_y.upper().strip()
articol_x_modificat = articol_x.replace(",","").replace(".","").replace("?","").replace("!","").capitalize()[::-1]
print(articol_y_modificat + articol_x_modificat)