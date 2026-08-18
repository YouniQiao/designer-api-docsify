# onDidLayout

## Modules to Import

```TypeScript
```

## onDidLayout

```TypeScript
export function onDidLayout(context: UIContext, callback: Callback<void>): void
```

Registers a callback function to be called when the layout is done.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-uiObserver-export function onDidLayout(context: UIContext, callback: Callback<void>): void--><!--Device-uiObserver-export function onDidLayout(context: UIContext, callback: Callback<void>): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| context | [UIContext](../../apis-arkui/arkts-apis/arkts-arkui-arkui-uicontext-uicontext-c.md) | Yes | The context scope of the observer. |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;void&gt; | Yes | The callback function to be called when the layout is done. |

