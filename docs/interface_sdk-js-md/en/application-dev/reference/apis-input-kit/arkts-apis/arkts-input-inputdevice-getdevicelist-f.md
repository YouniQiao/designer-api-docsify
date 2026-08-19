# getDeviceList

## Modules to Import

```TypeScript
import { inputDevice } from '@kit.InputKit';
import { inputDeviceCooperate } from '@kit.InputKit';
```

## getDeviceList

```TypeScript
function getDeviceList(callback: AsyncCallback<Array<int>>): void
```

Obtains the IDs of all input devices. This API uses an asynchronous callback to return the result.

**Since:** 23

<!--Device-inputDevice-function getDeviceList(callback: AsyncCallback<Array<int>>): void--><!--Device-inputDevice-function getDeviceList(callback: AsyncCallback<Array<int>>): void-End-->

**System capability:** SystemCapability.MultimodalInput.Input.InputDevice

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-asynccallback-t.md)&lt;Array&lt;int&gt;&gt; | Yes | Callback function. If the operation is successful, **err** is **undefined**, and **data** is the ID list of all input devices (the ID is the unique identifier of an input device). Otherwise, **err** is an error object. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; <br>2. Incorrect parameter types; 3. Parameter verification failed. |

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
          try {
            inputDevice.getDeviceList((error: BusinessError, ids: Array<number>) => {
              if (error) {
                console.error(`Failed to get device id list, error: ${JSON.stringify(error, [`code`, `message`])}`);
                return;
              }
              console.info(`Device id list: ${JSON.stringify(ids)}`);
            });
          } catch (error) {
            console.error(`Failed to get device id list, error: ${JSON.stringify(error, [`code`, `message`])}`);
          }
        })
    }
  }
}
```


## getDeviceList

```TypeScript
function getDeviceList(): Promise<Array<int>>
```

Obtains the IDs of all input devices. This API uses a promise to return the result.

**Since:** 23

<!--Device-inputDevice-function getDeviceList(): Promise<Array<int>>--><!--Device-inputDevice-function getDeviceList(): Promise<Array<int>>-End-->

**System capability:** SystemCapability.MultimodalInput.Input.InputDevice

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;Array&lt;int&gt;&gt; | Promise used to return the IDs of all input devices. The ID is the unique ID of an input device. |

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
          try {
            inputDevice.getDeviceList().then((ids: Array<number>) => {
              console.info(`Device id list: ${JSON.stringify(ids)}`);
            }).catch((error: BusinessError) => {
              console.error(`Failed to get device id list, error: ${JSON.stringify(error, [`code`, `message`])}`);
            });
          } catch (error) {
            console.error(`Failed to get device id list, error: ${JSON.stringify(error, [`code`, `message`])}`);
          }
        })
    }
  }
}
```

