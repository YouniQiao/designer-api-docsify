# getMaxTransmitDataSize

## Modules to Import

```TypeScript
import { socket } from '@kit.ConnectivityKit';
```

## getMaxTransmitDataSize

```TypeScript
function getMaxTransmitDataSize(clientSocket: int): int
```

Obtain the maximum data size that can be transmitted through this socket channel.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Deprecated since:** -1

<!--Device-socket-function getMaxTransmitDataSize(clientSocket: int): int--><!--Device-socket-function getMaxTransmitDataSize(clientSocket: int): int-End-->

**System capability:** SystemCapability.Communication.Bluetooth.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| clientSocket | int | Yes | Indicates the client socket ID, returned by [sppAccept](arkts-connectivity-socket-sppaccept-f.md#sppAccept) or [sppConnect](arkts-connectivity-socket-sppconnect-f.md#sppConnect). |

**Return value:**

| Type | Description |
| --- | --- |
| int | Maximum transmitted data size |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

// clientNumber is obtained via sppAccept or sppConnect.
let clientSocket = 1; 
try {
    let result: number = socket.getMaxTransmitDataSize(clientSocket);
} catch (err) {
    console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}
```

