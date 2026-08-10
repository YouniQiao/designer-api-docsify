# Rect

控件的边框信息。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-unnamed-declare interface Rect--><!--Device-unnamed-declare interface Rect-End-->

**System capability:** SystemCapability.Test.UiTest

## Modules to Import

```TypeScript
import { ResizeDirection, WindowMode, PenMode, PenKeyOperation, Driver, MatchPattern, UiDirection, TouchOptions, ComponentEventType, PointerMatrix, WindowChangeType, Component, ON, PenKey, Rect, InputTextMode, UIEventObserver, WindowFilter, WindowChangeOptions, UiWindow, TouchPadSwipeOptions, Point, KeyOptions, DisplayRotation, UIElementInfo, PenKeyOperationOptions, ComponentEventOptions, MouseButton, On } from 'kits/@kit.TestKit';
```

## bottom

```TypeScript
bottom: int
```

控件边框的右下角的Y坐标，取值大于等于0的整数，单位：px。

**说明：** 从API version 20开始，该属性不再为只读属性。

从API version 11开始，该接口支持在原子化服务中使用。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Rect-bottom: int--><!--Device-Rect-bottom: int-End-->

**System capability:** SystemCapability.Test.UiTest

## displayId

```TypeScript
displayId?: int
```

控件边框所属的屏幕ID，取值大于或等于0的整数。默认值为设备默认屏幕ID。

从API version 20开始，该接口支持在原子化服务中使用。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-Rect-displayId?: int--><!--Device-Rect-displayId?: int-End-->

**System capability:** SystemCapability.Test.UiTest

## left

```TypeScript
left: int
```

控件边框的左上角的X坐标，取值大于等于0的整数，单位：px。

**说明：** 从API version 20开始，该属性不再为只读属性。

从API version 11开始，该接口支持在原子化服务中使用。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Rect-left: int--><!--Device-Rect-left: int-End-->

**System capability:** SystemCapability.Test.UiTest

## right

```TypeScript
right: int
```

控件边框的右下角的X坐标，取值大于等于0的整数，单位：px。

**说明：** 从API version 20开始，该属性不再为只读属性。

从API version 11开始，该接口支持在原子化服务中使用。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Rect-right: int--><!--Device-Rect-right: int-End-->

**System capability:** SystemCapability.Test.UiTest

## top

```TypeScript
top: int
```

控件边框的左上角的Y坐标，取值大于等于0的整数，单位：px。

**说明：** 从API version 20开始，该属性不再为只读属性。

从API version 11开始，该接口支持在原子化服务中使用。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Rect-top: int--><!--Device-Rect-top: int-End-->

**System capability:** SystemCapability.Test.UiTest

