# StartLineInfo (System API)

用于记录Grid页面内起始行的位置信息。

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

<!--Device-unnamed-declare interface StartLineInfo--><!--Device-unnamed-declare interface StartLineInfo-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

## startIndex

```TypeScript
startIndex: int
```

在OnGetStartIndexByOffsetCallback中，表示滚动偏移量所在行的起始索引；在OnGetStartIndexByIndexCallback中，表示目标索引所在行的起始索引。

**Type:** int

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-StartLineInfo-startIndex: int--><!--Device-StartLineInfo-startIndex: int-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

## startLine

```TypeScript
startLine: int
```

startIndex对应GridItem在Grid布局中的起始行号。若该GridItem跨多行，且当前视窗从该GridItem中间位置开始显示，startLine仍表示该GridItem在完整Grid布局中实际占用的首行行号。

**Type:** int

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-StartLineInfo-startLine: int--><!--Device-StartLineInfo-startLine: int-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

## startOffset

```TypeScript
startOffset: double
```

startIndex对应的GridItem的顶部与Grid顶部之间的偏移量。

单位：vp

**Type:** double

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-StartLineInfo-startOffset: double--><!--Device-StartLineInfo-startOffset: double-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

## totalOffset

```TypeScript
totalOffset: double
```

总滚动偏移量，即Grid中第一个GridItem的顶部与Grid顶部之间的偏移量。

单位：vp

**Type:** double

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-StartLineInfo-totalOffset: double--><!--Device-StartLineInfo-totalOffset: double-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

