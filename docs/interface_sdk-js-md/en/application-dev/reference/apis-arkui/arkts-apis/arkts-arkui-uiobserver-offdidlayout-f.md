# offDidLayout

## Modules to Import

```TypeScript
import { uiObserver } from '@kit.ArkUI';
```

## offDidLayout

```TypeScript
export function offDidLayout(context: UIContext, callback?: Callback<void>): void
```

Removes a callback function that was previously registered with `on()`.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-uiObserver-export function offDidLayout(context: UIContext, callback?: Callback<void>): void--><!--Device-uiObserver-export function offDidLayout(context: UIContext, callback?: Callback<void>): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| context | [UIContext](arkts-arkui-arkui-uicontext-uicontext-c.md) | Yes | The context scope of the observer. |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-callback-t.md)&lt;void&gt; | No | The callback function to remove. If not provided, all callbacks for the given event type will be removed. |

