# Music Rights Fund Modelling

Financial model for a $150M music royalty fund with staged deployment, debt financing, and exit analysis.

## Overview

This model calculates returns for a music royalty acquisition fund from the perspective of a 44% shareholder in the UK company that owns 33.33% of the management company.

**Key Structure:**
- $150M equity deployed over 3 years (~$4M deals at 10x revenues)
- $100M debt raised mid-year 3, deployed beginning year 4
- 10% annual asset returns (12-month lag)
- 2% management fee on AUM
- 20% management company upside, 80% investor upside
- 5-year hold period, 14-18x exit multiple

## Usage

```bash
python3 financial_model.py
```

This generates four HTML reports:
- `financial_model.html` — Base case detailed analysis
- `financial_model_optimized.html` — Optimized scenario hitting 20% IRR target
- `financial_model_comparison.html` — Side-by-side comparison
- `financial_model_sensitivity.html` — Sensitivity tables for all key levers

## Model Parameters

Edit the `ModelParams` class in `financial_model.py` to adjust:
- Fund size and deployment schedule
- Asset acquisition costs (data work, valuation, legal, broker)
- Annual asset return percentage
- Management fee rate (% of AUM)
- Debt amount, interest rate, tenor, and amortization type
- Exit multiple and costs
- Reinvestment rate

## Key Levers for IRR

From sensitivity analysis:

1. **Exit Multiple** — Most impactful
   - 14x → 15.9% IRR
   - 16x → 19.9% IRR
   - 17x → 21.7% IRR
   - 18x → 23.5% IRR

2. **Management Fee** — Highly sensitive
   - 1.0% → 19.4% IRR
   - 2.0% → 15.9% IRR
   - 3.0% → 12.6% IRR

3. **Reinvestment Rate**
   - 0% (distribute all) → 18.9% IRR
   - 50% → 15.9% IRR
   - 100% (reinvest all) → 13.0% IRR

4. **Debt Interest Rate**
   - 5% → 17.2% IRR
   - 7% → 15.9% IRR
   - 9% → 14.6% IRR

5. **Asset Return** — Least sensitive
   - 8% → 15.6% IRR
   - 15% → 16.6% IRR

## Optimized Scenario

The optimized scenario achieves **22.9% IRR** with:
- Exit multiple: 14x → 16x
- Management fee: 2.0% → 1.5%
- Reinvestment rate: 50% → 25%
- Debt interest: 7.0% → 6.5%

## Local Viewing

With Caddy configured for .test domains:

```bash
echo "127.0.0.1 financial-model.test" | sudo tee -a /etc/hosts
sudo caddy reload --config ~/Caddyfile
```

Then visit: http://financial-model.test/

## Dependencies

- Python 3.7+
- pandas
- numpy
- scipy (for IRR calculation via Newton method)

## Output Format

All outputs are standalone HTML files with embedded styling — no external dependencies for viewing.

## Author

Andrew Goodwin
