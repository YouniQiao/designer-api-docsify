# getMaxReceiveDataSize

## Modules to Import

```TypeScript
import { socket } from '@kit.ConnectivityKit';
```

## getMaxReceiveDataSize

```TypeScript
function getMaxReceiveDataSize(clientSocket: int): int
```

Obtain the maximum data size that can be received through this socket channel.

**Since:** 22

**ArkTS mode:** ArkTS-Dyn since version 22; ArkTS-Sta since version 26.0.0.

<!--Device-socket-function getMaxReceiveDataSize(clientSocket: int): int--><!--Device-socket-function getMaxReceiveDataSize(clientSocket: int): int-End-->

**System capability:** SystemCapability.Communication.Bluetooth.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| clientSocket | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | Indicates the client socket ID, returned by [sppAccept](arkts-connectivity-socket-sppaccept-f.md#sppAccept) or [sppConnect](arkts-connectivity-socket-sppconnect-f.md#sppConnect). |

**Return value:**

| Type | Description |
| --- | --- |
| ArkTS-Dyn: number  <br>ArkTS-Sta：int | Maximum received data size |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

// clientNumber is obtained via sppAccept or sppConnect.
let clientSocket = 1; 
try {
    let result: number = socket.getMaxReceiveDataSize(clientSocket);
} catch (err) {
    console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}
```

