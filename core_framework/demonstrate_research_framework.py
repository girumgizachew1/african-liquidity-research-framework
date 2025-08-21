"""
Demonstration of the LAVA Research Framework with sample data and onchain integration.

This script shows how to use the AfricanLiquidityResearchFramework
to analyze real market data and generate research findings, including
the new onchain data integration capabilities.
"""

import json
from liquidity_research_methodology import AfricanLiquidityResearchFramework

def demonstrate_research_framework():
    """Demonstrate the research framework in action with onchain integration."""
    
    print("🔬 LAVA RESEARCH FRAMEWORK DEMONSTRATION")
    print("=" * 80)
    print("This demonstration shows how the framework analyzes real market data")
    print("to answer the two key research questions about African liquidity.")
    print("NOW INCLUDING ONCHAIN DATA INTEGRATION! 🚀")
    print()
    
    # Initialize the research framework
    framework = AfricanLiquidityResearchFramework()
    
    # Load sample market data with onchain integration
    print("📊 Loading sample market data with onchain integration...")
    try:
        with open('sample_onchain_data.json', 'r') as f:
            market_data = json.load(f)
        print("✅ Loaded onchain-enabled data for analysis")
    except FileNotFoundError:
        print("⚠️  sample_onchain_data.json not found, using traditional data...")
        with open('sample_market_data_template.json', 'r') as f:
            market_data = json.load(f)
    
    print(f"✅ Loaded data for {len(market_data)} markets:")
    for market_key, data in market_data.items():
        print(f"   - {data['market_name']} ({data['region']})")
        # Check if onchain data is available
        if 'blockchain_metrics' in data:
            print(f"     🔗 Blockchain Integration: ✅ Available")
        else:
            print(f"     🔗 Blockchain Integration: ❌ Not Available")
    print()
    
    # Generate comprehensive research report with onchain analysis
    print("🔍 Generating research report with onchain integration...")
    research_report = framework.generate_research_report(
        market_data, 
        output_file='lava_research_report_with_onchain.json'
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
        
        # Show blockchain integration if available
        if 'blockchain_integration' in finding['liquidity_sources']:
            print(f"   🔗 Blockchain Integration: ✅ Active")
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
    
    # NEW: Research Question 3: Onchain Integration
    print("\n3️⃣ 🚀 HOW DOES ONCHAIN DATA INTEGRATION ENHANCE LIQUIDITY ANALYSIS?")
    print("-" * 70)
    
    if "onchain_analysis" in research_report["findings"]:
        onchain_findings = research_report["findings"]["onchain_analysis"]
        
        # Blockchain Network Analysis
        if onchain_findings["blockchain_networks"]:
            print("🔗 BLOCKCHAIN NETWORK ADOPTION:")
            for market_key, network_data in onchain_findings["blockchain_networks"].items():
                market_name = network_data["market_name"]
                region = network_data["region"]
                tvl = network_data["liquidity_metrics"]["total_value_locked"]
                daily_volume = network_data["liquidity_metrics"]["daily_volume"]
                
                print(f"   📊 {market_name} ({region}):")
                print(f"     Total Value Locked: ${tvl:,.0f}")
                print(f"     Daily Volume: ${daily_volume:,.0f}")
                print(f"     Celo Transactions: {network_data['network_adoption']['celo_transactions']:,}/day")
                print(f"     Stellar Transactions: {network_data['network_adoption']['stellar_transactions']:,}/day")
                print()
        
        # DeFi Integration Analysis
        if onchain_findings["defi_protocols"]:
            print("🏦 DEFI PROTOCOL INTEGRATION:")
            for market_key, defi_data in onchain_findings["defi_protocols"].items():
                market_name = defi_data["market_name"]
                region = defi_data["region"]
                avg_apy = defi_data["yield_metrics"]["avg_apy"]
                uniswap_liquidity = defi_data["protocol_adoption"]["uniswap_liquidity"]
                
                print(f"   📊 {market_name} ({region}):")
                print(f"     Average APY: {avg_apy:.1f}%")
                print(f"     Uniswap Liquidity: ${uniswap_liquidity:,.0f}")
                print(f"     Risk Score: {defi_data['risk_metrics'].get('smart_contract_risk_score', 0):.2f}")
                print()
        
        # Cross-Chain Efficiency Analysis
        if onchain_findings["cross_chain_efficiency"]:
            print("🌉 CROSS-CHAIN EFFICIENCY:")
            for market_key, bridge_data in onchain_findings["cross_chain_efficiency"].items():
                market_name = bridge_data["market_name"]
                region = bridge_data["region"]
                daily_bridge_volume = bridge_data["cross_chain_volume"]["daily_bridge_volume"]
                celo_stellar_success = bridge_data["bridge_efficiency"]["celo_stellar_bridge"]["success_rate"]
                
                print(f"   📊 {market_name} ({region}):")
                print(f"     Daily Bridge Volume: ${daily_bridge_volume:,.0f}")
                print(f"     Celo-Stellar Success Rate: {celo_stellar_success:.1f}%")
                print(f"     Bridge Fee Revenue: ${bridge_data['cross_chain_volume']['bridge_fee_revenue']:,.0f}")
                print()
        
        # Smart Contract Performance Analysis
        if onchain_findings["smart_contract_performance"]:
            print("⚡ SMART CONTRACT PERFORMANCE:")
            for market_key, contract_data in onchain_findings["smart_contract_performance"].items():
                market_name = contract_data["market_name"]
                region = contract_data["region"]
                gas_optimization = contract_data["gas_efficiency"]["gas_optimization_score"]
                execution_success = contract_data["contract_performance"]["execution_success_rate"]
                audit_score = contract_data["security_metrics"]["audit_score"]
                
                print(f"   📊 {market_name} ({region}):")
                print(f"     Gas Optimization Score: {gas_optimization:.2f}")
                print(f"     Execution Success Rate: {execution_success:.1f}%")
                print(f"     Audit Score: {audit_score:.2f}")
                print()
        
        # Onchain Insights
        if onchain_findings["onchain_insights"]:
            print("💡 ONCHAIN INTEGRATION INSIGHTS:")
            insights = onchain_findings["onchain_insights"]
            
            if insights["blockchain_adoption_trends"]:
                for trend in insights["blockchain_adoption_trends"]:
                    print(f"   🔗 {trend['trend']}")
                    print(f"      Evidence: {trend['evidence']}")
                    print(f"      Implication: {trend['implication']}")
                    print()
            
            if insights["defi_integration_opportunities"]:
                for opportunity in insights["defi_integration_opportunities"]:
                    print(f"   🏦 {opportunity['opportunity']}")
                    print(f"      Evidence: {opportunity['evidence']}")
                    print(f"      Implication: {opportunity['implication']}")
                    print()
            
            if insights["cross_chain_efficiency_gains"]:
                for gain in insights["cross_chain_efficiency_gains"]:
                    print(f"   🌉 {gain['gain']}")
                    print(f"      Evidence: {gain['evidence']}")
                    print(f"      Implication: {gain['implication']}")
                    print()
    else:
        print("⚠️  No onchain data available for analysis")
        print("   Framework is ready for onchain integration when data becomes available")
        print()
    
    # Research Question 2: Efficiency (Traditional + Onchain)
    print("\n2️⃣ HOW EFFICIENTLY IS THIS LIQUIDITY USED? (Traditional + Onchain)")
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
        
        # Show onchain efficiency if available
        if market_key in market_data and 'blockchain_metrics' in market_data[market_key]:
            blockchain_data = market_data[market_key]['blockchain_metrics']
            print(f"   🔗 Blockchain Efficiency:")
            print(f"      Gas Cost: ${blockchain_data.get('avg_gas_fee_usd', 0):.2f}")
            print(f"      Confirmation Time: {blockchain_data.get('avg_confirmation_time_seconds', 0):.1f}s")
            print(f"      Throughput: {blockchain_data.get('transactions_per_second', 0):,} TPS")
        
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
    
    # NEW: Onchain Integration Conclusions
    if "onchain_conclusions" in research_report["conclusions"]:
        print("🚀 ONCHAIN INTEGRATION CONCLUSIONS:")
        onchain_conclusions = research_report["conclusions"]["onchain_conclusions"]
        for conclusion in onchain_conclusions:
            if 'trend' in conclusion:
                print(f"   🔗 {conclusion['trend']}")
                print(f"      Evidence: {conclusion['evidence']}")
                print(f"      Implication: {conclusion['implication']}")
            elif 'opportunity' in conclusion:
                print(f"   🏦 {conclusion['opportunity']}")
                print(f"      Evidence: {conclusion['evidence']}")
                print(f"      Implication: {conclusion['implication']}")
            elif 'gain' in conclusion:
                print(f"   🌉 {conclusion['gain']}")
                print(f"      Evidence: {conclusion['evidence']}")
                print(f"      Implication: {conclusion['implication']}")
            print()
    
    print("✅ Research report with onchain integration generated and saved to 'lava_research_report_with_onchain.json'")
    print("\n🔬 This framework now provides:")
    print("   1. Traditional liquidity analysis (sourcing + efficiency)")
    print("   2. 🆕 ONCHAIN DATA INTEGRATION (blockchain + DeFi + cross-chain)")
    print("   3. Comprehensive methodology for investigating African liquidity markets")
    print("   4. Extensible design for future blockchain and DeFi data sources")
    print("\n🚀 The framework is ready for onchain data integration and can analyze:")
    print("   • Blockchain network adoption and efficiency")
    print("   • DeFi protocol integration and yield opportunities")
    print("   • Cross-chain bridge efficiency and costs")
    print("   • Smart contract performance and gas optimization")

if __name__ == "__main__":
    demonstrate_research_framework()
