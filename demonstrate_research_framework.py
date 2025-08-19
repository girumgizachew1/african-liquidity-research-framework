"""
Demonstration of the LAVA Research Framework with sample data.

This script shows how to use the AfricanLiquidityResearchFramework
to analyze real market data and generate research findings.
"""

import json
from liquidity_research_methodology import AfricanLiquidityResearchFramework

def demonstrate_research_framework():
    """Demonstrate the research framework in action."""
    
    print("🔬 LAVA RESEARCH FRAMEWORK DEMONSTRATION")
    print("=" * 80)
    print("This demonstration shows how the framework analyzes real market data")
    print("to answer the two key research questions about African liquidity.")
    print()
    
    # Initialize the research framework
    framework = AfricanLiquidityResearchFramework()
    
    # Load sample market data
    print("📊 Loading sample market data...")
    with open('sample_market_data_template.json', 'r') as f:
        market_data = json.load(f)
    
    print(f"✅ Loaded data for {len(market_data)} markets:")
    for market_key, data in market_data.items():
        print(f"   - {data['market_name']} ({data['region']})")
    print()
    
    # Generate comprehensive research report
    print("🔍 Generating research report...")
    research_report = framework.generate_research_report(
        market_data, 
        output_file='lava_research_report.json'
    )
    
    # Display key findings
    print("\n📈 RESEARCH FINDINGS")
    print("=" * 80)
    
    # Research Question 1: Liquidity Sourcing
    print("\n1️⃣ WHERE CAN AND DO AFRICAN PAYMENT ORCHESTRATION COMPANIES SOURCE LIQUIDITY?")
    print("-" * 70)
    
    sourcing_findings = research_report["findings"]["liquidity_sourcing"]["findings"]
    for market_key, finding in sourcing_findings.items():
        market_name = finding["market_name"]
        region = finding["region"]
        primary_source = finding["primary_source"]
        total_volume = finding["total_liquidity_volume"]
        
        print(f"📊 {market_name} ({region}):")
        print(f"   Primary Source: {primary_source}")
        print(f"   Total Liquidity: ${total_volume:,.0f}")
        print(f"   Sources: {', '.join(finding['liquidity_sources'])}")
        print()
    
    # Regional patterns
    regional_patterns = research_report["findings"]["liquidity_sourcing"]["regional_patterns"]
    print("🌍 REGIONAL LIQUIDITY SOURCING PATTERNS:")
    for region, data in regional_patterns.items():
        print(f"   {region}:")
        print(f"     Markets: {data['market_count']}")
        print(f"     Common Sources: {', '.join(data['common_sources'])}")
        print(f"     Total Volume: ${data['total_volume']:,.0f}")
        print(f"     Avg per Market: ${data['avg_volume_per_market']:,.0f}")
        print()
    
    # Research Question 2: Efficiency
    print("\n2️⃣ HOW EFFICIENTLY IS THIS LIQUIDITY USED?")
    print("-" * 70)
    
    efficiency_findings = research_report["findings"]["efficiency_analysis"]["market_efficiency"]
    for market_key, finding in efficiency_findings.items():
        market_name = finding["market_name"]
        region = finding["region"]
        efficiency_score = finding["efficiency_score"]
        friction_analysis = finding["friction_analysis"]
        
        print(f"📊 {market_name} ({region}):")
        print(f"   Overall Efficiency: {efficiency_score['overall_score']:.1f}/100 ({efficiency_score['grade']})")
        print(f"   Transaction Success: {finding['efficiency_metrics']['transaction_efficiency']['success_rate']:.1f}%")
        print(f"   Float Turnover: {finding['efficiency_metrics']['float_efficiency']['turnover']:.1f}x")
        print(f"   Agent Network Health: {finding['efficiency_metrics']['agent_network_efficiency']['utilization_rate']:.1f}%")
        
        # Friction points
        friction_points = friction_analysis["friction_points"]
        if friction_points["low_liquidity_agents"] > 0:
            print(f"   ⚠️  {friction_points['low_liquidity_agents']:,} agents lack e-float (cash-out failures)")
        if friction_points["low_cash_agents"] > 0:
            print(f"   ⚠️  {friction_points['low_cash_agents']:,} agents lack cash (cash-in failures)")
        print()
    
    # Regional efficiency comparison
    regional_comparison = research_report["findings"]["efficiency_analysis"]["regional_comparison"]
    if "disparity_analysis" in regional_comparison:
        print("🌍 REGIONAL EFFICIENCY DISPARITIES:")
        for comparison, data in regional_comparison["disparity_analysis"].items():
            print(f"   {comparison}:")
            print(f"     Success Rate Gap: {data['success_rate_gap']:+.1f}%")
            print(f"     Agent Health Gap: {data['agent_health_gap']:+.1f}%")
            print(f"     Float Efficiency Gap: {data['float_efficiency_gap']:+.1f}x")
            print(f"     Overall Efficiency Gap: {data['overall_efficiency_gap']:+.1f}")
            print()
    
    # Key insights
    insights = research_report["findings"]["efficiency_analysis"]["efficiency_insights"]
    if insights["key_findings"]:
        print("💡 KEY RESEARCH INSIGHTS:")
        for finding in insights["key_findings"]:
            print(f"   • {finding['finding']}")
            print(f"     Evidence: {finding['evidence']}")
            print(f"     Implication: {finding['implication']}")
            print()
    
    if insights["regional_patterns"]:
        print("🌍 REGIONAL PATTERNS IDENTIFIED:")
        for pattern in insights["regional_patterns"]:
            print(f"   • {pattern['pattern']}")
            print(f"     Evidence: {pattern['evidence']}")
            print(f"     Implication: {pattern['implication']}")
            print()
    
    if insights["efficiency_drivers"]:
        print("⚡ EFFICIENCY DRIVERS IDENTIFIED:")
        for driver in insights["efficiency_drivers"]:
            print(f"   • {driver['driver']}")
            print(f"     Evidence: {driver['evidence']}")
            print(f"     Impact: {driver['impact']}")
            print()
    
    # Conclusions
    print("\n🎯 RESEARCH CONCLUSIONS")
    print("=" * 80)
    
    sourcing_conclusions = research_report["conclusions"]["liquidity_sourcing_conclusions"]
    efficiency_conclusions = research_report["conclusions"]["efficiency_conclusions"]
    
    print("📊 LIQUIDITY SOURCING CONCLUSIONS:")
    for conclusion in sourcing_conclusions:
        print(f"   • {conclusion['conclusion']}")
        print(f"     Evidence: {conclusion['evidence']}")
        print(f"     Implication: {conclusion['implication']}")
        print()
    
    print("⚡ EFFICIENCY CONCLUSIONS:")
    for conclusion in efficiency_conclusions:
        if 'finding' in conclusion:
            print(f"   • {conclusion['finding']}")
            print(f"     Evidence: {conclusion['evidence']}")
            print(f"     Implication: {conclusion['implication']}")
        else:
            print(f"   • {conclusion}")
        print()
    
    print("✅ Research report generated and saved to 'lava_research_report.json'")
    print("\n🔬 This framework provides the methodology for investigating African liquidity markets")
    print("   and can be applied to real market data to generate actionable insights.")

if __name__ == "__main__":
    demonstrate_research_framework()
