"""
LAVA Research Methodology: African Liquidity Efficiency Analysis

Focused framework for calculating liquidity efficiency in African markets.
"""

import pandas as pd
import numpy as np
from datetime import datetime
import json
from typing import Dict, List, Union
import logging

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class AfricanLiquidityResearchFramework:
    """Research framework for analyzing African liquidity efficiency."""
    
    def __init__(self):
        self.research_timestamp = datetime.now()
        self.methodology_version = "2.0"
        logger.info(f"Initialized African Liquidity Research Framework v{self.methodology_version}")
    
    def load_market_data(self, data_source: Union[str, pd.DataFrame, Dict]) -> Dict:
        """Load market data from various sources."""
        logger.info("Loading market data for analysis")
        
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
        """Validate market data contains required fields."""
        if "providers" in data:
            providers = data["providers"]
            for provider in providers:
                provider_type = provider.get("type", "unknown")
                metrics = provider.get("metrics", {})
                
                if provider_type == "offchain":
                    required_fields = ["transaction_metrics", "float_metrics", "agent_network_metrics"]
                    for field in required_fields:
                        if field not in metrics:
                            logger.warning(f"Missing field '{field}' for provider {provider.get('name', 'Unknown')}")
                elif provider_type == "onchain":
                    required_fields = ["tvl_usd", "daily_volume_usd", "apy_avg"]
                    for field in required_fields:
                        if field not in metrics:
                            logger.warning(f"Missing field '{field}' for provider {provider.get('name', 'Unknown')}")
    
    def _get_providers_data(self, data: Dict) -> List[Dict]:
        """Extract providers data from data structure."""
        if "providers" in data:
            return data["providers"]
        else:
            # Convert legacy structure
            providers = []
            for market_key, market_data in data.items():
                provider_type = "offchain"
                if "blockchain_metrics" in market_data:
                    provider_type = "hybrid"
                
                providers.append({
                    "name": market_data.get("market_name", market_key),
                    "type": provider_type,
                    "metrics": market_data
                })
            return providers
    
    def analyze_liquidity_efficiency(self, market_data: Dict) -> Dict:
        """Calculate liquidity efficiency for all providers."""
        logger.info("Analyzing liquidity efficiency across African markets")
        
        efficiency_analysis = {
            "research_question": "How efficiently is this liquidity used?",
            "analysis_timestamp": self.research_timestamp.isoformat(),
            "methodology": "Multi-dimensional efficiency measurement with regional comparison",
            "market_efficiency": {},
            "onchain_efficiency": {},
            "regional_comparison": {},
            "efficiency_insights": {}
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
                
                onchain_efficiency_metrics = {
                    "tvl_efficiency": tvl_usd / 1000000,
                    "volume_efficiency": daily_volume_usd / 1000000,
                    "yield_efficiency": apy_avg,
                    "cross_chain_efficiency": metrics.get("cross_chain_transfers", 0) / 1000
                }
                
                efficiency_analysis["onchain_efficiency"][provider_name] = {
                    "provider_type": provider_type,
                    "market_name": provider_name,
                    "region": "Blockchain Network",
                    "efficiency_metrics": onchain_efficiency_metrics,
                    "efficiency_score": self._calculate_onchain_efficiency_score(onchain_efficiency_metrics)
                }
        
        # Process regional comparison
        if efficiency_analysis["market_efficiency"]:
            efficiency_analysis["regional_comparison"] = self._compare_regional_efficiency(
                efficiency_analysis["market_efficiency"]
            )
            
            efficiency_analysis["efficiency_insights"] = self._generate_efficiency_insights(
                efficiency_analysis["market_efficiency"],
                efficiency_analysis["regional_comparison"]
            )
        
        logger.info(f"Completed efficiency analysis for {len(efficiency_analysis.get('market_efficiency', {}))} providers")
        return efficiency_analysis
    
    def _calculate_efficiency_metrics(self, transaction_metrics: Dict, float_metrics: Dict, agent_network_metrics: Dict) -> Dict:
        """Calculate comprehensive efficiency metrics."""
        # Transaction efficiency
        attempted_tx = transaction_metrics.get("attempted", 0)
        successful_tx = transaction_metrics.get("successful", 0)
        success_rate = (successful_tx / attempted_tx * 100) if attempted_tx > 0 else 0
        
        # Float efficiency
        total_volume = float_metrics.get("total_volume", 0)
        average_float = float_metrics.get("average_float", 0)
        float_turnover = total_volume / average_float if average_float > 0 else 0
        
        # Agent network efficiency
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
                "attempted_transactions": attempted_tx,
                "successful_transactions": successful_tx
            },
            "float_efficiency": {
                "turnover": float_turnover,
                "total_volume": total_volume,
                "average_float": average_float
            },
            "agent_network_efficiency": {
                "utilization_rate": agent_utilization,
                "liquidity_coverage": liquidity_coverage,
                "cash_coverage": cash_coverage,
                "total_agents": total_agents,
                "active_agents": active_agents
            }
        }
    
    def _calculate_overall_efficiency_score(self, efficiency_metrics: Dict) -> Dict:
        """Calculate overall efficiency score (0-100) using weighted methodology."""
        transaction = efficiency_metrics["transaction_efficiency"]
        float_eff = efficiency_metrics["float_efficiency"]
        agent = efficiency_metrics["agent_network_efficiency"]
        
        # Weighted scoring: Transaction (40%), Agent Network (35%), Float (25%)
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
        
        # Grade assignment
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
            }
        }
    
    def _analyze_agent_frictions(self, agent_network_metrics: Dict) -> Dict:
        """Analyze agent network friction points."""
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
        """Compare efficiency across regions."""
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
        
        for market_key, market_data in market_efficiency.items():
            friction_analysis = market_data["friction_analysis"]
            if friction_analysis["friction_points"]["low_liquidity_agents"] > 0:
                insights["efficiency_drivers"].append({
                    "driver": "Agent liquidity shortages",
                    "evidence": f"{market_data['market_name']}: {friction_analysis['friction_points']['low_liquidity_agents']} agents lack e-float",
                    "impact": "Cash-out service failures, reduced user trust"
                })
        
        return insights
    
    def _calculate_onchain_efficiency_score(self, onchain_metrics: Dict) -> float:
        """Calculate efficiency score for onchain providers."""
        try:
            tvl_score = min(onchain_metrics.get("tvl_efficiency", 0) / 100, 1.0) * 25
            volume_score = min(onchain_metrics.get("volume_efficiency", 0) / 10, 1.0) * 25
            yield_score = min(onchain_metrics.get("yield_efficiency", 0) / 15, 1.0) * 25
            cross_chain_score = min(onchain_metrics.get("cross_chain_efficiency", 0) / 100, 1.0) * 25
            
            total_score = tvl_score + volume_score + yield_score + cross_chain_score
            return round(total_score, 2)
        except Exception as e:
            logger.error(f"Error calculating onchain efficiency score: {e}")
            return 0.0

if __name__ == "__main__":
    print("🔬 LAVA RESEARCH METHODOLOGY: African Liquidity Efficiency Analysis")
    print("=" * 80)
    print("This framework calculates liquidity efficiency for African markets.")
    print("\nTo use this framework:")
    print("1. Initialize: framework = AfricanLiquidityResearchFramework()")
    print("2. Load data: framework.load_market_data(your_data)")
    print("3. Calculate efficiency: framework.analyze_liquidity_efficiency(market_data)")
    print("\nThe framework will produce efficiency scores and regional comparisons.")