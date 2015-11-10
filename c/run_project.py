from c.z.the_module import the_module_function, the_module_write_function


def run():
    print('Running run_project.py!')
    the_module_function()
    # write a file:
    the_module_write_function(read_file='./z/y/template.md', write_file='../README.md')

if __name__ == '__main__':
    run()
