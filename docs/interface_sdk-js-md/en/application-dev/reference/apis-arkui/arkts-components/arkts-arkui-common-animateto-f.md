# animateTo

## Modules to Import

```TypeScript
```

## animateTo

```TypeScript
declare function animateTo(value: AnimateParam, event: () => void): void
```

Defines an explicit animation. When an animation is required, call this API explicitly to modify state and produce an animation effect. &gt; **NOTE：**&gt; &gt; - Since API version 10, you can use &gt; [animateTo](../../../reference/apis-arkui/arkts-apis-uicontext-uicontext.md#animateto) in &gt; [UIContext](../arkts-apis/arkts-arkui-arkui-uicontext-uicontext-c.md) to specify the UI execution context. &gt; &gt; - Avoid using **animateTo** in **aboutToAppear** or **aboutToDisappear**. &gt; &gt; - When **animateTo** is called in &gt; [aboutToAppear](../../../reference/apis-arkui/arkui-ts/ts-custom-component-lifecycle.md#abouttoappear), the &gt; component's build method is not executed yet, and internal components are not created. This means the animation has &gt; no initial values to work with and will not function as expected. &gt; &gt; - During &gt; [aboutToDisappear](../../../reference/apis-arkui/arkui-ts/ts-custom-component-lifecycle.md#abouttodisappear), the &gt; component is being destroyed, so animations should not be used. &gt; &gt; - When a component appears or disappears, you can add animation effects through the transition &gt; attribute. &gt; &gt; - For attributes not supported by component transitions, see &gt; [Example 2](../../../reference/apis-arkui/arkui-ts/ts-explicit-animation.md#example-2-enabling-component-disappearance-after-animation-completion) &gt; and use **animateTo** to implement the component disappearance effect after animation completion. &gt; &gt; - In certain scenarios, using **animateTo** with &gt; [state management V2](../../../ui/state-management/arkts-state-management-overview.md#state-management-v2) may &gt; produce unexpected results. For details, see &gt; [Using animateTo Failed in State Management V2](../../../ui/state-management/arkts-new-local.md#using-animateto-failed-in-state-management-v2).

**Since:** 7

**Deprecated since:** 18

**Substitutes:** animateTo

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

<!--Device-unnamed-declare function animateTo(value: AnimateParam, event: () => void): void--><!--Device-unnamed-declare function animateTo(value: AnimateParam, event: () => void): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [AnimateParam](arkts-arkui-animateparam-i.md) | Yes |  |
| event | () =&gt; void | Yes |  |

