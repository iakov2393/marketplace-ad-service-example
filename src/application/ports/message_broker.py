from abc import ABC, abstractmethod
from typing import Any


class MessageBroker(ABC):
    @abstractmethod
    async def send(
        self,
        payload: dict[str, Any],
        headers: list[tuple[str, bytes]] | None = None,
    ) -> None: ...
