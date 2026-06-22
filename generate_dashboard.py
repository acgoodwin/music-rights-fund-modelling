#!/usr/bin/env python3
"""
Generate interactive parameter dashboard for financial model.
Allows users to adjust parameters and see IRR results update.
"""

from pathlib import Path
from datetime import datetime

def generate_dashboard():
    """Generate interactive HTML dashboard."""

    html = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Financial Model — Interactive Dashboard</title>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <style>
            * {
                box-sizing: border-box;
            }

            body {
                font-family: Arial, sans-serif;
                margin: 0;
                padding: 20px;
                background-color: #f5f5f5;
            }

            .nav-tabs {
                display: flex;
                border-bottom: 2px solid #4CAF50;
                margin-bottom: 20px;
                background-color: #f9f9f9;
            }
            .nav-tab {
                padding: 12px 20px;
                text-decoration: none;
                color: #333;
                border-bottom: 3px solid transparent;
                cursor: pointer;
                font-weight: 500;
                transition: all 0.3s ease;
            }
            .nav-tab:hover {
                background-color: #f0f0f0;
                color: #4CAF50;
            }
            .nav-tab.active {
                color: #4CAF50;
                border-bottom: 3px solid #4CAF50;
            }

            .container {
                max-width: 1400px;
                margin: 0 auto;
                background-color: white;
                padding: 20px;
                border-radius: 5px;
            }

            h1 {
                color: #333;
                margin-top: 0;
            }

            .dashboard {
                display: grid;
                grid-template-columns: 1fr 1fr;
                gap: 30px;
                margin-top: 20px;
            }

            .panel {
                background-color: #f9f9f9;
                padding: 20px;
                border-radius: 5px;
                border-left: 4px solid #4CAF50;
            }

            .panel h2 {
                color: #4CAF50;
                margin-top: 0;
                font-size: 1.2em;
            }

            .param-group {
                margin-bottom: 20px;
            }

            .param-group h3 {
                font-size: 0.95em;
                color: #666;
                margin: 15px 0 10px 0;
                text-transform: uppercase;
                border-bottom: 1px solid #ddd;
                padding-bottom: 5px;
            }

            .param-row {
                display: flex;
                align-items: center;
                margin-bottom: 12px;
                gap: 10px;
            }

            label {
                flex: 1;
                font-size: 0.9em;
                color: #333;
            }

            input[type="number"],
            input[type="range"] {
                padding: 6px 8px;
                border: 1px solid #ccc;
                border-radius: 3px;
                font-size: 0.9em;
            }

            input[type="number"] {
                width: 100px;
            }

            input[type="range"] {
                flex: 0.5;
            }

            .value-display {
                min-width: 70px;
                text-align: right;
                font-weight: bold;
                color: #4CAF50;
                font-size: 0.9em;
            }

            .results {
                background-color: #e8f5e9;
                padding: 20px;
                border-radius: 5px;
                margin-bottom: 20px;
            }

            .result-row {
                display: flex;
                justify-content: space-between;
                padding: 10px 0;
                border-bottom: 1px solid #c8e6c9;
                font-size: 0.95em;
            }

            .result-row:last-child {
                border-bottom: none;
            }

            .result-label {
                font-weight: bold;
                color: #333;
            }

            .result-value {
                color: #2e7d32;
                font-weight: bold;
            }

            .result-value.target-met {
                color: #4CAF50;
                font-size: 1.1em;
            }

            .result-value.target-miss {
                color: #d32f2f;
            }

            button {
                background-color: #4CAF50;
                color: white;
                padding: 10px 20px;
                border: none;
                border-radius: 5px;
                cursor: pointer;
                font-size: 0.95em;
                font-weight: bold;
                margin-right: 10px;
                margin-top: 10px;
            }

            button:hover {
                background-color: #45a049;
            }

            button.secondary {
                background-color: #666;
            }

            button.secondary:hover {
                background-color: #555;
            }

            .sensitivity-table {
                width: 100%;
                border-collapse: collapse;
                margin-top: 15px;
                font-size: 0.85em;
            }

            .sensitivity-table th,
            .sensitivity-table td {
                padding: 8px;
                text-align: right;
                border-bottom: 1px solid #ddd;
            }

            .sensitivity-table th {
                background-color: #4CAF50;
                color: white;
                font-weight: bold;
            }

            .sensitivity-table td:first-child {
                text-align: left;
            }

            .sensitivity-table tr:hover {
                background-color: #f5f5f5;
            }

            .warning {
                background-color: #fff3cd;
                padding: 10px;
                border-radius: 3px;
                color: #856404;
                margin-top: 10px;
                font-size: 0.85em;
            }

            .success {
                background-color: #d4edda;
                padding: 10px;
                border-radius: 3px;
                color: #155724;
                margin-top: 10px;
                font-size: 0.85em;
            }

            @media (max-width: 1200px) {
                .dashboard {
                    grid-template-columns: 1fr;
                }
            }
        </style>
    </head>
    <body>
        <div class="container">
            <div class="nav-tabs">
                <a href="financial_model.html" class="nav-tab">Base Case</a>
                <a href="financial_model_timeline.html" class="nav-tab">Timeline</a>
                <a href="financial_model_optimized.html" class="nav-tab">Optimized</a>
                <a href="financial_model_comparison.html" class="nav-tab">Comparison</a>
                <a href="financial_model_sensitivity.html" class="nav-tab">Sensitivity</a>
                <a href="financial_model_dashboard.html" class="nav-tab active">Dashboard</a>
            </div>

            <h1>⚙️ Interactive Parameter Dashboard</h1>
            <p>Adjust parameters below to see real-time impact on IRR and returns.</p>

            <div class="dashboard">
                <!-- LEFT PANEL: Parameters -->
                <div class="panel">
                    <h2>Model Parameters</h2>

                    <div class="param-group">
                        <h3>Fund Structure</h3>
                        <div class="param-row">
                            <label>Total Equity ($M):</label>
                            <input type="number" id="total_equity" value="150" step="10" min="50" max="500">
                            <div class="value-display" id="display_total_equity">$150M</div>
                        </div>
                        <div class="param-row">
                            <label>Average Deal Size ($M):</label>
                            <input type="number" id="avg_deal_size" value="4" step="0.5" min="1" max="10">
                            <div class="value-display" id="display_avg_deal_size">$4M</div>
                        </div>
                        <div class="param-row">
                            <label>Purchase Multiple (x revenues):</label>
                            <input type="number" id="purchase_multiple" value="10" step="1" min="5" max="20">
                            <div class="value-display" id="display_purchase_multiple">10x</div>
                        </div>
                    </div>

                    <div class="param-group">
                        <h3>Asset Returns</h3>
                        <div class="param-row">
                            <label>Annual Return %:</label>
                            <input type="range" id="annual_return" value="10" min="5" max="20" step="0.5">
                            <div class="value-display" id="display_annual_return">10.0%</div>
                        </div>
                        <div class="param-row">
                            <label>Hold Period (years):</label>
                            <input type="number" id="hold_period" value="5" step="1" min="3" max="10">
                            <div class="value-display" id="display_hold_period">5y</div>
                        </div>
                    </div>

                    <div class="param-group">
                        <h3>Fees & Upside</h3>
                        <div class="param-row">
                            <label>Management Fee (% AUM):</label>
                            <input type="range" id="mgmt_fee" value="2.0" min="0.5" max="3.5" step="0.1">
                            <div class="value-display" id="display_mgmt_fee">2.0%</div>
                        </div>
                        <div class="param-row">
                            <label>Management Upside %:</label>
                            <input type="number" id="mgmt_upside" value="20" step="5" min="10" max="50">
                            <div class="value-display" id="display_mgmt_upside">20%</div>
                        </div>
                        <div class="param-row">
                            <label>Reinvestment Rate %:</label>
                            <input type="range" id="reinvest_rate" value="50" min="0" max="100" step="5">
                            <div class="value-display" id="display_reinvest_rate">50%</div>
                        </div>
                    </div>

                    <div class="param-group">
                        <h3>Debt Financing</h3>
                        <div class="param-row">
                            <label>Debt Amount ($M):</label>
                            <input type="number" id="debt_amount" value="100" step="10" min="0" max="200">
                            <div class="value-display" id="display_debt_amount">$100M</div>
                        </div>
                        <div class="param-row">
                            <label>Interest Rate %:</label>
                            <input type="range" id="debt_interest" value="7.0" min="3" max="12" step="0.5">
                            <div class="value-display" id="display_debt_interest">7.0%</div>
                        </div>
                    </div>

                    <div class="param-group">
                        <h3>Exit Assumptions</h3>
                        <div class="param-row">
                            <label>Exit Multiple (x):</label>
                            <input type="range" id="exit_multiple" value="14" min="10" max="20" step="1">
                            <div class="value-display" id="display_exit_multiple">14x</div>
                        </div>
                    </div>

                    <div style="margin-top: 20px;">
                        <button onclick="resetParameters()">Reset to Base</button>
                        <button class="secondary" onclick="loadOptimized()">Load Optimized</button>
                    </div>
                </div>

                <!-- RIGHT PANEL: Results -->
                <div class="panel">
                    <h2>📊 Live Results</h2>

                    <div class="results">
                        <div class="result-row">
                            <span class="result-label">Investor IRR:</span>
                            <span class="result-value" id="irr_result">101.0%</span>
                        </div>
                        <div class="result-row">
                            <span class="result-label">vs 20% Target:</span>
                            <span class="result-value" id="irr_gap">+81.0%</span>
                        </div>
                    </div>

                    <div id="irr_status"></div>

                    <h3 style="margin-top: 20px; color: #666; font-size: 0.95em;">Key Metrics</h3>
                    <div class="results">
                        <div class="result-row">
                            <span class="result-label">Cumulative AUM:</span>
                            <span class="result-value" id="aum_result">$250M</span>
                        </div>
                        <div class="result-row">
                            <span class="result-label">Total Deals:</span>
                            <span class="result-value" id="deals_result">37</span>
                        </div>
                        <div class="result-row">
                            <span class="result-label">Annual Returns (Yr 3):</span>
                            <span class="result-value" id="returns_result">$15.5M</span>
                        </div>
                    </div>

                    <h3 style="margin-top: 20px; color: #666; font-size: 0.95em;">Shareholder Returns</h3>
                    <div class="results">
                        <div class="result-row">
                            <span class="result-label">Fee Income (44%):</span>
                            <span class="result-value" id="fee_result">$4.4M</span>
                        </div>
                        <div class="result-row">
                            <span class="result-label">Exit Upside (44%):</span>
                            <span class="result-value" id="upside_result">$5.8M</span>
                        </div>
                        <div class="result-row" style="border-bottom: 2px solid #4CAF50; padding: 15px 0;">
                            <span class="result-label" style="font-size: 1.1em;">Total Cash:</span>
                            <span class="result-value" style="font-size: 1.1em;" id="total_result">$10.2M</span>
                        </div>
                    </div>

                    <h3 style="margin-top: 20px; color: #666; font-size: 0.95em;">IRR Sensitivity</h3>
                    <table class="sensitivity-table">
                        <tr>
                            <th>Exit Multiple</th>
                            <th>IRR</th>
                        </tr>
                        <tr><td>14x</td><td id="sens_14">101.0%</td></tr>
                        <tr><td>15x</td><td id="sens_15">103.0%</td></tr>
                        <tr><td>16x</td><td id="sens_16">105.0%</td></tr>
                        <tr><td>17x</td><td id="sens_17">107.0%</td></tr>
                        <tr><td>18x</td><td id="sens_18">109.0%</td></tr>
                    </table>
                </div>
            </div>
        </div>

        <script>
            // Simple financial model calculation in JavaScript
            function calculateModel() {
                // Get parameter values
                const totalEquity = parseFloat(document.getElementById('total_equity').value) * 1e6;
                const avgDealSize = parseFloat(document.getElementById('avg_deal_size').value) * 1e6;
                const purchaseMultiple = parseFloat(document.getElementById('purchase_multiple').value);
                const annualReturn = parseFloat(document.getElementById('annual_return').value) / 100;
                const holdPeriod = parseInt(document.getElementById('hold_period').value);
                const mgmtFee = parseFloat(document.getElementById('mgmt_fee').value) / 100;
                const mgmtUpside = parseFloat(document.getElementById('mgmt_upside').value) / 100;
                const reinvestRate = parseFloat(document.getElementById('reinvest_rate').value) / 100;
                const debtAmount = parseFloat(document.getElementById('debt_amount').value) * 1e6;
                const debtInterest = parseFloat(document.getElementById('debt_interest').value) / 100;
                const exitMultiple = parseInt(document.getElementById('exit_multiple').value);

                // Deal economics
                const dealCostPct = 0.075; // 7.5% deal costs
                const dealCost = avgDealSize * dealCostPct;
                const totalInvested = avgDealSize + dealCost;

                // Number of deals
                const numDeals = Math.floor(totalEquity / avgDealSize);

                // Annual returns when fully deployed (simplified)
                const annualReturns = totalInvested * annualReturn * (numDeals / 3);

                // AUM at end
                const aum = totalEquity * 1.2; // Simplified

                // Exit value
                const exitValue = (avgDealSize / purchaseMultiple) * exitMultiple * numDeals;
                const exitCosts = exitValue * 0.02;
                const netProceeds = exitValue - exitCosts;

                // Fee income (simplified)
                const totalFees = aum * mgmtFee * holdPeriod;
                const mgmtFeeIncome = totalFees * 0.1467; // 14.67% to shareholder

                // Upside (simplified)
                const upside = netProceeds * mgmtUpside * 0.0293; // 2.93% to shareholder

                // Simplified IRR calculation (approximate)
                const cashIn = mgmtFeeIncome + upside;
                const cashOut = 0;
                const approxIRR = Math.pow(cashIn / totalEquity, 1/holdPeriod) - 1;
                const irrPercent = approxIRR * 100;

                // Update displays
                document.getElementById('irr_result').textContent = irrPercent.toFixed(1) + '%';
                document.getElementById('irr_gap').textContent = (irrPercent - 20).toFixed(1) + '%';

                // Update status
                const statusDiv = document.getElementById('irr_status');
                if (irrPercent >= 20) {
                    statusDiv.innerHTML = '<div class="success">✓ MEETS 20% Target</div>';
                } else {
                    statusDiv.innerHTML = '<div class="warning">⚠ Below 20% Target</div>';
                }

                document.getElementById('aum_result').textContent = '$' + (aum/1e6).toFixed(0) + 'M';
                document.getElementById('deals_result').textContent = numDeals;
                document.getElementById('returns_result').textContent = '$' + (annualReturns/1e6).toFixed(1) + 'M';
                document.getElementById('fee_result').textContent = '$' + (mgmtFeeIncome/1e6).toFixed(1) + 'M';
                document.getElementById('upside_result').textContent = '$' + (upside/1e6).toFixed(1) + 'M';
                document.getElementById('total_result').textContent = '$' + ((mgmtFeeIncome + upside)/1e6).toFixed(1) + 'M';

                // Update sensitivity table
                for (let mult = 14; mult <= 18; mult++) {
                    const sensExitValue = (avgDealSize / purchaseMultiple) * mult * numDeals;
                    const sensProceeds = (sensExitValue - sensExitValue * 0.02) * mgmtUpside * 0.0293;
                    const sensCashIn = mgmtFeeIncome + sensProceeds;
                    const sensIRR = (Math.pow(sensCashIn / totalEquity, 1/holdPeriod) - 1) * 100;
                    document.getElementById('sens_' + mult).textContent = sensIRR.toFixed(1) + '%';
                }
            }

            function updateDisplays() {
                document.getElementById('display_total_equity').textContent = document.getElementById('total_equity').value + 'M';
                document.getElementById('display_avg_deal_size').textContent = '$' + document.getElementById('avg_deal_size').value + 'M';
                document.getElementById('display_purchase_multiple').textContent = document.getElementById('purchase_multiple').value + 'x';
                document.getElementById('display_annual_return').textContent = document.getElementById('annual_return').value + '%';
                document.getElementById('display_hold_period').textContent = document.getElementById('hold_period').value + 'y';
                document.getElementById('display_mgmt_fee').textContent = document.getElementById('mgmt_fee').value + '%';
                document.getElementById('display_mgmt_upside').textContent = document.getElementById('mgmt_upside').value + '%';
                document.getElementById('display_reinvest_rate').textContent = document.getElementById('reinvest_rate').value + '%';
                document.getElementById('display_debt_amount').textContent = '$' + document.getElementById('debt_amount').value + 'M';
                document.getElementById('display_debt_interest').textContent = document.getElementById('debt_interest').value + '%';
                document.getElementById('display_exit_multiple').textContent = document.getElementById('exit_multiple').value + 'x';
            }

            function resetParameters() {
                document.getElementById('total_equity').value = 150;
                document.getElementById('avg_deal_size').value = 4;
                document.getElementById('purchase_multiple').value = 10;
                document.getElementById('annual_return').value = 10;
                document.getElementById('hold_period').value = 5;
                document.getElementById('mgmt_fee').value = 2.0;
                document.getElementById('mgmt_upside').value = 20;
                document.getElementById('reinvest_rate').value = 50;
                document.getElementById('debt_amount').value = 100;
                document.getElementById('debt_interest').value = 7.0;
                document.getElementById('exit_multiple').value = 14;
                updateDisplays();
                calculateModel();
            }

            function loadOptimized() {
                document.getElementById('exit_multiple').value = 16;
                document.getElementById('mgmt_fee').value = 1.5;
                document.getElementById('reinvest_rate').value = 25;
                document.getElementById('debt_interest').value = 6.5;
                updateDisplays();
                calculateModel();
            }

            // Add event listeners
            document.querySelectorAll('input').forEach(input => {
                input.addEventListener('change', () => {
                    updateDisplays();
                    calculateModel();
                });
                input.addEventListener('input', () => {
                    updateDisplays();
                    calculateModel();
                });
            });

            // Initial calculation
            updateDisplays();
            calculateModel();
        </script>
    </body>
    </html>
    """

    return html


if __name__ == "__main__":
    html = generate_dashboard()
    output_path = Path("/Users/andrewgoodwin/financial_model_dashboard.html")
    output_path.write_text(html)
    print(f"✓ Interactive dashboard generated: {output_path}")
