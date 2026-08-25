# queryDriverInfo (System API)

## Modules to Import

```TypeScript
import { deviceManager } from 'kits/@kit.DriverDevelopmentKit';
```

## queryDriverInfo

```TypeScript
function queryDriverInfo(driverUid?: string): Array<Readonly<DriverInfo>>
```

Obtains the list of detailed information about peripheral drivers. If the device has no peripheral device connected, an empty list is returned.

**Since:** 12

**Required permissions:** ohos.permission.ACCESS_EXTENSIONAL_DEVICE_DRIVER

**System capability:** SystemCapability.Driver.ExternalDevice

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| driverUid | string | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Array&lt;Readonly&lt;[DriverInfo](arkts-driverdevelopment-devicemanager-driverinfo-i-sys.md)&gt;&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [26300001](../errorcode-deviceManager.md#26300001-externaldevicemanager-service-exception) |
