# TabsNestedScrollMode

Tabs组件和父组件的嵌套滚动模式枚举。

**Since:** 24

**ArkTS mode:** ArkTS-Dyn only, since version 24.

<!--Device-unnamed-declare enum TabsNestedScrollMode--><!--Device-unnamed-declare enum TabsNestedScrollMode-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## SELF_ONLY

```TypeScript
SELF_ONLY = 0
```

Tabs自身滚动，不与父组件联动。适用于Tabs组件内部有完整滚动功能、需要独立控制滚动行为的场景。

**Since:** 24

**ArkTS mode:** ArkTS-Dyn only, since version 24.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 24.

<!--Device-TabsNestedScrollMode-SELF_ONLY = 0--><!--Device-TabsNestedScrollMode-SELF_ONLY = 0-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## SELF_FIRST

```TypeScript
SELF_FIRST = 1
```

Tabs自身先滚动，自身滚动到边缘以后父组件滚动。父组件滚动到边缘以后，如果父组件有边缘效果，则父组件触发边缘效果，否则Tabs触发边缘效果。适用于Tabs作为主要滚动区域、滚动到边缘后需要与父组件联动的嵌套滚动场景。

**Since:** 24

**ArkTS mode:** ArkTS-Dyn only, since version 24.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 24.

<!--Device-TabsNestedScrollMode-SELF_FIRST = 1--><!--Device-TabsNestedScrollMode-SELF_FIRST = 1-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

