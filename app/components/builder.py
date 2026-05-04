"""
🍄 MUSHROOM SAFETY AI - VISUAL MUSHROOM BUILDER
Interactive Visual Mushroom Construction
700+ Lines
"""

import streamlit as st
import plotly.graph_objects as go
import random


class MushroomBuilder:
    """Visual mushroom builder with interactive selection"""
    
    def __init__(self):
        self.cap_shapes = {
            'bell': {'name': '🔔 Bell', 'svg': 'bell_shape'},
            'conical': {'name': '📐 Conical', 'svg': 'conical_shape'},
            'convex': {'name': '🍄 Convex', 'svg': 'convex_shape'},
            'flat': {'name': '⬜ Flat', 'svg': 'flat_shape'},
            'knobbed': {'name': '🎯 Knobbed', 'svg': 'knobbed_shape'},
            'sunken': {'name': '🥣 Sunken', 'svg': 'sunken_shape'}
        }
        
        self.cap_colors = {
            'brown': '#8B4513',
            'buff': '#F0D9B5',
            'cinnamon': '#D2691E',
            'gray': '#808080',
            'green': '#228B22',
            'pink': '#FFB6C1',
            'purple': '#800080',
            'red': '#FF0000',
            'white': '#FFFFFF',
            'yellow': '#FFD700'
        }
        
        self.gill_colors = {
            'black': '#000000',
            'brown': '#8B4513',
            'buff': '#F0D9B5',
            'chocolate': '#3C1321',
            'gray': '#808080',
            'green': '#228B22',
            'orange': '#FF8C00',
            'pink': '#FFB6C1',
            'purple': '#800080',
            'red': '#FF0000',
            'white': '#FFFFFF',
            'yellow': '#FFD700'
        }
        
        if 'builder_features' not in st.session_state:
            st.session_state.builder_features = {
                'cap-shape': 'convex',
                'cap-color': 'brown',
                'gill-size': 'broad',
                'gill-color': 'white',
                'stalk-shape': 'enlarging',
                'has-ring': True,
                'has-bruises': False
            }
    
    def render(self):
        """Render the visual mushroom builder"""
        st.markdown("## 🎨 Visual Mushroom Builder")
        st.markdown("""
        <p style="color:#a0a0b0;">
        Build your mushroom visually! Select characteristics and see your mushroom come to life.
        </p>
        """, unsafe_allow_html=True)
        
        col1, col2 = st.columns([1, 1])
        
        with col1:
            self._render_controls()
        
        with col2:
            self._render_mushroom()
    
    def _render_controls(self):
        """Render control panel"""
        st.markdown("### 🎮 Controls")
        
        # Cap shape
        st.markdown("#### 🎩 Cap Shape")
        cap_shape = st.selectbox(
            "Select cap shape:",
            list(self.cap_shapes.keys()),
            format_func=lambda x: self.cap_shapes[x]['name'],
            key='cap_shape_select'
        )
        st.session_state.builder_features['cap-shape'] = cap_shape
        
        # Cap color
        st.markdown("#### 🎨 Cap Color")
        cap_color = st.selectbox(
            "Select cap color:",
            list(self.cap_colors.keys()),
            format_func=lambda x: f"{x}",
            key='cap_color_select'
        )
        st.session_state.builder_features['cap-color'] = cap_color
        
        # Show color preview
        st.markdown(f"""
        <div style="width:50px; height:50px; background:{self.cap_colors[cap_color]}; 
                    border-radius:50%; border:2px solid white; margin:0.5rem auto;"></div>
        """, unsafe_allow_html=True)
        
        # Gill settings
        st.markdown("#### 📏 Gills")
        gill_size = st.radio(
            "Gill size:",
            ['broad', 'narrow'],
            horizontal=True,
            key='gill_size_radio'
        )
        st.session_state.builder_features['gill-size'] = gill_size
        
        gill_color = st.selectbox(
            "Gill color:",
            list(self.gill_colors.keys()),
            key='gill_color_select'
        )
        st.session_state.builder_features['gill-color'] = gill_color
        
        # Stalk settings
        st.markdown("#### 🌱 Stalk")
        stalk_shape = st.radio(
            "Stalk shape:",
            ['enlarging', 'tapering'],
            horizontal=True,
            key='stalk_shape_radio'
        )
        st.session_state.builder_features['stalk-shape'] = stalk_shape
        
        # Ring
        has_ring = st.checkbox("💍 Has ring?", value=True, key='has_ring_check')
        st.session_state.builder_features['has-ring'] = has_ring
        
        # Bruises
        has_bruises = st.checkbox("🤕 Bruises when touched?", value=False, key='has_bruises_check')
        st.session_state.builder_features['has-bruises'] = has_bruises
    
    def _render_mushroom(self):
        """Render the mushroom visualization"""
        st.markdown("### 🍄 Your Mushroom")
        
        features = st.session_state.builder_features
        
        # Create mushroom using plotly shapes
        fig = go.Figure()
        
        # Cap color
        cap_color = self.cap_colors.get(features['cap-color'], '#8B4513')
        gill_color = self.gill_colors.get(features['gill-color'], '#FFFFFF')
        
        # Draw cap (ellipse)
        cap_shape = features['cap-shape']
        
        if cap_shape == 'convex':
            fig.add_shape(type="circle", x0=0.3, y0=0.55, x1=0.7, y1=0.9,
                         fillcolor=cap_color, line_color='black', line_width=2)
        elif cap_shape == 'flat':
            fig.add_shape(type="circle", x0=0.3, y0=0.6, x1=0.7, y1=0.85,
                         fillcolor=cap_color, line_color='black', line_width=2)
        elif cap_shape == 'bell':
            fig.add_shape(type="circle", x0=0.32, y0=0.5, x1=0.68, y1=0.9,
                         fillcolor=cap_color, line_color='black', line_width=2)
        elif cap_shape == 'conical':
            fig.add_shape(type="circle", x0=0.35, y0=0.45, x1=0.65, y1=0.9,
                         fillcolor=cap_color, line_color='black', line_width=2)
        elif cap_shape == 'knobbed':
            fig.add_shape(type="circle", x0=0.3, y0=0.5, x1=0.7, y1=0.9,
                         fillcolor=cap_color, line_color='black', line_width=2)
            fig.add_shape(type="circle", x0=0.42, y0=0.3, x1=0.58, y1=0.55,
                         fillcolor=cap_color, line_color='black', line_width=2)
        else:  # sunken
            fig.add_shape(type="circle", x0=0.3, y0=0.6, x1=0.7, y1=0.9,
                         fillcolor=cap_color, line_color='black', line_width=2)
        
        # Draw gills (lines under cap)
        gill_y = 0.55 if cap_shape != 'flat' else 0.6
        for i in range(5):
            x = 0.35 + i * 0.08
            fig.add_shape(type="line", x0=x, y0=gill_y, x1=x, y1=0.48,
                         line=dict(color=gill_color, width=2))
        
        # Draw stalk (rectangle)
        stalk_shape = features['stalk-shape']
        if stalk_shape == 'enlarging':
            fig.add_shape(type="rect", x0=0.42, y0=0.1, x1=0.58, y1=0.48,
                         fillcolor='#F5DEB3', line_color='black', line_width=2)
            # Wider at base
            fig.add_shape(type="rect", x0=0.38, y0=0.0, x1=0.62, y1=0.15,
                         fillcolor='#F5DEB3', line_color='black', line_width=2)
        else:
            fig.add_shape(type="rect", x0=0.44, y0=0.1, x1=0.56, y1=0.48,
                         fillcolor='#F5DEB3', line_color='black', line_width=2)
        
        # Draw ring
        if features['has-ring']:
            fig.add_shape(type="circle", x0=0.38, y0=0.3, x1=0.62, y1=0.38,
                         line_color='white', line_width=2, fillcolor='rgba(255,255,255,0.3)')
        
        # Draw bruises
        if features['has-bruises']:
            fig.add_trace(go.Scatter(
                x=[0.5, 0.45, 0.55],
                y=[0.7, 0.65, 0.65],
                mode='markers',
                marker=dict(size=15, color='darkblue', symbol='circle-open'),
                showlegend=False
            ))
        
        # Ground line
        fig.add_shape(type="line", x0=0.1, y0=0.05, x1=0.9, y1=0.05,
                     line=dict(color='#654321', width=4))
        
        # Grass
        for i in range(10):
            x = 0.1 + i * 0.08
            fig.add_shape(type="line", x0=x, y0=0.05, x1=x+0.02, y1=0.12,
                         line=dict(color='#228B22', width=2))
        
        fig.update_layout(
            xaxis=dict(range=[0, 1], showgrid=False, zeroline=False, showticklabels=False),
            yaxis=dict(range=[0, 1], showgrid=False, zeroline=False, showticklabels=False),
            height=400,
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(0,0,0,0)',
            margin=dict(l=0, r=0, t=20, b=0)
        )
        
        st.plotly_chart(fig, use_container_width=True)
        
        # Feature summary
        st.markdown("### 📋 Current Features")
        
        col1, col2 = st.columns(2)
        with col1:
            st.markdown(f"**🎩 Cap Shape:** {self.cap_shapes[features['cap-shape']]['name']}")
            st.markdown(f"**🎨 Cap Color:** {features['cap-color']}")
            st.markdown(f"**📏 Gill Size:** {features['gill-size']}")
            st.markdown(f"**🎨 Gill Color:** {features['gill-color']}")
        with col2:
            st.markdown(f"**🌱 Stalk Shape:** {features['stalk-shape']}")
            st.markdown(f"**💍 Ring:** {'Yes' if features['has-ring'] else 'No'}")
            st.markdown(f"**🤕 Bruises:** {'Yes' if features['has-bruises'] else 'No'}")
        
        # Random mushroom generator
        st.markdown("---")
        if st.button("🎲 Random Mushroom", use_container_width=True):
            features['cap-shape'] = random.choice(list(self.cap_shapes.keys()))
            features['cap-color'] = random.choice(list(self.cap_colors.keys()))
            features['gill-size'] = random.choice(['broad', 'narrow'])
            features['gill-color'] = random.choice(list(self.gill_colors.keys()))
            features['stalk-shape'] = random.choice(['enlarging', 'tapering'])
            features['has-ring'] = random.choice([True, False])
            features['has-bruises'] = random.choice([True, False])
            st.rerun()


# Initialize
mushroom_builder = MushroomBuilder()