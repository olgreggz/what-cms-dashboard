"""Somnething"""

import plotly.graph_objects as go


def make_sankey(df, labels):
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
                        "cms_2021_idx"
                    ],  # indices correspond to labels, eg A1, A2, A1, B1, ...
                    target=list(df["cms_now_idx"]),
                    value=list(df["count"]),
                ),
            )
        ]
    )

    fig.update_layout(title_text="Basic Sankey Diagram", font_size=10)
    return fig
