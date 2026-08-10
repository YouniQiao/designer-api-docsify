# getFoldDisplayMode

## Modules to Import

```TypeScript
import { display } from 'kits/@kit.ArkUI';
```

## getFoldDisplayMode

```TypeScript
function getFoldDisplayMode(): FoldDisplayMode
```

获取可折叠设备当前的显示模式。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-display-function getFoldDisplayMode(): FoldDisplayMode--><!--Device-display-function getFoldDisplayMode(): FoldDisplayMode-End-->

**System capability:** SystemCapability.Window.SessionManager

**Return value:**

| Type | Description |
| --- | --- |
| [FoldDisplayMode](arkts-arkui-display-folddisplaymode-e.md) | FoldDisplayMode对象，返回可折叠设备当前的显示模式。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 1400003 | This display manager service works abnormally. |

## Examples

```TypeScript
let data: display.FoldDisplayMode = display.getFoldDisplayMode();
console.info(`Succeeded in obtaining fold display mode. Data: ${data}`);
```

