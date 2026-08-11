# getPointerColorSync (System API)

## Modules to Import

```TypeScript
import { pointer } from 'kits/@kit.InputKit';
```

## getPointerColorSync

```TypeScript
function getPointerColorSync(): int
```

Obtains the pointer color. This API returns the result synchronously.

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

<!--Device-pointer-function getPointerColorSync(): int--><!--Device-pointer-function getPointerColorSync(): int-End-->

**System capability:** SystemCapability.MultimodalInput.Input.Pointer

**System API:** This is a system API.

**Return value:**

| Type | Description |
| --- | --- |
| ArkTS-Dyn: number  <br>ArkTS-Sta：int | Pointer color. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | SystemAPI permission error. |

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
            let pointerColor = pointer.getPointerColorSync();
            console.info(`getPointerColorSync success, pointerColor: ${JSON.stringify(pointerColor)}`);
          } catch (error) {
            console.error(`getPointerColorSync failed, error: ${JSON.stringify(error, [`code`, `message`])}`);
          }
        })
    }
  }
}
```

