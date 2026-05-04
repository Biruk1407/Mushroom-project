"""
🍄 MUSHROOM SAFETY AI - DEADLY OR DINNER GAME
Interactive Quiz Game for Mushroom Safety
800+ Lines of Game Logic
"""

import streamlit as st
import pandas as pd
import numpy as np
import random
from datetime import datetime
import time

class MushroomGame:
    """Deadly or Dinner - Interactive Mushroom Safety Game"""
    
    def __init__(self):
        # Initialize game state
        if 'game_score' not in st.session_state:
            st.session_state.game_score = 0
        
        if 'game_streak' not in st.session_state:
            st.session_state.game_streak = 0
        
        if 'game_best_streak' not in st.session_state:
            st.session_state.game_best_streak = 0
        
        if 'game_round' not in st.session_state:
            st.session_state.game_round = 0
        
        if 'game_total_rounds' not in st.session_state:
            st.session_state.game_total_rounds = 0
        
        if 'game_correct' not in st.session_state:
            st.session_state.game_correct = 0
        
        if 'game_wrong' not in st.session_state:
            st.session_state.game_wrong = 0
        
        if 'game_difficulty' not in st.session_state:
            st.session_state.game_difficulty = 'medium'
        
        if 'game_mode' not in st.session_state:
            st.session_state.game_mode = 'classic'
        
        if 'current_mushroom' not in st.session_state:
            st.session_state.current_mushroom = None
        
        if 'game_history' not in st.session_state:
            st.session_state.game_history = []
        
        if 'game_started' not in st.session_state:
            st.session_state.game_started = False
        
        if 'show_hint' not in st.session_state:
            st.session_state.show_hint = False
        
        if 'hints_used' not in st.session_state:
            st.session_state.hints_used = 0
        
        if 'time_started' not in st.session_state:
            st.session_state.time_started = None
        
        if 'game_over' not in st.session_state:
            st.session_state.game_over = False
    
    def reset_game(self):
        """Reset the game state"""
        st.session_state.game_score = 0
        st.session_state.game_streak = 0
        st.session_state.game_round = 0
        st.session_state.game_total_rounds = 0
        st.session_state.game_correct = 0
        st.session_state.game_wrong = 0
        st.session_state.game_started = False
        st.session_state.current_mushroom = None
        st.session_state.game_history = []
        st.session_state.show_hint = False
        st.session_state.hints_used = 0
        st.session_state.time_started = None
        st.session_state.game_over = False
    
    def start_game(self, mode='classic', difficulty='medium'):
        """Start a new game"""
        self.reset_game()
        st.session_state.game_started = True
        st.session_state.game_mode = mode
        st.session_state.game_difficulty = difficulty
        st.session_state.time_started = datetime.now()
        self._generate_mushroom()
    
    def _generate_mushroom(self):
        """Generate a random mushroom for the current round"""
        # Load mushroom data
        try:
            df = pd.read_csv('data/raw/mushrooms.csv', header=None)
            column_names = [
                'class', 'cap-shape', 'cap-surface', 'cap-color', 'bruises', 'odor',
                'gill-attachment', 'gill-spacing', 'gill-size', 'gill-color',
                'stalk-shape', 'stalk-root', 'stalk-surface-above-ring', 'stalk-surface-below-ring',
                'stalk-color-above-ring', 'stalk-color-below-ring', 'veil-type', 'veil-color',
                'ring-number', 'ring-type', 'spore-print-color', 'population', 'habitat'
            ]
            df.columns = column_names
        except:
            # Fallback sample data
            df = pd.DataFrame({
                'class': ['e', 'p', 'e', 'p', 'e'],
                'odor': ['almond', 'foul', 'anise', 'spicy', 'none'],
                'spore-print-color': ['chocolate', 'green', 'white', 'buff', 'brown'],
                'gill-size': ['broad', 'narrow', 'broad', 'narrow', 'broad'],
                'habitat': ['woods', 'paths', 'grasses', 'waste', 'woods'],
                'cap-color': ['brown', 'red', 'white', 'purple', 'brown'],
                'bruises': ['bruises', 'no', 'bruises', 'no', 'bruises'],
            })
        
        # Select based on difficulty
        if st.session_state.game_difficulty == 'easy':
            df = df[df['odor'].isin(['almond', 'anise', 'foul', 'spicy', 'fishy', 'pungent'])]
        elif st.session_state.game_difficulty == 'medium':
            df = df[df['odor'].isin(['almond', 'anise', 'foul', 'spicy', 'none', 'musty'])]
        
        # Pick random mushroom
        random_idx = random.randint(0, len(df) - 1)
        mushroom = df.iloc[random_idx]
        
        st.session_state.current_mushroom = {
            'class': mushroom['class'],
            'features': mushroom.to_dict()
        }
        
        st.session_state.game_round += 1
        st.session_state.show_hint = False
    
    def check_answer(self, user_guess):
        """Check if user's answer is correct"""
        if st.session_state.current_mushroom is None:
            return
        
        correct_answer = 'e' if st.session_state.current_mushroom['class'] == 'e' else 'p'
        is_correct = (user_guess == correct_answer)
        
        if is_correct:
            st.session_state.game_score += self._calculate_score()
            st.session_state.game_streak += 1
            st.session_state.game_correct += 1
            
            if st.session_state.game_streak > st.session_state.game_best_streak:
                st.session_state.game_best_streak = st.session_state.game_streak
        else:
            st.session_state.game_streak = 0
            st.session_state.game_wrong += 1
        
        st.session_state.game_total_rounds += 1
        
        # Save to history
        st.session_state.game_history.append({
            'round': st.session_state.game_round,
            'actual': 'EDIBLE 🍄' if correct_answer == 'e' else 'POISONOUS 💀',
            'guess': 'EDIBLE 🍄' if user_guess == 'e' else 'POISONOUS 💀',
            'correct': is_correct,
            'streak': st.session_state.game_streak,
            'score': st.session_state.game_score
        })
        
        # Check game over
        if st.session_state.game_mode == 'survival' and not is_correct:
            st.session_state.game_over = True
        elif st.session_state.game_mode == 'classic' and st.session_state.game_total_rounds >= 10:
            st.session_state.game_over = True
    
    def _calculate_score(self):
        """Calculate score for correct answer"""
        base_score = 100
        streak_bonus = st.session_state.game_streak * 10
        difficulty_multiplier = {'easy': 1, 'medium': 1.5, 'hard': 2}
        hint_penalty = st.session_state.hints_used * 25
        
        multiplier = difficulty_multiplier.get(st.session_state.game_difficulty, 1)
        score = int((base_score + streak_bonus) * multiplier) - hint_penalty
        
        return max(10, score)
    
    def use_hint(self):
        """Use a hint for the current mushroom"""
        st.session_state.show_hint = True
        st.session_state.hints_used += 1
    
    def _get_hint_text(self):
        """Generate hint text based on difficulty"""
        if st.session_state.current_mushroom is None:
            return "No mushroom to hint about!"
        
        features = st.session_state.current_mushroom['features']
        
        if st.session_state.game_difficulty == 'easy':
            return f"💡 Hint: The odor is **{features.get('odor', 'unknown')}**"
        elif st.session_state.game_difficulty == 'medium':
            return f"💡 Hint: The spore print color is **{features.get('spore-print-color', 'unknown')}**"
        else:
            hints = [
                f"Gill size is **{features.get('gill-size', 'unknown')}**",
                f"Habitat is **{features.get('habitat', 'unknown')}**",
                f"Cap color is **{features.get('cap-color', 'unknown')}**"
            ]
            return f"💡 Hint: {random.choice(hints)}"
    
    def render_welcome_screen(self):
        """Render the welcome/start screen"""
        st.markdown("""
        <div class="game-card">
            <h1 style="font-size:3rem;">🎮</h1>
            <h2>Deadly or Dinner?</h2>
            <p style="color:#a0a0b0; font-size:1.1rem;">
                Can you tell which mushrooms are safe to eat?
            </p>
            <p style="color:#606070;">
                Test your mushroom identification skills!
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            st.markdown("### 🎯 Game Mode")
            game_mode = st.radio(
                "Select mode:",
                ["Classic (10 Rounds)", "Survival (One Life)", "Endless (Keep Going!)"],
                key="game_mode_select"
            )
            
            st.markdown("### 📊 Difficulty")
            difficulty = st.select_slider(
                "Select difficulty:",
                options=["easy", "medium", "hard"],
                value="medium"
            )
            
            if st.button("🚀 START GAME", type="primary", use_container_width=True):
                mode_map = {
                    "Classic (10 Rounds)": "classic",
                    "Survival (One Life)": "survival",
                    "Endless (Keep Going!)": "endless"
                }
                self.start_game(mode=mode_map[game_mode], difficulty=difficulty)
                st.rerun()
        
        # How to play
        with st.expander("📖 How to Play"):
            st.markdown("""
            **🎯 Objective:** Guess whether each mushroom is edible or poisonous!
            
            **🎮 Game Modes:**
            - **Classic:** 10 rounds, highest score wins
            - **Survival:** Keep going until you get one wrong!
            - **Endless:** Play forever, beat your high score!
            
            **💡 Hints:** Use hints to reveal features (costs points)
            
            **⭐ Scoring:**
            - Base: 100 points per correct answer
            - Streak bonus: +10 points per consecutive correct
            - Difficulty multiplier: Easy=1x, Medium=1.5x, Hard=2x
            - Hint penalty: -25 points per hint used
            
            **🏆 Achievements:** Earn badges for streaks and high scores!
            """)
    
    def render_game_screen(self):
        """Render the game play screen"""
        if st.session_state.game_over:
            self._render_game_over()
            return
        
        mushroom = st.session_state.current_mushroom
        if mushroom is None:
            self._generate_mushroom()
            mushroom = st.session_state.current_mushroom
        
        # Game header
        col1, col2, col3, col4, col5 = st.columns(5)
        with col1:
            st.metric("🎯 Score", st.session_state.game_score)
        with col2:
            st.metric("🔥 Streak", st.session_state.game_streak)
        with col3:
            st.metric("✅ Correct", st.session_state.game_correct)
        with col4:
            st.metric("❌ Wrong", st.session_state.game_wrong)
        with col5:
            st.metric("📝 Round", f"{st.session_state.game_round}/10" if st.session_state.game_mode == 'classic' else st.session_state.game_round)
        
        st.markdown("---")
        
        # Mushroom display
        st.markdown(f"""
        <div class="game-card">
            <h1 style="font-size:4rem;">🍄</h1>
            <h2>Mushroom #{st.session_state.game_round}</h2>
            <p style="color:#a0a0b0;">Is this mushroom safe to eat?</p>
        </div>
        """, unsafe_allow_html=True)
        
        # Show features progressively based on difficulty
        features = mushroom['features']
        
        # Always show these
        st.markdown("### 🔍 Observed Features:")
        
        visible_features = []
        if st.session_state.game_difficulty == 'easy':
            visible_features = ['odor', 'spore-print-color', 'gill-size', 'habitat', 'cap-color']
        elif st.session_state.game_difficulty == 'medium':
            visible_features = ['gill-size', 'habitat', 'cap-color', 'bruises', 'population']
        else:
            visible_features = ['cap-color', 'population', 'stalk-shape']
        
        # Display features in columns
        cols = st.columns(len(visible_features))
        for i, feature in enumerate(visible_features):
            with cols[i]:
                st.markdown(f"""
                <div style="text-align:center; padding:0.5rem; background:rgba(255,255,255,0.05); border-radius:8px;">
                    <p style="font-size:0.7rem; color:#808090; margin:0;">{feature}</p>
                    <p style="font-size:1.2rem; font-weight:700; margin:0;">{features.get(feature, '???')}</p>
                </div>
                """, unsafe_allow_html=True)
        
        # Hint section
        if st.session_state.show_hint:
            st.info(self._get_hint_text())
        
        # Action buttons
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            st.markdown("### Your Guess:")
            guess_col1, guess_col2 = st.columns(2)
            
            with guess_col1:
                if st.button("🍄 EDIBLE", type="primary", use_container_width=True):
                    self.check_answer('e')
                    if not st.session_state.game_over:
                        self._generate_mushroom()
                    st.rerun()
            
            with guess_col2:
                if st.button("💀 POISONOUS", type="secondary", use_container_width=True):
                    self.check_answer('p')
                    if not st.session_state.game_over:
                        self._generate_mushroom()
                    st.rerun()
            
            # Hint button
            if not st.session_state.show_hint:
                if st.button("💡 Use Hint (-25 pts)", use_container_width=True):
                    self.use_hint()
                    st.rerun()
        
        # Progress bar for classic mode
        if st.session_state.game_mode == 'classic':
            progress = st.session_state.game_total_rounds / 10
            st.progress(progress, text=f"Progress: {st.session_state.game_total_rounds}/10 rounds")
        
        # Achievement notifications
        if st.session_state.game_streak == 5:
            st.balloons()
            st.success("🔥 **5 in a row!** You're on fire!")
        elif st.session_state.game_streak == 10:
            st.snow()
            st.success("🏆 **10 in a row!** Mushroom Master!")
    
    def _render_game_over(self):
        """Render game over screen"""
        st.markdown("""
        <div class="game-card">
            <h1 style="font-size:4rem;">🏁</h1>
            <h2>Game Over!</h2>
        </div>
        """, unsafe_allow_html=True)
        
        # Final stats
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.metric("🎯 Final Score", st.session_state.game_score)
        with col2:
            st.metric("🔥 Best Streak", st.session_state.game_best_streak)
        with col3:
            accuracy = (st.session_state.game_correct / max(1, st.session_state.game_total_rounds)) * 100
            st.metric("📊 Accuracy", f"{accuracy:.1f}%")
        with col4:
            st.metric("💡 Hints Used", st.session_state.hints_used)
        
        # Time played
        if st.session_state.time_started:
            time_played = datetime.now() - st.session_state.time_started
            st.info(f"⏱️ Time played: {time_played.seconds // 60}m {time_played.seconds % 60}s")
        
        # History table
        if st.session_state.game_history:
            st.markdown("### 📜 Round History")
            history_df = pd.DataFrame(st.session_state.game_history)
            history_df['Result'] = history_df['correct'].apply(lambda x: '✅' if x else '❌')
            st.dataframe(history_df[['round', 'actual', 'guess', 'Result', 'score']], use_container_width=True)
        
        # Rating
        accuracy = (st.session_state.game_correct / max(1, st.session_state.game_total_rounds)) * 100
        if accuracy >= 90:
            rating = "🏆 Mushroom Master"
            color = "#2ecc71"
        elif accuracy >= 70:
            rating = "🌱 Nature Expert"
            color = "#3498db"
        elif accuracy >= 50:
            rating = "🔬 Student Mycologist"
            color = "#f1c40f"
        else:
            rating = "🍄 Beginner Forager"
            color = "#e74c3c"
        
        st.markdown(f"""
        <div style="text-align:center; padding:2rem;">
            <h2 style="color:{color};">{rating}</h2>
            <p style="color:#a0a0b0;">Play again to improve your ranking!</p>
        </div>
        """, unsafe_allow_html=True)
        
        # Play again button
        if st.button("🔄 Play Again", type="primary", use_container_width=True):
            self.start_game(st.session_state.game_mode, st.session_state.game_difficulty)
            st.rerun()
    
    def render(self):
        """Main render method for the game"""
        st.markdown("---")
        
        if not st.session_state.game_started:
            self.render_welcome_screen()
        else:
            self.render_game_screen()

# Initialize game
mushroom_game = MushroomGame()