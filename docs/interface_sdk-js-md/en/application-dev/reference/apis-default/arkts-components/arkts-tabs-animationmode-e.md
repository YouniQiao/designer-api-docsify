# AnimationMode

Declare the animation mode of tab content.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-unnamed-export declare enum AnimationMode--><!--Device-unnamed-export declare enum AnimationMode-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## CONTENT_FIRST

```TypeScript
CONTENT_FIRST = 0
```

Load the content of the target page before starting the switching animation.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AnimationMode-CONTENT_FIRST = 0--><!--Device-AnimationMode-CONTENT_FIRST = 0-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## ACTION_FIRST

```TypeScript
ACTION_FIRST = 1
```

Start the switching animation before loading the content of the target page.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AnimationMode-ACTION_FIRST = 1--><!--Device-AnimationMode-ACTION_FIRST = 1-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## NO_ANIMATION

```TypeScript
NO_ANIMATION = 2
```

Disable the default switching animation.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AnimationMode-NO_ANIMATION = 2--><!--Device-AnimationMode-NO_ANIMATION = 2-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## CONTENT_FIRST_WITH_JUMP

```TypeScript
CONTENT_FIRST_WITH_JUMP = 3
```

Load the content of the target page first, then jump to the vicinity of the target page without animation, and finally jump to the target page with animation.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AnimationMode-CONTENT_FIRST_WITH_JUMP = 3--><!--Device-AnimationMode-CONTENT_FIRST_WITH_JUMP = 3-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## ACTION_FIRST_WITH_JUMP

```TypeScript
ACTION_FIRST_WITH_JUMP = 4
```

Jump to the vicinity of the target page without animation first, then jump to the target page with animation, and finally load the content of the target page.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AnimationMode-ACTION_FIRST_WITH_JUMP = 4--><!--Device-AnimationMode-ACTION_FIRST_WITH_JUMP = 4-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

