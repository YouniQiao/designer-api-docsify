# getRemoteDeviceClass

## Modules to Import

```TypeScript
import { bluetoothManager } from '@kit.ConnectivityKit';
```

## getRemoteDeviceClass

```TypeScript
function getRemoteDeviceClass(deviceId: string): DeviceClass
```

Obtains the class of a peer Bluetooth device. On API 10 and above, the permission required by this interface is changed from USE_BLUETOOTH to ACCESS_BLUETOOTH.

**Since:** 9

**Deprecated since:** 10

**Substitutes:** [getRemoteDeviceClass](arkts-connectivity-connection-getremotedeviceclass-f.md#getRemoteDeviceClass)

**Required permissions:** 
- API version 10+: ohos.permission.ACCESS_BLUETOOTH
- API version 9: ohos.permission.USE_BLUETOOTH

<!--Device-bluetoothManager-function getRemoteDeviceClass(deviceId: string): DeviceClass--><!--Device-bluetoothManager-function getRemoteDeviceClass(deviceId: string): DeviceClass-End-->

**System capability:** SystemCapability.Communication.Bluetooth.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| deviceId | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [DeviceClass](arkts-connectivity-connection-deviceclass-i.md) |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| 2900001 |
| 2900003 |
| 2900099 |

## Examples

```TypeScript
import { BusinessError } from '@ohos.base';
try {
    let remoteDeviceClass: bluetoothManager.DeviceClass  = bluetoothManager.getRemoteDeviceClass("XX:XX:XX:XX:XX:XX");
} catch (err) {
    console.error("errCode:" + (err as BusinessError).code + ",errMessage:" + (err as BusinessError).message);
}
```
