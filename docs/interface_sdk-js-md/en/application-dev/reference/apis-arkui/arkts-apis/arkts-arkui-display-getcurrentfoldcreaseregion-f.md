# getCurrentFoldCreaseRegion

## Modules to Import

```TypeScript
import { display } from 'kits/@kit.ArkUI';
```

## getCurrentFoldCreaseRegion

```TypeScript
function getCurrentFoldCreaseRegion(): FoldCreaseRegion
```

在当前显示模式下获取折叠折痕区域。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-display-function getCurrentFoldCreaseRegion(): FoldCreaseRegion--><!--Device-display-function getCurrentFoldCreaseRegion(): FoldCreaseRegion-End-->

**System capability:** SystemCapability.Window.SessionManager

**Return value:**

| Type | Description |
| --- | --- |
| [FoldCreaseRegion](arkts-arkui-display-foldcreaseregion-i.md) | FoldCreaseRegion对象，返回设备在当前显示模式下的折叠折痕区域。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 1400003 | This display manager service works abnormally. |

## Examples

```TypeScript
let data: display.FoldCreaseRegion = display.getCurrentFoldCreaseRegion();
console.info(`Succeeded in obtaining current fold crease region. Data: ${JSON.stringify(data)}`);
```

