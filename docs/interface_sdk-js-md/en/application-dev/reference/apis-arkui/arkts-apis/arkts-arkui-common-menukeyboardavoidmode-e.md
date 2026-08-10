# MenuKeyboardAvoidMode

Define the mode of menu how to avoid keyboard.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export declare enum MenuKeyboardAvoidMode--><!--Device-unnamed-export declare enum MenuKeyboardAvoidMode-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## NONE

```TypeScript
NONE = 0
```

Menu will not avoid keyboard.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-MenuKeyboardAvoidMode-NONE = 0--><!--Device-MenuKeyboardAvoidMode-NONE = 0-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## TRANSLATE_AND_RESIZE

```TypeScript
TRANSLATE_AND_RESIZE = 1
```

First menu will avoid keyboard by changing its placement.And then menu will avoid by resizing height when new placement is still not high enough.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-MenuKeyboardAvoidMode-TRANSLATE_AND_RESIZE = 1--><!--Device-MenuKeyboardAvoidMode-TRANSLATE_AND_RESIZE = 1-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

