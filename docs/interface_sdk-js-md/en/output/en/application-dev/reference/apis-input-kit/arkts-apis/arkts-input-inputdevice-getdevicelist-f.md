# getDeviceList

## getDeviceList

```TypeScript
function getDeviceList(callback: AsyncCallback<Array<int>>): void
```

Obtains the IDs of all input devices. This API uses an asynchronous callback to return the result.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-inputDevice-function getDeviceList(callback: AsyncCallback<Array<int>>): void--><!--Device-inputDevice-function getDeviceList(callback: AsyncCallback<Array<int>>): void-End-->

**System capability:** SystemCapability.MultimodalInput.Input.InputDevice

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | ArkTS-Dyn: \_\_\_MD\_LINK\_USD\_0\_\_\_&lt;Array&lt;number&gt;&gt;  \_\_\_HTML\_TAG\_USD\_2\_\_\_ArkTS-Sta：\_\_\_MD\_LINK\_USD\_1\_\_\_&lt;Array&lt;int&gt;&gt; | Yes | Callback function. If the operation is successful, **err** is **undefined**, and **data** is the ID list of all input devices (the ID is the unique identifier of an input device). Otherwise, **err** is an error object. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_HTML\_\_\_ESCAPED\_UNDERSCORE\_\_\_TAG\_\_\_ESCAPED\_UNDERSCORE\_\_\_DESC\_\_\_ESCAPED\_UNDERSCORE\_\_\_USD\_\_\_ESCAPED\_UNDERSCORE\_\_\_0\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_2. Incorrect parameter types; 3. Parameter verification failed. |

**Example**

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

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-inputDevice-function getDeviceList(): Promise<Array<int>>--><!--Device-inputDevice-function getDeviceList(): Promise<Array<int>>-End-->

**System capability:** SystemCapability.MultimodalInput.Input.InputDevice

**Return value:**

| Type | Description |
| --- | --- |
| ArkTS-Dyn: Promise&lt;Array&lt;number&gt;&gt;  \_\_\_HTML\_TAG\_USD\_0\_\_\_ArkTS-Sta：Promise&lt;Array&lt;int&gt;&gt; | Promise used to return the IDs of all input devices. The ID is the unique ID of an |

**Example**

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

