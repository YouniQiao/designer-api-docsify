# queryDriverInfo (System API)

## Modules to Import

```TypeScript
import { deviceManager } from '@kit.DriverDevelopmentKit';
```

## queryDriverInfo

```TypeScript
function queryDriverInfo(driverUid?: string): Array<Readonly<DriverInfo>>
```

Obtains the list of detailed information about peripheral drivers. If the device has no peripheral device connected, an empty list is returned.

**Since:** 23

**Deprecated since:** -1

**Required permissions:** ohos.permission.ACCESS_EXTENSIONAL_DEVICE_DRIVER

<!--Device-deviceManager-function queryDriverInfo(driverUid?: string): Array<Readonly<DriverInfo>>--><!--Device-deviceManager-function queryDriverInfo(driverUid?: string): Array<Readonly<DriverInfo>>-End-->

**System capability:** SystemCapability.Driver.ExternalDevice

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| driverUid | string | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Array&lt;[Readonly](../../apis-na/arkts-apis/arkts-na-readonly-t.md)&lt;[DriverInfo](arkts-driverdevelopment-devicemanager-driverinfo-i-sys.md)&gt;&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [26300001](../../apis-driverdevelopment-kit/errorcode-deviceManager.md#26300001-externaldevicemanager-service-exception) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## Examples

```TypeScript
import { deviceManager } from '@kit.DriverDevelopmentKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  // In this example, driver-12345 is the driver UID. During application development, you can use queryDeviceInfo to query the driver UID and use it as the input parameter.
  let driverInfos : Array<deviceManager.DriverInfo> = deviceManager.queryDriverInfo("driver-12345");
  for (let item of driverInfos) {
    console.info(`driver name is ${item.driverName}`)
  }
} catch (error) {
  let err: BusinessError = error as BusinessError;
  console.error(`Failed to query driver info. Code is ${err.code}, message is ${err.message}`);
}
```
