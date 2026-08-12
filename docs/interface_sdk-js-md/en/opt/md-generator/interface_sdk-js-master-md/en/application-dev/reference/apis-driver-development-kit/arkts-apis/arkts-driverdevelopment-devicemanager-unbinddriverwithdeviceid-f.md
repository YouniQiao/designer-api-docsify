# unbindDriverWithDeviceId

## Modules to Import

```TypeScript
import { deviceManager } from '@kit.DriverDevelopmentKit';
```

## unbindDriverWithDeviceId

```TypeScript
function unbindDriverWithDeviceId(deviceId: number): Promise<number>
```

Unbinds a peripheral device. This API uses a promise to return the result.

**Since:** 19

**Required permissions:** ohos.permission.ACCESS_DDK_DRIVERS

<!--Device-deviceManager-function unbindDriverWithDeviceId(deviceId: long): Promise<int>--><!--Device-deviceManager-function unbindDriverWithDeviceId(deviceId: long): Promise<int>-End-->

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
| [26300001](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-driverdevelopment-kit/errorcode-deviceManager.md#26300001-externaldevicemanager-service-exception) |
| [26300003](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-driverdevelopment-kit/errorcode-deviceManager.md#26300003-driver-client-not-bound-to-any-driver-server) |
| [201](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#201-permission-denied) |

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
