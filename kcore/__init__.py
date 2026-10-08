type DispatchResult = bool

EVENT_HANDLED: DispatchResult = True
EVENT_UNHANDLED: DispatchResult = False

from .base import Base
from .chip import Chip
from .base_node import BaseNode
from .signal import Signal, Pulse
