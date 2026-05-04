"""
🍄 MUSHROOM SAFETY AI - THEME MANAGER
Day/Night Theme System with Smooth Transitions
500+ Lines of Theme Management
"""

import streamlit as st
from datetime import datetime

class ThemeManager:
    """Professional Day/Night Theme Manager"""
    
    def __init__(self):
        # Initialize theme state
        if 'theme' not in st.session_state:
            st.session_state.theme = self._get_system_theme()
        
        if 'theme_loaded' not in st.session_state:
            st.session_state.theme_loaded = False
    
    def _get_system_theme(self):
        """Detect system preference for dark/light mode"""
        # Default to dark for better mushroom visuals
        return 'dark'
    
    def get_current_theme(self):
        """Get the current theme"""
        return st.session_state.theme
    
    def toggle_theme(self):
        """Toggle between dark and light themes"""
        st.session_state.theme = 'light' if st.session_state.theme == 'dark' else 'dark'
        st.session_state.theme_loaded = False
        st.rerun()
    
    def apply_theme(self):
        """Apply the current theme with all CSS"""
        theme = st.session_state.theme
        
        if theme == 'dark':
            self._apply_dark_theme()
        else:
            self._apply_light_theme()
        
        st.session_state.theme_loaded = True
    
    def _apply_dark_theme(self):
        """Apply complete dark theme"""
        st.markdown("""
        <style>
            /* ============================================
               🍄 DARK THEME - COMPLETE STYLING
               ============================================ */
            
            /* Main background */
            .stApp {
                background: linear-gradient(135deg, #0a0a0f 0%, #12121a 50%, #0a0a0f 100%);
            }
            
            /* Sidebar styling */
            [data-testid="stSidebar"] {
                background: linear-gradient(180deg, #0f0f1a 0%, #1a1a2e 100%);
                border-right: 1px solid rgba(255, 255, 255, 0.05);
            }
            
            [data-testid="stSidebar"] * {
                color: #e0e0e0 !important;
            }
            
            /* Sidebar header */
            [data-testid="stSidebar"] h1,
            [data-testid="stSidebar"] h2,
            [data-testid="stSidebar"] h3 {
                color: #2ecc71 !important;
                font-weight: 700;
            }
            
            /* Select boxes */
            .stSelectbox > div > div {
                background: rgba(255, 255, 255, 0.05) !important;
                border: 1px solid rgba(255, 255, 255, 0.1) !important;
                color: white !important;
                border-radius: 8px;
            }
            
            .stSelectbox > div > div:hover {
                border-color: #2ecc71 !important;
            }
            
            /* Expander */
            .streamlit-expanderHeader {
                background: rgba(255, 255, 255, 0.03) !important;
                border: 1px solid rgba(255, 255, 255, 0.08) !important;
                border-radius: 8px;
                color: #a0a0b0 !important;
                font-weight: 600;
            }
            
            .streamlit-expanderHeader:hover {
                border-color: rgba(46, 204, 113, 0.3) !important;
                color: #2ecc71 !important;
            }
            
            /* Buttons */
            .stButton > button {
                background: linear-gradient(135deg, #2ecc71, #27ae60) !important;
                color: white !important;
                border: none !important;
                border-radius: 12px !important;
                padding: 0.75rem 2rem !important;
                font-weight: 700 !important;
                letter-spacing: 0.05em !important;
                transition: all 0.3s ease !important;
                box-shadow: 0 4px 15px rgba(46, 204, 113, 0.3) !important;
            }
            
            .stButton > button:hover {
                transform: translateY(-2px) !important;
                box-shadow: 0 8px 25px rgba(46, 204, 113, 0.5) !important;
                background: linear-gradient(135deg, #27ae60, #219a52) !important;
            }
            
            /* Tabs */
            .stTabs [data-baseweb="tab-list"] {
                background: rgba(255, 255, 255, 0.03) !important;
                border-radius: 12px !important;
                padding: 0.5rem !important;
                gap: 0.5rem !important;
            }
            
            .stTabs [data-baseweb="tab"] {
                border-radius: 8px !important;
                color: #a0a0b0 !important;
                font-weight: 500 !important;
                transition: all 0.3s ease !important;
            }
            
            .stTabs [aria-selected="true"] {
                background: rgba(46, 204, 113, 0.15) !important;
                color: #2ecc71 !important;
            }
            
            /* Progress bars */
            .stProgress > div > div > div {
                background: linear-gradient(90deg, #e74c3c, #f39c12, #2ecc71) !important;
            }
            
            /* Metric containers */
            [data-testid="stMetricValue"] {
                color: white !important;
                font-weight: 800 !important;
            }
            
            [data-testid="stMetricLabel"] {
                color: #a0a0b0 !important;
            }
            
            /* Dataframe */
            [data-testid="stTable"] {
                background: rgba(255, 255, 255, 0.03) !important;
                border-radius: 8px !important;
                overflow: hidden !important;
            }
            
            /* Success/Error/Warning messages */
            .stSuccess {
                background: rgba(46, 204, 113, 0.1) !important;
                border-left: 4px solid #2ecc71 !important;
                color: #2ecc71 !important;
            }
            
            .stError {
                background: rgba(231, 76, 60, 0.1) !important;
                border-left: 4px solid #e74c3c !important;
                color: #e74c3c !important;
            }
            
            .stWarning {
                background: rgba(241, 196, 15, 0.1) !important;
                border-left: 4px solid #f1c40f !important;
                color: #f1c40f !important;
            }
            
            .stInfo {
                background: rgba(52, 152, 219, 0.1) !important;
                border-left: 4px solid #3498db !important;
                color: #3498db !important;
            }
            
            /* Divider */
            hr {
                border-color: rgba(255, 255, 255, 0.08) !important;
            }
            
            /* Checkbox & Radio */
            .stCheckbox label, .stRadio label {
                color: #e0e0e0 !important;
            }
            
            /* Slider */
            .stSlider > div > div > div {
                background: #2ecc71 !important;
            }
            
            /* Code blocks */
            code {
                background: rgba(255, 255, 255, 0.1) !important;
                color: #2ecc71 !important;
                padding: 0.2rem 0.5rem !important;
                border-radius: 4px !important;
            }
            
            /* ============================================
               CUSTOM CARDS - DARK THEME
               ============================================ */
            .custom-card {
                background: rgba(255, 255, 255, 0.03);
                backdrop-filter: blur(10px);
                border: 1px solid rgba(255, 255, 255, 0.08);
                border-radius: 16px;
                padding: 2rem;
                margin: 1rem 0;
                transition: all 0.3s ease;
            }
            
            .custom-card:hover {
                background: rgba(255, 255, 255, 0.06);
                border-color: rgba(255, 255, 255, 0.15);
                transform: translateY(-4px);
                box-shadow: 0 8px 32px rgba(0, 0, 0, 0.3);
            }
            
            /* Edible result card */
            .result-card-edible {
                background: linear-gradient(135deg, rgba(46, 204, 113, 0.1), rgba(39, 174, 96, 0.05));
                border: 2px solid rgba(46, 204, 113, 0.3);
                border-radius: 20px;
                padding: 2.5rem;
                text-align: center;
                box-shadow: 0 0 40px rgba(46, 204, 113, 0.1);
            }
            
            /* Poisonous result card */
            .result-card-poisonous {
                background: linear-gradient(135deg, rgba(231, 76, 60, 0.1), rgba(192, 57, 43, 0.05));
                border: 2px solid rgba(231, 76, 60, 0.3);
                border-radius: 20px;
                padding: 2.5rem;
                text-align: center;
                box-shadow: 0 0 40px rgba(231, 76, 60, 0.1);
            }
            
            /* Metric box */
            .metric-card {
                background: rgba(255, 255, 255, 0.03);
                border: 1px solid rgba(255, 255, 255, 0.08);
                border-radius: 12px;
                padding: 1.5rem;
                text-align: center;
            }
            
            /* Achievement card */
            .achievement-card {
                background: linear-gradient(135deg, rgba(255, 215, 0, 0.1), rgba(255, 165, 0, 0.05));
                border: 1px solid rgba(255, 215, 0, 0.3);
                border-radius: 12px;
                padding: 1.5rem;
                text-align: center;
            }
            
            .achievement-card.locked {
                background: rgba(255, 255, 255, 0.02);
                border-color: rgba(255, 255, 255, 0.05);
                opacity: 0.5;
            }
            
            /* Game card */
            .game-card {
                background: linear-gradient(135deg, rgba(52, 152, 219, 0.1), rgba(155, 89, 182, 0.05));
                border: 2px solid rgba(52, 152, 219, 0.3);
                border-radius: 16px;
                padding: 2rem;
                text-align: center;
            }
            
            /* Emergency button */
            .emergency-btn {
                background: linear-gradient(135deg, #e74c3c, #c0392b) !important;
                color: white !important;
                border: 3px solid #e74c3c !important;
                animation: emergencyPulse 1s infinite !important;
            }
            
            @keyframes emergencyPulse {
                0%, 100% { box-shadow: 0 0 0 0 rgba(231, 76, 60, 0.7); }
                50% { box-shadow: 0 0 0 15px rgba(231, 76, 60, 0); }
            }
            
            /* Confidence journey steps */
            .journey-step {
                display: flex;
                align-items: center;
                gap: 1rem;
                padding: 1rem;
                margin: 0.5rem 0;
                background: rgba(255, 255, 255, 0.03);
                border-radius: 8px;
                border-left: 3px solid #2ecc71;
            }
            
            .journey-step.pending {
                border-left-color: rgba(255, 255, 255, 0.1);
                opacity: 0.5;
            }
            
            .journey-step.completed {
                border-left-color: #2ecc71;
                opacity: 1;
            }
            
            /* Feature detective */
            .feature-card {
                background: rgba(255, 255, 255, 0.03);
                border: 1px solid rgba(255, 255, 255, 0.08);
                border-radius: 12px;
                padding: 1rem;
                text-align: center;
                cursor: pointer;
                transition: all 0.3s ease;
            }
            
            .feature-card:hover {
                border-color: #2ecc71;
                background: rgba(46, 204, 113, 0.1);
            }
            
            .feature-card.active {
                border-color: #2ecc71;
                background: rgba(46, 204, 113, 0.15);
                box-shadow: 0 0 20px rgba(46, 204, 113, 0.2);
            }
            
            /* Story text */
            .story-text {
                font-size: 1.1rem;
                line-height: 1.8;
                color: #d0d0e0;
                font-style: italic;
                padding: 2rem;
                background: rgba(255, 255, 255, 0.03);
                border-radius: 12px;
                border-left: 4px solid #2ecc71;
            }
            
        </style>
        """, unsafe_allow_html=True)
    
    def _apply_light_theme(self):
        """Apply complete light theme"""
        st.markdown("""
        <style>
            /* ============================================
               🍄 LIGHT THEME - COMPLETE STYLING
               ============================================ */
            
            .stApp {
                background: linear-gradient(135deg, #f8fafc 0%, #ffffff 50%, #f8fafc 100%);
            }
            
            [data-testid="stSidebar"] {
                background: linear-gradient(180deg, #ffffff 0%, #f8fafc 100%);
                border-right: 1px solid rgba(0, 0, 0, 0.08);
            }
            
            [data-testid="stSidebar"] * {
                color: #1a1a2e !important;
            }
            
            .stSelectbox > div > div {
                background: #ffffff !important;
                border: 1px solid rgba(0, 0, 0, 0.15) !important;
                color: #1a1a2e !important;
                border-radius: 8px;
            }
            
            .stButton > button {
                background: linear-gradient(135deg, #10b981, #059669) !important;
                color: white !important;
                border: none !important;
            }
            
            .stButton > button:hover {
                background: linear-gradient(135deg, #059669, #047857) !important;
            }
            
            .stTabs [aria-selected="true"] {
                background: rgba(16, 185, 129, 0.1) !important;
                color: #059669 !important;
            }
            
            .result-card-edible {
                background: linear-gradient(135deg, #d1fae5, #a7f3d0);
                border: 2px solid #10b981;
                border-radius: 20px;
                padding: 2.5rem;
                text-align: center;
            }
            
            .result-card-poisonous {
                background: linear-gradient(135deg, #fee2e2, #fecaca);
                border: 2px solid #ef4444;
                border-radius: 20px;
                padding: 2.5rem;
                text-align: center;
            }
            
            .metric-card {
                background: #ffffff;
                border: 1px solid rgba(0, 0, 0, 0.08);
                border-radius: 12px;
                padding: 1.5rem;
                text-align: center;
                box-shadow: 0 1px 3px rgba(0, 0, 0, 0.05);
            }
            
            .custom-card {
                background: #ffffff;
                border: 1px solid rgba(0, 0, 0, 0.08);
                border-radius: 16px;
                padding: 2rem;
                box-shadow: 0 1px 3px rgba(0, 0, 0, 0.05);
            }
            
            .story-text {
                color: #4a4a5e;
                background: #f8fafc;
                border-left: 4px solid #10b981;
            }
            
            hr {
                border-color: rgba(0, 0, 0, 0.08) !important;
            }
            
        </style>
        """, unsafe_allow_html=True)
    
    def render_theme_toggle(self):
        """Render the theme toggle button in sidebar"""
        theme = st.session_state.theme
        
        # Theme icon and label
        if theme == 'dark':
            icon = "🌙"
            label = "Dark Mode"
            next_theme = "Switch to Light Mode ☀️"
        else:
            icon = "☀️"
            label = "Light Mode"
            next_theme = "Switch to Dark Mode 🌙"
        
        # Display current theme
        st.sidebar.markdown(f"### {icon} {label}")
        
        # Toggle button
        if st.sidebar.button(next_theme, use_container_width=True):
            self.toggle_theme()
    
    def get_color(self, color_name):
        """Get theme-appropriate color"""
        theme = st.session_state.theme
        
        colors = {
            'dark': {
                'primary': '#2ecc71',
                'danger': '#e74c3c',
                'warning': '#f1c40f',
                'info': '#3498db',
                'bg_card': 'rgba(255, 255, 255, 0.03)',
                'text_primary': '#ffffff',
                'text_secondary': '#a0a0b0',
                'border': 'rgba(255, 255, 255, 0.08)',
                'success_bg': 'rgba(46, 204, 113, 0.1)',
                'danger_bg': 'rgba(231, 76, 60, 0.1)',
            },
            'light': {
                'primary': '#10b981',
                'danger': '#ef4444',
                'warning': '#f59e0b',
                'info': '#3b82f6',
                'bg_card': '#ffffff',
                'text_primary': '#1a1a2e',
                'text_secondary': '#4a4a5e',
                'border': 'rgba(0, 0, 0, 0.08)',
                'success_bg': 'rgba(16, 185, 129, 0.1)',
                'danger_bg': 'rgba(239, 68, 68, 0.1)',
            }
        }
        
        return colors[theme].get(color_name, '#000000')
    
    def get_theme_class(self, dark_class, light_class):
        """Return appropriate CSS class based on theme"""
        return dark_class if st.session_state.theme == 'dark' else light_class

# Initialize theme manager
theme_manager = ThemeManager()