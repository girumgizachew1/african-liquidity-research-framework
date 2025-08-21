"""
LAVA Research Methodology: African Liquidity Analysis Framework

This framework provides the methodology for investigating:
1. Where African payment orchestration companies source liquidity
2. How efficiently this liquidity is used
3. How onchain data integration enhances liquidity analysis

The framework is designed to analyze real market data and generate research findings.
"""

import pandas as pd
import numpy as np
from datetime import datetime
import json
from typing import Dict, List, Union
import logging

# Set up logging for research transparency
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class AfricanLiquidityResearchFramework:
    """
    Research methodology framework for analyzing African liquidity markets.
    
    Addresses the LAVA research questions:
    1. Liquidity sourcing patterns across African markets
    2. Efficiency measurement and comparison methodologies
    3. Regional disparity analysis
    4. Agent network health assessment
    5. Onchain data integration and blockchain efficiency analysis
    """
    
    def __init__(self):
        self.research_timestamp = datetime.now()
        self.methodology_version = "2.0"  # Updated for onchain integration
        
        # Initialize onchain data sources
        self.onchain_sources = {
            "blockchain_networks": ["Celo", "Stellar", "Ethereum", "Polygon"],
            "defi_protocols": ["Uniswap", "Aave", "Compound", "MakerDAO"],
            "african_defi": ["Mara", "Yellow Card", "BitPesa", "Paxful"],
            "analytics_platforms": ["Dune Analytics", "The Graph", "Etherscan", "Celo Explorer"]
        }
        
        logger.info(f"Initialized African Liquidity Research Framework v{self.methodology_version} with onchain integration")
    
    def load_market_data(self, data_source: Union[str, pd.DataFrame, Dict]) -> Dict:
        """Load market data from various sources including onchain data."""
        logger.info("Loading market data for analysis (including onchain sources)")
        
        if isinstance(data_source, str):
            if data_source.endswith('.csv'):
                data = pd.read_csv(data_source)
            elif data_source.endswith('.json'):
                with open(data_source, 'r') as f:
                    data = json.load(f)
            elif data_source.endswith('.xlsx'):
                data = pd.read_excel(data_source)
            else:
                raise ValueError(f"Unsupported file format: {data_source}")
        elif isinstance(data_source, pd.DataFrame):
            data = data_source.to_dict('records')
        elif isinstance(data_source, dict):
            data = data_source
        else:
            raise TypeError("data_source must be string, DataFrame, or dictionary")
        
        self._validate_market_data(data)
        logger.info(f"Successfully loaded data for {len(data)} markets")
        return data
    
    def _validate_market_data(self, data: Dict) -> None:
        """Validate that market data contains required fields for analysis."""
        # Check if data has the new providers structure
        if "providers" in data:
            logger.info("Detected new providers array structure - validating onchain/offchain data")
            providers = data["providers"]
            
            for provider in providers:
                provider_name = provider.get("name", "Unknown")
                provider_type = provider.get("type", "unknown")
                metrics = provider.get("metrics", {})
                
                logger.info(f"Validating {provider_type} provider: {provider_name}")
                
                if provider_type == "offchain":
                    # Validate traditional metrics
                    required_offchain_fields = ["market_name", "country", "region", "liquidity_sources", "liquidity_volumes"]
                    for field in required_offchain_fields:
                        if field not in metrics:
                            logger.warning(f"Missing offchain field '{field}' for provider {provider_name}")
                
                elif provider_type == "onchain":
                    # Validate onchain metrics
                    required_onchain_fields = ["tvl_usd", "daily_volume_usd", "apy_avg", "cross_chain_transfers", "source"]
                    for field in required_onchain_fields:
                        if field not in metrics:
                            logger.warning(f"Missing onchain field '{field}' for provider {provider_name}")
                    
                    # Check for optional blockchain metrics
                    if "blockchain_metrics" not in metrics:
                        logger.info(f"No detailed blockchain metrics for {provider_name} - will use basic onchain data")
                    if "defi_integration" not in metrics:
                        logger.info(f"No DeFi integration data for {provider_name} - will use basic onchain data")
                
                else:
                    logger.warning(f"Unknown provider type '{provider_type}' for {provider_name}")
        
        else:
            # Fallback to old structure validation
            logger.info("Using legacy data structure validation")
            required_fields = {
                "basic": ["market_name", "country", "region"],
                "liquidity_sourcing": ["liquidity_sources", "liquidity_volumes"],
                "efficiency": ["transaction_metrics", "float_metrics", "agent_network_metrics"],
                "onchain": ["blockchain_metrics", "defi_integration", "cross_chain_efficiency"]
            }
            
            for market_key, market_data in data.items():
                logger.info(f"Validating data for market: {market_data.get('market_name', market_key)}")
                
                for field in required_fields["basic"]:
                    if field not in market_data:
                        logger.warning(f"Missing basic field '{field}' for market {market_key}")
                
                if "liquidity_sources" not in market_data:
                    logger.warning(f"Missing liquidity_sources for market {market_key}")
                if "liquidity_volumes" not in market_data:
                    logger.warning(f"Missing liquidity_volumes for market {market_key}")
                
                if "transaction_metrics" not in market_data:
                    logger.warning(f"Missing transaction_metrics for market {market_key}")
                if "float_metrics" not in market_data:
                    logger.warning(f"Missing float_metrics for market {market_key}")
                if "agent_network_metrics" not in market_data:
                    logger.warning(f"Missing agent_network_metrics for market {market_key}")
                
                # Check for onchain data (optional but recommended)
                if "blockchain_metrics" not in market_data:
                    logger.info(f"No blockchain metrics for market {market_key} - will use traditional analysis")
                if "defi_integration" not in market_data:
                    logger.info(f"No DeFi integration data for market {market_key} - will use traditional analysis")
    
    def _get_providers_data(self, data: Dict) -> List[Dict]:
        """Extract providers data from either new or legacy structure."""
        if "providers" in data:
            return data["providers"]
        else:
            # Convert legacy structure to providers format
            providers = []
            for market_key, market_data in data.items():
                provider_type = "offchain"  # Legacy data is assumed to be offchain
                if "blockchain_metrics" in market_data or "defi_integration" in market_data:
                    provider_type = "hybrid"  # Has both traditional and blockchain data
                
                providers.append({
                    "name": market_data.get("market_name", market_key),
                    "type": provider_type,
                    "metrics": market_data
                })
            return providers
    
    def analyze_liquidity_sourcing(self, market_data: Dict) -> Dict:
        """
        RESEARCH QUESTION 1: Where can and do African payment orchestration companies source liquidity?
        
        Identifies:
        - Primary liquidity sources (banks, agents, users, etc.)
        - Liquidity volume distribution across sources
        - Regional patterns in liquidity sourcing
        - Market maturity impact on sourcing strategies
        """
        logger.info("Analyzing liquidity sourcing patterns across African markets")
        
        sourcing_analysis = {
            "research_question": "Where can and do African payment orchestration companies source liquidity?",
            "analysis_timestamp": self.research_timestamp.isoformat(),
            "methodology": "Source identification and volume analysis by market and region",
            "findings": {},
            "regional_patterns": {},
            "onchain_offchain_comparison": {}
        }
        
        providers = self._get_providers_data(market_data)
        
        for provider in providers:
            provider_name = provider.get("name", "Unknown")
            provider_type = provider.get("type", "unknown")
            metrics = provider.get("metrics", {})
            
            if provider_type == "offchain":
                # Traditional liquidity sourcing analysis
                region = metrics.get("region", "Unknown")
                liquidity_sources = metrics.get("liquidity_sources", [])
                liquidity_volumes = metrics.get("liquidity_volumes", {})
                
                if liquidity_sources and liquidity_volumes:
                    total_volume = sum(liquidity_volumes.values())
                    source_distribution = {
                        source: {
                            "volume": volume,
                            "percentage": (volume / total_volume * 100) if total_volume > 0 else 0
                        }
                        for source, volume in liquidity_volumes.items()
                    }
                    
                    primary_source = max(source_distribution.items(), key=lambda x: x[1]["volume"])[0]
                    
                    sourcing_analysis["findings"][provider_name] = {
                        "provider_type": provider_type,
                        "market_name": provider_name,
                        "region": region,
                        "liquidity_sources": liquidity_sources,
                        "source_distribution": source_distribution,
                        "primary_source": primary_source,
                        "total_liquidity_volume": total_volume
                    }
                    
                    if region not in sourcing_analysis["regional_patterns"]:
                        sourcing_analysis["regional_patterns"][region] = {
                            "markets": [],
                            "common_sources": set(),
                            "total_volume": 0
                        }
                    
                    sourcing_analysis["regional_patterns"][region]["markets"].append(provider_name)
                    sourcing_analysis["regional_patterns"][region]["common_sources"].update(liquidity_sources)
                    sourcing_analysis["regional_patterns"][region]["total_volume"] += total_volume
            
            elif provider_type == "onchain":
                # Onchain liquidity sourcing analysis
                tvl_usd = metrics.get("tvl_usd", 0)
                daily_volume_usd = metrics.get("daily_volume_usd", 0)
                source = metrics.get("source", "Unknown")
                
                sourcing_analysis["findings"][provider_name] = {
                    "provider_type": provider_type,
                    "market_name": provider_name,
                    "region": "Blockchain Network",
                    "liquidity_sources": ["blockchain_tvl", "daily_volume", "cross_chain_transfers"],
                    "source_distribution": {
                        "blockchain_tvl": {"volume": tvl_usd, "percentage": 100},
                        "daily_volume": {"volume": daily_volume_usd, "percentage": 100}
                    },
                    "primary_source": "blockchain_tvl",
                    "total_liquidity_volume": tvl_usd,
                    "onchain_metrics": {
                        "tvl_usd": tvl_usd,
                        "daily_volume_usd": daily_volume_usd,
                        "data_source": source
                    }
                }
                
                # Track onchain vs offchain comparison
                if "onchain" not in sourcing_analysis["onchain_offchain_comparison"]:
                    sourcing_analysis["onchain_offchain_comparison"]["onchain"] = {
                        "providers": [],
                        "total_tvl": 0,
                        "total_daily_volume": 0
                    }
                
                sourcing_analysis["onchain_offchain_comparison"]["onchain"]["providers"].append(provider_name)
                sourcing_analysis["onchain_offchain_comparison"]["onchain"]["total_tvl"] += tvl_usd
                sourcing_analysis["onchain_offchain_comparison"]["onchain"]["total_daily_volume"] += daily_volume_usd
        
        # Process regional patterns
        for region, data in sourcing_analysis["regional_patterns"].items():
            data["common_sources"] = list(data["common_sources"])
            data["market_count"] = len(data["markets"])
            data["avg_volume_per_market"] = data["total_volume"] / data["market_count"] if data["market_count"] > 0 else 0
        
        # Calculate offchain totals for comparison
        offchain_providers = [p for p in providers if p.get("type") == "offchain"]
        if offchain_providers:
            total_offchain_volume = sum(
                sum(provider.get("metrics", {}).get("liquidity_volumes", {}).values())
                for provider in offchain_providers
            )
            sourcing_analysis["onchain_offchain_comparison"]["offchain"] = {
                "providers": [p.get("name") for p in offchain_providers],
                "total_volume": total_offchain_volume
            }
        
        logger.info(f"Completed liquidity sourcing analysis for {len(sourcing_analysis['findings'])} providers")
        return sourcing_analysis
    
    def analyze_liquidity_efficiency(self, market_data: Dict) -> Dict:
        """
        RESEARCH QUESTION 2: How efficiently is this liquidity used?
        
        Measures:
        - Transaction success rates and failure patterns
        - Float turnover and velocity metrics
        - Agent network health and friction points
        - Regional efficiency disparities
        - Onchain efficiency metrics (if available)
        """
        logger.info("Analyzing liquidity efficiency across African markets")
        
        efficiency_analysis = {
            "research_question": "How efficiently is this liquidity used?",
            "analysis_timestamp": self.research_timestamp.isoformat(),
            "methodology": "Multi-dimensional efficiency measurement with regional comparison and onchain integration",
            "market_efficiency": {},
            "regional_comparison": {},
            "efficiency_insights": {},
            "onchain_efficiency": {}
        }
        
        providers = self._get_providers_data(market_data)
        
        for provider in providers:
            provider_name = provider.get("name", "Unknown")
            provider_type = provider.get("type", "unknown")
            metrics = provider.get("metrics", {})
            
            if provider_type == "offchain":
                # Traditional efficiency analysis
                market_name = metrics.get("market_name", provider_name)
                region = metrics.get("region", "Unknown")
                
                transaction_metrics = metrics.get("transaction_metrics", {})
                float_metrics = metrics.get("float_metrics", {})
                agent_network_metrics = metrics.get("agent_network_metrics", {})
                
                if transaction_metrics and float_metrics and agent_network_metrics:
                    efficiency_metrics = self._calculate_efficiency_metrics(
                        transaction_metrics, float_metrics, agent_network_metrics
                    )
                    
                    efficiency_analysis["market_efficiency"][provider_name] = {
                        "provider_type": provider_type,
                        "market_name": market_name,
                        "region": region,
                        "efficiency_metrics": efficiency_metrics,
                        "efficiency_score": self._calculate_overall_efficiency_score(efficiency_metrics),
                        "friction_analysis": self._analyze_agent_frictions(agent_network_metrics)
                    }
            
            elif provider_type == "onchain":
                # Onchain efficiency analysis
                tvl_usd = metrics.get("tvl_usd", 0)
                daily_volume_usd = metrics.get("daily_volume_usd", 0)
                apy_avg = metrics.get("apy_avg", 0)
                cross_chain_transfers = metrics.get("cross_chain_transfers", 0)
                
                # Calculate onchain efficiency metrics
                onchain_efficiency_metrics = {
                    "tvl_efficiency": tvl_usd / 1000000,  # Convert to millions for readability
                    "volume_efficiency": daily_volume_usd / 1000000,
                    "yield_efficiency": apy_avg,
                    "cross_chain_efficiency": cross_chain_transfers / 1000  # Convert to thousands
                }
                
                efficiency_analysis["onchain_efficiency"][provider_name] = {
                    "provider_type": provider_type,
                    "market_name": provider_name,
                    "region": "Blockchain Network",
                    "efficiency_metrics": onchain_efficiency_metrics,
                    "efficiency_score": self._calculate_onchain_efficiency_score(onchain_efficiency_metrics),
                    "blockchain_metrics": metrics.get("blockchain_metrics", {}),
                    "defi_integration": metrics.get("defi_integration", {}),
                    "cross_chain_efficiency": metrics.get("cross_chain_efficiency", {}),
                    "smart_contract_performance": metrics.get("smart_contract_performance", {})
                }
        
        # Process traditional efficiency analysis
        if efficiency_analysis["market_efficiency"]:
            efficiency_analysis["regional_comparison"] = self._compare_regional_efficiency(
                efficiency_analysis["market_efficiency"]
            )
            
            efficiency_analysis["efficiency_insights"] = self._generate_efficiency_insights(
                efficiency_analysis["market_efficiency"],
                efficiency_analysis["regional_comparison"]
            )
        
        # Process onchain efficiency analysis
        if efficiency_analysis["onchain_efficiency"]:
            efficiency_analysis["onchain_insights"] = self._generate_onchain_efficiency_insights(
                efficiency_analysis["onchain_efficiency"]
            )
        
        logger.info(f"Completed efficiency analysis for {len(efficiency_analysis['market_efficiency'])} offchain and {len(efficiency_analysis['onchain_efficiency'])} onchain providers")
        return efficiency_analysis
    
    def analyze_onchain_liquidity_sources(self, market_data: Dict) -> Dict:
        """
        NEW: Analyze onchain liquidity sources and blockchain integration.
        
        Identifies:
        - Blockchain network adoption and transaction volumes
        - DeFi protocol integration and liquidity pools
        - Cross-chain bridge efficiency and costs
        - Smart contract performance and gas optimization
        """
        logger.info("Analyzing onchain liquidity sources and blockchain integration")
        
        onchain_analysis = {
            "research_question": "How do onchain data sources enhance liquidity analysis?",
            "analysis_timestamp": self.research_timestamp.isoformat(),
            "methodology": "Blockchain metrics, DeFi integration, and cross-chain efficiency analysis",
            "blockchain_networks": {},
            "defi_protocols": {},
            "cross_chain_efficiency": {},
            "smart_contract_performance": {},
            "onchain_insights": {}
        }
        
        providers = self._get_providers_data(market_data)
        
        for provider in providers:
            provider_name = provider.get("name", "Unknown")
            provider_type = provider.get("type", "unknown")
            metrics = provider.get("metrics", {})
            
            if provider_type == "onchain":
                # Analyze blockchain metrics if available
                blockchain_metrics = metrics.get("blockchain_metrics", {})
                defi_integration = metrics.get("defi_integration", {})
                
                if blockchain_metrics:
                    onchain_analysis["blockchain_networks"][provider_name] = self._analyze_blockchain_metrics(
                        provider_name, "Blockchain Network", blockchain_metrics
                    )
                
                if defi_integration:
                    onchain_analysis["defi_protocols"][provider_name] = self._analyze_defi_integration(
                        provider_name, "Blockchain Network", defi_integration
                    )
                
                # Analyze cross-chain efficiency
                cross_chain_data = metrics.get("cross_chain_efficiency", {})
                if cross_chain_data:
                    onchain_analysis["cross_chain_efficiency"][provider_name] = self._analyze_cross_chain_efficiency(
                        provider_name, "Blockchain Network", cross_chain_data
                    )
                
                # Analyze smart contract performance
                smart_contract_data = metrics.get("smart_contract_performance", {})
                if smart_contract_data:
                    onchain_analysis["smart_contract_performance"][provider_name] = self._analyze_smart_contract_performance(
                        provider_name, "Blockchain Network", smart_contract_data
                    )
        
        # Generate onchain insights
        onchain_analysis["onchain_insights"] = self._generate_onchain_insights(onchain_analysis)
        
        logger.info(f"Completed onchain analysis for {len(onchain_analysis['blockchain_networks'])} onchain providers")
        return onchain_analysis
    
    def _calculate_efficiency_metrics(self, transaction_metrics: Dict, float_metrics: Dict, agent_network_metrics: Dict) -> Dict:
        """Calculate comprehensive efficiency metrics from raw data."""
        attempted_tx = transaction_metrics.get("attempted", 0)
        successful_tx = transaction_metrics.get("successful", 0)
        failed_tx = transaction_metrics.get("failed", 0)
        
        success_rate = (successful_tx / attempted_tx * 100) if attempted_tx > 0 else 0
        failure_rate = (failed_tx / attempted_tx * 100) if attempted_tx > 0 else 0
        
        total_volume = float_metrics.get("total_volume", 0)
        average_float = float_metrics.get("average_float", 0)
        
        float_turnover = total_volume / average_float if average_float > 0 else 0
        float_velocity = attempted_tx / average_float if average_float > 0 else 0
        
        total_agents = agent_network_metrics.get("total", 0)
        active_agents = agent_network_metrics.get("active", 0)
        liquidity_agents = agent_network_metrics.get("with_liquidity", 0)
        cash_agents = agent_network_metrics.get("with_cash", 0)
        
        agent_utilization = (active_agents / total_agents * 100) if total_agents > 0 else 0
        liquidity_coverage = (liquidity_agents / total_agents * 100) if total_agents > 0 else 0
        cash_coverage = (cash_agents / total_agents * 100) if total_agents > 0 else 0
        
        return {
            "transaction_efficiency": {
                "success_rate": success_rate,
                "failure_rate": failure_rate,
                "attempted_transactions": attempted_tx,
                "successful_transactions": successful_tx,
                "failed_transactions": failed_tx
            },
            "float_efficiency": {
                "turnover": float_turnover,
                "velocity": float_velocity,
                "total_volume": total_volume,
                "average_float": average_float
            },
            "agent_network_efficiency": {
                "utilization_rate": agent_utilization,
                "liquidity_coverage": liquidity_coverage,
                "cash_coverage": cash_coverage,
                "total_agents": total_agents,
                "active_agents": active_agents,
                "liquidity_agents": liquidity_agents,
                "cash_agents": cash_agents
            }
        }
    
    def _calculate_overall_efficiency_score(self, efficiency_metrics: Dict) -> Dict:
        """
        Calculate overall efficiency score (0-100) using weighted methodology.
        
        Weights:
        - Transaction success (40%): Core measure of system reliability
        - Agent network health (35%): Key friction point in African markets
        - Float utilization (25%): Measure of liquidity efficiency
        """
        transaction = efficiency_metrics["transaction_efficiency"]
        float_eff = efficiency_metrics["float_efficiency"]
        agent = efficiency_metrics["agent_network_efficiency"]
        
        transaction_score = transaction["success_rate"]
        agent_score = (agent["utilization_rate"] * 0.4 + 
                      agent["liquidity_coverage"] * 0.4 + 
                      agent["cash_coverage"] * 0.2)
        float_score = min((float_eff["turnover"] / 20) * 100, 100)
        
        overall_score = (
            transaction_score * 0.40 +
            agent_score * 0.35 +
            float_score * 0.25
        )
        
        if overall_score >= 90:
            grade = "A+"
        elif overall_score >= 85:
            grade = "A"
        elif overall_score >= 80:
            grade = "A-"
        elif overall_score >= 75:
            grade = "B+"
        elif overall_score >= 70:
            grade = "B"
        elif overall_score >= 65:
            grade = "B-"
        elif overall_score >= 60:
            grade = "C+"
        elif overall_score >= 55:
            grade = "C"
        elif overall_score >= 50:
            grade = "C-"
        else:
            grade = "F"
        
        return {
            "overall_score": overall_score,
            "grade": grade,
            "component_scores": {
                "transaction": transaction_score,
                "agent_network": agent_score,
                "float_utilization": float_score
            },
            "weights": {
                "transaction": 0.40,
                "agent_network": 0.35,
                "float_utilization": 0.25
            }
        }
    
    def _analyze_agent_frictions(self, agent_network_metrics: Dict) -> Dict:
        """
        Analyze agent network friction points - critical for African markets.
        
        Identifies where service failures occur due to:
        - Insufficient e-float (cash-out failures)
        - Insufficient physical cash (cash-in failures)
        - Agent network underutilization
        """
        total_agents = agent_network_metrics.get("total", 0)
        active_agents = agent_network_metrics.get("active", 0)
        liquidity_agents = agent_network_metrics.get("with_liquidity", 0)
        cash_agents = agent_network_metrics.get("with_cash", 0)
        
        return {
            "friction_points": {
                "low_liquidity_agents": total_agents - liquidity_agents,
                "low_cash_agents": total_agents - cash_agents,
                "inactive_agents": total_agents - active_agents
            },
            "friction_rates": {
                "liquidity_friction_rate": ((total_agents - liquidity_agents) / total_agents * 100) if total_agents > 0 else 0,
                "cash_friction_rate": ((total_agents - cash_agents) / total_agents * 100) if total_agents > 0 else 0,
                "utilization_friction_rate": ((total_agents - active_agents) / total_agents * 100) if total_agents > 0 else 0
            },
            "service_impact": {
                "cash_out_failures_likely": (total_agents - liquidity_agents) > 0,
                "cash_in_failures_likely": (total_agents - cash_agents) > 0,
                "network_underutilization": (total_agents - active_agents) > 0
            }
        }
    
    def _compare_regional_efficiency(self, market_efficiency: Dict) -> Dict:
        """Compare efficiency across regions to identify patterns and disparities."""
        regional_data = {}
        
        for market_key, market_data in market_efficiency.items():
            region = market_data["region"]
            if region not in regional_data:
                regional_data[region] = []
            regional_data[region].append(market_data)
        
        regional_comparison = {}
        for region, markets in regional_data.items():
            if markets:
                avg_success_rate = np.mean([m["efficiency_metrics"]["transaction_efficiency"]["success_rate"] for m in markets])
                avg_agent_health = np.mean([m["efficiency_metrics"]["agent_network_efficiency"]["utilization_rate"] for m in markets])
                avg_float_turnover = np.mean([m["efficiency_metrics"]["float_efficiency"]["turnover"] for m in markets])
                avg_efficiency_score = np.mean([m["efficiency_score"]["overall_score"] for m in markets])
                
                regional_comparison[region] = {
                    "market_count": len(markets),
                    "average_metrics": {
                        "success_rate": avg_success_rate,
                        "agent_utilization": avg_agent_health,
                        "float_turnover": avg_float_turnover,
                        "efficiency_score": avg_efficiency_score
                    },
                    "markets": [m["market_name"] for m in markets]
                }
        
        if len(regional_comparison) > 1:
            regions = list(regional_comparison.keys())
            regional_comparison["disparity_analysis"] = {}
            
            for i, region1 in enumerate(regions):
                for region2 in regions[i+1:]:
                    comparison_key = f"{region1}_vs_{region2}"
                    
                    region1_data = regional_comparison[region1]["average_metrics"]
                    region2_data = regional_comparison[region2]["average_metrics"]
                    
                    regional_comparison["disparity_analysis"][comparison_key] = {
                        "success_rate_gap": region1_data["success_rate"] - region2_data["success_rate"],
                        "agent_health_gap": region1_data["agent_utilization"] - region2_data["agent_utilization"],
                        "float_efficiency_gap": region1_data["float_turnover"] - region2_data["float_turnover"],
                        "overall_efficiency_gap": region1_data["efficiency_score"] - region2_data["efficiency_score"]
                    }
        
        return regional_comparison
    
    def _generate_efficiency_insights(self, market_efficiency: Dict, regional_comparison: Dict) -> Dict:
        """Generate research insights from efficiency analysis."""
        insights = {
            "key_findings": [],
            "regional_patterns": [],
            "efficiency_drivers": []
        }
        
        efficiency_scores = [m["efficiency_score"]["overall_score"] for m in market_efficiency.values()]
        if efficiency_scores:
            insights["key_findings"].append({
                "finding": "Efficiency variation across African markets",
                "evidence": f"Efficiency scores range from {min(efficiency_scores):.1f} to {max(efficiency_scores):.1f}",
                "implication": "Significant variation in liquidity utilization across markets"
            })
        
        if "disparity_analysis" in regional_comparison:
            for comparison, data in regional_comparison["disparity_analysis"].items():
                if abs(data["success_rate_gap"]) > 5:
                    insights["regional_patterns"].append({
                        "pattern": f"Significant success rate gap between {comparison}",
                        "evidence": f"{data['success_rate_gap']:+.1f}% difference",
                        "implication": "Regional factors significantly impact transaction reliability"
                    })
        
        for market_key, market_data in market_efficiency.items():
            friction_analysis = market_data["friction_analysis"]
            if friction_analysis["friction_points"]["low_liquidity_agents"] > 0:
                insights["efficiency_drivers"].append({
                    "driver": "Agent liquidity shortages",
                    "evidence": f"{market_data['market_name']}: {friction_analysis['friction_points']['low_liquidity_agents']} agents lack e-float",
                    "impact": "Cash-out service failures, reduced user trust"
                })
        
        return insights
    
    def _analyze_blockchain_metrics(self, market_name: str, region: str, blockchain_metrics: Dict) -> Dict:
        """Analyze blockchain network metrics for a specific market."""
        return {
            "market_name": market_name,
            "region": region,
            "network_adoption": {
                "celo_transactions": blockchain_metrics.get("celo_daily_tx", 0),
                "stellar_transactions": blockchain_metrics.get("stellar_daily_tx", 0),
                "ethereum_transactions": blockchain_metrics.get("ethereum_daily_tx", 0),
                "polygon_transactions": blockchain_metrics.get("polygon_daily_tx", 0)
            },
            "transaction_efficiency": {
                "avg_gas_fee": blockchain_metrics.get("avg_gas_fee_usd", 0),
                "tx_confirmation_time": blockchain_metrics.get("avg_confirmation_time_seconds", 0),
                "throughput_tps": blockchain_metrics.get("transactions_per_second", 0)
            },
            "liquidity_metrics": {
                "total_value_locked": blockchain_metrics.get("tvl_usd", 0),
                "daily_volume": blockchain_metrics.get("daily_volume_usd", 0),
                "active_addresses": blockchain_metrics.get("active_addresses", 0)
            }
        }
    
    def _analyze_defi_integration(self, market_name: str, region: str, defi_integration: Dict) -> Dict:
        """Analyze DeFi protocol integration for a specific market."""
        return {
            "market_name": market_name,
            "region": region,
            "protocol_adoption": {
                "uniswap_liquidity": defi_integration.get("uniswap_liquidity_usd", 0),
                "aave_deposits": defi_integration.get("aave_deposits_usd", 0),
                "compound_borrowing": defi_integration.get("compound_borrowing_usd", 0),
                "makerdao_collateral": defi_integration.get("makerdao_collateral_usd", 0)
            },
            "yield_metrics": {
                "avg_apy": defi_integration.get("average_apy_percentage", 0),
                "liquidity_mining_rewards": defi_integration.get("liquidity_mining_usd", 0),
                "governance_token_holdings": defi_integration.get("governance_tokens", 0)
            },
            "risk_metrics": {
                "impermanent_loss_risk": defi_integration.get("impermanent_loss_risk_score", 0),
                "smart_contract_risk": defi_integration.get("smart_contract_risk_score", 0),
                "liquidity_depth": defi_integration.get("liquidity_depth_score", 0)
            }
        }
    
    def _analyze_cross_chain_efficiency(self, market_name: str, region: str, cross_chain_data: Dict) -> Dict:
        """Analyze cross-chain bridge efficiency and costs."""
        return {
            "market_name": market_name,
            "region": region,
            "bridge_efficiency": {
                "celo_stellar_bridge": {
                    "transfer_time": cross_chain_data.get("celo_stellar_time_seconds", 0),
                    "transfer_cost": cross_chain_data.get("celo_stellar_cost_usd", 0),
                    "success_rate": cross_chain_data.get("celo_stellar_success_rate", 0)
                },
                "ethereum_polygon_bridge": {
                    "transfer_time": cross_chain_data.get("eth_polygon_time_seconds", 0),
                    "transfer_cost": cross_chain_data.get("eth_polygon_cost_usd", 0),
                    "success_rate": cross_chain_data.get("eth_polygon_success_rate", 0)
                }
            },
            "cross_chain_volume": {
                "daily_bridge_volume": cross_chain_data.get("daily_bridge_volume_usd", 0),
                "monthly_bridge_volume": cross_chain_data.get("monthly_bridge_volume_usd", 0),
                "bridge_fee_revenue": cross_chain_data.get("bridge_fee_revenue_usd", 0)
            }
        }
    
    def _analyze_smart_contract_performance(self, market_name: str, region: str, smart_contract_data: Dict) -> Dict:
        """Analyze smart contract performance and gas optimization."""
        return {
            "market_name": market_name,
            "region": region,
            "gas_efficiency": {
                "avg_gas_used": smart_contract_data.get("average_gas_used", 0),
                "gas_optimization_score": smart_contract_data.get("gas_optimization_score", 0),
                "cost_per_transaction": smart_contract_data.get("cost_per_transaction_usd", 0)
            },
            "contract_performance": {
                "execution_success_rate": smart_contract_data.get("execution_success_rate", 0),
                "average_execution_time": smart_contract_data.get("avg_execution_time_ms", 0),
                "contract_complexity_score": smart_contract_data.get("complexity_score", 0)
            },
            "security_metrics": {
                "audit_score": smart_contract_data.get("audit_score", 0),
                "bug_bounty_program": smart_contract_data.get("bug_bounty_active", False),
                "insurance_coverage": smart_contract_data.get("insurance_coverage_usd", 0)
            }
        }
    
    def _generate_onchain_insights(self, onchain_analysis: Dict) -> Dict:
        """Generate insights from onchain data analysis."""
        insights = {
            "blockchain_adoption_trends": [],
            "defi_integration_opportunities": [],
            "cross_chain_efficiency_gains": [],
            "smart_contract_optimization": []
        }
        
        # Analyze blockchain adoption trends
        if onchain_analysis["blockchain_networks"]:
            total_tvl = sum([
                market["liquidity_metrics"]["total_value_locked"] 
                for market in onchain_analysis["blockchain_networks"].values()
            ])
            
            insights["blockchain_adoption_trends"].append({
                "trend": "Total Value Locked across blockchain networks",
                "evidence": f"${total_tvl:,.0f} TVL across {len(onchain_analysis['blockchain_networks'])} markets",
                "implication": "Significant blockchain adoption in African markets"
            })
        
        # Analyze DeFi integration opportunities
        if onchain_analysis["defi_protocols"]:
            avg_apy = np.mean([
                market["yield_metrics"]["avg_apy"] 
                for market in onchain_analysis["defi_protocols"].values()
                if market["yield_metrics"]["avg_apy"] > 0
            ])
            
            if avg_apy > 0:
                insights["defi_integration_opportunities"].append({
                    "opportunity": "High yield opportunities in DeFi protocols",
                    "evidence": f"Average APY: {avg_apy:.2f}% across DeFi protocols",
                    "implication": "Significant yield farming potential for liquidity providers"
                })
        
        # Analyze cross-chain efficiency gains
        if onchain_analysis["cross_chain_efficiency"]:
            total_bridge_volume = sum([
                market["cross_chain_volume"]["daily_bridge_volume"] 
                for market in onchain_analysis["cross_chain_efficiency"].values()
            ])
            
            insights["cross_chain_efficiency_gains"].append({
                "gain": "Cross-chain liquidity movement",
                "evidence": f"${total_bridge_volume:,.0f} daily bridge volume",
                "implication": "Efficient cross-chain liquidity management"
            })
        
        return insights
    
    def generate_research_report(self, market_data: Dict, output_file: str = None) -> Dict:
        """
        Generate comprehensive research report addressing both LAVA research questions.
        
        Produces methodology and findings for the research document.
        """
        logger.info("Generating comprehensive research report")
        
        liquidity_sourcing_analysis = self.analyze_liquidity_sourcing(market_data)
        efficiency_analysis = self.analyze_liquidity_efficiency(market_data)
        onchain_analysis = self.analyze_onchain_liquidity_sources(market_data)
        
        research_report = {
            "research_metadata": {
                "title": "African Liquidity Markets: Sourcing Patterns and Efficiency Analysis",
                "research_questions": [
                    "Where can and do African payment orchestration companies source liquidity?",
                    "How efficiently is this liquidity used?",
                    "How does onchain data integration enhance liquidity analysis?"
                ],
                "methodology_version": self.methodology_version,
                "analysis_timestamp": self.research_timestamp.isoformat(),
                "providers_analyzed": len(self._get_providers_data(market_data)),
                "data_structure": "New providers array with offchain/onchain classification"
            },
            "methodology": {
                "liquidity_sourcing_methodology": "Source identification and volume analysis by provider type (offchain/onchain) and region",
                "efficiency_measurement_methodology": "Multi-dimensional efficiency measurement with regional comparison and onchain integration",
                "onchain_integration_methodology": "Blockchain metrics, DeFi protocols, cross-chain efficiency, and smart contract performance analysis",
                "data_requirements": "Provider data with type classification (offchain/onchain), traditional metrics, and blockchain metrics",
                "analysis_framework": "Hybrid analysis combining traditional and blockchain efficiency scoring with cross-chain optimization"
            },
            "findings": {
                "liquidity_sourcing": liquidity_sourcing_analysis,
                "efficiency_analysis": efficiency_analysis,
                "onchain_analysis": onchain_analysis
            },
            "conclusions": {
                "liquidity_sourcing_conclusions": self._generate_sourcing_conclusions(liquidity_sourcing_analysis),
                "efficiency_conclusions": self._generate_efficiency_conclusions(efficiency_analysis),
                "onchain_conclusions": self._generate_onchain_conclusions(onchain_analysis)
            }
        }
        
        if output_file:
            with open(output_file, 'w') as f:
                json.dump(research_report, f, indent=2, default=str)
            logger.info(f"Research report saved to {output_file}")
        
        return research_report
    
    def _generate_sourcing_conclusions(self, sourcing_analysis: Dict) -> List[Dict]:
        """Generate conclusions about liquidity sourcing patterns."""
        conclusions = []
        
        if sourcing_analysis["regional_patterns"]:
            for region, data in sourcing_analysis["regional_patterns"].items():
                conclusions.append({
                    "conclusion": f"Regional liquidity sourcing patterns in {region}",
                    "evidence": f"{data['market_count']} markets, {len(data['common_sources'])} common sources",
                    "implication": "Regional coordination opportunities for liquidity management"
                })
        
        return conclusions
    
    def _generate_efficiency_conclusions(self, efficiency_analysis: Dict) -> List[Dict]:
        """Generate conclusions about liquidity efficiency."""
        conclusions = []
        
        if efficiency_analysis["efficiency_insights"]["key_findings"]:
            conclusions.extend(efficiency_analysis["efficiency_insights"]["key_findings"])
        
        if efficiency_analysis["efficiency_insights"]["regional_patterns"]:
            conclusions.extend(efficiency_analysis["efficiency_insights"]["regional_patterns"])
        
        return conclusions
    
    def _generate_onchain_conclusions(self, onchain_analysis: Dict) -> List[Dict]:
        """Generate conclusions about onchain data integration."""
        conclusions = []
        
        if onchain_analysis["onchain_insights"]["blockchain_adoption_trends"]:
            conclusions.extend(onchain_analysis["onchain_insights"]["blockchain_adoption_trends"])
        
        if onchain_analysis["onchain_insights"]["defi_integration_opportunities"]:
            conclusions.extend(onchain_analysis["onchain_insights"]["defi_integration_opportunities"])
        
        if onchain_analysis["onchain_insights"]["cross_chain_efficiency_gains"]:
            conclusions.extend(onchain_analysis["onchain_insights"]["cross_chain_efficiency_gains"])
        
        if onchain_analysis["onchain_insights"]["smart_contract_optimization"]:
            conclusions.extend(onchain_analysis["onchain_insights"]["smart_contract_optimization"])
        
        return conclusions

    def _calculate_onchain_efficiency_score(self, onchain_metrics: Dict) -> float:
        """Calculate overall efficiency score for onchain providers."""
        try:
            # Weighted scoring based on onchain metrics
            tvl_score = min(onchain_metrics.get("tvl_efficiency", 0) / 100, 1.0) * 25  # Max 25 points
            volume_score = min(onchain_metrics.get("volume_efficiency", 0) / 10, 1.0) * 25  # Max 25 points
            yield_score = min(onchain_metrics.get("yield_efficiency", 0) / 15, 1.0) * 25  # Max 25 points
            cross_chain_score = min(onchain_metrics.get("cross_chain_efficiency", 0) / 100, 1.0) * 25  # Max 25 points
            
            total_score = tvl_score + volume_score + yield_score + cross_chain_score
            return round(total_score, 2)
        except Exception as e:
            logger.error(f"Error calculating onchain efficiency score: {e}")
            return 0.0
    
    def _generate_onchain_efficiency_insights(self, onchain_efficiency: Dict) -> Dict:
        """Generate insights from onchain efficiency analysis."""
        insights = {
            "key_findings": [],
            "blockchain_advantages": [],
            "defi_opportunities": [],
            "cross_chain_benefits": []
        }
        
        if not onchain_efficiency:
            return insights
        
        # Analyze TVL efficiency
        total_tvl = sum(provider["efficiency_metrics"]["tvl_efficiency"] for provider in onchain_efficiency.values())
        avg_tvl = total_tvl / len(onchain_efficiency) if onchain_efficiency else 0
        
        insights["key_findings"].append({
            "finding": "Onchain providers show significant TVL efficiency",
            "evidence": f"${total_tvl:.2f}M total TVL across {len(onchain_efficiency)} providers",
            "implication": "High liquidity utilization in blockchain networks"
        })
        
        # Analyze yield efficiency
        total_yield = sum(provider["efficiency_metrics"]["yield_efficiency"] for provider in onchain_efficiency.values())
        avg_yield = total_yield / len(onchain_efficiency) if onchain_efficiency else 0
        
        insights["defi_opportunities"].append({
            "opportunity": "High yield opportunities in DeFi protocols",
            "evidence": f"Average APY: {avg_yield:.2f}% across onchain providers",
            "implication": "Significant yield farming potential for liquidity providers"
        })
        
        # Analyze cross-chain efficiency
        total_cross_chain = sum(provider["efficiency_metrics"]["cross_chain_efficiency"] for provider in onchain_efficiency.values())
        
        insights["cross_chain_benefits"].append({
            "benefit": "Efficient cross-chain liquidity movement",
            "evidence": f"{total_cross_chain:.0f}K daily cross-chain transfers",
            "implication": "Seamless liquidity flow across blockchain networks"
        })
        
        return insights

if __name__ == "__main__":
    print("🔬 LAVA RESEARCH METHODOLOGY: African Liquidity Analysis Framework")
    print("=" * 80)
    print("This framework provides the methodology for investigating:")
    print("1. Where African payment orchestration companies source liquidity")
    print("2. How efficiently this liquidity is used")
    print("\nTo use this framework:")
    print("1. Prepare market data in the required format")
    print("2. Initialize the framework: framework = AfricanLiquidityResearchFramework()")
    print("3. Load your data: framework.load_market_data(your_data)")
    print("4. Generate research report: framework.generate_research_report(market_data)")
    print("\nThe framework will produce methodology-compliant analysis addressing both research questions.")
