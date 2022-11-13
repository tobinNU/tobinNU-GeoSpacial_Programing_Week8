import matplotlib.pyplot as plt
import pandas as pd
import arcgis

#Diocese dataframe
dioc = pd.DataFrame.spatial.from_featureclass("diocese1350")


series = dioc[['Country_Mo', 'DioceseID',]].groupby('Country_Mo').count().sort_values(['DioceseID'], ascending=False).reset_index()

Top10 = series.head(10)

#print(series)

print(Top10)


#Bar chart
plt.barh(Top10.Country_Mo, Top10.DioceseID)


plt.ylabel('Diocese Count')
plt.suptitle('Diocese per Country in 1350 AD')


plt.show()



