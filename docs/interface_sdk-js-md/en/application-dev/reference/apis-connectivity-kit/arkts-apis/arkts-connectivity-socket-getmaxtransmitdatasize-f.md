# getMaxTransmitDataSize

## Modules to Import

```TypeScript
import { socket } from 'kits/@kit.ConnectivityKit';
```

## getMaxTransmitDataSize

```TypeScript
function getMaxTransmitDataSize(clientSocket: int): int
```

Obtain the maximum data size that can be transmitted through this socket channel.

**Since:** 22

**ArkTS mode:** ArkTS-Dyn since version 22; ArkTS-Sta since version 26.0.0.

<!--Device-socket-function getMaxTransmitDataSize(clientSocket: int): int--><!--Device-socket-function getMaxTransmitDataSize(clientSocket: int): int-End-->

**System capability:** SystemCapability.Communication.Bluetooth.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| clientSocket | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | Indicates the client socket ID, returned by {@link sppAccept} or {@link sppConnect}. |

**Return value:**

| Type | Description |
| --- | --- |
| ArkTS-Dyn: number  <br>ArkTS-Sta：int | Maximum transmitted data size |

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

