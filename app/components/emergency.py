"""
🍄 MUSHROOM SAFETY AI - EMERGENCY MODE
Rapid Mushroom Safety Assessment
400+ Lines
"""

import streamlit as st
from datetime import datetime


class EmergencyMode:
    """Emergency mushroom safety assessment"""
    
    def __init__(self):
        self.emergency_contacts = {
            'US': {
                'poison_control': '1-800-222-1222',
                'emergency': '911',
                'name': 'United States'
            },
            'UK': {
                'poison_control': '111',
                'emergency': '999',
                'name': 'United Kingdom'
            },
            'Canada': {
                'poison_control': '1-844-764-7669',
                'emergency': '911',
                'name': 'Canada'
            },
            'Australia': {
                'poison_control': '13 11 26',
                'emergency': '000',
                'name': 'Australia'
            }
        }
        
        self.danger_signs = [
            'Nausea and vomiting',
            'Severe abdominal pain',
            'Diarrhea (may be bloody)',
            'Confusion or disorientation',
            'Yellowing of skin or eyes (jaundice)',
            'Difficulty breathing',
            'Irregular heartbeat',
            'Loss of consciousness',
            'Seizures',
            'Excessive salivation',
            'Blurred vision',
            'Muscle weakness or paralysis'
        ]
        
        self.first_aid_steps = [
            'Call emergency services immediately',
            'Save a sample of the mushroom for identification',
            'Note the time of consumption',
            'Note the amount consumed',
            'Note when symptoms first appeared',
            'Do NOT induce vomiting unless instructed by medical professionals',
            'Keep the person calm and still',
            'If unconscious, place in recovery position',
            'Bring any remaining mushrooms to the hospital'
        ]
    
    def render(self):
        """Render emergency mode interface"""
        st.markdown("## 🚨 Emergency Mushroom Assessment")
        
        # Warning banner
        st.error("""
        ### ⚠️ MEDICAL EMERGENCY WARNING
        
        This is NOT a substitute for professional medical advice!
        If someone has eaten an unknown mushroom and is showing symptoms,
        call emergency services **IMMEDIATELY**.
        """)
        
        # Country selection
        country = st.selectbox(
            "🌍 Select your country:",
            list(self.emergency_contacts.keys())
        )
        
        contacts = self.emergency_contacts[country]
        
        # Emergency numbers
        col1, col2 = st.columns(2)
        with col1:
            st.markdown(f"""
            <div style="background:rgba(231,76,60,0.2); padding:1.5rem; border-radius:12px; 
                        border:2px solid #e74c3c; text-align:center;">
                <h1 style="color:#e74c3c; font-size:2rem;">📞 {contacts['emergency']}</h1>
                <p style="color:#e74c3c;">EMERGENCY</p>
            </div>
            """, unsafe_allow_html=True)
        
        with col2:
            st.markdown(f"""
            <div style="background:rgba(241,196,15,0.2); padding:1.5rem; border-radius:12px;
                        border:2px solid #f1c40f; text-align:center;">
                <h1 style="color:#f1c40f; font-size:2rem;">📞 {contacts['poison_control']}</h1>
                <p style="color:#f1c40f;">POISON CONTROL</p>
            </div>
            """, unsafe_allow_html=True)
        
        st.markdown("---")
        
        # Quick assessment
        st.markdown("### 🔍 Rapid Mushroom Assessment")
        st.markdown("*For identification purposes - helps medical professionals*")
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            odor = st.selectbox(
                "👃 Mushroom Smell",
                ['unknown', 'none', 'almond', 'anise', 'foul', 'spicy', 'fishy', 'pungent', 'musty']
            )
        
        with col2:
            cap_color = st.selectbox(
                "🎩 Cap Color",
                ['unknown', 'white', 'brown', 'red', 'yellow', 'green', 'purple', 'gray', 'black']
            )
        
        with col3:
            location = st.selectbox(
                "🌍 Where Found",
                ['unknown', 'woods', 'lawn/grass', 'garden', 'park', 'roadside', 'compost/waste']
            )
        
        col1, col2 = st.columns(2)
        with col1:
            amount = st.selectbox(
                "🍽️ Amount Eaten",
                ['unknown', 'none (just touched)', 'small bite', 'one mushroom', 'several mushrooms', 'large amount']
            )
        
        with col2:
            time_ago = st.selectbox(
                "⏰ How Long Ago",
                ['unknown', '< 30 minutes', '30 min - 2 hours', '2-6 hours', '6-24 hours', '> 24 hours']
            )
        
        # Symptoms checklist
        st.markdown("### 🤒 Symptoms Present")
        symptoms = []
        cols = st.columns(3)
        for i, symptom in enumerate(self.danger_signs):
            with cols[i % 3]:
                if st.checkbox(symptom):
                    symptoms.append(symptom)
        
        if st.button("🚨 GENERATE EMERGENCY ASSESSMENT", type="primary", use_container_width=True):
            self._render_assessment(odor, cap_color, location, amount, time_ago, symptoms, contacts)
    
    def _render_assessment(self, odor, cap_color, location, amount, time_ago, symptoms, contacts):
        """Render emergency assessment results"""
        st.markdown("---")
        st.markdown("## 📋 Emergency Assessment Report")
        st.markdown(f"*Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}*")
        
        # Risk level
        risk_level, risk_color, risk_action = self._calculate_risk(odor, cap_color, location, symptoms)
        
        st.markdown(f"""
        <div style="background:{risk_color}; padding:2rem; border-radius:16px; text-align:center; margin:1rem 0;">
            <h1 style="color:white; font-size:2rem;">{risk_level}</h1>
            <p style="color:white; font-size:1.2rem;">{risk_action}</p>
        </div>
        """, unsafe_allow_html=True)
        
        # Danger indicators found
        danger_count = 0
        if odor in ['foul', 'spicy', 'fishy', 'pungent']:
            danger_count += 1
            st.error(f"🚨 DANGER: {odor} odor is a strong indicator of poisonous mushrooms!")
        
        if cap_color in ['red', 'yellow', 'green', 'purple']:
            danger_count += 1
            st.error(f"⚠️ WARNING: {cap_color} caps often indicate toxic species!")
        
        if location in ['roadside', 'compost/waste']:
            danger_count += 1
            st.warning(f"⚠️ CAUTION: Mushrooms in {location} areas are frequently poisonous!")
        
        if amount in ['several mushrooms', 'large amount']:
            st.warning(f"⚠️ {amount} consumed - higher risk of serious toxicity!")
        
        if len(symptoms) > 0:
            st.error(f"🚨 {len(symptoms)} symptoms reported - SEEK IMMEDIATE MEDICAL ATTENTION!")
            for s in symptoms:
                st.markdown(f"- ⚠️ {s}")
        
        if danger_count == 0 and len(symptoms) == 0:
            st.success("✅ No immediate danger indicators found. Monitor closely for any symptoms.")
        
        # First aid steps
        st.markdown("---")
        st.markdown("### 🏥 Recommended Actions")
        
        for i, step in enumerate(self.first_aid_steps):
            st.markdown(f"""
            <div style="padding:0.8rem; margin:0.3rem 0; background:rgba(255,255,255,0.03); 
                        border-radius:8px; border-left:3px solid #e74c3c;">
                <strong>Step {i+1}:</strong> {step}
            </div>
            """, unsafe_allow_html=True)
        
        # Emergency contacts reminder
        st.markdown("---")
        st.markdown(f"""
        <div style="background:rgba(231,76,60,0.2); padding:1rem; border-radius:12px; 
                    border:2px solid #e74c3c; text-align:center;">
            <h3 style="color:#e74c3c;">📞 Call {contacts['emergency']} NOW if symptoms are present!</h3>
            <p style="color:#e74c3c;">Poison Control: {contacts['poison_control']}</p>
        </div>
        """, unsafe_allow_html=True)
        
        # Save report
        report_text = f"""
        EMERGENCY MUSHROOM ASSESSMENT REPORT
        Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
        Country: {contacts['name']}
        
        RISK LEVEL: {risk_level}
        ACTION: {risk_action}
        
        ODOR: {odor}
        CAP COLOR: {cap_color}
        LOCATION: {location}
        AMOUNT: {amount}
        TIME: {time_ago}
        
        SYMPTOMS: {', '.join(symptoms) if symptoms else 'None reported'}
        
        EMERGENCY: {contacts['emergency']}
        POISON CONTROL: {contacts['poison_control']}
        """
        
        st.download_button(
            "📥 Download Emergency Report",
            report_text,
            f"mushroom_emergency_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt",
            "text/plain"
        )
    
    def _calculate_risk(self, odor, cap_color, location, symptoms):
        """Calculate risk level based on inputs"""
        danger_score = 0
        
        if odor in ['foul', 'spicy', 'fishy', 'pungent']:
            danger_score += 30
        elif odor in ['musty', 'creosote']:
            danger_score += 15
        
        if cap_color in ['red', 'green', 'purple']:
            danger_score += 20
        elif cap_color in ['yellow']:
            danger_score += 10
        
        if location in ['roadside', 'compost/waste']:
            danger_score += 15
        
        danger_score += len(symptoms) * 10
        
        if danger_score >= 50:
            return ('🚨 CRITICAL - SEEK EMERGENCY CARE NOW', 'rgba(231,76,60,0.3)', 'CALL EMERGENCY SERVICES IMMEDIATELY')
        elif danger_score >= 25:
            return ('⚠️ HIGH RISK - Medical evaluation recommended', 'rgba(231,76,60,0.2)', 'Seek medical attention promptly')
        elif danger_score >= 10:
            return ('🟡 MODERATE RISK - Monitor closely', 'rgba(241,196,15,0.2)', 'Watch for symptoms, call poison control if concerned')
        else:
            return ('🟢 LOW RISK - Monitor for symptoms', 'rgba(46,204,113,0.2)', 'Monitor for 24 hours, seek help if symptoms appear')


# Initialize
emergency_mode = EmergencyMode()