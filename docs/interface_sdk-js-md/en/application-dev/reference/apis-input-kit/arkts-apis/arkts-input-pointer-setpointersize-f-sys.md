# setPointerSize (System API)

## Modules to Import

```TypeScript
import { pointer } from '@kit.InputKit';
```

## setPointerSize

```TypeScript
function setPointerSize(size: int, callback: AsyncCallback<void>): void
```

Sets the mouse pointer size. This API uses an asynchronous callback to return the result.

**Since:** 23

<!--Device-pointer-function setPointerSize(size: int, callback: AsyncCallback<void>): void--><!--Device-pointer-function setPointerSize(size: int, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.MultimodalInput.Input.Pointer

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| size | int | Yes | Pointer size. The value ranges from **1** to **7**. The default value is **1**. |
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
            pointer.setPointerSize(1, (error: BusinessError) => {
              if (error) {
                console.error(`setPointerSize failed, error: ${JSON.stringify(error, [`code`, `message`])}`);
                return;
              }
              console.info(`setPointerSize success`);
            });
          } catch (error) {
            console.error(`setPointerSize failed, error: ${JSON.stringify(error, [`code`, `message`])}`);
          }
        })
    }
  }
}
```


## setPointerSize

```TypeScript
function setPointerSize(size: int): Promise<void>
```

Sets the mouse pointer size. This API uses a promise to return the result.

**Since:** 23

<!--Device-pointer-function setPointerSize(size: int): Promise<void>--><!--Device-pointer-function setPointerSize(size: int): Promise<void>-End-->

**System capability:** SystemCapability.MultimodalInput.Input.Pointer

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| size | int | Yes | Pointer size. The value ranges from **1** to **7**. The default value is **1**. |

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
            pointer.setPointerSize(3).then(() => {
              console.info(`setPointerSize success`);
            }).catch((error: BusinessError) => {
              console.error(`Set pointer size failed, error: ${JSON.stringify(error, [`code`, `message`])}`);
            })
          } catch (error) {
            console.error(`setPointerSize failed, error: ${JSON.stringify(error, [`code`, `message`])}`);
          }
        })
    }
  }
}
```

