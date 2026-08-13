# getTouchModeSync

## Modules to Import

```TypeScript
import { accessibility } from '@kit.AccessibilityKit';
```

## getTouchModeSync

```TypeScript
function getTouchModeSync(): string
```

Queries single- or double-touch mode.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 23.

**Widget capability:** This API can be used in ArkTS widgets since API version 23.

<!--Device-accessibility-function getTouchModeSync(): string--><!--Device-accessibility-function getTouchModeSync(): string-End-->

**System capability:** SystemCapability.BarrierFree.Accessibility.Core

**Return value:**

| Type | Description |
| --- | --- |
| string | Touch mode. &lt;br&gt;- **singleTouchMode**: Single-touch mode. &lt;br&gt;- **doubleTouchMode**: Double-touch mode. &lt;br&gt;- **none**: Touch guide mode is disabled. |

