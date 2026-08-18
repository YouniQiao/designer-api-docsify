# InputWindowInfo

Information of input window.

**Since:** 23

<!--Device-inputMethod-export interface InputWindowInfo--><!--Device-inputMethod-export interface InputWindowInfo-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

## Modules to Import

```TypeScript
import { inputMethod } from '@kit.IMEKit';
import { inputMethodEngine } from '@kit.IMEKit';
import { InputMethodListDialog, PatternOptions, Pattern } from '@kit.IMEKit';
import { PanelInfo, PanelType, PanelFlag } from '@kit.IMEKit';
import { InputMethodExtraConfig } from '@kit.IMEKit';
import { inputMethodSystemPanelManager } from '@kit.IMEKit';
```

## displayId

```TypeScript
displayId?: long
```

Indicates the id of the display where the input window is shown.

**Type:** long

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-InputWindowInfo-displayId?: long--><!--Device-InputWindowInfo-displayId?: long-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

## height

```TypeScript
height: long
```

Indicates the height of the input window, unit is px.

**Type:** long

**Since:** 23

<!--Device-InputWindowInfo-height: long--><!--Device-InputWindowInfo-height: long-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

## left

```TypeScript
left: int
```

Indicates the abscissa of the upper-left vertex of input window, unit is px.

**Type:** int

**Since:** 23

<!--Device-InputWindowInfo-left: int--><!--Device-InputWindowInfo-left: int-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

## name

```TypeScript
name: string
```

Indicates name of the input window.

**Type:** string

**Since:** 23

<!--Device-InputWindowInfo-name: string--><!--Device-InputWindowInfo-name: string-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

## top

```TypeScript
top: int
```

Indicates the ordinate of the upper-left vertex of input window, unit is px.

**Type:** int

**Since:** 23

<!--Device-InputWindowInfo-top: int--><!--Device-InputWindowInfo-top: int-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

## width

```TypeScript
width: long
```

Indicates the width of the input window, unit is px.

**Type:** long

**Since:** 23

<!--Device-InputWindowInfo-width: long--><!--Device-InputWindowInfo-width: long-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

