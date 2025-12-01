from endstone.plugin import Plugin
from endstone import ColorFormat
from endstone.event import event_handler, PlayerJoinEvent, PlayerQuitEvent
from endstone import Player

class Joinedms(Plugin):
    api_version = "0.10"
    @event_handler
    def on_player_join(self, event: PlayerJoinEvent):
        event.join_message = (ColorFormat.DARK_GREEN + "[+] " + ColorFormat.WHITE + f"{event.player.name}")
    @event_handler
    def on_player_quit(self, event:PlayerQuitEvent):
        event.quit_message = (ColorFormat.DARK_RED + "[-] " + ColorFormat.WHITE + f"{event.player.name}")


    def on_load(self) -> None:
        self.logger.info("on_load is called!")
    def on_enable(self) -> None:
        self.logger.info("on_enable is called!")
        self.register_events(self)
    def on_disable(self) -> None:
        self.logger.info("on_disable is called!")