library(tidyverse)

train <- read.csv(file = file.path(getwd(), 'input', 'train.csv'))
test <- read.csv(file = file.path(getwd(), 'input', 'test.csv'))

#EDA----
#Distribution of Sale Price
train %>%
  ggplot() +
  geom_density(aes(x=SalePrice)) +
  scale_x_continuous(labels = scales::dollar)

#Avg SalePrice by Year
train %>%
  group_by(YearBuilt) %>%
  summarise(YearlyAvgSalePrice = mean(SalePrice, na.rm=T)) %>%
  left_join(data.frame(YearBuilt = seq(min(train$YearBuilt), max(train$YearBuilt))),
            ., by='YearBuilt') %>%
  ggplot() +
  geom_line(aes(x=YearBuilt, y=YearlyAvgSalePrice)) +
  geom_point(aes(x=YearBuilt, y=YearlyAvgSalePrice)) +
  geom_hline(yintercept = mean(train$SalePrice, na.rm = T))
