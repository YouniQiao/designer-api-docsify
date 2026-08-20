# getKeyboardRepeatRate (System API)

## Modules to Import

```TypeScript
import { inputDevice } from '@kit.InputKit';
import { inputDeviceCooperate } from '@kit.InputKit';
```

## getKeyboardRepeatRate

```TypeScript
function getKeyboardRepeatRate(callback: AsyncCallback<int>): void
```

Obtains the keyboard repeat rate. This API uses an asynchronous callback to return the result.

**Since:** 23

<!--Device-inputDevice-function getKeyboardRepeatRate(callback: AsyncCallback<int>): void--><!--Device-inputDevice-function getKeyboardRepeatRate(callback: AsyncCallback<int>): void-End-->

**System capability:** SystemCapability.MultimodalInput.Input.InputDevice

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-asynccallback-t.md)&lt;int&gt; | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined**, and **data** is the keyboard repeat rate. Otherwise, **err** is an error object. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | SystemAPI permission error. |
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
            inputDevice.getKeyboardRepeatRate((error: BusinessError, rate: number) => {
              if (error) {
                console.error(`Get keyboard repeat rate failed, error: ${JSON.stringify(error, [`code`, `message`])}`);
                return;
              }
              console.info(`Get keyboard repeat rate success`);
            });
          } catch (error) {
            console.error(`Get keyboard repeat rate failed, error: ${JSON.stringify(error, [`code`, `message`])}`);
          }
        })
    }
  }
}
```


## getKeyboardRepeatRate

```TypeScript
function getKeyboardRepeatRate(): Promise<int>
```

Obtains the keyboard repeat rate. This API uses a promise to return the result.

**Since:** 23

<!--Device-inputDevice-function getKeyboardRepeatRate(): Promise<int>--><!--Device-inputDevice-function getKeyboardRepeatRate(): Promise<int>-End-->

**System capability:** SystemCapability.MultimodalInput.Input.InputDevice

**System API:** This is a system API.

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;int&gt; | Promise used to return the keyboard repeat rate. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | SystemAPI permission error. |
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
            inputDevice.getKeyboardRepeatRate().then((rate: number) => {
              console.info(`Get keyboard repeat rate success`);
            }).catch((error: BusinessError) => {
              console.error(`Get keyboard failed, error: ${JSON.stringify(error, [`code`, `message`])}`);
            })
          } catch (error) {
            console.error(`Get keyboard repeat rate failed, error: ${JSON.stringify(error, [`code`, `message`])}`);
          }
        })
    }
  }
}
```

