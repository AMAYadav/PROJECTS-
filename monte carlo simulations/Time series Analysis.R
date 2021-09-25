
stock <- round(getSymbols('IRCTC.NS',auto.assign = FALSE) %>% na.omit(.)) 
  

colnames(stock)<- colnames(stock) %>% make_clean_names(.) %>% str_to_lower(.)

stockadjprice <- stock$irctc_ns_adjusted

stockadjprice %>% plot.ts()


stockadjprice_plot <- plot( data=stockadjprice, x=stockadjprice$irctc_ns_adjusted ,y=time,
                          col = 'blue',xlab='Time',
                          ylab='Adj. Closing Price',
                          main = 'TIME SERIES PLOT')

stockadjprice_plot

adf.test(stockadjprice)
acf(stockadjprice)
pacf(stockadjprice,col= 'green')


##p-value = 0.9159 there for the series is  NOT STATIONARY

stockadjprice_log <- log(stock$irctc_ns_adjusted) 

stockadjprice_log_plot <- plot(data=stockadjprice, 
                                x=stockadjprice_log$irctc_ns_adjusted,
                                y=time,
                                col = 'coral',xlab='Time',
                                ylab='Adj. Closing Price(Log. Transformed)',
                                main = 'TIME SERIES PLOT')
stockadjprice_log_plot 

stockadjprice_log_differenced <- diff(log(stock$irctc_ns_adjusted)) %>% na.omit()

stockadjprice_log_differenced_plot <- plot(data=stockadjprice, 
                               x=stockadjprice_log_differenced$irctc_ns_adjusted,
                               y=time,
                               col = 'coral2',xlab='Time',
                               ylab='Adj. Closing Price(DIFFERENCED)',
                               main = 'TIME SERIES PLOT')

stockadjprice_log_differenced_plot

(adf.test(x=stockadjprice_log_differenced)) ## Series is stationary

stockadjprice_log_differenced_arimamodel_fitting <- 
  auto.arima(stockadjprice_log_differenced,trace = TRUE) 

(summary_stats <- summary(stockadjprice_log_differenced_arimamodel_fitting))

stockadjprice_log_differenced_arimamodel_fitting_predict <-




