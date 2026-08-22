# getKeyboardRepeatDelay (System API)

## Modules to Import

```TypeScript
import { inputDevice } from '@kit.InputKit';
import { inputDeviceCooperate } from '@kit.InputKit';
```

## getKeyboardRepeatDelay

```TypeScript
function getKeyboardRepeatDelay(callback: AsyncCallback<int>): void
```

Obtains the keyboard repeat delay. This API uses an asynchronous callback to return the result.

**Since:** 23

<!--Device-inputDevice-function getKeyboardRepeatDelay(callback: AsyncCallback<int>): void--><!--Device-inputDevice-function getKeyboardRepeatDelay(callback: AsyncCallback<int>): void-End-->

**System capability:** SystemCapability.MultimodalInput.Input.InputDevice

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;int&gt; | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined**, and **data** is the keyboard repeat rate. Otherwise, **err** is an error object. |

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
            inputDevice.getKeyboardRepeatDelay((error: BusinessError, delay: number) => {
              if (error) {
                console.error(`Get keyboard repeat delay failed, error: ${JSON.stringify(error, [`code`, `message`])}`);
                return;
              }
              console.info(`Get keyboard repeat delay success`);
            });
          } catch (error) {
            console.error(`Get keyboard repeat delay failed, error: ${JSON.stringify(error, [`code`, `message`])}`);
          }
        })
    }
  }
}
```

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
            inputDevice.getKeyboardRepeatDelay().then((delay: number) => {
              console.info(`Get keyboard repeat delay success`);
            }).catch((error: BusinessError) => {
              console.error(`Get keyboard failed, error: ${JSON.stringify(error, [`code`, `message`])}`);
            })
          } catch (error) {
            console.error(`Get keyboard repeat delay failed, error: ${JSON.stringify(error, [`code`, `message`])}`);
          }
        })
    }
  }
}
```


## getKeyboardRepeatDelay

```TypeScript
function getKeyboardRepeatDelay(): Promise<int>
```

Obtains the keyboard repeat delay. This API uses a promise to return the result.

**Since:** 23

<!--Device-inputDevice-function getKeyboardRepeatDelay(): Promise<int>--><!--Device-inputDevice-function getKeyboardRepeatDelay(): Promise<int>-End-->

**System capability:** SystemCapability.MultimodalInput.Input.InputDevice

**System API:** This is a system API.

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;int&gt; | Promise used to return the keyboard repeat delay. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | SystemAPI permission error. |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; <br>2. Incorrect parameter types; 3. Parameter verification failed. |

**Examples**

See [getKeyboardRepeatDelay](#getkeyboardrepeatdelay)

