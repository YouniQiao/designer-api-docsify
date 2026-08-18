# isFlashReminderEnabledSync

## Modules to Import

```TypeScript
```

## isFlashReminderEnabledSync

```TypeScript
function isFlashReminderEnabledSync(): boolean
```

Checks whether flash alerts mode is enabled. This API is the synchronous version of [accessibility.isFlashReminderEnabled](arkts-accessibility-accessibility-isflashreminderenabled-f.md#isflashreminderenabled) (asynchronous version). They have the same functionality. Use this API if you need to obtain the result immediately. Use the asynchronous version if you need to query in non-blocking scenarios.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-accessibility-function isFlashReminderEnabledSync(): boolean--><!--Device-accessibility-function isFlashReminderEnabledSync(): boolean-End-->

**System capability:** SystemCapability.BarrierFree.Accessibility.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

**Examples**

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
