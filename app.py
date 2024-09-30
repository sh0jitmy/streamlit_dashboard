import streamlit as st
import pandas as pd

# カスタムCSSの埋め込み（選択中のURIを赤色にする）
shadcn_ui_css = """
<style>
body {
    font-family: 'Inter', sans-serif;
    background-color: #f9fafb;
}
.sidebar .sidebar-content {
    background-color: #111827;
    color: white;
    padding: 20px;
}
.sidebar .sidebar-content h1 {
    color: #3b82f6;
}
a {
    color: white;
    text-decoration: none;
    padding: 5px;
    display: block;
}
a.selected {
    color: red;
}
</style>
"""

st.markdown(shadcn_ui_css, unsafe_allow_html=True)

# URIのリスト（ダッシュボードのコンポーネント）
uris = {
    "Home": "/home",
    "Device Status": "/device-status",
    "Temperature": "/temperature",
    "Humidity": "/humidity"
}

# セッションステートに選択されたURIを保存
if "selected_uri" not in st.session_state:
    st.session_state.selected_uri = "/home"  # デフォルトのURI

# サイドバーにURIを表示
st.sidebar.title("Dashboard Navigation")
for name, uri in uris.items():
    # 現在選択されているURIに基づいてクラスを付与
    if uri == st.session_state.selected_uri:
        st.sidebar.markdown(f'<a href="#" class="selected">{name}</a>', unsafe_allow_html=True)
    else:
        if st.sidebar.markdown(f'<a href="#" onclick="set_uri(\'{uri}\')">{name}</a>', unsafe_allow_html=True):
            st.session_state.selected_uri = uri

# URIに応じたコンテンツを表示
st.title(f"Dashboard Component: {st.session_state.selected_uri}")

if st.session_state.selected_uri == "/home":
    st.write("これはホームページです。")
elif st.session_state.selected_uri == "/device-status":
    # IoTデバイスのステータス
    iot_data = pd.DataFrame({
        "Device": ["Device 1", "Device 2", "Device 3"],
        "Status": ["Online", "Offline", "Online"]
    })
    st.subheader("デバイスステータス")
    st.table(iot_data)
elif st.session_state.selected_uri == "/temperature":
    # 温度データのグラフ
    temperature_data = pd.DataFrame({
        "Device": ["Device 1", "Device 2", "Device 3"],
        "Temperature": [25, 30, 28]
    })
    st.subheader("温度データ")
    st.line_chart(temperature_data.set_index("Device"))
elif st.session_state.selected_uri == "/humidity":
    # 湿度データのグラフ
    humidity_data = pd.DataFrame({
        "Device": ["Device 1", "Device 2", "Device 3"],
        "Humidity": [40, 35, 42]
    })
    st.subheader("湿度データ")
    st.line_chart(humidity_data.set_index("Device"))
