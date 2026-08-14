# sppCloseServerSocket

## Modules to Import

```TypeScript
import { socket } from 'socket';
```

## sppCloseServerSocket

```TypeScript
function sppCloseServerSocket(socket: int): void
```

Disables an spp server socket and releases related resources.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Deprecated since:** -1

<!--Device-socket-function sppCloseServerSocket(socket: int): void--><!--Device-socket-function sppCloseServerSocket(socket: int): void-End-->

**System capability:** SystemCapability.Communication.Bluetooth.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| socket | int | Yes | Indicates the server socket ID, returned by [sppListen](arkts-connectivity-socket-spplisten-f.md#sppListen). |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| [801](../../errorcode-universal.md#801-api-not-supported) | Capability not supported. |
| 2900001 | Service stopped. |
| 2900099 | Operation failed. |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let serverNumber = 1; // Set serverNumber to the value of serverNumber returned by the sppListen callback.
try {
    socket.sppCloseServerSocket(serverNumber);
} catch (err) {
    console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}
```

