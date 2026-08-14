# getAccessibilityExtensionListSync

## Modules to Import

```TypeScript
import { accessibility } from 'accessibility';
```

## getAccessibilityExtensionListSync

```TypeScript
function getAccessibilityExtensionListSync(
    abilityType: AbilityType,
    stateType: AbilityState
  ): Array<AccessibilityAbilityInfo>
```

Query the list of accessibility applications in the current system, which can be queried by criteria. This API is the synchronous version of [accessibility.getAccessibilityExtensionList](arkts-accessibility-accessibility-getaccessibilityextensionlist-f.md#getAccessibilityExtensionList) (asynchronous version). They have the same functionality. Use this API if you need to obtain the result immediately. Use the asynchronous version if you need to query in non-blocking scenarios.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 23.

**Widget capability:** This API can be used in ArkTS widgets since API version 23.

<!--Device-accessibility-function getAccessibilityExtensionListSync(    abilityType: AbilityType,    stateType: AbilityState  ): Array<AccessibilityAbilityInfo>--><!--Device-accessibility-function getAccessibilityExtensionListSync(    abilityType: AbilityType,    stateType: AbilityState  ): Array<AccessibilityAbilityInfo>-End-->

**System capability:** SystemCapability.BarrierFree.Accessibility.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| abilityType | AbilityType | Yes | Accessibility application type. |
| stateType | AbilityState | Yes | Accessibility application status. |

**Return value:**

| Type | Description |
| --- | --- |
| Array&lt;[AccessibilityAbilityInfo](arkts-accessibility-accessibility-accessibilityabilityinfo-i.md)&gt; | Promise used to return the accessibility application list. |

