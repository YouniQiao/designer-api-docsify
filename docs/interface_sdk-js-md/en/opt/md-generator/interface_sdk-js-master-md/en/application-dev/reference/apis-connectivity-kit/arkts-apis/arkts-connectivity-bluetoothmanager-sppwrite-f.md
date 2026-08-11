# sppWrite

## Modules to Import

```TypeScript
import { bluetoothManager } from 'kits/@kit.ConnectivityKit';
```

## sppWrite

```TypeScript
function sppWrite(clientSocket: number, data: ArrayBuffer): void
```

Write data through the socket.

**Since:** 9

**Deprecated since:** 10

**Substitutes:** ohos.bluetooth.socket/socket#sppWrite

<!--Device-bluetoothManager-function sppWrite(clientSocket: number, data: ArrayBuffer): void--><!--Device-bluetoothManager-function sppWrite(clientSocket: number, data: ArrayBuffer): void-End-->

**System capability:** SystemCapability.Communication.Bluetooth.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| clientSocket | number | Yes |
| data | ArrayBuffer | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [801](../../apis-ads-kit/errorcode-ads.md#801-ad-request-failure) |
| 2901054 |
| 2900099 |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
let clientNumber = -1;
function clientSocket(code: BusinessError, number: number) {
  if (code == null || code.code != 0) {
    return;
  }
  console.info(`bluetooth serverSocket Number: ${number}`);
  // The obtained clientNumber is used as the socket ID for subsequent read/write operations on the client.
  clientNumber = number;
}
let arrayBuffer = new ArrayBuffer(8);
let data = new Uint8Array(arrayBuffer);
data[0] = 123;
try {
    bluetoothManager.sppWrite(clientNumber, arrayBuffer);
} catch (err) {
    console.error(`errCode: ${err.code}, errMessage: ${err.message}`);
}
```
