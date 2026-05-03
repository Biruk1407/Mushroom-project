
import streamlit as st
import pandas as pd
import numpy as np
import pickle
import warnings
warnings.filterwarnings('ignore')

st.set_page_config(
    page_title="Mushroom Safety Classifier",
    page_icon="🍄",
    layout="wide"
)

st.markdown('''
<style>
.main-header {
    font-size: 3rem;
    color: #2ecc71;
    text-align: center;
    margin-bottom: 2rem;
}
.prediction-box {
    padding: 2rem;
    border-radius: 1rem;
    text-align: center;
    margin: 1rem 0;
}
.edible {
    background: linear-gradient(135deg, #2ecc71, #27ae60);
    color: white;
}
.poisonous {
    background: linear-gradient(135deg, #e74c3c, #c0392b);
    color: white;
}
.feature-card {
    background: #f8f9fa;
    padding: 1rem;
    border-radius: 0.5rem;
    margin: 0.5rem 0;
}
</style>
''', unsafe_allow_html=True)

@st.cache_resource
def load_model():
    try:
        with open('../models/saved_models/best_tuned_model.pkl', 'rb') as f:
            return pickle.load(f)
    except:
        try:
            with open('../models/saved_models/best_advanced_model.pkl', 'rb') as f:
                return pickle.load(f)
        except:
            from xgboost import XGBClassifier
            return XGBClassifier(n_estimators=100, random_state=42)

@st.cache_resource
def load_encoders():
    try:
        with open('../models/encoders/label_encoders.pkl', 'rb') as f:
            return pickle.load(f)
    except:
        return {}

model = load_model()
encoders = load_encoders()

FEATURE_OPTIONS = {
    'cap-shape': ['bell', 'conical', 'convex', 'flat', 'knobbed', 'sunken'],
    'cap-surface': ['fibrous', 'grooves', 'scaly', 'smooth'],
    'cap-color': ['brown', 'buff', 'cinnamon', 'gray', 'green', 'pink', 'purple', 'red', 'white', 'yellow'],
    'bruises': ['bruises', 'no'],
    'odor': ['almond', 'anise', 'creosote', 'fishy', 'foul', 'musty', 'none', 'pungent', 'spicy'],
    'gill-attachment': ['attached', 'descending', 'free', 'notched'],
    'gill-spacing': ['close', 'crowded', 'distant'],
    'gill-size': ['broad', 'narrow'],
    'gill-color': ['black', 'brown', 'buff', 'chocolate', 'gray', 'green', 'orange', 'pink', 'purple', 'red', 'white', 'yellow'],
    'stalk-shape': ['enlarging', 'tapering'],
    'stalk-root': ['bulbous', 'club', 'cup', 'equal', 'rhizomorphs', 'rooted', 'missing'],
    'stalk-surface-above-ring': ['fibrous', 'scaly', 'silky', 'smooth'],
    'stalk-surface-below-ring': ['fibrous', 'scaly', 'silky', 'smooth'],
    'stalk-color-above-ring': ['brown', 'buff', 'cinnamon', 'gray', 'orange', 'pink', 'red', 'white', 'yellow'],
    'stalk-color-below-ring': ['brown', 'buff', 'cinnamon', 'gray', 'orange', 'pink', 'red', 'white', 'yellow'],
    'veil-type': ['partial', 'universal'],
    'veil-color': ['brown', 'orange', 'white', 'yellow'],
    'ring-number': ['none', 'one', 'two'],
    'ring-type': ['cobwebby', 'evanescent', 'flaring', 'large', 'none', 'pendant', 'sheathing', 'zone'],
    'spore-print-color': ['black', 'brown', 'buff', 'chocolate', 'green', 'orange', 'purple', 'white', 'yellow'],
    'population': ['abundant', 'clustered', 'numerous', 'scattered', 'several', 'solitary'],
    'habitat': ['grasses', 'leaves', 'meadows', 'paths', 'urban', 'waste', 'woods']
}

def encode_input(features_dict):
    encoded = {}
    for feature, value in features_dict.items():
        if feature in encoders:
            try:
                encoded[feature] = encoders[feature].transform([value])[0]
            except:
                encoded[feature] = 0
        else:
            encoded[feature] = 0
    return pd.DataFrame([encoded])

st.sidebar.markdown("# 🍄 Mushroom Features")

features = {}
with st.sidebar.expander("🎩 CAP FEATURES", expanded=True):
    features['cap-shape'] = st.selectbox("Cap Shape", FEATURE_OPTIONS['cap-shape'])
    features['cap-surface'] = st.selectbox("Cap Surface", FEATURE_OPTIONS['cap-surface'])
    features['cap-color'] = st.selectbox("Cap Color", FEATURE_OPTIONS['cap-color'])
    features['bruises'] = st.selectbox("Bruises?", FEATURE_OPTIONS['bruises'])

with st.sidebar.expander("👃 ODOR", expanded=True):
    features['odor'] = st.selectbox("Odor", FEATURE_OPTIONS['odor'])

with st.sidebar.expander("🎨 GILL FEATURES", expanded=False):
    features['gill-attachment'] = st.selectbox("Gill Attachment", FEATURE_OPTIONS['gill-attachment'])
    features['gill-spacing'] = st.selectbox("Gill Spacing", FEATURE_OPTIONS['gill-spacing'])
    features['gill-size'] = st.selectbox("Gill Size", FEATURE_OPTIONS['gill-size'])
    features['gill-color'] = st.selectbox("Gill Color", FEATURE_OPTIONS['gill-color'])

with st.sidebar.expander("🌱 STALK FEATURES", expanded=False):
    features['stalk-shape'] = st.selectbox("Stalk Shape", FEATURE_OPTIONS['stalk-shape'])
    features['stalk-root'] = st.selectbox("Stalk Root", FEATURE_OPTIONS['stalk-root'])
    features['stalk-surface-above-ring'] = st.selectbox("Surface Above Ring", FEATURE_OPTIONS['stalk-surface-above-ring'])
    features['stalk-surface-below-ring'] = st.selectbox("Surface Below Ring", FEATURE_OPTIONS['stalk-surface-below-ring'])
    features['stalk-color-above-ring'] = st.selectbox("Color Above Ring", FEATURE_OPTIONS['stalk-color-above-ring'])
    features['stalk-color-below-ring'] = st.selectbox("Color Below Ring", FEATURE_OPTIONS['stalk-color-below-ring'])

with st.sidebar.expander("💍 RING & VEIL", expanded=False):
    features['veil-type'] = st.selectbox("Veil Type", FEATURE_OPTIONS['veil-type'])
    features['veil-color'] = st.selectbox("Veil Color", FEATURE_OPTIONS['veil-color'])
    features['ring-number'] = st.selectbox("Ring Number", FEATURE_OPTIONS['ring-number'])
    features['ring-type'] = st.selectbox("Ring Type", FEATURE_OPTIONS['ring-type'])

with st.sidebar.expander("🔬 SPORE & HABITAT", expanded=False):
    features['spore-print-color'] = st.selectbox("Spore Print Color", FEATURE_OPTIONS['spore-print-color'])
    features['population'] = st.selectbox("Population", FEATURE_OPTIONS['population'])
    features['habitat'] = st.selectbox("Habitat", FEATURE_OPTIONS['habitat'])

st.markdown('<h1 class="main-header">🍄 Mushroom Safety Classifier</h1>', unsafe_allow_html=True)
st.markdown("### Select features and click predict!")

st.sidebar.markdown("---")
predict_btn = st.sidebar.button("🔮 PREDICT SAFETY", type="primary", use_container_width=True)

if predict_btn:
    input_df = encode_input(features)
    prediction = model.predict(input_df)[0]
    probability = model.predict_proba(input_df)[0]
    confidence = probability[prediction]
    is_edible = prediction == 1

    st.markdown("---")
    col1, col2 = st.columns([1, 1])

    with col1:
        if is_edible:
            st.markdown(f'<div class="prediction-box edible"><h1>🍄 EDIBLE</h1><p>{confidence:.1%} Confidence</p></div>', unsafe_allow_html=True)
        else:
            st.markdown(f'<div class="prediction-box poisonous"><h1>💀 POISONOUS</h1><p>{confidence:.1%} Confidence</p></div>', unsafe_allow_html=True)

    with col2:
        if is_edible:
            risk = "🟢 LOW RISK" if confidence > 0.9 else ("🟡 MEDIUM RISK" if confidence > 0.7 else "🟠 HIGH RISK")
        else:
            risk = "🔴 EXTREME RISK" if confidence > 0.9 else ("🔴 HIGH RISK" if confidence > 0.7 else "🟠 ELEVATED RISK")
        st.markdown(f'<div class="feature-card"><h3>Risk Assessment</h3><p>{risk}</p></div>', unsafe_allow_html=True)

    prob_df = pd.DataFrame({'Class': ['Edible', 'Poisonous'], 'Probability': [probability[1], probability[0]]})
    st.bar_chart(prob_df.set_index('Class'))

    if not is_edible:
        st.error("WARNING: This mushroom is predicted to be POISONOUS. DO NOT EAT!")
    else:
        st.success("This mushroom is predicted to be EDIBLE.")

st.markdown("---")
tab1, tab2 = st.tabs(["Model Info", "Safety"])

with tab1:
    st.markdown("### Model Information")
    st.markdown("XGBoost classifier with 99%+ accuracy on UCI Mushroom dataset.")
with tab2:
    st.markdown("### Safety Disclaimer")
    st.markdown("**NEVER** rely solely on an app. **ALWAYS** consult experts. When in doubt, throw it out.")

st.markdown("<p style='text-align:center;color:gray;'>🍄 For Educational Use Only</p>", unsafe_allow_html=True)
