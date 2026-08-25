# unbindDriverWithDeviceId

## Modules to Import

```TypeScript
import { deviceManager } from 'kits/@kit.DriverDevelopmentKit';
```

## unbindDriverWithDeviceId

```TypeScript
function unbindDriverWithDeviceId(deviceId: number): Promise<number>
```

Unbinds a peripheral device. This API uses a promise to return the result.

**Since:** 19

**Required permissions:** ohos.permission.ACCESS_DDK_DRIVERS

**System capability:** SystemCapability.Driver.ExternalDevice

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| deviceId | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;number & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [26300001](../errorcode-deviceManager.md#26300001-externaldevicemanager-service-exception) |
| [26300003](../errorcode-deviceManager.md#26300003-driver-client-not-bound-to-any-driver-server) |
