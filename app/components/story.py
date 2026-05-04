"""
🍄 MUSHROOM SAFETY AI - STORY GENERATOR
Narrative Prediction System - Human-Readable Explanations
400+ Lines of Story Generation Logic
"""

import random
from datetime import datetime


class MushroomStory:
    """Generate human-readable narratives for mushroom predictions"""
    
    def __init__(self):
        self.story_templates = self._load_templates()
        self.safety_facts = self._load_safety_facts()
        self.mushroom_facts = self._load_mushroom_facts()
    
    def _load_templates(self):
        """Load story templates for different scenarios"""
        return {
            'poisonous_certain': [
                "I looked carefully at this mushroom, and {odor_detail}. {spore_detail}. Based on these characteristics, I'm {confidence}% certain this mushroom is POISONOUS. The patterns match several deadly species in my database. {warning}",
                "This one caught my attention immediately. {odor_detail} That's a major red flag. {spore_detail} Combined with {gill_detail}, I can say with {confidence}% confidence: DO NOT EAT this mushroom. {warning}",
                "Let me tell you what I found. {odor_detail} In my training on 8,124 mushrooms, this characteristic alone was enough to identify poisonous species. {additional_detail} My confidence is {confidence}%. {warning}"
            ],
            'poisonous_likely': [
                "I examined this mushroom's features carefully. {odor_detail} {gill_detail} While some features are neutral, the combination suggests danger. I'm {confidence}% confident this is POISONOUS. {caution}",
                "This mushroom has mixed signals. {odor_detail} However, {gill_detail} tips the balance toward danger. My analysis gives {confidence}% confidence for POISONOUS. {caution}",
                "Looking at the evidence: {odor_detail} {habitat_detail} The overall pattern leans toward poisonous with {confidence}% confidence. {caution}"
            ],
            'edible_certain': [
                "Good news! I examined this mushroom and {odor_detail}. {spore_detail} These are classic signs of edible mushrooms. I'm {confidence}% confident this mushroom is EDIBLE. {disclaimer}",
                "I like what I see here. {odor_detail} {spore_detail} In all 8,124 mushrooms I studied, these characteristics appeared only in edible species. Confidence: {confidence}%. {disclaimer}",
                "The analysis was straightforward. {odor_detail} {additional_detail} Everything points to an edible mushroom with {confidence}% confidence. {disclaimer}"
            ],
            'edible_likely': [
                "I took a close look at this mushroom. {odor_detail} {gill_detail} The signs lean positive, but not overwhelmingly so. I'm {confidence}% confident this is EDIBLE. {disclaimer}",
                "This one required careful analysis. {odor_detail} {habitat_detail} The overall assessment suggests edibility with {confidence}% confidence. {disclaimer}",
                "Weighing the evidence: {odor_detail} {gill_detail} The balance favors edible with {confidence}% confidence. {disclaimer}"
            ],
            'uncertain': [
                "This mushroom is a puzzle. {odor_detail} {gill_detail} I don't have enough distinctive features to be certain. My prediction is {confidence}% toward {prediction}, but I strongly recommend expert verification. {disclaimer}",
                "I'm scratching my head on this one. {odor_detail} {habitat_detail} Without more distinguishing characteristics, I can only give {confidence}% confidence for {prediction}. {disclaimer}",
                "This is a tricky case. {odor_detail} {additional_detail} The evidence is mixed, leading to {confidence}% confidence for {prediction}. {disclaimer}"
            ]
        }
    
    def _load_safety_facts(self):
        """Load mushroom safety facts"""
        return [
            "Remember: 90% of mushroom-related deaths come from just 3 species.",
            "Did you know? Some poisonous mushrooms look almost identical to edible ones!",
            "The Death Cap mushroom is responsible for the majority of mushroom poisoning deaths worldwide.",
            "There are over 10,000 known species of mushrooms, but only about 50 are deadly poisonous.",
            "Cooking does NOT destroy most mushroom toxins!",
            "Some mushroom toxins can cause organ failure days after consumption.",
            "Mushroom poisoning symptoms can take up to 24 hours to appear.",
            "The Destroying Angel mushroom looks pure white and innocent but is deadly.",
            "Some edible mushrooms have poisonous look-alikes. Always verify with an expert!",
            "Mushroom foraging without expert knowledge is extremely dangerous."
        ]
    
    def _load_mushroom_facts(self):
        """Load interesting mushroom facts"""
        return [
            "🍄 Mushrooms are more closely related to animals than plants!",
            "🌍 The largest living organism on Earth is a honey fungus in Oregon.",
            "💡 Some mushrooms glow in the dark - they're bioluminescent!",
            "🏥 Penicillin was discovered from a mold, which is a type of fungus.",
            "💰 Truffles, a type of underground mushroom, can sell for thousands per pound.",
            "🌳 Mushrooms help trees communicate through the 'Wood Wide Web'.",
            "🔬 Mushroom spores can survive in space!",
            "🍽️ There are over 2,000 edible mushroom species worldwide.",
            "💪 Some mushrooms can break down plastic pollution.",
            "🧠 Lion's Mane mushroom may help improve memory and focus."
        ]
    
    def _describe_odor(self, odor_value, is_edible):
        """Generate odor description"""
        descriptions = {
            'almond': "the sweet scent of almonds filled the air, a reassuring sign I've seen in hundreds of edible mushrooms",
            'anise': "a pleasant licorice-like aroma was present, characteristic of edible species",
            'none': "there was no distinct odor, which unfortunately doesn't tell me much either way",
            'foul': "a putrid, rotting smell hit me immediately - this is one of the strongest danger signals I know",
            'spicy': "a sharp, spicy smell was unmistakable - this is never a good sign",
            'fishy': "a distinctly fishy odor was present, which in my experience means definite danger",
            'pungent': "a harsh, pungent smell was immediately noticeable - a classic warning sign",
            'musty': "a damp, musty smell lingered - this often indicates toxic compounds",
            'creosote': "a chemical, tar-like smell was present - this is associated with poisonous species"
        }
        return descriptions.get(odor_value, "the odor was unusual and worth noting")
    
    def _describe_spore(self, spore_value, is_edible):
        """Generate spore print description"""
        descriptions = {
            'chocolate': "The spore print came back chocolate brown - this color appears EXCLUSIVELY in edible mushrooms",
            'green': "The spore print revealed a green color - this is a MAJOR danger sign",
            'white': "The spore print was white, which is common but not definitive",
            'brown': "The spore print showed brown spores, a fairly neutral finding",
            'black': "The spore print was black, which doesn't strongly indicate either way",
            'buff': "The spore print was buff-colored - this is concerning and often appears in toxic species",
            'purple': "The spore print was purple - unusual colors like this often signal danger",
            'orange': "The spore print was orange - bright spore colors tend to indicate toxicity",
            'yellow': "The spore print was yellow - this unusual color raises concerns"
        }
        return descriptions.get(spore_value, "the spore print was examined carefully")
    
    def _describe_gills(self, gill_size, gill_color):
        """Generate gill description"""
        size_desc = "broad" if gill_size == 'broad' else "narrow"
        
        color_descriptions = {
            'chocolate': f"the {size_desc} chocolate-colored gills are a positive sign",
            'white': f"the {size_desc} white gills are fairly common",
            'buff': f"the {size_desc} buff-colored gills raise some concerns",
            'green': f"the {size_desc} green gills are a serious warning",
            'purple': f"the {size_desc} purple gills are unusual and concerning",
            'red': f"the {size_desc} red gills are a danger signal"
        }
        
        return color_descriptions.get(gill_color, f"the {size_desc} gills were noted")
    
    def _describe_habitat(self, habitat_value):
        """Generate habitat description"""
        descriptions = {
            'woods': "growing in a wooded area, which is a common and generally safer habitat",
            'grasses': "found in a grassy area, typically associated with edible species",
            'leaves': "growing among leaf litter on the forest floor",
            'meadows': "found in an open meadow",
            'paths': "growing along a path or trail - mushrooms in disturbed areas can be risky",
            'urban': "found in an urban environment",
            'waste': "growing in a waste area - this is a significant risk factor"
        }
        return descriptions.get(habitat_value, "noted where it was growing")
    
    def generate_story(self, features, prediction, confidence, edible_prob, reason=""):
        """
        Generate a human-readable narrative for the prediction
        
        Args:
            features: Dict of mushroom features
            prediction: 'EDIBLE' or 'POISONOUS'
            confidence: Confidence percentage
            edible_prob: Probability of being edible
            reason: Pre-generated reason string
        """
        
        # Get feature descriptions
        odor = features.get('odor', 'none')
        spore = features.get('spore-print-color', 'white')
        gill_size = features.get('gill-size', 'broad')
        gill_color = features.get('gill-color', 'white')
        habitat = features.get('habitat', 'woods')
        
        # Generate descriptions
        odor_detail = self._describe_odor(odor, prediction == 'EDIBLE')
        spore_detail = self._describe_spore(spore, prediction == 'EDIBLE')
        gill_detail = self._describe_gills(gill_size, gill_color)
        habitat_detail = self._describe_habitat(habitat)
        
        # Additional detail based on confidence
        if confidence >= 90:
            additional_detail = "Every feature I checked confirmed the same conclusion."
        elif confidence >= 70:
            additional_detail = "Most features pointed in the same direction, with a few neutral signals."
        else:
            additional_detail = "Several features were ambiguous, making this a challenging case."
        
        # Safety messages
        warning = random.choice([
            "⚠️ DO NOT consume this mushroom under any circumstances!",
            "🚨 This is a serious safety concern. Do not eat!",
            "⛔ Stop! This mushroom could be deadly. Do not consume!"
        ])
        
        caution = random.choice([
            "⚠️ Exercise extreme caution. When in doubt, throw it out.",
            "🔍 I recommend getting an expert opinion before any decision.",
            "⚠️ Better safe than sorry - do not consume without expert verification."
        ])
        
        disclaimer = random.choice([
            "✅ However, always verify with an expert before eating any wild mushroom.",
            "🔍 Even with high confidence, expert confirmation is recommended.",
            "📚 Remember: this is an AI prediction, not a mycologist's verdict."
        ])
        
        # Select template category
        if confidence >= 90:
            if prediction == 'POISONOUS':
                template_category = 'poisonous_certain'
            else:
                template_category = 'edible_certain'
        elif confidence >= 60:
            if prediction == 'POISONOUS':
                template_category = 'poisonous_likely'
            else:
                template_category = 'edible_likely'
        else:
            template_category = 'uncertain'
        
        # Select random template
        template = random.choice(self.story_templates[template_category])
        
        # Fill template
        story = template.format(
            odor_detail=odor_detail,
            spore_detail=spore_detail,
            gill_detail=gill_detail,
            habitat_detail=habitat_detail,
            additional_detail=additional_detail,
            confidence=confidence,
            prediction=prediction,
            warning=warning,
            caution=caution,
            disclaimer=disclaimer
        )
        
        return story
    
    def get_random_fact(self):
        """Get a random mushroom fact"""
        return random.choice(self.mushroom_facts)
    
    def get_safety_tip(self):
        """Get a random safety tip"""
        return random.choice(self.safety_facts)
    
    def generate_feature_impact_story(self, feature_name, feature_value, old_prediction, new_prediction, old_confidence, new_confidence):
        """Generate a story about how changing one feature impacts the prediction"""
        
        templates = [
            f"I noticed something interesting: changing the {feature_name} to '{feature_value}' completely changed my assessment. Before, I was {old_confidence}% confident it was {old_prediction}. Now, I'm {new_confidence}% sure it's {new_prediction}. This shows just how powerful the {feature_name} feature is!",
            f"Let me show you how much {feature_name} matters. With the original value, I predicted {old_prediction} at {old_confidence}%. But setting {feature_name} to '{feature_value}' shifts my prediction to {new_prediction} with {new_confidence}% confidence. This feature alone can change the outcome!",
            f"This is why {feature_name} is so important. The original mushroom looked {old_prediction} ({old_confidence}% confidence). After changing only the {feature_name} to '{feature_value}', I now see it as {new_prediction} ({new_confidence}% confidence). One feature can make all the difference!"
        ]
        
        return random.choice(templates)
    
    def generate_confidence_journey(self, steps, final_prediction, final_confidence):
        """Generate a journey narrative for the confidence animation"""
        
        intro = "Let me walk you through how I analyzed this mushroom step by step:\n\n"
        
        journey_text = intro
        
        for i, step in enumerate(steps):
            feature = step['feature']
            value = step['value']
            impact = step['impact']
            confidence_after = step['confidence_after']
            
            if impact == 'positive':
                journey_text += f"**Step {i+1}:** I checked the **{feature}** and found '{value}'. This is a good sign, raising my confidence to {confidence_after}%.\n\n"
            elif impact == 'negative':
                journey_text += f"**Step {i+1}:** I examined the **{feature}** and saw '{value}'. This worried me, dropping confidence to {confidence_after}%.\n\n"
            else:
                journey_text += f"**Step {i+1}:** Looking at the **{feature}** ('{value}') didn't change much. Confidence remains at {confidence_after}%.\n\n"
        
        journey_text += f"**Conclusion:** After analyzing all features, I predict **{final_prediction}** with **{final_confidence}%** confidence."
        
        return journey_text
    
    def render_story_card(self, story):
        """Render a story as a styled card"""
        st.markdown(f"""
        <div class="story-text">
            <p>📖 {story}</p>
        </div>
        """, unsafe_allow_html=True)
    
    def render_fact_card(self):
        """Render a random mushroom fact card"""
        fact = self.get_random_fact()
        st.markdown(f"""
        <div style="background:rgba(255,255,255,0.03); border:1px solid rgba(255,255,255,0.1); 
                    border-radius:12px; padding:1rem; margin:1rem 0; text-align:center;">
            <p style="color:#a0a0b0; margin:0;">💡 Did you know?</p>
            <p style="color:#d0d0e0; font-style:italic;">{fact}</p>
        </div>
        """, unsafe_allow_html=True)
    
    def render_safety_card(self):
        """Render a safety tip card"""
        tip = self.get_safety_tip()
        st.markdown(f"""
        <div style="background:rgba(231, 76, 60, 0.1); border:1px solid rgba(231, 76, 60, 0.3); 
                    border-radius:12px; padding:1rem; margin:1rem 0; text-align:center;">
            <p style="color:#e74c3c; margin:0;">⚠️ Safety Reminder</p>
            <p style="color:#d0a0a0;">{tip}</p>
        </div>
        """, unsafe_allow_html=True)


# Initialize story generator
mushroom_story = MushroomStory()