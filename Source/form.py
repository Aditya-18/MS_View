def get_forms(browser):
    forms = browser.find_elements_by_tag_name('form')
    if not forms:
        return False

    forms = [ form for form in forms if (form.size["width"] != 0 and form.size["height"] != 0) ]
    if not forms:
        return False

    return [ extract_form_details(form) for form in forms ]

def extract_form_details(form):
    role = form.get_attribute('role')
    all_input_boxes = form.find_elements_by_tag_name('input')
    input_boxes = []
    for input_box in all_input_boxes:
        if(input_box.get_attribute('type') == 'text' and input_box.get_attribute('name')):
            input_boxes.append(input_box)
        elif(input_box.get_attribute('type') == 'password'):
            input_boxes.append(input_box)
    return {
        "form": form,
        "role": role,
        "input_boxes": input_boxes
    }
