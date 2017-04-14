from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    import src1
    bus_entries = src1.get_bus()
    ubike_entries = src1.get_ubike()
    entries = dict(bus_pt=bus_entries, ubike_pt=ubike_entries)

    return render_template('map1.html', entries=entries)

if __name__ == '__main__':
    app.debug = True
    app.run()
