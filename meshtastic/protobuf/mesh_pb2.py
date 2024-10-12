# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: meshtastic/protobuf/mesh.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from meshtastic.protobuf import channel_pb2 as meshtastic_dot_protobuf_dot_channel__pb2
from meshtastic.protobuf import config_pb2 as meshtastic_dot_protobuf_dot_config__pb2
from meshtastic.protobuf import module_config_pb2 as meshtastic_dot_protobuf_dot_module__config__pb2
from meshtastic.protobuf import portnums_pb2 as meshtastic_dot_protobuf_dot_portnums__pb2
from meshtastic.protobuf import telemetry_pb2 as meshtastic_dot_protobuf_dot_telemetry__pb2
from meshtastic.protobuf import xmodem_pb2 as meshtastic_dot_protobuf_dot_xmodem__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1emeshtastic/protobuf/mesh.proto\x12\x13meshtastic.protobuf\x1a!meshtastic/protobuf/channel.proto\x1a meshtastic/protobuf/config.proto\x1a\'meshtastic/protobuf/module_config.proto\x1a\"meshtastic/protobuf/portnums.proto\x1a#meshtastic/protobuf/telemetry.proto\x1a meshtastic/protobuf/xmodem.proto\"\x99\x07\n\x08Position\x12\x17\n\nlatitude_i\x18\x01 \x01(\x0fH\x00\x88\x01\x01\x12\x18\n\x0blongitude_i\x18\x02 \x01(\x0fH\x01\x88\x01\x01\x12\x15\n\x08\x61ltitude\x18\x03 \x01(\x05H\x02\x88\x01\x01\x12\x0c\n\x04time\x18\x04 \x01(\x07\x12@\n\x0flocation_source\x18\x05 \x01(\x0e\x32\'.meshtastic.protobuf.Position.LocSource\x12@\n\x0f\x61ltitude_source\x18\x06 \x01(\x0e\x32\'.meshtastic.protobuf.Position.AltSource\x12\x11\n\ttimestamp\x18\x07 \x01(\x07\x12\x1f\n\x17timestamp_millis_adjust\x18\x08 \x01(\x05\x12\x19\n\x0c\x61ltitude_hae\x18\t \x01(\x11H\x03\x88\x01\x01\x12(\n\x1b\x61ltitude_geoidal_separation\x18\n \x01(\x11H\x04\x88\x01\x01\x12\x0c\n\x04PDOP\x18\x0b \x01(\r\x12\x0c\n\x04HDOP\x18\x0c \x01(\r\x12\x0c\n\x04VDOP\x18\r \x01(\r\x12\x14\n\x0cgps_accuracy\x18\x0e \x01(\r\x12\x19\n\x0cground_speed\x18\x0f \x01(\rH\x05\x88\x01\x01\x12\x19\n\x0cground_track\x18\x10 \x01(\rH\x06\x88\x01\x01\x12\x13\n\x0b\x66ix_quality\x18\x11 \x01(\r\x12\x10\n\x08\x66ix_type\x18\x12 \x01(\r\x12\x14\n\x0csats_in_view\x18\x13 \x01(\r\x12\x11\n\tsensor_id\x18\x14 \x01(\r\x12\x13\n\x0bnext_update\x18\x15 \x01(\r\x12\x12\n\nseq_number\x18\x16 \x01(\r\x12\x16\n\x0eprecision_bits\x18\x17 \x01(\r\"N\n\tLocSource\x12\r\n\tLOC_UNSET\x10\x00\x12\x0e\n\nLOC_MANUAL\x10\x01\x12\x10\n\x0cLOC_INTERNAL\x10\x02\x12\x10\n\x0cLOC_EXTERNAL\x10\x03\"b\n\tAltSource\x12\r\n\tALT_UNSET\x10\x00\x12\x0e\n\nALT_MANUAL\x10\x01\x12\x10\n\x0c\x41LT_INTERNAL\x10\x02\x12\x10\n\x0c\x41LT_EXTERNAL\x10\x03\x12\x12\n\x0e\x41LT_BAROMETRIC\x10\x04\x42\r\n\x0b_latitude_iB\x0e\n\x0c_longitude_iB\x0b\n\t_altitudeB\x0f\n\r_altitude_haeB\x1e\n\x1c_altitude_geoidal_separationB\x0f\n\r_ground_speedB\x0f\n\r_ground_track\"\xea\x01\n\x04User\x12\n\n\x02id\x18\x01 \x01(\t\x12\x11\n\tlong_name\x18\x02 \x01(\t\x12\x12\n\nshort_name\x18\x03 \x01(\t\x12\x13\n\x07macaddr\x18\x04 \x01(\x0c\x42\x02\x18\x01\x12\x34\n\x08hw_model\x18\x05 \x01(\x0e\x32\".meshtastic.protobuf.HardwareModel\x12\x13\n\x0bis_licensed\x18\x06 \x01(\x08\x12;\n\x04role\x18\x07 \x01(\x0e\x32-.meshtastic.protobuf.Config.DeviceConfig.Role\x12\x12\n\npublic_key\x18\x08 \x01(\x0c\"Z\n\x0eRouteDiscovery\x12\r\n\x05route\x18\x01 \x03(\x07\x12\x13\n\x0bsnr_towards\x18\x02 \x03(\x05\x12\x12\n\nroute_back\x18\x03 \x03(\x07\x12\x10\n\x08snr_back\x18\x04 \x03(\x05\"\xfd\x03\n\x07Routing\x12<\n\rroute_request\x18\x01 \x01(\x0b\x32#.meshtastic.protobuf.RouteDiscoveryH\x00\x12:\n\x0broute_reply\x18\x02 \x01(\x0b\x32#.meshtastic.protobuf.RouteDiscoveryH\x00\x12:\n\x0c\x65rror_reason\x18\x03 \x01(\x0e\x32\".meshtastic.protobuf.Routing.ErrorH\x00\"\xb0\x02\n\x05\x45rror\x12\x08\n\x04NONE\x10\x00\x12\x0c\n\x08NO_ROUTE\x10\x01\x12\x0b\n\x07GOT_NAK\x10\x02\x12\x0b\n\x07TIMEOUT\x10\x03\x12\x10\n\x0cNO_INTERFACE\x10\x04\x12\x12\n\x0eMAX_RETRANSMIT\x10\x05\x12\x0e\n\nNO_CHANNEL\x10\x06\x12\r\n\tTOO_LARGE\x10\x07\x12\x0f\n\x0bNO_RESPONSE\x10\x08\x12\x14\n\x10\x44UTY_CYCLE_LIMIT\x10\t\x12\x0f\n\x0b\x42\x41\x44_REQUEST\x10 \x12\x12\n\x0eNOT_AUTHORIZED\x10!\x12\x0e\n\nPKI_FAILED\x10\"\x12\x16\n\x12PKI_UNKNOWN_PUBKEY\x10#\x12\x19\n\x15\x41\x44MIN_BAD_SESSION_KEY\x10$\x12!\n\x1d\x41\x44MIN_PUBLIC_KEY_UNAUTHORIZED\x10%B\t\n\x07variant\"\xd4\x01\n\x04\x44\x61ta\x12-\n\x07portnum\x18\x01 \x01(\x0e\x32\x1c.meshtastic.protobuf.PortNum\x12\x0f\n\x07payload\x18\x02 \x01(\x0c\x12\x15\n\rwant_response\x18\x03 \x01(\x08\x12\x0c\n\x04\x64\x65st\x18\x04 \x01(\x07\x12\x0e\n\x06source\x18\x05 \x01(\x07\x12\x12\n\nrequest_id\x18\x06 \x01(\x07\x12\x10\n\x08reply_id\x18\x07 \x01(\x07\x12\r\n\x05\x65moji\x18\x08 \x01(\x07\x12\x15\n\x08\x62itfield\x18\t \x01(\rH\x00\x88\x01\x01\x42\x0b\n\t_bitfield\"\xbc\x01\n\x08Waypoint\x12\n\n\x02id\x18\x01 \x01(\r\x12\x17\n\nlatitude_i\x18\x02 \x01(\x0fH\x00\x88\x01\x01\x12\x18\n\x0blongitude_i\x18\x03 \x01(\x0fH\x01\x88\x01\x01\x12\x0e\n\x06\x65xpire\x18\x04 \x01(\r\x12\x11\n\tlocked_to\x18\x05 \x01(\r\x12\x0c\n\x04name\x18\x06 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x07 \x01(\t\x12\x0c\n\x04icon\x18\x08 \x01(\x07\x42\r\n\x0b_latitude_iB\x0e\n\x0c_longitude_i\"l\n\x16MqttClientProxyMessage\x12\r\n\x05topic\x18\x01 \x01(\t\x12\x0e\n\x04\x64\x61ta\x18\x02 \x01(\x0cH\x00\x12\x0e\n\x04text\x18\x03 \x01(\tH\x00\x12\x10\n\x08retained\x18\x04 \x01(\x08\x42\x11\n\x0fpayload_variant\"\xf3\x04\n\nMeshPacket\x12\x0c\n\x04\x66rom\x18\x01 \x01(\x07\x12\n\n\x02to\x18\x02 \x01(\x07\x12\x0f\n\x07\x63hannel\x18\x03 \x01(\r\x12,\n\x07\x64\x65\x63oded\x18\x04 \x01(\x0b\x32\x19.meshtastic.protobuf.DataH\x00\x12\x13\n\tencrypted\x18\x05 \x01(\x0cH\x00\x12\n\n\x02id\x18\x06 \x01(\x07\x12\x0f\n\x07rx_time\x18\x07 \x01(\x07\x12\x0e\n\x06rx_snr\x18\x08 \x01(\x02\x12\x11\n\thop_limit\x18\t \x01(\r\x12\x10\n\x08want_ack\x18\n \x01(\x08\x12:\n\x08priority\x18\x0b \x01(\x0e\x32(.meshtastic.protobuf.MeshPacket.Priority\x12\x0f\n\x07rx_rssi\x18\x0c \x01(\x05\x12<\n\x07\x64\x65layed\x18\r \x01(\x0e\x32\'.meshtastic.protobuf.MeshPacket.DelayedB\x02\x18\x01\x12\x10\n\x08via_mqtt\x18\x0e \x01(\x08\x12\x11\n\thop_start\x18\x0f \x01(\r\x12\x12\n\npublic_key\x18\x10 \x01(\x0c\x12\x15\n\rpki_encrypted\x18\x11 \x01(\x08\"s\n\x08Priority\x12\t\n\x05UNSET\x10\x00\x12\x07\n\x03MIN\x10\x01\x12\x0e\n\nBACKGROUND\x10\n\x12\x0b\n\x07\x44\x45\x46\x41ULT\x10@\x12\x0c\n\x08RELIABLE\x10\x46\x12\x0c\n\x08RESPONSE\x10P\x12\x08\n\x04HIGH\x10\x64\x12\x07\n\x03\x41\x43K\x10x\x12\x07\n\x03MAX\x10\x7f\"B\n\x07\x44\x65layed\x12\x0c\n\x08NO_DELAY\x10\x00\x12\x15\n\x11\x44\x45LAYED_BROADCAST\x10\x01\x12\x12\n\x0e\x44\x45LAYED_DIRECT\x10\x02\x42\x11\n\x0fpayload_variant\"\xac\x02\n\x08NodeInfo\x12\x0b\n\x03num\x18\x01 \x01(\r\x12\'\n\x04user\x18\x02 \x01(\x0b\x32\x19.meshtastic.protobuf.User\x12/\n\x08position\x18\x03 \x01(\x0b\x32\x1d.meshtastic.protobuf.Position\x12\x0b\n\x03snr\x18\x04 \x01(\x02\x12\x12\n\nlast_heard\x18\x05 \x01(\x07\x12:\n\x0e\x64\x65vice_metrics\x18\x06 \x01(\x0b\x32\".meshtastic.protobuf.DeviceMetrics\x12\x0f\n\x07\x63hannel\x18\x07 \x01(\r\x12\x10\n\x08via_mqtt\x18\x08 \x01(\x08\x12\x16\n\thops_away\x18\t \x01(\rH\x00\x88\x01\x01\x12\x13\n\x0bis_favorite\x18\n \x01(\x08\x42\x0c\n\n_hops_away\"P\n\nMyNodeInfo\x12\x13\n\x0bmy_node_num\x18\x01 \x01(\r\x12\x14\n\x0creboot_count\x18\x08 \x01(\r\x12\x17\n\x0fmin_app_version\x18\x0b \x01(\r\"\xc9\x01\n\tLogRecord\x12\x0f\n\x07message\x18\x01 \x01(\t\x12\x0c\n\x04time\x18\x02 \x01(\x07\x12\x0e\n\x06source\x18\x03 \x01(\t\x12\x33\n\x05level\x18\x04 \x01(\x0e\x32$.meshtastic.protobuf.LogRecord.Level\"X\n\x05Level\x12\t\n\x05UNSET\x10\x00\x12\x0c\n\x08\x43RITICAL\x10\x32\x12\t\n\x05\x45RROR\x10(\x12\x0b\n\x07WARNING\x10\x1e\x12\x08\n\x04INFO\x10\x14\x12\t\n\x05\x44\x45\x42UG\x10\n\x12\t\n\x05TRACE\x10\x05\"P\n\x0bQueueStatus\x12\x0b\n\x03res\x18\x01 \x01(\x05\x12\x0c\n\x04\x66ree\x18\x02 \x01(\r\x12\x0e\n\x06maxlen\x18\x03 \x01(\r\x12\x16\n\x0emesh_packet_id\x18\x04 \x01(\r\"\xb8\x06\n\tFromRadio\x12\n\n\x02id\x18\x01 \x01(\r\x12\x31\n\x06packet\x18\x02 \x01(\x0b\x32\x1f.meshtastic.protobuf.MeshPacketH\x00\x12\x32\n\x07my_info\x18\x03 \x01(\x0b\x32\x1f.meshtastic.protobuf.MyNodeInfoH\x00\x12\x32\n\tnode_info\x18\x04 \x01(\x0b\x32\x1d.meshtastic.protobuf.NodeInfoH\x00\x12-\n\x06\x63onfig\x18\x05 \x01(\x0b\x32\x1b.meshtastic.protobuf.ConfigH\x00\x12\x34\n\nlog_record\x18\x06 \x01(\x0b\x32\x1e.meshtastic.protobuf.LogRecordH\x00\x12\x1c\n\x12\x63onfig_complete_id\x18\x07 \x01(\rH\x00\x12\x12\n\x08rebooted\x18\x08 \x01(\x08H\x00\x12\x39\n\x0cmoduleConfig\x18\t \x01(\x0b\x32!.meshtastic.protobuf.ModuleConfigH\x00\x12/\n\x07\x63hannel\x18\n \x01(\x0b\x32\x1c.meshtastic.protobuf.ChannelH\x00\x12\x37\n\x0bqueueStatus\x18\x0b \x01(\x0b\x32 .meshtastic.protobuf.QueueStatusH\x00\x12\x33\n\x0cxmodemPacket\x18\x0c \x01(\x0b\x32\x1b.meshtastic.protobuf.XModemH\x00\x12\x37\n\x08metadata\x18\r \x01(\x0b\x32#.meshtastic.protobuf.DeviceMetadataH\x00\x12M\n\x16mqttClientProxyMessage\x18\x0e \x01(\x0b\x32+.meshtastic.protobuf.MqttClientProxyMessageH\x00\x12\x31\n\x08\x66ileInfo\x18\x0f \x01(\x0b\x32\x1d.meshtastic.protobuf.FileInfoH\x00\x12\x45\n\x12\x63lientNotification\x18\x10 \x01(\x0b\x32\'.meshtastic.protobuf.ClientNotificationH\x00\x42\x11\n\x0fpayload_variant\"\x8c\x01\n\x12\x43lientNotification\x12\x15\n\x08reply_id\x18\x01 \x01(\rH\x00\x88\x01\x01\x12\x0c\n\x04time\x18\x02 \x01(\x07\x12\x33\n\x05level\x18\x03 \x01(\x0e\x32$.meshtastic.protobuf.LogRecord.Level\x12\x0f\n\x07message\x18\x04 \x01(\tB\x0b\n\t_reply_id\"1\n\x08\x46ileInfo\x12\x11\n\tfile_name\x18\x01 \x01(\t\x12\x12\n\nsize_bytes\x18\x02 \x01(\r\"\xb8\x02\n\x07ToRadio\x12\x31\n\x06packet\x18\x01 \x01(\x0b\x32\x1f.meshtastic.protobuf.MeshPacketH\x00\x12\x18\n\x0ewant_config_id\x18\x03 \x01(\rH\x00\x12\x14\n\ndisconnect\x18\x04 \x01(\x08H\x00\x12\x33\n\x0cxmodemPacket\x18\x05 \x01(\x0b\x32\x1b.meshtastic.protobuf.XModemH\x00\x12M\n\x16mqttClientProxyMessage\x18\x06 \x01(\x0b\x32+.meshtastic.protobuf.MqttClientProxyMessageH\x00\x12\x33\n\theartbeat\x18\x07 \x01(\x0b\x32\x1e.meshtastic.protobuf.HeartbeatH\x00\x42\x11\n\x0fpayload_variant\"I\n\nCompressed\x12-\n\x07portnum\x18\x01 \x01(\x0e\x32\x1c.meshtastic.protobuf.PortNum\x12\x0c\n\x04\x64\x61ta\x18\x02 \x01(\x0c\"\x90\x01\n\x0cNeighborInfo\x12\x0f\n\x07node_id\x18\x01 \x01(\r\x12\x17\n\x0flast_sent_by_id\x18\x02 \x01(\r\x12$\n\x1cnode_broadcast_interval_secs\x18\x03 \x01(\r\x12\x30\n\tneighbors\x18\x04 \x03(\x0b\x32\x1d.meshtastic.protobuf.Neighbor\"d\n\x08Neighbor\x12\x0f\n\x07node_id\x18\x01 \x01(\r\x12\x0b\n\x03snr\x18\x02 \x01(\x02\x12\x14\n\x0clast_rx_time\x18\x03 \x01(\x07\x12$\n\x1cnode_broadcast_interval_secs\x18\x04 \x01(\r\"\xcf\x02\n\x0e\x44\x65viceMetadata\x12\x18\n\x10\x66irmware_version\x18\x01 \x01(\t\x12\x1c\n\x14\x64\x65vice_state_version\x18\x02 \x01(\r\x12\x13\n\x0b\x63\x61nShutdown\x18\x03 \x01(\x08\x12\x0f\n\x07hasWifi\x18\x04 \x01(\x08\x12\x14\n\x0chasBluetooth\x18\x05 \x01(\x08\x12\x13\n\x0bhasEthernet\x18\x06 \x01(\x08\x12;\n\x04role\x18\x07 \x01(\x0e\x32-.meshtastic.protobuf.Config.DeviceConfig.Role\x12\x16\n\x0eposition_flags\x18\x08 \x01(\r\x12\x34\n\x08hw_model\x18\t \x01(\x0e\x32\".meshtastic.protobuf.HardwareModel\x12\x19\n\x11hasRemoteHardware\x18\n \x01(\x08\x12\x0e\n\x06hasPKC\x18\x0b \x01(\x08\"\x0b\n\tHeartbeat\"^\n\x15NodeRemoteHardwarePin\x12\x10\n\x08node_num\x18\x01 \x01(\r\x12\x33\n\x03pin\x18\x02 \x01(\x0b\x32&.meshtastic.protobuf.RemoteHardwarePin\"e\n\x0e\x43hunkedPayload\x12\x12\n\npayload_id\x18\x01 \x01(\r\x12\x13\n\x0b\x63hunk_count\x18\x02 \x01(\r\x12\x13\n\x0b\x63hunk_index\x18\x03 \x01(\r\x12\x15\n\rpayload_chunk\x18\x04 \x01(\x0c\"\x1f\n\rresend_chunks\x12\x0e\n\x06\x63hunks\x18\x01 \x03(\r\"\xb3\x01\n\x16\x43hunkedPayloadResponse\x12\x12\n\npayload_id\x18\x01 \x01(\r\x12\x1a\n\x10request_transfer\x18\x02 \x01(\x08H\x00\x12\x19\n\x0f\x61\x63\x63\x65pt_transfer\x18\x03 \x01(\x08H\x00\x12;\n\rresend_chunks\x18\x04 \x01(\x0b\x32\".meshtastic.protobuf.resend_chunksH\x00\x42\x11\n\x0fpayload_variant*\xcb\x0c\n\rHardwareModel\x12\t\n\x05UNSET\x10\x00\x12\x0c\n\x08TLORA_V2\x10\x01\x12\x0c\n\x08TLORA_V1\x10\x02\x12\x12\n\x0eTLORA_V2_1_1P6\x10\x03\x12\t\n\x05TBEAM\x10\x04\x12\x0f\n\x0bHELTEC_V2_0\x10\x05\x12\x0e\n\nTBEAM_V0P7\x10\x06\x12\n\n\x06T_ECHO\x10\x07\x12\x10\n\x0cTLORA_V1_1P3\x10\x08\x12\x0b\n\x07RAK4631\x10\t\x12\x0f\n\x0bHELTEC_V2_1\x10\n\x12\r\n\tHELTEC_V1\x10\x0b\x12\x18\n\x14LILYGO_TBEAM_S3_CORE\x10\x0c\x12\x0c\n\x08RAK11200\x10\r\x12\x0b\n\x07NANO_G1\x10\x0e\x12\x12\n\x0eTLORA_V2_1_1P8\x10\x0f\x12\x0f\n\x0bTLORA_T3_S3\x10\x10\x12\x14\n\x10NANO_G1_EXPLORER\x10\x11\x12\x11\n\rNANO_G2_ULTRA\x10\x12\x12\r\n\tLORA_TYPE\x10\x13\x12\x0b\n\x07WIPHONE\x10\x14\x12\x0e\n\nWIO_WM1110\x10\x15\x12\x0b\n\x07RAK2560\x10\x16\x12\x13\n\x0fHELTEC_HRU_3601\x10\x17\x12\x1a\n\x16HELTEC_WIRELESS_BRIDGE\x10\x18\x12\x0e\n\nSTATION_G1\x10\x19\x12\x0c\n\x08RAK11310\x10\x1a\x12\x14\n\x10SENSELORA_RP2040\x10\x1b\x12\x10\n\x0cSENSELORA_S3\x10\x1c\x12\r\n\tCANARYONE\x10\x1d\x12\x0f\n\x0bRP2040_LORA\x10\x1e\x12\x0e\n\nSTATION_G2\x10\x1f\x12\x11\n\rLORA_RELAY_V1\x10 \x12\x0e\n\nNRF52840DK\x10!\x12\x07\n\x03PPR\x10\"\x12\x0f\n\x0bGENIEBLOCKS\x10#\x12\x11\n\rNRF52_UNKNOWN\x10$\x12\r\n\tPORTDUINO\x10%\x12\x0f\n\x0b\x41NDROID_SIM\x10&\x12\n\n\x06\x44IY_V1\x10\'\x12\x15\n\x11NRF52840_PCA10059\x10(\x12\n\n\x06\x44R_DEV\x10)\x12\x0b\n\x07M5STACK\x10*\x12\r\n\tHELTEC_V3\x10+\x12\x11\n\rHELTEC_WSL_V3\x10,\x12\x13\n\x0f\x42\x45TAFPV_2400_TX\x10-\x12\x17\n\x13\x42\x45TAFPV_900_NANO_TX\x10.\x12\x0c\n\x08RPI_PICO\x10/\x12\x1b\n\x17HELTEC_WIRELESS_TRACKER\x10\x30\x12\x19\n\x15HELTEC_WIRELESS_PAPER\x10\x31\x12\n\n\x06T_DECK\x10\x32\x12\x0e\n\nT_WATCH_S3\x10\x33\x12\x11\n\rPICOMPUTER_S3\x10\x34\x12\x0f\n\x0bHELTEC_HT62\x10\x35\x12\x12\n\x0e\x45\x42YTE_ESP32_S3\x10\x36\x12\x11\n\rESP32_S3_PICO\x10\x37\x12\r\n\tCHATTER_2\x10\x38\x12\x1e\n\x1aHELTEC_WIRELESS_PAPER_V1_0\x10\x39\x12 \n\x1cHELTEC_WIRELESS_TRACKER_V1_0\x10:\x12\x0b\n\x07UNPHONE\x10;\x12\x0c\n\x08TD_LORAC\x10<\x12\x13\n\x0f\x43\x44\x45\x42YTE_EORA_S3\x10=\x12\x0f\n\x0bTWC_MESH_V4\x10>\x12\x16\n\x12NRF52_PROMICRO_DIY\x10?\x12\x1f\n\x1bRADIOMASTER_900_BANDIT_NANO\x10@\x12\x1c\n\x18HELTEC_CAPSULE_SENSOR_V3\x10\x41\x12\x1d\n\x19HELTEC_VISION_MASTER_T190\x10\x42\x12\x1d\n\x19HELTEC_VISION_MASTER_E213\x10\x43\x12\x1d\n\x19HELTEC_VISION_MASTER_E290\x10\x44\x12\x19\n\x15HELTEC_MESH_NODE_T114\x10\x45\x12\x16\n\x12SENSECAP_INDICATOR\x10\x46\x12\x13\n\x0fTRACKER_T1000_E\x10G\x12\x0b\n\x07RAK3172\x10H\x12\n\n\x06WIO_E5\x10I\x12\x1a\n\x16RADIOMASTER_900_BANDIT\x10J\x12\x13\n\x0fME25LS01_4Y10TD\x10K\x12\x18\n\x14RP2040_FEATHER_RFM95\x10L\x12\x15\n\x11M5STACK_COREBASIC\x10M\x12\x11\n\rM5STACK_CORE2\x10N\x12\r\n\tRPI_PICO2\x10O\x12\x12\n\x0eM5STACK_CORES3\x10P\x12\x11\n\rSEEED_XIAO_S3\x10Q\x12\x0b\n\x07MS24SF1\x10R\x12\x0c\n\x08TLORA_C6\x10S\x12\x0f\n\nPRIVATE_HW\x10\xff\x01*,\n\tConstants\x12\x08\n\x04ZERO\x10\x00\x12\x15\n\x10\x44\x41TA_PAYLOAD_LEN\x10\xed\x01*\xb4\x02\n\x11\x43riticalErrorCode\x12\x08\n\x04NONE\x10\x00\x12\x0f\n\x0bTX_WATCHDOG\x10\x01\x12\x14\n\x10SLEEP_ENTER_WAIT\x10\x02\x12\x0c\n\x08NO_RADIO\x10\x03\x12\x0f\n\x0bUNSPECIFIED\x10\x04\x12\x15\n\x11UBLOX_UNIT_FAILED\x10\x05\x12\r\n\tNO_AXP192\x10\x06\x12\x19\n\x15INVALID_RADIO_SETTING\x10\x07\x12\x13\n\x0fTRANSMIT_FAILED\x10\x08\x12\x0c\n\x08\x42ROWNOUT\x10\t\x12\x12\n\x0eSX1262_FAILURE\x10\n\x12\x11\n\rRADIO_SPI_BUG\x10\x0b\x12 \n\x1c\x46LASH_CORRUPTION_RECOVERABLE\x10\x0c\x12\"\n\x1e\x46LASH_CORRUPTION_UNRECOVERABLE\x10\rB_\n\x13\x63om.geeksville.meshB\nMeshProtosZ\"github.com/meshtastic/go/generated\xaa\x02\x14Meshtastic.Protobufs\xba\x02\x00\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'meshtastic.protobuf.mesh_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\023com.geeksville.meshB\nMeshProtosZ\"github.com/meshtastic/go/generated\252\002\024Meshtastic.Protobufs\272\002\000'
  _USER.fields_by_name['macaddr']._options = None
  _USER.fields_by_name['macaddr']._serialized_options = b'\030\001'
  _MESHPACKET.fields_by_name['delayed']._options = None
  _MESHPACKET.fields_by_name['delayed']._serialized_options = b'\030\001'
  _globals['_HARDWAREMODEL']._serialized_start=6280
  _globals['_HARDWAREMODEL']._serialized_end=7891
  _globals['_CONSTANTS']._serialized_start=7893
  _globals['_CONSTANTS']._serialized_end=7937
  _globals['_CRITICALERRORCODE']._serialized_start=7940
  _globals['_CRITICALERRORCODE']._serialized_end=8248
  _globals['_POSITION']._serialized_start=273
  _globals['_POSITION']._serialized_end=1194
  _globals['_POSITION_LOCSOURCE']._serialized_start=889
  _globals['_POSITION_LOCSOURCE']._serialized_end=967
  _globals['_POSITION_ALTSOURCE']._serialized_start=969
  _globals['_POSITION_ALTSOURCE']._serialized_end=1067
  _globals['_USER']._serialized_start=1197
  _globals['_USER']._serialized_end=1431
  _globals['_ROUTEDISCOVERY']._serialized_start=1433
  _globals['_ROUTEDISCOVERY']._serialized_end=1523
  _globals['_ROUTING']._serialized_start=1526
  _globals['_ROUTING']._serialized_end=2035
  _globals['_ROUTING_ERROR']._serialized_start=1720
  _globals['_ROUTING_ERROR']._serialized_end=2024
  _globals['_DATA']._serialized_start=2038
  _globals['_DATA']._serialized_end=2250
  _globals['_WAYPOINT']._serialized_start=2253
  _globals['_WAYPOINT']._serialized_end=2441
  _globals['_MQTTCLIENTPROXYMESSAGE']._serialized_start=2443
  _globals['_MQTTCLIENTPROXYMESSAGE']._serialized_end=2551
  _globals['_MESHPACKET']._serialized_start=2554
  _globals['_MESHPACKET']._serialized_end=3181
  _globals['_MESHPACKET_PRIORITY']._serialized_start=2979
  _globals['_MESHPACKET_PRIORITY']._serialized_end=3094
  _globals['_MESHPACKET_DELAYED']._serialized_start=3096
  _globals['_MESHPACKET_DELAYED']._serialized_end=3162
  _globals['_NODEINFO']._serialized_start=3184
  _globals['_NODEINFO']._serialized_end=3484
  _globals['_MYNODEINFO']._serialized_start=3486
  _globals['_MYNODEINFO']._serialized_end=3566
  _globals['_LOGRECORD']._serialized_start=3569
  _globals['_LOGRECORD']._serialized_end=3770
  _globals['_LOGRECORD_LEVEL']._serialized_start=3682
  _globals['_LOGRECORD_LEVEL']._serialized_end=3770
  _globals['_QUEUESTATUS']._serialized_start=3772
  _globals['_QUEUESTATUS']._serialized_end=3852
  _globals['_FROMRADIO']._serialized_start=3855
  _globals['_FROMRADIO']._serialized_end=4679
  _globals['_CLIENTNOTIFICATION']._serialized_start=4682
  _globals['_CLIENTNOTIFICATION']._serialized_end=4822
  _globals['_FILEINFO']._serialized_start=4824
  _globals['_FILEINFO']._serialized_end=4873
  _globals['_TORADIO']._serialized_start=4876
  _globals['_TORADIO']._serialized_end=5188
  _globals['_COMPRESSED']._serialized_start=5190
  _globals['_COMPRESSED']._serialized_end=5263
  _globals['_NEIGHBORINFO']._serialized_start=5266
  _globals['_NEIGHBORINFO']._serialized_end=5410
  _globals['_NEIGHBOR']._serialized_start=5412
  _globals['_NEIGHBOR']._serialized_end=5512
  _globals['_DEVICEMETADATA']._serialized_start=5515
  _globals['_DEVICEMETADATA']._serialized_end=5850
  _globals['_HEARTBEAT']._serialized_start=5852
  _globals['_HEARTBEAT']._serialized_end=5863
  _globals['_NODEREMOTEHARDWAREPIN']._serialized_start=5865
  _globals['_NODEREMOTEHARDWAREPIN']._serialized_end=5959
  _globals['_CHUNKEDPAYLOAD']._serialized_start=5961
  _globals['_CHUNKEDPAYLOAD']._serialized_end=6062
  _globals['_RESEND_CHUNKS']._serialized_start=6064
  _globals['_RESEND_CHUNKS']._serialized_end=6095
  _globals['_CHUNKEDPAYLOADRESPONSE']._serialized_start=6098
  _globals['_CHUNKEDPAYLOADRESPONSE']._serialized_end=6277
# @@protoc_insertion_point(module_scope)
