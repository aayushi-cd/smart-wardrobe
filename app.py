import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from pathlib import Path

# ============================================================
# PAGE CONFIG
# ============================================================

st.set_page_config(
    page_title="Closetra",
    page_icon="✦",
    layout="wide",
    initial_sidebar_state="expanded"
)

DATA = Path(__file__).with_name("wardrobe.csv")


@st.cache_data
def load_data():
    return pd.read_csv(DATA)


def save_data(data):
    data.to_csv(DATA, index=False)
    load_data.clear()


DF = load_data()


# ============================================================
# PREMIUM UI
# ============================================================

st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Playfair+Display:wght@600;700&display=swap');

:root {
    --purple: #7357ff;
    --purple2: #9b6dff;
    --pink: #e96fae;
    --ink: #211c32;
    --muted: #777185;
    --surface: rgba(255,255,255,.88);
}

html, body, [class*="css"] {
    font-family: 'DM Sans', sans-serif;
}

.stApp {
    background:
        radial-gradient(circle at 5% 0%, rgba(139,110,255,.13), transparent 28%),
        radial-gradient(circle at 95% 15%, rgba(235,111,174,.12), transparent 26%),
        linear-gradient(135deg,#f8f7ff,#fffafd 48%,#f5fbff);
}

.block-container {
    max-width: 1400px;
    padding-top: 1.4rem;
    padding-bottom: 4rem;
}

/* SIDEBAR */

[data-testid="stSidebar"] {
    background: rgba(255,255,255,.92);
    border-right: 1px solid rgba(115,87,255,.10);
}

[data-testid="stSidebar"] [data-testid="stMarkdownContainer"] p {
    color: #716b7e;
}

.brand {
    padding: 8px 4px 20px 4px;
}

.brand-name {
    font-family: 'Playfair Display', serif;
    font-size: 2rem;
    font-weight: 700;
    color: #2a223c;
    letter-spacing: -.5px;
}

.brand-dot {
    color: #8c68ff;
}

.brand-sub {
    color: #8a8495;
    font-size: .76rem;
    letter-spacing: 1.5px;
    text-transform: uppercase;
    margin-top: 3px;
}

.phase {
    background: linear-gradient(135deg,#f0ecff,#fff1f8);
    border: 1px solid #e8e0ff;
    padding: 14px;
    border-radius: 15px;
    color: #61577b;
    font-size: .82rem;
    margin-top: 15px;
}

/* HERO */

.hero {
    position: relative;
    overflow: hidden;
    padding: 34px 36px;
    border-radius: 26px;
    background:
        radial-gradient(circle at 85% 25%, rgba(255,255,255,.22), transparent 20%),
        linear-gradient(120deg,#6755ef,#9664f3 55%,#df6dac);
    color: white;
    box-shadow: 0 22px 55px rgba(100,75,210,.23);
    margin-bottom: 24px;
}

.hero:after {
    content: "✦";
    position: absolute;
    right: 45px;
    top: 6px;
    font-size: 8rem;
    opacity: .08;
}

.hero-eyebrow {
    font-size: .76rem;
    letter-spacing: 2px;
    text-transform: uppercase;
    opacity: .82;
    margin-bottom: 8px;
}

.hero h1 {
    font-family: 'Playfair Display', serif;
    color: white;
    font-size: 2.7rem;
    margin: 0;
    line-height: 1.05;
}

.hero p {
    margin: 10px 0 0 0;
    opacity: .9;
    max-width: 700px;
    font-size: 1rem;
}

/* KPI CARDS */

.kpi {
    background: var(--surface);
    border: 1px solid rgba(115,87,255,.10);
    border-radius: 20px;
    padding: 19px 20px;
    box-shadow: 0 10px 30px rgba(48,37,85,.06);
    min-height: 128px;
    transition: transform .2s ease, box-shadow .2s ease;
}

.kpi:hover {
    transform: translateY(-4px);
    box-shadow: 0 16px 36px rgba(48,37,85,.11);
}

.kpi-icon {
    font-size: 1.35rem;
    margin-bottom: 9px;
}

.kpi-value {
    font-size: 1.65rem;
    font-weight: 700;
    color: #292238;
}

.kpi-label {
    font-size: .78rem;
    color: #8b8596;
    text-transform: uppercase;
    letter-spacing: .7px;
}

.kpi-note {
    margin-top: 4px;
    font-size: .78rem;
    color: #7b6fd0;
}

/* SECTION */

.section-label {
    color: #8a8495;
    font-size: .73rem;
    font-weight: 700;
    letter-spacing: 1.7px;
    text-transform: uppercase;
    margin-top: 28px;
    margin-bottom: 3px;
}

.section-title {
    font-family: 'Playfair Display', serif;
    color: #292238;
    font-size: 1.65rem;
    margin-bottom: 15px;
}

/* CLOTHING CARD */

.item-card {
    background: rgba(255,255,255,.94);
    border: 1px solid rgba(115,87,255,.10);
    border-radius: 20px;
    padding: 19px;
    min-height: 185px;
    box-shadow: 0 9px 28px rgba(43,32,78,.055);
    transition: .2s ease;
}

.item-card:hover {
    transform: translateY(-4px);
    box-shadow: 0 15px 35px rgba(43,32,78,.10);
    border-color: rgba(115,87,255,.22);
}

.item-icon {
    width: 52px;
    height: 52px;
    display: flex;
    align-items: center;
    justify-content: center;
    border-radius: 16px;
    background: linear-gradient(135deg,#f1edff,#fff0f7);
    font-size: 1.75rem;
    margin-bottom: 13px;
}

.item-title {
    color: #2a2436;
    font-size: 1rem;
    font-weight: 700;
}

.muted {
    color: #8a8495;
    font-size: .82rem;
}

.tag {
    display: inline-block;
    background: #f2efff;
    color: #6f5bd2;
    padding: 4px 9px;
    border-radius: 999px;
    font-size: .72rem;
    margin: 8px 3px 7px 0;
}

/* INSIGHT CARD */

.insight {
    background: rgba(255,255,255,.92);
    border: 1px solid rgba(115,87,255,.10);
    border-radius: 18px;
    padding: 18px;
    min-height: 115px;
    box-shadow: 0 8px 25px rgba(43,32,78,.05);
}

.insight-icon {
    font-size: 1.5rem;
}

.insight-title {
    font-weight: 700;
    color: #302942;
    margin-top: 7px;
}

.insight-text {
    color: #827c8e;
    font-size: .82rem;
    margin-top: 3px;
}

/* OUTFIT */

.outfit-card {
    background: rgba(255,255,255,.95);
    border: 1px solid rgba(115,87,255,.12);
    border-radius: 23px;
    padding: 27px 18px;
    text-align: center;
    min-height: 230px;
    box-shadow: 0 12px 32px rgba(43,32,78,.07);
}

.outfit-icon {
    width: 80px;
    height: 80px;
    border-radius: 25px;
    background: linear-gradient(135deg,#eeeaff,#fff0f7);
    margin: 0 auto 15px auto;
    display:flex;
    align-items:center;
    justify-content:center;
    font-size:2.8rem;
}

.outfit-type {
    color: #9b94a6;
    font-size: .69rem;
    letter-spacing: 1.5px;
    font-weight: 700;
}

.outfit-title {
    color:#2a2436;
    font-weight:700;
    font-size:1.08rem;
    margin:5px 0;
}

.match {
    margin-top: 20px;
    border-radius: 21px;
    padding: 21px;
    background: linear-gradient(110deg,#6755ef,#9c63ef,#df6dac);
    color: white;
    text-align:center;
    box-shadow:0 15px 35px rgba(110,75,210,.2);
}

.match-number {
    font-size:2rem;
    font-weight:700;
}

.match-small {
    opacity:.86;
    font-size:.83rem;
}

/* WHY CARD */

.why {
    background: rgba(255,255,255,.9);
    border-left: 4px solid #8465f5;
    border-radius: 15px;
    padding: 17px 20px;
    color:#655e70;
    margin-top:15px;
}

/* BUTTONS */

.stButton > button,
.stFormSubmitButton > button {
    min-height: 46px;
    border: none;
    border-radius: 13px;
    font-weight: 700;
    box-shadow: 0 8px 20px rgba(100,75,210,.10);
}

/* INPUTS */

div[data-baseweb="select"] > div,
div[data-baseweb="input"] > div {
    border-radius: 12px;
}

/* PLOTLY */

.js-plotly-plot {
    border-radius: 20px;
    overflow: hidden;
}

</style>
""", unsafe_allow_html=True)


# ============================================================
# HELPERS
# ============================================================

icons = {
    "Top": "👕",
    "Bottom": "👖",
    "Dress": "👗",
    "Outerwear": "🧥",
    "Footwear": "👟"
}


def hero(title, subtitle, eyebrow="CLOSETRA · DIGITAL CLOSET"):
    st.markdown(
        '<div class="hero">'
        f'<div class="hero-eyebrow">{eyebrow}</div>'
        f'<h1>{title}</h1>'
        f'<p>{subtitle}</p>'
        '</div>',
        unsafe_allow_html=True
    )


def section(label, title):
    st.markdown(
        f'<div class="section-label">{label}</div>'
        f'<div class="section-title">{title}</div>',
        unsafe_allow_html=True
    )


def kpi(icon, value, label, note):
    return (
        '<div class="kpi">'
        f'<div class="kpi-icon">{icon}</div>'
        f'<div class="kpi-value">{value}</div>'
        f'<div class="kpi-label">{label}</div>'
        f'<div class="kpi-note">{note}</div>'
        '</div>'
    )


def item_card(row):
    icon = icons.get(row["category"], "👚")

    return (
        '<div class="item-card">'
        f'<div class="item-icon">{icon}</div>'
        f'<div class="item-title">{row["item_name"]}</div>'
        f'<div class="muted">{row["color"]} · {row["category"]}</div>'
        f'<span class="tag">{row["occasion"]}</span>'
        f'<span class="tag">{row["style"]}</span>'
        f'<div class="muted">↻ Worn {row["times_worn"]} times</div>'
        '</div>'
    )


def insight_card(icon, title, text):
    return (
        '<div class="insight">'
        f'<div class="insight-icon">{icon}</div>'
        f'<div class="insight-title">{title}</div>'
        f'<div class="insight-text">{text}</div>'
        '</div>'
    )


# ============================================================
# SIDEBAR
# ============================================================

st.sidebar.markdown(
    '<div class="brand">'
    '<div class="brand-name">Closetra<span class="brand-dot">.</span></div>'
    '<div class="brand-sub">Intelligent Wardrobe</div>'
    '</div>',
    unsafe_allow_html=True
)

page = st.sidebar.radio(
    "Explore",
    [
        "🏠 Dashboard",
        "👗 My Wardrobe",
        "✦ Outfit Stylist",
        "📊 Closet Insights",
        "＋ Add Item"
    ]
)

st.sidebar.markdown(
    '<div class="phase">'
    '<b>✦ Phase 01 Prototype</b><br>'
    'Core wardrobe intelligence is live.<br><br>'
    '● Dashboard<br>'
    '● Digital closet<br>'
    '● Smart styling<br>'
    '● Usage insights'
    '</div>',
    unsafe_allow_html=True
)


# ============================================================
# DASHBOARD
# ============================================================

if page == "🏠 Dashboard":

    hero(
        "Your wardrobe, intelligently styled.",
        "Closetra turns your digital closet into useful insights and context-aware outfit recommendations."
    )

    most_worn = DF.loc[DF.times_worn.idxmax(), "item_name"]
    utilization = int(DF.times_worn.gt(5).mean() * 100)
    underused = int((DF.times_worn <= 5).sum())

    cols = st.columns(4)

    cols[0].markdown(
        kpi("◈", len(DF), "Total Pieces", "Your digital closet"),
        unsafe_allow_html=True
    )

    cols[1].markdown(
        kpi("▦", DF.category.nunique(), "Categories", "Closet organized"),
        unsafe_allow_html=True
    )

    cols[2].markdown(
        kpi("♛", most_worn, "Top Wear", f"{DF.times_worn.max()} total wears"),
        unsafe_allow_html=True
    )

    cols[3].markdown(
        kpi("◎", f"{utilization}%", "Utilization", "Healthy closet usage"),
        unsafe_allow_html=True
    )

    section(
        "CLOSET ANALYTICS",
        "Wardrobe at a glance"
    )

    left, right = st.columns([1, 1.2])

    cats = (
        DF.category
        .value_counts()
        .rename_axis("Category")
        .reset_index(name="Items")
    )

    fig1 = px.pie(
        cats,
        names="Category",
        values="Items",
        hole=.67,
        color_discrete_sequence=[
            "#7257f2",
            "#9a6df0",
            "#dc6daa",
            "#6e9fe8",
            "#a8a0e9"
        ]
    )

    fig1.update_traces(
        textposition="inside",
        textinfo="percent"
    )

    fig1.update_layout(
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        margin=dict(l=15, r=15, t=20, b=15),
        legend_title_text="",
        height=380,
        font=dict(family="DM Sans")
    )

    left.plotly_chart(
        fig1,
        use_container_width=True
    )

    top = (
        DF.nlargest(7, "times_worn")
        .sort_values("times_worn")
    )

    fig2 = px.bar(
        top,
        x="times_worn",
        y="item_name",
        orientation="h",
        text="times_worn",
        labels={
            "times_worn": "Times worn",
            "item_name": ""
        },
        color="times_worn",
        color_continuous_scale=[
            "#ddd7ff",
            "#7558ee",
            "#d966a7"
        ]
    )

    fig2.update_traces(
        textposition="outside",
        marker_line_width=0
    )

    fig2.update_layout(
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        coloraxis_showscale=False,
        margin=dict(l=10, r=30, t=20, b=10),
        height=380,
        xaxis=dict(showgrid=False),
        yaxis=dict(showgrid=False),
        font=dict(family="DM Sans")
    )

    right.plotly_chart(
        fig2,
        use_container_width=True
    )

    section(
        "CLOSET INTELLIGENCE",
        "What Closetra noticed"
    )

    i1, i2, i3 = st.columns(3)

    favourite_color = DF.color.value_counts().idxmax()
    favourite_style = DF["style"].value_counts().idxmax()

    i1.markdown(
        insight_card(
            "♻️",
            f"{underused} pieces need more love",
            "Closetra can prioritize under-used pieces in future outfit suggestions."
        ),
        unsafe_allow_html=True
    )

    i2.markdown(
        insight_card(
            "🎨",
            f"{favourite_color} leads your closet",
            "This is currently the most represented color in your wardrobe."
        ),
        unsafe_allow_html=True
    )

    i3.markdown(
        insight_card(
            "✦",
            f"{favourite_style} is your top style",
            "Your wardrobe composition suggests this as your dominant aesthetic."
        ),
        unsafe_allow_html=True
    )

    section(
        "MOST WORN",
        "Your closet favourites"
    )

    cards = st.columns(4)

    for i, (_, row) in enumerate(
        DF.nlargest(4, "times_worn").iterrows()
    ):
        cards[i].markdown(
            item_card(row),
            unsafe_allow_html=True
        )


# ============================================================
# MY WARDROBE
# ============================================================

elif page == "👗 My Wardrobe":

    hero(
        "Your digital closet.",
        "Search, filter and explore everything you already own.",
        "CLOSETRA · WARDROBE"
    )

    a, b, c, d = st.columns(4)

    search = a.text_input(
        "Search wardrobe",
        placeholder="Try 'jeans'..."
    )

    category = b.selectbox(
        "Category",
        ["All"] + sorted(DF.category.unique())
    )

    color = c.selectbox(
        "Color",
        ["All"] + sorted(DF.color.unique())
    )

    occasion = d.selectbox(
        "Occasion",
        ["All"] + sorted(DF.occasion.unique())
    )

    filtered = DF.copy()

    if search:
        filtered = filtered[
            filtered.item_name.str.contains(
                search,
                case=False,
                na=False
            )
        ]

    if category != "All":
        filtered = filtered[
            filtered.category == category
        ]

    if color != "All":
        filtered = filtered[
            filtered.color == color
        ]

    if occasion != "All":
        filtered = filtered[
            filtered.occasion == occasion
        ]

    section(
        f"{len(filtered)} PIECES FOUND",
        "Your collection"
    )

    rows = list(filtered.iterrows())

    if not rows:
        st.info("No pieces match your current filters.")

    for start in range(0, len(rows), 4):

        cols = st.columns(4)

        for j, (_, row) in enumerate(
            rows[start:start + 4]
        ):
            cols[j].markdown(
                item_card(row),
                unsafe_allow_html=True
            )


# ============================================================
# OUTFIT STYLIST
# ============================================================

elif page == "✦ Outfit Stylist":

    hero(
        "Meet your digital stylist.",
        "Tell Closetra where you're going and the look you want. We'll build an outfit from pieces you already own.",
        "CLOSETRA · SMART STYLING"
    )

    section(
        "01 · SET THE MOOD",
        "What are we dressing for?"
    )

    a, b, c = st.columns(3)

    occasion = a.selectbox(
        "Occasion",
        sorted(DF.occasion.unique())
    )

    season = b.selectbox(
        "Weather / Season",
        ["Summer", "Winter", "All Season"]
    )

    style = c.selectbox(
        "Style direction",
        ["Any"] + sorted(DF["style"].unique())
    )

    if st.button(
        "✦ STYLE MY LOOK",
        use_container_width=True,
        type="primary"
    ):

        pool = DF[
            (DF.occasion == occasion)
            &
            (
                (DF.season == season)
                |
                (DF.season == "All Season")
            )
        ].copy()

        if style != "Any":

            styled = pool[
                pool["style"] == style
            ]

            if not styled.empty:
                pool = styled


        def pick(cat):

            x = pool[
                pool.category == cat
            ]

            if x.empty:
                x = DF[
                    (DF.category == cat)
                    &
                    (
                        (DF.occasion == occasion)
                        |
                        (DF.occasion == "Casual")
                    )
                ]

            if x.empty:
                return None

            return x.sort_values(
                "times_worn",
                ascending=False
            ).iloc[0]


        if (
            occasion == "Party"
            and
            not pool[
                pool.category == "Dress"
            ].empty
        ):
            chosen = [
                pick("Dress"),
                pick("Footwear")
            ]

        else:
            chosen = [
                pick("Top"),
                pick("Bottom"),
                pick("Footwear")
            ]

        chosen = [
            x for x in chosen
            if x is not None
        ]

        if not chosen:

            st.warning(
                "Closetra couldn't find enough matching pieces."
            )

        else:

            section(
                "02 · YOUR LOOK",
                "Closetra's recommendation"
            )

            cols = st.columns(
                len(chosen)
            )

            for col, row in zip(
                cols,
                chosen
            ):

                icon = icons.get(
                    row["category"],
                    "👚"
                )

                html = (
                    '<div class="outfit-card">'
                    f'<div class="outfit-icon">{icon}</div>'
                    f'<div class="outfit-type">{row["category"].upper()}</div>'
                    f'<div class="outfit-title">{row["item_name"]}</div>'
                    f'<div class="muted">{row["color"]} · {row["style"]}</div>'
                    f'<span class="tag">{row["season"]}</span>'
                    '</div>'
                )

                col.markdown(
                    html,
                    unsafe_allow_html=True
                )

            score = min(
                97,
                80
                + len(chosen) * 4
                + (5 if style != "Any" else 0)
            )

            st.markdown(
                '<div class="match">'
                f'<div class="match-number">{score}% MATCH</div>'
                '<div class="match-small">'
                f'Optimized for {occasion.lower()} · {season.lower()} · '
                f'{"adaptive style" if style == "Any" else style.lower()}'
                '</div>'
                '</div>',
                unsafe_allow_html=True
            )

            st.markdown(
                '<div class="why">'
                '<b>✦ Why this look?</b><br>'
                f'This combination matches your <b>{occasion.lower()}</b> context '
                f'and <b>{season.lower()}</b> conditions. '
                'Closetra also considers how often pieces are used so your '
                'existing wardrobe can work harder for you.'
                '</div>',
                unsafe_allow_html=True
            )

            st.caption(
                "Phase 1 uses transparent rule-based recommendations. "
                "Future phases can introduce learned personalization."
            )


# ============================================================
# INSIGHTS
# ============================================================

elif page == "📊 Closet Insights":

    hero(
        "Know your closet better.",
        "Closetra transforms wardrobe activity into simple, useful visual insights.",
        "CLOSETRA · INTELLIGENCE"
    )

    total_wears = int(DF.times_worn.sum())
    avg_wears = round(DF.times_worn.mean(), 1)
    low_count = int((DF.times_worn <= 5).sum())

    a, b, c = st.columns(3)

    a.markdown(
        kpi("↻", total_wears, "Recorded Wears", "Across your wardrobe"),
        unsafe_allow_html=True
    )

    b.markdown(
        kpi("◎", avg_wears, "Average Wears", "Per clothing item"),
        unsafe_allow_html=True
    )

    c.markdown(
        kpi("◇", low_count, "Under-used Pieces", "Opportunity to re-style"),
        unsafe_allow_html=True
    )

    section(
        "VISUAL PROFILE",
        "Your wardrobe DNA"
    )

    left, right = st.columns(2)

    colors = (
        DF.color.value_counts()
        .rename_axis("Color")
        .reset_index(name="Items")
    )

    color_fig = px.bar(
        colors,
        x="Color",
        y="Items",
        color="Items",
        color_continuous_scale=[
            "#ddd7ff",
            "#7759ef",
            "#dd69aa"
        ]
    )

    color_fig.update_layout(
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        coloraxis_showscale=False,
        xaxis=dict(showgrid=False),
        yaxis=dict(showgrid=False),
        height=370
    )

    left.plotly_chart(
        color_fig,
        use_container_width=True
    )

    styles = (
        DF["style"].value_counts()
        .rename_axis("Style")
        .reset_index(name="Items")
    )

    style_fig = px.pie(
        styles,
        names="Style",
        values="Items",
        hole=.63,
        color_discrete_sequence=[
            "#7257f2",
            "#a36cec",
            "#dc6eac",
            "#6e9ee8",
            "#aaa3e9"
        ]
    )

    style_fig.update_layout(
        paper_bgcolor="rgba(0,0,0,0)",
        margin=dict(l=10, r=10, t=20, b=10),
        height=370
    )

    right.plotly_chart(
        style_fig,
        use_container_width=True
    )

    section(
        "OPPORTUNITY",
        "Pieces that deserve another wear"
    )

    low = DF.nsmallest(
        6,
        "times_worn"
    )[
        [
            "item_name",
            "category",
            "color",
            "style",
            "times_worn"
        ]
    ]

    st.dataframe(
        low,
        use_container_width=True,
        hide_index=True
    )

    st.info(
        "💡 Smart Closet Tip: Instead of immediately buying something new, "
        "future Closetra recommendations can prioritize these lower-use pieces."
    )


# ============================================================
# ADD ITEM
# ============================================================

elif page == "＋ Add Item":

    hero(
        "Grow your digital closet.",
        "Add a new piece and make it available to Closetra's wardrobe intelligence.",
        "CLOSETRA · WARDROBE"
    )

    section(
        "NEW PIECE",
        "Tell us about your clothing"
    )

    with st.form("add_item"):

        name = st.text_input(
            "Item name",
            placeholder="e.g. Navy Overshirt"
        )

        a, b = st.columns(2)

        category = a.selectbox(
            "Category",
            [
                "Top",
                "Bottom",
                "Dress",
                "Outerwear",
                "Footwear"
            ]
        )

        color = b.text_input(
            "Color",
            placeholder="e.g. Navy"
        )

        c, d = st.columns(2)

        season = c.selectbox(
            "Season",
            [
                "Summer",
                "Winter",
                "All Season"
            ]
        )

        occasion = d.selectbox(
            "Occasion",
            [
                "Casual",
                "Formal",
                "Party"
            ]
        )

        style = st.selectbox(
            "Style",
            [
                "Minimal",
                "Streetwear",
                "Classic",
                "Elegant",
                "Feminine"
            ]
        )

        submitted = st.form_submit_button(
            "＋ ADD TO CLOSETRA",
            use_container_width=True,
            type="primary"
        )

    if submitted:

        if not name.strip() or not color.strip():

            st.error(
                "Please enter both an item name and color."
            )

        else:

            new_item = pd.DataFrame([
                {
                    "id": int(DF.id.max()) + 1,
                    "item_name": name.strip(),
                    "category": category,
                    "color": color.strip().title(),
                    "season": season,
                    "occasion": occasion,
                    "style": style,
                    "times_worn": 0
                }
            ])

            updated = pd.concat(
                [DF, new_item],
                ignore_index=True
            )

            save_data(updated)

            st.success(
                f"✦ {name} has been added to your Closetra wardrobe."
            )
