try:
    from aiohttp import web
except ImportError:
    from subprocess import run
    run("uv pip install aiohttp", shell=True, check=True)
    from aiohttp import web
    
import random


DOMAINS = [
"https://serene-brushlands-72781-fb40f4a5e926.herokuapp.com/",
"https://immense-wildwood-50417-2bbd00a4745a.herokuapp.com/",
"https://lit-forest-91753-e86dafd1de80.herokuapp.com/",
]


async def redirect_handler(request):

    domain = random.choice(DOMAINS).rstrip("/")

    raise web.HTTPFound(
        f"{domain}{request.rel_url.path_qs}"
    )


app = web.Application()

app.router.add_route(
    "*",
    "/{path:.*}",
    redirect_handler
)

if __name__ == "__main__":

    web.run_app(
        app,
        port=8097
    )
