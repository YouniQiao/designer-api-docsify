# getTouchpadScrollDirection (System API)

## Modules to Import

```TypeScript
import { pointer } from '@kit.InputKit';
```

## getTouchpadScrollDirection

```TypeScript
function getTouchpadScrollDirection(callback: AsyncCallback<boolean>): void
```

Obtains the touchpad scroll direction. This API uses an asynchronous callback to return the result.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-pointer-function getTouchpadScrollDirection(callback: AsyncCallback<boolean>): void--><!--Device-pointer-function getTouchpadScrollDirection(callback: AsyncCallback<boolean>): void-End-->

**System capability:** SystemCapability.MultimodalInput.Input.Pointer

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;boolean&gt; | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined**, and **state** indicates whether the touchpad scroll direction matches the direction of finger movement (**true** indicates yes). Otherwise, **err** is an error object. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; &lt;br&gt;2. Incorrect parameter types; 3. Parameter verification failed. |
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
            pointer.getTouchpadScrollDirection ((error: BusinessError, state: boolean) => {
              console.info(`getTouchpadScrollDirection success, state: ${JSON.stringify(state)}`);
            });
          } catch (error) {
            console.error(`getTouchpadScrollDirection failed, error: ${JSON.stringify(error, [`code`, `message`])}`);
          }
        })
    }
  }
}
```


## getTouchpadScrollDirection

```TypeScript
function getTouchpadScrollDirection(): Promise<boolean>
```

Obtains the scroll direction of the touchpad. This API uses a promise to return the result.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-pointer-function getTouchpadScrollDirection(): Promise<boolean>--><!--Device-pointer-function getTouchpadScrollDirection(): Promise<boolean>-End-->

**System capability:** SystemCapability.MultimodalInput.Input.Pointer

**System API:** This is a system API.

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;boolean&gt; | Promise used to return the result. The value **true** indicates that the touchpad scroll direction matches the direction of finger movement, and the value **false** indicates the opposite. The default value is **true**. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; &lt;br&gt;2. Incorrect parameter types; 3. Parameter verification failed. |
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
            pointer.getTouchpadScrollDirection().then((state: boolean) => {
              console.info(`getTouchpadScrollDirection success, state: ${JSON.stringify(state)}`);
            }).catch((error: BusinessError) => {
              console.error(`Get touchpad scroll direction failed, error: ${JSON.stringify(error, [`code`, `message`])}`);
            })
          } catch (error) {
            console.error(`getTouchpadScrollDirection failed, error: ${JSON.stringify(error, [`code`, `message`])}`);
          }
        })
    }
  }
}
```

