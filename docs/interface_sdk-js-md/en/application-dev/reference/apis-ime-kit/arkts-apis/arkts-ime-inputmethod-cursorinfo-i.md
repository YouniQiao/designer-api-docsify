# CursorInfo

光标信息。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

<!--Device-inputMethod-export interface CursorInfo--><!--Device-inputMethod-export interface CursorInfo-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

## Modules to Import

```TypeScript
import { inputMethod } from 'kits/@kit.IMEKit';
```

## displayId

```TypeScript
displayId?: long
```

光标所在显示器的ID。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：long

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CursorInfo-displayId?: long--><!--Device-CursorInfo-displayId?: long-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

## height

```TypeScript
height: double
```

光标的高度，单位为px。该参数应为整数，最小值为0，最大值为当前屏幕的高度。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：double

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

<!--Device-CursorInfo-height: double--><!--Device-CursorInfo-height: double-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

## left

```TypeScript
left: double
```

光标的横坐标，单位为px。该参数应为整数，最小值为0，最大值为当前屏幕的宽度。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：double

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

<!--Device-CursorInfo-left: double--><!--Device-CursorInfo-left: double-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

## top

```TypeScript
top: double
```

光标的纵坐标，单位为px。该参数应为整数，最小值为0，最大值为当前屏幕的高度。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：double

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

<!--Device-CursorInfo-top: double--><!--Device-CursorInfo-top: double-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

## width

```TypeScript
width: double
```

光标的宽度，单位为px。该参数应为整数，最小值为0，最大值为当前屏幕的宽度。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：double

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

<!--Device-CursorInfo-width: double--><!--Device-CursorInfo-width: double-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

