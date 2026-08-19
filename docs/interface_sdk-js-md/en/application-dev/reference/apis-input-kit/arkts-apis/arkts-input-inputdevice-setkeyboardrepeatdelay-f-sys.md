# setKeyboardRepeatDelay (System API)

## Modules to Import

```TypeScript
import { inputDevice } from '@kit.InputKit';
import { inputDeviceCooperate } from '@kit.InputKit';
```

## setKeyboardRepeatDelay

```TypeScript
function setKeyboardRepeatDelay(delay: int, callback: AsyncCallback<void>): void
```

Sets the keyboard repeat delay. This API uses an asynchronous callback to return the result.

**Since:** 23

<!--Device-inputDevice-function setKeyboardRepeatDelay(delay: int, callback: AsyncCallback<void>): void--><!--Device-inputDevice-function setKeyboardRepeatDelay(delay: int, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.MultimodalInput.Input.InputDevice

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| delay | int | Yes | Keyboard repeat delay, in ms. The value range is [300, 1000] and the default value is **500**. |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-asynccallback-t.md)&lt;void&gt; | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined**. Otherwise, **err** is an error object. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; <br>2. Incorrect parameter types; 3. Parameter verification failed. |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | SystemAPI permission error. |

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
            inputDevice.setKeyboardRepeatDelay(350, (error: BusinessError) => {
              if (error) {
                console.error(`Set keyboard repeat delay failed, error: ${JSON.stringify(error, [`code`, `message`])}`);
                return;
              }
              console.info(`Set keyboard repeat delay success`);
            });
          } catch (error) {
            console.error(`Set keyboard repeat delay failed, error: ${JSON.stringify(error, [`code`, `message`])}`);
          }
        })
    }
  }
}
```


## setKeyboardRepeatDelay

```TypeScript
function setKeyboardRepeatDelay(delay: int): Promise<void>
```

Sets the keyboard repeat delay. This API uses a promise to return the result.

**Since:** 23

<!--Device-inputDevice-function setKeyboardRepeatDelay(delay: int): Promise<void>--><!--Device-inputDevice-function setKeyboardRepeatDelay(delay: int): Promise<void>-End-->

**System capability:** SystemCapability.MultimodalInput.Input.InputDevice

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| delay | int | Yes | Keyboard repeat delay, in ms. The value range is [300, 1000] and the default value is **500**. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; <br>2. Incorrect parameter types; 3. Parameter verification failed. |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | SystemAPI permission error. |

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
            inputDevice.setKeyboardRepeatDelay(350).then(() => {
              console.info(`Set keyboard repeat delay success`);
            }).catch((error: BusinessError) => {
              console.error(`Set keyboard failed, error: ${JSON.stringify(error, [`code`, `message`])}`);
            })
          } catch (error) {
            console.error(`Set keyboard repeat delay failed, error: ${JSON.stringify(error, [`code`, `message`])}`);
          }
        })
    }
  }
}
```

