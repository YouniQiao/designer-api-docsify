# StyledStringChangedListener

Define the StyledString changed listener.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-unnamed-export declare interface StyledStringChangedListener--><!--Device-unnamed-export declare interface StyledStringChangedListener-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## onDidChange

```TypeScript
onDidChange?: OnDidChangeCallback
```

Called after text changed.

**Type:** [OnDidChangeCallback](arkts-arkui-ondidchangecallback-t.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-StyledStringChangedListener-onDidChange?: OnDidChangeCallback--><!--Device-StyledStringChangedListener-onDidChange?: OnDidChangeCallback-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## onWillChange

```TypeScript
onWillChange?: Callback<StyledStringChangeValue, boolean>
```

Called before text changed.

**Type:** [Callback](../arkts-components/arkts-arkui-callback-i.md)&lt;[StyledStringChangeValue](arkts-arkui-textcommon-styledstringchangevalue-i.md), boolean&gt;

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-StyledStringChangedListener-onWillChange?: Callback<StyledStringChangeValue, boolean>--><!--Device-StyledStringChangedListener-onWillChange?: Callback<StyledStringChangeValue, boolean>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

