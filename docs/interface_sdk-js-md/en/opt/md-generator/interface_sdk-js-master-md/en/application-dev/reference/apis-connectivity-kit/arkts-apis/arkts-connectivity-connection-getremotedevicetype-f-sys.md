# getRemoteDeviceType (System API)

## Modules to Import

```TypeScript
import { connection } from '@kit.ConnectivityKit';
```

## getRemoteDeviceType

```TypeScript
function getRemoteDeviceType(deviceId: string): Promise<DeviceType>
```

Get remote device custom type.

**Since:** 23

**Deprecated since:** -1

**Required permissions:** 
- API version 12 - 17: ohos.permission.ACCESS_BLUETOOTH

**Model restriction:** This API can be used only in the stage model.

<!--Device-connection-function getRemoteDeviceType(deviceId: string): Promise<DeviceType>--><!--Device-connection-function getRemoteDeviceType(deviceId: string): Promise<DeviceType>-End-->

**System capability:** SystemCapability.Communication.Bluetooth.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| deviceId | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;DeviceType & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| 2900001 |
| 2900003 |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
// promise
try {
    connection.getRemoteDeviceType('11:22:33:44:55:66').then((data: connection.DeviceType) => {
        console.info('getRemoteDeviceType success, DeviceType:' + JSON.stringify(data));
    });
} catch (err) {
    console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}
```
