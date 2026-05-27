import uvicorn
from loguru import logger

from app.config import config


def main() -> None:
    logger.info("start server, doc...")
    uvicorn.run(
        "app.asgi:app",
        host=config.listen_host,
        port=config.listen_port,
        reload=getattr(config, "reload", False),
        log_level="warning",
    )


if __name__ == "__main__":
    main()
 
    import uvicorn
    from loguru import logger
    from app.config import config

    if __name__ == "__main__":
        logger.info("start server, doc...")
            uvicorn.run(
                    app="app.asgi:app",
                            host=config.listen_host,
                                    port=config.listen_port,
        