# sppCloseClientSocket

## Modules to Import

```TypeScript
import { socket } from 'socket';
```

## sppCloseClientSocket

```TypeScript
function sppCloseClientSocket(socket: int): void
```

Disables an spp client socket and releases related resources.

**Since:** 26.0.0

<!--Device-socket-function sppCloseClientSocket(socket: int): void--><!--Device-socket-function sppCloseClientSocket(socket: int): void-End-->

**System capability:** SystemCapability.Communication.Bluetooth.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| socket | int | Yes | Indicates the client socket ID, returned by [sppAccept](arkts-connectivity-socket-sppaccept-f.md#sppaccept) or [sppConnect](arkts-connectivity-socket-sppconnect-f.md#sppconnect). |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| [801](../../errorcode-universal.md#801-api-not-supported) | Capability not supported. |
| 2900001 | Service stopped. |
| 2900099 | Operation failed. |

**Examples**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let clientNumber = 1; // clientNumber is obtained by sppAccept or sppConnect.
try {
    socket.sppCloseClientSocket(clientNumber);
} catch (err) {
    console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}
```

