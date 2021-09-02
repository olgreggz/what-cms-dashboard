"""Somnething"""

import plotly.graph_objects as go
import plotly.express as px


def make_sankey(df, labels, mode):
    if mode == "count":
        title = "CMS Competitor Intel by Count"
    elif mode == "revenue":
        title = "CMS Competitor Intel by Revenue"
    else:
        raise ValueError("mode must be one of count, revenue")

    fig = go.Figure(
        data=[
            go.Sankey(
                node=dict(
                    pad=15,
                    thickness=20,
                    line=dict(color="black", width=0.5),
                    label=labels,
                ),
                link=dict(
                    source=df[
                        "cms_2020_idx"
                    ],  # indices correspond to labels, eg A1, A2, A1, B1, ...
                    target=list(df["cms_now_idx"]),
                    value=list(df[mode]),
                ),
            )
        ]
    )

    fig.update_layout(title_text=title, font_size=10)
    return fig


def make_market_share_bar(df, mode):
    if mode == "indy":
        title = "Customers by CMS (Independent Schools)"
        dtick = 50
    elif mode == "public":
        title = "Customers by CMS (Public Schools)"
        dtick = 100
    else:
        return ValueError("mode must be one of indy, public")

    df = df.sort_values("cms_2021_08", ascending=False).rename(
        columns={
            "cms_2020_07": "Jul 2020",
            "cms_2020_11": "Nov 2020",
            "cms_2021_08": "Aug 2021",
        }
    )
    fig = px.bar(
        df,
        x="cms",
        y=["Jul 2020", "Nov 2020", "Aug 2021"],
        barmode="group",
        labels={"cms": "CMS",},
    )
    fig.update_yaxes(dtick=dtick)
    fig.update_layout(
        title_text=title, font_size=10, yaxis_title="Count", legend_title="Date"
    )
    return fig
