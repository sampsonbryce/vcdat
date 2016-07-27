import os
import vcs, cdms2
import json, base64
from flask import Flask, send_from_directory, request
from GraphicsMethods import get_gm
from Templates import get_t
from Files import getFilesObject
from Plot import vcs_plot
app = Flask(__name__, static_url_path='')

_ = vcs.init()

@app.route("/")
def hello():
    path = os.path.abspath(os.path.join(os.path.dirname(os.path.realpath(__file__)), '..', '..', 'frontend/src/'))
    return send_from_directory(path, 'index.html')

@app.route("/deps/<path:path>")
def serve_resource_file(path):
    dir_path = os.path.abspath(os.path.join(os.path.dirname(os.path.realpath(__file__)), '..', '..', 'frontend/'))
    if path in ['Styles.css', 'jquery-2.2.4.min.js', 'jquery-ui.min.js', 'jquery-ui.min.css', 'clt_image.png', 'bootstrap-themed.min.css', 'add_plot.svg']:
        return send_from_directory(dir_path, 'deps/' + path)
    if path in ['Bundle.js', 'Bundle.js.map']:
        return send_from_directory(dir_path, 'dist/' + path)
    else:
        print 'Unable to serve file ', path
        return send_from_directory(dir_path, 'taco')

@app.route("/getTemplates")
def get_templates():
    templates = get_t()
    return json.dumps(templates)

@app.route("/getGraphicsMethods")
def get_graphics_methods():
    graphics_methods = get_gm()
    return graphics_methods


@app.route("/getInitialFileTree")
def get_initial_file_tree():
    start_path = os.path.expanduser('~')
    dir_list = start_path.split('/')
    del dir_list[0]
    dir_list.insert(0, '/')
    print dir_list
    base_files = {}
    total_path = ''
    prev_obj = {}
    for index, directory in enumerate(dir_list):
        total_path += directory
        if index:
            total_path += '/'
        files = getFilesObject(total_path)

        if index:
            prev_obj['sub_items'][directory] = files
        else:
            base_files = files
        prev_obj = files

    print base_files
    return json.dumps(base_files)

@app.route("/browseFiles")
def browse_files():
    start_path = request.args.get('path') + '/'
    file_obj = getFilesObject(start_path)
    return json.dumps(file_obj)

@app.route("/loadVariablesFromFile")
def load_variables_from_file():
    file_path = request.args.get('path')
    f = cdms2.open(file_path);
    return json.dumps({'variables': f.listvariables()})

@app.route('/plot', methods=['POST'])
def plot():
    json_string = request.form.get('plot_data')
    plot_data = json.loads(json_string)
    variables = plot_data['variables']
    graphics_method_parent = str(plot_data['graphics_method_parent'])
    graphics_method = str(plot_data['graphics_method'])
    template = str(plot_data['template'])
    width = int(plot_data['width'])
    height = int(plot_data['height'])
    assert template is not None
    assert variables is not None
    assert graphics_method is not None
    assert graphics_method_parent is not None
    assert width is not None
    assert height is not None

    image_path = vcs_plot(variables, graphics_method_parent, graphics_method, template, width, height)
    with open(image_path, 'rb') as image_file:
            encoded_string = base64.b64encode(image_file.read())
    return encoded_string

if __name__ == "__main__":
    app.run()
