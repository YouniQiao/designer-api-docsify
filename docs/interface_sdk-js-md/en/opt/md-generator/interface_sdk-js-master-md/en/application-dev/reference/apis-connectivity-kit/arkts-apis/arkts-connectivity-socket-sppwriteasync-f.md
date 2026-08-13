# sppWriteAsync

## Modules to Import

```TypeScript
import { socket } from '@kit.ConnectivityKit';
```

## sppWriteAsync

```TypeScript
function sppWriteAsync(clientSocket: number, data: ArrayBuffer): Promise<void>
```

Asynchronous interface for writing data to the socket.

**Since:** 26.0.0

**Deprecated since:** -1

<!--Device-socket-function sppWriteAsync(clientSocket: int, data: ArrayBuffer): Promise<void>--><!--Device-socket-function sppWriteAsync(clientSocket: int, data: ArrayBuffer): Promise<void>-End-->

**System capability:** SystemCapability.Communication.Bluetooth.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| clientSocket | number | Yes |
| data | ArrayBuffer | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| 2901054 |
| 2900099 |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let clientNumber = 1; // clientNumber is obtained by sppAccept or sppConnect.
let arrayBuffer = new ArrayBuffer(8);
let data = new Uint8Array(arrayBuffer);
try {
    socket.sppWriteAsync(clientNumber, arrayBuffer).then(() => {
      console.info("sppWrite success");
    });
} catch (err) {
    console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}
```
