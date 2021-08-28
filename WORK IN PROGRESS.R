#REAL_STATE_PRICE_PREDICTION
#PACKAGES_USED = PSYCH,PERFORMANCE,SMARTLOOKUP,FLEXTABLE,GGALLY


library(flextable)
library(performance)
library(GGally)
library(PerformanceAnalytics)
library(psych)
df= read.csv(file.choose())
df1 =  flextable(df)
head(df)
tail(df)
colnames(df)
nrow(df)
ncol(df)
str(df)
head(df$X4.number.of.convenience.stores,20)  #category
class(df)

describe(df)
describeData(df, head = 5,tail = 5)
df$No = NULL # remove a column
df
describe(df)
sum(is.null(df)) # count for null values

#converting a categorical variable into factors

df$X4.number.of.convenience.stores= as.factor(df$X4.number.of.convenience.stores)

#visualization 
hist(df$X2.house.age)

df$X1.transaction.date = NULL
colnames(df)
pairs(df)
ggpairs(df)

#RENAME COLUMNS

colnames(df)
names(df)[names(df)=='X2.house.age'] ='house_age'
names(df)[names(df)=='X3.distance.to.the.nearest.MRT.station'] = 'house_age'
names(df)[names(df)=='X3.distance.to.the.nearest.MRT.station'] = 'house_age'
names(df)[names(df)=='X4.number.of.convenience.stores'] = 'house_age'
names(df)[names(df)=='X5.latitude'] = 'X5.latitude' 
names(df)[names(df)=='X6.longitude'] = 'X6.longitude' 
names(df)[names(df)=='Y.house.price.of.unit.area'] = 'Y.house.price.of.unit.area' 



names(df)[names(df)=="df$house_age"] ="house_age"

model = lm(df$house_age~.,df)
summary(model)

model_predict = predict(model)
View(model_predict)
a = performance_mse(model)
sqrt(a)
View(df)

























