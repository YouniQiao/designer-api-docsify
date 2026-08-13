# @ohos.bluetooth.socket

Provides methods to operate or manage bluetooth socket connection.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Deprecated since:** -1

<!--Device-unnamed-declare namespace socket--><!--Device-unnamed-declare namespace socket-End-->

**System capability:** SystemCapability.Communication.Bluetooth.Core

## Modules to Import

```TypeScript
import { socket } from '@kit.ConnectivityKit';
```

## Summary

### Functions

| Name | Description |
| --- | --- |
| [getDeviceId](arkts-connectivity-socket-getdeviceid-f.md#getDeviceId) | Obtain the device id in the client socket. |
| [getL2capPsm](arkts-connectivity-socket-getl2cappsm-f.md#getL2capPsm) | Get l2cap socket psm. |
| [getMaxReceiveDataSize](arkts-connectivity-socket-getmaxreceivedatasize-f.md#getMaxReceiveDataSize) | Obtain the maximum data size that can be received through this socket channel. |
| [getMaxTransmitDataSize](arkts-connectivity-socket-getmaxtransmitdatasize-f.md#getMaxTransmitDataSize) | Obtain the maximum data size that can be transmitted through this socket channel. |
| [isConnected](arkts-connectivity-socket-isconnected-f.md#isConnected) | Check whether the current socket connection has been established. |
| [offSppRead](arkts-connectivity-socket-offsppread-f.md#offSppRead) | Unsubscribe the event reported when data is read from the socket. |
| off_sppRead | Unsubscribe the event reported when data is read from the socket. |
| [onSppRead](arkts-connectivity-socket-onsppread-f.md#onSppRead) | Subscribe the event reported when data is read from the socket. |
| on_sppRead | Subscribe the event reported when data is read from the socket. |
| [sppAccept](arkts-connectivity-socket-sppaccept-f.md#sppAccept) | Waits for a remote device to connect. |
| [sppCloseClientSocket](arkts-connectivity-socket-sppcloseclientsocket-f.md#sppCloseClientSocket) | Disables an spp client socket and releases related resources. |
| [sppCloseServerSocket](arkts-connectivity-socket-sppcloseserversocket-f.md#sppCloseServerSocket) | Disables an spp server socket and releases related resources. |
| [sppConnect](arkts-connectivity-socket-sppconnect-f.md#sppConnect) | Connects to a remote device over the socket. |
| [sppListen](arkts-connectivity-socket-spplisten-f.md#sppListen) | Creates a Bluetooth server listening socket. |
| [sppReadAsync](arkts-connectivity-socket-sppreadasync-f.md#sppReadAsync) | Asynchronous interface for reading data from the socket. |
| [sppWrite](arkts-connectivity-socket-sppwrite-f.md#sppWrite) | Write data through the socket. |
| [sppWriteAsync](arkts-connectivity-socket-sppwriteasync-f.md#sppWriteAsync) | Asynchronous interface for writing data to the socket. |

### Interfaces

| Name | Description |
| --- | --- |
| [SppOptions](arkts-connectivity-socket-sppoptions-i.md) | Describes the spp parameters. |

### Enums

| Name | Description |
| --- | --- |
| [SppType](arkts-connectivity-socket-spptype-e.md) | The enum of SPP type. |

