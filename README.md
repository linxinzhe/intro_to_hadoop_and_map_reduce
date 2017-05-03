## Project - Intro to Hadoop and MapReduce - Udacity

### Folder project_purchases
- [Input data format](https://github.com/linxinzhe/intro_to_hadoop_and_map_reduce/blob/master/project_puchases/sample_purchases.txt)
    - 2012-01-01	09:00	San Jose	Men's Clothing	214.05	Amex
    - 2012-01-01	09:00	Fort Worth	Women's Clothing	153.57	Visa
    - 2012-01-01	09:00	San Diego	Music	66.08	Cash
    - 2012-01-01	09:00	Pittsburgh	Pet Supplies	493.51	Discover

##### Q1: Sales per Store
- [q1_mapper_product_category.py](https://github.com/linxinzhe/intro_to_hadoop_and_map_reduce/blob/master/project_puchases/q1_mapper_product_category.py) : read product category and sales 
- [q1_reduce_product_category.py](https://github.com/linxinzhe/intro_to_hadoop_and_map_reduce/blob/master/project_puchases/q1_reducer_sales_per_product_category.py) : sales per product category
- [q1_result.txt](https://github.com/linxinzhe/intro_to_hadoop_and_map_reduce/blob/master/project_puchases/q1_result.txt): sales per product category

##### Q2: Highest Sales per Store
- [q2_mapper_store.py](https://github.com/linxinzhe/intro_to_hadoop_and_map_reduce/blob/master/project_puchases/q2_mapper_store.py) : read store and sales 
- [q2_reducer_highest_sales_per_store.py](https://github.com/linxinzhe/intro_to_hadoop_and_map_reduce/blob/master/project_puchases/q2_reducer_highest_sales_per_store.py) : highest sales per store
- [q2_result.txt](https://github.com/linxinzhe/intro_to_hadoop_and_map_reduce/blob/master/project_puchases/q2_result.txt): highest sales per store

##### Q3: Total Sales of All Store
- [q3_mapper_store.py](https://github.com/linxinzhe/intro_to_hadoop_and_map_reduce/blob/master/project_puchases/q3_mapper_store.py) : read store and sales 
- [q3_reducer_total_sales.py](https://github.com/linxinzhe/intro_to_hadoop_and_map_reduce/blob/master/project_puchases/q3_reducer_total_sales.py) : total sales of all stores
- [q3_result.txt](https://github.com/linxinzhe/intro_to_hadoop_and_map_reduce/blob/master/project_puchases/q3_result.txt): total sales of all stores

### Folder project_web_access_log
- [Input data format](https://github.com/linxinzhe/intro_to_hadoop_and_map_reduce/blob/master/project_web_access_log/sample_access.txt)
    - 10.223.157.186 - - [15/Jul/2009:14:58:59 -0700] "GET / HTTP/1.1" 403 202
    - 10.223.157.186 - - [15/Jul/2009:14:58:59 -0700] "GET /favicon.ico HTTP/1.1" 404 209
    - 10.223.157.186 - - [15/Jul/2009:15:50:35 -0700] "GET / HTTP/1.1" 200 9157

##### Q1: Hits to Page
- [q1_mapper_page.py](https://github.com/linxinzhe/intro_to_hadoop_and_map_reduce/blob/master/project_web_access_log/q1_mapper_page.py) : read page
- [q1_reducer_hits_page.py](https://github.com/linxinzhe/intro_to_hadoop_and_map_reduce/blob/master/project_web_access_log/q1_reducer_hits_page.py) : hits to page
- [q1_result.txt](https://github.com/linxinzhe/intro_to_hadoop_and_map_reduce/blob/master/project_web_access_log/q1_result.txt): total hits to page

##### Q2: Hits to IP
- [q2_mapper_ip.py](https://github.com/linxinzhe/intro_to_hadoop_and_map_reduce/blob/master/project_web_access_log/q2_mapper_ip.py) : read IP
- [q2_reducer_hits_ip.py](https://github.com/linxinzhe/intro_to_hadoop_and_map_reduce/blob/master/project_web_access_log/q2_reducer_hits_ip.py) : hits to IP
- [q2_result.txt](https://github.com/linxinzhe/intro_to_hadoop_and_map_reduce/blob/master/project_web_access_log/q2_result.txt): total hits to IP