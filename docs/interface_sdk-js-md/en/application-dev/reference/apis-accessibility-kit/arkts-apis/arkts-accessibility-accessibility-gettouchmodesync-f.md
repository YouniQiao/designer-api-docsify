# getTouchModeSync

## Modules to Import

```TypeScript
import { accessibility } from 'kits/@kit.AccessibilityKit';
```

## getTouchModeSync

```TypeScript
function getTouchModeSync(): string
```

查询触摸浏览功能下的单击/双击操作模式。

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 23.

**Widget capability:** This API can be used in ArkTS widgets since API version 23.

<!--Device-accessibility-function getTouchModeSync(): string--><!--Device-accessibility-function getTouchModeSync(): string-End-->

**System capability:** SystemCapability.BarrierFree.Accessibility.Core

**Return value:**

| Type | Description |
| --- | --- |
| string | 表示当前操作模式。 &lt;br&gt;- singleTouchMode：表示单击操作模式。 &lt;br&gt;- doubleTouchMode：表示双击操作模式。 &lt;br&gt;- none：表示未开启触摸浏览功能。 |

