# deletePersistentDeviceId

## Modules to Import

```TypeScript
import { access } from '@kit.ConnectivityKit';
```

## deletePersistentDeviceId

```TypeScript
function deletePersistentDeviceId(deviceId: string): Promise<void>
```

Delete a persistent random device address.

**Since:** 23

**Deprecated since:** -1

**Required permissions:** ohos.permission.ACCESS_BLUETOOTH and ohos.permission.PERSISTENT_BLUETOOTH_PEERS_MAC

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-access-function deletePersistentDeviceId(deviceId: string): Promise<void>--><!--Device-access-function deletePersistentDeviceId(deviceId: string): Promise<void>-End-->

**System capability:** SystemCapability.Communication.Bluetooth.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| deviceId | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| 2900003 |
| 2900099 |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let deviceId = '11:22:33:44:55:66' // The address can be obtained through BLE scanning.
try {
    access.deletePersistentDeviceId(deviceId);
} catch (err) {
    console.error('errCode: ' + err.code + ', errMessage: ' + err.message);
}
```
