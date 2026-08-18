# setKeyboardRepeatRate (System API)

## Modules to Import

```TypeScript
import { inputDevice } from '@kit.InputKit';
import { inputDeviceCooperate } from '@kit.InputKit';
```

## setKeyboardRepeatRate

```TypeScript
function setKeyboardRepeatRate(rate: int, callback: AsyncCallback<void>): void
```

Sets the keyboard repeat rate. This API uses an asynchronous callback to return the result.

**Since:** 23

<!--Device-inputDevice-function setKeyboardRepeatRate(rate: int, callback: AsyncCallback<void>): void--><!--Device-inputDevice-function setKeyboardRepeatRate(rate: int, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.MultimodalInput.Input.InputDevice

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| rate | int | Yes | Keyboard repeat rate, in ms/time. The value range is [36, 100] and the default value is 50. |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined**. Otherwise, **err** is an error object. |

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
            inputDevice.setKeyboardRepeatRate(60, (error: BusinessError) => {
              if (error) {
                console.error(`Set keyboard repeat rate failed, error: ${JSON.stringify(error, [`code`, `message`])}`);
                return;
              }
              console.info(`Set keyboard repeat rate success`);
            });
          } catch (error) {
            console.error(`Set keyboard repeat rate failed, error: ${JSON.stringify(error, [`code`, `message`])}`);
          }
        })
    }
  }
}
```


## setKeyboardRepeatRate

```TypeScript
function setKeyboardRepeatRate(rate: int): Promise<void>
```

Sets the keyboard repeat rate. This API uses a promise to return the result.

**Since:** 23

<!--Device-inputDevice-function setKeyboardRepeatRate(rate: int): Promise<void>--><!--Device-inputDevice-function setKeyboardRepeatRate(rate: int): Promise<void>-End-->

**System capability:** SystemCapability.MultimodalInput.Input.InputDevice

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| rate | int | Yes | Keyboard repeat rate, in ms/time. The value range is [36, 100] and the default value is 50. |

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
            inputDevice.setKeyboardRepeatRate(60).then(() => {
              console.info(`Set keyboard repeat rate success`);
            }).catch((error: BusinessError) => {
              console.error(`Set keyboard failed, error: ${JSON.stringify(error, [`code`, `message`])}`);
            })
          } catch (error) {
            console.error(`Set keyboard repeat rate failed, error: ${JSON.stringify(error, [`code`, `message`])}`);
          }
        })
    }
  }
}
```

