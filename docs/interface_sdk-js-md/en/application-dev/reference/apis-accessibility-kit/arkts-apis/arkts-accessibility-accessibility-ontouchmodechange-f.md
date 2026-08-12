# onTouchModeChange

## Modules to Import

```TypeScript
import { accessibility } from '@kit.AccessibilityKit';
```

## onTouchModeChange

```TypeScript
function onTouchModeChange(callback: Callback<string>): void
```

Register the observe of the touch mode changed.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Atomic service API:** This API can be used in atomic services since API version 23.

**Widget capability:** This API can be used in ArkTS widgets since API version 23.

<!--Device-accessibility-function onTouchModeChange(callback: Callback<string>): void--><!--Device-accessibility-function onTouchModeChange(callback: Callback<string>): void-End-->

**System capability:** SystemCapability.BarrierFree.Accessibility.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-callback-t.md)&lt;string&gt; | Yes | callback Asynchronous callback interface. |

