# Component

Defining Component Annotation

Component is an Annotation to define a custom component using state management V1.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export @interface Component--><!--Device-unnamed-export @interface Component-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## poolAccepts

```TypeScript
poolAccepts: string[] = []
```

要重用的自定义组件的集合。

**Type:** string[]

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Component-poolAccepts: string[] = []--><!--Device-Component-poolAccepts: string[] = []-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## reusePool

```TypeScript
reusePool: ReusePoolOwnership = ReusePoolOwnership.OFF
```

自定义组件的重用类型。默认值为OFF。

**Type:** [ReusePoolOwnership](arkts-arkui-customcomponent-reusepoolownership-e.md)

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Component-reusePool: ReusePoolOwnership = ReusePoolOwnership.OFF--><!--Device-Component-reusePool: ReusePoolOwnership = ReusePoolOwnership.OFF-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

