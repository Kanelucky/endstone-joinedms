from endstone.plugin import Plugin
from endstone import ColorFormat
from endstone.event import event_handler, PlayerJoinEvent, PlayerQuitEvent
from endstone import Player

class Joinedms(Plugin):
    api_version = "0.10"
    @event_handler
    def on_player_join(self, event: PlayerJoinEvent):
        msg = self.config.get("joined-message")
        msg = msg.replace("{player_name}", event.player.name)
        event.join_message = (msg)
    @event_handler
    def on_player_quit(self, event:PlayerQuitEvent):
        msg = self.config.get("quit-message")
        msg = msg.replace("{player_name}", event.player.name)
        event.quit_message = (msg)


    def on_load(self) -> None:
        self.logger.info("Joinedms loaded")
        self.save_default_config()
    def on_enable(self) -> None:
        self.save_config()
        self.logger.info(ColorFormat.DARK_GREEN + "JoinedMS enabled. Enjoy!")
        self.register_events(self)
    def on_disable(self) -> None:
        self.logger.info("JoinedMS disabled. Goodbye!")
