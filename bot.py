try:
    from aiohttp import web
except ImportError:
    from subprocess import run
    run("uv pip install aiohttp", shell=True, check=True)
    from aiohttp import web
    
import random


DOMAINS = [
    "https://desolate-everglades-74468-96c52faedeed.herokuapp.com/https://desolate-everglades-74468-96c52faedeed.herokuapp.com/",
    "https://ronchon-maison-92327-2f40c4807b1b.herokuapp.com/",
    "https://feala8-595a8018a79b.herokuapp.com/",
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
        port=8007
    )
