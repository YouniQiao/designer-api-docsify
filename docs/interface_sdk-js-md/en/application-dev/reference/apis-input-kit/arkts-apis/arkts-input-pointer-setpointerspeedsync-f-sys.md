# setPointerSpeedSync (System API)

## Modules to Import

```TypeScript
import { pointer } from '@kit.InputKit';
```

## setPointerSpeedSync

```TypeScript
function setPointerSpeedSync(speed: int): void
```

Sets the mouse pointer speed. This API returns the result synchronously.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-pointer-function setPointerSpeedSync(speed: int): void--><!--Device-pointer-function setPointerSpeedSync(speed: int): void-End-->

**System capability:** SystemCapability.MultimodalInput.Input.Pointer

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| speed | int | Yes | Mouse pointer speed. The value ranges from **1** to **20**. The default value is **10**. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; &lt;br&gt;2. Incorrect parameter types; 3. Parameter verification failed. |
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
            let speed = pointer.setPointerSpeedSync(5);
            console.info(`Set pointer speed success`);
          } catch (error) {
            console.error(`Set pointer speed failed, error: ${JSON.stringify(error, [`code`, `message`])}`);
          }
        })
    }
  }
}
```

