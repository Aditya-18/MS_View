def get_child_by_class(container, class_name):
    elem = None
    try:
        elem = container.find_element_by_class_name(class_name)
    except:
        pass
    return elem

def extract_notification(elem):
    heading = ''
    try:
        heading = elem.find_element_by_class_name("ActivityItem-textSection").text
    except common.exceptions.NoSuchElementException:
        heading = ''
    return {
        "heading": heading,
        "target": elem
    }
