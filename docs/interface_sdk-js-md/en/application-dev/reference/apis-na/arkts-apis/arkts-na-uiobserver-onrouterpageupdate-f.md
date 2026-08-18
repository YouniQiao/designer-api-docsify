# onRouterPageUpdate

## Modules to Import

```TypeScript
```

## onRouterPageUpdate

```TypeScript
export function onRouterPageUpdate(context: UIAbilityContext | UIContext, callback: Callback<RouterPageInfo>): void
```

Registers a callback function to be called when the router page is updated.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-uiObserver-export function onRouterPageUpdate(context: UIAbilityContext | UIContext, callback: Callback<RouterPageInfo>): void--><!--Device-uiObserver-export function onRouterPageUpdate(context: UIAbilityContext | UIContext, callback: Callback<RouterPageInfo>): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| context | [UIAbilityContext](../../apis-ability-kit/arkts-apis/arkts-ability-uiabilitycontext-c.md) \| [UIContext](../../apis-arkui/arkts-apis/arkts-arkui-arkui-uicontext-uicontext-c.md) | Yes | The context scope of the observer. |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;RouterPageInfo&gt; | Yes | The callback function to be called when the router page is updated. |

