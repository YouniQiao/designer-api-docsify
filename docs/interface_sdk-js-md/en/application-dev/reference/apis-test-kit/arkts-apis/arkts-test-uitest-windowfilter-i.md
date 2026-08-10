# WindowFilter

窗口的标志属性信息。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-unnamed-declare interface WindowFilter--><!--Device-unnamed-declare interface WindowFilter-End-->

**System capability:** SystemCapability.Test.UiTest

## Modules to Import

```TypeScript
import { ResizeDirection, WindowMode, PenMode, PenKeyOperation, Driver, MatchPattern, UiDirection, TouchOptions, ComponentEventType, PointerMatrix, WindowChangeType, Component, ON, PenKey, Rect, InputTextMode, UIEventObserver, WindowFilter, WindowChangeOptions, UiWindow, TouchPadSwipeOptions, Point, KeyOptions, DisplayRotation, UIElementInfo, PenKeyOperationOptions, ComponentEventOptions, MouseButton, On } from 'kits/@kit.TestKit';
```

## active

```TypeScript
active?: boolean
```

窗口是否正与用户进行交互，true：交互状态，false：未交互状态，默认值为false。

从API version 11开始，该接口支持在原子化服务中使用。

**Type:** boolean

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-WindowFilter-active?: boolean--><!--Device-WindowFilter-active?: boolean-End-->

**System capability:** SystemCapability.Test.UiTest

## actived

```TypeScript
actived?: boolean
```

窗口是否正与用户进行交互，true：交互状态，false：未交互状态，默认值为false。

从API version 11开始废弃，建议使用active替代。

**Type:** boolean

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

**Deprecated since:** 11

**Substitutes:** ohos.UiTest.WindowFilter#active

<!--Device-WindowFilter-actived?: boolean--><!--Device-WindowFilter-actived?: boolean-End-->

**System capability:** SystemCapability.Test.UiTest

## bundleName

```TypeScript
bundleName?: string
```

窗口归属应用的包名，默认值为空，用于在多窗口场景下根据应用包名筛选目标窗口。

从API version 11开始，该接口支持在原子化服务中使用。

**Type:** string

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-WindowFilter-bundleName?: string--><!--Device-WindowFilter-bundleName?: string-End-->

**System capability:** SystemCapability.Test.UiTest

## displayId

```TypeScript
displayId?: int
```

窗口所属的屏幕ID。取值大于或等于0的整数。默认值为设备默认屏幕ID。

从API version 20开始，该接口支持在原子化服务中使用。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-WindowFilter-displayId?: int--><!--Device-WindowFilter-displayId?: int-End-->

**System capability:** SystemCapability.Test.UiTest

## focused

```TypeScript
focused?: boolean
```

窗口是否处于获焦状态，true：获焦状态，false：未获焦状态，默认值为false。

从API version 11开始，该接口支持在原子化服务中使用。

**Type:** boolean

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-WindowFilter-focused?: boolean--><!--Device-WindowFilter-focused?: boolean-End-->

**System capability:** SystemCapability.Test.UiTest

## title

```TypeScript
title?: string
```

窗口的标题信息，默认值为空，用于在多窗口场景下根据窗口标题筛选目标窗口。 从API version 11开始，该接口支持在原子化服务中使用。

**Type:** string

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-WindowFilter-title?: string--><!--Device-WindowFilter-title?: string-End-->

**System capability:** SystemCapability.Test.UiTest

