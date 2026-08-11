# setDevicePairingConfirmation

## Modules to Import

```TypeScript
import { connection } from 'kits/@kit.ConnectivityKit';
```

## setDevicePairingConfirmation

```TypeScript
function setDevicePairingConfirmation(deviceId: string, accept: boolean): void
```

Sets the confirmation of pairing with a certain device.

**Since:** 10

**Required permissions:** ohos.permission.ACCESS_BLUETOOTH and ohos.permission.MANAGE_BLUETOOTH

**Model restriction:** This API can be used only in the stage model.

<!--Device-connection-function setDevicePairingConfirmation(deviceId: string, accept: boolean): void--><!--Device-connection-function setDevicePairingConfirmation(deviceId: string, accept: boolean): void-End-->

**System capability:** SystemCapability.Communication.Bluetooth.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| deviceId | string | Yes |
| accept | boolean | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [801](../../apis-ads-kit/errorcode-ads.md#801-ad-request-failure) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| 2900001 |
| 2900003 |
| 2900099 |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
// Subscribe to the pinRequired event and configure the pairing confirmation after receiving a pairing request from the peer device.
function onReceivePinRequiredEvent(data: connection.PinRequiredParam) { // data is the input parameter for the pairing request.
    console.info('pin required  = '+ JSON.stringify(data));
    connection.setDevicePairingConfirmation(data.deviceId, true);
}
try {
    connection.on('pinRequired', onReceivePinRequiredEvent);
} catch (err) {
    console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}
```
