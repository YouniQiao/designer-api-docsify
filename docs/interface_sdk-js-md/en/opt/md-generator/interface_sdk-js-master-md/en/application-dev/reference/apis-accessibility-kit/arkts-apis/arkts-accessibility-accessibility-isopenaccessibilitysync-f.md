# isOpenAccessibilitySync

## Modules to Import

```TypeScript
import { accessibility } from '@kit.AccessibilityKit';
```

## isOpenAccessibilitySync

```TypeScript
function isOpenAccessibilitySync(): boolean
```

Checks whether any accessibility application has been enabled in the system. To obtain information about accessibility applications in the system, use   
[accessibility.getAccessibilityExtensionListSync](arkts-accessibility-accessibility-getaccessibilityextensionlistsync-f.md#getAccessibilityExtensionListSync).

**Since:** 10

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 23.

<!--Device-accessibility-function isOpenAccessibilitySync(): boolean--><!--Device-accessibility-function isOpenAccessibilitySync(): boolean-End-->

**System capability:** SystemCapability.BarrierFree.Accessibility.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

## Examples

```TypeScript
import { accessibility } from '@kit.AccessibilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

// 1. If no accessibility application is enabled, the system returns false.
// 2. If any accessibility application is enabled, the system returns true.
let status: boolean = accessibility.isOpenAccessibilitySync();
```
