import pandas as pd
import os.path

my_path = os.path.abspath(os.path.dirname(__file__))
path = os.path.join(my_path, "Data Ekspor Impor\Perkembangan Ekspor NonMigas (Komoditi) Periode 2017 - 2022.xlsx")
df = pd.read_excel(path)
print(df)