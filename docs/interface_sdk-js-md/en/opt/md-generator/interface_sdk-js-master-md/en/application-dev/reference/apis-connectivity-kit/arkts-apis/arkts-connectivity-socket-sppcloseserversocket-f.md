# sppCloseServerSocket

## Modules to Import

```TypeScript
import { socket } from '@kit.ConnectivityKit';
```

## sppCloseServerSocket

```TypeScript
function sppCloseServerSocket(socket: number): void
```

Disables an spp server socket and releases related resources.

**Since:** 26.0.0

**Deprecated since:** -1

<!--Device-socket-function sppCloseServerSocket(socket: int): void--><!--Device-socket-function sppCloseServerSocket(socket: int): void-End-->

**System capability:** SystemCapability.Communication.Bluetooth.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [socket](arkts-bluetooth-socket.md) | number | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| 2900001 |
| 2900099 |

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
