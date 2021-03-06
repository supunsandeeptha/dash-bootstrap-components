import dash_bootstrap_components as dbc
import dash_html_components as html

input_group = html.Div(
    [
        dbc.InputGroup(
            [
                dbc.InputGroupAddon("@", addon_type="prepend"),
                dbc.Input(placeholder="username"),
            ]
        ),
        html.Br(),
        dbc.InputGroup(
            [
                dbc.Input(placeholder="username"),
                dbc.InputGroupAddon("@example.com", addon_type="append"),
            ]
        ),
        html.Br(),
        dbc.InputGroup(
            [
                dbc.InputGroupAddon("$", addon_type="prepend"),
                dbc.Input(placeholder="Amount", type="number"),
                dbc.InputGroupAddon(".00", addon_type="append"),
            ]
        ),
    ]
)
