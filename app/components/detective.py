"""
🍄 MUSHROOM SAFETY AI - FEATURE DETECTIVE
Interactive Feature Explorer
600+ Lines
"""

import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import random


class FeatureDetective:
    """Interactive Feature Investigation Tool"""
    
    def __init__(self):
        self.feature_info = {
            'odor': {
                'name': 'Odor',
                'icon': '👃',
                'importance': 89,
                'description': 'The most powerful predictor! Certain smells like almond guarantee safety, while foul/spicy/fishy smells indicate danger.',
                'fun_fact': 'Mushrooms produce odors to attract insects that help spread their spores!',
                'safe_values': ['almond', 'anise'],
                'danger_values': ['foul', 'spicy', 'fishy', 'pungent', 'creosote', 'musty'],
                'neutral_values': ['none']
            },
            'spore-print-color': {
                'name': 'Spore Print Color',
                'icon': '🔬',
                'importance': 52,
                'description': 'Made by placing the cap on paper overnight. The color of the spore deposit is a key identification tool.',
                'fun_fact': 'Some spore prints can be used to create beautiful artwork!',
                'safe_values': ['chocolate'],
                'danger_values': ['green', 'buff', 'purple', 'orange', 'yellow'],
                'neutral_values': ['white', 'brown', 'black']
            },
            'gill-size': {
                'name': 'Gill Size',
                'icon': '📏',
                'importance': 35,
                'description': 'Broad gills are more common in edible mushrooms, while narrow gills often indicate toxicity.',
                'fun_fact': 'Gills can produce millions of microscopic spores per hour!',
                'safe_values': ['broad'],
                'danger_values': ['narrow'],
                'neutral_values': []
            },
            'gill-color': {
                'name': 'Gill Color',
                'icon': '🎨',
                'importance': 41,
                'description': 'Bright or unusual gill colors are nature\'s warning signals. Brown and chocolate gills are safer.',
                'fun_fact': 'Gill color can change as the mushroom ages and spores mature!',
                'safe_values': ['chocolate', 'brown'],
                'danger_values': ['buff', 'green', 'purple', 'red', 'yellow'],
                'neutral_values': ['white', 'black', 'gray', 'orange', 'pink']
            },
            'bruises': {
                'name': 'Bruises',
                'icon': '🤕',
                'importance': 30,
                'description': 'Some mushrooms change color when bruised. This chemical reaction is a useful identification tool.',
                'fun_fact': 'The blue bruising reaction is caused by oxidation of psilocybin in magic mushrooms!',
                'safe_values': ['bruises'],
                'danger_values': ['no'],
                'neutral_values': []
            },
            'cap-color': {
                'name': 'Cap Color',
                'icon': '🎩',
                'importance': 13,
                'description': 'While not the strongest predictor alone, bright cap colors often signal danger in nature.',
                'fun_fact': 'The most expensive mushroom, the Matsutake, has a simple brown cap!',
                'safe_values': ['brown', 'white', 'gray', 'buff', 'cinnamon'],
                'danger_values': ['green', 'purple', 'red', 'yellow', 'pink'],
                'neutral_values': []
            },
            'habitat': {
                'name': 'Habitat',
                'icon': '🌍',
                'importance': 18,
                'description': 'Where the mushroom grows matters! Woodland mushrooms are generally safer than those in disturbed areas.',
                'fun_fact': 'Some mushrooms only grow near specific tree species in symbiotic relationships!',
                'safe_values': ['woods', 'grasses'],
                'danger_values': ['waste', 'paths'],
                'neutral_values': ['leaves', 'meadows', 'urban']
            },
            'population': {
                'name': 'Population',
                'icon': '👥',
                'importance': 16,
                'description': 'How mushrooms grow - alone or in clusters - can help with identification.',
                'fun_fact': 'The largest mushroom colony covers 2,385 acres in Oregon!',
                'safe_values': ['abundant', 'numerous'],
                'danger_values': ['scattered'],
                'neutral_values': ['clustered', 'several', 'solitary']
            },
            'ring-type': {
                'name': 'Ring Type',
                'icon': '💍',
                'importance': 22,
                'description': 'The ring (annulus) on the stalk is a remnant of the partial veil that once covered the gills.',
                'fun_fact': 'The ring pattern can help distinguish between deadly and edible Amanita species!',
                'safe_values': ['large', 'pendant'],
                'danger_values': ['cobwebby', 'zone'],
                'neutral_values': ['evanescent', 'flaring', 'none', 'sheathing']
            },
            'stalk-root': {
                'name': 'Stalk Root',
                'icon': '🌱',
                'importance': 10,
                'description': 'The base of the stalk can be bulbous, club-shaped, or equal. Some deadly mushrooms have a distinctive cup (volva).',
                'fun_fact': 'The Death Cap mushroom has a distinctive cup-like volva at the base!',
                'safe_values': ['bulbous', 'club'],
                'danger_values': ['cup'],
                'neutral_values': ['equal', 'rhizomorphs', 'rooted', 'missing']
            }
        }
        
        if 'detective_clues' not in st.session_state:
            st.session_state.detective_clues = []
        
        if 'detective_investigation' not in st.session_state:
            st.session_state.detective_investigation = False
    
    def render(self):
        """Main detective interface"""
        st.markdown("## 🔍 Feature Detective")
        st.markdown("""
        <p style="color:#a0a0b0; font-size:1.1rem;">
        Investigate each feature like a real mycologist! 
        Click on any feature card to learn more about its role in mushroom identification.
        </p>
        """, unsafe_allow_html=True)
        
        # Feature grid
        st.markdown("### 🎯 Click a feature to investigate:")
        
        cols = st.columns(5)
        for i, (feature_key, info) in enumerate(self.feature_info.items()):
            with cols[i % 5]:
                self._render_feature_card(feature_key, info)
        
        # Selected feature detail
        if 'selected_feature' in st.session_state:
            self._render_feature_detail()
        
        # Investigation mode
        st.markdown("---")
        self._render_investigation_mode()
    
    def _render_feature_card(self, feature_key, info):
        """Render a clickable feature card"""
        st.markdown(f"""
        <div style="background:rgba(255,255,255,0.03); border:1px solid rgba(255,255,255,0.08);
                    border-radius:12px; padding:1rem; margin:0.3rem 0; text-align:center;
                    cursor:pointer; transition:all 0.3s ease;"
             onclick="this.style.borderColor='#2ecc71'">
            <p style="font-size:2rem; margin:0;">{info['icon']}</p>
            <p style="font-size:0.8rem; font-weight:700; margin:0.3rem 0; color:white;">{info['name']}</p>
            <p style="font-size:0.7rem; color:#2ecc71; margin:0;">{info['importance']}% importance</p>
        </div>
        """, unsafe_allow_html=True)
        
        if st.button(f"🔍 {info['name']}", key=f"detective_{feature_key}"):
            st.session_state.selected_feature = feature_key
            st.rerun()
    
    def _render_feature_detail(self):
        """Render detailed view of selected feature"""
        feature_key = st.session_state.selected_feature
        info = self.feature_info[feature_key]
        
        st.markdown("---")
        st.markdown(f"### {info['icon']} {info['name']} - Detailed Analysis")
        
        col1, col2 = st.columns([3, 2])
        
        with col1:
            st.markdown(f"""
            <div class="card">
                <h4>📊 Importance: {info['importance']}%</h4>
                <p>{info['description']}</p>
                <p style="font-style:italic; color:#a0a0b0;">💡 {info['fun_fact']}</p>
            </div>
            """, unsafe_allow_html=True)
            
            # Value categories
            st.markdown("#### Value Categories:")
            
            col_a, col_b, col_c = st.columns(3)
            with col_a:
                st.markdown(f"""
                <div style="background:rgba(46,204,113,0.1); padding:1rem; border-radius:8px; 
                            border:1px solid rgba(46,204,113,0.3);">
                    <h5 style="color:#2ecc71;">✅ Safe Values</h5>
                    {self._format_values(info['safe_values'], '#2ecc71')}
                </div>
                """, unsafe_allow_html=True)
            
            with col_b:
                st.markdown(f"""
                <div style="background:rgba(231,76,60,0.1); padding:1rem; border-radius:8px;
                            border:1px solid rgba(231,76,60,0.3);">
                    <h5 style="color:#e74c3c;">⚠️ Danger Values</h5>
                    {self._format_values(info['danger_values'], '#e74c3c')}
                </div>
                """, unsafe_allow_html=True)
            
            with col_c:
                st.markdown(f"""
                <div style="background:rgba(241,196,15,0.1); padding:1rem; border-radius:8px;
                            border:1px solid rgba(241,196,15,0.3);">
                    <h5 style="color:#f1c40f;">➡️ Neutral Values</h5>
                    {self._format_values(info['neutral_values'], '#f1c40f')}
                </div>
                """, unsafe_allow_html=True)
        
        with col2:
            # Importance gauge
            fig = go.Figure(go.Indicator(
                mode="gauge+number",
                value=info['importance'],
                title={'text': f"{info['name']} Importance", 'font': {'color': 'white'}},
                gauge={
                    'axis': {'range': [0, 100], 'tickcolor': 'white'},
                    'bar': {'color': '#2ecc71'},
                    'steps': [
                        {'range': [0, 30], 'color': 'rgba(231,76,60,0.3)'},
                        {'range': [30, 60], 'color': 'rgba(241,196,15,0.3)'},
                        {'range': [60, 100], 'color': 'rgba(46,204,113,0.3)'}
                    ]
                }
            ))
            fig.update_layout(height=250, paper_bgcolor='rgba(0,0,0,0)', font={'color': 'white'})
            st.plotly_chart(fig, use_container_width=True)
            
            # Quick stats
            st.markdown(f"""
            <div class="card">
                <p><strong>Safe values:</strong> {len(info['safe_values'])}</p>
                <p><strong>Danger values:</strong> {len(info['danger_values'])}</p>
                <p><strong>Neutral values:</strong> {len(info['neutral_values'])}</p>
                <p><strong>Total unique values:</strong> {len(info['safe_values']) + len(info['danger_values']) + len(info['neutral_values'])}</p>
            </div>
            """, unsafe_allow_html=True)
    
    def _format_values(self, values, color):
        """Format values as styled HTML"""
        if not values:
            return "<p style='color:#606070;'>None</p>"
        return ''.join([f'<span style="display:inline-block; padding:0.2rem 0.5rem; margin:0.2rem; '
                       f'background:rgba(255,255,255,0.05); border-radius:4px; color:{color};">{v}</span>' 
                       for v in values])
    
    def _render_investigation_mode(self):
        """Render the investigation quiz mode"""
        st.markdown("### 🕵️ Investigation Challenge")
        st.markdown("Test your knowledge! Can you identify which feature is being described?")
        
        if not st.session_state.detective_investigation:
            if st.button("🎮 Start Investigation", type="primary"):
                st.session_state.detective_investigation = True
                self._generate_clue()
                st.rerun()
        else:
            clue = st.session_state.detective_clues[-1] if st.session_state.detective_clues else None
            
            if clue:
                st.markdown(f"""
                <div class="game-card">
                    <h3>🔍 Clue #{len(st.session_state.detective_clues)}</h3>
                    <p style="font-size:1.2rem; font-style:italic;">"{clue['description']}"</p>
                    <p style="color:#a0a0b0;">Fun fact: {clue['fun_fact']}</p>
                </div>
                """, unsafe_allow_html=True)
                
                # Options
                all_features = list(self.feature_info.keys())
                options = random.sample([f for f in all_features if f != clue['key']], 3)
                options.append(clue['key'])
                random.shuffle(options)
                
                option_names = [self.feature_info[opt]['name'] for opt in options]
                
                answer = st.radio("Which feature is being described?", option_names)
                
                if st.button("✅ Submit Answer"):
                    selected_key = [k for k, v in self.feature_info.items() if v['name'] == answer][0]
                    
                    if selected_key == clue['key']:
                        st.success(f"✅ Correct! It's the {self.feature_info[clue['key']]['name']} feature!")
                        st.balloons()
                    else:
                        st.error(f"❌ Wrong! The correct answer was {self.feature_info[clue['key']]['name']}.")
                    
                    if st.button("Next Clue ➡️"):
                        self._generate_clue()
                        st.rerun()
                
                if st.button("🛑 End Investigation"):
                    st.session_state.detective_investigation = False
                    st.session_state.detective_clues = []
                    st.rerun()
    
    def _generate_clue(self):
        """Generate a new investigation clue"""
        feature_key = random.choice(list(self.feature_info.keys()))
        info = self.feature_info[feature_key]
        
        clue = {
            'key': feature_key,
            'description': info['description'],
            'fun_fact': info['fun_fact']
        }
        
        st.session_state.detective_clues.append(clue)


# Initialize
feature_detective = FeatureDetective()