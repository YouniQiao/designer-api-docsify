# queryDeviceInfo (System API)

## Modules to Import

```TypeScript
```

## queryDeviceInfo

```TypeScript
function queryDeviceInfo(deviceId?: number): Array<Readonly<DeviceInfo>>
```

Obtains the list of detailed information about peripherals. If the device has no peripheral device connected, an empty list is returned.

**Since:** 23

**Required permissions:** ohos.permission.ACCESS_EXTENSIONAL_DEVICE_DRIVER

<!--Device-deviceManager-function queryDeviceInfo(deviceId?: long): Array<Readonly<DeviceInfo>>--><!--Device-deviceManager-function queryDeviceInfo(deviceId?: long): Array<Readonly<DeviceInfo>>-End-->

**System capability:** SystemCapability.Driver.ExternalDevice

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| deviceId | number | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Array&lt;[Readonly](../../apis-na/arkts-apis/arkts-na-readonly-t.md)&lt;DeviceInfo&gt;&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [26300001](../../apis-driverdevelopment-kit/errorcode-deviceManager.md#26300001-externaldevicemanager-service-exception) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

**Examples**

```TypeScript
import { deviceManager } from '@kit.DriverDevelopmentKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  // For example, deviceId is 12345678. You can use queryDevices() to obtain the deviceId.
  let deviceInfos : Array<deviceManager.DeviceInfo> = deviceManager.queryDeviceInfo(12345678);
  for (let item of deviceInfos) {
    console.info(`Device id is ${item.deviceId}`)
  }
} catch (error) {
  let err: BusinessError = error as BusinessError;
  console.error(`Failed to query device info. Code is ${err.code}, message is ${err.message}`);
}
```
