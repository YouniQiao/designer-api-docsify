# TabsNestedScrollMode

Tabs组件和父组件的嵌套滚动模式枚举。

**Since:** 24

**ArkTS mode:** ArkTS-Sta only, since version 24.

<!--Device-unnamed-export declare enum TabsNestedScrollMode--><!--Device-unnamed-export declare enum TabsNestedScrollMode-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## SELF_ONLY

```TypeScript
SELF_ONLY = 0
```

滚动效果只会在Tabs组件内发生，不会发生其他的嵌套滚动行为，也就是说，当内层组件滚动达到边界时，父容器不会随之滚动。

**Since:** 24

**ArkTS mode:** ArkTS-Sta only, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-TabsNestedScrollMode-SELF_ONLY = 0--><!--Device-TabsNestedScrollMode-SELF_ONLY = 0-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## SELF_FIRST

```TypeScript
SELF_FIRST = 1
```

Tabs组件首先滚动，当它到达边界时，父容器开始滚动。

**Since:** 24

**ArkTS mode:** ArkTS-Sta only, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-TabsNestedScrollMode-SELF_FIRST = 1--><!--Device-TabsNestedScrollMode-SELF_FIRST = 1-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

