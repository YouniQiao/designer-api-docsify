# ContextMenuAnimationOptions

Defines the ContextMenu's preview animator options.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-unnamed-export interface ContextMenuAnimationOptions--><!--Device-unnamed-export interface ContextMenuAnimationOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## hoverScale

```TypeScript
hoverScale?: AnimationNumberRange
```

Sets the scale start and end animator of the image displayed before the custom builder preview is displayed.

**Type:** [AnimationNumberRange](arkts-na-animationnumberrange-t.md)

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ContextMenuAnimationOptions-hoverScale?: AnimationNumberRange--><!--Device-ContextMenuAnimationOptions-hoverScale?: AnimationNumberRange-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## hoverScaleInterruption

```TypeScript
hoverScaleInterruption?: boolean
```

Sets whether support to interrupt the process of hover scale.

**Type:** boolean

**Default:** false

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ContextMenuAnimationOptions-hoverScaleInterruption?: boolean--><!--Device-ContextMenuAnimationOptions-hoverScaleInterruption?: boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## scale

```TypeScript
scale?: AnimationNumberRange
```

Sets the start animator scale and end animator scale.

**Type:** [AnimationNumberRange](arkts-na-animationnumberrange-t.md)

**Default:** -

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ContextMenuAnimationOptions-scale?: AnimationNumberRange--><!--Device-ContextMenuAnimationOptions-scale?: AnimationNumberRange-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## transition

```TypeScript
transition?: TransitionEffect
```

Defines the transition effect of menu preview opening and closing.

**Type:** [TransitionEffect](arkts-na-common-transitioneffect-c.md)

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ContextMenuAnimationOptions-transition?: TransitionEffect--><!--Device-ContextMenuAnimationOptions-transition?: TransitionEffect-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

