# isAudioMonoEnabledSync

## Modules to Import

```TypeScript
import { accessibility } from 'accessibility';
```

## isAudioMonoEnabledSync

```TypeScript
function isAudioMonoEnabledSync(): boolean
```

Checks whether mono audio mode is enabled. This API is the synchronous version of [accessibility.isAudioMonoEnabled](arkts-accessibility-accessibility-isaudiomonoenabled-f.md#isAudioMonoEnabled) ( asynchronous version). They have the same functionality. Use this API if you need to obtain the result immediately. Use the asynchronous version if you need to query in non-blocking scenarios.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

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

