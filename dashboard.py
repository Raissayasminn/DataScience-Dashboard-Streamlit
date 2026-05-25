import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from PIL import Image

# =====================================
# PAGE CONFIG
# =====================================
st.set_page_config(
    page_title="PharmaSix Dashboard",
    layout="wide"
)

# =====================================
# LOAD DATA
# =====================================
df = pd.read_csv("pharmasix_dataset.csv")
df["date"] = pd.to_datetime(df["date"])
logo = Image.open("pharmasix_logo.png")

# =====================================
# CUSTOM CSS
# =====================================
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700;800&display=swap');

html, body, [class*="css"], .stApp {
    font-family: 'Poppins', sans-serif !important;
}

.stApp {
    background: #D9E7F7 !important;
    color: #0F172A !important;
}

.block-container {
    padding-top: 2rem !important;
    padding-left: 2.5rem !important;
    padding-right: 2.5rem !important;
}

/* SIDEBAR */
section[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #071B4D 0%, #102A72 100%) !important;
    border-right: none !important;
}

section[data-testid="stSidebar"] * {
    color: white !important;
}

section[data-testid="stSidebar"] hr {
    border-color: rgba(255,255,255,0.20) !important;
}

.sidebar-title {
    font-size: 31px;
    font-weight: 800;
    margin-bottom: 6px;
    color: white !important;
}

.sidebar-subtitle {
    font-size: 13px;
    color: #C7D2FE !important;
    margin-bottom: 24px;
}

.filter-title {
    font-size: 24px;
    font-weight: 800;
    margin-top: 14px;
    margin-bottom: 6px;
    color: white !important;
}

.filter-caption {
    font-size: 13px;
    color: #BFDBFE !important;
    margin-bottom: 18px;
}

section[data-testid="stSidebar"] label p {
    font-size: 14px !important;
    font-weight: 600 !important;
    color: #E0EAFF !important;
}

section[data-testid="stSidebar"] .stCheckbox label p {
    color: #FFFFFF !important;
    font-weight: 600 !important;
}

/* MULTISELECT */
.stMultiSelect div[data-baseweb="select"] {
    background-color: #F8FAFC !important;
    border-radius: 14px !important;
    border: 2px solid #E2E8F0 !important;
    min-height: 48px !important;
}

.stMultiSelect input {
    color: #111827 !important;
}

.stMultiSelect div[data-baseweb="select"] span {
    color: #111827 !important;
}

[data-baseweb="tag"] {
    background-color: #2563EB !important;
    border-radius: 9px !important;
    border: none !important;
}

[data-baseweb="tag"] span {
    color: white !important;
}

[data-baseweb="tag"] svg {
    fill: white !important;
}

div[data-baseweb="popover"],
div[data-baseweb="menu"],
div[data-baseweb="option"] {
    background-color: #F8FAFC !important;
    color: #111827 !important;
}

/* HEADER */
.dashboard-title {
    font-size: 42px;
    font-weight: 800;
    color: #0F172A !important;
    margin-bottom: 2px;
}

.dashboard-subtitle {
    color: #475569 !important;
    font-size: 16px;
    margin-bottom: 28px;
}

/* KPI */
.kpi-card {
    background: #FFFFFF !important;
    padding: 20px;
    border-radius: 16px;
    border: 1px solid #E5E7EB;
    box-shadow: 0px 8px 22px rgba(15, 23, 42, 0.10);

    min-height: 135px;
    height: 100%;

    display: flex;
    flex-direction: column;
    justify-content: flex-start;

    overflow: hidden;
}
.kpi-title {
    color: #334155 !important;
    font-size: 14px;
    font-weight: 600;
    margin-bottom: 9px;
}

.kpi-value {
    color: #0F172A !important;
    font-size: 30px;
    font-weight: 800;
    line-height: 1.15;
}

.kpi-desc {
    font-size: 13px;
    margin-top: 10px;
    font-weight: 500;
}

.green { color: #16A34A !important; }
.red { color: #EF4444 !important; }
.orange { color: #F97316 !important; }

/* CHART BOX */
.chart-box {
    background: #FFFFFF !important;
    padding: 22px;
    border-radius: 18px;
    border: 1px solid #E5E7EB;
    box-shadow: 0px 8px 22px rgba(15, 23, 42, 0.10);
    margin-bottom: 22px;
    display: block;
    overflow: hidden;
}

.chart-title {
    color: #0F172A !important;
    font-size: 22px;
    font-weight: 800;
    margin-bottom: 6px;
}

.chart-subtitle {
    color: #13161A !important;
    font-size: 14px;
    margin-bottom: 16px;
}

/* INSIGHT BOX */
.insight-box {
    background: #F8FAFC;
    padding: 18px 20px;
    border-radius: 14px;
    border: 1px solid #CBD5E1;
    border-left: 6px solid #363779;
    color: #334155 !important;
    font-size: 15px;
    line-height: 1.7;
    margin-top: 14px;
    display: flex;
    align-items: center;
    gap: 16px;
}

.insight-icon {
    background: #363779;
    color: white !important;
    min-width: 46px;
    height: 46px;
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
}

.insight-text {
    color: #334155 !important;
}

.insight-text b {
    color: #1E293B !important;
}

/* SELECTBOX */
.stSelectbox div[data-baseweb="select"] {
    background-color: #F8FAFC !important;
    border-radius: 12px !important;
    border: 1px solid #CBD5E1 !important;
}

.stSelectbox span {
    color: #111827 !important;
}

/* BUTTON */
div.stButton > button {
    background: linear-gradient(90deg, #2E86FF, #0C72D6) !important;
    color: white !important;
    border-radius: 12px !important;
    border: none !important;
    font-weight: bold !important;
    padding: 12px 20px !important;
    min-height: 50px !important;
    width: 240px !important;
}

/* DOWNLOAD BUTTON */
div.stDownloadButton > button {
    background: linear-gradient(90deg, #FF7F50, #FF6347) !important;
    color: white !important;
    border-radius: 12px !important;
    border: none !important;
    font-weight: bold !important;
    padding: 12px 20px !important;
    min-height: 50px !important;
    width: 240px !important;
}

</style>
""", unsafe_allow_html=True)

# =====================================
# SIDEBAR
# =====================================
st.sidebar.image(logo, width=105)

st.sidebar.markdown("""
<div class="sidebar-title">PharmaSix</div>
<div class="sidebar-subtitle">Medicine Sales Intelligence</div>
<hr>
<div class="filter-title">🧭 Control Panel</div>
<div class="filter-caption">Atur data yang ingin ditampilkan pada dashboard.</div>
""", unsafe_allow_html=True)

all_years = sorted(df["year"].unique())
select_all_years = st.sidebar.checkbox("Pilih semua tahun", value=True)

if select_all_years:
    selected_years = st.sidebar.multiselect("Periode Tahun", options=all_years, default=all_years)
else:
    selected_years = st.sidebar.multiselect("Periode Tahun", options=all_years, default=[])

all_regions = sorted(df["region"].unique())
select_all_regions = st.sidebar.checkbox("Pilih semua region", value=True)

if select_all_regions:
    selected_regions = st.sidebar.multiselect("Region", options=all_regions, default=all_regions)
else:
    selected_regions = st.sidebar.multiselect("Region", options=all_regions, default=[])

all_categories = sorted(df["category"].unique())
select_all_categories = st.sidebar.checkbox("Pilih semua kategori", value=True)

if select_all_categories:
    selected_category = st.sidebar.multiselect("Kategori Obat", options=all_categories, default=all_categories)
else:
    selected_category = st.sidebar.multiselect("Kategori Obat", options=all_categories, default=[])

# =====================================
# FILTER DATA
# =====================================
filtered_df = df[
    (df["year"].isin(selected_years)) &
    (df["region"].isin(selected_regions)) &
    (df["category"].isin(selected_category))
]

if filtered_df.empty:
    st.warning("Data kosong. Pilih minimal satu tahun, region, dan kategori.")
    st.stop()

# =====================================
# HEADER
# =====================================
col_logo, col_title = st.columns([0.7, 8])

with col_logo:
    st.image(logo, width=78)

with col_title:
    st.markdown("""
    <div class="dashboard-title">PharmaSix Dashboard</div>
    <div class="dashboard-subtitle">Analisis penjualan dan permintaan obat tahun 2020-2025</div>
    """, unsafe_allow_html=True)

# =====================================
# KPI SECTION
# =====================================
unit_sold = filtered_df["units_sold"].sum()

medicine_sales = (
    filtered_df.groupby("medicine", as_index=False)["units_sold"]
    .sum()
    .sort_values("units_sold", ascending=False)
)

top_med = medicine_sales.iloc[0]
low_med = medicine_sales.iloc[-1]

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown(f"""
    <div class="kpi-card">
        <div class="kpi-title">📦 Unit Sold</div>
        <div class="kpi-value" style="font-size:22px;">{unit_sold:,.0f}</div>
        <div class="kpi-desc green">Total unit terjual</div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown(f"""
    <div class="kpi-card">
        <div class="kpi-title">📈 Penjualan Tertinggi</div>
        <div class="kpi-value" style="font-size:25px;">{top_med["medicine"]}</div>
        <div class="kpi-desc green">{top_med["units_sold"]:,.3f} pcs terjual</div>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown(f"""
    <div class="kpi-card">
        <div class="kpi-title">📉 Penjualan Terendah</div>
        <div class="kpi-value" style="font-size:25px;">{low_med["medicine"]}</div>
        <div class="kpi-desc red">{low_med["units_sold"]:,.3f} pcs terjual</div>
    </div>
    """, unsafe_allow_html=True)

with col4:
    total_price = (filtered_df["units_sold"] * filtered_df["unit_price"]).sum()

    st.markdown(f"""
    <div class="kpi-card">
        <div class="kpi-title">💰 Total Price</div>
        <div class="kpi-value" style="font-size:25px;">Rp {total_price:,.2f}</div>
        <div class="kpi-desc orange">Harga total penjualan</div>
    </div>
    """, unsafe_allow_html=True)

# =====================================
# ROW 1: VOLUME + POLA MUSIMAN
# =====================================
col5, col6 = st.columns(2)

# =====================================
# CHART 1: VOLUME PENJUALAN
# =====================================
with col5:
    # st.markdown('<div class="chart-box">', unsafe_allow_html=True)
    st.markdown("<div style='margin-top:35px;'></div>", unsafe_allow_html=True)

    st.markdown("""
    <div class="chart-title">Volume Penjualan Obat Tertinggi & Terendah</div>
    <div class="chart-subtitle">
        Kontribusi penjualan masing - masing obat (%) berdasarkan total unit sold
    </div>
    """, unsafe_allow_html=True)

    medicine_sales_percent = (
        filtered_df.groupby("medicine", as_index=False)["units_sold"]
        .sum()
        .sort_values("units_sold", ascending=False)
    )

    total_units = medicine_sales_percent["units_sold"].sum()
    medicine_sales_percent["percentage"] = medicine_sales_percent["units_sold"] / total_units * 100

    medicine_sales_percent = medicine_sales_percent.sort_values("percentage", ascending=False)

    medicine_sales_percent["label"] = medicine_sales_percent["percentage"].map(lambda x: f"{x:.1f}%")

    medicine_sales_percent["color_group"] = [
        "Top" if i < 5 else "Bottom"
        for i in range(len(medicine_sales_percent))
    ]

    fig = px.bar(
        medicine_sales_percent.sort_values("percentage", ascending=True),
        x="percentage",
        y="medicine",
        orientation="h",
        text="label",
        color="color_group",
        color_discrete_map={
            "Top": "#173B7A",
            "Bottom": "#42BFD3"
        }
    )

    fig.update_traces(
        textposition="outside",
        marker_line_width=0,
        hovertemplate="<b>%{y}</b><br>Kontribusi: %{x:.3f}%<extra></extra>",
        textfont=dict(color="#000000", size=12, family="Poppins")
    )

    fig.update_layout(
        paper_bgcolor="#DDECFB",
        plot_bgcolor="#DDECFB",
        font=dict(color="#000000", family="Poppins", size=13),
        height=470,
        showlegend=False,
        margin=dict(l=95, r=80, t=20, b=55),
        xaxis=dict(
            title="Persentase (%)",
            title_font=dict(color="#000000", size=14),
            tickfont=dict(color="#000000", size=12),
            gridcolor="#C7D7EA",
            zeroline=False
        ),
        yaxis=dict(
            title="Nama Obat",
            title_font=dict(color="#000000", size=14),
            tickfont=dict(color="#000000", size=12)
        )
    )

    st.plotly_chart(fig, use_container_width=True, config={"displayModeBar": False})

    top_medicine_percent = medicine_sales_percent.iloc[0]
    low_medicine_percent = medicine_sales_percent.iloc[-1]

    st.markdown(f"""
    <div class="insight-box">
        <div class="insight-icon">💡</div>
        <div class="insight-text">
            <b>Insight:</b><br>
            <b>{top_medicine_percent["medicine"]}</b> memiliki kontribusi penjualan tertinggi sebesar 
            <b>{top_medicine_percent["percentage"]:.3f}%</b> dari total unit sold, sementara 
            <b>{low_medicine_percent["medicine"]}</b> memiliki kontribusi terendah sebesar 
            <b>{low_medicine_percent["percentage"]:.3f}%</b>.
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)

# =====================================
# CHART 2: POLA MUSIMAN DI SEBELAH VOLUME
# =====================================
with col6:
    # st.markdown('<div class="chart-box">', unsafe_allow_html=True)
    st.markdown("<div style='margin-top:35px;'></div>", unsafe_allow_html=True)

    st.markdown("""
    <div class="chart-title">Pola Musiman Permintaan Obat</div>
    <div class="chart-subtitle">Persentase rata-rata unit sold berdasarkan bulan</div>
    """, unsafe_allow_html=True)

    month_map = {
        1: "Jan", 2: "Feb", 3: "Mar", 4: "Apr",
        5: "Mei", 6: "Jun", 7: "Jul", 8: "Agu",
        9: "Sep", 10: "Okt", 11: "Nov", 12: "Des"
    }

    seasonal = (
        filtered_df.groupby("month", as_index=False)["units_sold"]
        .mean()
        .sort_values("month")
    )

    seasonal["month_name"] = seasonal["month"].map(month_map)

    total_avg = seasonal["units_sold"].sum()
    seasonal["percentage"] = seasonal["units_sold"] / total_avg * 100

    max_month = seasonal.loc[seasonal["percentage"].idxmax()]
    min_month = seasonal.loc[seasonal["percentage"].idxmin()]

    fig = px.line(
        seasonal,
        x="month_name",
        y="percentage",
        markers=True,
        text="percentage"
    )

    fig.update_traces(
        line_color="#1D4ED8",
        line_width=3,
        marker=dict(size=8, color="#1D4ED8"),
        texttemplate="%{text:.3f}",
        textposition="top center",
        textfont=dict(size=11, color="#000000"),
        hovertemplate="<b>%{x}</b><br>Persentase: %{y:.3f}%<extra></extra>"
    )

    fig.add_scatter(
        x=[max_month["month_name"]],
        y=[max_month["percentage"]],
        mode="markers+text",
        marker=dict(size=15, color="#16A34A"),
        textposition="top center",
        textfont=dict(size=11, color="#000000"),
        name="Tertinggi"
    )

    fig.add_scatter(
        x=[min_month["month_name"]],
        y=[min_month["percentage"]],
        mode="markers+text",
        marker=dict(size=15, color="#EF4444"),
        textposition="bottom center",
        textfont=dict(size=11, color="#000000"),
        name="Terendah"
    )

    fig.update_layout(
        paper_bgcolor="#DDECFB",
        plot_bgcolor="#DDECFB",
        font=dict(color="#000000", family="Poppins", size=12),
        height=470,
        margin=dict(l=55, r=35, t=20, b=55),
        xaxis=dict(
            title="Bulan",
            title_font=dict(color="#000000", size=13),
            tickfont=dict(color="#000000", size=11),
            gridcolor="#C7D7EA",
            zeroline=False
        ),
        yaxis=dict(
            title="Persentase (%)",
            title_font=dict(color="#000000", size=13),
            tickfont=dict(color="#000000", size=11),
            gridcolor="#C7D7EA",
            zeroline=False,
            range=[
                seasonal["percentage"].min() - 1,
                seasonal["percentage"].max() + 1.8
            ]
        ),
        legend_title_text="Keterangan",
        legend=dict(font=dict(color="#000000", size=11))
    )

    st.plotly_chart(fig, use_container_width=True, config={"displayModeBar": False})

    st.markdown(f"""
    <div class="insight-box">
        <div class="insight-icon">💡</div>
        <div class="insight-text">
            <b>Insight:</b><br>
            Permintaan tertinggi terjadi pada bulan <b>{max_month["month_name"]}</b> sebesar 
            <b>{max_month["percentage"]:.3f}%</b>, sedangkan permintaan terendah terjadi pada bulan 
            <b>{min_month["month_name"]}</b> sebesar <b>{min_month["percentage"]:.3f}%</b>.
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)

# =====================================
# ROW 2: TREND PENJUALAN FULL WIDTH
# =====================================
st.markdown("<div style='margin-top:35px;'></div>", unsafe_allow_html=True)

st.markdown("""
<div class="chart-title">Trend Penjualan Obat (%)</div>
<div class="chart-subtitle">Persentase kontribusi penjualan obat per tahun</div>
""", unsafe_allow_html=True)

medicine_options = sorted(filtered_df["medicine"].dropna().unique())

selected_medicine_trend = st.selectbox(
    "Pilih nama obat",
    options=medicine_options,
    index=0,
    key="trend_medicine_selectbox"
)

trend_base = filtered_df.copy()

yearly_total = (
    trend_base.groupby("year", as_index=False)["units_sold"]
    .sum()
    .rename(columns={"units_sold": "total_units"})
)

medicine_yearly = (
    trend_base[trend_base["medicine"] == selected_medicine_trend]
    .groupby("year", as_index=False)["units_sold"]
    .sum()
    .rename(columns={"units_sold": "medicine_units"})
)

trend = yearly_total.merge(medicine_yearly, on="year", how="left")
trend["medicine_units"] = trend["medicine_units"].fillna(0)

trend["percentage"] = (
    trend["medicine_units"] / trend["total_units"] * 100
)

trend = trend.sort_values("year")

max_trend = trend.loc[trend["percentage"].idxmax()]
min_trend = trend.loc[trend["percentage"].idxmin()]

earliest = trend.iloc[0]["percentage"]
latest = trend.iloc[-1]["percentage"]
change = latest - earliest

if abs(change) < 0.1:
    trend_status = "stabil ➖"
elif change > 0:
    trend_status = "meningkat 📈"
else:
    trend_status = "menurun 📉"

fig = px.line(
    trend,
    x="year",
    y="percentage",
    markers=True,
    text="percentage"
)

fig.update_traces(
    line_color="#1D4ED8",
    line_width=4,
    marker=dict(size=10, color="#1D4ED8"),
    texttemplate="%{text:.2f}",
    textposition="top center",
    textfont=dict(size=13, color="#000000"),
    hovertemplate="<b>Tahun %{x}</b><br>Persentase: %{y:.2f}%<extra></extra>"
)

fig.add_scatter(
    x=[max_trend["year"]],
    y=[max_trend["percentage"]],
    mode="markers",
    marker=dict(
        size=18,
        color="#FF7F50",
        line=dict(color="white", width=2)
    ),
    name="Nilai Tertinggi"
)

fig.update_layout(
    paper_bgcolor="#DDECFB",
    plot_bgcolor="#DDECFB",
    font=dict(color="#000000", family="Poppins"),
    height=480,
    xaxis_title="Tahun",
    yaxis_title="Persentase (%)",
    xaxis=dict(
        dtick=1,
        gridcolor="#C7D7EA",
        title_font=dict(color="#000000"),
        tickfont=dict(color="#000000")
    ),
    yaxis=dict(
        gridcolor="#C7D7EA",
        title_font=dict(color="#000000"),
        tickfont=dict(color="#000000"),
        range=[0, trend["percentage"].max() + 5],
        tickmode="linear",
        dtick=5
    ),
    legend=dict(
        font=dict(color="#000000")
    )
)

st.plotly_chart(
    fig,
    use_container_width=True,
    config={"displayModeBar": False}
)

st.markdown(f"""
<div class="insight-box">
<div class="insight-icon">💡</div>

<div class="insight-text">

<b>Insight:</b><br>

Kontribusi penjualan <b>{selected_medicine_trend}</b> menunjukkan tren 
<b>{trend_status}</b> selama periode 2020–2025. 
Kontribusi awal sebesar <b>{earliest:.2f}%</b> dan kontribusi akhir sebesar 
<b>{latest:.2f}%</b>.<br>

Nilai tertinggi terjadi pada tahun <b>{int(max_trend["year"])}</b> sebesar 
<b>{max_trend["percentage"]:.2f}%</b>. 
Nilai terendah terjadi pada tahun <b>{int(min_trend["year"])}</b> sebesar 
<b>{min_trend["percentage"]:.2f}%</b>.

</div>
</div>
""", unsafe_allow_html=True)
# =====================================
# ROW COUNTRY & REGION
# =====================================
col_country, col_region = st.columns(2)

# =====================================
# COUNTRY
# =====================================
with col_country:
    st.markdown("<div style='margin-top:35px;'></div>", unsafe_allow_html=True)

    st.markdown("""
    <div class="chart-title">Rata-rata Permintaan Obat per Country</div>
    <div class="chart-subtitle">
    Persentase kontribusi rata-rata permintaan obat berdasarkan negara
    </div>
    """, unsafe_allow_html=True)

    country_demand_all = (
        filtered_df.groupby("country", as_index=False)["units_sold"]
        .mean()
        .sort_values("units_sold", ascending=False)
    )

    total_country_mean = country_demand_all["units_sold"].sum()

    country_demand_all["percentage"] = (
        country_demand_all["units_sold"] / total_country_mean * 100
    )

    country_demand = country_demand_all.head(10).copy()

    country_demand["label"] = country_demand["percentage"].map(
        lambda x: f"{x:.2f}%"
    )

    fig = px.bar(
        country_demand.sort_values("percentage", ascending=True),
        x="percentage",
        y="country",
        orientation="h",
        text="label",
        color="percentage",
        color_continuous_scale=["#8FD3E8", "#1E1C3E"]
    )

    fig.update_traces(
        textposition="outside",
        marker_line_width=0,
        hovertemplate="<b>%{y}</b><br>Kontribusi: %{x:.2f}%<extra></extra>",
        textfont=dict(color="#000000", size=12, family="Poppins")
    )

    fig.update_layout(
        paper_bgcolor="#DDECFB",
        plot_bgcolor="#DDECFB",
        font=dict(color="#000000", family="Poppins", size=12),
        height=500,
        showlegend=False,
        coloraxis_showscale=False,
        margin=dict(l=95, r=70, t=20, b=50),
        xaxis=dict(
            title="Persentase (%)",
            gridcolor="#C7D7EA",
            title_font=dict(color="#000000"),
            tickfont=dict(color="#000000"),
            range=[0, country_demand["percentage"].max() + 1]
        ),
        yaxis=dict(
            title="Country",
            title_font=dict(color="#000000"),
            tickfont=dict(color="#000000")
        )
    )

    st.plotly_chart(
        fig,
        use_container_width=True,
        config={"displayModeBar": False}
    )

    top_country = country_demand_all.iloc[0]

    st.markdown(f"""
    <div class="insight-box">
        <div class="insight-icon">💡</div>
        <div class="insight-text">
            <b>Insight:</b><br>
            Country dengan kontribusi permintaan tertinggi adalah 
            <b>{top_country["country"]}</b> sebesar 
            <b>{top_country["percentage"]:.2f}%</b>.
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)


# =====================================
# REGION
# =====================================
with col_region:
    st.markdown("<div style='margin-top:35px;'></div>", unsafe_allow_html=True)

    st.markdown("""
    <div class="chart-title">Distribusi Permintaan Obat di Setiap Region</div>
    <div class="chart-subtitle">
    Proporsi total unit sold berdasarkan region
    </div>
    """, unsafe_allow_html=True)

    region_sales = (
        filtered_df.groupby("region", as_index=False)["units_sold"]
        .sum()
        .sort_values("units_sold", ascending=False)
    )

    region_sales["percentage"] = (
        region_sales["units_sold"] / region_sales["units_sold"].sum() * 100
    )

    region_sales["label"] = region_sales.apply(
        lambda row: f"{row['region']}<br>{row['percentage']:.2f}%",
        axis=1
    )

    fig = go.Figure(
        data=[
            go.Pie(
                labels=region_sales["region"],
                values=region_sales["units_sold"],
                hole=0.45,
                text=region_sales["label"],
                textinfo="text",
                textposition="inside",
                marker=dict(
                    colors=[
                        "#1E3A8A",
                        "#1D4ED8",
                        "#2563EB",
                        "#3B82F6",
                        "#60A5FA",
                        "#93C5FD",
                        "#0F766E",
                        "#38BDF8"
                    ],
                    line=dict(color="#33346B", width=2)
                )
            )
        ]
    )

    fig.update_layout(
        paper_bgcolor="#DDECFB",
        plot_bgcolor="#DDECFB",
        font=dict(color="#000000", family="Poppins"),
        height=500,
        margin=dict(l=20, r=20, t=20, b=20),
        showlegend=True,
        legend=dict(
            font=dict(size=13, color="#1E3A8A")
        )
    )

    st.plotly_chart(
        fig,
        use_container_width=True,
        config={"displayModeBar": False}
    )

    top_region = region_sales.iloc[0]

    st.markdown(f"""
    <div class="insight-box">
        <div class="insight-icon">💡</div>
        <div class="insight-text">
            <b>Insight:</b><br>
            Region dengan kontribusi permintaan tertinggi adalah 
            <b>{top_region["region"]}</b> sebesar 
            <b>{top_region["percentage"]:.2f}%</b>.
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)

# =====================================
# TABLE SECTION
# =====================================
if "show_table" not in st.session_state:
    st.session_state.show_table = False

if st.button("📋 Lihat Tabel Data"):
    st.session_state.show_table = not st.session_state.show_table

if st.session_state.show_table:

    st.markdown("### 📋 Data Hasil Filter")

    st.dataframe(
        filtered_df,
        use_container_width=True,
        height=300
    )

    st.download_button(
        "⬇ Download CSV",
        data=filtered_df.to_csv(index=False),
        file_name="filtered_pharmasix_data.csv",
        mime="text/csv"
    )

    st.markdown("<br><br>", unsafe_allow_html=True)