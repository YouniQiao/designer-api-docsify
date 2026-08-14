# getPointerSize (System API)

## Modules to Import

```TypeScript
import { pointer } from 'pointer';
```

## getPointerSize

```TypeScript
function getPointerSize(callback: AsyncCallback<int>): void
```

Obtains the current mouse pointer size. This API uses an asynchronous callback to return the result.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-pointer-function getPointerSize(callback: AsyncCallback<int>): void--><!--Device-pointer-function getPointerSize(callback: AsyncCallback<int>): void-End-->

**System capability:** SystemCapability.MultimodalInput.Input.Pointer

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;int&gt; | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined**, and **number** is the obtained mouse pointer size (value range: [1-7]). Otherwise, **err** is an error object. |

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
            pointer.getPointerSize((error: BusinessError, size: number) => {
              if (error) {
                console.error(`getPointerSize error: ${JSON.stringify(error, [`code`, `message`])}`);
              } else {
                console.info(`getPointerSize success, size: ${JSON.stringify(size)}`);
              }
            });
          } catch (error) {
            console.error(`getPointerSize failed, error: ${JSON.stringify(error, [`code`, `message`])}`);
          }
        })
    }
  }
}
```


## getPointerSize

```TypeScript
function getPointerSize(): Promise<int>
```

Obtains the current mouse pointer size. This API uses a promise to return the result.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-pointer-function getPointerSize(): Promise<int>--><!--Device-pointer-function getPointerSize(): Promise<int>-End-->

**System capability:** SystemCapability.MultimodalInput.Input.Pointer

**System API:** This is a system API.

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;int&gt; | Promise used to return the mouse pointer size. The value ranges from 1 to 7. |

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
            pointer.getPointerSize().then((size: number) => {
              console.info(`getPointerSize success, size: ${JSON.stringify(size)}`);
            }).catch((error: BusinessError) => {
              console.error(`Get pointer size failed, error: ${JSON.stringify(error, [`code`, `message`])}`);
            })
          } catch (error) {
            console.error(`getPointerSize failed, error: ${JSON.stringify(error, [`code`, `message`])}`);
          }
        })
    }
  }
}
```

