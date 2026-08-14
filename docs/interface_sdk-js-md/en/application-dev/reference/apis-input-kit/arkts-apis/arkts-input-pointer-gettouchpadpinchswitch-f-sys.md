# getTouchpadPinchSwitch (System API)

## Modules to Import

```TypeScript
import { pointer } from 'pointer';
```

## getTouchpadPinchSwitch

```TypeScript
function getTouchpadPinchSwitch(callback: AsyncCallback<boolean>): void
```

Obtains the touchpad pinch switch state. This API uses an asynchronous callback to return the result.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-pointer-function getTouchpadPinchSwitch(callback: AsyncCallback<boolean>): void--><!--Device-pointer-function getTouchpadPinchSwitch(callback: AsyncCallback<boolean>): void-End-->

**System capability:** SystemCapability.MultimodalInput.Input.Pointer

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;boolean&gt; | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined**, and **state** indicates whether the touchpad pinch switch is enabled (**true** indicates yes and **false** indicates no; default value: **true**). Otherwise, **err** is an error object. |

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
            pointer.getTouchpadPinchSwitch((error: BusinessError, state: boolean) => {
              if (error) {
                console.error(`getTouchpadPinchSwitch error: ${JSON.stringify(error, [`code`, `message`])}`);
              } else {
                console.info(`getTouchpadPinchSwitch success, state: ${JSON.stringify(state)}`);
              }
            });
          } catch (error) {
            console.error(`getTouchpadPinchSwitch failed, error: ${JSON.stringify(error, [`code`, `message`])}`);
          }
        })
    }
  }
}
```


## getTouchpadPinchSwitch

```TypeScript
function getTouchpadPinchSwitch(): Promise<boolean>
```

Obtains the touchpad pinch switch state. This API uses a promise to return the result.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-pointer-function getTouchpadPinchSwitch(): Promise<boolean>--><!--Device-pointer-function getTouchpadPinchSwitch(): Promise<boolean>-End-->

**System capability:** SystemCapability.MultimodalInput.Input.Pointer

**System API:** This is a system API.

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;boolean&gt; | Promise used to return the result. The value **true** indicates that the touchpad pinch switch is enabled, and the value **false** indicates that the touchpad pinch switch is disabled. The default value is **true**. |

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
            pointer.getTouchpadPinchSwitch().then((state: boolean) => {
              console.info(`getTouchpadPinchSwitch success, state: ${JSON.stringify(state)}`);
            }).catch((error: BusinessError) => {
              console.error(`Get touchpad pinch switch failed, error: ${JSON.stringify(error, [`code`, `message`])}`);
            })
          } catch (error) {
            console.error(`getTouchpadPinchSwitch failed, error: ${JSON.stringify(error, [`code`, `message`])}`);
          }
        })
    }
  }
}
```

