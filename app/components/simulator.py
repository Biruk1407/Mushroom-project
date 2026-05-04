"""
🍄 MUSHROOM SAFETY AI - BEFORE & AFTER SIMULATOR
Change One Feature, See the Impact
500+ Lines
"""

import streamlit as st
import plotly.graph_objects as go
import pandas as pd


class FeatureSimulator:
    """Before & After feature change simulator"""
    
    def __init__(self):
        self.features_list = {
            'odor': {
                'name': 'Odor', 'icon': '👃',
                'safe': ['almond', 'anise'],
                'danger': ['foul', 'spicy', 'fishy', 'pungent', 'creosote', 'musty'],
                'neutral': ['none']
            },
            'spore-print-color': {
                'name': 'Spore Print Color', 'icon': '🔬',
                'safe': ['chocolate'],
                'danger': ['green', 'buff', 'purple', 'orange', 'yellow'],
                'neutral': ['white', 'brown', 'black']
            },
            'gill-size': {
                'name': 'Gill Size', 'icon': '📏',
                'safe': ['broad'],
                'danger': ['narrow'],
                'neutral': []
            },
            'gill-color': {
                'name': 'Gill Color', 'icon': '🎨',
                'safe': ['chocolate', 'brown'],
                'danger': ['buff', 'green', 'purple', 'red', 'yellow'],
                'neutral': ['white', 'black', 'gray', 'orange', 'pink']
            },
            'bruises': {
                'name': 'Bruises', 'icon': '🤕',
                'safe': ['bruises'],
                'danger': ['no'],
                'neutral': []
            },
            'cap-color': {
                'name': 'Cap Color', 'icon': '🎩',
                'safe': ['brown', 'white', 'gray', 'buff', 'cinnamon'],
                'danger': ['green', 'purple', 'red', 'yellow', 'pink'],
                'neutral': []
            },
            'habitat': {
                'name': 'Habitat', 'icon': '🌍',
                'safe': ['woods', 'grasses'],
                'danger': ['waste', 'paths'],
                'neutral': ['leaves', 'meadows', 'urban']
            },
            'population': {
                'name': 'Population', 'icon': '👥',
                'safe': ['abundant', 'numerous'],
                'danger': ['scattered'],
                'neutral': ['clustered', 'several', 'solitary']
            },
            'ring-type': {
                'name': 'Ring Type', 'icon': '💍',
                'safe': ['large', 'pendant'],
                'danger': ['cobwebby', 'zone'],
                'neutral': ['evanescent', 'flaring', 'none', 'sheathing']
            },
            'stalk-root': {
                'name': 'Stalk Root', 'icon': '🌱',
                'safe': ['bulbous', 'club'],
                'danger': ['cup'],
                'neutral': ['equal', 'rhizomorphs', 'rooted', 'missing']
            }
        }
        
        if 'simulation_history' not in st.session_state:
            st.session_state.simulation_history = []
    
    def render(self, current_features, predict_func):
        """Render the simulator interface"""
        st.markdown("## 🔄 Before & After Simulator")
        st.markdown("""
        <p style="color:#a0a0b0;">
        Change ONE feature at a time to see how it affects the prediction!
        This helps you understand which features are most powerful.
        </p>
        """, unsafe_allow_html=True)
        
        # Current prediction
        current_result = predict_func(current_features)
        
        # Display current state
        col1, col2 = st.columns(2)
        
        with col1:
            self._render_mushroom_card("🍄 CURRENT MUSHROOM", current_result, current_features, "current")
        
        with col2:
            # Feature selector
            st.markdown("### 🔄 Change One Feature")
            
            feature_to_change = st.selectbox(
                "Select feature to modify:",
                list(self.features_list.keys()),
                format_func=lambda x: f"{self.features_list[x]['icon']} {self.features_list[x]['name']}"
            )
            
            feature_info = self.features_list[feature_to_change]
            all_options = feature_info['safe'] + feature_info['danger'] + feature_info['neutral']
            current_value = current_features.get(feature_to_change, all_options[0])
            
            new_value = st.selectbox(
                f"New value for {feature_info['name']}:",
                all_options,
                index=all_options.index(current_value) if current_value in all_options else 0
            )
            
            if st.button("🔄 SIMULATE CHANGE", type="primary", use_container_width=True):
                # Create modified features
                modified_features = current_features.copy()
                modified_features[feature_to_change] = new_value
                
                # Get new prediction
                new_result = predict_func(modified_features)
                
                # Store in history
                st.session_state.simulation_history.append({
                    'feature': feature_to_change,
                    'old_value': current_value,
                    'new_value': new_value,
                    'old_prediction': current_result['prediction'],
                    'new_prediction': new_result['prediction'],
                    'old_confidence': current_result['confidence'],
                    'new_confidence': new_result['confidence'],
                    'flipped': current_result['prediction'] != new_result['prediction']
                })
                
                # Show result
                self._render_simulation_result(
                    feature_info, current_value, new_value,
                    current_result, new_result
                )
        
        # Simulation history
        if st.session_state.simulation_history:
            st.markdown("---")
            st.markdown("### 📜 Simulation History")
            self._render_history()
    
    def _render_mushroom_card(self, title, result, features, card_type):
        """Render a mushroom prediction card"""
        color = '#2ecc71' if result['prediction'] == 'EDIBLE' else '#e74c3c'
        emoji = '🍄' if result['prediction'] == 'EDIBLE' else '💀'
        
        st.markdown(f"""
        <div style="background:rgba(255,255,255,0.03); border:2px solid {color}; 
                    border-radius:16px; padding:1.5rem; text-align:center;">
            <h3>{title}</h3>
            <p style="font-size:3rem;">{emoji}</p>
            <h2 style="color:{color};">{result['prediction']}</h2>
            <p style="font-size:1.5rem; font-weight:700;">{result['confidence']}%</p>
            <p style="color:#a0a0b0;">confidence</p>
        </div>
        """, unsafe_allow_html=True)
        
        # Feature summary
        with st.expander("📋 View Features", expanded=False):
            for key, info in self.features_list.items():
                value = features.get(key, 'N/A')
                st.markdown(f"{info['icon']} **{info['name']}:** {value}")
    
    def _render_simulation_result(self, feature_info, old_value, new_value, old_result, new_result):
        """Render simulation comparison"""
        st.markdown("---")
        st.markdown("### 📊 Simulation Results")
        
        # Change highlight
        if old_result['prediction'] != new_result['prediction']:
            st.warning(f"""
            🚨 **DRAMATIC CHANGE!** Changing {feature_info['icon']} **{feature_info['name']}** 
            from '{old_value}' to '{new_value}' COMPLETELY FLIPPED the prediction 
            from **{old_result['prediction']}** to **{new_result['prediction']}**!
            """)
        
        # Comparison columns
        col1, col2, col3 = st.columns([2, 1, 2])
        
        with col1:
            st.markdown(f"""
            <div style="background:rgba(255,255,255,0.03); padding:1rem; border-radius:8px; text-align:center;">
                <h4>BEFORE</h4>
                <p style="font-size:1.2rem;">{feature_info['name']}: <strong>{old_value}</strong></p>
                <p style="font-size:2rem; font-weight:700; color:{'#2ecc71' if old_result['prediction']=='EDIBLE' else '#e74c3c'};">
                    {old_result['prediction']}
                </p>
                <p>{old_result['confidence']}% confidence</p>
            </div>
            """, unsafe_allow_html=True)
        
        with col2:
            # Arrow and delta
            delta = new_result['confidence'] - old_result['confidence']
            arrow = '📈' if delta > 0 else '📉' if delta < 0 else '➡️'
            
            st.markdown(f"""
            <div style="text-align:center; padding-top:3rem;">
                <p style="font-size:3rem;">{arrow}</p>
                <p style="font-size:1.2rem; color:{'#2ecc71' if delta>0 else '#e74c3c' if delta<0 else '#a0a0b0'};">
                    {delta:+d}%
                </p>
            </div>
            """, unsafe_allow_html=True)
        
        with col3:
            st.markdown(f"""
            <div style="background:rgba(255,255,255,0.03); padding:1rem; border-radius:8px; text-align:center;">
                <h4>AFTER</h4>
                <p style="font-size:1.2rem;">{feature_info['name']}: <strong>{new_value}</strong></p>
                <p style="font-size:2rem; font-weight:700; color:{'#2ecc71' if new_result['prediction']=='EDIBLE' else '#e74c3c'};">
                    {new_result['prediction']}
                </p>
                <p>{new_result['confidence']}% confidence</p>
            </div>
            """, unsafe_allow_html=True)
        
        # Feature power assessment
        impact = abs(new_result['confidence'] - old_result['confidence'])
        flipped = old_result['prediction'] != new_result['prediction']
        
        if flipped:
            power = "💪 VERY POWERFUL - This feature can completely change the outcome!"
        elif impact >= 20:
            power = "🔥 STRONG - This feature significantly affects confidence!"
        elif impact >= 10:
            power = "📊 MODERATE - This feature has a noticeable effect."
        else:
            power = "💡 SUBTLE - This feature has a minor impact on this mushroom."
        
        st.info(power)
    
    def _render_history(self):
        """Render simulation history"""
        history = st.session_state.simulation_history[-10:]  # Last 10
        
        for i, entry in enumerate(reversed(history)):
            feature_info = self.features_list[entry['feature']]
            flipped = entry['flipped']
            
            bg = 'rgba(231,76,60,0.1)' if flipped else 'rgba(255,255,255,0.03)'
            border = '#e74c3c' if flipped else 'rgba(255,255,255,0.1)'
            
            st.markdown(f"""
            <div style="background:{bg}; border:1px solid {border}; 
                        border-radius:8px; padding:0.8rem; margin:0.3rem 0;">
                <strong>{feature_info['icon']} {feature_info['name']}:</strong> 
                {entry['old_value']} → {entry['new_value']}
                <span style="float:right;">
                    {entry['old_prediction']} ({entry['old_confidence']}%) 
                    → {entry['new_prediction']} ({entry['new_confidence']}%)
                    {'⚠️ FLIPPED!' if flipped else ''}
                </span>
            </div>
            """, unsafe_allow_html=True)
        
        if st.button("🗑️ Clear History"):
            st.session_state.simulation_history = []
            st.rerun()


# Initialize
feature_simulator = FeatureSimulator()
# Initialize - ADD THIS AT THE BOTTOM
feature_simulator = FeatureSimulator()