import streamlit as st
import pandas as pd
import datetime

# --- إعدادات النظام ---
st.set_page_config(page_title="غرفة العمليات المركزية", layout="wide")

# 1. نظام الحماية (Login)
def check_auth():
    if "authenticated" not in st.session_state:
        st.session_state.authenticated = False
    
    if not st.session_state.authenticated:
        st.title("🛡️ نظام الوصول الآمن")
        password = st.text_input("أدخل كلمة مرور الإدارة", type="password")
        if st.button("دخول"):
            if password == "Admin2026": # غير كلمة السر هنا
                st.session_state.authenticated = True
                st.rerun()
            else:
                st.error("كلمة المرور غير صحيحة")
        return False
    return True

if check_auth():
    # 2. الهيكل الجانبي (المراقبة والتحكم)
    st.sidebar.title("🎮 لوحة التحكم بالعمليات")
    page = st.sidebar.selectbox("اختر القسم", ["الداشبورد الرئيسية", "سجل الأخطاء والحلول", "تحديث البيانات حياً"])

    # 3. محاكي "حساسات الأخطاء" (النظام الذي اقترحته أنت)
    if 'error_log' not in st.session_state:
        st.session_state.error_log = []

    def add_error(title, details, severity):
        new_error = {
            "Time": datetime.datetime.now().strftime("%Y-%m-%d %H:%M"),
            "Issue": title,
            "Details": details,
            "Severity": severity
        }
        st.session_state.error_log.append(new_error)

    # 4. عرض الداشبورد الرئيسية
    if page == "الداشبورد الرئيسية":
        st.title("📊 مركز قيادة الشركة")
        col1, col2, col3 = st.columns(3)
        col1.metric("المبيعات (ERP)", "150,000 ج.م", "8%+")
        col2.metric("التكاليف", "45,000 ج.م", "-2% (تحسن)")
        col3.metric("نشاط الـ GPS", "95%", "مستقر")
        
        st.divider()
        st.subheader("📍 خريطة الأداء اللحظي")
        # هنا يمكن إضافة خرائط حقيقية لاحقاً
        st.info("النظام جاهز لاستقبال بيانات حقيقية من ملفات Excel أو قواعد بيانات SQL.")

    # 5. سجل الأخطاء (غرفة العمليات)
    elif page == "سجل الأخطاء والحلول":
        st.title("⚠️ مركز إدارة الأزمات")
        
        # تجربة الحساسات (Thresholds)
        with st.expander("فحص الحساسات (Manual Trigger)"):
            exp = st.number_input("أدخل قيمة المصروفات الحالية", value=800)
            gps = st.number_input("وقت انقطاع الإشارة (بالدقائق)", value=10)
            if st.button("تشغيل الفحص الآلي"):
                if exp > 1000: add_error("تجاوز ميزانية", f"تم صرف {exp} ج.م", "🔴 حرجة")
                if gps > 60: add_error("انقطاع اتصال", f"فقدان GPS لمدة {gps} دقيقة", "🟡 متوسطة")
                st.success("تم تحديث السجل")

        if st.session_state.error_log:
            df = pd.DataFrame(st.session_state.error_log)
            st.table(df)
            
            # تحميل التقرير
            csv = df.to_csv(index=False).encode('utf-8-sig')
            st.download_button("📥 تحميل سجل الأخطاء للمدير", data=csv, file_name="error_report.csv", mime="text/csv")
        else:
            st.write("✅ لا توجد مشكلات مسجلة حالياً.")

    # زر خروج
    if st.sidebar.button("تسجيل الخروج"):
        st.session_state.authenticated = False
        st.rerun()
