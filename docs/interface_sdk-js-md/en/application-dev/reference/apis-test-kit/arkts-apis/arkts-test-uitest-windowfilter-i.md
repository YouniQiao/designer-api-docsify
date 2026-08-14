# WindowFilter

Provides the flag attributes of this window.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-unnamed-declare interface WindowFilter--><!--Device-unnamed-declare interface WindowFilter-End-->

**System capability:** SystemCapability.Test.UiTest

## Modules to Import

```TypeScript
import { Component } from 'Component';
import { DisplayRotation } from 'DisplayRotation';
import { Driver } from 'Driver';
import { MatchPattern } from 'MatchPattern';
import { MouseButton } from 'MouseButton';
import { ON } from 'ON';
import { On } from 'On';
import { PointerMatrix } from 'PointerMatrix';
import { ResizeDirection } from 'ResizeDirection';
import { UIElementInfo } from 'UIElementInfo';
import { UIEventObserver } from 'UIEventObserver';
import { UiDirection } from 'UiDirection';
import { UiWindow } from 'UiWindow';
import { WindowMode } from 'WindowMode';
import { Point } from 'Point';
import { WindowFilter } from 'WindowFilter';
import { Rect } from 'Rect';
import { TouchPadSwipeOptions } from 'TouchPadSwipeOptions';
import { InputTextMode } from 'InputTextMode';
import { WindowChangeType } from 'WindowChangeType';
import { ComponentEventType } from 'ComponentEventType';
import { WindowChangeOptions } from 'WindowChangeOptions';
import { ComponentEventOptions } from 'ComponentEventOptions';
import { TouchOptions } from 'TouchOptions';
import { KeyOptions } from 'KeyOptions';
import { PenKey } from 'PenKey';
import { PenMode } from 'PenMode';
import { PenKeyOperation } from 'PenKeyOperation';
import { PenKeyOperationOptions } from 'PenKeyOperationOptions';
```

## active

```TypeScript
active?: boolean
```

Whether the window is interacting with the user. The value **true** indicates that the window is interacting with the user, and **false** indicates the opposite.

**Type:** boolean

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-WindowFilter-active?: boolean--><!--Device-WindowFilter-active?: boolean-End-->

**System capability:** SystemCapability.Test.UiTest

## actived

```TypeScript
actived?: boolean
```

Whether the window is interacting with the user. The value **true** indicates that the window is interacting with the user, and **false** indicates the opposite. This API is supported since API version 9 and deprecated since API version 11. You are advised to use [active](#active) instead.

**Type:** boolean

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

**Deprecated since:** 11

**Substitutes:** active

<!--Device-WindowFilter-actived?: boolean--><!--Device-WindowFilter-actived?: boolean-End-->

**System capability:** SystemCapability.Test.UiTest

## bundleName

```TypeScript
bundleName?: string
```

Bundle name of the application to which the window belongs, which is used to filter the target window in multi-window scenarios. This parameter is left empty by default.

**Type:** string

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-WindowFilter-bundleName?: string--><!--Device-WindowFilter-bundleName?: string-End-->

**System capability:** SystemCapability.Test.UiTest

## displayId

```TypeScript
displayId?: int
```

ID of the display to which the window belongs. The value is an integer greater than or equal to 0. The default value is the default screen ID of the device.

**Type:** int

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-WindowFilter-displayId?: int--><!--Device-WindowFilter-displayId?: int-End-->

**System capability:** SystemCapability.Test.UiTest

## focused

```TypeScript
focused?: boolean
```

Whether the window is focused. The value **true** indicates that the window is focused, and **false** indicates the opposite. The default value is **false**.

**Type:** boolean

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-WindowFilter-focused?: boolean--><!--Device-WindowFilter-focused?: boolean-End-->

**System capability:** SystemCapability.Test.UiTest

## title

```TypeScript
title?: string
```

Window title, which is used to filter the target window in multi-window scenarios. This parameter is left empty by default.

**Type:** string

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-WindowFilter-title?: string--><!--Device-WindowFilter-title?: string-End-->

**System capability:** SystemCapability.Test.UiTest

