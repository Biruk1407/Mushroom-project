"""
🍄 MUSHROOM SAFETY AI - CONFIDENCE JOURNEY
Animated Step-by-Step Analysis Visualization
400+ Lines
"""

import streamlit as st
import plotly.graph_objects as go
import time


class ConfidenceJourney:
    """Animated confidence journey visualization"""
    
    def __init__(self):
        self.steps_data = [
            {
                'feature': 'Odor',
                'icon': '👃',
                'description': 'Checking the smell...',
                'weight': 35,
                'safe_indicators': ['almond', 'anise'],
                'danger_indicators': ['foul', 'spicy', 'fishy', 'pungent', 'creosote', 'musty']
            },
            {
                'feature': 'Spore Print',
                'icon': '🔬',
                'description': 'Analyzing spore print color...',
                'weight': 20,
                'safe_indicators': ['chocolate'],
                'danger_indicators': ['green', 'buff', 'purple', 'orange', 'yellow']
            },
            {
                'feature': 'Gill Size',
                'icon': '📏',
                'description': 'Measuring gill width...',
                'weight': 15,
                'safe_indicators': ['broad'],
                'danger_indicators': ['narrow']
            },
            {
                'feature': 'Gill Color',
                'icon': '🎨',
                'description': 'Examining gill color...',
                'weight': 15,
                'safe_indicators': ['chocolate', 'brown'],
                'danger_indicators': ['buff', 'green', 'purple', 'red', 'yellow']
            },
            {
                'feature': 'Bruises',
                'icon': '🤕',
                'description': 'Checking for bruising...',
                'weight': 10,
                'safe_indicators': ['bruises'],
                'danger_indicators': ['no']
            },
            {
                'feature': 'Habitat',
                'icon': '🌍',
                'description': 'Examining habitat...',
                'weight': 5,
                'safe_indicators': ['woods', 'grasses'],
                'danger_indicators': ['waste', 'paths']
            }
        ]
    
    def render(self, features, predict_func):
        """Render the confidence journey"""
        st.markdown("## 🗺️ Confidence Journey")
        st.markdown("""
        <p style="color:#a0a0b0;">
        Watch as I analyze each feature step by step, building confidence toward the final prediction!
        </p>
        """, unsafe_allow_html=True)
        
        if st.button("🚀 START JOURNEY", type="primary", use_container_width=True):
            self._animate_journey(features, predict_func)
    
    def _animate_journey(self, features, predict_func):
        """Animate the confidence building process"""
        
        # Progress containers
        progress_bar = st.progress(0)
        status_text = st.empty()
        journey_container = st.container()
        
        confidence_history = [50]  # Start at 50% (neutral)
        step_details = []
        
        # Partial features start
        partial_features = {}
        
        for i, step in enumerate(self.steps_data):
            # Update progress
            progress = (i + 1) / len(self.steps_data)
            progress_bar.progress(progress)
            
            # Add this step's feature
            feature_key = step['feature'].lower().replace(' ', '-')
            if feature_key in features:
                partial_features[feature_key] = features[feature_key]
            
            # Get intermediate prediction
            if len(partial_features) >= 2:
                result = predict_func(partial_features)
                current_confidence = result['confidence']
            else:
                current_confidence = 50
            
            confidence_history.append(current_confidence)
            
            # Determine impact
            value = features.get(feature_key, 'unknown')
            if value in step['safe_indicators']:
                impact = 'positive'
                impact_color = '#2ecc71'
                impact_icon = '✅'
            elif value in step['danger_indicators']:
                impact = 'negative'
                impact_color = '#e74c3c'
                impact_icon = '⚠️'
            else:
                impact = 'neutral'
                impact_color = '#f1c40f'
                impact_icon = '➡️'
            
            step_details.append({
                'step': i + 1,
                'icon': step['icon'],
                'feature': step['feature'],
                'value': value,
                'impact': impact,
                'impact_icon': impact_icon,
                'impact_color': impact_color,
                'confidence': current_confidence,
                'description': step['description']
            })
            
            # Update status
            status_text.markdown(f"""
            <div style="text-align:center; padding:1rem;">
                <h3>{step['icon']} Step {i+1}/{len(self.steps_data)}: {step['feature']}</h3>
                <p style="color:{impact_color};">{impact_icon} Value: '{value}' - Impact: {impact.upper()}</p>
                <h2 style="color:#2ecc71;">Confidence: {current_confidence}%</h2>
            </div>
            """, unsafe_allow_html=True)
            
            time.sleep(0.5)
        
        # Final prediction
        final_result = predict_func(features)
        progress_bar.progress(1.0)
        
        status_text.markdown(f"""
        <div style="text-align:center; padding:2rem; 
                    background:rgba({'46,204,113' if final_result['prediction']=='EDIBLE' else '231,76,60'},0.1);
                    border-radius:16px; border:2px solid {'#2ecc71' if final_result['prediction']=='EDIBLE' else '#e74c3c'};">
            <h1>{'🍄' if final_result['prediction']=='EDIBLE' else '💀'}</h1>
            <h2 style="color:{'#2ecc71' if final_result['prediction']=='EDIBLE' else '#e74c3c'};">
                FINAL: {final_result['prediction']}
            </h2>
            <h1>{final_result['confidence']}%</h1>
            <p>{final_result['reason']}</p>
        </div>
        """, unsafe_allow_html=True)
        
        # Show all steps
        with journey_container:
            st.markdown("---")
            st.markdown("### 📋 Analysis Steps")
            
            for detail in step_details:
                st.markdown(f"""
                <div style="display:flex; align-items:center; gap:1rem; 
                            padding:0.8rem; margin:0.3rem 0;
                            background:rgba(255,255,255,0.03); border-radius:8px;
                            border-left:3px solid {detail['impact_color']};">
                    <span style="font-size:2rem;">{detail['icon']}</span>
                    <div style="flex:1;">
                        <strong>Step {detail['step']}: {detail['feature']}</strong>
                        <span style="float:right; font-weight:700; color:{detail['impact_color']};">
                            {detail['impact_icon']} {detail['impact'].upper()}
                        </span>
                        <br>
                        <span style="color:#a0a0b0;">Value: '{detail['value']}'</span>
                        <span style="float:right; color:#2ecc71;">→ {detail['confidence']}%</span>
                    </div>
                </div>
                """, unsafe_allow_html=True)
        
        # Confidence evolution chart
        st.markdown("---")
        st.markdown("### 📈 Confidence Evolution")
        
        fig = go.Figure()
        
        fig.add_trace(go.Scatter(
            x=['Start'] + [s['feature'] for s in step_details] + ['Final'],
            y=confidence_history + [final_result['confidence']],
            mode='lines+markers',
            line=dict(color='#2ecc71', width=3),
            marker=dict(size=12, color=[
                '#a0a0b0',  # Start
                *[s['impact_color'] for s in step_details],
                '#2ecc71' if final_result['prediction']=='EDIBLE' else '#e74c3c'  # Final
            ]),
            fill='tozeroy',
            fillcolor='rgba(46,204,113,0.1)'
        ))
        
        fig.add_hline(y=50, line_dash="dash", line_color="rgba(255,255,255,0.3)")
        
        fig.update_layout(
            title='Confidence Building Journey',
            yaxis=dict(range=[0, 100], title='Confidence %'),
            height=400,
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(0,0,0,0)',
            font={'color': 'white'},
            hovermode='x unified'
        )
        
        st.plotly_chart(fig, use_container_width=True)


# Initialize
confidence_journey = ConfidenceJourney()
confidence_journey = ConfidenceJourney()