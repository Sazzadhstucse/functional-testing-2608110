
import os
import json
import inspect
from flask import Flask, request, render_template_string
import target

app = Flask(__name__)

FUNCTIONS = {
    name: func
    for name, func in inspect.getmembers(target, inspect.isfunction)
    if func.__module__ == target.__name__
}

HTML = """
<!doctype html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Functional Testing Lab</title>
    <style>
        body { font-family: Arial, sans-serif; max-width: 850px;
               margin: 40px auto; padding: 0 18px; background: #f3f6fb; }
        h1 { color: #073b74; }
        form, .result { background: white; padding: 22px;
                        border-radius: 10px; margin-top: 20px; }
        label { display: block; margin-top: 14px; font-weight: bold; }
        select, textarea, button { width: 100%; padding: 11px;
                                   margin-top: 7px; box-sizing: border-box; }
        button { background: #0756a4; color: white; border: 0;
                 cursor: pointer; border-radius: 5px; }
        pre { white-space: pre-wrap; overflow-wrap: anywhere; }
    </style>
</head>
<body>
    <h1>Functional Testing Lab</h1>
    <p>Run the functions from target.py and inspect their results.</p>

    <form method="post">
        <label for="function">Choose a function</label>
        <select name="function" id="function">
            {% for name in functions %}
            <option value="{{ name }}"
                {% if name == selected %}selected{% endif %}>
                {{ name }}
            </option>
            {% endfor %}
        </select>

        <label for="args">Arguments (JSON list)</label>
        <textarea name="args" id="args" rows="4"
          placeholder='Example: [20]'>{{ args_text }}</textarea>
        <button type="submit">Run Function</button>
    </form>

    {% if result is not none %}
    <div class="result">
        <h2>Result</h2>
        <pre>{{ result }}</pre>
    </div>
    {% endif %}

    <p>Health endpoint: <a href="/health">/health</a></p>
</body>
</html>
"""


@app.route("/", methods=["GET", "POST"])
def index():
    selected = request.form.get("function", "is_adult")
    args_text = request.form.get("args", "[18]")
    result = None

    if request.method == "POST":
        try:
            if selected not in FUNCTIONS:
                raise ValueError("Unknown function")

            args = json.loads(args_text)
            if not isinstance(args, list):
                raise ValueError("Arguments must be a JSON list")

            result = repr(FUNCTIONS[selected](*args))
        except Exception as exc:
            result = f"Error: {type(exc).__name__}: {exc}"

    return render_template_string(
        HTML,
        functions=FUNCTIONS,
        selected=selected,
        args_text=args_text,
        result=result,
    )


@app.route("/health")
def health():
    return {
        "status": "ok",
        "commit_sha": os.environ.get("COMMIT_SHA", "local"),
    }


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=False)
