# setRemoteDeviceType (System API)

## Modules to Import

```TypeScript
import { connection } from '@kit.ConnectivityKit';
```

## setRemoteDeviceType

```TypeScript
function setRemoteDeviceType(deviceId: string, type: DeviceType): Promise<void>
```

Set remote device custom type.

**Since:** 23

**Deprecated since:** -1

**Required permissions:** ohos.permission.ACCESS_BLUETOOTH

**Model restriction:** This API can be used only in the stage model.

<!--Device-connection-function setRemoteDeviceType(deviceId: string, type: DeviceType): Promise<void>--><!--Device-connection-function setRemoteDeviceType(deviceId: string, type: DeviceType): Promise<void>-End-->

**System capability:** SystemCapability.Communication.Bluetooth.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| deviceId | string | Yes |
| type | [DeviceType](../../apis-avsession-kit/arkts-apis/arkts-avsession-avsession-devicetype-e.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| 2900001 |
| 2900003 |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
// promise
try {
    connection.setRemoteDeviceType('11:22:33:44:55:66', connection.DeviceType.DEVICE_TYPE_HEADSET).then(() => {
        console.info('setRemoteDeviceType success');
    });
} catch (err) {
    console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}
```
