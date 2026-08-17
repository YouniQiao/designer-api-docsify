# getPointerStyleSync

## Modules to Import

```TypeScript
import { pointer } from 'pointer';
```

## getPointerStyleSync

```TypeScript
function getPointerStyleSync(windowId: int): PointerStyle
```

Queries the mouse pointer style type of a specified window, such as east arrow, west arrow, south arrow, and north arrow. This API can obtain only the mouse pointer style type of windows within the current application process.

**Since:** 23

<!--Device-pointer-function getPointerStyleSync(windowId: int): PointerStyle--><!--Device-pointer-function getPointerStyleSync(windowId: int): PointerStyle-End-->

**System capability:** SystemCapability.MultimodalInput.Input.Pointer

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| windowId | int | Yes | Window ID. The value is an integer greater than or equal to **-1**. The value **-1** indicates the global window. <br>If the window ID is valid and the corresponding window exists, the mouse pointer style of the window is returned. <br>If the window ID is valid but the window does not exist, the global mouse pointer style is returned by default. <br>If the mouse pointer style is set for a non-existent window through [setPointerStyleSync](arkts-input-pointer-setpointerstylesync-f.md#setpointerstylesync), this API can obtain the mouse pointer style properly. |

**Return value:**

| Type | Description |
| --- | --- |
| PointerStyle | Mouse pointer style. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; <br>2. Incorrect parameter types; 3. Parameter verification failed. |

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
          let windowId = -1;
          try {
            let style: pointer.PointerStyle = pointer.getPointerStyleSync(windowId);
            console.info(`Get pointer style success, style: ${JSON.stringify(style)}`);
          } catch (error) {
            console.error(`Get pointer style failed, error: ${JSON.stringify(error, [`code`, `message`])}`);
          }
        })
    }
  }
}
```

