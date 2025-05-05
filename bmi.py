import streamlit as st
import matplotlib.pyplot as plt

# Title and page config
st.set_page_config(page_title="BMI Calculator", layout="centered")
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["BMI Calculator", "Nutrition Chart", "Daily Workout"])

# Initialize session state for history
if 'bmi_history' not in st.session_state:
    st.session_state.bmi_history = []

if page == "BMI Calculator":
    st.title("💪 Enhanced BMI Calculator")
    st.write("Calculate your Body Mass Index (BMI) and get health insights.")

    # Unit selection
    unit = st.radio("Choose Unit System:", ("Metric (kg, cm)", "Imperial (lbs, inches)"))

    # Input fields
    if unit == "Metric (kg, cm)":
        weight = st.number_input("Enter your weight (kg):", min_value=1.0, step=0.1)
        height = st.number_input("Enter your height (cm):", min_value=30.0, step=0.1)
        height_m = height / 100
    else:
        weight_lbs = st.number_input("Enter your weight (lbs):", min_value=1.0, step=0.1)
        height_in = st.number_input("Enter your height (inches):", min_value=10.0, step=0.1)
        weight = weight_lbs * 0.453592
        height_m = height_in * 0.0254

    # Additional inputs
    age = st.number_input("Enter your age:", min_value=1, max_value=120, step=1)
    gender = st.selectbox("Select Gender:", ["Male", "Female", "Other"])

    calculate = st.button("Calculate BMI")

    if calculate and weight and height_m:
        bmi = weight / (height_m ** 2)
        st.markdown(f"### 🧮 Your BMI is: `{bmi:.2f}`")

        # Determine category and tips
        if bmi < 18.5:
            category = "Underweight"
            tip = "You may need to gain weight. Consider a nutrition-rich diet and talk to a healthcare provider."
            color = "#3498db"
        elif 18.5 <= bmi < 24.9:
            category = "Normal weight"
            tip = "Great job! Keep maintaining a healthy lifestyle."
            color = "#2ecc71"
        elif 25 <= bmi < 29.9:
            category = "Overweight"
            tip = "Consider regular exercise and a balanced diet to reduce weight."
            color = "#f1c40f"
        else:
            category = "Obese"
            tip = "High BMI may lead to health risks. Please consult a healthcare provider."
            color = "#e74c3c"

        st.success(f"💡 Category: **{category}**")
        st.info(f"📌 Tip: {tip}")

        # Save to history
        st.session_state.bmi_history.append({
            'age': age,
            'gender': gender,
            'bmi': round(bmi, 2),
            'category': category
        })

        # Show visual chart
        fig, ax = plt.subplots(figsize=(6, 1.2))
        ax.axhline(y=0.5, xmin=0, xmax=1, color='lightgray', linewidth=10)
        ax.axhline(y=0.5, xmin=0, xmax=bmi/40 if bmi < 40 else 1, color=color, linewidth=10)
        ax.set_xlim(0, 1)
        ax.axis('off')
        st.pyplot(fig)

        # Weight goal estimator (optional)
        target_bmi = st.slider("🎯 Select your target BMI:", 18.5, 24.9, 22.0)
        target_weight = target_bmi * (height_m ** 2)
        diff = target_weight - weight
        if abs(diff) < 1:
            st.info("✅ You're already at your target BMI!")
        elif diff > 0:
            st.warning(f"👉 You need to gain **{diff:.1f} kg** to reach your target BMI.")
        else:
            st.warning(f"👉 You need to lose **{abs(diff):.1f} kg** to reach your target BMI.")

        # Water intake estimate
        water_intake = weight * 0.033
        st.markdown(f"💧 **Recommended Daily Water Intake:** {water_intake:.1f} liters")

    # Show history
    if st.session_state.bmi_history:
        st.markdown("---")
        st.subheader("📊 BMI History")
        st.table(st.session_state.bmi_history)

    # Footer
    st.markdown("---")
    st.caption("Made with ❤️ using Streamlit")

elif page == "Nutrition Chart":
    st.title("🥗 Nutrition Chart")
    st.write("Here is a general guideline for daily nutrition based on a 2000-calorie diet:")

    nutrition_data = {
        "Nutrient": ["Carbohydrates", "Proteins", "Fats", "Fiber", "Sugars", "Sodium"],
        "Recommended Intake": ["275g", "50g", "70g", "28g", "50g", "2300mg"],
        "Good Sources": [
            "Brown rice, oats, bananas",
            "Chicken breast, lentils, Greek yogurt",
            "Avocados, almonds, olive oil",
            "Broccoli, apples, barley",
            "Oranges, milk, soft drinks",
            "Salted snacks, canned soups, deli meats"
        ]
    }

    st.table(nutrition_data)
    st.info("📌 Tip: Balanced nutrition helps maintain healthy weight and body function.")

    # Footer
    st.markdown("---")
    st.caption("Made with ❤️ using Streamlit")

elif page == "Daily Workout":
    st.title("🏃 Daily Workout & Exercise Guide")
    st.write("Stay active and healthy with these recommended daily exercises:")

    st.subheader("🚶 Steps to Walk Daily")
    st.markdown("- Aim for **8,000 to 10,000 steps** per day")

    st.subheader("💪 Suggested Exercises")
    st.markdown("""
    - **Stretching**: 5–10 minutes (morning/evening)
    - **Bodyweight exercises**:
        - Push-ups: 2 sets of 10–15 reps
        - Squats: 2 sets of 15 reps
        - Lunges: 2 sets per leg
    - **Cardio**:
        - Brisk walking, cycling or jogging: 20–30 minutes
    - **Core strengthening**:
        - Plank: Hold for 30–60 seconds
        - Crunches: 2 sets of 15 reps
    """)

    st.subheader("💧 Hydration Reminder")
    st.info("Drink at least **2 to 3 liters of water** daily. Increase intake during physical activity.")

    st.markdown("---")
    st.caption("Stay active 💥 Stay healthy")

