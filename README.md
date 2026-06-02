# 📊 Retail Price Monitoring Automation Using Playwright

## **Description**

This project demonstrates web automation and competitor price monitoring using **Playwright (Python)**.

The solution automatically navigates to an e-commerce website, searches for a predefined list of products, extracts pricing information, and generates a structured CSV report for further analysis.

The project was developed as a learning exercise to understand browser automation, web scraping, data collection, and automated reporting using Python and Playwright.

---

## **Author**

**Rachel Purnima Johnpeter**

This project was created as part of my automation and data analytics learning journey using Playwright and Python.

---

## **Business Use Case**

Retail organizations often monitor competitor pricing to remain competitive in the market.

This automation demonstrates how pricing information can be collected automatically and transformed into a structured report that can support:

* Competitive pricing analysis
* Market trend monitoring
* Pricing strategy decisions
* Retail analytics and reporting
* Automated data collection workflows

---

## **Tech Stack**

* Python 3.x
* Playwright
* Pandas
* CSV Reporting
* Chromium Browser Automation

---

## **Project Components**

### **1. Playwright Learning Demo**

File:

```python
playwright_keyfunctions.py
```

Purpose:

* Launch Chromium browser
* Navigate to Google
* Demonstrate Playwright browser automation basics
* Understand asynchronous browser interactions

Key Concepts Learned:

* Async Playwright execution
* Browser launch and navigation
* Page interactions
* Browser lifecycle management

---

### **2. Retail Price Monitoring Automation**

File:

```python
retail_price_monitor.py
```

Purpose:

* Search multiple products on an e-commerce website
* Extract product pricing information
* Store results in a structured dataset
* Generate a CSV report automatically

---

## **Features**

* Automated browser interaction
* Product search automation
* Price extraction
* Data collection and transformation
* CSV report generation
* Automated competitor price monitoring workflow

---

## **How It Works**

### Step 1

Launch Chromium browser using Playwright.

### Step 2

Navigate to the target retail website.

### Step 3

Search for predefined products.

### Step 4

Open each product page.

### Step 5

Extract product pricing information.

### Step 6

Store collected data in a Pandas DataFrame.

### Step 7

Sort products by price.

### Step 8

Generate a CSV report automatically.

---

## **Sample Output**

Generated CSV Report:

```text
Retail_Price_Report.csv
```

Example Structure:

| Product Name | Price |
| ------------ | ----- |
| Product A    | 10.99 |
| Product B    | 12.50 |
| Product C    | 15.75 |

---

## **Project Structure**

```text
Retail-Price-Monitoring-Playwright/
│
├── playwright_keyfunctions.py
├── retail_price_monitor.py
└── README.md
```

---


## **Run Playwright Learning Demo**

```bash
python playwright_keyfunctions.py
```

---

## **Run Retail Price Monitoring Automation**

```bash
python retail_price_monitor.py
```

---

## **Learning Objectives**

This project helped in understanding:

* Browser automation using Playwright
* Web scraping fundamentals
* Data extraction techniques
* Automation workflows
* CSV report generation
* Retail analytics use cases
* Competitor price monitoring concepts

---

## **Future Enhancements**

* Scheduled price monitoring
* Multi-website competitor tracking
* Dashboard integration using Power BI
* Automated email reporting
* Historical price trend analysis
* Alert generation for price changes
* AI-powered pricing recommendations

---

## **Limitations**

* Designed for learning purposes
* Website structure changes may impact scraping
* Limited product list
* No real-time monitoring
* No retry/error recovery framework

---

## **Disclaimer**

This project was developed for educational and learning purposes only. The implementation demonstrates browser automation, web scraping, and reporting concepts using Playwright and Python.
