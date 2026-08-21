# offDidLayout

## Modules to Import

```TypeScript
```

## offDidLayout

```TypeScript
export function offDidLayout(context: UIContext, callback?: Callback<void>): void
```

Removes a callback function that was previously registered with `on()`.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-uiObserver-export function offDidLayout(context: UIContext, callback?: Callback<void>): void--><!--Device-uiObserver-export function offDidLayout(context: UIContext, callback?: Callback<void>): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| context | [UIContext](../../apis-arkui/arkts-apis/arkts-arkui-arkui-uicontext-uicontext-c.md) | Yes | The context scope of the observer. |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-callback-t.md)&lt;void&gt; | No | The callback function to remove. If not provided, all callbacks for the given event type will be removed. |

