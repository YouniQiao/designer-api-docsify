# onAudioMonoStateChange

## Modules to Import

```TypeScript
import { accessibility } from 'kits/@kit.AccessibilityKit';
import { AccessibilityEventType, AccessibilityAction, FocusMoveResultCode, InjectActionType, AccessibilityFocusScene, FocusRuleType, OperateVirtualNodeResult, AccessibilitySourceType } from 'kits/@kit.AccessibilityKit';
```

## onAudioMonoStateChange

```TypeScript
function onAudioMonoStateChange(callback: Callback<boolean>): void
```

Subscribes to the state changes of mono audio mode. This API uses an asynchronous callback to return the result.

> **NOTE：**&gt;
> - The callback parameter for registering a listener must use a named function instead of an anonymous function.
> Otherwise, a new underlying object is created each time the function is called, causing memory leakage.&gt;
> - After calling this method, ensure that
> [accessibility.offAudioMonoStateChange](arkts-accessibility-accessibility-offaudiomonostatechange-f.md) is used to unsubscribe
> before the component instance is destroyed (for example, in the **aboutToDisappear** lifecycle callback).
> Otherwise, a crash may occur.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.BarrierFree.Accessibility.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;boolean&gt; | Yes |
