# getTouchModeSync

## Modules to Import

```TypeScript
import config from '@kit.AccessibilityKit.config';
import accessibility from '@kit.AccessibilityKit';
import { GesturePath } from '@kit.AccessibilityKit.GesturePath';
import { GesturePoint } from '@kit.AccessibilityKit.GesturePoint';
import { AccessibilityEventType, AccessibilityAction, FocusMoveResultCode, InjectActionType, AccessibilityFocusScene, FocusRuleType, OperateVirtualNodeResult, AccessibilitySourceType } from '@kit.AccessibilityKit';
```

## getTouchModeSync

```TypeScript
function getTouchModeSync(): string
```

Obtains the single-tap/number-tap operation mode in touch guide mode. This can be used to adjust the app's interaction response mode based on the current operation mode (for example, responding directly to taps in single- tap mode, or requiring number-tap confirmation in number-tap mode).

**Since:** 20

**Atomic service API:** This API can be used in atomic services since API version 23.

**Widget capability:** This API can be used in ArkTS widgets since API version 23.

**System capability:** SystemCapability.BarrierFree.Accessibility.Core

**Return value:**

| Type | Description |
| --- | --- |
| string | Touch mode. |

**Examples**

```TypeScript
import { accessibility } from '@kit.AccessibilityKit';

@Entry
@Component
struct Index {
  aboutToAppear(): void {
    let touchMode: string = accessibility.getTouchModeSync();
    console.info(`current touch mode: ${JSON.stringify(touchMode)}`);
  }

  build() {
    Column() {
    }
  }
}
```
