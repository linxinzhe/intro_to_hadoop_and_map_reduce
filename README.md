## Project - Intro to Hadoop and MapReduce - Udacity

### Folder project_purchases
- Input data format
    - 2012-01-01	09:00	San Jose	Men's Clothing	214.05	Amex
    - 2012-01-01	09:00	Fort Worth	Women's Clothing	153.57	Visa
    - 2012-01-01	09:00	San Diego	Music	66.08	Cash
    - 2012-01-01	09:00	Pittsburgh	Pet Supplies	493.51	Discover

##### Q1: Sales per Store
- [q1_mapper_product_category.py](https://github.com/linxinzhe/intro_to_hadoop_and_map_reduce/blob/master/project_puchases/q1_mapper_product_category.py) : read product category and sales 
- [q1_reduce_product_category.py](https://github.com/linxinzhe/intro_to_hadoop_and_map_reduce/blob/master/project_puchases/q1_reducer_sales_per_product_category.py) : total sales per product category
- [q1_result.txt](https://github.com/linxinzhe/intro_to_hadoop_and_map_reduce/blob/master/project_puchases/q1_result.txt):

##### Q2: Highest Sales per Store
- [q2_mapper_store.py](https://github.com/linxinzhe/intro_to_hadoop_and_map_reduce/blob/master/project_puchases/q2_mapper_store.py) : read store and sales 
- [q2_reducer_highest_sales_per_store.py](https://github.com/linxinzhe/intro_to_hadoop_and_map_reduce/blob/master/project_puchases/q2_reducer_highest_sales_per_store.py) : highest sales per store
- [q2_result.txt](https://github.com/linxinzhe/intro_to_hadoop_and_map_reduce/blob/master/project_puchases/q2_result.txt):

##### Q3: Highest Sales per Store
- [q3_mapper_store.py](https://github.com/linxinzhe/intro_to_hadoop_and_map_reduce/blob/master/project_puchases/q3_mapper_store.py) : read store and sales 
- [q3_reducer_total_sales.py](https://github.com/linxinzhe/intro_to_hadoop_and_map_reduce/blob/master/project_puchases/q3_reducer_total_sales.py) : total sales of all stores
- [q3_result.txt](https://github.com/linxinzhe/intro_to_hadoop_and_map_reduce/blob/master/project_puchases/q3_result.txt):