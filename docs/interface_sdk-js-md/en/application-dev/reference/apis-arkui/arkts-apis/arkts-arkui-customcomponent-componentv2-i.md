# ComponentV2

Defining ComponentV2 Annotation

ComponentV2 is an Annotation to define a custom component using state management V2.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export @interface ComponentV2--><!--Device-unnamed-export @interface ComponentV2-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## poolAccepts

```TypeScript
poolAccepts: string[] = []
```

Collection of custom components to be reused.

**Type:** string[]

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ComponentV2-poolAccepts: string[] = []--><!--Device-ComponentV2-poolAccepts: string[] = []-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## reusePool

```TypeScript
reusePool: ReusePoolOwnership = ReusePoolOwnership.OFF
```

the reuse type of a custom component. Default value is OFF.

**Type:** [ReusePoolOwnership](arkts-arkui-customcomponent-reusepoolownership-e.md)

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ComponentV2-reusePool: ReusePoolOwnership = ReusePoolOwnership.OFF--><!--Device-ComponentV2-reusePool: ReusePoolOwnership = ReusePoolOwnership.OFF-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

