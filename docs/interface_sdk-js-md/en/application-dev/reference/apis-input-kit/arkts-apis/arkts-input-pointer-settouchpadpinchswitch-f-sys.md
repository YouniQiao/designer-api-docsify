# setTouchpadPinchSwitch (System API)

## Modules to Import

```TypeScript
import { pointer } from 'pointer';
```

## setTouchpadPinchSwitch

```TypeScript
function setTouchpadPinchSwitch(state: boolean, callback: AsyncCallback<void>): void
```

Sets the touchpad pinch switch. This API uses an asynchronous callback to return the result.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-pointer-function setTouchpadPinchSwitch(state: boolean, callback: AsyncCallback<void>): void--><!--Device-pointer-function setTouchpadPinchSwitch(state: boolean, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.MultimodalInput.Input.Pointer

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| state | boolean | Yes | Touchpad pinch switch state. The value **true** indicates that the switch is enabled, and the value **false** indicates the opposite. The default value is **true**. |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined**. Otherwise, **err** is an error object. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; <br>2. Incorrect parameter types; 3. Parameter verification failed. |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | SystemAPI permission error. |

## Examples

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
            pointer.setTouchpadPinchSwitch(true, (error: BusinessError) => {
              if (error) {
                console.error(`setTouchpadPinchSwitch failed, error: ${JSON.stringify(error, [`code`, `message`])}`);
                return;
              }
              console.info(`setTouchpadPinchSwitch success`);
            });
          } catch (error) {
            console.error(`setTouchpadPinchSwitch failed, error: ${JSON.stringify(error, [`code`, `message`])}`);
          }
        })
    }
  }
}
```


## setTouchpadPinchSwitch

```TypeScript
function setTouchpadPinchSwitch(state: boolean): Promise<void>
```

Sets the touchpad pinch switch. This API uses a promise to return the result.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-pointer-function setTouchpadPinchSwitch(state: boolean): Promise<void>--><!--Device-pointer-function setTouchpadPinchSwitch(state: boolean): Promise<void>-End-->

**System capability:** SystemCapability.MultimodalInput.Input.Pointer

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| state | boolean | Yes | Touchpad pinch switch state. The value **true** indicates that the switch is enabled, and the value **false** indicates the opposite. The default value is **true**. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; <br>2. Incorrect parameter types; 3. Parameter verification failed. |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | SystemAPI permission error. |

## Examples

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
            pointer.setTouchpadPinchSwitch(false).then(() => {
              console.info(`setTouchpadPinchSwitch success`);
            }).catch((error: BusinessError) => {
              console.error(`Set touchpad pinch switch failed, error: ${JSON.stringify(error, [`code`, `message`])}`);
            })
          } catch (error) {
            console.error(`setTouchpadPinchSwitch failed, error: ${JSON.stringify(error, [`code`, `message`])}`);
          }
        })
    }
  }
}
```

