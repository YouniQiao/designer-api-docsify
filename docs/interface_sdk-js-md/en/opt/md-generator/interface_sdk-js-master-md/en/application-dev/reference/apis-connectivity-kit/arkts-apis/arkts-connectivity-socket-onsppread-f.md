# onSppRead

## Modules to Import

```TypeScript
import { socket } from '@kit.ConnectivityKit';
```

## onSppRead

```TypeScript
function onSppRead(clientSocket: number, callback: Callback<ArrayBuffer>): void
```

Subscribe the event reported when data is read from the socket.

**Since:** 26.0.0

**Deprecated since:** -1

<!--Device-socket-function onSppRead(clientSocket: int, callback: Callback<ArrayBuffer>): void--><!--Device-socket-function onSppRead(clientSocket: int, callback: Callback<ArrayBuffer>): void-End-->

**System capability:** SystemCapability.Communication.Bluetooth.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| clientSocket | number | Yes |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;ArrayBuffer&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| 2901054 |
| 2900099 |
