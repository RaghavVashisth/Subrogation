import streamlit as st
import pandas as pd

# -------------------- Login Credential System --------------------
# Define user credentials
USER_CREDENTIALS = {
    "admin": "admin123",
    "exluser": "exl2025"
}

# Initialize login state
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
    st.session_state.username = ""

def login():
    st.image("exl logo.png", use_container_width=True)

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    login_btn = st.button("Login")

    if login_btn:
        if username in USER_CREDENTIALS and USER_CREDENTIALS[username] == password:
            st.session_state.logged_in = True
            st.session_state.username = username
            st.success(f"✅ Welcome, {username}!")
            st.rerun()
        else:
            st.error("❌ Invalid username or password")

if not st.session_state.logged_in:
    login()
    st.stop()

# -------------------- Main Page Config --------------------
st.set_page_config(page_title="Subrogation Propensity Claims Dashboard", layout="wide")
st.title("🚨 Subrogation Propensity Claims Review Dashboard")

# -------------------- CSS Styling --------------------
st.markdown("""
    <style>
        .stApp {
            background-color: #FFFFFF;
            color: black;
        }

        section[data-testid="stSidebar"] {
            background-color: #F5F5F5 !important;
            color: black !important;
        }

        * {
            color: black !important;
        }

        div[data-baseweb="select"] > div,
        div[data-baseweb="select"],
        div[data-baseweb="popover"],
        div[data-baseweb="option"],
        div[data-baseweb="menu"] {
            background-color: white !important;
            color: black !important;
            border: 1px solid #ccc !important;
            border-radius: 5px !important;
        }

        div[data-baseweb="option"]:hover,
        div[data-baseweb="option"][aria-selected="true"] {
            background-color: #e6e6e6 !important;
        }

        .stButton > button {
            background-color: white !important;
            color: black !important;
            border: 1px solid #ccc !important;
            border-radius: 5px !important;
        }

        .stButton > button:hover {
            background-color: #e6e6e6 !important;
        }
    </style>
""", unsafe_allow_html=True)

# -------------------- Load Data --------------------
path = 'syntheticsubrogationfulldataset_2.csv'

@st.cache_data(ttl=0)
def load_data():
    df = pd.read_csv(path)
    df['Prediction'] = pd.to_numeric(df['Prediction'], errors='coerce').fillna(0).astype(int)
    if 'User_Action' not in df.columns:
        df['User_Action'] = ''
    return df

df = load_data()

# -------------------- Sidebar Filters --------------------
st.sidebar.image("exl logo.png", use_container_width=True)
st.sidebar.header("🔎 Filters")

state_filter = st.sidebar.selectbox('STATE', df['STATE_GROUP'].unique())
peril_filter = st.sidebar.selectbox("MAJOR PERIL", df['MAJ_PERIL_CD'].unique())
sub_det = st.sidebar.selectbox("LOB SUB-LOB", df['SUB_DTL_DESC'].unique())

# -------------------- Filter Data --------------------
filtered_df = df[
    (df['STATE_GROUP'] == state_filter) &
    (df['MAJ_PERIL_CD'] == peril_filter) &
    (df['SUB_DTL_DESC'] == sub_det)
]

# -------------------- Show Suspicious Claims --------------------
suspicious_df = filtered_df[filtered_df['Prediction'] == 1].copy()

if suspicious_df.empty:
    st.info("No suspected fraudulent claims found with current filters.")
else:
    st.subheader("📋 Review and Act on Each Suspected Claim")

    for idx, row in suspicious_df.iterrows():
        st.markdown("---")
        cols = st.columns([1.5, 1.2, 1.2, 1.2, 1, 1.2, 1.2, 1.2, 1, 2, 1.2])

        with cols[0]: st.markdown(f"**Claim:** {row['Claim_Number']}")
        with cols[1]: st.markdown(f"**Peril:** {row['MAJ_PERIL_CD']}")
        with cols[2]: st.markdown(f"**State:** {row['FTR_JRSDTN_ST']}")
        with cols[3]: st.markdown(f"**Paid:** ${row['PAID_FINAL']:.2f}")
        with cols[4]: st.markdown(f"**Age:** {row['CLMNT_AGE_AT_TM_OF_LOSS']}")
        with cols[5]: st.markdown(f"**Injury:** {row['INJRY_TYPE_DESC']}")
        with cols[6]: st.markdown(f"**Loss Party:** {row['LOSS_PARTY']}")
        with cols[7]: st.markdown(f"**Severity:** {row['CLM_LOSS_SEVERITY_CD']}")
        with cols[8]: st.markdown(f"**ML Score:** {row['Prediction']}")

        with cols[9]:
            selected_action = st.selectbox(
                "Action",
                ["", "ASSIGNED", "NOT ASSIGNED", "No Action"],
                key=f"action_{idx}",
                index=["", "ASSIGNED", "NOT ASSIGNED", "No Action"].index(row['User_Action']) if row['User_Action'] in ["", "ASSIGNED", "NOT ASSIGNED", "No Action"] else 0
            )


        with cols[10]:
            if st.button("💾 Save", key=f"save_{idx}"):
                df_all = pd.read_csv(path)
                df_all.at[idx, 'User_Action'] = selected_action
                df_all.to_csv('claims_data.csv', index=False)
                st.success(f"✅ Action saved for Claim {row['Claim_Number']}")
