# onTouchModeChange

## Modules to Import

```TypeScript
import { accessibility } from '@kit.AccessibilityKit';
import { AccessibilityEventType, AccessibilityAction, FocusMoveResultCode, InjectActionType, AccessibilityFocusScene, FocusRuleType, OperateVirtualNodeResult, AccessibilitySourceType } from '@kit.AccessibilityKit';
```

## onTouchModeChange

```TypeScript
function onTouchModeChange(callback: Callback<string>): void
```

Register the observe of the touch mode changed.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 23.

**Widget capability:** This API can be used in ArkTS widgets since API version 23.

<!--Device-accessibility-function onTouchModeChange(callback: Callback<string>): void--><!--Device-accessibility-function onTouchModeChange(callback: Callback<string>): void-End-->

**System capability:** SystemCapability.BarrierFree.Accessibility.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;string&gt; | Yes | callback Asynchronous callback interface. |

