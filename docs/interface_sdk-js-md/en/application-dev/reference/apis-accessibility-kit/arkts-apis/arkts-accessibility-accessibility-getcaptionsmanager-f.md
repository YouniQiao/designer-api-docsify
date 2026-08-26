# getCaptionsManager

## Modules to Import

```TypeScript
import config from '@kit.AccessibilityKit.config';
import accessibility from '@kit.AccessibilityKit';
import { GesturePath } from '@kit.AccessibilityKit.GesturePath';
import { GesturePoint } from '@kit.AccessibilityKit.GesturePoint';
import { AccessibilityEventType, AccessibilityAction, FocusMoveResultCode, InjectActionType, AccessibilityFocusScene, FocusRuleType, OperateVirtualNodeResult, AccessibilitySourceType } from '@kit.AccessibilityKit';
```

## getCaptionsManager

```TypeScript
function getCaptionsManager(): CaptionsManager
```

Obtains a **CaptionsManager** instance.

**Since:** 8

**Deprecated since:** 12

**System capability:** SystemCapability.BarrierFree.Accessibility.Hearing

**Return value:**

| Type | Description |
| --- | --- |
| [CaptionsManager](arkts-accessibility-accessibility-captionsmanager-i.md) | Captions configuration. |

**Examples**

```TypeScript
import { accessibility } from '@kit.AccessibilityKit';

let captionsManager = accessibility.getCaptionsManager();
```
