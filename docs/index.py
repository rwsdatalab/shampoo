#this is the working one


import panel as pn
from panel.widgets import Button, Gauge, CrossSelector,FileInput
import time
import re
import io
import zipfile
import http


clean_files = []
clean_filenames = []
list_regex_default = ["Artikel regel 2<OOV>: Artikel=<OOV>: artikel",
                      "Nummers 1<OOV>\^3\^<OOV>3",
                      "Nummers 2<OOV>\^2\^<OOV>2",]


def savecookie():
    import datetime
    import requests

    import http.cookiejar

    # create a new cookie
    import datetime
    import http.cookiejar

    expires = datetime.datetime.now() + datetime.timedelta(hours=1)
    expires = expires.strftime("%a, %d %b %Y %H:%M:%S GMT")
    expires_time = time.mktime(time.strptime(expires, '%a, %d %b %Y %H:%M:%S GMT'))
    # create a new cookie
    cookie = http.cookiejar.Cookie(
        version=0,
        name="example",
        value="value",
        expires=expires_time,
        port=None,
        port_specified=False,
        domain="example.com",
        domain_specified=True,
        domain_initial_dot=False,
        path="/",
        path_specified=True,
        secure=False,
        discard=True,
        comment=None,
        comment_url=None,
        rest={'HttpOnly': None},
        rfc2109=False
    )

    # create a new cookie jar
    cookie_jar = http.cookiejar.MozillaCookieJar('cookies.txt')

    # add the cookie to the cookie jar
    cookie_jar.set_cookie(cookie)
    cookie_jar.save()


    print(pn.state.cookies.items())
    

def updatecookie():
    html = pn.pane.HTML('')
    html.object = """
    <script>
        document.cookie = "custom_cookie=custom_value; Expires=Fri, 14 Jan 2023 14:28:00 GMT, SameSite=None; Secure";
    </script>
    """
def on_press_download_button():
    global clean_files
    global clean_filenames
    output = io.BytesIO()
    zf = zipfile.ZipFile(output, mode='w')
    for filename, filecontent in zip(clean_filenames, clean_files):
        zf.writestr(filename, filecontent)
    zf.close()
    output.seek(0)
    return output

""" 
add manual regex
"""
def on_add_regex_button(event):
    regx = search_selector.value 
    
    for r in regx:
        print(str(r.split('<OOV>')))
    
    print("|||||||||||")
    #get_panel()
    global list_regex_default
    # Add string to search_selector
    #list_regex_default.append(str(textbox_regex_name.value)+"<OOV>"+str(textbox_regex_from.value)+"<OOV>"+str(textbox_regex_to.value))
    #print(list_regex_default)
    reg_val = str(str(textbox_regex_name.value)+"<OOV>"+\
            str(textbox_regex_from.value)+"<OOV>"+str(textbox_regex_to.value))

    if reg_val not in list_regex_default and len(reg_val)>10:

        print("original list, ", list_regex_default)
        print(search_selector.value)
        list_regex_default.append(reg_val)
        print("Manually added, ", list_regex_default[-1])
    #search_selector.value = search_selector.value + list_regex_default[-1]
        search_selector.value.append(list_regex_default[-1])
        print(search_selector.value)
        search_selector.param.trigger('value')
    #search_selector.force_new_dynamic_value()
    # print(list_regex_default)
    

# Create a file input component
file_input = pn.widgets.FileInput(multiple=True)

#file_input = pn.widgets.FileSelector('~')

# Create a button to start processing the files.
process_button = Button(name='Process files')

# Create a button to save button that contains the zipped files.
# save_button = Button(name='Save files')
#upload_regex = Button(name='Upload regex')
##
##
"""
Upload regex file
"""
def upload_file(event):

    
    lines = upload_regex.value
    lines = lines.decode()
    #print(lines,' lines')
    regex_lines = lines.split('\n')
    #print(regex_lines, ' regex_lines')
    print('-----------------')
    for i in regex_lines:
        if str(i) not in list_regex_default and len(str(i))>0:
            list_regex_default.append(str(i))
            print(str(i))
            search_selector.value.append(str(i))
            search_selector.param.trigger('value')

upload_regex = FileInput(accept='.txt', name='Upload regex txt file')
upload_regex.param.watch(upload_file, 'value')
# Create download button
download_button = pn.widgets.FileDownload(filename="data.zip", callback=on_press_download_button, button_type="primary", disabled=True)

# Create a gauge bar to show the progress
#progress_gauge = Gauge(name='Progress', value=0, width=300, title_size=10, colors=[(0.2, 'red'), (0.8, 'gold'), (1, 'green')])
progress_gauge = pn.indicators.LinearGauge(name='Progress of applying regex', value=0,bounds=(0,100),format='{value:.0f} %', horizontal=True,width=100)
# Create a crossSelector to search the input in each of the files
search_selector = CrossSelector(name='Regular Expression', options=list_regex_default, value=[], width=1000, definition_order=False)


#werkt alleen als je met values heen en weer gaat
# oplossing bedenken voor het wijzigen van een value
# def print_value(value):
#     print("Selected value:", value)
#     print(search_selector.value)

# pn.interact(print_value, value=search_selector)



# @pn.depends(search_selector.param.value)
# def callback(value):
#     print("Selected value:", value)
#     # Edit the selected value here
#     print(value)
# def print_value(event):
#     print("Selected value:", event.new)
# search_selector.param.value.on_change('click',print_value)
# search_selector.param.watch(callback, 'value')
# search_selector.param.watch_values(callback, 'value')

# Create textbox to show processed files
textbox = pn.widgets.input.TextAreaInput(placeholder='Processed files are shown here..', width=1000, height=225)

# Create textbox to add new regular expressions
textbox_regex_name = pn.widgets.input.TextAreaInput(placeholder='regex name', width=250, height=50)
textbox_regex_from = pn.widgets.input.TextAreaInput(placeholder='regex expression', width=250, height=50)
textbox_regex_to = pn.widgets.input.TextAreaInput(placeholder='replace char', width=250, height=50)
add_regex_button = Button(name='Add regex', width=180, height=50)

# Create a callback function to handle the button press
def on_button_press(event):
    global clean_files
    global clean_filenames
    clean_files, clean_filenames = [], []
    textboxstring = ''
    progress_gauge.value = 0

    if process_button.clicks:
        regex = search_selector.value
        files = file_input.value
        #print(regex)

        if files is not None:
            # Iterate over the selected files
            for i, _ in enumerate(files):
                string = ''
                # Update process for files
                progress_gauge.value = ((i + 1) / len(files) )* 100
                # print(file_input.filename[i])
                string =  file_input.value[i].decode('utf-8')
                for reg in regex:
                    # Do some processing here
                    #print('Replace %s with %s' %(reg[1], reg[2]))
                    
                    reg = reg.split('<OOV>')
                    string = re.sub(str(reg[1]), reg[2], string)
                    string = re.sub(str(reg[1]),reg[2],r'{}'.format(string))
                    string = re.sub(r'{}'.format(reg[1]),reg[2],r'{}'.format(string))
                    string = re.sub(r'{}'.format(reg[1]),reg[2],string)
                    print(string)
                # Store clean filename
                clean_files.append(string)
                clean_filenames.append(file_input.filename[i])
                textbox.value = ', '.join(clean_filenames)
                
                #print(file_input.value[i])
                #print(file_input.filename[i])
                # time.sleep(0.1)

            if len(clean_files)>0:
                download_button.disabled = False


# Create the separator line
separator_vertical = pn.pane.HTML("""
    <style>
        .vertical {
            border-left: 1px solid black;
            height: 450px;
            position:absolute;
            left: 0%;
        }
    </style>

<div class= "vertical"></div>
""")    


# Link the button to the callback function
process_button.on_click(on_button_press)

# Link the regex button to the callback function
add_regex_button.on_click(on_add_regex_button)

# Link the button to the callback function
# save_button.on_click(on_save_button_press)


# Create the left-side panel
left_panel = pn.Column(
    "Upload file to apply Regex",
    file_input,
    pn.Spacer(width=50),  # Add some space between the panels
    process_button,
    progress_gauge,
    # save_button,
    download_button,
    "Upload text file to import regex rules",
    upload_regex,
)


# Create the main top panel
top_panel = pn.Column()


# Create the main panel
main_panel = pn.Column(
    top_panel,    
    search_selector,
    pn.Row(textbox_regex_name, textbox_regex_from, textbox_regex_to, add_regex_button),
    
    pn.Row(textbox),
    
)


# Create the main dashboard
dashboard = pn.Row(
    left_panel,
    pn.Spacer(width=20),  # Set the left panel width to 20%
    separator_vertical,
    pn.Spacer(width=50),  # Add some space between the panels
    main_panel,
    pn.Spacer(width=10),  # Set the top panel width to 30%
)



# Serve the dashboard
dashboard.servable()       

pn.extension('bokeh')
#pn.extension(sizing_mode="stretch_width", template="fast")
# panel serve hvplot_interactive.ipynb
#panel serve --show --autoreload
