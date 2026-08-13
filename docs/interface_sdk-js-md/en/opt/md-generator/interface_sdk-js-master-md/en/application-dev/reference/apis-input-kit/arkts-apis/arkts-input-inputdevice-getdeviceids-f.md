# getDeviceIds

## Modules to Import

```TypeScript
import { inputDevice } from '@kit.InputKit';
```

## getDeviceIds

```TypeScript
function getDeviceIds(callback: AsyncCallback<Array<number>>): void
```

Obtains the IDs of all input devices. This API uses an asynchronous callback to return the result. > **NOTE：**> > This API is supported since API version 8 and deprecated since API version 9. Use > [inputDevice.getDeviceList](arkts-input-inputdevice-getdevicelist-f.md#getDeviceList) instead.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [getDeviceList](arkts-input-inputdevice-getdevicelist-f.md#getDeviceList)

<!--Device-inputDevice-function getDeviceIds(callback: AsyncCallback<Array<number>>): void--><!--Device-inputDevice-function getDeviceIds(callback: AsyncCallback<Array<number>>): void-End-->

**System capability:** SystemCapability.MultimodalInput.Input.InputDevice

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;number&gt;&gt; | Yes |

## Examples

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
          // Obtaining the Input Device ID List
          inputDevice.getDeviceIds((error: BusinessError, ids: Array<number>) => {
            if (error) {
              console.error(`Failed to get device id list, Code: ${(error as BusinessError).code}, message: ${(error as BusinessError).message}.`);
              return;
            }
            console.info(`Succeeded in getting device id list: ${JSON.stringify(ids)}.`);
          });
        })
    }
  }
}
```


## getDeviceIds

```TypeScript
function getDeviceIds(): Promise<Array<number>>
```

Obtains the IDs of all input devices. This API uses a promise to return the result. > **NOTE：**> > This API is supported since API version 8 and deprecated since API version 9. Use > [inputDevice.getDeviceList](arkts-input-inputdevice-getdevicelist-f.md#getDeviceList) instead.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [getDeviceList](arkts-input-inputdevice-getdevicelist-f.md#getDeviceList)

<!--Device-inputDevice-function getDeviceIds(): Promise<Array<number>>--><!--Device-inputDevice-function getDeviceIds(): Promise<Array<number>>-End-->

**System capability:** SystemCapability.MultimodalInput.Input.InputDevice

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;Array & lt;number & gt; & gt; |

## Examples

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
          // Obtaining the Input Device ID List
          inputDevice.getDeviceIds().then((ids: Array<number>) => {
            console.info(`Succeeded in getting device id list: ${JSON.stringify(ids)}.`);
          }).catch((error: BusinessError) => {
            console.error(`Failed to get device id list, Code: ${(error as BusinessError).code}, message: ${(error as BusinessError).message}.`);
          })
        })
    }
  }
}
```
