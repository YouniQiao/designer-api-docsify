# Point

坐标点信息。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-unnamed-declare interface Point--><!--Device-unnamed-declare interface Point-End-->

**System capability:** SystemCapability.Test.UiTest

## Modules to Import

```TypeScript
import { ResizeDirection, WindowMode, PenMode, PenKeyOperation, Driver, MatchPattern, UiDirection, TouchOptions, ComponentEventType, PointerMatrix, WindowChangeType, Component, ON, PenKey, Rect, InputTextMode, UIEventObserver, WindowFilter, WindowChangeOptions, UiWindow, TouchPadSwipeOptions, Point, KeyOptions, DisplayRotation, UIElementInfo, PenKeyOperationOptions, ComponentEventOptions, MouseButton, On } from 'kits/@kit.TestKit';
```

## displayId

```TypeScript
displayId?: int
```

坐标点所属的屏幕ID，取值范围：大于等于0的整数。默认值为设备默认屏幕ID。

从API version 20开始，该接口支持在原子化服务中使用。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-Point-displayId?: int--><!--Device-Point-displayId?: int-End-->

**System capability:** SystemCapability.Test.UiTest

## x

```TypeScript
x: int
```

坐标点的横坐标，取值大于等于0的整数，单位：px。

**说明：** 从API version 20开始，该属性不再为只读属性。

从API version 11开始，该接口支持在原子化服务中使用。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Point-x: int--><!--Device-Point-x: int-End-->

**System capability:** SystemCapability.Test.UiTest

## y

```TypeScript
y: int
```

坐标点的纵坐标，取值大于等于0的整数，单位：px。

**说明：** 从API version 20开始，该属性不再为只读属性。

从API version 11开始，该接口支持在原子化服务中使用。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Point-y: int--><!--Device-Point-y: int-End-->

**System capability:** SystemCapability.Test.UiTest

