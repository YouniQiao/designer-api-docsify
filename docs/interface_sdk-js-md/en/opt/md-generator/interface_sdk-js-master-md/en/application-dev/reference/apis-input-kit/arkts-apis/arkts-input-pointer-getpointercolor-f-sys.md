# getPointerColor (System API)

## Modules to Import

```TypeScript
import { pointer } from '@kit.InputKit';
```

## getPointerColor

```TypeScript
function getPointerColor(callback: AsyncCallback<number>): void
```

Obtains the mouse pointer color. This API uses an asynchronous callback to return the result.

**Since:** 23

**Deprecated since:** -1

<!--Device-pointer-function getPointerColor(callback: AsyncCallback<int>): void--><!--Device-pointer-function getPointerColor(callback: AsyncCallback<int>): void-End-->

**System capability:** SystemCapability.MultimodalInput.Input.Pointer

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;number&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

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
            // Obtain the mouse pointer color.
            pointer.getPointerColor((error: BusinessError, color: number) => {
              if (error) {
                console.error(`Failed to get pointer color, Code: ${(error as BusinessError).code}, message: ${(error as BusinessError).message}.`);
              } else {
                console.info(`Succeeded in getting pointer color, color: ${JSON.stringify(color)}.`);
              }
            });
          } catch (error) {
            console.error(`Failed to get pointer color, Code: ${(error as BusinessError).code}, message: ${(error as BusinessError).message}.`);
          }
        })
    }
  }
}
```


## getPointerColor

```TypeScript
function getPointerColor(): Promise<number>
```

Obtains the current mouse pointer color. This API uses a promise to return the result.

**Since:** 23

**Deprecated since:** -1

<!--Device-pointer-function getPointerColor(): Promise<int>--><!--Device-pointer-function getPointerColor(): Promise<int>-End-->

**System capability:** SystemCapability.MultimodalInput.Input.Pointer

**System API:** This is a system API.

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;number & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

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
            // Obtain the mouse pointer color.
            pointer.getPointerColor().then((color: number) => {
              console.info(`Succeeded in getting pointer color, color: ${JSON.stringify(color)}.`);
            }).catch((error: BusinessError) => {
              console.error(`Failed to get pointer color, Code: ${(error as BusinessError).code}, message: ${(error as BusinessError).message}.`);
            })
          } catch (error) {
            console.error(`Failed to get pointer color, Code: ${(error as BusinessError).code}, message: ${(error as BusinessError).message}.`);
          }
        })
    }
  }
}
```
