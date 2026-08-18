# isOpenAccessibilitySync

## Modules to Import

```TypeScript
```

## isOpenAccessibilitySync

```TypeScript
function isOpenAccessibilitySync(): boolean
```

Checks whether any accessibility application has been enabled in the system. To obtain information about accessibility applications in the system, you are advised to use [accessibility.getAccessibilityExtensionListSync](arkts-accessibility-accessibility-getaccessibilityextensionlistsync-f.md#getaccessibilityextensionlistsync).

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 23.

<!--Device-accessibility-function isOpenAccessibilitySync(): boolean--><!--Device-accessibility-function isOpenAccessibilitySync(): boolean-End-->

**System capability:** SystemCapability.BarrierFree.Accessibility.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

**Examples**

```TypeScript
import { accessibility } from '@kit.AccessibilityKit';

// 1. Multiple accessibility apps are installed in the system. If none of them is enabled, false is returned.
// 2. Multiple accessibility apps are installed in the system. If any of them is enabled, true is returned.
let status: boolean = accessibility.isOpenAccessibilitySync();
```
