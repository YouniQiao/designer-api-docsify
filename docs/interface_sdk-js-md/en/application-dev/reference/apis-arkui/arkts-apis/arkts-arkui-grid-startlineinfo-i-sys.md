# StartLineInfo (System API)

用于记录Grid页面内起始行的位置信息。

**系统接口：** 此接口为系统接口。

**模型约束：** 此接口仅可在Stage模型下使用。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export declare interface StartLineInfo--><!--Device-unnamed-export declare interface StartLineInfo-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

## startIndex

```TypeScript
startIndex: int
```

目标索引或目标偏移量所在行的起始索引。取值限定为整数。

**Type:** int

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-StartLineInfo-startIndex: int--><!--Device-StartLineInfo-startIndex: int-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

## startLine

```TypeScript
startLine: int
```

startIndex对应的GridItem所在的起始行，一般为Grid视窗内的起始行，对于跨多行的GridItem需要找到该节点的起始行，可能在视窗外。取值限定为整数。

**Type:** int

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-StartLineInfo-startLine: int--><!--Device-StartLineInfo-startLine: int-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

## startOffset

```TypeScript
startOffset: double
```

startIndex对应的GridItem的顶部与Grid顶部之间的偏移量。单位：vp。

**Type:** double

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-StartLineInfo-startOffset: double--><!--Device-StartLineInfo-startOffset: double-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

## totalOffset

```TypeScript
totalOffset: double
```

总滚动偏移量，即Grid中第一个GridItem的顶部与Grid顶部之间的偏移量。单位：vp。

**Type:** double

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-StartLineInfo-totalOffset: double--><!--Device-StartLineInfo-totalOffset: double-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

