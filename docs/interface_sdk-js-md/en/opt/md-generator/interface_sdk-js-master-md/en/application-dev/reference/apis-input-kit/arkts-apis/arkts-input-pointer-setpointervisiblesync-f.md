# setPointerVisibleSync

## Modules to Import

```TypeScript
import { pointer } from '@kit.InputKit';
```

## setPointerVisibleSync

```TypeScript
function setPointerVisibleSync(visible: boolean): void
```

Sets whether the mouse pointer is visible in the current window. This API returns the result synchronously.

**Since:** 23

**Deprecated since:** -1

<!--Device-pointer-function setPointerVisibleSync(visible: boolean): void--><!--Device-pointer-function setPointerVisibleSync(visible: boolean): void-End-->

**System capability:** SystemCapability.MultimodalInput.Input.Pointer

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| visible | boolean | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |

## Examples

```TypeScript
import { pointer } from '@kit.InputKit';

@Entry
@Component
struct Index {
  build() {
    RelativeContainer() {
      Text()
        .onClick(() => {
          try {
            // Synchronously sets the visibility of the mouse pointer
            pointer.setPointerVisibleSync(false);
            console.info(`Succeeded in setting pointer cursor visible.`);
          } catch (error) {
            console.error(`Failed to set pointer cursor visible, Code: ${(error as BusinessError).code}, message: ${(error as BusinessError).message}.`);
          }
        })
    }
  }
}
```
