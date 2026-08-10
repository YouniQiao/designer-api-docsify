# NestedScrollOptions

[nestedScroll](../../../reference/apis-arkui/arkui-ts/ts-container-scrollable-common.md#nestedscroll11)属性参数对象。

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

<!--Device-unnamed-declare interface NestedScrollOptions--><!--Device-unnamed-declare interface NestedScrollOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## scrollBackward

```TypeScript
scrollBackward: NestedScrollMode
```

滚动组件往起始端滚动时的嵌套滚动选项。NestedScrollMode.SELF_ONLY表示仅自身滚动，不与父组件联动；NestedScrollMode.SELF_FIRST表示自身先滚动，自身滚动到边缘后父组件滚动；NestedScrollMode.PARENT_FIRST表示父组件先滚动，父组件滚动到边缘后自身滚动。

**Type:** [NestedScrollMode](../arkts-apis/arkts-arkui-nestedscrollmode-e.md)

**Since:** 11

**ArkTS mode:** ArkTS-Dyn only, since version 11.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-NestedScrollOptions-scrollBackward: NestedScrollMode--><!--Device-NestedScrollOptions-scrollBackward: NestedScrollMode-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## scrollForward

```TypeScript
scrollForward: NestedScrollMode
```

滚动组件往末尾端滚动时的嵌套滚动选项。NestedScrollMode.SELF_ONLY表示仅自身滚动，不与父组件联动；NestedScrollMode.SELF_FIRST表示自身先滚动，自身滚动到边缘后父组件滚动；NestedScrollMode.PARENT_FIRST表示父组件先滚动，父组件滚动到边缘后自身滚动。

**Type:** [NestedScrollMode](../arkts-apis/arkts-arkui-nestedscrollmode-e.md)

**Since:** 11

**ArkTS mode:** ArkTS-Dyn only, since version 11.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-NestedScrollOptions-scrollForward: NestedScrollMode--><!--Device-NestedScrollOptions-scrollForward: NestedScrollMode-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

