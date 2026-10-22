# FinTech Platform Research — Zerodha (Example)

**Platform:** Zerodha  
**Research date:** [FILL IN]  
**Official sources:** See `../references/sources.md`

## 1. What does the platform do?
Zerodha is an Indian brokerage and financial-services platform that provides online tools for market participation and investor education. Describe only products and services verified on its official website.

## 2. Where data is used (analyst's view)
Examples of data use in a brokerage platform may include:
- displaying orders, holdings and portfolio information to the correct customer;
- monitoring order status and operational failures;
- tracking app performance, page load times and service availability;
- analyzing aggregate customer support topics to identify confusing workflows;
- detecting unusual activity for operational review and risk controls, subject to applicable rules;
- measuring education-content usage to improve learning materials.

These are industry-level examples of possible analytics applications, not claims that Zerodha uses a specific internal model or process. Public sources may not disclose internal analytics details.

## 3. Example analytics question
**Question:** At which step do users experience the most failed order submissions?

Possible fields in a properly governed, anonymized dataset:
- event timestamp;
- app version;
- workflow step;
- error category;
- request latency;
- successful/failed status.

Possible KPIs:
- failure rate = failed submissions ÷ total submissions × 100;
- median and 95th-percentile response time;
- failure rate by app version or workflow step.

## 4. How analytics could improve customer experience
If data shows that one workflow step has unusually high failure rates or long response times, the product team can investigate the cause, fix the interface or service, and compare the metrics before and after the change. Avoid collecting unnecessary personal information and never put credentials or account secrets in an analysis dataset.

## 5. Limitations
- Public information cannot prove the platform's internal data architecture.
- Correlation does not establish causation.
- Metrics must be interpreted with context, privacy, security and regulatory requirements.

## Conclusion
A brokerage platform creates operational and customer-interaction data. Data analysts can help teams monitor reliability, understand user friction and evaluate changes using carefully defined metrics. The report should distinguish verified facts from general examples.
