from motion_detector import data_frame
from bokeh.plotting import figure, show, output_file

p= figure(x_axis_type='datetime',height=500, width=500, title="Motion Graph")
q=p.quad(left=data_frame["Start"], right=data_frame["End"], bottom=0, top=1, color="green")
output_file("Graph.html")
show(p)