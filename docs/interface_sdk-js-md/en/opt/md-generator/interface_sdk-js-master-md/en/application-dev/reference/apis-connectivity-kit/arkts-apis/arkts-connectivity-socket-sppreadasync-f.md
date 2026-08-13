# sppReadAsync

## Modules to Import

```TypeScript
import { socket } from '@kit.ConnectivityKit';
```

## sppReadAsync

```TypeScript
function sppReadAsync(clientSocket: number): Promise<ArrayBuffer>
```

Asynchronous interface for reading data from the socket.

**Since:** 26.0.0

**Deprecated since:** -1

<!--Device-socket-function sppReadAsync(clientSocket: int): Promise<ArrayBuffer>--><!--Device-socket-function sppReadAsync(clientSocket: int): Promise<ArrayBuffer>-End-->

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

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

// clientNumber is obtained via sppAccept or sppConnect.
async function readAsync(clientNumber: number) {
  let flag = 1;
  try {
    while (flag) { // Call the API cyclically to read data. This example is for reference only. You need to change the implementation based on the service requirements. 
      let buffer = await socket.sppReadAsync(clientNumber); // Use await to ensure sequential reading.
      let data = new Uint8Array(buffer);
      if (data) {
        console.info('sppRead success, data length = ' + data.byteLength);
        // Process the received data.
      }
    }
  } catch (err) {
    console.error('startSppRead errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
    socket.sppCloseClientSocket(clientNumber); // Close the connection when an error occurs.
  }
}
```
