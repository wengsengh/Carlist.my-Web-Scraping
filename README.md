# Carlist.my Web Scraping with scrapy

## 1.0 Project Background
Carlist.my is website for used cars listing for sale in Malaysia. <p>
This project uses scrapy to extract the web car listing data from carlist.my <p>
  
![image](https://user-images.githubusercontent.com/24800888/176110115-1be8a033-4a49-477a-92cd-ac07ea9d5932.png)<p>
![image](https://user-images.githubusercontent.com/24800888/176110991-cfb15ab8-c0c1-4f73-a358-8a69c5c5e022.png)<p>

## 2.0 The Required Package and Extension
pip install scrapy <p>
pip lxml <p>
The Chrome Extension <p>
xpath helper

## 3.0 Extract the Web Data
1. Analyze the URL rules and format
2. Develop a data extraction strategy
3. Determine how data is stored

## 4.0 Data Cleansing
1. Remove the column that is not relevant like 'type', 'position', 'item_type', 'item_additionalType', 'item_url', 'item_image', 'item_offers_type', 'item_offers_priceCurrency', 'item_offers_itemCondition', 'item_offers_seller_url', etc.
2. Extract the car model year and engine capacity (cc) from the 'item_name' column by using regular expression (RegEx). <p>
![image](https://user-images.githubusercontent.com/24800888/177068707-e1a00f44-09e5-451b-aebc-9496344382ff.png)

## 5.0 Data Visualization with Tableau
The link: https://public.tableau.com/app/profile/weng.seng/viz/carlist2/Story1?publish=yes <p>

5.1 Toyota <p>
![image](https://user-images.githubusercontent.com/24800888/177069619-f518738f-b7cf-41a4-8e62-784204255749.png) <p>
The top listing model: Vios <p>
The top listing model year: 2014 <p>
The top listing body type: Sedan then followed by MPV <p>
5.2 Peroduo <p>
![image](https://user-images.githubusercontent.com/24800888/177069709-81179162-d286-4256-b0bd-6c700c8ad446.png) <p>
The top listing model: Myvi <p>
The top listing model year: 2015 <p>
The top listing body type: Hatchback



