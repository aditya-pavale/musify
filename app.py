import streamlit as st
from singers import singers

# ---------------- PAGE CONFIG (MUST BE FIRST) ----------------
st.set_page_config(
    page_title="Musify",
    page_icon="icon.png"
)

# ---------------- STATE ----------------
if "page" not in st.session_state:
    st.session_state.page = "Home"

if "artist" not in st.session_state:
    st.session_state.artist = None

# ---------------- LOAD CSS ----------------
with open("styles.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# ---------------- NAV GROUP ----------------
st.markdown('<div class="nav-group">', unsafe_allow_html=True)

col1, col2 = st.columns([1, 1], gap="small")

with col1:
    if st.button("Home", key="nav_home"):
        st.session_state.page = "Home"
        st.session_state.artist = None

with col2:
    if st.button("Artists", key="nav_artists"):
        st.session_state.page = "Artists"
        st.session_state.artist = None

st.markdown('</div>', unsafe_allow_html=True)
# ---------------- QUERY PARAM HANDLING ----------------
query_params = st.query_params
if "page" in query_params:
    st.session_state.page = query_params["page"]
    if st.session_state.page == "Artists":
        st.session_state.artist = None

# ---------------- PARALLAX BACKGROUND ----------------
st.markdown(
    """
    <div class="parallax-bg" id="parallax"></div>
    <div class="depth-overlay"></div>

    <script>
    let lastScroll = 0;
    let ticking = false;

    window.addEventListener('scroll', function() {
        lastScroll = window.scrollY;
        if (!ticking) {
            window.requestAnimationFrame(function() {
                const bg = document.getElementById("parallax");
                if (bg) {
                    bg.style.transform =
                        "translateY(" + (lastScroll * 0.08) + "px)";
                }
                ticking = false;
            });
            ticking = true;
        }
    });
    </script>
    """,
    unsafe_allow_html=True
)

# ================= HOME =================
if st.session_state.page == "Home":
    st.markdown(
        """
        <div class="hero">
            <div class="hero-title">MUSIFY</div>
            <div class="hero-sub">
                A calm, immersive showcase of legendary voices
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

# ================= ARTISTS =================
else:
    st.markdown(
        """
        <div class="hero">
            <div class="hero-title">Artists</div>
            <div class="hero-sub">
                Discover legendary voices in a focused space
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    # -------- GRID --------
    if st.session_state.artist is None:
        st.markdown('<div class="grid">', unsafe_allow_html=True)

        for name, data in singers.items():
            if st.button(name, key=name):
                st.session_state.artist = name

            st.markdown(
                f"""
                <div class="artist-card">
                    <img src="{data['image']}">
                    <div class="artist-name">{name}</div>
                </div>
                """,
                unsafe_allow_html=True
            )

        st.markdown('</div>', unsafe_allow_html=True)

    # -------- ARTIST FOCUS VIEW --------
    else:
        artist = st.session_state.artist
        data = singers[artist]

        if st.button("Back to Artists"):
            st.session_state.artist = None

        st.markdown(
            f"""
            <div class="section artist-focus">
                <img src="{data['image']}" width="320" style="border-radius:20px;">
                <h3>{artist}</h3>
                <p>{data['about']}</p>
            </div>
            """,
            unsafe_allow_html=True
        )

        if "song_about" in data:
            st.markdown(
                f"""
                <div class="section glass">
                    <h3>About the Song</h3>
                    <p style="line-height:1.8; opacity:0.85;">
                        {data["song_about"]}
                    </p>
                </div>
                """,
                unsafe_allow_html=True
            )

        st.markdown(
            f"""
            <div class="section glass" style="text-align:center;">
                <a href="{data['song'].replace('/embed/', '/watch?v=')}"
                   target="_blank"
                   style="text-decoration:none;
                          color:#ffd200;
                          font-size:1.1em;
                          font-weight:600;">
                   ▶ Watch on YouTube
                </a>
            </div>
            """,
            unsafe_allow_html=True
        )

# ---------------- FOOTER ----------------
st.markdown(
    '<div class="footer">Musify — Calm, immersive UI music showcase</div>',
    unsafe_allow_html=True
)
