# isPointerVisible

## Modules to Import

```TypeScript
import { pointer } from '@kit.InputKit';
```

## isPointerVisible

```TypeScript
function isPointerVisible(callback: AsyncCallback<boolean>): void
```

Obtains the visible status of the mouse pointer. This API uses an asynchronous callback to return the result.

**Since:** 23

<!--Device-pointer-function isPointerVisible(callback: AsyncCallback<boolean>): void--><!--Device-pointer-function isPointerVisible(callback: AsyncCallback<boolean>): void-End-->

**System capability:** SystemCapability.MultimodalInput.Input.Pointer

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;boolean&gt; | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined**, and **data** is the visible status of the mouse pointer (**true** if visible and **false** if invisible). Otherwise, **err** is an error object. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; <br>2. Incorrect parameter types; 3. Parameter verification failed. |

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
            pointer.isPointerVisible((error: BusinessError, visible: boolean) => {
              if (error) {
                console.error(`Get pointer visible failed, error: ${JSON.stringify(error, [`code`, `message`])}`);
                return;
              }
              console.info(`Get pointer visible success, visible: ${JSON.stringify(visible)}`);
            });
          } catch (error) {
            console.error(`Get pointer visible failed, error: ${JSON.stringify(error, [`code`, `message`])}`);
          }
        })
    }
  }
}
```

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
            pointer.isPointerVisible().then((visible: boolean) => {
              console.info(`Get pointer visible success, visible: ${JSON.stringify(visible)}`);
            }).catch((error: BusinessError) => {
              console.error(`Get pointer failed, error: ${JSON.stringify(error, [`code`, `message`])}`);
            })
          } catch (error) {
            console.error(`Get pointer visible failed, error: ${JSON.stringify(error, [`code`, `message`])}`);
          }
        })
    }
  }
}
```


## isPointerVisible

```TypeScript
function isPointerVisible(): Promise<boolean>
```

Obtains the visible status of the mouse pointer. This API uses a promise to return the result.

**Since:** 23

<!--Device-pointer-function isPointerVisible(): Promise<boolean>--><!--Device-pointer-function isPointerVisible(): Promise<boolean>-End-->

**System capability:** SystemCapability.MultimodalInput.Input.Pointer

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;boolean&gt; | Promise used to return the result. **true** is returned if the mouse pointer is visible; **false** is returned if the mouse pointer is hidden. |

**Examples**

See [isPointerVisible](#ispointervisible)

