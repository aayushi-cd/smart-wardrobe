import streamlit as st
import pandas as pd
import plotly.express as px
from pathlib import Path


# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="Closetra",
    page_icon="✨",
    layout="wide",
    initial_sidebar_state="expanded"
)

DATA = Path(__file__).with_name("wardrobe.csv")


# ============================================================
# DATA FUNCTIONS
# ============================================================

@st.cache_data
def load_data():
    return pd.read_csv(DATA)


def save_data(data):
    data.to_csv(DATA, index=False)
    load_data.clear()


DF = load_data()


# ============================================================
# CUSTOM DESIGN / CSS
# ============================================================

st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
}

.stApp {
    background: linear-gradient(
        135deg,
        #f7f5ff 0%,
        #fff7fb 48%,
        #f4fbff 100%
    );
}

.block-container {
    padding-top: 1.8rem;
    padding-bottom: 3rem;
}

[data-testid="stSidebar"] {
    background: rgba(255,255,255,.86);
    border-right: 1px solid #ece8f5;
}


/* HERO SECTION */

.hero {
    padding: 28px 30px;
    border-radius: 24px;
    background: linear-gradient(
        120deg,
        #6d5dfc,
        #a34ff0 55%,
        #e65da5
    );
    color: white;
    box-shadow: 0 18px 45px rgba(108,83,220,.22);
    margin-bottom: 20px;
}

.hero h1 {
    font-size: 2.35rem;
    margin: 0 0 6px 0;
    color: white;
}

.hero p {
    margin: 0;
    opacity: .9;
    font-size: 1.02rem;
}


/* METRIC CARDS */

[data-testid="stMetric"] {
    background: rgba(255,255,255,.92);
    border: 1px solid #eeeaf6;
    padding: 18px;
    border-radius: 18px;
    box-shadow: 0 8px 25px rgba(44,35,84,.07);
}


/* CLOTHING CARDS */

.card {
    background: rgba(255,255,255,.94);
    border: 1px solid #eeeaf6;
    border-radius: 18px;
    padding: 18px;
    margin: 7px 0;
    box-shadow: 0 8px 24px rgba(44,35,84,.06);
    min-height: 155px;
}

.card .emoji {
    font-size: 2rem;
}

.muted {
    color: #777187;
    font-size: .9rem;
}

.tag {
    display: inline-block;
    background: #f1edff;
    color: #6653d9;
    padding: 4px 9px;
    border-radius: 999px;
    font-size: .76rem;
    margin: 2px;
}


/* OUTFIT CARDS */

.outfit {
    background: white;
    border: 1px solid #eeeaf6;
    border-radius: 20px;
    padding: 22px;
    text-align: center;
    box-shadow: 0 8px 25px rgba(44,35,84,.07);
    min-height: 190px;
}


/* MATCH SCORE */

.score {
    background: linear-gradient(
        90deg,
        #6d5dfc,
        #d85cab
    );
    color: white;
    padding: 18px 22px;
    border-radius: 18px;
    text-align: center;
    font-size: 1.15rem;
    font-weight: 700;
    margin-top: 18px;
}


/* BUTTONS */

.stButton > button,
.stFormSubmitButton > button {
    border-radius: 12px;
    font-weight: 700;
    min-height: 44px;
    border: 0;
}

</style>
""", unsafe_allow_html=True)


# ============================================================
# CLOTHING ICONS
# ============================================================

emoji = {
    "Top": "👕",
    "Bottom": "👖",
    "Dress": "👗",
    "Outerwear": "🧥",
    "Footwear": "👟"
}


# ============================================================
# REUSABLE COMPONENTS
# ============================================================

def hero(title, subtitle):

    st.markdown(
        f"""
        <div class="hero">
            <h1>{title}</h1>
            <p>{subtitle}</p>
        </div>
        """,
        unsafe_allow_html=True
    )


def item_card(row):

    icon = emoji.get(row["category"], "👚")

    return f"""
    <div class='card'>

        <div class='emoji'>{icon}</div>

        <b>{row['item_name']}</b>

        <br>

        <span class='muted'>
            {row['color']} · {row['category']}
        </span>

        <br><br>

        <span class='tag'>
            {row['occasion']}
        </span>

        <span class='tag'>
            {row['style']}
        </span>

        <br>

        <span class='muted'>
            Worn {row['times_worn']} times
        </span>

    </div>
    """


# ============================================================
# SIDEBAR
# ============================================================

st.sidebar.markdown("## ✨ Closetra")

st.sidebar.caption(
    "YOUR INTELLIGENT WARDROBE"
)

page = st.sidebar.radio(
    "Navigation",
    [
        "🏠 Dashboard",
        "👗 My Wardrobe",
        "✨ Outfit Recommender",
        "📊 Insights",
        "➕ Add Item"
    ]
)

st.sidebar.divider()

st.sidebar.caption(
    "Prototype · Phase 1"
)

st.sidebar.progress(
    65,
    text="Project progress 65%"
)


# ============================================================
# DASHBOARD
# ============================================================

if page == "🏠 Dashboard":

    hero(
        "Closetra",
        "Your intelligent wardrobe & personal styling assistant."
    )

    c1, c2, c3, c4 = st.columns(4)

    c1.metric(
        "Total Items",
        len(DF),
        "Digital wardrobe"
    )

    c2.metric(
        "Categories",
        DF.category.nunique(),
        "Organized"
    )

    c3.metric(
        "Most Worn",
        DF.loc[
            DF.times_worn.idxmax(),
            "item_name"
        ],
        f"{DF.times_worn.max()} wears"
    )

    utilization = int(
        (DF.times_worn.gt(5).mean()) * 100
    )

    c4.metric(
        "Utilization",
        f"{utilization}%",
        "Worn > 5 times"
    )


    # -------------------------
    # CHARTS
    # -------------------------

    st.subheader(
        "Wardrobe at a glance"
    )

    left, right = st.columns(2)

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
        hole=.58
    )

    fig1.update_layout(
        margin=dict(
            l=10,
            r=10,
            t=20,
            b=10
        ),
        legend_title_text=""
    )

    left.plotly_chart(
        fig1,
        use_container_width=True
    )


    top = (
        DF.nlargest(
            8,
            "times_worn"
        )
        .sort_values(
            "times_worn"
        )
    )

    fig2 = px.bar(
        top,
        x="times_worn",
        y="item_name",
        orientation="h",
        labels={
            "times_worn": "Times worn",
            "item_name": ""
        }
    )

    fig2.update_layout(
        margin=dict(
            l=10,
            r=10,
            t=20,
            b=10
        )
    )

    right.plotly_chart(
        fig2,
        use_container_width=True
    )


    # -------------------------
    # MOST USED ITEMS
    # -------------------------

    st.subheader(
        "Most-used pieces"
    )

    cols = st.columns(4)

    for i, (_, row) in enumerate(
        DF.nlargest(
            4,
            "times_worn"
        ).iterrows()
    ):

        cols[i].markdown(
            item_card(row),
            unsafe_allow_html=True
        )


# ============================================================
# MY WARDROBE
# ============================================================

elif page == "👗 My Wardrobe":

    hero(
        "My Wardrobe",
        "Search and explore your digital clothing collection."
    )

    a, b, c, d = st.columns(4)

    search = a.text_input(
        "Search",
        placeholder="e.g. jeans"
    )

    category = b.selectbox(
        "Category",
        ["All"] +
        sorted(
            DF.category.unique().tolist()
        )
    )

    color = c.selectbox(
        "Color",
        ["All"] +
        sorted(
            DF.color.unique().tolist()
        )
    )

    occasion = d.selectbox(
        "Occasion",
        ["All"] +
        sorted(
            DF.occasion.unique().tolist()
        )
    )


    # -------------------------
    # FILTER DATA
    # -------------------------

    f = DF.copy()

    if search:

        f = f[
            f.item_name.str.contains(
                search,
                case=False,
                na=False
            )
        ]

    if category != "All":

        f = f[
            f.category == category
        ]

    if color != "All":

        f = f[
            f.color == color
        ]

    if occasion != "All":

        f = f[
            f.occasion == occasion
        ]


    st.caption(
        f"Showing {len(f)} of {len(DF)} items"
    )


    # -------------------------
    # DISPLAY CLOTHING CARDS
    # -------------------------

    rows = list(
        f.iterrows()
    )

    for start in range(
        0,
        len(rows),
        4
    ):

        cols = st.columns(4)

        for j, (_, row) in enumerate(
            rows[start:start + 4]
        ):

            cols[j].markdown(
                item_card(row),
                unsafe_allow_html=True
            )


# ============================================================
# OUTFIT RECOMMENDER
# ============================================================

elif page == "✨ Outfit Recommender":

    hero(
        "Outfit Recommender",
        "Choose the context and Closetra will assemble a suitable outfit from your wardrobe."
    )

    a, b, c = st.columns(3)

    occasion = a.selectbox(
        "Occasion",
        sorted(
            DF.occasion.unique()
        )
    )

    season = b.selectbox(
        "Season / Weather",
        [
            "Summer",
            "Winter",
            "All Season"
        ]
    )

    style = c.selectbox(
        "Preferred style",
        ["Any"] +
        sorted(
            DF["style"].unique()
        )
    )


    if st.button(
        "✨ Generate my outfit",
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


        # -------------------------
        # STYLE FILTER
        # -------------------------

        if style != "Any":

            styled = pool[
                pool["style"] == style
            ]

            if not styled.empty:

                pool = styled


        # -------------------------
        # ITEM PICKING FUNCTION
        # -------------------------

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

            return (
                x.sort_values(
                    "times_worn",
                    ascending=False
                )
                .iloc[0]
            )


        # -------------------------
        # BUILD OUTFIT
        # -------------------------

        chosen = []

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


        # -------------------------
        # DISPLAY OUTFIT
        # -------------------------

        cols = (
            st.columns(len(chosen))
            if chosen
            else []
        )

        for col, row in zip(
            cols,
            chosen
        ):

            col.markdown(
                f"""
                <div class='outfit'>

                    <div style='font-size:3rem'>
                        {emoji.get(row['category'], '👚')}
                    </div>

                    <h3>
                        {row['item_name']}
                    </h3>

                    <div class='muted'>

                        {row['color']}
                        ·
                        {row['style']}

                        <br>

                        {row['season']}

                    </div>

                </div>
                """,
                unsafe_allow_html=True
            )


        # -------------------------
        # MATCH SCORE
        # -------------------------

        score = min(
            97,
            78
            + len(chosen) * 4
            + (
                5
                if style != "Any"
                else 0
            )
        )

        st.markdown(
            f"""
            <div class='score'>

            🎯 {score}% MATCH

            · Suitable for
            {occasion.lower()} use
            and
            {season.lower()} conditions

            </div>
            """,
            unsafe_allow_html=True
        )


        st.info(
            "Prototype logic: recommendations currently use "
            "occasion, season, style and wardrobe usage. "
            "A later phase can replace this with a learned "
            "personalization model."
        )


# ============================================================
# INSIGHTS
# ============================================================

elif page == "📊 Insights":

    hero(
        "Wardrobe Insights",
        "Understand what you own, what you use and what may be under-utilized."
    )

    a, b = st.columns(2)


    # -------------------------
    # COLOR DISTRIBUTION
    # -------------------------

    colors = (
        DF.color
        .value_counts()
        .rename_axis("Color")
        .reset_index(name="Items")
    )

    color_chart = px.bar(
        colors,
        x="Color",
        y="Items",
        title="Color Distribution"
    )

    a.plotly_chart(
        color_chart,
        use_container_width=True
    )


    # -------------------------
    # STYLE DISTRIBUTION
    # -------------------------

    styles = (
        DF["style"]
        .value_counts()
        .rename_axis("Style")
        .reset_index(name="Items")
    )

    style_chart = px.pie(
        styles,
        names="Style",
        values="Items",
        hole=.5,
        title="Style Mix"
    )

    b.plotly_chart(
        style_chart,
        use_container_width=True
    )


    # -------------------------
    # UNDERUTILIZED CLOTHES
    # -------------------------

    st.subheader(
        "Under-utilized items"
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

    st.caption(
        "💡 Closetra Insight: Items with low wear counts "
        "can be prioritized in future outfit recommendations "
        "instead of purchasing new clothes."
    )


# ============================================================
# ADD ITEM
# ============================================================

elif page == "➕ Add Item":

    hero(
        "Add Clothing Item",
        "Expand your Closetra digital wardrobe by adding a new piece."
    )


    with st.form("add"):

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
            placeholder="Navy"
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
            "Add to wardrobe",
            use_container_width=True,
            type="primary"
        )


    # -------------------------
    # SAVE ITEM
    # -------------------------

    if submitted:

        if (
            not name.strip()
            or
            not color.strip()
        ):

            st.error(
                "Please enter both item name and color."
            )

        else:

            new = pd.DataFrame(
                [
                    {
                        "id": int(
                            DF.id.max()
                        ) + 1,

                        "item_name":
                            name.strip(),

                        "category":
                            category,

                        "color":
                            color.strip().title(),

                        "season":
                            season,

                        "occasion":
                            occasion,

                        "style":
                            style,

                        "times_worn":
                            0
                    }
                ]
            )


            save_data(
                pd.concat(
                    [
                        DF,
                        new
                    ],
                    ignore_index=True
                )
            )


            st.success(
                f"✨ {name} was successfully added to your Closetra wardrobe!"
            )
