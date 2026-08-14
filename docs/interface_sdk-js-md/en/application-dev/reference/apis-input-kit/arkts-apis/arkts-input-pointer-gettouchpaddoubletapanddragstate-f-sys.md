# getTouchpadDoubleTapAndDragState (System API)

## Modules to Import

```TypeScript
import { pointer } from 'pointer';
```

## getTouchpadDoubleTapAndDragState

```TypeScript
function getTouchpadDoubleTapAndDragState(callback: AsyncCallback<boolean>): void
```

Obtains the touchpad double-tap and drag switch state. This API uses an asynchronous callback to return the result.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-pointer-function getTouchpadDoubleTapAndDragState(callback: AsyncCallback<boolean>): void--><!--Device-pointer-function getTouchpadDoubleTapAndDragState(callback: AsyncCallback<boolean>): void-End-->

**System capability:** SystemCapability.MultimodalInput.Input.Pointer

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;boolean&gt; | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined**, and **true** is returned if the switch is enabled while **false** is returned if the switch is disabled. Otherwise, **err** is an error object. |

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
            pointer.getTouchpadDoubleTapAndDragState((error: BusinessError, state: boolean) => {
              if (error) {
                console.error(`getTouchpadDoubleTapAndDragState error: ${JSON.stringify(error, [`code`, `message`])}`);
              } else {
                console.info(`getTouchpadDoubleTapAndDragState success, state: ${JSON.stringify(state)}`);
              }
            });
          } catch (error) {
            console.error(`getTouchpadDoubleTapAndDragState failed, error: ${JSON.stringify(error, [`code`, `message`])}`);
          }
        })
    }
  }
}
```


## getTouchpadDoubleTapAndDragState

```TypeScript
function getTouchpadDoubleTapAndDragState(): Promise<boolean>
```

Obtains the touchpad double-tap and drag switch state. This API uses a promise to return the result.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-pointer-function getTouchpadDoubleTapAndDragState(): Promise<boolean>--><!--Device-pointer-function getTouchpadDoubleTapAndDragState(): Promise<boolean>-End-->

**System capability:** SystemCapability.MultimodalInput.Input.Pointer

**System API:** This is a system API.

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;boolean&gt; | Promise used to return the result. The value **true** indicates that the touchpad double-tap and drag switch is enabled, and the value **false** indicates that the touchpad double-tap and drag switch is disabled. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
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
            pointer.getTouchpadDoubleTapAndDragState().then((state) => {
              console.info(`getTouchpadDoubleTapAndDragState success, state: ${JSON.stringify(state)}`);
            }).catch((error: BusinessError) => {
              console.error(`Get touchpad failed, error: ${JSON.stringify(error, [`code`, `message`])}`);
            })
          } catch (error) {
            console.error(`getTouchpadDoubleTapAndDragState failed, error: ${JSON.stringify(error, [`code`, `message`])}`);
          }
        })
    }
  }
}
```

