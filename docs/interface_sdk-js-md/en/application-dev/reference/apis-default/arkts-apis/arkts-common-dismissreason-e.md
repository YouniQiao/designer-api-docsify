# DismissReason

Dismiss reason type.

@enum { number }

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-unnamed-export declare enum DismissReason--><!--Device-unnamed-export declare enum DismissReason-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## PRESS_BACK

```TypeScript
PRESS_BACK = 0
```

Touching the Back button, swiping left or right on the screen, or pressing the Esc key.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DismissReason-PRESS_BACK = 0--><!--Device-DismissReason-PRESS_BACK = 0-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## TOUCH_OUTSIDE

```TypeScript
TOUCH_OUTSIDE = 1
```

Touching the mask.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DismissReason-TOUCH_OUTSIDE = 1--><!--Device-DismissReason-TOUCH_OUTSIDE = 1-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## CLOSE_BUTTON

```TypeScript
CLOSE_BUTTON = 2
```

Touching the Close button.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DismissReason-CLOSE_BUTTON = 2--><!--Device-DismissReason-CLOSE_BUTTON = 2-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## SLIDE_DOWN

```TypeScript
SLIDE_DOWN = 3
```

Slide down <p>&lt;strong&gt;NOTE&lt;/strong&gt;: <br>This API is effective only in sheet transition. </p>

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DismissReason-SLIDE_DOWN = 3--><!--Device-DismissReason-SLIDE_DOWN = 3-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## SLIDE

```TypeScript
SLIDE = 4
```

Slide, not slide down. Default means slide right, after mirroring it means slide left. Choosing to slide left or slide right is not supported.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DismissReason-SLIDE = 4--><!--Device-DismissReason-SLIDE = 4-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

