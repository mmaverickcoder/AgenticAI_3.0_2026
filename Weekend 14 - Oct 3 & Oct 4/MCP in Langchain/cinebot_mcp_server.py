from fastmcp import FastMCP

mcp = FastMCP("CineBot")

@mcp.tool()
def check_showtimes(movie_title: str) -> str:
    """Check available showtimes for a movie."""
    fake_showtimes = {
        "interstellar": "7:00 PM and 10:15 PM",
        "dune part two": "9:30 PM",
    }
    return fake_showtimes.get(movie_title.lower(), "No showtimes found.")

if __name__ == "__main__":
    mcp.run()
