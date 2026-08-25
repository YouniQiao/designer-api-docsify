# sppWrite

## Modules to Import

```TypeScript
import { socket } from 'kits/@kit.ConnectivityKit';
```

## sppWrite

```TypeScript
function sppWrite(clientSocket: number, data: ArrayBuffer): void
```

Write data through the socket.

**Since:** 10

**System capability:** SystemCapability.Communication.Bluetooth.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| clientSocket | number | Yes |
| data | ArrayBuffer | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| 2901054 |
| 2900099 |
