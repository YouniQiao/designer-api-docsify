# WindowChangeOptions

Describes the extended configuration of window change event listening, which is used to specify the listening process configuration and event filtering conditions.

**Since:** 23

**Deprecated since:** -1

<!--Device-unnamed-declare interface WindowChangeOptions--><!--Device-unnamed-declare interface WindowChangeOptions-End-->

**System capability:** SystemCapability.Test.UiTest

## Modules to Import

```TypeScript
import { ResizeDirection, WindowMode, PenMode, PenKeyOperation, Driver, MatchPattern, UiDirection, TouchOptions, ComponentEventType, PointerMatrix, WindowChangeType, Component, ON, PenKey, Rect, InputTextMode, UIEventObserver, WindowFilter, WindowChangeOptions, UiWindow, TouchPadSwipeOptions, Point, KeyOptions, DisplayRotation, UIElementInfo, PenKeyOperationOptions, ComponentEventOptions, MouseButton, On } from '@kit.TestKit';
```

## bundleName

```TypeScript
bundleName?: string
```

Bundle name of the window to be listened for. By default, all windows are listened for.

**Type:** string

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-WindowChangeOptions-bundleName?: string--><!--Device-WindowChangeOptions-bundleName?: string-End-->

**System capability:** SystemCapability.Test.UiTest

## timeout

```TypeScript
timeout?: number
```

Listening timeout interval, in milliseconds. The value is an integer greater than or equal to 500. The default value is **10000**. If the value is out of range, an error code is thrown.

**Type:** number

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-WindowChangeOptions-timeout?: int--><!--Device-WindowChangeOptions-timeout?: int-End-->

**System capability:** SystemCapability.Test.UiTest
