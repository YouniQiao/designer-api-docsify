# getCaptionsManager

## getCaptionsManager

```TypeScript
function getCaptionsManager(): CaptionsManager
```

Obtains a **CaptionsManager** instance.

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Deprecated since:** 12

<!--Device-accessibility-function getCaptionsManager(): CaptionsManager--><!--Device-accessibility-function getCaptionsManager(): CaptionsManager-End-->

**System capability:** SystemCapability.BarrierFree.Accessibility.Hearing

**Return value:**

| Type | Description |
| --- | --- |
| \_\_\_MD\_LINK\_USD\_0\_\_\_ | Captions configuration. |

**Example**

```TypeScript
import { accessibility } from '@kit.AccessibilityKit';

let captionsManager = accessibility.getCaptionsManager();
```

