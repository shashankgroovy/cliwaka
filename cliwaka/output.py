from pygments import highlight, lexers, formatters
import json

DEFAULT_INDENT = 4

def pretty_output(data, sort=False):
    try:
        obj = json.loads(data)
    except JSONDecodeError:
        pass # Invalid JSON, ignore.
    else:
        # Indent, sort keys by name and avoid unicode escapes to improve
        # redability.

        data = json.dumps(
            obj=obj,
            sort_keys=sort,
            #ensure_ascii=False,
            indent=DEFAULT_INDENT
        )
        pretty_json = highlight(
                        unicode(data, 'UTF-8'),
                        lexers.JsonLexer(),
                        formatters.TerminalFormatter()
                    )
    return pretty_json

