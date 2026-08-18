# getDevice

## Modules to Import

```TypeScript
```

## getDevice

```TypeScript
function getDevice(deviceId: number, callback: AsyncCallback<InputDeviceData>): void
```

Obtains the information about the input device with the specified ID. This API uses an asynchronous callback to return the result. > **NOTE：**> > This API is supported since API version 8 and deprecated since API version 9. Use > [inputDevice.getDeviceInfo](arkts-input-inputdevice-getdeviceinfo-f.md#getdeviceinfo) instead.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** getDeviceInfo

<!--Device-inputDevice-function getDevice(deviceId: number, callback: AsyncCallback<InputDeviceData>): void--><!--Device-inputDevice-function getDevice(deviceId: number, callback: AsyncCallback<InputDeviceData>): void-End-->

**System capability:** SystemCapability.MultimodalInput.Input.InputDevice

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| deviceId | number | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[InputDeviceData](arkts-input-inputdevice-inputdevicedata-i.md)&gt; | Yes |

**Examples**

```TypeScript
import { inputDevice } from '@kit.InputKit';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct Index {
  build() {
    RelativeContainer() {
      Text()
        .onClick(() => {
          // Obtain the name of the device whose ID is 1.
          inputDevice.getDevice(1, (error: BusinessError, deviceData: inputDevice.InputDeviceData) => {
            if (error) {
              console.error(`Failed to get device info, Code: ${(error as BusinessError).code}, message: ${(error as BusinessError).message}.`);
              return;
            }
            console.info(`Succeeded in getting device info: ${JSON.stringify(deviceData)}.`);
          });
        })
    }
  }
}
```


## getDevice

```TypeScript
function getDevice(deviceId: number): Promise<InputDeviceData>
```

Obtains the information about the input device with the specified ID. This API uses a promise to return the result. > **NOTE：**> > This API is supported since API version 8 and deprecated since API version 9. Use > [inputDevice.getDeviceInfo](arkts-input-inputdevice-getdeviceinfo-f.md#getdeviceinfo) instead.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** getDeviceInfo

<!--Device-inputDevice-function getDevice(deviceId: number): Promise<InputDeviceData>--><!--Device-inputDevice-function getDevice(deviceId: number): Promise<InputDeviceData>-End-->

**System capability:** SystemCapability.MultimodalInput.Input.InputDevice

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| deviceId | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[InputDeviceData](arkts-input-inputdevice-inputdevicedata-i.md)&gt; |

**Examples**

```TypeScript
import { inputDevice } from '@kit.InputKit';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct Index {
  build() {
    RelativeContainer() {
      Text()
        .onClick(() => {
          // Obtain the name of the device whose ID is 1.
          inputDevice.getDevice(1).then((deviceData: inputDevice.InputDeviceData) => {
            console.info(`Succeeded in getting device info: ${JSON.stringify(deviceData)}.`);
          }).catch((error: BusinessError) => {
            console.error(`Failed to get device info, Code: ${(error as BusinessError).code}, message: ${(error as BusinessError).message}.`);
          })
        })
    }
  }
}
```
