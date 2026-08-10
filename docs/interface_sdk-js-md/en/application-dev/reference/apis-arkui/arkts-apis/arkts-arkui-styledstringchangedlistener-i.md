# StyledStringChangedListener

属性字符串的文本内容变化监听器。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

<!--Device-unnamed-declare interface StyledStringChangedListener--><!--Device-unnamed-declare interface StyledStringChangedListener-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## onDidChange

```TypeScript
onDidChange?: OnDidChangeCallback
```

文本内容完成变化回调函数。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-StyledStringChangedListener-onDidChange?: OnDidChangeCallback--><!--Device-StyledStringChangedListener-onDidChange?: OnDidChangeCallback-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## onWillChange

```TypeScript
onWillChange?: Callback<StyledStringChangeValue, boolean>
```

文本内容将要变化回调函数。

**Type:** [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-callback-t.md)&lt;StyledStringChangeValue, boolean&gt;

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-StyledStringChangedListener-onWillChange?: Callback<StyledStringChangeValue, boolean>--><!--Device-StyledStringChangedListener-onWillChange?: Callback<StyledStringChangeValue, boolean>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

