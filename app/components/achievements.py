"""
🍄 MUSHROOM SAFETY AI - ACHIEVEMENT SYSTEM
Gamification with Badges, Levels, and Rewards
500+ Lines of Achievement Logic
"""

import streamlit as st
from datetime import datetime
import json


class AchievementSystem:
    """Professional Achievement & Gamification System"""
    
    def __init__(self):
        # Initialize achievement state
        if 'achievements' not in st.session_state:
            st.session_state.achievements = self._load_achievements()
        
        if 'achievement_points' not in st.session_state:
            st.session_state.achievement_points = 0
        
        if 'achievement_level' not in st.session_state:
            st.session_state.achievement_level = 1
        
        if 'notifications' not in st.session_state:
            st.session_state.notifications = []
        
        if 'stats' not in st.session_state:
            st.session_state.stats = self._init_stats()
        
        if 'badges_earned' not in st.session_state:
            st.session_state.badges_earned = []
    
    def _load_achievements(self):
        """Define all achievements"""
        return {
            # ============================================
            # BEGINNER ACHIEVEMENTS
            # ============================================
            'first_prediction': {
                'name': '🌱 First Steps',
                'description': 'Make your first mushroom prediction',
                'category': 'Beginner',
                'points': 10,
                'icon': '🌱',
                'unlocked': False,
                'progress': 0,
                'max_progress': 1,
                'secret': False
            },
            'five_predictions': {
                'name': '🔬 Curious Mind',
                'description': 'Make 5 predictions',
                'category': 'Beginner',
                'points': 25,
                'icon': '🔬',
                'unlocked': False,
                'progress': 0,
                'max_progress': 5,
                'secret': False
            },
            'ten_predictions': {
                'name': '🍄 Enthusiast',
                'description': 'Make 10 predictions',
                'category': 'Beginner',
                'points': 50,
                'icon': '🍄',
                'unlocked': False,
                'progress': 0,
                'max_progress': 10,
                'secret': False
            },
            
            # ============================================
            # EXPLORER ACHIEVEMENTS
            # ============================================
            'all_odors': {
                'name': '👃 The Nose Knows',
                'description': 'Test all 9 odor types',
                'category': 'Explorer',
                'points': 100,
                'icon': '👃',
                'unlocked': False,
                'progress': 0,
                'max_progress': 9,
                'secret': False
            },
            'all_habitats': {
                'name': '🗺️ World Explorer',
                'description': 'Test mushrooms from all 7 habitats',
                'category': 'Explorer',
                'points': 100,
                'icon': '🗺️',
                'unlocked': False,
                'progress': 0,
                'max_progress': 7,
                'secret': False
            },
            'all_spore_colors': {
                'name': '🔬 Spore Collector',
                'description': 'Test all 9 spore print colors',
                'category': 'Explorer',
                'points': 100,
                'icon': '🔬',
                'unlocked': False,
                'progress': 0,
                'max_progress': 9,
                'secret': False
            },
            'all_features': {
                'name': '📊 Data Scientist',
                'description': 'Use all 10 selectable features at least once',
                'category': 'Explorer',
                'points': 150,
                'icon': '📊',
                'unlocked': False,
                'progress': 0,
                'max_progress': 10,
                'secret': False
            },
            
            # ============================================
            # ACCURACY ACHIEVEMENTS
            # ============================================
            'streak_3': {
                'name': '🔥 On Fire',
                'description': 'Get 3 correct predictions in a row',
                'category': 'Accuracy',
                'points': 50,
                'icon': '🔥',
                'unlocked': False,
                'progress': 0,
                'max_progress': 3,
                'secret': False
            },
            'streak_5': {
                'name': '⭐ Sharpshooter',
                'description': 'Get 5 correct predictions in a row',
                'category': 'Accuracy',
                'points': 100,
                'icon': '⭐',
                'unlocked': False,
                'progress': 0,
                'max_progress': 5,
                'secret': False
            },
            'streak_10': {
                'name': '🏆 Mushroom Master',
                'description': 'Get 10 correct predictions in a row',
                'category': 'Accuracy',
                'points': 250,
                'icon': '🏆',
                'unlocked': False,
                'progress': 0,
                'max_progress': 10,
                'secret': False
            },
            
            # ============================================
            # HIDDEN/SECRET ACHIEVEMENTS
            # ============================================
            'deadly_encounter': {
                'name': '💀 Close Call',
                'description': 'Identify a foul-smelling poisonous mushroom',
                'category': 'Secret',
                'points': 25,
                'icon': '💀',
                'unlocked': False,
                'progress': 0,
                'max_progress': 1,
                'secret': True
            },
            'almond_surprise': {
                'name': '😋 Sweet Discovery',
                'description': 'Find an almond-scented edible mushroom',
                'category': 'Secret',
                'points': 25,
                'icon': '😋',
                'unlocked': False,
                'progress': 0,
                'max_progress': 1,
                'secret': True
            },
            'midnight_mycologist': {
                'name': '🌙 Night Owl',
                'description': 'Make a prediction between midnight and 4 AM',
                'category': 'Secret',
                'points': 50,
                'icon': '🌙',
                'unlocked': False,
                'progress': 0,
                'max_progress': 1,
                'secret': True
            },
            'speed_demon': {
                'name': '⚡ Speed Demon',
                'description': 'Make 3 predictions within 30 seconds',
                'category': 'Secret',
                'points': 75,
                'icon': '⚡',
                'unlocked': False,
                'progress': 0,
                'max_progress': 3,
                'secret': True
            },
            'perfect_game': {
                'name': '💯 Perfect Score',
                'description': 'Get 100% accuracy in a game of 10 rounds',
                'category': 'Secret',
                'points': 500,
                'icon': '💯',
                'unlocked': False,
                'progress': 0,
                'max_progress': 10,
                'secret': True
            },
            
            # ============================================
            # MASTERY ACHIEVEMENTS
            # ============================================
            'hundred_predictions': {
                'name': '🧑‍🔬 Research Scientist',
                'description': 'Make 100 predictions',
                'category': 'Mastery',
                'points': 500,
                'icon': '🧑‍🔬',
                'unlocked': False,
                'progress': 0,
                'max_progress': 100,
                'secret': False
            },
            'thousand_predictions': {
                'name': '👑 Mushroom King',
                'description': 'Make 1000 predictions',
                'category': 'Mastery',
                'points': 1000,
                'icon': '👑',
                'unlocked': False,
                'progress': 0,
                'max_progress': 1000,
                'secret': False
            },
            'collector_complete': {
                'name': '🎖️ Completionist',
                'description': 'Unlock all non-secret achievements',
                'category': 'Mastery',
                'points': 1000,
                'icon': '🎖️',
                'unlocked': False,
                'progress': 0,
                'max_progress': 12,
                'secret': False
            },
        }
    
    def _init_stats(self):
        """Initialize tracking statistics"""
        return {
            'total_predictions': 0,
            'correct_predictions': 0,
            'wrong_predictions': 0,
            'streak': 0,
            'best_streak': 0,
            'odors_tested': set(),
            'habitats_tested': set(),
            'spore_colors_tested': set(),
            'features_used': set(),
            'last_prediction_time': None,
            'recent_predictions': [],
            'game_rounds_played': 0,
            'game_correct': 0,
            'total_time_spent': 0,
        }
    
    def track_prediction(self, features, prediction, confidence, is_correct=None):
        """Track a prediction for achievements"""
        stats = st.session_state.stats
        
        # Update totals
        stats['total_predictions'] += 1
        
        # Track features used
        if 'odor' in features:
            stats['odors_tested'].add(features['odor'])
        if 'spore-print-color' in features:
            stats['spore_colors_tested'].add(features['spore-print-color'])
        if 'habitat' in features:
            stats['habitats_tested'].add(features['habitat'])
        
        for key in features:
            stats['features_used'].add(key)
        
        # Track streak
        if is_correct is not None:
            if is_correct:
                stats['correct_predictions'] += 1
                stats['streak'] += 1
                if stats['streak'] > stats['best_streak']:
                    stats['best_streak'] = stats['streak']
            else:
                stats['wrong_predictions'] += 1
                stats['streak'] = 0
        
        # Track timing
        now = datetime.now()
        if stats['last_prediction_time']:
            time_diff = (now - stats['last_prediction_time']).total_seconds()
            stats['recent_predictions'].append({
                'time': now,
                'interval': time_diff
            })
            # Keep only last 10
            stats['recent_predictions'] = stats['recent_predictions'][-10:]
        stats['last_prediction_time'] = now
        
        # Check achievements
        self._check_achievements(features, prediction)
    
    def _check_achievements(self, features, prediction):
        """Check and unlock achievements"""
        stats = st.session_state.stats
        achievements = st.session_state.achievements
        notifications = []
        
        # First prediction
        if stats['total_predictions'] >= 1 and not achievements['first_prediction']['unlocked']:
            self._unlock_achievement('first_prediction')
            notifications.append('🌱 First prediction made!')
        
        # Five predictions
        achievements['five_predictions']['progress'] = min(stats['total_predictions'], 5)
        if stats['total_predictions'] >= 5 and not achievements['five_predictions']['unlocked']:
            self._unlock_achievement('five_predictions')
            notifications.append('🔬 5 predictions completed!')
        
        # Ten predictions
        achievements['ten_predictions']['progress'] = min(stats['total_predictions'], 10)
        if stats['total_predictions'] >= 10 and not achievements['ten_predictions']['unlocked']:
            self._unlock_achievement('ten_predictions')
            notifications.append('🍄 10 predictions reached!')
        
        # All odors
        achievements['all_odors']['progress'] = len(stats['odors_tested'])
        if len(stats['odors_tested']) >= 9 and not achievements['all_odors']['unlocked']:
            self._unlock_achievement('all_odors')
            notifications.append('👃 All odors tested!')
        
        # All habitats
        achievements['all_habitats']['progress'] = len(stats['habitats_tested'])
        if len(stats['habitats_tested']) >= 7 and not achievements['all_habitats']['unlocked']:
            self._unlock_achievement('all_habitats')
            notifications.append('🗺️ All habitats explored!')
        
        # All spore colors
        achievements['all_spore_colors']['progress'] = len(stats['spore_colors_tested'])
        if len(stats['spore_colors_tested']) >= 9 and not achievements['all_spore_colors']['unlocked']:
            self._unlock_achievement('all_spore_colors')
            notifications.append('🔬 All spore colors collected!')
        
        # All features
        achievements['all_features']['progress'] = len(stats['features_used'])
        if len(stats['features_used']) >= 10 and not achievements['all_features']['unlocked']:
            self._unlock_achievement('all_features')
            notifications.append('📊 All features used!')
        
        # Streak checks
        streak = stats['streak']
        achievements['streak_3']['progress'] = min(streak, 3)
        if streak >= 3 and not achievements['streak_3']['unlocked']:
            self._unlock_achievement('streak_3')
            notifications.append('🔥 3-streak achieved!')
        
        achievements['streak_5']['progress'] = min(streak, 5)
        if streak >= 5 and not achievements['streak_5']['unlocked']:
            self._unlock_achievement('streak_5')
            notifications.append('⭐ 5-streak! Sharpshooter!')
        
        achievements['streak_10']['progress'] = min(streak, 10)
        if streak >= 10 and not achievements['streak_10']['unlocked']:
            self._unlock_achievement('streak_10')
            notifications.append('🏆 10-STREAK! MUSHROOM MASTER!')
            st.balloons()
        
        # Secret achievements
        if features.get('odor') == 'foul' and not achievements['deadly_encounter']['unlocked']:
            self._unlock_achievement('deadly_encounter')
            notifications.append('💀 Secret: Close Call unlocked!')
        
        if features.get('odor') == 'almond' and not achievements['almond_surprise']['unlocked']:
            self._unlock_achievement('almond_surprise')
            notifications.append('😋 Secret: Sweet Discovery unlocked!')
        
        # Midnight mycologist
        now = datetime.now()
        if 0 <= now.hour < 4 and not achievements['midnight_mycologist']['unlocked']:
            self._unlock_achievement('midnight_mycologist')
            notifications.append('🌙 Secret: Night Owl unlocked!')
        
        # Speed demon
        recent = stats['recent_predictions']
        if len(recent) >= 3:
            last_three = recent[-3:]
            total_time = sum(r['interval'] for r in last_three)
            if total_time <= 30 and not achievements['speed_demon']['unlocked']:
                self._unlock_achievement('speed_demon')
                notifications.append('⚡ Secret: Speed Demon unlocked!')
        
        # Hundred predictions
        achievements['hundred_predictions']['progress'] = min(stats['total_predictions'], 100)
        if stats['total_predictions'] >= 100 and not achievements['hundred_predictions']['unlocked']:
            self._unlock_achievement('hundred_predictions')
            notifications.append('🧑‍🔬 100 predictions! Research Scientist!')
        
        # Save notifications
        if notifications:
            st.session_state.notifications.extend(notifications)
    
    def _unlock_achievement(self, achievement_id):
        """Unlock an achievement"""
        achievements = st.session_state.achievements
        achievements[achievement_id]['unlocked'] = True
        achievements[achievement_id]['progress'] = achievements[achievement_id]['max_progress']
        
        # Add points
        points = achievements[achievement_id]['points']
        st.session_state.achievement_points += points
        
        # Add badge
        badge = {
            'id': achievement_id,
            'name': achievements[achievement_id]['name'],
            'icon': achievements[achievement_id]['icon'],
            'unlocked_at': datetime.now().strftime("%Y-%m-%d %H:%M")
        }
        st.session_state.badges_earned.append(badge)
        
        # Update level
        self._update_level()
    
    def _update_level(self):
        """Update user level based on points"""
        points = st.session_state.achievement_points
        
        if points >= 5000:
            st.session_state.achievement_level = 10
        elif points >= 3000:
            st.session_state.achievement_level = 8
        elif points >= 2000:
            st.session_state.achievement_level = 6
        elif points >= 1000:
            st.session_state.achievement_level = 4
        elif points >= 500:
            st.session_state.achievement_level = 3
        elif points >= 250:
            st.session_state.achievement_level = 2
        else:
            st.session_state.achievement_level = 1
    
    def get_level_title(self):
        """Get title for current level"""
        level = st.session_state.achievement_level
        titles = {
            1: '🍄 Beginner Forager',
            2: '🌱 Nature Explorer',
            3: '🔬 Student Mycologist',
            4: '📊 Data Scientist',
            5: '🔥 Mushroom Hunter',
            6: '⭐ Expert Identifier',
            7: '🏆 Master Mycologist',
            8: '👑 Mushroom King',
            9: '💀 Death Defier',
            10: '🎖️ Legendary Forager'
        }
        return titles.get(level, '🍄 Mushroom Friend')
    
    def render_achievements_panel(self):
        """Render the achievements display"""
        achievements = st.session_state.achievements
        
        # Level display
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            st.markdown(f"""
            <div style="text-align:center; padding:1rem;">
                <h1 style="font-size:3rem;">{self.get_level_icon()}</h1>
                <h2>{self.get_level_title()}</h2>
                <p style="color:#a0a0b0;">Level {st.session_state.achievement_level}</p>
                <p style="color:#2ecc71;">🏆 {st.session_state.achievement_points} Points</p>
            </div>
            """, unsafe_allow_html=True)
        
        # Progress to next level
        points = st.session_state.achievement_points
        next_level_points = self._get_next_level_points()
        progress = min(points / next_level_points, 1.0) if next_level_points > 0 else 1.0
        
        st.progress(progress, text=f"Progress to Level {st.session_state.achievement_level + 1}: {points}/{next_level_points} pts")
        
        st.markdown("---")
        
        # Categories
        categories = ['Beginner', 'Explorer', 'Accuracy', 'Mastery', 'Secret']
        tabs = st.tabs(categories)
        
        for tab, category in zip(tabs, categories):
            with tab:
                cat_achievements = {k: v for k, v in achievements.items() if v['category'] == category}
                
                for ach_id, ach in cat_achievements.items():
                    self._render_achievement_card(ach_id, ach)
    
    def _render_achievement_card(self, ach_id, achievement):
        """Render a single achievement card"""
        unlocked = achievement['unlocked']
        secret = achievement['secret']
        
        # For secret achievements, show ??? if not unlocked
        if secret and not unlocked:
            name = '???'
            description = 'Mystery achievement - keep exploring!'
            icon = '🔒'
            progress_text = ''
            opacity = 0.4
        else:
            name = achievement['name']
            description = achievement['description']
            icon = achievement['icon']
            progress = achievement['progress']
            max_progress = achievement['max_progress']
            progress_text = f"{progress}/{max_progress}"
            opacity = 1.0 if unlocked else 0.7
        
        # Card color
        if unlocked:
            border_color = '#2ecc71'
            bg_color = 'rgba(46, 204, 113, 0.1)'
            status_icon = '✅'
        else:
            border_color = 'rgba(255, 255, 255, 0.1)'
            bg_color = 'rgba(255, 255, 255, 0.03)'
            status_icon = '🔒' if not secret else '❓'
        
        st.markdown(f"""
        <div style="background:{bg_color}; border:1px solid {border_color}; 
                    border-radius:12px; padding:1rem; margin:0.5rem 0; opacity:{opacity};">
            <div style="display:flex; align-items:center; gap:1rem;">
                <span style="font-size:2rem;">{icon}</span>
                <div style="flex:1;">
                    <strong style="color:{'#2ecc71' if unlocked else '#a0a0b0'};">
                        {status_icon} {name}
                    </strong>
                    <p style="color:#a0a0b0; margin:0.2rem 0; font-size:0.9rem;">{description}</p>
                    <p style="color:#606070; font-size:0.8rem; margin:0;">
                        {progress_text} | {achievement['points']} pts | {achievement['category']}
                    </p>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    def _get_next_level_points(self):
        """Get points required for next level"""
        level_thresholds = {
            1: 250,
            2: 500,
            3: 1000,
            4: 2000,
            5: 3000,
            6: 5000,
            7: 7500,
            8: 10000,
            9: 15000,
        }
        return level_thresholds.get(st.session_state.achievement_level, 20000)
    
    def get_level_icon(self):
        """Get icon for current level"""
        level = st.session_state.achievement_level
        icons = {
            1: '🍄', 2: '🌱', 3: '🔬', 4: '📊', 5: '🔥',
            6: '⭐', 7: '🏆', 8: '👑', 9: '💀', 10: '🎖️'
        }
        return icons.get(level, '🍄')
    
    def render_notifications(self):
        """Render achievement notifications"""
        if st.session_state.notifications:
            for notification in st.session_state.notifications[-3:]:  # Show last 3
                st.toast(notification, icon='🎉')
            st.session_state.notifications = []
    
    def render_badge_collection(self):
        """Render earned badges"""
        badges = st.session_state.badges_earned
        
        if not badges:
            st.info("No badges earned yet! Start making predictions to earn badges.")
            return
        
        # Display badges in a grid
        cols = st.columns(4)
        for i, badge in enumerate(badges[-8:]):  # Show last 8
            with cols[i % 4]:
                st.markdown(f"""
                <div style="text-align:center; padding:0.5rem;">
                    <span style="font-size:2rem;">{badge['icon']}</span>
                    <p style="font-size:0.8rem; margin:0; color:#a0a0b0;">{badge['name']}</p>
                    <p style="font-size:0.6rem; margin:0; color:#606070;">{badge['unlocked_at']}</p>
                </div>
                """, unsafe_allow_html=True)


# Initialize achievement system
achievement_system = AchievementSystem()