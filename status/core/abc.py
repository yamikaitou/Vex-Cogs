from abc import ABC, ABCMeta, abstractmethod

from aiohttp import ClientSession
from discord.ext.commands.cog import CogMeta
from redbot.core.bot import Red
from redbot.core.config import Config

from status.core.statusapi import StatusAPI
from status.objects import (
    ConfigWrapper,
    LastChecked,
    ServiceCooldown,
    ServiceRestrictionsCache,
    UsedFeeds,
)
from status.updateloop.updatechecker import UpdateChecker


class CompositeMetaClass(CogMeta, ABCMeta):
    """
    This allows the metaclass used for proper type detection to
    coexist with discord.py's metaclass
    """


class MixinMeta(ABC):
    """A wonderful class for typehinting :tada:"""

    bot: Red
    config: Config
    config_wrapper: ConfigWrapper

    update_checker: UpdateChecker

    used_feeds: UsedFeeds
    last_checked: LastChecked
    service_cooldown: ServiceCooldown
    service_restrictions_cache: ServiceRestrictionsCache

    session: ClientSession
    statusapi: StatusAPI

    @abstractmethod
    async def get_initial_data(self) -> None:
        raise NotImplementedError()