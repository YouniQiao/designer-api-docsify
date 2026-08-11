# isAudioMonoEnabledSync

## Modules to Import

```TypeScript
import { accessibility } from 'kits/@kit.AccessibilityKit';
```

## isAudioMonoEnabledSync

```TypeScript
function isAudioMonoEnabledSync(): boolean
```

Checks whether mono audio mode is enabled with a synchronous mode.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-accessibility-function isAudioMonoEnabledSync(): boolean--><!--Device-accessibility-function isAudioMonoEnabledSync(): boolean-End-->

**System capability:** SystemCapability.BarrierFree.Accessibility.Core

**Return value:**

| Type | Description |
| --- | --- |
| boolean | Whether mono audio mode is enabled. Returns **true** if mono audio mode is enabled; returns **false** otherwise. |

## Examples

```TypeScript
import { accessibility } from '@kit.AccessibilityKit';

@Entry
@Component
struct Index {
  aboutToAppear(): void {
    let status: boolean = accessibility.isAudioMonoEnabledSync();
    console.info(`status: ${JSON.stringify(status)}`);
  }

  build() {
    Column() {
    }
  }
}
```

