# setTouchpadPointerSpeed (System API)

## Modules to Import

```TypeScript
import { pointer } from '@kit.InputKit';
```

## setTouchpadPointerSpeed

```TypeScript
function setTouchpadPointerSpeed(speed: int, callback: AsyncCallback<void>): void
```

Sets the touchpad pointer speed. This API uses an asynchronous callback to return the result.

**Since:** 23

<!--Device-pointer-function setTouchpadPointerSpeed(speed: int, callback: AsyncCallback<void>): void--><!--Device-pointer-function setTouchpadPointerSpeed(speed: int, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.MultimodalInput.Input.Pointer

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| speed | int | Yes | Touchpad pointer speed The value range is [1,11]. The default value is **6**. |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-asynccallback-t.md)&lt;void&gt; | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined**. Otherwise, **err** is an error object. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; <br>2. Incorrect parameter types; 3. Parameter verification failed. |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | SystemAPI permission error. |

**Examples**

```TypeScript
import { pointer } from '@kit.InputKit';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct Index {
  build() {
    RelativeContainer() {
      Text()
        .onClick(() => {
          try {
            pointer.setTouchpadPointerSpeed(1, (error: BusinessError) => {
              if (error) {
                console.error(`setTouchpadPointerSpeedfailed, error: ${JSON.stringify(error, [`code`, `message`])}`);
                return;
              }
              console.info(`setTouchpadPointerSpeed success`);
            });
          } catch (error) {
            console.error(`setTouchpadPointerSpeed failed, error: ${JSON.stringify(error, [`code`, `message`])}`);
          }
        })
    }
  }
}
```


## setTouchpadPointerSpeed

```TypeScript
function setTouchpadPointerSpeed(speed: int): Promise<void>
```

Sets the touchpad pointer speed. This API uses a promise to return the result.

**Since:** 23

<!--Device-pointer-function setTouchpadPointerSpeed(speed: int): Promise<void>--><!--Device-pointer-function setTouchpadPointerSpeed(speed: int): Promise<void>-End-->

**System capability:** SystemCapability.MultimodalInput.Input.Pointer

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| speed | int | Yes | Touchpad pointer speed The value range is [1,11]. The default value is **6**. |

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
import { pointer } from '@kit.InputKit';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct Index {
  build() {
    RelativeContainer() {
      Text()
        .onClick(() => {
          try {
            pointer.setTouchpadPointerSpeed(10).then(() => {
              console.info(`setTouchpadPointerSpeed success`);
            }).catch((error: BusinessError) => {
              console.error(`Set touchpad pointer speed failed, error: ${JSON.stringify(error, [`code`, `message`])}`);
            })
          } catch (error) {
            console.error(`setTouchpadPointerSpeed failed, error: ${JSON.stringify(error, [`code`, `message`])}`);
          }
        })
    }
  }
}
```

