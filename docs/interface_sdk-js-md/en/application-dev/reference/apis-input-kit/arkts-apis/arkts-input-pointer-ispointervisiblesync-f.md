# isPointerVisibleSync

## Modules to Import

```TypeScript
import { pointer } from '@kit.InputKit';
```

## isPointerVisibleSync

```TypeScript
function isPointerVisibleSync(): boolean
```

Checks whether the mouse pointer is visible in the current window. This API returns the result synchronously.

**Since:** 23

<!--Device-pointer-function isPointerVisibleSync(): boolean--><!--Device-pointer-function isPointerVisibleSync(): boolean-End-->

**System capability:** SystemCapability.MultimodalInput.Input.Pointer

**Return value:**

| Type | Description |
| --- | --- |
| boolean | Visible status of the mouse pointer. The value **true** indicates that the mouse pointer is visible, and the value **false** indicates the opposite. |

**Examples**

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
            let visible: boolean = pointer.isPointerVisibleSync();
            console.info(`Get pointer visible success, visible: ${JSON.stringify(visible)}`);
          } catch (error) {
            console.error(`Get pointer visible failed, error: ${JSON.stringify(error, [`code`, `message`])}`);
          }
        })
    }
  }
}
```

