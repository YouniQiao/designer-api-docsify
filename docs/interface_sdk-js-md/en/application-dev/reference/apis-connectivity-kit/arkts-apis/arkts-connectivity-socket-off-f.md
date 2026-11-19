# off

## Modules to Import

```TypeScript
import { socket } from '@kit.ConnectivityKit';
```

## off('sppRead')

```TypeScript
function off(type: 'sppRead', clientSocket: number, callback?: Callback<ArrayBuffer>): void
```

Unsubscribe the event reported when data is read from the socket.

**Since:** 10

<!--Device-socket-function off(type: 'sppRead', clientSocket: number, callback?: Callback<ArrayBuffer>): void--><!--Device-socket-function off(type: 'sppRead', clientSocket: number, callback?: Callback<ArrayBuffer>): void-End-->

**System capability:** SystemCapability.Communication.Bluetooth.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'sppRead' | Yes | Type of the spp read event to listen for. |
| clientSocket | number | Yes | Client socket ID, which is obtained by sppAccept or sppConnect. |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;ArrayBuffer&gt; | No | Specifies the callback function notification for unsubscription. If the parameter is transferred, the parameter must be set to [socket.on('sppRead')](arkts-connectivity-socket-on-f.md#onsppread) The callback functions in * are the same. If no parameter is transferred, all callback function notifications corresponding to the type are unsubscribed from. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [801](../../errorcode-universal.md#801-api-not-supported) | Capability not supported. Possible causes: <br>1. The hardware does not support the capability; <br>2. The chip does not support the capability; <br>3. A dependent service feature is not supported. |

**Examples**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let clientNumber = 1; // clientNumber is obtained by sppAccept or sppConnect.
try {
    socket.off('sppRead', clientNumber);
} catch (err) {
    console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}
```
