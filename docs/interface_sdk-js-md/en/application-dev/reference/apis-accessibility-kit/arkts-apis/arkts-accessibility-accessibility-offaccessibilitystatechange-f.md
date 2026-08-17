# offAccessibilityStateChange

## Modules to Import

```TypeScript
import { accessibility } from 'accessibility';
```

## offAccessibilityStateChange

```TypeScript
function offAccessibilityStateChange(callback?: Callback<boolean>): void
```

Unregister the observe of the accessibility state changed.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 23.

**Widget capability:** This API can be used in ArkTS widgets since API version 23.

<!--Device-accessibility-function offAccessibilityStateChange(callback?: Callback<boolean>): void--><!--Device-accessibility-function offAccessibilityStateChange(callback?: Callback<boolean>): void-End-->

**System capability:** SystemCapability.BarrierFree.Accessibility.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;boolean&gt; | No | Asynchronous callback interface. |

