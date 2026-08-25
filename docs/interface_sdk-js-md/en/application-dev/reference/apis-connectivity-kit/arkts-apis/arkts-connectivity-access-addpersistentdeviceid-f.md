# addPersistentDeviceId

## Modules to Import

```TypeScript
import { access } from 'kits/@kit.ConnectivityKit';
```

## addPersistentDeviceId

```TypeScript
function addPersistentDeviceId(deviceId: string): Promise<void>
```

Add a persistent random device address. Once the randomized address is successfully added, the application can save it for an extended period of time.

**Since:** 16

**Required permissions:** ohos.permission.ACCESS_BLUETOOTH and ohos.permission.PERSISTENT_BLUETOOTH_PEERS_MAC

**Atomic service API:** This API can be used in atomic services since API version 16.

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
| [201](../../errorcode-universal.md#201-permission-denied) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| 2900003 |
| 2900010 |
| 2900099 |
