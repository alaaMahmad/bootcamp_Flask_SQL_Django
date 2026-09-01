USE lead_gen_business;

#1
SELECT 'March' AS month, SUM(amount) AS revenue
FROM billing
WHERE charged_datetime >= '2012-03-01' AND charged_datetime < '2012-04-01';

#2
SELECT client_id, SUM(	amount) AS total_revenue
FROM billing
WHERE client_id = 2;

#3
SELECT client_id, domain_name AS website
FROM sites
WHERE client_id = 10;

#4a
SELECT client_id, COUNT(site_id) AS number_of_websites, MONTHNAME(created_datetime) AS month_created, YEAR(created_datetime) AS year_created
FROM sites
WHERE client_id = 1
GROUP BY YEAR(created_datetime),  MONTHNAME(created_datetime);

#4b
SELECT client_id, COUNT(site_id) AS number_of_websites, MONTHNAME(created_datetime) AS month_created, YEAR(created_datetime) AS year_created
FROM sites
WHERE client_id = 20
GROUP BY YEAR(created_datetime),  MONTHNAME(created_datetime);

#5
SELECT sites.domain_name AS website, COUNT(leads.leads_id) AS number_of_leads
FROM sites
JOIN leads ON sites.site_id = leads.site_id
WHERE leads.registered_datetime >= '2011-01-01' AND leads.registered_datetime <= '2011-02-15'
GROUP BY sites.site_id;

#6
SELECT CONCAT(clients.first_name, ' ', clients.last_name) AS client, COUNT(leads.leads_id) AS number_of_leads
FROM clients
JOIN sites ON clients.client_id = sites.client_id
JOIN leads ON sites.site_id = leads.site_id
WHERE leads.registered_datetime >= '2011-01-01' AND leads.registered_datetime <= '2011-12-31'
GROUP BY clients.client_id;

#7
SELECT CONCAT(clients.first_name, ' ', clients.last_name) AS client, COUNT(leads.leads_id) AS number_of_leads, MONTHNAME(leads.registered_datetime) AS month_generated
FROM clients
JOIN sites ON clients.client_id = sites.client_id
JOIN leads ON sites.site_id = leads.site_id
WHERE leads.registered_datetime >= '2011-01-01' AND leads.registered_datetime < '2011-07-01'
GROUP BY clients.client_id, month_generated;

#8a
SELECT CONCAT(clients.first_name, ' ', clients.last_name) AS client, sites.domain_name AS website, COUNT(leads.leads_id) AS number_of_leads
FROM clients
JOIN sites ON clients.client_id = sites.client_id
JOIN leads ON sites.site_id = leads.site_id
WHERE leads.registered_datetime >= '2011-01-01' AND leads.registered_datetime <= '2011-12-31'
GROUP BY clients.client_id, sites.site_id
ORDER BY clients.client_id;

#8b
SELECT CONCAT(clients.first_name, ' ', clients.last_name) AS client, sites.domain_name AS website, COUNT(leads.leads_id) AS number_of_leads
FROM clients
JOIN sites ON clients.client_id = sites.client_id
LEFT JOIN leads ON sites.site_id = leads.site_id
GROUP BY clients.client_id, sites.site_id
ORDER BY clients.client_id;

#9a
SELECT CONCAT(clients.first_name, ' ', clients.last_name) AS client_name, SUM(billing.amount) AS total_revenue, MONTH(billing.charged_datetime) AS month_charged, YEAR(billing.charged_datetime) AS year_charged
FROM clients
JOIN billing ON clients.client_id = billing.client_id
GROUP BY clients.client_id, YEAR(billing.charged_datetime),  month_charged;

#9b
SELECT CONCAT(clients.first_name, ' ', clients.last_name) AS client_name, SUM(billing.amount) AS total_revenue, MONTHNAME(billing.charged_datetime) AS month_charge, YEAR(billing.charged_datetime) AS year_charged
FROM clients
JOIN billing ON clients.client_id = billing.client_id
GROUP BY clients.client_id, YEAR(billing.charged_datetime), month_charge;

#10
SELECT CONCAT(clients.first_name, ' ', clients.last_name) AS client_name, GROUP_CONCAT(sites.domain_name SEPARATOR '/') AS sites
FROM clients
LEFT JOIN sites ON clients.client_id = sites.client_id
GROUP BY clients.client_id;