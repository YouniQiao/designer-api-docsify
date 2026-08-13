# isScreenReaderOpenSync

## Modules to Import

```TypeScript
import { accessibility } from '@kit.AccessibilityKit';
```

## isScreenReaderOpenSync

```TypeScript
function isScreenReaderOpenSync(): boolean
```

Checks whether screen reader mode is enabled.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 23.

**Widget capability:** This API can be used in ArkTS widgets since API version 23.

<!--Device-accessibility-function isScreenReaderOpenSync(): boolean--><!--Device-accessibility-function isScreenReaderOpenSync(): boolean-End-->

**System capability:** SystemCapability.BarrierFree.Accessibility.Vision

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

## Examples

```TypeScript
import { accessibility } from '@kit.AccessibilityKit';

let status: boolean = accessibility.isScreenReaderOpenSync();
```
