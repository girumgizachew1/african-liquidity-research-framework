"""
LAVA Research Framework - Liquidity Efficiency Calculator

Clean, focused script that calculates liquidity efficiency for African markets.
"""

import json
from liquidity_research_methodology import AfricanLiquidityResearchFramework

def calculate_liquidity_efficiency():
    """Calculate liquidity efficiency for African markets."""
    
    print("🔬 LAVA LIQUIDITY EFFICIENCY CALCULATOR")
    print("=" * 50)
    
    # Initialize framework
    framework = AfricanLiquidityResearchFramework()
    
    # Load data
    print("📊 Loading market data...")
    try:
        with open('sample_onchain_data.json', 'r') as f:
            market_data = json.load(f)
    except FileNotFoundError:
        with open('sample_market_data_template.json', 'r') as f:
            market_data = json.load(f)
    
    # Calculate efficiency
    print("⚡ Calculating liquidity efficiency...")
    efficiency_analysis = framework.analyze_liquidity_efficiency(market_data)
    
    # Display results
    print("\n📈 KEY METRICS")
    print("=" * 50)
    
    # Traditional efficiency with key metrics only
    if efficiency_analysis.get("market_efficiency"):
        print("\n📊 TRADITIONAL MARKETS:")
        for provider_name, data in efficiency_analysis["market_efficiency"].items():
            metrics = data["efficiency_metrics"]
            score = data["efficiency_score"]["overall_score"]
            grade = data["efficiency_score"]["grade"]
            
            print(f"\n   {data['market_name']} ({data['region']}): {score:.1f}/100 ({grade})")
            
            # Key metrics only
            tx_metrics = metrics["transaction_efficiency"]
            float_metrics = metrics["float_efficiency"]
            agent_metrics = metrics["agent_network_efficiency"]
            
            print(f"      Success Rate: {tx_metrics['success_rate']:.2f}%")
            print(f"      Float Turnover: {float_metrics['turnover']:.2f}x")
            print(f"      Agent Utilization: {agent_metrics['utilization_rate']:.2f}%")
            print(f"      Liquidity Coverage: {agent_metrics['liquidity_coverage']:.2f}%")
            print(f"      Cash Coverage: {agent_metrics['cash_coverage']:.2f}%")
    
    # Onchain efficiency
    if efficiency_analysis.get("onchain_efficiency"):
        print("\n🔗 BLOCKCHAIN MARKETS:")
        for provider_name, data in efficiency_analysis["onchain_efficiency"].items():
            score = data["efficiency_score"]
            print(f"   {data['market_name']}: {score:.1f}/100")
    
    # Regional comparison
    if efficiency_analysis.get("regional_comparison"):
        print("\n🌍 REGIONAL COMPARISON:")
        for region, data in efficiency_analysis["regional_comparison"].items():
            if region != "disparity_analysis":
                avg_score = data["average_metrics"]["efficiency_score"]
                print(f"   {region}: {avg_score:.1f}/100 ({data['market_count']} markets)")
    
    print("\n✅ Key metrics calculation complete!")
    return efficiency_analysis

if __name__ == "__main__":
    calculate_liquidity_efficiency()