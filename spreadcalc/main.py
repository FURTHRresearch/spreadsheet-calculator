import time

import flask
import tempfile
from .auth import check_key
import os
import uuid
bp = flask.Blueprint('main', __name__)




@bp.route('/',methods=["GET"])
def hello():
    return 'Hello!'


@bp.route('/evaluate')
@check_key
def evaluate():
    root_file_path = flask.current_app.config.get("ROOT_FILE_PATH")
    spreadsheet_file = uuid.uuid4()
    spreadsheet_file = f"{spreadsheet_file}.xlsx"
    spreadsheet_file_new = uuid.uuid4()
    spreadsheet_file_new = f"{spreadsheet_file_new}.xlsx"
    with open(spreadsheet_file, "wb+") as f:
        spreadsheet_bytes = flask.request.data
        f.write(spreadsheet_bytes)

    # spreadsheet_file = tempfile.NamedTemporaryFile(delete=False, suffix=".xlsx")


    # spreadsheet_file.close()

    docbuilder_file = uuid.uuid4()
    docbuilder_file = f"{docbuilder_file}.docbuilder"

    with open("recalculate_template.docbuilder", "r") as f:
        docbuilder_string = f.read()
        docbuilder_string = docbuilder_string.replace("<filename>", spreadsheet_file)
        docbuilder_string = docbuilder_string.replace("<filename_new>", f"{spreadsheet_file_new}")

    with open(docbuilder_file, "w+") as f:
        f.write(docbuilder_string)

    while not os.path.isfile(docbuilder_file):
        time.sleep(0.01)

    command = ["documentbuilder", f"'{docbuilder_file}'"]
    os.system(" ".join(command))

    timeout = 10
    start = time.time()
    while not os.path.isfile(spreadsheet_file_new):
        time.sleep(0.01)
        if time.time() - start > timeout:
            return

    with open(spreadsheet_file_new, "rb") as f:
        spreadsheet_bytes = f.read()

    os.remove(docbuilder_file)
    os.remove(spreadsheet_file)
    os.remove(spreadsheet_file_new)

    return spreadsheet_bytes

