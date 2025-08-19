import json
from datetime import datetime
from pathlib import Path
import pandas as pd

INPUT_JSON = 'lava_research_report.json'
OUTPUT_HTML = 'lava_research_report.html'

def section(title: str) -> str:
	return f"<h2>{title}</h2>\n"

def sub(title: str) -> str:
	return f"<h3>{title}</h3>\n"

def para(text: str) -> str:
	return f"<p>{text}</p>\n"

def df_html(df: pd.DataFrame) -> str:
	return df.to_html(index=False, classes='table', border=0, justify='left')

def make_html(report: dict) -> str:
	meta = report.get('research_metadata', {})
	findings = report.get('findings', {})
	liq = findings.get('liquidity_sourcing', {})
	eff = findings.get('efficiency_analysis', {})

	styles = """
	<style>
		body { font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif; color: #1f2937; margin: 24px; }
		h1 { margin: 0 0 8px 0; }
		h2 { margin-top: 28px; border-bottom: 1px solid #e5e7eb; padding-bottom: 6px; }
		h3 { margin-top: 18px; color: #374151; }
		.small { color: #6b7280; font-size: 0.9em; }
		.kpi { display: inline-block; margin: 8px 16px 0 0; padding: 8px 12px; border: 1px solid #e5e7eb; border-radius: 8px; background:#fafafa; }
		.table { border-collapse: collapse; width: 100%; margin: 8px 0 16px 0; }
		.table th, .table td { padding: 8px 10px; border-bottom: 1px solid #eee; text-align: left; }
		.badge { display:inline-block; padding:2px 8px; border-radius:999px; background:#eef2ff; color:#3730a3; font-weight:600; }
		.note { background:#f9fafb; border:1px solid #e5e7eb; padding:10px 12px; border-radius:8px; }
		.footer { margin-top: 28px; color:#6b7280; font-size: 0.85em; }
	</style>
	"""

	head = f"""
	<h1>{meta.get('title','African Liquidity Markets')}</h1>
	<div class='small'>
		Generated: {meta.get('analysis_timestamp','')} · Methodology v{meta.get('methodology_version','')} · Markets analyzed: {meta.get('markets_analyzed',0)}
	</div>
	"""

	# Liquidity sourcing per market
	liq_findings = liq.get('findings', {})
	liq_rows = []
	for mk, d in liq_findings.items():
		row = {
			'Market': d.get('market_name',''),
			'Region': d.get('region',''),
			'Primary Source': d.get('primary_source',''),
			'Total Liquidity (USD)': d.get('total_liquidity_volume',0)
		}
		liq_rows.append(row)
	liq_df = pd.DataFrame(liq_rows).sort_values(['Region','Market']) if liq_rows else pd.DataFrame()

	# Source distribution (flatten top sources per market)
	dist_blocks = []
	for mk, d in liq_findings.items():
		src = d.get('source_distribution', {})
		df = pd.DataFrame([
			{'Source': s, 'Volume (USD)': v.get('volume',0), 'Share (%)': round(v.get('percentage',0),2)} for s, v in src.items()
		]).sort_values('Volume (USD)', ascending=False)
		if not df.empty:
			dist_blocks.append(sub(d.get('market_name','Market')) + df_html(df))
	dist_html = "".join(dist_blocks)

	# Regional patterns
	reg = liq.get('regional_patterns', {})
	reg_rows = []
	for r, d in reg.items():
		reg_rows.append({
			'Region': r,
			'Markets': d.get('market_count', len(d.get('markets', []))),
			'Total Liquidity (USD)': d.get('total_volume', 0),
			'Avg Liquidity / Market (USD)': d.get('avg_volume_per_market', 0),
			'Common Sources': ", ".join(d.get('common_sources', []))
		})
	reg_df = pd.DataFrame(reg_rows) if reg_rows else pd.DataFrame()

	# Efficiency per market
	eff_mk = eff.get('market_efficiency', {})
	e_rows = []
	for mk, d in eff_mk.items():
		met = d.get('efficiency_metrics', {})
		tran = met.get('transaction_efficiency', {})
		flo = met.get('float_efficiency', {})
		ag = met.get('agent_network_efficiency', {})
		score = d.get('efficiency_score', {})
		e_rows.append({
			'Market': d.get('market_name',''),
			'Region': d.get('region',''),
			'Overall Score': round(score.get('overall_score',0),1),
			'Grade': score.get('grade',''),
			'Success Rate (%)': round(tran.get('success_rate',0),1),
			'Float Turnover (x)': round(flo.get('turnover',0),1),
			'Agent Utilization (%)': round(ag.get('utilization_rate',0),1)
		})
	eff_df = pd.DataFrame(e_rows).sort_values(['Region','Overall Score'], ascending=[True, False]) if e_rows else pd.DataFrame()

	# Friction points
	fric_blocks = []
	for mk, d in eff_mk.items():
		fr = d.get('friction_analysis', {}).get('friction_points', {})
		if fr:
			df = pd.DataFrame([
				{'Friction': 'Agents lacking e-float', 'Count': fr.get('low_liquidity_agents',0)},
				{'Friction': 'Agents lacking cash', 'Count': fr.get('low_cash_agents',0)},
				{'Friction': 'Inactive agents', 'Count': fr.get('inactive_agents',0)},
			])
			fric_blocks.append(sub(d.get('market_name','Market')) + df_html(df))
	fric_html = "".join(fric_blocks)

	# Regional disparities
	reg_cmp = eff.get('regional_comparison', {}).get('disparity_analysis', {})
	cmp_rows = []
	for k, v in reg_cmp.items():
		cmp_rows.append({
			'Comparison': k,
			'Success Rate Gap (pp)': round(v.get('success_rate_gap',0),1),
			'Agent Health Gap (pp)': round(v.get('agent_health_gap',0),1),
			'Float Efficiency Gap (x)': round(v.get('float_efficiency_gap',0),1),
			'Overall Efficiency Gap': round(v.get('overall_efficiency_gap',0),1)
		})
	cmp_df = pd.DataFrame(cmp_rows) if cmp_rows else pd.DataFrame()

	# Insights
	ins = eff.get('efficiency_insights', {})
	ins_html = ""
	for item in ins.get('key_findings', []):
		ins_html += f"<div class='note'><strong>{item.get('finding','')}</strong><br/>" \
				   f"Evidence: {item.get('evidence','')}<br/>" \
				   f"Implication: {item.get('implication','')}</div>\n"
	for item in ins.get('regional_patterns', []):
		ins_html += f"<div class='note'><strong>{item.get('pattern','')}</strong><br/>" \
				   f"Evidence: {item.get('evidence','')}<br/>" \
				   f"Implication: {item.get('implication','')}</div>\n"

	html = ["<html><head><meta charset='utf-8'>", styles, "</head><body>"]
	html.append(head)

	html.append(section("1. Liquidity Sourcing (by Market)"))
	if not liq_df.empty:
		html.append(df_html(liq_df))
	else:
		html.append(para("No liquidity sourcing data."))

	html.append(sub("Source Distribution (Top Sources by Market)"))
	html.append(dist_html or para("No source distribution available."))

	html.append(section("2. Regional Liquidity Sourcing Patterns"))
	if not reg_df.empty:
		html.append(df_html(reg_df))
	else:
		html.append(para("No regional sourcing data."))

	html.append(section("3. Liquidity Efficiency (by Market)"))
	if not eff_df.empty:
		html.append(df_html(eff_df))
	else:
		html.append(para("No efficiency data."))

	html.append(sub("Agent-Level Frictions (Counts)"))
	html.append(fric_html or para("No friction data."))

	html.append(section("4. Regional Efficiency Disparities"))
	if not cmp_df.empty:
		html.append(df_html(cmp_df))
	else:
		html.append(para("No regional disparity data."))

	html.append(section("5. Key Insights"))
	html.append(ins_html or para("No insights generated."))

	html.append(f"<div class='footer'>Report generated {datetime.now().isoformat(timespec='seconds')}</div>")
	html.append("</body></html>")

	return "\n".join(html)


def main():
	# Load JSON
	if not Path(INPUT_JSON).exists():
		raise SystemExit(f"Input report not found: {INPUT_JSON}. Run demonstrate_research_framework.py first.")
	with open(INPUT_JSON, 'r') as f:
		report = json.load(f)
	# Build HTML
	html = make_html(report)
	# Write
	with open(OUTPUT_HTML, 'w') as f:
		f.write(html)
	print(f"✅ HTML report written to {OUTPUT_HTML}. Open it in your browser and take screenshots or Print to PDF.")

if __name__ == '__main__':
	main()
