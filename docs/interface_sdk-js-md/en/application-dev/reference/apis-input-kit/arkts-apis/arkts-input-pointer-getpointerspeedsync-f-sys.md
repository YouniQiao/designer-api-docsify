# getPointerSpeedSync (System API)

## Modules to Import

```TypeScript
import { pointer } from 'pointer';
```

## getPointerSpeedSync

```TypeScript
function getPointerSpeedSync(): int
```

Obtains the mouse pointer speed. This API returns the result synchronously.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-pointer-function getPointerSpeedSync(): int--><!--Device-pointer-function getPointerSpeedSync(): int-End-->

**System capability:** SystemCapability.MultimodalInput.Input.Pointer

**System API:** This is a system API.

**Return value:**

| Type | Description |
| --- | --- |
| int | Mouse pointer speed. The value ranges from 1 to 20. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; <br>2. Incorrect parameter types; 3. Parameter verification failed. |
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
            let speed = pointer.getPointerSpeedSync();
            console.info(`Get pointer speed success, speed: ${JSON.stringify(speed)}`);
          } catch (error) {
            console.error(`Get pointer speed failed, error: ${JSON.stringify(error, [`code`, `message`])}`);
          }
        })
    }
  }
}
```

