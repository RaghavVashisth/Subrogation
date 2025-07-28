import streamlit as st
import pandas as pd





# st.markdown("""
#     <style>
#         /* Main app background */
#         .stApp {
#             background-color: #FFFFFF;
#             color: black;
#         }

#         /* Sidebar background */
#         section[data-testid="stSidebar"] {
#             background-color: #F5F5F5 !important;
#             color: black !important;
#         }

#         /* Force black text everywhere */
#         h1, h2, h3, h4, h5, h6,
#         p, div, span, label, input, select,
#         .stMarkdown, .css-16idsys, .css-1cpxqw2, .stTextInput, .stSelectbox {
#             color: black !important;
#         }

#         /* Optional: Button text color */
#         .stButton > button {
#             color: black !important;
#         }

#     </style>
# """, unsafe_allow_html=True)

# st.markdown("""
#     <style>
#         /* App background */
#         .stApp {
#             background-color: #FFFFFF;
#             color: black;
#         }

#         /* Sidebar background */
#         section[data-testid="stSidebar"] {
#             background-color: #F5F5F5 !important;
#             color: black !important;
#         }

#         /* Force all text to black */
#         * {
#             color: black !important;
#         }

#         /* Sidebar selectbox background fix */
#         section[data-testid="stSidebar"] .stSelectbox > div[data-baseweb="select"] {
#             background-color: white !important;
#             color: black !important;
#             border: 1px solid #ccc !important;
#             border-radius: 6px !important;
#         }

#         /* Selected value text in selectbox */
#         section[data-testid="stSidebar"] .stSelectbox div[class*="SingleValue"] {
#             color: black !important;
#         }

#         /* Dropdown menu background + text */
#         div[data-baseweb="popover"] > div {
#             background-color: white !important;
#             color: black !important;
#             border: 1px solid #ccc !important;
#         }

#         /* Each option in dropdown */
#         div[data-baseweb="option"] {
#             background-color: white !important;
#             color: black !important;
#         }

#         /* Hover effect */
#         div[data-baseweb="option"]:hover {
#             background-color: #f0f0f0 !important;
#         }

#         /* Buttons */
#         .stButton > button {
#             background-color: white !important;
#             color: black !important;
#             border: 1px solid #ccc !important;
#             border-radius: 5px !important;
#         }

#         .stButton > button:hover {
#             background-color: #e6e6e6 !important;
#         }
#         /* Style for all selectbox containers */
#         div[data-baseweb="select"] {
#             background-color: white !important;
#             color: black !important;
#         }

#         /* Style the control (text + dropdown arrow area) */
#         div[data-baseweb="select"] > div {
#             background-color: white !important;
#             color: black !important;
#         }

#         /* Style selected text */
#         div[data-baseweb="select"] span {
#             color: black !important;
#         }

#         /* Style dropdown items */
#         div[data-baseweb="menu"] {
#             background-color: white !important;
#             color: black !important;
#         }
        
#         /* Style dropdown option hover */
#         div[data-baseweb="option"]:hover {
#             background-color: #e6e6e6 !important;
#         }


#     </style>
# """, unsafe_allow_html=True)


st.markdown("""
    <style>
        /* Main app background and text */
        .stApp {
            background-color: #FFFFFF;
            color: black;
        }

        /* Sidebar background and text */
        section[data-testid="stSidebar"] {
            background-color: #F5F5F5 !important;
            color: black !important;
        }

        /* Force all text to black globally */
        * {
            color: black !important;
        }
            
    /* Change selectbox main area */
    div[data-baseweb="select"] > div {
        background-color: white !important;
        color: black !important;
    }

    /* Change dropdown background and text */
    div[data-baseweb="popover"] {
        background-color: white !important;
        color: black !important;
    }

    /* Dropdown option items */
    div[data-baseweb="option"] {
        background-color: white !important;
        color: black !important;
    }

    /* Hover effect on dropdown items */
    div[data-baseweb="option"]:hover {
        background-color: #f0f0f0 !important;
        color: black !important;
    }
            
        /* Buttons */
        .stButton > button {
            background-color: white !important;
            color: black !important;
            border: 1px solid #ccc !important;
            border-radius: 5px !important;
        }

        .stButton > button:hover {
            background-color: #e6e6e6 !important;
        }

    /* Focused/active selected item */
    div[data-baseweb="option"][aria-selected="true"] {
        background-color: #e0e0e0 !important;
        color: black !important;
    }

        div[role="listbox"] li:nth-of-type(1){
            background-color: red;
        }
        div[role="listbox"] li:nth-of-type(2){
            background-color: blue;
        }

    </style>
""", unsafe_allow_html=True)


# Load data
# @st.cache_data
# def load_data():
#     df = pd.read_csv('syntheticsubrogationfulldataset_2.csv')
#     df['Prediction'] = df['Prediction'].astype(int)
#     return df

path = 'syntheticsubrogationfulldataset_2.csv'
@st.cache_data(ttl=0)
def load_data():
    df = pd.read_csv(path)
    df['Prediction'] = pd.to_numeric(df['Prediction'], errors='coerce').fillna(0).astype(int)
    
    # Ensure action column exists
    if 'User_Action' not in df.columns:
        df['User_Action'] = ''  # Empty string for no action
    return df



df = load_data()






st.set_page_config(page_title="Subrogation Propensity Claims Dashboard", layout="wide")
st.title("🚨 Subrogation Propensity Claims Review Dashboard")

# state_filter = st.sidebar.multiselect("State", options=df['FTR_JRSDTN_ST'].unique(), default=df['FTR_JRSDTN_ST'].unique())
# peril_filter = st.sidebar.multiselect("Major Peril", options=df['MAJ_PERIL_CD'].unique(), default=df['MAJ_PERIL_CD'].unique())
# sub_det = st.sidebar.multiselect("Major Peril", options=df['SUB_DTL_DESC'].unique(), default=df['SUB_DTL_DESC'].unique())

# Dropdown for filtering
st.sidebar.image("exl logo.png", use_container_width=True)

# Sidebar filters
st.sidebar.header("🔎 Filters")

state_filter = st.sidebar.selectbox('STATE', df['STATE_GROUP'].unique())
peril_filter = st.sidebar.selectbox("MAJOR PERIL", df['MAJ_PERIL_CD'].unique())
sub_det = st.sidebar.selectbox("LOB SUB-LOB", df['SUB_DTL_DESC'].unique())

# Filter datae
# filtered_data = data[data['Category'] == category]


# filtered_df = df[
#     (df['STATE_GROUP'].isin(state_filter)) &
#     (df['MAJ_PERIL_CD'].isin(peril_filter)) &
#     (df['SUB_DTL_DESC'].isin(sub_det))
# ]

filtered_df = df[
    (df['STATE_GROUP'] == state_filter) &
    (df['MAJ_PERIL_CD'] == peril_filter) &
    (df['SUB_DTL_DESC'] == sub_det)
]


# Display suspicious claims
st.subheader("🔍 Suspected Subrogation propensity Claims")
# suspicious_df = filtered_df[filtered_df['Prediction'] == 1]

# if suspicious_df.empty:
#     st.info("No suspected Subrogated propensity claims found with current filters.")
# else:
#     selected_index = st.selectbox("Select a Claim", suspicious_df.index, format_func=lambda i: suspicious_df.loc[i, "Claim_Number"])
#     selected_claim = suspicious_df.loc[selected_index]

#     # Display details
#     with st.expander("📋 Claim Details", expanded=True):
#         st.write(selected_claim)

#     # Allow actions
#     st.subheader("🚦 Take Action on This Claim")
#     action = st.radio("Choose Action", ["Mark as Reviewed", "Flag for Investigation", "No Action"])
    
#     if st.button("Submit Action"):
#         st.success(f"✅ Action '{action}' submitted for Claim {selected_claim['Claim_Number']}")

#     # Optional: Show table
#     with st.expander("📊 All Suspected Claims Table"):
#         st.dataframe(suspicious_df)


# Filter suspicious claims
# suspicious_df = filtered_df[filtered_df['Prediction'] == 1].copy()

# if suspicious_df.empty:
#     st.info("No suspected fraudulent claims found with current filters.")
# else:
#     st.subheader("📝 Take Action on Suspected Claims")

#     # Create session state for updates
#     if 'updated_actions' not in st.session_state:
#         st.session_state.updated_actions = {}

#     # Build table with actions
#     for idx, row in suspicious_df.iterrows():
#         cols = st.columns([1.5, 3, 2, 2, 2])
#         with cols[0]:
#             st.markdown(f"**{row['Claim_Number']}**")

#         with cols[1]:
#             st.markdown(f"**Peril:** {row['MAJ_PERIL_CD']}, **State:** {row['FTR_JRSDTN_ST']}")
#         with cols[2]:
#             st.markdown(f"Paid: ${row['PAID_FINAL']:.2f}")
#         with cols[3]:
#             selected_action = st.selectbox(
#                 "Select Action",
#                 ["", "ASSIGNED", "NOT ASSIGNED"],
#                 key=f"action_{idx}",
#                 index=["", "ASSIGNED", "NOT ASSIGNED"].index(row['User_Action']) if row['User_Action'] in ["", "ASSIGNED", "NOT ASSIGNED"] else 0
#             )
#         with cols[4]:
#             st.session_state.updated_actions[idx] = selected_action

#     # Save Button
#     if st.button("💾 Save All Actions"):
#         df = pd.read_csv(path)  # Reload full data
#         for idx, action in st.session_state.updated_actions.items():
#             df.at[idx, 'User_Action'] = action
#         df.to_csv(path, index=False)
#         st.success("✅ Actions saved to CSV successfully!")


suspicious_df = filtered_df[filtered_df['Prediction'] == 1].copy()

if suspicious_df.empty:
    st.info("No suspected fraudulent claims found with current filters.")
else:
    st.subheader("📋 Review and Act on Each Suspected Claim")

    for idx, row in suspicious_df.iterrows():
        st.markdown(f"---")
        cols = st.columns([1.5, 1.2, 1.2, 1.2, 1, 1.2, 1.2, 1.2, 1, 2, 1.2])
        
        with cols[0]:
            st.markdown(f"**Claim:** {row['Claim_Number']}")
        with cols[1]:
            st.markdown(f"**Peril:** {row['MAJ_PERIL_CD']}")
        with cols[2]:
            st.markdown(f"**State:** {row['FTR_JRSDTN_ST']}")
        with cols[3]:
            st.markdown(f"**Paid:** ${row['PAID_FINAL']:.2f}")
        with cols[4]:
            st.markdown(f"**Age:** {row['CLMNT_AGE_AT_TM_OF_LOSS']}")
        with cols[5]:
            st.markdown(f"**Injury:** {row['INJRY_TYPE_DESC']}")
        with cols[6]:
            st.markdown(f"**Loss Party:** {row['LOSS_PARTY']}")
        with cols[7]:
            st.markdown(f"**Severity:** {row['CLM_LOSS_SEVERITY_CD']}")
        with cols[8]:
            st.markdown(f"**Ml Score:** {row['Prediction']}")
        
        # Action selector
        with cols[9]:
            selected_action = st.selectbox(
                "Action",
                ["", "ASSIGNED", "NOT ASSIGNED", "No Action"],
                key=f"action_{idx}",
                index=["", "ASSIGNED", "NOT ASSIGNED", "No Action"].index(row['User_Action']) if row['User_Action'] in ["", "ASSIGNED", "NOT ASSIGNED", "No Action"] else 0
            )
        
        # Save button
        with cols[10]:
            if st.button("💾 Save", key=f"save_{idx}"):
                df_all = pd.read_csv(path)
                df_all.at[idx, 'User_Action'] = selected_action
                df_all.to_csv('claims_data.csv', index=False)
                st.success(f"✅ Action saved for Claim {row['Claim_Number']}")
