# ScrollSnapAlign

设置列表项滚动结束对齐效果。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

<!--Device-unnamed-declare enum ScrollSnapAlign--><!--Device-unnamed-declare enum ScrollSnapAlign-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## NONE

```TypeScript
NONE = 0
```

默认无列表项滚动结束对齐效果。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-ScrollSnapAlign-NONE = 0--><!--Device-ScrollSnapAlign-NONE = 0-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## START

```TypeScript
START = 1
```

视图中的第一项将在列表的开头对齐。

**说明：**

当列表位移至末端，需要将末端的item完整显示，可能出现开头不对齐的情况。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-ScrollSnapAlign-START = 1--><!--Device-ScrollSnapAlign-START = 1-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## CENTER

```TypeScript
CENTER = 2
```

视图中的中间项将在列表中心对齐。

**说明：**

顶端和末尾的item都可以在列表中心对齐，列表显示可能露出空白。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-ScrollSnapAlign-CENTER = 2--><!--Device-ScrollSnapAlign-CENTER = 2-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## END

```TypeScript
END = 3
```

视图中的最后一项将在列表末尾对齐。

**说明：**

当列表位移至顶端，需要将顶端的item完整显示，可能出现末尾不对齐的情况。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-ScrollSnapAlign-END = 3--><!--Device-ScrollSnapAlign-END = 3-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

