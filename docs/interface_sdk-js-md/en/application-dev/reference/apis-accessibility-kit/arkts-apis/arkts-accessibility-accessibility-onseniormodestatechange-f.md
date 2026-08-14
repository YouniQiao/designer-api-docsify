# onSeniorModeStateChange

## Modules to Import

```TypeScript
import { accessibility } from 'accessibility';
```

## onSeniorModeStateChange

```TypeScript
function onSeniorModeStateChange(callback: Callback<boolean>): void
```

Subscribes to the state changes of the senior mode. This API uses an asynchronous callback to return the result. > **NOTE：**> > - The callback parameter for registering a listener must use a named function instead of an anonymous function. > Otherwise, a new underlying object is created each time the function is called, causing memory leakage. > > - After calling this method, ensure that > [accessibility.offSeniorModeStateChange](arkts-accessibility-accessibility-offseniormodestatechange-f.md#offSeniorModeStateChange) is used to unsubscribe > before the component instance is destroyed (for example, in the **aboutToDisappear** lifecycle callback). > Otherwise, a crash may occur.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-accessibility-function onSeniorModeStateChange(callback: Callback<boolean>): void--><!--Device-accessibility-function onSeniorModeStateChange(callback: Callback<boolean>): void-End-->

**System capability:** SystemCapability.BarrierFree.Accessibility.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;boolean&gt; | Yes | Callback invoked to return the result. The value **true** indicates that the senior mode is enabled, and **false** indicates that the senior mode is disabled. |

