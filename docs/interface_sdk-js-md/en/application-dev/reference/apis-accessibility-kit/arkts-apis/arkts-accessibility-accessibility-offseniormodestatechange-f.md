# offSeniorModeStateChange

## Modules to Import

```TypeScript
import { accessibility } from 'accessibility';
```

## offSeniorModeStateChange

```TypeScript
function offSeniorModeStateChange(callback?: Callback<boolean>): void
```

Unsubscribes from the state changes of the senior mode. This API uses an asynchronous callback to return the result.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-accessibility-function offSeniorModeStateChange(callback?: Callback<boolean>): void--><!--Device-accessibility-function offSeniorModeStateChange(callback?: Callback<boolean>): void-End-->

**System capability:** SystemCapability.BarrierFree.Accessibility.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;boolean&gt; | No | Callback for the senior mode state change event. It must be the same as the callback used in [accessibility.onSeniorModeStateChange](arkts-accessibility-accessibility-onseniormodestatechange-f.md#onseniormodestatechange). If this parameter is not specified, all registered events are unsubscribed. |

