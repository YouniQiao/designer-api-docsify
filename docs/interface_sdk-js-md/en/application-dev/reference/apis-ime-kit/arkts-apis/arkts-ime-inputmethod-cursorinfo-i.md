# CursorInfo

Information of Cursor.

**Since:** 10

<!--Device-inputMethod-export interface CursorInfo--><!--Device-inputMethod-export interface CursorInfo-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

## Modules to Import

```TypeScript
import { inputMethod } from '@kit.IMEKit';
```

## displayId

```TypeScript
displayId?: number
```

Indicates the ID of the display where the cursor locates.

**Type:** number

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-CursorInfo-displayId?: long--><!--Device-CursorInfo-displayId?: long-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

## height

```TypeScript
height: number
```

Indicates the height point of the cursor info, unit is px.

**Type:** number

**Since:** 10

<!--Device-CursorInfo-height: double--><!--Device-CursorInfo-height: double-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

## left

```TypeScript
left: number
```

Indicates the left point of the cursor info and must be absolute coordinate of the physical screen, unit is px.

**Type:** number

**Since:** 10

<!--Device-CursorInfo-left: double--><!--Device-CursorInfo-left: double-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

## top

```TypeScript
top: number
```

Indicates the top point of the cursor info and must be absolute coordinate of the physical screen, unit is px.

**Type:** number

**Since:** 10

<!--Device-CursorInfo-top: double--><!--Device-CursorInfo-top: double-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

## width

```TypeScript
width: number
```

Indicates the width point of the cursor info, unit is px.

**Type:** number

**Since:** 10

<!--Device-CursorInfo-width: double--><!--Device-CursorInfo-width: double-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

