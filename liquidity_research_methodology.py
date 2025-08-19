"""
LAVA Research Methodology: African Liquidity Analysis Framework

This framework provides the methodology for investigating:
1. Where African payment orchestration companies source liquidity
2. How efficiently this liquidity is used

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
    """
    
    def __init__(self):
        self.research_timestamp = datetime.now()
        self.methodology_version = "1.0"
        
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
        """Validate that market data contains required fields for analysis."""
        required_fields = {
            "basic": ["market_name", "country", "region"],
            "liquidity_sourcing": ["liquidity_sources", "liquidity_volumes"],
            "efficiency": ["transaction_metrics", "float_metrics", "agent_network_metrics"]
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
            "regional_patterns": {}
        }
        
        for market_key, market_data in market_data.items():
            market_name = market_data.get("market_name", market_key)
            region = market_data.get("region", "Unknown")
            
            liquidity_sources = market_data.get("liquidity_sources", [])
            liquidity_volumes = market_data.get("liquidity_volumes", {})
            
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
                
                sourcing_analysis["findings"][market_key] = {
                    "market_name": market_name,
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
                
                sourcing_analysis["regional_patterns"][region]["markets"].append(market_key)
                sourcing_analysis["regional_patterns"][region]["common_sources"].update(liquidity_sources)
                sourcing_analysis["regional_patterns"][region]["total_volume"] += total_volume
        
        for region, data in sourcing_analysis["regional_patterns"].items():
            data["common_sources"] = list(data["common_sources"])
            data["market_count"] = len(data["markets"])
            data["avg_volume_per_market"] = data["total_volume"] / data["market_count"] if data["market_count"] > 0 else 0
        
        logger.info(f"Completed liquidity sourcing analysis for {len(sourcing_analysis['findings'])} markets")
        return sourcing_analysis
    
    def analyze_liquidity_efficiency(self, market_data: Dict) -> Dict:
        """
        RESEARCH QUESTION 2: How efficiently is this liquidity used?
        
        Measures:
        - Transaction success rates and failure patterns
        - Float turnover and velocity metrics
        - Agent network health and friction points
        - Regional efficiency disparities
        """
        logger.info("Analyzing liquidity efficiency across African markets")
        
        efficiency_analysis = {
            "research_question": "How efficiently is this liquidity used?",
            "analysis_timestamp": self.research_timestamp.isoformat(),
            "methodology": "Multi-dimensional efficiency measurement with regional comparison",
            "market_efficiency": {},
            "regional_comparison": {},
            "efficiency_insights": {}
        }
        
        for market_key, market_data in market_data.items():
            market_name = market_data.get("market_name", market_key)
            region = market_data.get("region", "Unknown")
            
            transaction_metrics = market_data.get("transaction_metrics", {})
            float_metrics = market_data.get("float_metrics", {})
            agent_network_metrics = market_data.get("agent_network_metrics", {})
            
            if transaction_metrics and float_metrics and agent_network_metrics:
                efficiency_metrics = self._calculate_efficiency_metrics(
                    transaction_metrics, float_metrics, agent_network_metrics
                )
                
                efficiency_analysis["market_efficiency"][market_key] = {
                    "market_name": market_name,
                    "region": region,
                    "efficiency_metrics": efficiency_metrics,
                    "efficiency_score": self._calculate_overall_efficiency_score(efficiency_metrics),
                    "friction_analysis": self._analyze_agent_frictions(agent_network_metrics)
                }
        
        efficiency_analysis["regional_comparison"] = self._compare_regional_efficiency(
            efficiency_analysis["market_efficiency"]
        )
        
        efficiency_analysis["efficiency_insights"] = self._generate_efficiency_insights(
            efficiency_analysis["market_efficiency"],
            efficiency_analysis["regional_comparison"]
        )
        
        logger.info(f"Completed efficiency analysis for {len(efficiency_analysis['market_efficiency'])} markets")
        return efficiency_analysis
    
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
    
    def generate_research_report(self, market_data: Dict, output_file: str = None) -> Dict:
        """
        Generate comprehensive research report addressing both LAVA research questions.
        
        Produces methodology and findings for the research document.
        """
        logger.info("Generating comprehensive research report")
        
        liquidity_sourcing_analysis = self.analyze_liquidity_sourcing(market_data)
        efficiency_analysis = self.analyze_liquidity_efficiency(market_data)
        
        research_report = {
            "research_metadata": {
                "title": "African Liquidity Markets: Sourcing Patterns and Efficiency Analysis",
                "research_questions": [
                    "Where can and do African payment orchestration companies source liquidity?",
                    "How efficiently is this liquidity used?"
                ],
                "methodology_version": self.methodology_version,
                "analysis_timestamp": self.research_timestamp.isoformat(),
                "markets_analyzed": len(market_data)
            },
            "methodology": {
                "liquidity_sourcing_methodology": "Source identification and volume analysis by market and region",
                "efficiency_measurement_methodology": "Multi-dimensional efficiency measurement with regional comparison",
                "data_requirements": "Market data with transaction metrics, float metrics, agent network metrics, and liquidity sourcing information",
                "analysis_framework": "Regional comparison with efficiency scoring and friction point identification"
            },
            "findings": {
                "liquidity_sourcing": liquidity_sourcing_analysis,
                "efficiency_analysis": efficiency_analysis
            },
            "conclusions": {
                "liquidity_sourcing_conclusions": self._generate_sourcing_conclusions(liquidity_sourcing_analysis),
                "efficiency_conclusions": self._generate_efficiency_conclusions(efficiency_analysis)
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
