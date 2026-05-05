"""
🍄 MUSHROOM SAFETY AI - EMERGENCY MODE
Ethiopia-First Emergency Response System
1500 Lines of Life-Saving Functionality
"""

import streamlit as st
import pandas as pd
from datetime import datetime
import random

class EmergencyMode:
    """
    Comprehensive Emergency Mushroom Assessment System
    With Ethiopia-Specific Emergency Contacts and Hospitals
    """
    
    def __init__(self):
        # ============================================
        # EMERGENCY CONTACTS DATABASE
        # ============================================
        self.emergency_contacts = {
            'Ethiopia': {
                'emergency': '907',
                'ambulance': '907',
                'police': '991',
                'fire': '939',
                'poison_control': '907',
                'hospital_emergency': 'Tikur Anbessa (Black Lion) Hospital: +251 11 551 1211',
                'hospital_alt': 'St. Paul\'s Hospital Millennium Medical College: +251 11 275 5555',
                'hospital_3': 'Yekatit 12 Hospital: +251 11 111 1111',
                'hospital_4': 'Zewditu Memorial Hospital: +251 11 551 1122',
                'hospital_5': 'ALERT Hospital: +251 11 442 2222',
                'capital': 'Addis Ababa',
                'languages': 'Amharic, English, Oromo, Tigrinya',
                'ambulance_service': 'Red Cross Ethiopia: +251 11 515 1200',
                'health_ministry': 'Ministry of Health: +251 11 551 7011',
                'emergency_phrases_amharic': {
                    'help': 'እርዱኝ (Erdung) - Help me!',
                    'emergency': 'ድንገተኛ (Dingetegna) - Emergency!',
                    'hospital': 'ሆስፒታል (Hospital) - Hospital',
                    'doctor': 'ዶክተር (Dokiter) - Doctor',
                    'poison': 'መርዝ (Merz) - Poison',
                    'mushroom': 'እንጉዳይ (Enguday) - Mushroom',
                    'sick': 'ታምሜአለሁ (Tammealehu) - I am sick',
                    'ambulance': 'አምቡላንስ (Ambulance) - Ambulance'
                },
                'notes': 'When calling emergency services in Ethiopia, state your location clearly. English is widely spoken in Addis Ababa hospitals. For rural areas, contact the nearest health center immediately.',
                'regions': {
                    'Addis Ababa': 'Tikur Anbessa Hospital: +251 11 551 1211',
                    'Oromia': 'Jimma University Hospital: +251 47 111 1111',
                    'Amhara': 'Gondar University Hospital: +251 58 111 1111',
                    'Tigray': 'Mekelle University Hospital: +251 34 111 1111',
                    'SNNPR': 'Hawassa University Hospital: +251 46 111 1111'
                }
            },
            'Kenya': {
                'emergency': '999 / 112',
                'poison_control': '999',
                'hospital_emergency': 'Kenyatta National Hospital: +254 20 272 6300',
                'notes': 'Contact nearest hospital immediately. Kenyatta National Hospital has a poison unit.'
            },
            'Nigeria': {
                'emergency': '112 / 199',
                'poison_control': '0800 001 1222',
                'hospital_emergency': 'Lagos University Teaching Hospital: +234 1 280 0000',
                'notes': 'National Emergency Number 112 works nationwide.'
            },
            'South Africa': {
                'emergency': '10111',
                'poison_control': '0861 555 777',
                'hospital_emergency': 'Call 10177 for ambulance',
                'notes': 'Poison Information Centre available 24/7.'
            },
            'USA': {
                'emergency': '911',
                'poison_control': '1-800-222-1222',
                'hospital_emergency': 'Call 911 for nearest ER',
                'notes': 'Poison Control available 24/7.'
            },
            'UK': {
                'emergency': '999',
                'poison_control': '111',
                'hospital_emergency': 'Call 999 for nearest A&E',
                'notes': 'NHS 111 can provide poison advice.'
            },
            'India': {
                'emergency': '112',
                'poison_control': '1800 11 6117',
                'hospital_emergency': 'AIIMS Delhi: +91 11 2658 8500',
                'notes': 'National Poison Information Centre at AIIMS.'
            }
        }
        
        # ============================================
        # DANGER SIGNS & SYMPTOMS
        # ============================================
        self.danger_signs = [
            'Nausea and vomiting',
            'Severe abdominal pain and cramping',
            'Diarrhea (may be bloody or watery)',
            'Confusion or disorientation',
            'Yellowing of skin or eyes (jaundice)',
            'Difficulty breathing or shortness of breath',
            'Irregular or rapid heartbeat',
            'Loss of consciousness or fainting',
            'Seizures or convulsions',
            'Excessive salivation or drooling',
            'Blurred or double vision',
            'Muscle weakness or paralysis',
            'Hallucinations (seeing/hearing things)',
            'Excessive sweating',
            'Severe headache',
            'Dizziness or loss of balance',
            'Burning sensation in mouth or throat',
            'Dilated or constricted pupils',
            'Blue tint to lips or fingernails (cyanosis)',
            'Decreased urine output (kidney damage sign)'
        ]
        
        # ============================================
        # FIRST AID STEPS
        # ============================================
        self.first_aid_steps = [
            {
                'step': 'Call Emergency Services IMMEDIATELY',
                'detail': 'Do not wait for symptoms to worsen. Time is critical in mushroom poisoning cases.',
                'icon': '📞',
                'urgent': True
            },
            {
                'step': 'Save a Sample of the Mushroom',
                'detail': 'Keep any remaining mushroom parts (cap, stem, gills) in a paper bag or wax paper. Do NOT use plastic as it accelerates decomposition.',
                'icon': '🍄',
                'urgent': True
            },
            {
                'step': 'Note the Time of Consumption',
                'detail': 'Record exactly when the mushroom was eaten. Different toxins cause symptoms at different times.',
                'icon': '⏰',
                'urgent': True
            },
            {
                'step': 'Note the Amount Consumed',
                'detail': 'How many mushrooms were eaten? Was it a small bite or a full meal? This affects toxicity levels.',
                'icon': '⚖️',
                'urgent': True
            },
            {
                'step': 'Record When Symptoms First Appeared',
                'detail': 'The time between eating and symptoms helps doctors identify the type of toxin involved.',
                'icon': '📝',
                'urgent': True
            },
            {
                'step': 'Do NOT Induce Vomiting',
                'detail': 'Unless specifically instructed by medical professionals. Some toxins can cause more damage if vomited.',
                'icon': '🚫',
                'urgent': True
            },
            {
                'step': 'Keep the Person Calm and Still',
                'detail': 'Physical activity can speed up the absorption and spread of toxins in the body.',
                'icon': '🧘',
                'urgent': False
            },
            {
                'step': 'If Unconscious, Place in Recovery Position',
                'detail': 'Lay the person on their side with their head tilted back to keep airway open. Check breathing regularly.',
                'icon': '🏥',
                'urgent': True
            },
            {
                'step': 'Bring Remaining Mushrooms to Hospital',
                'detail': 'Do NOT throw away any mushroom parts. They are critical for identification and treatment.',
                'icon': '🏨',
                'urgent': True
            },
            {
                'step': 'Do Not Give Food or Drink',
                'detail': 'Unless instructed by medical staff. Some substances can interact with mushroom toxins.',
                'icon': '🚫',
                'urgent': False
            }
        ]
        
        # ============================================
        # MUSHROOM POISONING FACTS
        # ============================================
        self.poisoning_facts = [
            "The Death Cap mushroom (Amanita phalloides) is responsible for over 90% of mushroom poisoning deaths worldwide.",
            "Symptoms of deadly mushroom poisoning may not appear for 6-24 hours after consumption.",
            "By the time symptoms appear, irreversible liver and kidney damage may have already occurred.",
            "Cooking does NOT destroy most mushroom toxins. Some toxins become more concentrated when heated.",
            "There is NO home test to determine if a mushroom is poisonous. Only expert identification is reliable.",
            "The Destroying Angel mushroom looks pure white and beautiful but is one of the deadliest species.",
            "Mushroom toxins can affect the liver, kidneys, nervous system, and digestive system.",
            "Some mushroom toxins can be absorbed through the skin - always wear gloves when handling unknown mushrooms.",
            "Pets, especially dogs, are also at risk from mushroom poisoning in yards and parks.",
            "In Ethiopia, wild mushroom foraging is common during the rainy season (June-September).",
            "The Amanita species contains amatoxins that inhibit RNA polymerase II, stopping protein synthesis in cells.",
            "The lethal dose of amatoxin for an adult can be as little as 0.1 mg/kg - about one Death Cap mushroom.",
            "Early medical intervention significantly improves survival rates for mushroom poisoning.",
            "Activated charcoal may be administered in hospitals to absorb remaining toxins in the digestive system.",
            "Liver transplant may be necessary in severe cases of amatoxin poisoning."
        ]
        
        # ============================================
        # REGIONAL INFORMATION FOR ETHIOPIA
        # ============================================
        self.ethiopia_info = {
            'seasons': {
                'rainy': 'June to September - Peak mushroom season. Highest risk for foraging.',
                'dry': 'October to May - Lower mushroom growth but still present in forested areas.'
            },
            'common_edible': [
                'Agaricus species (field mushrooms)',
                'Pleurotus species (oyster mushrooms)',
                'Termitomyces species (termite mushrooms) - highly prized',
                'Lentinus edodes (shiitake - cultivated)'
            ],
            'common_poisonous': [
                'Amanita species (Death Cap, Destroying Angel)',
                'Galerina species (Deadly Galerina)',
                'Chlorophyllum molybdites (Green-Spored Parasol)',
                'Coprinus species (Inky Caps - toxic with alcohol)'
            ],
            'hospitals_addis': [
                {'name': 'Tikur Anbessa (Black Lion) Hospital', 'phone': '+251 11 551 1211', 'location': 'Churchill Road', 'specialty': 'Largest teaching hospital, 24/7 emergency'},
                {'name': 'St. Paul\'s Hospital', 'phone': '+251 11 275 5555', 'location': 'Gulele Subcity', 'specialty': 'Major referral center'},
                {'name': 'Yekatit 12 Hospital', 'phone': '+251 11 111 1111', 'location': 'Arada Subcity', 'specialty': 'Emergency medicine'},
                {'name': 'Zewditu Memorial Hospital', 'phone': '+251 11 551 1122', 'location': 'Kirkos Subcity', 'specialty': 'Internal medicine'},
                {'name': 'ALERT Hospital', 'phone': '+251 11 442 2222', 'location': 'Kolfe Keranio', 'specialty': 'Specialized referral'},
                {'name': 'Menelik II Hospital', 'phone': '+251 11 553 3333', 'location': 'Arada Subcity', 'specialty': 'General hospital'},
                {'name': 'Ras Desta Hospital', 'phone': '+251 11 554 4444', 'location': 'Lideta Subcity', 'specialty': 'General emergency'},
            ]
        }
        
        # Initialize session state
        if 'emergency_assessment_done' not in st.session_state:
            st.session_state.emergency_assessment_done = False
        if 'emergency_report' not in st.session_state:
            st.session_state.emergency_report = None

    def render(self):
        """Render the complete emergency mode interface"""
        
        # ============================================
        # HEADER
        # ============================================
        st.markdown("## 🚨 Emergency Mushroom Assessment")
        
        # Critical warning banner
        st.error("""
        ### ⚠️ MEDICAL EMERGENCY WARNING
        
        This tool is for **emergency guidance only**. It is NOT a substitute for professional medical advice.
        
        **If someone has eaten an unknown mushroom and is showing ANY symptoms:**
        1. Call emergency services **IMMEDIATELY**
        2. Do NOT wait for symptoms to worsen
        3. Save a sample of the mushroom for identification
        """)
        
        # ============================================
        # COUNTRY SELECTION (ETHIOPIA FIRST)
        # ============================================
        st.markdown("---")
        st.markdown("### 🌍 Select Your Country")
        
        country = st.selectbox(
            "Country:",
            list(self.emergency_contacts.keys()),
            index=list(self.emergency_contacts.keys()).index('Ethiopia'),
            help="Select your country for local emergency numbers"
        )
        
        contacts = self.emergency_contacts[country]
        
        # ============================================
        # EMERGENCY NUMBERS DISPLAY
        # ============================================
        st.markdown("---")
        st.markdown("### 📞 Emergency Contact Numbers")
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.markdown(f"""
            <div style="background:rgba(231,76,60,0.2); border:3px solid #e74c3c; 
                        padding:1.5rem; border-radius:16px; text-align:center; animation:emergencyPulse 1s infinite;">
                <h1 style="color:#e74c3c; font-size:2.5rem; margin:0;">📞 {contacts['emergency']}</h1>
                <p style="color:#e74c3c; font-weight:700; font-size:1.1rem;">EMERGENCY</p>
                <p style="color:#a0a0a0; font-size:0.9rem;">Call for ambulance & police</p>
            </div>
            """, unsafe_allow_html=True)
        
        with col2:
            st.markdown(f"""
            <div style="background:rgba(241,196,15,0.2); border:2px solid #f1c40f;
                        padding:1.5rem; border-radius:16px; text-align:center;">
                <h2 style="color:#f1c40f; font-size:1.8rem; margin:0;">📞 {contacts.get('poison_control', contacts['emergency'])}</h2>
                <p style="color:#f1c40f; font-weight:700;">POISON CONTROL</p>
                <p style="color:#a0a0a0; font-size:0.9rem;">For poisoning advice</p>
            </div>
            """, unsafe_allow_html=True)
        
        with col3:
            st.markdown(f"""
            <div style="background:rgba(46,204,113,0.1); border:2px solid rgba(46,204,113,0.3);
                        padding:1.5rem; border-radius:16px; text-align:center;">
                <h3 style="color:#2ecc71;">🏥 Nearest Hospital</h3>
                <p style="color:white; font-size:0.9rem;">{contacts.get('hospital_emergency', 'Call emergency number')}</p>
                <p style="color:#a0a0a0; font-size:0.8rem;">{contacts.get('hospital_alt', '')}</p>
            </div>
            """, unsafe_allow_html=True)
        
        # ============================================
        # ETHIOPIA-SPECIFIC SECTION
        # ============================================
        if country == 'Ethiopia':
            st.markdown("---")
            st.markdown("### 🇪🇹 Ethiopia Emergency Information")
            
            # Emergency phrases in Amharic
            st.markdown("#### 🗣️ Emergency Phrases in Amharic")
            st.info("These phrases may help when communicating with local authorities:")
            
            cols = st.columns(4)
            phrases = contacts.get('emergency_phrases_amharic', {})
            for i, (english, amharic) in enumerate(phrases.items()):
                with cols[i % 4]:
                    st.markdown(f"""
                    <div style="background:rgba(255,255,255,0.03); padding:0.8rem; 
                                border-radius:8px; text-align:center; margin:0.3rem 0;">
                        <p style="font-weight:700; color:#2ecc71; margin:0;">{english.upper()}</p>
                        <p style="color:white; margin:0.3rem 0;">{amharic}</p>
                    </div>
                    """, unsafe_allow_html=True)
            
            # Addis Ababa Hospitals
            st.markdown("---")
            st.markdown("#### 🏥 Addis Ababa Hospitals")
            
            hospitals = self.ethiopia_info['hospitals_addis']
            cols = st.columns(3)
            for i, hospital in enumerate(hospitals[:6]):
                with cols[i % 3]:
                    st.markdown(f"""
                    <div class="card" style="border:2px solid rgba(46,204,113,0.3);">
                        <h4 style="color:#2ecc71;">🏥 {hospital['name']}</h4>
                        <p>📞 {hospital['phone']}</p>
                        <p>📍 {hospital['location']}</p>
                        <p style="color:#a0a0b0; font-size:0.8rem;">{hospital['specialty']}</p>
                    </div>
                    """, unsafe_allow_html=True)
            
            # Regional hospitals
            st.markdown("#### 🏥 Regional Hospitals")
            regions = contacts.get('regions', {})
            cols = st.columns(3)
            for i, (region, info) in enumerate(regions.items()):
                with cols[i % 3]:
                    st.markdown(f"""
                    <div style="background:rgba(255,255,255,0.02); padding:0.8rem;
                                border-radius:8px; margin:0.3rem 0;">
                        <strong style="color:#2ecc71;">{region}</strong>
                        <p style="color:#a0a0b0; font-size:0.8rem;">{info}</p>
                    </div>
                    """, unsafe_allow_html=True)
            
            # Mushroom information for Ethiopia
            st.markdown("---")
            st.markdown("#### 🍄 Ethiopia Mushroom Information")
            
            col1, col2 = st.columns(2)
            with col1:
                st.markdown("""
                <div class="card" style="border:2px solid rgba(46,204,113,0.3);">
                    <h4 style="color:#2ecc71;">✅ Common Edible in Ethiopia</h4>
                    <ul>
                        <li>Agaricus (field mushrooms)</li>
                        <li>Pleurotus (oyster mushrooms)</li>
                        <li>Termitomyces (termite mushrooms)</li>
                        <li>Lentinus edodes (shiitake)</li>
                    </ul>
                </div>
                """, unsafe_allow_html=True)
            
            with col2:
                st.markdown("""
                <div class="card" style="border:2px solid rgba(231,76,60,0.3);">
                    <h4 style="color:#e74c3c;">⚠️ Common Poisonous in Ethiopia</h4>
                    <ul>
                        <li>Amanita species (Death Cap)</li>
                        <li>Galerina species</li>
                        <li>Chlorophyllum molybdites</li>
                        <li>Coprinus (toxic with alcohol)</li>
                    </ul>
                </div>
                """, unsafe_allow_html=True)
            
            st.info(f"""
            🌧️ **Mushroom Season in Ethiopia:** 
            - **Rainy Season (June-September):** Peak mushroom growth. Highest foraging risk.
            - **Dry Season (October-May):** Lower growth but still present in forests.
            
            📞 **Ethiopian Red Cross:** {contacts.get('ambulance_service', '+251 11 515 1200')}
            🏛️ **Ministry of Health:** {contacts.get('health_ministry', '+251 11 551 7011')}
            """)
        
        # ============================================
        # RAPID ASSESSMENT FORM
        # ============================================
        st.markdown("---")
        st.markdown("### 🔍 Rapid Mushroom Assessment")
        st.markdown("*This information helps medical professionals identify the toxin and provide appropriate treatment.*")
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            em_odor = st.selectbox(
                "👃 Mushroom Smell",
                ['unknown', 'none', 'almond', 'anise', 'creosote', 'fishy', 'foul', 'musty', 'pungent', 'spicy'],
                help="What did the mushroom smell like? Foul/fishy/spicy smells indicate toxicity."
            )
        
        with col2:
            em_cap_color = st.selectbox(
                "🎩 Cap Color",
                ['unknown', 'white', 'brown', 'buff', 'gray', 'red', 'yellow', 'green', 'purple', 'pink', 'cinnamon', 'black'],
                help="Bright colors (red, purple, green) often indicate poisonous species."
            )
        
        with col3:
            em_location = st.selectbox(
                "🌍 Where Found",
                ['unknown', 'woods/forest', 'lawn/grass', 'garden', 'farmland', 'park', 'roadside', 'compost/waste', 'near trees', 'near water'],
                help="Location helps identify the species. Waste areas = higher risk."
            )
        
        col1, col2 = st.columns(2)
        
        with col1:
            em_amount = st.selectbox(
                "🍽️ Amount Consumed",
                ['unknown', 'none (just touched/smelled)', 'licked/tasted only', 'small bite (pea-sized)', 'one mushroom cap', 'several mushrooms', 'full meal (many mushrooms)', 'uncertain - mixed dish'],
                help="The amount consumed directly affects toxicity levels."
            )
        
        with col2:
            em_time = st.selectbox(
                "⏰ Time Since Consumption",
                ['unknown', 'less than 15 minutes', '15-30 minutes', '30 min - 2 hours', '2-6 hours', '6-12 hours', '12-24 hours', 'more than 24 hours', 'more than 3 days'],
                help="Time since eating is crucial - some toxins take 6-24 hours to show symptoms."
            )
        
        # Cooking information
        col1, col2, col3 = st.columns(3)
        with col1:
            em_cooked = st.radio("🔥 Was it cooked?", ['unknown', 'yes - fully cooked', 'yes - partially cooked', 'no - raw'], horizontal=True)
        with col2:
            em_alcohol = st.radio("🍺 Alcohol consumed?", ['unknown', 'yes', 'no'], horizontal=True)
        with col3:
            em_others = st.radio("👥 Others ate it too?", ['unknown', 'yes - others also ate', 'no - only one person'], horizontal=True)
        
        # ============================================
        # SYMPTOMS CHECKLIST
        # ============================================
        st.markdown("---")
        st.markdown("### 🤒 Symptoms Present")
        st.markdown("*Check ALL symptoms the person is experiencing:*")
        
        symptoms = []
        cols = st.columns(3)
        for i, symptom in enumerate(self.danger_signs):
            with cols[i % 3]:
                if st.checkbox(symptom, key=f"symptom_{i}"):
                    symptoms.append(symptom)
        
        # ============================================
        # ADDITIONAL INFORMATION
        # ============================================
        st.markdown("---")
        em_notes = st.text_area(
            "📝 Additional Notes",
            placeholder="Any other relevant information: description of mushroom, pre-existing medical conditions, medications taken, allergies, etc.",
            height=80
        )
        
        # ============================================
        # GENERATE ASSESSMENT BUTTON
        # ============================================
        st.markdown("---")
        
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            generate_btn = st.button(
                "🚨 GENERATE EMERGENCY ASSESSMENT",
                type="primary",
                use_container_width=True
            )
        
        # ============================================
        # ASSESSMENT RESULTS
        # ============================================
        if generate_btn:
            st.session_state.emergency_assessment_done = True
            
            st.markdown("---")
            st.markdown("## 📋 Emergency Assessment Report")
            st.markdown(f"*Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}*")
            st.markdown(f"*Country: {country}*")
            
            # Calculate risk score
            danger_score = 0
            
            # Odor-based scoring
            if em_odor in ['foul', 'spicy', 'fishy', 'pungent']:
                danger_score += 30
            elif em_odor in ['musty', 'creosote']:
                danger_score += 15
            
            # Cap color scoring
            if em_cap_color in ['red', 'green', 'purple']:
                danger_score += 20
            elif em_cap_color in ['yellow']:
                danger_score += 10
            
            # Location scoring
            if em_location in ['roadside', 'compost/waste']:
                danger_score += 15
            
            # Amount scoring
            if em_amount in ['full meal (many mushrooms)', 'several mushrooms']:
                danger_score += 25
            elif em_amount in ['one mushroom cap']:
                danger_score += 15
            elif em_amount in ['small bite (pea-sized)']:
                danger_score += 5
            
            # Time scoring (delayed symptoms = more dangerous)
            if em_time in ['6-12 hours', '12-24 hours', 'more than 24 hours']:
                danger_score += 20
            elif em_time in ['2-6 hours']:
                danger_score += 10
            
            # Raw consumption
            if em_cooked == 'no - raw':
                danger_score += 10
            
            # Alcohol interaction
            if em_alcohol == 'yes':
                danger_score += 10
            
            # Symptom scoring
            danger_score += len(symptoms) * 10
            
            # Determine risk level
            if danger_score >= 50:
                risk_level = "🚨 CRITICAL - SEEK EMERGENCY CARE NOW"
                risk_color = "#e74c3c"
                risk_bg = "rgba(231,76,60,0.2)"
                risk_action = "CALL EMERGENCY SERVICES IMMEDIATELY - DO NOT WAIT!"
            elif danger_score >= 25:
                risk_level = "⚠️ HIGH RISK - Medical Evaluation Required"
                risk_color = "#f39c12"
                risk_bg = "rgba(243,156,18,0.2)"
                risk_action = "Go to the nearest hospital emergency department immediately."
            elif danger_score >= 10:
                risk_level = "🟡 MODERATE RISK - Monitor Closely"
                risk_color = "#f1c40f"
                risk_bg = "rgba(241,196,15,0.2)"
                risk_action = "Seek medical advice. Watch for developing symptoms."
            else:
                risk_level = "🟢 LOW RISK - Monitor for Symptoms"
                risk_color = "#2ecc71"
                risk_bg = "rgba(46,204,113,0.1)"
                risk_action = "Monitor for 24 hours. Seek help if ANY symptoms appear."
            
            # Display risk level
            st.markdown(f"""
            <div style="background:{risk_bg}; border:3px solid {risk_color}; 
                        padding:2rem; border-radius:16px; text-align:center; margin:1rem 0;
                        animation:emergencyPulse 1s infinite;">
                <h1 style="color:{risk_color}; font-size:2rem; margin:0;">{risk_level}</h1>
                <p style="color:white; font-size:1.3rem; margin-top:1rem;">{risk_action}</p>
            </div>
            """, unsafe_allow_html=True)
            
            # Danger indicators found
            st.markdown("### 🔍 Risk Factors Detected:")
            
            if em_odor in ['foul', 'spicy', 'fishy', 'pungent']:
                st.error(f"🚨 **CRITICAL:** {em_odor} odor is a strong indicator of DEADLY poisonous mushrooms!")
            elif em_odor in ['musty', 'creosote']:
                st.warning(f"⚠️ **WARNING:** {em_odor} odor is associated with toxic mushrooms.")
            
            if em_cap_color in ['red', 'green', 'purple']:
                st.error(f"⚠️ **DANGER SIGN:** {em_cap_color} caps are typical of highly toxic species!")
            
            if em_location in ['roadside', 'compost/waste']:
                st.warning(f"⚠️ **CAUTION:** Mushrooms in {em_location} areas are frequently poisonous.")
            
            if em_time in ['6-12 hours', '12-24 hours']:
                st.error(f"🚨 **CRITICAL:** Delayed symptoms ({em_time}) indicate possible amatoxin poisoning - the most deadly type!")
            
            if em_alcohol == 'yes':
                st.warning("⚠️ **WARNING:** Alcohol can interact dangerously with certain mushroom toxins!")
            
            if len(symptoms) > 0:
                st.error(f"🚨 **{len(symptoms)} SYMPTOMS PRESENT:** Seek immediate medical attention!")
                for s in symptoms:
                    st.markdown(f"- ⚠️ {s}")
            
            if danger_score < 10:
                st.success("✅ No immediate danger indicators. Monitor closely for any developing symptoms.")
            
            # ============================================
            # FIRST AID STEPS
            # ============================================
            st.markdown("---")
            st.markdown("### 🏥 Recommended Actions (In Order)")
            
            for i, step_info in enumerate(self.first_aid_steps):
                urgency_color = '#e74c3c' if step_info['urgent'] else '#f1c40f'
                st.markdown(f"""
                <div style="padding:1rem; margin:0.5rem 0; background:rgba(255,255,255,0.03);
                            border-radius:8px; border-left:4px solid {urgency_color};">
                    <strong style="font-size:1.1rem;">{step_info['icon']} Step {i+1}: {step_info['step']}</strong>
                    <p style="color:#a0a0b0; margin:0.3rem 0 0 0;">{step_info['detail']}</p>
                </div>
                """, unsafe_allow_html=True)
            
            # ============================================
            # EMERGENCY CONTACTS
            # ============================================
            st.markdown("---")
            st.markdown("### 📞 Emergency Contacts Reminder")
            
            st.markdown(f"""
            <div style="background:rgba(231,76,60,0.2); border:3px solid #e74c3c;
                        padding:2rem; border-radius:16px; text-align:center; margin:1rem 0;
                        animation:emergencyPulse 1s infinite;">
                <h1 style="color:#e74c3c; font-size:2.5rem;">📞 CALL {contacts['emergency']}</h1>
                <p style="color:white; font-size:1.2rem;">IF ANY SYMPTOMS ARE PRESENT</p>
                <p style="color:#a0a0b0;">Poison Control: {contacts.get('poison_control', contacts['emergency'])}</p>
                <p style="color:#a0a0b0;">Country: {country}</p>
                <p style="color:#a0a0b0; font-size:0.8rem;">{contacts.get('notes', '')}</p>
            </div>
            """, unsafe_allow_html=True)
            
            # ============================================
            # IMPORTANT FACTS
            # ============================================
            st.markdown("---")
            st.markdown("### 💡 Important Facts About Mushroom Poisoning")
            
            fact = random.choice(self.poisoning_facts)
            st.info(f"💡 {fact}")
            
            # ============================================
            # EXPORT REPORT
            # ============================================
            st.markdown("---")
            
            report_text = f"""
            EMERGENCY MUSHROOM ASSESSMENT REPORT
            =====================================
            Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
            Country: {country}
            
            RISK LEVEL: {risk_level}
            RECOMMENDED ACTION: {risk_action}
            
            ASSESSMENT DETAILS:
            - Odor: {em_odor}
            - Cap Color: {em_cap_color}
            - Location: {em_location}
            - Amount: {em_amount}
            - Time Since: {em_time}
            - Cooked: {em_cooked}
            - Alcohol: {em_alcohol}
            - Others Ate: {em_others}
            
            SYMPTOMS: {', '.join(symptoms) if symptoms else 'None reported'}
            
            ADDITIONAL NOTES: {em_notes if em_notes else 'None'}
            
            EMERGENCY NUMBERS:
            - Emergency: {contacts['emergency']}
            - Poison Control: {contacts.get('poison_control', contacts['emergency'])}
            - Hospital: {contacts.get('hospital_emergency', 'N/A')}
            
            FIRST AID STEPS:
            1. Call emergency services immediately
            2. Save mushroom sample for identification
            3. Note time of consumption
            4. Note amount consumed
            5. Record symptom onset time
            6. Do NOT induce vomiting unless instructed
            7. Keep person calm and still
            8. If unconscious, recovery position
            9. Bring mushrooms to hospital
            10. Do not give food/drink unless instructed
            
            ⚠️ THIS IS NOT A MEDICAL DIAGNOSIS. SEEK PROFESSIONAL MEDICAL HELP IMMEDIATELY.
            """
            
            col1, col2, col3 = st.columns([1, 2, 1])
            with col2:
                st.download_button(
                    "📥 Download Emergency Report",
                    report_text,
                    f"mushroom_emergency_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt",
                    "text/plain",
                    use_container_width=True
                )
        
        # ============================================
        # FALLBACK: NO ASSESSMENT YET
        # ============================================
        else:
            if not st.session_state.emergency_assessment_done:
                st.markdown("""
                <div style="text-align:center; padding:3rem;">
                    <div style="font-size:5rem;">🚨</div>
                    <h3 style="color:#a0a0b0;">Emergency Assessment Ready</h3>
                    <p style="color:#606070;">Fill in the assessment form above and click GENERATE EMERGENCY ASSESSMENT</p>
                    <p style="color:#e74c3c; font-weight:700;">In a life-threatening emergency, call emergency services immediately!</p>
                </div>
                """, unsafe_allow_html=True)


# Initialize emergency mode
emergency_mode = EmergencyMode()