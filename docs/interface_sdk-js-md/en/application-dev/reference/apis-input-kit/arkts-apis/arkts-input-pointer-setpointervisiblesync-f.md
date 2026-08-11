# setPointerVisibleSync

## Modules to Import

```TypeScript
import { pointer } from 'kits/@kit.InputKit';
```

## setPointerVisibleSync

```TypeScript
function setPointerVisibleSync(visible: boolean): void
```

Sets whether the mouse pointer is visible in the current window. This API returns the result synchronously.

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

<!--Device-pointer-function setPointerVisibleSync(visible: boolean): void--><!--Device-pointer-function setPointerVisibleSync(visible: boolean): void-End-->

**System capability:** SystemCapability.MultimodalInput.Input.Pointer

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| visible | boolean | Yes | Whether the mouse pointer is visible in the current window. The value **true** indicates that the mouse pointer is visible, and the value **false** indicates the opposite. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; &lt;br&gt;2. Incorrect parameter types; 3. Parameter verification failed. |

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
            pointer.setPointerVisibleSync(false);
            console.info(`Set pointer visible success`);
          } catch (error) {
            console.error(`Set pointer visible failed, error: ${JSON.stringify(error, [`code`, `message`])}`);
          }
        })
    }
  }
}
```

