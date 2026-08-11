# getKeyboardType

## Modules to Import

```TypeScript
import { inputDevice } from 'kits/@kit.InputKit';
```

## getKeyboardType

```TypeScript
function getKeyboardType(deviceId: int, callback: AsyncCallback<KeyboardType>): void
```

Obtains the keyboard type of the input device, such as full keyboard and numeric keypad. The keyboard type of the input device is subject to the result returned by this API. This API uses an asynchronous callback to return the result.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-inputDevice-function getKeyboardType(deviceId: int, callback: AsyncCallback<KeyboardType>): void--><!--Device-inputDevice-function getKeyboardType(deviceId: int, callback: AsyncCallback<KeyboardType>): void-End-->

**System capability:** SystemCapability.MultimodalInput.Input.InputDevice

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| deviceId | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | Unique ID of the input device. If a physical device is repeatedly reinstalled or restarted, its ID may change. |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;KeyboardType&gt; | Yes | Callback function. If the query is successful, **err** is **undefined**, and **data** is the keyboard type of the input device. Otherwise, **err** is an error object. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; &lt;br&gt;2. Incorrect parameter types; 3. Parameter verification failed. |

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
          // Query the keyboard type of the input device whose ID is 1.
          try {
            inputDevice.getKeyboardType(1, (error: BusinessError, type: number) => {
              if (error) {
                console.error(`Failed to get keyboard type, error: ${JSON.stringify(error, [`code`, `message`])}`);
                return;
              }
              console.info(`Keyboard type: ${JSON.stringify(type)}`);
            });
          } catch (error) {
            console.error(`Failed to get keyboard type, error: ${JSON.stringify(error, [`code`, `message`])}`);
          }
        })
    }
  }
}
```


## getKeyboardType

```TypeScript
function getKeyboardType(deviceId: int): Promise<KeyboardType>
```

Obtains the keyboard type of an input device. This API uses a promise to return the result.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-inputDevice-function getKeyboardType(deviceId: int): Promise<KeyboardType>--><!--Device-inputDevice-function getKeyboardType(deviceId: int): Promise<KeyboardType>-End-->

**System capability:** SystemCapability.MultimodalInput.Input.InputDevice

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| deviceId | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | Unique ID of the input device. If a physical device is repeatedly reinstalled or restarted, its ID may change. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;KeyboardType&gt; | Promise used to return the keyboard type of the input device. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; &lt;br&gt;2. Incorrect parameter types; 3. Parameter verification failed. |

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
          // Query the keyboard type of the input device whose ID is 1.
          try {
            inputDevice.getKeyboardType(1).then((type: number) => {
              console.info(`Keyboard type: ${JSON.stringify(type)}`);
            }).catch((error: BusinessError) => {
              console.error(`Get keyboard type failed, error: ${JSON.stringify(error, [`code`, `message`])}`);
            })
          } catch (error) {
            console.error(`Failed to get keyboard type, error: ${JSON.stringify(error, [`code`, `message`])}`);
          }
        })
    }
  }
}
```

