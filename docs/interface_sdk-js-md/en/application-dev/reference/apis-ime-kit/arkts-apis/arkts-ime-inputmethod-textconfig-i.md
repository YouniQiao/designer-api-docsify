# TextConfig

Describes the configuration of the edit box.

**Since:** 23

<!--Device-inputMethod-export interface TextConfig--><!--Device-inputMethod-export interface TextConfig-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

## Modules to Import

```TypeScript
import { inputMethod } from '@kit.IMEKit';
```

## capitalizeMode

```TypeScript
capitalizeMode?: CapitalizeMode
```

Whether to capitalize the first letter in the edit box. If it is not set or is set to an invalid value, the first letter is not capitalized by default.

**Type:** CapitalizeMode

**Default:** CapitalizeMode.NONE

**Since:** 23

<!--Device-TextConfig-capitalizeMode?: CapitalizeMode--><!--Device-TextConfig-capitalizeMode?: CapitalizeMode-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

## cursorInfo

```TypeScript
cursorInfo?: CursorInfo
```

Cursor information.

**Type:** [CursorInfo](arkts-ime-inputmethod-cursorinfo-i.md)

**Since:** 23

<!--Device-TextConfig-cursorInfo?: CursorInfo--><!--Device-TextConfig-cursorInfo?: CursorInfo-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

## inputAttribute

```TypeScript
inputAttribute: InputAttribute
```

Edit box attribute.

**Type:** [InputAttribute](arkts-ime-inputmethod-inputattribute-i.md)

**Since:** 23

<!--Device-TextConfig-inputAttribute: InputAttribute--><!--Device-TextConfig-inputAttribute: InputAttribute-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

## newEditBox

```TypeScript
newEditBox?: boolean
```

Whether the edit box is new. The value **true** means the edit box is new; the value **false** means the opposite.

**Type:** boolean

**Since:** 23

<!--Device-TextConfig-newEditBox?: boolean--><!--Device-TextConfig-newEditBox?: boolean-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

## selection

```TypeScript
selection?: Range
```

Text selection range.

**Type:** Range

**Since:** 23

<!--Device-TextConfig-selection?: Range--><!--Device-TextConfig-selection?: Range-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

## windowId

```TypeScript
windowId?: int
```

ID of the window where the edit box is located. The value must be an integer. <br> <br>You are advised to call [getWindowProperties](../../apis-arkui/arkts-apis/arkts-arkui-window-window-i.md#getwindowproperties) to obtain the window ID.

**Type:** int

**Since:** 23

<!--Device-TextConfig-windowId?: int--><!--Device-TextConfig-windowId?: int-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

