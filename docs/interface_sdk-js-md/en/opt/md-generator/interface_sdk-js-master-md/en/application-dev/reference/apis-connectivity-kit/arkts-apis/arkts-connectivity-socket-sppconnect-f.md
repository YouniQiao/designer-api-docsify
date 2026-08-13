# sppConnect

## Modules to Import

```TypeScript
import { socket } from '@kit.ConnectivityKit';
```

## sppConnect

```TypeScript
function sppConnect(deviceId: string, options: SppOptions, callback: AsyncCallback<number>): void
```

Connects to a remote device over the socket.

**Since:** 26.0.0

**Deprecated since:** -1

**Required permissions:** ohos.permission.ACCESS_BLUETOOTH

<!--Device-socket-function sppConnect(deviceId: string, options: SppOptions, callback: AsyncCallback<int>): void--><!--Device-socket-function sppConnect(deviceId: string, options: SppOptions, callback: AsyncCallback<int>): void-End-->

**System capability:** SystemCapability.Communication.Bluetooth.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| deviceId | string | Yes |
| options | [SppOptions](arkts-connectivity-socket-sppoptions-i.md) | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;number&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| 2900004 |
| [201](../../errorcode-universal.md#201-permission-denied) |
| 2900001 |
| 2900003 |
| 2900099 |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let clientSocket = (code: BusinessError, number: number) => {
  if (code) {
    console.error('sppConnect error, code is ' + code);
    return;
  } else {
    // The obtained number is used as the socket ID for subsequent read/write operations on the client.
    console.info('bluetooth clientSocket Number: ' + number);
  }
}

// Use the RFCOMM socket as an example.
let sppOption:socket.SppOptions = {uuid: '00001810-0000-1000-8000-00805F9B34FB', secure: false, type: socket.SppType.SPP_RFCOMM};
try {
    socket.sppConnect('XX:XX:XX:XX:XX:XX', sppOption, clientSocket);
} catch (err) {
    console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}
```
