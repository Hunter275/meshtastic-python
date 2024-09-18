"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""

import builtins
import collections.abc
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.internal.enum_type_wrapper
import google.protobuf.message
import meshtastic.protobuf.channel_pb2
import meshtastic.protobuf.config_pb2
import meshtastic.protobuf.localonly_pb2
import meshtastic.protobuf.mesh_pb2
import meshtastic.protobuf.telemetry_pb2
import sys
import typing

if sys.version_info >= (3, 10):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class _ScreenFonts:
    ValueType = typing.NewType("ValueType", builtins.int)
    V: typing_extensions.TypeAlias = ValueType

class _ScreenFontsEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_ScreenFonts.ValueType], builtins.type):
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
    FONT_SMALL: _ScreenFonts.ValueType  # 0
    """
    TODO: REPLACE
    """
    FONT_MEDIUM: _ScreenFonts.ValueType  # 1
    """
    TODO: REPLACE
    """
    FONT_LARGE: _ScreenFonts.ValueType  # 2
    """
    TODO: REPLACE
    """

class ScreenFonts(_ScreenFonts, metaclass=_ScreenFontsEnumTypeWrapper):
    """
    Font sizes for the device screen
    """

FONT_SMALL: ScreenFonts.ValueType  # 0
"""
TODO: REPLACE
"""
FONT_MEDIUM: ScreenFonts.ValueType  # 1
"""
TODO: REPLACE
"""
FONT_LARGE: ScreenFonts.ValueType  # 2
"""
TODO: REPLACE
"""
global___ScreenFonts = ScreenFonts

@typing.final
class PositionLite(google.protobuf.message.Message):
    """
    Position with static location information only for NodeDBLite
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    LATITUDE_I_FIELD_NUMBER: builtins.int
    LONGITUDE_I_FIELD_NUMBER: builtins.int
    ALTITUDE_FIELD_NUMBER: builtins.int
    TIME_FIELD_NUMBER: builtins.int
    LOCATION_SOURCE_FIELD_NUMBER: builtins.int
    latitude_i: builtins.int
    """
    The new preferred location encoding, multiply by 1e-7 to get degrees
    in floating point
    """
    longitude_i: builtins.int
    """
    TODO: REPLACE
    """
    altitude: builtins.int
    """
    In meters above MSL (but see issue #359)
    """
    time: builtins.int
    """
    This is usually not sent over the mesh (to save space), but it is sent
    from the phone so that the local device can set its RTC If it is sent over
    the mesh (because there are devices on the mesh without GPS), it will only
    be sent by devices which has a hardware GPS clock.
    seconds since 1970
    """
    location_source: meshtastic.protobuf.mesh_pb2.Position.LocSource.ValueType
    """
    TODO: REPLACE
    """
    def __init__(
        self,
        *,
        latitude_i: builtins.int = ...,
        longitude_i: builtins.int = ...,
        altitude: builtins.int = ...,
        time: builtins.int = ...,
        location_source: meshtastic.protobuf.mesh_pb2.Position.LocSource.ValueType = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["altitude", b"altitude", "latitude_i", b"latitude_i", "location_source", b"location_source", "longitude_i", b"longitude_i", "time", b"time"]) -> None: ...

global___PositionLite = PositionLite

@typing.final
class UserLite(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    MACADDR_FIELD_NUMBER: builtins.int
    LONG_NAME_FIELD_NUMBER: builtins.int
    SHORT_NAME_FIELD_NUMBER: builtins.int
    HW_MODEL_FIELD_NUMBER: builtins.int
    IS_LICENSED_FIELD_NUMBER: builtins.int
    ROLE_FIELD_NUMBER: builtins.int
    PUBLIC_KEY_FIELD_NUMBER: builtins.int
    macaddr: builtins.bytes
    """
    This is the addr of the radio.
    """
    long_name: builtins.str
    """
    A full name for this user, i.e. "Kevin Hester"
    """
    short_name: builtins.str
    """
    A VERY short name, ideally two characters.
    Suitable for a tiny OLED screen
    """
    hw_model: meshtastic.protobuf.mesh_pb2.HardwareModel.ValueType
    """
    TBEAM, HELTEC, etc...
    Starting in 1.2.11 moved to hw_model enum in the NodeInfo object.
    Apps will still need the string here for older builds
    (so OTA update can find the right image), but if the enum is available it will be used instead.
    """
    is_licensed: builtins.bool
    """
    In some regions Ham radio operators have different bandwidth limitations than others.
    If this user is a licensed operator, set this flag.
    Also, "long_name" should be their licence number.
    """
    role: meshtastic.protobuf.config_pb2.Config.DeviceConfig.Role.ValueType
    """
    Indicates that the user's role in the mesh
    """
    public_key: builtins.bytes
    """
    The public key of the user's device.
    This is sent out to other nodes on the mesh to allow them to compute a shared secret key.
    """
    def __init__(
        self,
        *,
        macaddr: builtins.bytes = ...,
        long_name: builtins.str = ...,
        short_name: builtins.str = ...,
        hw_model: meshtastic.protobuf.mesh_pb2.HardwareModel.ValueType = ...,
        is_licensed: builtins.bool = ...,
        role: meshtastic.protobuf.config_pb2.Config.DeviceConfig.Role.ValueType = ...,
        public_key: builtins.bytes = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["hw_model", b"hw_model", "is_licensed", b"is_licensed", "long_name", b"long_name", "macaddr", b"macaddr", "public_key", b"public_key", "role", b"role", "short_name", b"short_name"]) -> None: ...

global___UserLite = UserLite

@typing.final
class NodeInfoLite(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    NUM_FIELD_NUMBER: builtins.int
    USER_FIELD_NUMBER: builtins.int
    POSITION_FIELD_NUMBER: builtins.int
    SNR_FIELD_NUMBER: builtins.int
    LAST_HEARD_FIELD_NUMBER: builtins.int
    DEVICE_METRICS_FIELD_NUMBER: builtins.int
    CHANNEL_FIELD_NUMBER: builtins.int
    VIA_MQTT_FIELD_NUMBER: builtins.int
    HOPS_AWAY_FIELD_NUMBER: builtins.int
    IS_FAVORITE_FIELD_NUMBER: builtins.int
    num: builtins.int
    """
    The node number
    """
    snr: builtins.float
    """
    Returns the Signal-to-noise ratio (SNR) of the last received message,
    as measured by the receiver. Return SNR of the last received message in dB
    """
    last_heard: builtins.int
    """
    Set to indicate the last time we received a packet from this node
    """
    channel: builtins.int
    """
    local channel index we heard that node on. Only populated if its not the default channel.
    """
    via_mqtt: builtins.bool
    """
    True if we witnessed the node over MQTT instead of LoRA transport
    """
    hops_away: builtins.int
    """
    Number of hops away from us this node is (0 if adjacent)
    """
    is_favorite: builtins.bool
    """
    True if node is in our favorites list
    Persists between NodeDB internal clean ups
    """
    @property
    def user(self) -> global___UserLite:
        """
        The user info for this node
        """

    @property
    def position(self) -> global___PositionLite:
        """
        This position data. Note: before 1.2.14 we would also store the last time we've heard from this node in position.time, that is no longer true.
        Position.time now indicates the last time we received a POSITION from that node.
        """

    @property
    def device_metrics(self) -> meshtastic.protobuf.telemetry_pb2.DeviceMetrics:
        """
        The latest device metrics for the node.
        """

    def __init__(
        self,
        *,
        num: builtins.int = ...,
        user: global___UserLite | None = ...,
        position: global___PositionLite | None = ...,
        snr: builtins.float = ...,
        last_heard: builtins.int = ...,
        device_metrics: meshtastic.protobuf.telemetry_pb2.DeviceMetrics | None = ...,
        channel: builtins.int = ...,
        via_mqtt: builtins.bool = ...,
        hops_away: builtins.int | None = ...,
        is_favorite: builtins.bool = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["_hops_away", b"_hops_away", "device_metrics", b"device_metrics", "hops_away", b"hops_away", "position", b"position", "user", b"user"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["_hops_away", b"_hops_away", "channel", b"channel", "device_metrics", b"device_metrics", "hops_away", b"hops_away", "is_favorite", b"is_favorite", "last_heard", b"last_heard", "num", b"num", "position", b"position", "snr", b"snr", "user", b"user", "via_mqtt", b"via_mqtt"]) -> None: ...
    def WhichOneof(self, oneof_group: typing.Literal["_hops_away", b"_hops_away"]) -> typing.Literal["hops_away"] | None: ...

global___NodeInfoLite = NodeInfoLite

@typing.final
class DeviceState(google.protobuf.message.Message):
    """
    This message is never sent over the wire, but it is used for serializing DB
    state to flash in the device code
    FIXME, since we write this each time we enter deep sleep (and have infinite
    flash) it would be better to use some sort of append only data structure for
    the receive queue and use the preferences store for the other stuff
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    MY_NODE_FIELD_NUMBER: builtins.int
    OWNER_FIELD_NUMBER: builtins.int
    RECEIVE_QUEUE_FIELD_NUMBER: builtins.int
    VERSION_FIELD_NUMBER: builtins.int
    RX_TEXT_MESSAGE_FIELD_NUMBER: builtins.int
    NO_SAVE_FIELD_NUMBER: builtins.int
    DID_GPS_RESET_FIELD_NUMBER: builtins.int
    RX_WAYPOINT_FIELD_NUMBER: builtins.int
    NODE_REMOTE_HARDWARE_PINS_FIELD_NUMBER: builtins.int
    NODE_DB_LITE_FIELD_NUMBER: builtins.int
    version: builtins.int
    """
    A version integer used to invalidate old save files when we make
    incompatible changes This integer is set at build time and is private to
    NodeDB.cpp in the device code.
    """
    no_save: builtins.bool
    """
    Used only during development.
    Indicates developer is testing and changes should never be saved to flash.
    Deprecated in 2.3.1
    """
    did_gps_reset: builtins.bool
    """
    Some GPS receivers seem to have bogus settings from the factory, so we always do one factory reset.
    """
    @property
    def my_node(self) -> meshtastic.protobuf.mesh_pb2.MyNodeInfo:
        """
        Read only settings/info about this node
        """

    @property
    def owner(self) -> meshtastic.protobuf.mesh_pb2.User:
        """
        My owner info
        """

    @property
    def receive_queue(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[meshtastic.protobuf.mesh_pb2.MeshPacket]:
        """
        Received packets saved for delivery to the phone
        """

    @property
    def rx_text_message(self) -> meshtastic.protobuf.mesh_pb2.MeshPacket:
        """
        We keep the last received text message (only) stored in the device flash,
        so we can show it on the screen.
        Might be null
        """

    @property
    def rx_waypoint(self) -> meshtastic.protobuf.mesh_pb2.MeshPacket:
        """
        We keep the last received waypoint stored in the device flash,
        so we can show it on the screen.
        Might be null
        """

    @property
    def node_remote_hardware_pins(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[meshtastic.protobuf.mesh_pb2.NodeRemoteHardwarePin]:
        """
        The mesh's nodes with their available gpio pins for RemoteHardware module
        """

    @property
    def node_db_lite(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___NodeInfoLite]:
        """
        New lite version of NodeDB to decrease memory footprint
        """

    def __init__(
        self,
        *,
        my_node: meshtastic.protobuf.mesh_pb2.MyNodeInfo | None = ...,
        owner: meshtastic.protobuf.mesh_pb2.User | None = ...,
        receive_queue: collections.abc.Iterable[meshtastic.protobuf.mesh_pb2.MeshPacket] | None = ...,
        version: builtins.int = ...,
        rx_text_message: meshtastic.protobuf.mesh_pb2.MeshPacket | None = ...,
        no_save: builtins.bool = ...,
        did_gps_reset: builtins.bool = ...,
        rx_waypoint: meshtastic.protobuf.mesh_pb2.MeshPacket | None = ...,
        node_remote_hardware_pins: collections.abc.Iterable[meshtastic.protobuf.mesh_pb2.NodeRemoteHardwarePin] | None = ...,
        node_db_lite: collections.abc.Iterable[global___NodeInfoLite] | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["my_node", b"my_node", "owner", b"owner", "rx_text_message", b"rx_text_message", "rx_waypoint", b"rx_waypoint"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["did_gps_reset", b"did_gps_reset", "my_node", b"my_node", "no_save", b"no_save", "node_db_lite", b"node_db_lite", "node_remote_hardware_pins", b"node_remote_hardware_pins", "owner", b"owner", "receive_queue", b"receive_queue", "rx_text_message", b"rx_text_message", "rx_waypoint", b"rx_waypoint", "version", b"version"]) -> None: ...

global___DeviceState = DeviceState

@typing.final
class ChannelFile(google.protobuf.message.Message):
    """
    The on-disk saved channels
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CHANNELS_FIELD_NUMBER: builtins.int
    VERSION_FIELD_NUMBER: builtins.int
    version: builtins.int
    """
    A version integer used to invalidate old save files when we make
    incompatible changes This integer is set at build time and is private to
    NodeDB.cpp in the device code.
    """
    @property
    def channels(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[meshtastic.protobuf.channel_pb2.Channel]:
        """
        The channels our node knows about
        """

    def __init__(
        self,
        *,
        channels: collections.abc.Iterable[meshtastic.protobuf.channel_pb2.Channel] | None = ...,
        version: builtins.int = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["channels", b"channels", "version", b"version"]) -> None: ...

global___ChannelFile = ChannelFile

@typing.final
class OEMStore(google.protobuf.message.Message):
    """
    This can be used for customizing the firmware distribution. If populated,
    show a secondary bootup screen with custom logo and text for 2.5 seconds.
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    OEM_ICON_WIDTH_FIELD_NUMBER: builtins.int
    OEM_ICON_HEIGHT_FIELD_NUMBER: builtins.int
    OEM_ICON_BITS_FIELD_NUMBER: builtins.int
    OEM_FONT_FIELD_NUMBER: builtins.int
    OEM_TEXT_FIELD_NUMBER: builtins.int
    OEM_AES_KEY_FIELD_NUMBER: builtins.int
    OEM_LOCAL_CONFIG_FIELD_NUMBER: builtins.int
    OEM_LOCAL_MODULE_CONFIG_FIELD_NUMBER: builtins.int
    oem_icon_width: builtins.int
    """
    The Logo width in Px
    """
    oem_icon_height: builtins.int
    """
    The Logo height in Px
    """
    oem_icon_bits: builtins.bytes
    """
    The Logo in XBM bytechar format
    """
    oem_font: global___ScreenFonts.ValueType
    """
    Use this font for the OEM text.
    """
    oem_text: builtins.str
    """
    Use this font for the OEM text.
    """
    oem_aes_key: builtins.bytes
    """
    The default device encryption key, 16 or 32 byte
    """
    @property
    def oem_local_config(self) -> meshtastic.protobuf.localonly_pb2.LocalConfig:
        """
        A Preset LocalConfig to apply during factory reset
        """

    @property
    def oem_local_module_config(self) -> meshtastic.protobuf.localonly_pb2.LocalModuleConfig:
        """
        A Preset LocalModuleConfig to apply during factory reset
        """

    def __init__(
        self,
        *,
        oem_icon_width: builtins.int = ...,
        oem_icon_height: builtins.int = ...,
        oem_icon_bits: builtins.bytes = ...,
        oem_font: global___ScreenFonts.ValueType = ...,
        oem_text: builtins.str = ...,
        oem_aes_key: builtins.bytes = ...,
        oem_local_config: meshtastic.protobuf.localonly_pb2.LocalConfig | None = ...,
        oem_local_module_config: meshtastic.protobuf.localonly_pb2.LocalModuleConfig | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["oem_local_config", b"oem_local_config", "oem_local_module_config", b"oem_local_module_config"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["oem_aes_key", b"oem_aes_key", "oem_font", b"oem_font", "oem_icon_bits", b"oem_icon_bits", "oem_icon_height", b"oem_icon_height", "oem_icon_width", b"oem_icon_width", "oem_local_config", b"oem_local_config", "oem_local_module_config", b"oem_local_module_config", "oem_text", b"oem_text"]) -> None: ...

global___OEMStore = OEMStore
