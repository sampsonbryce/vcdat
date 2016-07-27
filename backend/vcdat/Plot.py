import vcs, cdms2, os, tempfile

def vcs_plot(variables, graphics_method_parent, graphics_method, template, width, height):
    print 'plotting', variables, graphics_method_parent, graphics_method, template, width, height
    f = cdms2.open(variables[0]['path'])
    v = f(variables[0]['cdms_var_name'])
    c = vcs.init()
    gm = vcs.creategraphicsmethod(graphics_method_parent, graphics_method)
    c.plot(v, template, gm)
    image_path = tempfile.mkstemp(suffix='.png')[1]
    c.png(image_path, width, height)
    c.close()
    return image_path
