# ComponentEventOptions

控件操作事件监听的扩展配置，用于指定监听过程配置及事件筛选条件。

**Since:** 22

**ArkTS mode:** ArkTS-Dyn since version 22; ArkTS-Sta since version 23.

<!--Device-unnamed-declare interface ComponentEventOptions--><!--Device-unnamed-declare interface ComponentEventOptions-End-->

**System capability:** SystemCapability.Test.UiTest

## Modules to Import

```TypeScript
import { ResizeDirection, WindowMode, PenMode, PenKeyOperation, Driver, MatchPattern, UiDirection, TouchOptions, ComponentEventType, PointerMatrix, WindowChangeType, Component, ON, PenKey, Rect, InputTextMode, UIEventObserver, WindowFilter, WindowChangeOptions, UiWindow, TouchPadSwipeOptions, Point, KeyOptions, DisplayRotation, UIElementInfo, PenKeyOperationOptions, ComponentEventOptions, MouseButton, On } from 'kits/@kit.TestKit';
```

## on

```TypeScript
on?: On
```

监听目标控件的属性要求，默认监听所有控件。

**说明：** 仅支持监听指定属性要求的控件，不支持监听指定On.isBefore、On.isAfter、On.within等相对位置的控件。

**Type:** [On](arkts-test-uitest-on-c.md)

**Since:** 22

**ArkTS mode:** ArkTS-Dyn since version 22; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-ComponentEventOptions-on?: On--><!--Device-ComponentEventOptions-on?: On-End-->

**System capability:** SystemCapability.Test.UiTest

## timeout

```TypeScript
timeout?: int
```

监听超时时间，取值范围：大于等于500的整数，默认值为10000，单位：ms。传入不在范围内的值抛出错误码。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 22

**ArkTS mode:** ArkTS-Dyn since version 22; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-ComponentEventOptions-timeout?: int--><!--Device-ComponentEventOptions-timeout?: int-End-->

**System capability:** SystemCapability.Test.UiTest

