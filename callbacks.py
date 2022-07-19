def navigate(root, next):
    next_view = next(root)
    next_view.show()


def navigate_back(views):
    views.pop()
    views[-1].show()


"""
def perform_operation(view, db_callback, *args):
    db_callback(args)
    view.show()
"""
