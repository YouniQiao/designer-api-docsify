# setTouchpadScrollDirection (System API)

## Modules to Import

```TypeScript
import { pointer } from '@kit.InputKit';
```

## setTouchpadScrollDirection

```TypeScript
function setTouchpadScrollDirection(state: boolean, callback: AsyncCallback<void>): void
```

Sets the touchpad scroll direction. This API uses an asynchronous callback to return the result.

**Since:** 23

**Deprecated since:** -1

<!--Device-pointer-function setTouchpadScrollDirection(state: boolean, callback: AsyncCallback<void>): void--><!--Device-pointer-function setTouchpadScrollDirection(state: boolean, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.MultimodalInput.Input.Pointer

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| state | boolean | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

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
            // Set the touchpad scroll direction.
            pointer.setTouchpadScrollDirection(true, (error: BusinessError) => {
              if (error) {
                console.error(`Failed to set touchpad scroll direction, Code: ${(error as BusinessError).code}, message: ${(error as BusinessError).message}.`);
                return;
              }
              console.info(`Succeeded in setting touchpad scroll direction.`);
            });
          } catch (error) {
            console.error(`Failed to set touchpad scroll direction, Code: ${(error as BusinessError).code}, message: ${(error as BusinessError).message}.`);
          }
        })
    }
  }
}
```


## setTouchpadScrollDirection

```TypeScript
function setTouchpadScrollDirection(state: boolean): Promise<void>
```

Sets the touchpad scroll direction. This API uses a promise to return the result.

**Since:** 23

**Deprecated since:** -1

<!--Device-pointer-function setTouchpadScrollDirection(state: boolean): Promise<void>--><!--Device-pointer-function setTouchpadScrollDirection(state: boolean): Promise<void>-End-->

**System capability:** SystemCapability.MultimodalInput.Input.Pointer

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| state | boolean | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

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
            // Set the touchpad scroll direction.
            pointer.setTouchpadScrollDirection (false).then(() => {
              console.info(`Succeeded in setting touchpad scroll direction.`);
            }).catch((error: BusinessError) => {
              console.error(`Failed to set touchpad scroll direction, Code: ${(error as BusinessError).code}, message: ${(error as BusinessError).message}.`);
            })
          } catch (error) {
            console.error(`Failed to set touchpad scroll direction, Code: ${(error as BusinessError).code}, message: ${(error as BusinessError).message}.`);
          }
        })
    }
  }
}
```
