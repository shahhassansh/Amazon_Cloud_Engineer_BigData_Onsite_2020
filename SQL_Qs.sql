-- Product Table
-- product_id, Date, Qty, Price, Product_Category
-- 101,    01-01-2019,5,  100,  B
-- 102,    01-01-2019,20, 200,  C
-- 103,    03-01-2019,20, 1,    B
-- 104,    04-01-2019,100,10,   A

-- Product_category Table
-- product_id,category
-- A,Apparel
-- B,Toys
-- C,Electronic
-- D,Sports

-- 1. Write a query to get total sale of all product in category toys

select sum(total_sale) from
(
select a.product_id, qty*price as total_sale from sale
int #t1
from sale as a inner join product_category as b
on a.product_id = b.product_id
where b.Product_Category = 'Toys';
);
 
 -- 2. Write a query to get days where total sale is more than 500
 
 select date, sum(qty*price) as total_sale 
 from sale
 group by date
 having total_sale >500;
 
-- 3. Write a query to capture the highest selling category
 
 select a.*, b.category from sale as a 
 into #t1
 left join Product_Category as b
 on a.product_id = b.product_id
 
 
 select category, sum(qty*price) as total_sale 
 into #t2
 from #t1
 group by category;

select category from #t2
where total_sale in (select max(total_sale) from #t2);

-- 4. Color

-- col1    col2    col3
-- yellow   red      green
-- red      yellow   red
-- yellow   yellow   yellow
-- blue     orange   green
-- red      orange   yellow

-- write a query to print the rows where at least one of the column is having the value yellow without using OR


select *
from Color
where concat(col1,col2,col3) like '%Yellow%'