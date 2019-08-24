from application import app
from application.models import *
from application.validators import *
from flask import request, render_template


@app.route("/", methods=['GET','POST'])
def index():
    form = CNPForm(request.form)
    if request.method == 'POST' and form.validate():
            return render_template("index.html",
                                    form=form,
                                    CNP_valid=True,
                                    status=status,
                                    luna=luna,
                                    judet=judet
                                    )
    else:
        return render_template("index.html", form=form)
