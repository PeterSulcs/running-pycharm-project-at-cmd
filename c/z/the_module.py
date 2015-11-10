from c.z.y.the_module_module import the_module_module_function


def the_module_function():
    print('the_module_function is running!')
    the_module_module_function()
    pass

def the_module_write_function(read_file, write_file):
    with open(read_file, 'r') as fid:
        with open(write_file, 'w') as fid_out:
            contents = fid.read()
            contents.replace('{}', 'THE-FINAL-PRODUCT!')
            fid_out.write(contents)