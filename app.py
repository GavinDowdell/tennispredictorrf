import dash
import utils.layout_callbacks as lc

##################################################################################################################################################################
# we need to set up a basic dash app
app = dash.Dash()
server = app.server
# Now do the actual web page layout
app.layout = lc.create_layout(app)
lc.demo_callbacks(app)

if __name__ == '__main__':
		app.run_server(debug=False)



