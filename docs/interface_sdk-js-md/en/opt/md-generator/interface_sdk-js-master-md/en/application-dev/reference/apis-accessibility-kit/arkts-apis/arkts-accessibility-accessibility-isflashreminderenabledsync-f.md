# isFlashReminderEnabledSync

## Modules to Import

```TypeScript
import { accessibility } from '@kit.AccessibilityKit';
```

## isFlashReminderEnabledSync

```TypeScript
function isFlashReminderEnabledSync(): boolean
```

Checks whether flash alerts mode is enabled with a synchronous method.

**Since:** 23

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-accessibility-function isFlashReminderEnabledSync(): boolean--><!--Device-accessibility-function isFlashReminderEnabledSync(): boolean-End-->

**System capability:** SystemCapability.BarrierFree.Accessibility.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

## Examples

```TypeScript
import { accessibility } from '@kit.AccessibilityKit';

@Entry
@Component
struct Index {
  aboutToAppear(): void {
    let status: boolean = accessibility.isFlashReminderEnabledSync();
    console.info(`status: ${JSON.stringify(status)}`);
  }

  build() {
    Column() {
    }
  }
}
```
