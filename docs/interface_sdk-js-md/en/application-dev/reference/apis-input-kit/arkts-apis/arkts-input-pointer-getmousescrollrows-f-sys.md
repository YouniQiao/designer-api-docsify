# getMouseScrollRows (System API)

## Modules to Import

```TypeScript
import { pointer } from '@kit.InputKit';
```

## getMouseScrollRows

```TypeScript
function getMouseScrollRows(callback: AsyncCallback<int>): void
```

Obtains the number of mouse scroll lines. This API uses an asynchronous callback to return the result.

**Since:** 23

<!--Device-pointer-function getMouseScrollRows(callback: AsyncCallback<int>): void--><!--Device-pointer-function getMouseScrollRows(callback: AsyncCallback<int>): void-End-->

**System capability:** SystemCapability.MultimodalInput.Input.Pointer

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-asynccallback-t.md)&lt;int&gt; | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined**, and **number** is the number of mouse scroll lines. Otherwise, **err** is an error object. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | SystemAPI permission error. |
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
            pointer.getMouseScrollRows((error: BusinessError, rows: number) => {
              if (error) {
                console.error(`getMouseScrollRows error: ${JSON.stringify(error, [`code`, `message`])}`);
              } else {
                console.info(`getMouseScrollRows success, rows: ${JSON.stringify(rows)}`);
              }
            });
          } catch (error) {
            console.error(`getMouseScrollRows failed, error: ${JSON.stringify(error, [`code`, `message`])}`);
          }
        })
    }
  }
}
```


## getMouseScrollRows

```TypeScript
function getMouseScrollRows(): Promise<int>
```

Obtains the number of mouse scroll lines. This API uses a promise to return the result.

**Since:** 23

<!--Device-pointer-function getMouseScrollRows(): Promise<int>--><!--Device-pointer-function getMouseScrollRows(): Promise<int>-End-->

**System capability:** SystemCapability.MultimodalInput.Input.Pointer

**System API:** This is a system API.

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;int&gt; | Promise used to return the number of mouse scroll lines. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | SystemAPI permission error. |
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
            pointer.getMouseScrollRows().then((rows: number) => {
              console.info(`getMouseScrollRows success, rows: ${JSON.stringify(rows)}`);
            }).catch((error: BusinessError) => {
              console.error(`Get mouse scroll rows failed, error: ${JSON.stringify(error, [`code`, `message`])}`);
            })
          } catch (error) {
            console.error(`getMouseScrollRows failed, error: ${JSON.stringify(error, [`code`, `message`])}`);
          }
        })
    }
  }
}
```

