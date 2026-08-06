# SheetKeyboardAvoidMode

Define the mode of sheet how to avoid keyboard.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export declare enum SheetKeyboardAvoidMode--><!--Device-unnamed-export declare enum SheetKeyboardAvoidMode-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## NONE

```TypeScript
NONE = 0
```

Sheet will not aovid keyboard.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SheetKeyboardAvoidMode-NONE = 0--><!--Device-SheetKeyboardAvoidMode-NONE = 0-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## TRANSLATE_AND_RESIZE

```TypeScript
TRANSLATE_AND_RESIZE = 1
```

Firstly sheet will avoid keyboard by changing its height. And then sheet will avoid by resizing after reaching its maximum height.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SheetKeyboardAvoidMode-TRANSLATE_AND_RESIZE = 1--><!--Device-SheetKeyboardAvoidMode-TRANSLATE_AND_RESIZE = 1-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## RESIZE_ONLY

```TypeScript
RESIZE_ONLY = 2
```

Sheet will only avoid keyboard by resizing the content.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SheetKeyboardAvoidMode-RESIZE_ONLY = 2--><!--Device-SheetKeyboardAvoidMode-RESIZE_ONLY = 2-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## TRANSLATE_AND_SCROLL

```TypeScript
TRANSLATE_AND_SCROLL = 3
```

Firstly sheet will avoid keyboard by changing its height. And then sheet will avoid keyboard by scrolling after reaching its maximum height.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SheetKeyboardAvoidMode-TRANSLATE_AND_SCROLL = 3--><!--Device-SheetKeyboardAvoidMode-TRANSLATE_AND_SCROLL = 3-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## POPUP_SHEET

```TypeScript
POPUP_SHEET = 4
```

Popup sheet will avoid keyboard by default.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SheetKeyboardAvoidMode-POPUP_SHEET = 4--><!--Device-SheetKeyboardAvoidMode-POPUP_SHEET = 4-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

