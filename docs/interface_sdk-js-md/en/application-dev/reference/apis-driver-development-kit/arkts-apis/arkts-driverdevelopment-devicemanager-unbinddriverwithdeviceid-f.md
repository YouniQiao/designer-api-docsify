# unbindDriverWithDeviceId

## Modules to Import

```TypeScript
import { deviceManager } from 'kits/@kit.DriverDevelopmentKit';
```

## unbindDriverWithDeviceId

```TypeScript
function unbindDriverWithDeviceId(deviceId: long): Promise<int>
```

解除设备绑定。使用Promise异步回调。

**Since:** 19

**ArkTS mode:** ArkTS-Dyn since version 19; ArkTS-Sta since version 23.

**Required permissions:** ohos.permission.ACCESS_DDK_DRIVERS

<!--Device-deviceManager-function unbindDriverWithDeviceId(deviceId: long): Promise<int>--><!--Device-deviceManager-function unbindDriverWithDeviceId(deviceId: long): Promise<int>-End-->

**System capability:** SystemCapability.Driver.ExternalDevice

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| deviceId | ArkTS-Dyn: number  <br>ArkTS-Sta：long | Yes | 设备ID，通过[queryDevices](arkts-driverdevelopment-devicemanager-querydevices-f.md#querydevices)获得。 |

**Return value:**

| Type | Description |
| --- | --- |
| ArkTS-Dyn: Promise&lt;number&gt;  <br>ArkTS-Sta：Promise&lt;int&gt; | Promise对象，返回解除绑定的设备ID。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 26300001 | ExternalDeviceManager service exception. |
| 26300003 | There is no binding relationship. |
| 201 | The permission check failed. |

## Examples

```TypeScript
import { deviceManager } from '@kit.DriverDevelopmentKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  // For example, deviceId is 12345678. You can use queryDevices() to obtain the deviceId.
  deviceManager.unbindDriverWithDeviceId(12345678).then((data : number) => {
    console.info(`unbindDriverWithDeviceId success, Device_Id is ${data}.`);
  }, (error : BusinessError) => {
    console.error(`unbindDriverWithDeviceId async fail. Code is ${error.code}, message is ${error.message}`);
  });
} catch (error) {
  console.error(`unbindDriverWithDeviceId fail. Code is ${error.code}, message is ${error.message}`);
}
```

