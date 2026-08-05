# animateTo

## animateTo

```TypeScript
declare function animateTo(value: AnimateParam, event: () => void): void
```

Defines an explicit animation. When an animation is required, call this API explicitly to modify state and produce an animation effect. > **NOTE** > > - Since API version 10, you can use > \_\_\_MD\_LINK\_DESC\_USD\_0\_\_\_ in > [UIContext]\_\_\_JSDOC\_LINK\_DESC\_USD\_6\_\_\_ to specify the UI execution context. > > - Avoid using **animateTo** in **aboutToAppear** or **aboutToDisappear**. > > - When **animateTo** is called in > \_\_\_MD\_LINK\_DESC\_USD\_1\_\_\_, the > component's build method is not executed yet, and internal components are not created. This means the animation has > no initial values to work with and will not function as expected. > > - During > \_\_\_MD\_LINK\_DESC\_USD\_2\_\_\_, the > component is being destroyed, so animations should not be used. > > - When a component appears or disappears, you can add animation effects through the [transition]\_\_\_JSDOC\_LINK\_DESC\_USD\_7\_\_\_ > attribute. > > - For attributes not supported by component transitions, see > \_\_\_MD\_LINK\_DESC\_USD\_3\_\_\_ > and use **animateTo** to implement the component disappearance effect after animation completion. > > - In certain scenarios, using **animateTo** with > \_\_\_MD\_LINK\_DESC\_USD\_4\_\_\_ may > produce unexpected results. For details, see > \_\_\_MD\_LINK\_DESC\_USD\_5\_\_\_.

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 18

**Substitutes:** ohos.arkui.UIContext.UIContext#animateTo

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

<!--Device-unnamed-declare function animateTo(value: AnimateParam, event: () => void): void--><!--Device-unnamed-declare function animateTo(value: AnimateParam, event: () => void): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes |  |
| event | () =&gt; void | Yes |  |

