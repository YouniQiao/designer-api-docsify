# offSppRead

## offSppRead

```TypeScript
function offSppRead(clientSocket: int, callback?: Callback<ArrayBuffer>): void
```

Unsubscribe the event reported when data is read from the socket.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

<!--Device-socket-function offSppRead(clientSocket: int, callback?: Callback<ArrayBuffer>): void--><!--Device-socket-function offSppRead(clientSocket: int, callback?: Callback<ArrayBuffer>): void-End-->

**System capability:** SystemCapability.Communication.Bluetooth.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| clientSocket | int | Yes | Client socket ID, which is obtained by sppAccept or sppConnect. The value should be an integer. |
| callback | \_\_\_MD\_LINK\_USD\_0\_\_\_&lt;ArrayBuffer&gt; | No | Callback used to listen for the spp read event. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [801](../../apis-ads-kit/errorcode-ads.md#801-ad-request-failure) | Capability not supported. |

