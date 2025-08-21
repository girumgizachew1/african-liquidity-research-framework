# LAVA Research: African Liquidity Analysis Framework

**This repository contains the methodology and framework for investigating liquidity in Africa, addressing the LAVA Technical Research Analyst Task 1.**

## 🎯 Research Questions Addressed

1. **Where can and do African payment orchestration companies source liquidity?**
2. **How efficiently is this liquidity used?**

## 🔬 Research Methodology Framework

**`liquidity_research_methodology.py`** - Core research framework that provides:

### **Liquidity Sourcing Analysis**
- Source identification and volume analysis by market and region
- Primary liquidity source identification
- Regional sourcing pattern analysis
- Market maturity impact assessment

### **Efficiency Measurement Methodology**
- Multi-dimensional efficiency measurement with regional comparison
- Transaction success rates and failure patterns
- Float turnover and velocity metrics
- Agent network health and friction point identification
- Regional efficiency disparity analysis

### **Data Requirements**
The framework requires market data with:
- **Basic Info**: market_name, country, region
- **Liquidity Sourcing**: liquidity_sources, liquidity_volumes
- **Transaction Metrics**: attempted, successful, failed transactions
- **Float Metrics**: total_volume, average_float
- **Agent Network**: total, active, with_liquidity, with_cash agents

## 📊 Sample Data & Demonstration

**`sample_market_data_template.json`** - Template showing required data format
**`demonstrate_research_framework.py`** - Shows the framework in action

## 🚀 Quick Start

1. **Install dependencies:**
```bash
pip install -r requirements.txt
```

2. **Run the demonstration:**
```bash
python demonstrate_research_framework.py
```

3. **Use with your own data:**
```python
from liquidity_research_methodology import AfricanLiquidityResearchFramework

framework = AfricanLiquidityResearchFramework()
market_data = framework.load_market_data(your_data_file)
research_report = framework.generate_research_report(market_data)
```

## 📈 Key Research Findings (Sample Analysis)

### **Liquidity Sourcing Patterns**
- **Commercial Banks** are the primary source across all markets
- **Agent Networks** provide 30-31% of liquidity
- **User Deposits** contribute 15-16% of liquidity
- Regional coordination opportunities exist for liquidity management

### **Efficiency Analysis**
- **Kenya M-PESA**: 79.3/100 (B+) - Mature market efficiency
- **Ghana MTN MoMo**: 77.2/100 (B+) - Growth market challenges
- **Nigeria OPay**: 69.4/100 (B-) - Emerging market inefficiencies

### **Agent Network Frictions**
- **Cash-out failures**: 32K-40K agents lack sufficient e-float
- **Cash-in failures**: 35K-60K agents lack sufficient physical cash
- **Regional pattern**: East Africa shows higher transaction success rates

## 🔍 Research Output

The framework generates comprehensive research reports including:
- Methodology documentation
- Liquidity sourcing analysis
- Efficiency measurement results
- Regional comparison analysis
- Research insights and conclusions
- JSON export for further analysis

