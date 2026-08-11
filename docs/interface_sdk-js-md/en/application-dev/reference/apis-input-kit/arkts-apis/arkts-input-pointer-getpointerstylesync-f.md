# getPointerStyleSync

## Modules to Import

```TypeScript
import { pointer } from 'kits/@kit.InputKit';
```

## getPointerStyleSync

```TypeScript
function getPointerStyleSync(windowId: int): PointerStyle
```

Queries the mouse pointer style type of a specified window, such as east arrow, west arrow, south arrow, and north arrow. This API can obtain only the mouse pointer style type of windows within the current application process.

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

<!--Device-pointer-function getPointerStyleSync(windowId: int): PointerStyle--><!--Device-pointer-function getPointerStyleSync(windowId: int): PointerStyle-End-->

**System capability:** SystemCapability.MultimodalInput.Input.Pointer

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| windowId | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | Window ID. The value is an integer greater than or equal to **-1**. The value **-1** indicates the global window. &lt;br&gt;If the window ID is valid and the corresponding window exists, the mouse pointer style of the window is returned. &lt;br&gt;If the window ID is valid but the window does not exist, the global mouse pointer style is returned by default. &lt;br&gt;If the mouse pointer style is set for a non-existent window through [setPointerStyleSync](arkts-input-pointer-setpointerstylesync-f.md#setpointerstylesync), this API can obtain the mouse pointer style properly. |

**Return value:**

| Type | Description |
| --- | --- |
| [PointerStyle](../../apis-arkui/arkts-components/arkts-arkui-pointerstyle-t.md) | Mouse pointer style. |

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

