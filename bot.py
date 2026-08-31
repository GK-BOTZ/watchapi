try:
    from aiohttp import web
except ImportError:
    from subprocess import run
    run("uv pip install aiohttp", shell=True, check=True)
    from aiohttp import web
    
import random


DOMAINS = [
    "https://calm-wildwood-11126-3f21a217b614.herokuapp.com/",
    "https://fast-peak-16120-de47b85e8208.herokuapp.com/",
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
