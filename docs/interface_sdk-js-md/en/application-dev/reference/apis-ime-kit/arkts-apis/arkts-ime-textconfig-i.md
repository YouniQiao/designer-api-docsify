# TextConfig

Config of editor.

**Since:** 10

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

Indicates the capitalize mode of the edit box.

**Type:** CapitalizeMode

**Default:** CapitalizeMode.NONE

**Since:** 20

<!--Device-TextConfig-capitalizeMode?: CapitalizeMode--><!--Device-TextConfig-capitalizeMode?: CapitalizeMode-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

## cursorInfo

```TypeScript
cursorInfo?: CursorInfo
```

Cursor information.

**Type:** CursorInfo

**Since:** 10

<!--Device-TextConfig-cursorInfo?: CursorInfo--><!--Device-TextConfig-cursorInfo?: CursorInfo-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

## inputAttribute

```TypeScript
inputAttribute: InputAttribute
```

Attribute of Input.

**Type:** InputAttribute

**Since:** 10

<!--Device-TextConfig-inputAttribute: InputAttribute--><!--Device-TextConfig-inputAttribute: InputAttribute-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

## newEditBox

```TypeScript
newEditBox?: boolean
```

Indicates that this is a new edit box.

**Type:** boolean

**Since:** 20

<!--Device-TextConfig-newEditBox?: boolean--><!--Device-TextConfig-newEditBox?: boolean-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

## selection

```TypeScript
selection?: Range
```

Selection information.

**Type:** Range

**Since:** 10

<!--Device-TextConfig-selection?: Range--><!--Device-TextConfig-selection?: Range-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

## windowId

```TypeScript
windowId?: number
```

The window ID of the application currently bound to the input method.

**Type:** number

**Since:** 10

<!--Device-TextConfig-windowId?: int--><!--Device-TextConfig-windowId?: int-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

