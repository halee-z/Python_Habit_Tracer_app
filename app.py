import streamlit as st
import datetime

st.set_page_config(page_title="🗓️ Habit Tracker", layout="centered")
st.title("🗓️ Daily Habit Tracker")

# -----------------------------
# Initialize data (in-memory)
if 'habit_data' not in st.session_state:
    st.session_state.habit_data = {}

# -----------------------------
# Add new habit
st.subheader("➕ Add a New Habit")
new_habit = st.text_input("Enter habit name (e.g., Drink Water, Read 30 mins):")

if st.button("Add Habit"):
    if new_habit:
        today = datetime.date.today().isoformat()
        if new_habit not in st.session_state.habit_data:
            st.session_state.habit_data[new_habit] = {}
        st.session_state.habit_data[new_habit][today] = False
        st.success(f"Habit '{new_habit}' added for today.")
    else:
        st.warning("Please enter a habit name.")

# -----------------------------
# Track today's habits
st.subheader("✅ Track Today's Habits")
today = datetime.date.today().isoformat()

if st.session_state.habit_data:
    for habit in list(st.session_state.habit_data.keys()):
        if today not in st.session_state.habit_data[habit]:
            st.session_state.habit_data[habit][today] = False

        checked = st.checkbox(habit, value=st.session_state.habit_data[habit][today])
        st.session_state.habit_data[habit][today] = checked
else:
    st.info("No habits yet. Add one above! 😊")

# -----------------------------
# View Progress
st.subheader("📊 Habit History")
if st.session_state.habit_data:
    for habit, days in st.session_state.habit_data.items():
        st.markdown(f"**{habit}**")
        for date, status in sorted(days.items()):
            st.write(f"{date}: {'✅' if status else '❌'}")
        st.markdown("---")
