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
    print("to answer the three key research questions about African liquidity.")
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
    
    # Check if data has the new providers structure
    if "providers" in market_data:
        print(f"✅ Loaded data for {len(market_data['providers'])} providers:")
        for provider in market_data["providers"]:
            provider_name = provider["name"]
            provider_type = provider["type"]
            metrics = provider["metrics"]
            
            if provider_type == "offchain":
                market_name = metrics.get("market_name", provider_name)
                region = metrics.get("region", "Unknown")
                print(f"   - {market_name} ({region}) - Type: {provider_type}")
            elif provider_type == "onchain":
                source = metrics.get("source", "Unknown")
                print(f"   - {provider_name} (Blockchain Network) - Type: {provider_type} - Source: {source}")
                print(f"     🔗 Blockchain Integration: ✅ Available")
        print()
    else:
        # Fallback for old structure
        print(f"✅ Loaded data for {len(market_data)} markets:")
        for market_key, data in market_data.items():
            print(f"   - {data.get('market_name', market_key)} ({data.get('region', 'Unknown')})")
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
    for provider_name, finding in sourcing_findings.items():
        provider_type = finding.get("provider_type", "unknown")
        market_name = finding["market_name"]
        region = finding["region"]
        primary_source = finding["primary_source"]
        total_volume = finding["total_liquidity_volume"]
        
        if provider_type == "offchain":
            print(f"📊 {market_name} ({region}) - Type: {provider_type}:")
            print(f"   Primary Source: {primary_source}")
            print(f"   Total Liquidity: ${total_volume:,.0f}")
            print(f"   Sources: {', '.join(finding['liquidity_sources'])}")
        elif provider_type == "onchain":
            print(f"🔗 {market_name} (Blockchain Network) - Type: {provider_type}:")
            print(f"   Primary Source: {primary_source}")
            print(f"   Total Liquidity: ${total_volume:,.0f}")
            if "onchain_metrics" in finding:
                onchain_metrics = finding["onchain_metrics"]
                print(f"   TVL: ${onchain_metrics.get('tvl_usd', 0):,.0f}")
                print(f"   Daily Volume: ${onchain_metrics.get('daily_volume_usd', 0):,.0f}")
                print(f"   Data Source: {onchain_metrics.get('data_source', 'Unknown')}")
        print()
    
    # Regional patterns (only for offchain providers)
    regional_patterns = research_report["findings"]["liquidity_sourcing"]["regional_patterns"]
    if regional_patterns:
        print("🌍 REGIONAL LIQUIDITY SOURCING PATTERNS:")
        for region, data in regional_patterns.items():
            print(f"   {region}:")
            print(f"     Markets: {data['market_count']}")
            print(f"     Common Sources: {', '.join(data['common_sources'])}")
            print(f"     Total Volume: ${data['total_volume']:,.0f}")
            print(f"     Avg per Market: ${data['avg_volume_per_market']:,.0f}")
            print()
    
    # Onchain vs Offchain comparison
    onchain_offchain_comparison = research_report["findings"]["liquidity_sourcing"].get("onchain_offchain_comparison", {})
    if onchain_offchain_comparison:
        print("🔄 ONCHAIN VS OFFCHAIN COMPARISON:")
        if "offchain" in onchain_offchain_comparison:
            offchain_data = onchain_offchain_comparison["offchain"]
            print(f"   Offchain Providers: {', '.join(offchain_data['providers'])}")
            print(f"   Total Offchain Volume: ${offchain_data['total_volume']:,.0f}")
        if "onchain" in onchain_offchain_comparison:
            onchain_data = onchain_offchain_comparison["onchain"]
            print(f"   Onchain Providers: {', '.join(onchain_data['providers'])}")
            print(f"   Total TVL: ${onchain_data['total_tvl']:,.0f}")
            print(f"   Total Daily Volume: ${onchain_data['total_daily_volume']:,.0f}")
        print()
    
    # Research Question 2: Liquidity Efficiency
    print("\n2️⃣ HOW EFFICIENTLY IS THIS LIQUIDITY USED?")
    print("-" * 70)
    
    efficiency_findings = research_report["findings"]["efficiency_analysis"]
    
    # Traditional efficiency (offchain)
    if "market_efficiency" in efficiency_findings and efficiency_findings["market_efficiency"]:
        print("📊 TRADITIONAL EFFICIENCY ANALYSIS:")
        for provider_name, efficiency_data in efficiency_findings["market_efficiency"].items():
            market_name = efficiency_data["market_name"]
            region = efficiency_data["region"]
            efficiency_score = efficiency_data["efficiency_score"]
            print(f"   {market_name} ({region}): Efficiency Score: {efficiency_score}/100")
        print()
    
    # Onchain efficiency
    if "onchain_efficiency" in efficiency_findings and efficiency_findings["onchain_efficiency"]:
        print("🔗 ONCHAIN EFFICIENCY ANALYSIS:")
        for provider_name, efficiency_data in efficiency_findings["onchain_efficiency"].items():
            market_name = efficiency_data["market_name"]
            efficiency_score = efficiency_data["efficiency_score"]
            onchain_metrics = efficiency_data["efficiency_metrics"]
            print(f"   {market_name} (Blockchain): Efficiency Score: {efficiency_score}/100")
            print(f"     TVL Efficiency: ${onchain_metrics.get('tvl_efficiency', 0):.2f}M")
            print(f"     Yield Efficiency: {onchain_metrics.get('yield_efficiency', 0):.1f}% APY")
            print(f"     Cross-Chain Efficiency: {onchain_metrics.get('cross_chain_efficiency', 0):.0f}K transfers/day")
        print()
    
    # NEW: Research Question 3: Onchain Integration
    print("\n3️⃣ 🚀 HOW DOES ONCHAIN DATA INTEGRATION ENHANCE LIQUIDITY ANALYSIS?")
    print("-" * 70)
    
    if "onchain_analysis" in research_report["findings"]:
        onchain_findings = research_report["findings"]["onchain_analysis"]
        
        # Blockchain Network Analysis
        if onchain_findings["blockchain_networks"]:
            print("🔗 BLOCKCHAIN NETWORK ADOPTION:")
            for provider_name, network_data in onchain_findings["blockchain_networks"].items():
                market_name = network_data["market_name"]
                region = network_data["region"]
                print(f"   {market_name} ({region}):")
                if "network_metrics" in network_data:
                    metrics = network_data["network_metrics"]
                    print(f"     Daily Transactions: {metrics.get('daily_transactions', 0):,}")
                    print(f"     TVL: ${metrics.get('tvl_usd', 0):,.0f}")
                    print(f"     Active Addresses: {metrics.get('active_addresses', 0):,}")
                print()
        
        # DeFi Protocol Integration
        if onchain_findings["defi_protocols"]:
            print("💰 DEFI PROTOCOL INTEGRATION:")
            for provider_name, defi_data in onchain_findings["defi_protocols"].items():
                market_name = defi_data["market_name"]
                print(f"   {market_name}:")
                if "protocol_metrics" in defi_data:
                    metrics = defi_data["protocol_metrics"]
                    print(f"     Uniswap Liquidity: ${metrics.get('uniswap_liquidity_usd', 0):,.0f}")
                    print(f"     Aave Deposits: ${metrics.get('aave_deposits_usd', 0):,.0f}")
                    print(f"     Average APY: {metrics.get('average_apy_percentage', 0):.1f}%")
                print()
        
        # Cross-Chain Efficiency
        if onchain_findings["cross_chain_efficiency"]:
            print("🌉 CROSS-CHAIN EFFICIENCY:")
            for provider_name, cross_chain_data in onchain_findings["cross_chain_efficiency"].items():
                market_name = cross_chain_data["market_name"]
                print(f"   {market_name}:")
                if "bridge_metrics" in cross_chain_data:
                    metrics = cross_chain_data["bridge_metrics"]
                    print(f"     Daily Bridge Volume: ${metrics.get('daily_bridge_volume_usd', 0):,.0f}")
                    print(f"     Success Rate: {metrics.get('success_rate_percentage', 0):.1f}%")
                    print(f"     Average Transfer Time: {metrics.get('avg_transfer_time_seconds', 0):.1f}s")
                print()
        
        # Smart Contract Performance
        if onchain_findings["smart_contract_performance"]:
            print("⚡ SMART CONTRACT PERFORMANCE:")
            for provider_name, contract_data in onchain_findings["smart_contract_performance"].items():
                market_name = contract_data["market_name"]
                print(f"   {market_name}:")
                if "performance_metrics" in contract_data:
                    metrics = contract_data["performance_metrics"]
                    print(f"     Gas Optimization Score: {metrics.get('gas_optimization_score', 0):.2f}")
                    print(f"     Execution Success Rate: {metrics.get('execution_success_rate', 0):.1f}%")
                    print(f"     Audit Score: {metrics.get('audit_score', 0):.2f}")
                print()
        
        # Onchain Insights
        if "onchain_insights" in onchain_findings:
            insights = onchain_findings["onchain_insights"]
            print("💡 ONCHAIN INTEGRATION INSIGHTS:")
            if "blockchain_adoption_trends" in insights:
                for trend in insights["blockchain_adoption_trends"]:
                    print(f"   📈 {trend['trend']}")
                    print(f"      Evidence: {trend['evidence']}")
                    print(f"      Implication: {trend['implication']}")
                    print()
            if "defi_integration_opportunities" in insights:
                for opportunity in insights["defi_integration_opportunities"]:
                    print(f"   💰 {opportunity['opportunity']}")
                    print(f"      Evidence: {opportunity['evidence']}")
                    print(f"      Implication: {opportunity['implication']}")
                    print()
    
    # Summary
    print("\n🎯 SUMMARY")
    print("=" * 80)
    print("✅ Successfully analyzed both traditional and blockchain liquidity sources")
    print("✅ Generated comprehensive research report with onchain integration")
    print("✅ Demonstrated hybrid analysis capabilities")
    print("✅ Framework ready for real-world blockchain data integration")
    print()
    print("📁 Output saved to: lava_research_report_with_onchain.json")
    print("🚀 Framework ready for LAVA submission!")

if __name__ == "__main__":
    demonstrate_research_framework()
