# sppReadAsync

## Modules to Import

```TypeScript
import { socket } from 'kits/@kit.ConnectivityKit';
```

## sppReadAsync

```TypeScript
function sppReadAsync(clientSocket: number): Promise<ArrayBuffer>
```

Asynchronous interface for reading data from the socket.

**Since:** 18

**System capability:** SystemCapability.Communication.Bluetooth.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| clientSocket | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;ArrayBuffer & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| 2901054 |
| 2900099 |
