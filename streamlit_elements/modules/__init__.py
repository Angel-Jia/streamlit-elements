from streamlit_elements.modules.callbacks import sync, lazy, partial
from streamlit_elements.modules.dashboard import Dashboard
from streamlit_elements.modules.editors import Editors
from streamlit_elements.modules.events import Events
from streamlit_elements.modules.html import HTML
from streamlit_elements.modules.media import Media
from streamlit_elements.modules.mui import MUI
from streamlit_elements.modules.nivo import Nivo
from streamlit_elements.modules.echarts import Echarts
from streamlit_elements.modules.table import CustomTable

__all__ = [
    "dashboard",
    "editor",
    "event",
    "html",
    "lazy",
    "media",
    "mui",
    "nivo",
    "customTable",
    "echarts",
    "partial",
    "sync",
]


dashboard = Dashboard()
editor = Editors()
event = Events()
html = HTML()
media = Media()
mui = MUI()
nivo = Nivo()
echarts = Echarts()
customTable = CustomTable()
