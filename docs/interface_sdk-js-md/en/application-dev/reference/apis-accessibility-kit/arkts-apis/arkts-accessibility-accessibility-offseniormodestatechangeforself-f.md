# offSeniorModeStateChangeForSelf

## Modules to Import

```TypeScript
import { accessibility } from 'accessibility';
```

## offSeniorModeStateChangeForSelf

```TypeScript
function offSeniorModeStateChangeForSelf(callback?: Callback<boolean>): void
```

Unsubscribes from the "senior mode" change event of the app itself. This API uses an asynchronous callback to return the result.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-accessibility-function offSeniorModeStateChangeForSelf(callback?: Callback<boolean>): void--><!--Device-accessibility-function offSeniorModeStateChangeForSelf(callback?: Callback<boolean>): void-End-->

**System capability:** SystemCapability.BarrierFree.Accessibility.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;boolean&gt; | No | Callback for the senior mode state change event. It must be the same as the callback in [accessibility.onSeniorModeStateChangeForSelf](arkts-accessibility-accessibility-onseniormodestatechangeforself-f.md#onSeniorModeStateChangeForSelf). If not specified, all registered events are unregistered. |

