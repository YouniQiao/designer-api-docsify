# getMaxTransmitDataSize

## Modules to Import

```TypeScript
import { socket } from 'socket';
```

## getMaxTransmitDataSize

```TypeScript
function getMaxTransmitDataSize(clientSocket: int): int
```

Obtain the maximum data size that can be transmitted through this socket channel.

**Since:** 26.0.0

<!--Device-socket-function getMaxTransmitDataSize(clientSocket: int): int--><!--Device-socket-function getMaxTransmitDataSize(clientSocket: int): int-End-->

**System capability:** SystemCapability.Communication.Bluetooth.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| clientSocket | int | Yes | Indicates the client socket ID, returned by [sppAccept](arkts-connectivity-socket-sppaccept-f.md#sppaccept) or [sppConnect](arkts-connectivity-socket-sppconnect-f.md#sppconnect). |

**Return value:**

| Type | Description |
| --- | --- |
| int | Maximum transmitted data size |

**Examples**

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

