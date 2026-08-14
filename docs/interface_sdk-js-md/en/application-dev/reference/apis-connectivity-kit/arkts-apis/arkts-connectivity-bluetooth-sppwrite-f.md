# sppWrite

## Modules to Import

```TypeScript
import { bluetooth } from 'bluetooth';
```

## sppWrite

```TypeScript
function sppWrite(clientSocket: number, data: ArrayBuffer): boolean
```

Write data through the socket.

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Deprecated since:** 9

**Substitutes:** [sppWrite](arkts-connectivity-bluetoothmanager-sppwrite-f.md#sppWrite)

<!--Device-bluetooth-function sppWrite(clientSocket: number, data: ArrayBuffer): boolean--><!--Device-bluetooth-function sppWrite(clientSocket: number, data: ArrayBuffer): boolean-End-->

**System capability:** SystemCapability.Communication.Bluetooth.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| clientSocket | number | Yes | Indicates the client socket ID, returned by [sppAccept](arkts-connectivity-bluetooth-sppaccept-f.md#sppAccept) or [sppConnect](arkts-connectivity-bluetooth-sppconnect-f.md#sppConnect). |
| data | ArrayBuffer | Yes | Indicates the data to write. |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | Returns { |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
let clientNumber = -1;
function clientSocket(code : BusinessError, number : number) {
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
let ret : boolean = bluetooth.sppWrite(clientNumber, arrayBuffer);
if (ret) {
  console.info('spp write successfully');
} else {
  console.error('spp write failed');
}
```

