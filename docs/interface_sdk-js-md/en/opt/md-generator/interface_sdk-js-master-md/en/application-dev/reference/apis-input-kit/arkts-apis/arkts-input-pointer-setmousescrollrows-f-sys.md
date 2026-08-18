# setMouseScrollRows (System API)

## Modules to Import

```TypeScript
```

## setMouseScrollRows

```TypeScript
function setMouseScrollRows(rows: number, callback: AsyncCallback<void>): void
```

Sets the number of mouse scroll lines. This API uses an asynchronous callback to return the result.

**Since:** 23

<!--Device-pointer-function setMouseScrollRows(rows: int, callback: AsyncCallback<void>): void--><!--Device-pointer-function setMouseScrollRows(rows: int, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.MultimodalInput.Input.Pointer

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| rows | number | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

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
            // Set the number of mouse scroll lines.
            pointer.setMouseScrollRows(1, (error: BusinessError) => {
              if (error) {
                console.error(`Failed to set mouse scroll rows, Code: ${(error as BusinessError).code}, message: ${(error as BusinessError).message}.`);
                return;
              }
              console.info(`Succeeded in setting mouse scroll rows.`);
            });
          } catch (error) {
            console.error(`Failed to set mouse scroll rows, Code: ${(error as BusinessError).code}, message: ${(error as BusinessError).message}.`);
          }
        })
    }
  }
}
```


## setMouseScrollRows

```TypeScript
function setMouseScrollRows(rows: number): Promise<void>
```

Sets the number of mouse scroll lines. This API uses a promise to return the result.

**Since:** 23

<!--Device-pointer-function setMouseScrollRows(rows: int): Promise<void>--><!--Device-pointer-function setMouseScrollRows(rows: int): Promise<void>-End-->

**System capability:** SystemCapability.MultimodalInput.Input.Pointer

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| rows | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

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
            // Set the number of mouse scroll lines.
            pointer.setMouseScrollRows(20).then(() => {
              console.info(`Succeeded in setting mouse scroll rows.`);
            }).catch((error: BusinessError) => {
              console.error(`Failed to set mouse scroll rows, Code: ${(error as BusinessError).code}, message: ${(error as BusinessError).message}.`);
            })
          } catch (error) {
            console.error(`Failed to set mouse scroll rows, Code: ${(error as BusinessError).code}, message: ${(error as BusinessError).message}.`);
          }
        })
    }
  }
}
```
