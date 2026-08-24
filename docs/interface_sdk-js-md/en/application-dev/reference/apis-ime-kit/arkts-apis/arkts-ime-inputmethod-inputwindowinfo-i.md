# InputWindowInfo

Describes the window information of the input method keyboard.

**Since:** 23

<!--Device-inputMethod-export interface InputWindowInfo--><!--Device-inputMethod-export interface InputWindowInfo-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

## Modules to Import

```TypeScript
import { inputMethod } from '@kit.IMEKit';
```

## displayId

```TypeScript
displayId?: long
```

ID of the display where the soft keyboard window is located. <br> <br>**Model restriction**: This parameter can be used only in the stage model.

**Type:** long

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-InputWindowInfo-displayId?: long--><!--Device-InputWindowInfo-displayId?: long-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

## height

```TypeScript
height: long
```

Height of the input method keyboard window, in px. The value must be an integer. The minimum value is 0 and the maximum value is the height of the current screen.

**Type:** long

**Since:** 23

<!--Device-InputWindowInfo-height: long--><!--Device-InputWindowInfo-height: long-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

## left

```TypeScript
left: int
```

Horizontal coordinate of the upper left corner of the input method keyboard window, in px. The value must be an integer. The minimum value is 0 and the maximum value is the width of the current screen.

**Type:** int

**Since:** 23

<!--Device-InputWindowInfo-left: int--><!--Device-InputWindowInfo-left: int-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

## name

```TypeScript
name: string
```

Name of the input method keyboard window.

**Type:** string

**Since:** 23

<!--Device-InputWindowInfo-name: string--><!--Device-InputWindowInfo-name: string-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

## top

```TypeScript
top: int
```

Vertical coordinate of the upper left corner of the input method keyboard window, in px. The value must be an integer. The minimum value is 0 and the maximum value is the height of the current screen.

**Type:** int

**Since:** 23

<!--Device-InputWindowInfo-top: int--><!--Device-InputWindowInfo-top: int-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

## width

```TypeScript
width: long
```

Width of the input method keyboard window, in px. The value must be an integer. The minimum value is 0 and the maximum value is the width of the current screen.

**Type:** long

**Since:** 23

<!--Device-InputWindowInfo-width: long--><!--Device-InputWindowInfo-width: long-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

