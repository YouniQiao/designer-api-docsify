# getHoverScrollState (System API)

## Modules to Import

```TypeScript
import { pointer } from '@kit.InputKit';
```

## getHoverScrollState

```TypeScript
function getHoverScrollState(callback: AsyncCallback<boolean>): void
```

Obtains the mouse hover scrolling switch state. This API uses an asynchronous callback to return the result.

**Since:** 23

**Deprecated since:** -1

<!--Device-pointer-function getHoverScrollState(callback: AsyncCallback<boolean>): void--><!--Device-pointer-function getHoverScrollState(callback: AsyncCallback<boolean>): void-End-->

**System capability:** SystemCapability.MultimodalInput.Input.Pointer

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;boolean&gt; | Yes |

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
            // Obtain the mouse hover scrolling switch state.
            pointer.getHoverScrollState((error: BusinessError, state: boolean) => {
              if (error) {
                console.error(`Failed to get mouse hover scroll, Code: ${(error as BusinessError).code}, message: ${(error as BusinessError).message}.`);
              } else {
                console.info(`Succeeded in getting mouse hover scroll, state: ${JSON.stringify(state)}.`);
              }
            });
          } catch (error) {
            console.error(`Failed to get mouse hover scroll, Code: ${(error as BusinessError).code}, message: ${(error as BusinessError).message}.`);
          }
        })
    }
  }
}
```


## getHoverScrollState

```TypeScript
function getHoverScrollState(): Promise<boolean>
```

Obtains the status of the mouse hover scroll switch. This API uses a promise to return the result.

**Since:** 23

**Deprecated since:** -1

<!--Device-pointer-function getHoverScrollState(): Promise<boolean>--><!--Device-pointer-function getHoverScrollState(): Promise<boolean>-End-->

**System capability:** SystemCapability.MultimodalInput.Input.Pointer

**System API:** This is a system API.

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;boolean & gt; |

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
            // Obtain the mouse hover scrolling switch state.
            pointer.getHoverScrollState().then((state: boolean) => {
              console.info(`Succeeded in getting mouse hover scroll, state: ${JSON.stringify(state)}.`);
            }).catch((error: BusinessError) => {
              console.error(`Failed to get mouse hover scroll, Code: ${(error as BusinessError).code}, message: ${(error as BusinessError).message}.`);
            })
          } catch (error) {
            console.error(`Failed to get mouse hover scroll, Code: ${(error as BusinessError).code}, message: ${(error as BusinessError).message}.`);
          }
        })
    }
  }
}
```
