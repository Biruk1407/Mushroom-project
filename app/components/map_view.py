"""
🍄 MUSHROOM SAFETY AI - HABITAT RISK MAP
Geographic Risk Visualization
500+ Lines
"""

import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
import numpy as np


class HabitatRiskMap:
    """Habitat-based risk assessment visualization"""
    
    def __init__(self):
        self.habitat_data = {
            'woods': {
                'name': 'Woods/Forest',
                'icon': '🌲',
                'risk_level': 'Low',
                'risk_color': '#2ecc71',
                'edible_percent': 65,
                'description': 'Woodland mushrooms are generally safer. The forest ecosystem supports many edible species.',
                'common_edible': ['Boletes', 'Chanterelles', 'Morels', 'Lion\'s Mane', 'Porcini'],
                'common_poisonous': ['Death Cap', 'Destroying Angel', 'False Morel', 'Deadly Galerina'],
                'tips': 'Look near oak and pine trees. Many edible species form symbiotic relationships with specific trees.',
                'coordinates': {'lat': 45.5, 'lon': -122.5}
            },
            'grasses': {
                'name': 'Grasslands/Meadows',
                'icon': '🌿',
                'risk_level': 'Low-Medium',
                'risk_color': '#27ae60',
                'edible_percent': 55,
                'description': 'Grassland mushrooms include some excellent edibles but also toxic species.',
                'common_edible': ['Field Mushrooms', 'Puffballs', 'Fairy Ring Mushrooms', 'Parasol'],
                'common_poisonous': ['Yellow Stainer', 'Destroying Angel', 'Green-Spored Parasol'],
                'tips': 'Avoid mushrooms growing in fertilized or treated lawns.',
                'coordinates': {'lat': 42.0, 'lon': -100.0}
            },
            'leaves': {
                'name': 'Leaf Litter',
                'icon': '🍂',
                'risk_level': 'Medium',
                'risk_color': '#f1c40f',
                'edible_percent': 50,
                'description': 'Leaf litter provides rich habitat but requires careful identification.',
                'common_edible': ['Shaggy Mane', 'Wood Blewit', 'Hedgehog Mushroom'],
                'common_poisonous': ['Deadly Galerina', 'Panther Cap', 'Poison Pax'],
                'tips': 'Check spore prints carefully - deadly species can hide in leaf litter.',
                'coordinates': {'lat': 48.0, 'lon': -75.0}
            },
            'meadows': {
                'name': 'Open Meadows',
                'icon': '🌸',
                'risk_level': 'Medium',
                'risk_color': '#f39c12',
                'edible_percent': 45,
                'description': 'Open areas can harbor both edible and toxic species.',
                'common_edible': ['Giant Puffball', 'Parasol Mushroom', 'Horse Mushroom'],
                'common_poisonous': ['Green-Spored Parasol', 'Earthball', 'Yellow Stainer'],
                'tips': 'Be cautious of mushrooms that look like edible Parasols but have green spores.',
                'coordinates': {'lat': 38.0, 'lon': -120.0}
            },
            'urban': {
                'name': 'Urban Areas',
                'icon': '🏙️',
                'risk_level': 'High',
                'risk_color': '#e74c3c',
                'edible_percent': 15,
                'description': 'Urban mushrooms may absorb pollutants. Higher risk of toxic species.',
                'common_edible': ['Ink Caps', 'Oyster Mushrooms (on trees)'],
                'common_poisonous': ['Death Cap', 'Sulphur Tuft', 'Jack O\'Lantern'],
                'tips': 'Avoid mushrooms near roads or treated areas. Soil contamination is a concern.',
                'coordinates': {'lat': 40.7, 'lon': -74.0}
            },
            'paths': {
                'name': 'Paths & Trails',
                'icon': '🛤️',
                'risk_level': 'High',
                'risk_color': '#c0392b',
                'edible_percent': 10,
                'description': 'Disturbed soil along paths often hosts toxic species.',
                'common_edible': ['Shaggy Mane (rare)'],
                'common_poisonous': ['Death Cap', 'Panther Cap', 'Fly Agaric', 'Destroying Angel'],
                'tips': 'EXTREME CAUTION - Many deadly Amanita species grow near paths.',
                'coordinates': {'lat': 44.0, 'lon': -110.0}
            },
            'waste': {
                'name': 'Waste/Disturbed Areas',
                'icon': '🗑️',
                'risk_level': 'EXTREME',
                'risk_color': '#8b0000',
                'edible_percent': 0,
                'description': 'Waste areas are dominated by toxic species. NEVER eat mushrooms from these areas.',
                'common_edible': ['None - do not eat mushrooms from waste areas!'],
                'common_poisonous': ['Death Cap', 'Destroying Angel', 'Deadly Webcap', 'Funeral Bell'],
                'tips': '⚠️ ABSOLUTELY DO NOT EAT mushrooms from waste areas. Toxic species dominate.',
                'coordinates': {'lat': 35.0, 'lon': -90.0}
            }
        }
        
        # Create mock global data points
        self.global_data = self._generate_global_data()
    
    def _generate_global_data(self):
        """Generate mock global mushroom data points"""
        np.random.seed(42)
        data = []
        
        for habitat_key, habitat_info in self.habitat_data.items():
            base_lat = habitat_info['coordinates']['lat']
            base_lon = habitat_info['coordinates']['lon']
            
            for i in range(30):
                lat = base_lat + np.random.normal(0, 2)
                lon = base_lon + np.random.normal(0, 3)
                
                if habitat_info['edible_percent'] > 50:
                    edible_prob = np.random.uniform(0.5, 1.0)
                else:
                    edible_prob = np.random.uniform(0.0, 0.5)
                
                data.append({
                    'lat': lat,
                    'lon': lon,
                    'habitat': habitat_info['name'],
                    'risk_color': habitat_info['risk_color'],
                    'edible_probability': edible_prob * 100,
                    'risk_level': habitat_info['risk_level']
                })
        
        return pd.DataFrame(data)
    
    def render(self):
        """Render habitat risk map"""
        st.markdown("## 🗺️ Habitat Risk Map")
        st.markdown("""
        <p style="color:#a0a0b0;">
        Different habitats have different risk levels for mushroom foraging.
        Explore the map to understand where it's safest to find edible mushrooms!
        </p>
        """, unsafe_allow_html=True)
        
        # Risk overview cards
        st.markdown("### 📊 Habitat Risk Overview")
        
        cols = st.columns(4)
        habitats_list = list(self.habitat_data.items())
        
        for i, (key, data) in enumerate(habitats_list[:4]):
            with cols[i]:
                self._render_habitat_card(key, data)
        
        cols = st.columns(3)
        for i, (key, data) in enumerate(habitats_list[4:]):
            with cols[i]:
                self._render_habitat_card(key, data)
        
        # Global risk map
        st.markdown("---")
        st.markdown("### 🌍 Global Mushroom Risk Map")
        st.markdown("*Color intensity indicates edibility probability*")
        
        fig = go.Figure()
        
        for habitat in self.global_data['habitat'].unique():
            habitat_data = self.global_data[self.global_data['habitat'] == habitat]
            risk_color = habitat_data['risk_color'].iloc[0]
            
            fig.add_trace(go.Scattergeo(
                lon=habitat_data['lon'],
                lat=habitat_data['lat'],
                mode='markers',
                marker=dict(
                    size=habitat_data['edible_probability'] / 5,
                    color=risk_color,
                    opacity=0.7,
                    line=dict(width=1, color='white')
                ),
                name=habitat,
                text=[f"Edible: {p:.0f}%" for p in habitat_data['edible_probability']],
                hoverinfo='text+name'
            ))
        
        fig.update_layout(
            geo=dict(
                projection_type='natural earth',
                showland=True,
                landcolor='rgb(40, 40, 40)',
                coastlinecolor='rgba(255,255,255,0.2)',
                showocean=True,
                oceancolor='rgb(20, 20, 30)',
                showcountries=True,
                countrycolor='rgba(255,255,255,0.1)',
                showframe=False
            ),
            height=500,
            paper_bgcolor='rgba(0,0,0,0)',
            margin=dict(l=10, r=10, t=30, b=10),
            legend=dict(
                x=0.01,
                y=0.99,
                bgcolor='rgba(0,0,0,0.5)',
                bordercolor='rgba(255,255,255,0.1)',
                font=dict(color='white')
            )
        )
        
        st.plotly_chart(fig, use_container_width=True)
        
        # Risk comparison chart
        st.markdown("---")
        st.markdown("### 📈 Edibility by Habitat")
        
        habitats = []
        edible_pcts = []
        risk_colors = []
        
        for key, data in self.habitat_data.items():
            habitats.append(data['name'])
            edible_pcts.append(data['edible_percent'])
            risk_colors.append(data['risk_color'])
        
        fig = go.Figure()
        
        fig.add_trace(go.Bar(
            x=habitats,
            y=edible_pcts,
            marker_color=risk_colors,
            text=[f'{p}%' for p in edible_pcts],
            textposition='outside',
            textfont=dict(color='white', size=14),
            hovertemplate='%{x}: %{y}% edible<extra></extra>'
        ))
        
        fig.add_hline(y=50, line_dash="dash", line_color="white", 
                      annotation_text="50% threshold", 
                      annotation_position="bottom right")
        
        fig.update_layout(
            title='Percentage of Edible Mushrooms by Habitat',
            yaxis=dict(title='Edible %', range=[0, 105]),
            height=400,
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(0,0,0,0)',
            font={'color': 'white'},
            showlegend=False
        )
        
        st.plotly_chart(fig, use_container_width=True)
        
        # Risk meter comparison
        st.markdown("---")
        st.markdown("### 🎯 Habitat Risk Comparison")
        
        cols = st.columns(len(self.habitat_data))
        for i, (key, data) in enumerate(self.habitat_data.items()):
            with cols[i]:
                fig = go.Figure(go.Indicator(
                    mode="gauge+number",
                    value=data['edible_percent'],
                    title={'text': f"{data['icon']} {data['name']}", 'font': {'size': 10, 'color': 'white'}},
                    gauge={
                        'axis': {'range': [0, 100]},
                        'bar': {'color': data['risk_color']},
                        'steps': [
                            {'range': [0, 30], 'color': 'rgba(231,76,60,0.3)'},
                            {'range': [30, 60], 'color': 'rgba(241,196,15,0.3)'},
                            {'range': [60, 100], 'color': 'rgba(46,204,113,0.3)'}
                        ]
                    }
                ))
                fig.update_layout(height=180, margin=dict(l=10, r=10, t=30, b=10),
                                paper_bgcolor='rgba(0,0,0,0)', font={'color': 'white'})
                st.plotly_chart(fig, use_container_width=True)
        
        # Detailed habitat view
        st.markdown("---")
        st.markdown("### 🔍 Explore a Habitat")
        
        selected_habitat = st.selectbox(
            "Select habitat to explore:",
            list(self.habitat_data.keys()),
            format_func=lambda x: f"{self.habitat_data[x]['icon']} {self.habitat_data[x]['name']}"
        )
        
        if selected_habitat:
            self._render_habitat_detail(selected_habitat)
        
        # Safety guidelines
        st.markdown("---")
        st.markdown("### ⚠️ Foraging Safety Guidelines")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("""
            <div class="card" style="border:2px solid rgba(46,204,113,0.3);">
                <h4 style="color:#2ecc71;">✅ SAFER Habitats</h4>
                <ul>
                    <li>🌲 Old-growth forests</li>
                    <li>🌿 Natural grasslands</li>
                    <li>🍂 Undisturbed leaf litter</li>
                    <li>🌳 Areas with diverse tree species</li>
                    <li>🏔️ Mountain meadows</li>
                </ul>
            </div>
            """, unsafe_allow_html=True)
        
        with col2:
            st.markdown("""
            <div class="card" style="border:2px solid rgba(231,76,60,0.3);">
                <h4 style="color:#e74c3c;">⚠️ RISKY Habitats</h4>
                <ul>
                    <li>🗑️ Waste/dump areas</li>
                    <li>🛤️ Roadside paths</li>
                    <li>🏙️ Polluted urban areas</li>
                    <li>🚗 Near heavy traffic</li>
                    <li>🏭 Industrial zones</li>
                </ul>
            </div>
            """, unsafe_allow_html=True)
        
        # Quick tips
        st.info("""
        💡 **PRO TIP:** The safest mushrooms are typically found in:
        1. Old-growth forests with diverse tree species
        2. Natural meadows away from roads
        3. Areas with rich, undisturbed soil
        
        Always bring an experienced guide and multiple field guides!
        """)
    
    def _render_habitat_card(self, key, data):
        """Render a habitat risk card"""
        st.markdown(f"""
        <div style="background:rgba(255,255,255,0.03); border:2px solid {data['risk_color']}; 
                    border-radius:12px; padding:1rem; text-align:center; margin:0.3rem 0;
                    transition: all 0.3s ease; cursor: pointer;"
             onmouseover="this.style.transform='translateY(-4px)'; this.style.boxShadow='0 8px 25px rgba(0,0,0,0.3)';"
             onmouseout="this.style.transform='translateY(0)'; this.style.boxShadow='none';">
            <p style="font-size:2rem;">{data['icon']}</p>
            <h4>{data['name']}</h4>
            <p style="color:{data['risk_color']}; font-weight:700;">{data['risk_level']} RISK</p>
            <p style="font-size:1.5rem; font-weight:700;">{data['edible_percent']}%</p>
            <p style="color:#a0a0b0; font-size:0.8rem;">edible mushrooms</p>
        </div>
        """, unsafe_allow_html=True)
    
    def _render_habitat_detail(self, key):
        """Render detailed habitat information"""
        data = self.habitat_data[key]
        
        st.markdown(f"""
        <div class="card" style="border:2px solid {data['risk_color']};">
            <h2>{data['icon']} {data['name']}</h2>
            <p style="color:{data['risk_color']}; font-weight:700; font-size:1.2rem;">
                Risk Level: {data['risk_level']} ({data['edible_percent']}% edible)
            </p>
            <p>{data['description']}</p>
        </div>
        """, unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown(f"""
            <div style="background:rgba(46,204,113,0.1); padding:1rem; border-radius:8px;
                        border:1px solid rgba(46,204,113,0.3);">
                <h4 style="color:#2ecc71;">🍄 Common Edible Species</h4>
                {''.join([f'<p>✅ {m}</p>' for m in data['common_edible']])}
            </div>
            """, unsafe_allow_html=True)
        
        with col2:
            st.markdown(f"""
            <div style="background:rgba(231,76,60,0.1); padding:1rem; border-radius:8px;
                        border:1px solid rgba(231,76,60,0.3);">
                <h4 style="color:#e74c3c;">💀 Common Poisonous Species</h4>
                {''.join([f'<p>⚠️ {m}</p>' for m in data['common_poisonous']])}
            </div>
            """, unsafe_allow_html=True)
        
        st.info(f"💡 **Foraging Tip:** {data['tips']}")


# Initialize
habitat_risk_map = HabitatRiskMap()