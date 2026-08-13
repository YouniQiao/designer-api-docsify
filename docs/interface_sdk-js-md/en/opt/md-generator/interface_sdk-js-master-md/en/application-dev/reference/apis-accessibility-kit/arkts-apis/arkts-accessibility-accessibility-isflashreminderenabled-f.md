# isFlashReminderEnabled

## Modules to Import

```TypeScript
import { accessibility } from '@kit.AccessibilityKit';
```

## isFlashReminderEnabled

```TypeScript
function isFlashReminderEnabled(): Promise<boolean>
```

Checks whether flash alerts mode is enabled. This API uses a promise to return the result.

**Since:** 23

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-accessibility-function isFlashReminderEnabled(): Promise<boolean>--><!--Device-accessibility-function isFlashReminderEnabled(): Promise<boolean>-End-->

**System capability:** SystemCapability.BarrierFree.Accessibility.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;boolean & gt; |

## Examples

```TypeScript
import { accessibility } from '@kit.AccessibilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct Index {
  aboutToAppear(): void {
    accessibility.isFlashReminderEnabled().then((data: boolean) => {
      console.info(`success data:isFlashReminderEnabled : ${JSON.stringify(data)}`);
    }).catch((err: BusinessError) => {
      console.error(`failed to isFlashReminderEnabled, Code is ${err.code}, message is ${err.message}`);
    });
  }

  build() {
    Column() {
    }
  }
}
```
