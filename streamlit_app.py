import streamlit as st
import pandas as pd

# --- إعدادات الصفحة والخط ---
st.set_page_config(page_title="نظام النخاع العصبي", layout="wide", initial_sidebar_state="expanded")

# دمج خط Rubik وتنسيق Apple عبر CSS
st.markdown("""
    <link href="https://fonts.googleapis.com/css2?family=Rubik:wght@400;700&display=swap" rel="stylesheet">
    <style>
    html, body, [class*="css"] {
        font-family: 'Rubik', sans-serif;
        direction: rtl;
        text-align: right;
    }
    .stButton>button {
        border-radius: 15px;
        height: 3em;
        width: 100%;
        font-weight: bold;
        border: None;
    }
    .main-card {
        padding: 20px;
        border-radius: 20px;
        background-color: #F2F2F7;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        margin-bottom: 20px;
    }
    .metric-card-green {
        background-color: #34C759;
        color: white;
        padding: 25px;
        border-radius: 20px;
        text-align: center;
    }
    .metric-card-red {
        background-color: #FF3B30;
        color: white;
        padding: 25px;
        border-radius: 20px;
        text-align: center;
    }
    </style>
    """, unsafe_allow_index=True)

# --- القائمة الجانبية (Sidebar) تشبه Apple ---
with st.sidebar:
    st.markdown("<h1 style='text-align: center;'></h1>", unsafe_allow_index=True)
    st.title("إدارة الشركة")
    st.markdown("---")
    menu = st.radio("القائمة الرئيسية", ["الرئيسية 🏠", "غرفة العمليات ⚠️", "التقارير 📊", "الإعدادات ⚙️"])

# --- الصفحة الرئيسية ---
if "الرئيسية" in menu:
    st.markdown("<h2 style='text-align: right;'>نظرة عامة على الأداء</h2>", unsafe_allow_index=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""<div class="metric-card-green">
            <h3>المبيعات والنمو</h3>
            <h1 style='color: white;'>150,000 ج.م</h1>
            <p>↑ 12% منذ الشهر الماضي</p>
        </div>""", unsafe_allow_index=True)
        
    with col2:
        st.markdown("""<div class="metric-card-red">
            <h3>المصروفات والديون</h3>
            <h1 style='color: white;'>45,000 ج.م</h1>
            <p>↑ 5% يحتاج مراجعة</p>
        </div>""", unsafe_allow_index=True)

    st.markdown("---")
    st.subheader("تحليل الأقسام")
    # محاكاة بيانات الأقسام من ملف الهيكل الخاص بك
    data = {
        "القسم": ["ERP", "المراقبة AI", "الـ GPS", "الرقم الموحد"],
        "الحالة": ["✅ يعمل", "⚠️ يحتاج صيانة", "✅ يعمل", "✅ يعمل"],
        "الكفاءة": ["95%", "60%", "99%", "88%"]
    }
    st.table(pd.DataFrame(data))

# --- غرفة العمليات (المشاكل والحلول) ---
elif "غرفة العمليات" in menu:
    st.markdown("<h2 style='color: #FF3B30;'>⚠️ مركز إدارة الأزمات</h2>", unsafe_allow_index=True)
    
    st.info("هنا تظهر المشاكل التي تتجاوز الحدود (Thresholds) التي حددتها.")
    
    issues = [
        {"المشكلة": "تجاوز مصروفات فرع أ", "الدرجة": "حرجة", "الحل المقترح": "مراجعة فواتير الصيانة"},
        {"المشكلة": "توقف كاميرا المنطقة 3", "الدرجة": "متوسطة", "الحل المقترح": "إعادة تشغيل الـ Raspberry Pi"},
        {"المشكلة": "انقطاع GPS سيارة 5", "الدرجة": "بسيطة", "الحل المقترح": "الاتصال بالسائق"}
    ]
    
    for issue in issues:
        with st.expander(f"{issue['المشكلة']} - ({issue['الدرجة']})"):
            st.write(f"**الحل المقترح:** {issue['الحل المقترح']}")
            if st.button(f"تحديد كمحلولة - {issue['المشكلة']}"):
                st.success("تم نقل المشكلة للأرشيف")
