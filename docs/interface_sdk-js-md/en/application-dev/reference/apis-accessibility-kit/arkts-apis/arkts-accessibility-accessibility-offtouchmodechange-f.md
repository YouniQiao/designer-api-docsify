# offTouchModeChange

## Modules to Import

```TypeScript
import { accessibility } from '@kit.AccessibilityKit';
```

## offTouchModeChange

```TypeScript
function offTouchModeChange(callback?: Callback<string>): void
```

Unregister the observe of the touch mode changed.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 23.

**Widget capability:** This API can be used in ArkTS widgets since API version 23.

<!--Device-accessibility-function offTouchModeChange(callback?: Callback<string>): void--><!--Device-accessibility-function offTouchModeChange(callback?: Callback<string>): void-End-->

**System capability:** SystemCapability.BarrierFree.Accessibility.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;string&gt; | No | callback Asynchronous callback interface. |

