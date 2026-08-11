# unbindDevice

## Modules to Import

```TypeScript
import { deviceManager } from 'kits/@kit.DriverDevelopmentKit';
```

## unbindDevice

```TypeScript
function unbindDevice(deviceId: number, callback: AsyncCallback<number>): void
```

Unbinds a peripheral device.

**Since:** 10

**Deprecated since:** 19

**Substitutes:** [deviceManager.unbindDriverWithDeviceId](arkts-driverdevelopment-devicemanager-unbinddriverwithdeviceid-f.md#unbinddriverwithdeviceid)(deviceId:

**Required permissions:** ohos.permission.ACCESS_EXTENSIONAL_DEVICE_DRIVER

<!--Device-deviceManager-function unbindDevice(deviceId: number, callback: AsyncCallback<number>): void--><!--Device-deviceManager-function unbindDevice(deviceId: number, callback: AsyncCallback<number>): void-End-->

**System capability:** SystemCapability.Driver.ExternalDevice

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| deviceId | number | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;number&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [22900001](../../apis-driverdevelopment-kit/errorcode-deviceManager.md#22900001-externaldevicemanager-service-exception-or-bustype-parameter-error) |

## Examples

```TypeScript
import { deviceManager } from '@kit.DriverDevelopmentKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  // For example, deviceId is 12345678. You can use queryDevices() to obtain the deviceId.
  deviceManager.unbindDevice(12345678, (error : BusinessError, data : number) => {
    if (error) {
      console.error(`unbindDevice async fail. Code is ${error.code}, message is ${error.message}`);
      return;
    }
    console.info(`unbindDevice success`);
  });
} catch (error) {
  console.error(`unbindDevice fail. Code is ${error.code}, message is ${error.message}`);
}
```


## unbindDevice

```TypeScript
function unbindDevice(deviceId: number): Promise<number>
```

Unbinds a peripheral device. This API uses a promise to return the result.

**Since:** 10

**Deprecated since:** 19

**Substitutes:** [deviceManager.unbindDriverWithDeviceId](arkts-driverdevelopment-devicemanager-unbinddriverwithdeviceid-f.md#unbinddriverwithdeviceid)(deviceId:

**Required permissions:** ohos.permission.ACCESS_EXTENSIONAL_DEVICE_DRIVER

<!--Device-deviceManager-function unbindDevice(deviceId: number): Promise<number>--><!--Device-deviceManager-function unbindDevice(deviceId: number): Promise<number>-End-->

**System capability:** SystemCapability.Driver.ExternalDevice

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| deviceId | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;number&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [22900001](../../apis-driverdevelopment-kit/errorcode-deviceManager.md#22900001-externaldevicemanager-service-exception-or-bustype-parameter-error) |

## Examples

```TypeScript
import { deviceManager } from '@kit.DriverDevelopmentKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  // For example, deviceId is 12345678. You can use queryDevices() to obtain the deviceId.
  deviceManager.unbindDevice(12345678).then((data : number) => {
    console.info(`unbindDevice success, Device_Id is ${data}.`);
  }, (error : BusinessError) => {
    console.error(`unbindDevice async fail. Code is ${error.code}, message is ${error.message}`);
  });
} catch (error) {
  console.error(`unbindDevice fail. Code is ${error.code}, message is ${error.message}`);
}
```
