import dash
import dash_html_components as html

app = dash.Dash(__name__)

app.layout = html.Div(
    children=[
        html.H1("Welcome to QuizApp"),
        html.P("This is a basic Dash app."),
    ]
)

if __name__ == "__main__":
    app.run_server(debug=True)