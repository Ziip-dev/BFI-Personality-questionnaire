from flask import Blueprint, render_template
from flask import current_app as app


# Blueprint configuration
home_bp = Blueprint(
    "home_bp",
    __name__,
    template_folder="templates",
    static_folder="static",
)


@home_bp.route("/", methods=["GET"])
def home():
    """Homepage."""
    return render_template(
        "index.jinja2",
        title="Choose a title",
        subtitle="Choose a subtitle",
        template="home-template",
    )
