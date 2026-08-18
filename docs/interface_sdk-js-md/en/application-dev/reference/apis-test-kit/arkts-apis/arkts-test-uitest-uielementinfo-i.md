# UIElementInfo

Provides information about the UI event.

**Since:** 23

<!--Device-unnamed-declare interface UIElementInfo--><!--Device-unnamed-declare interface UIElementInfo-End-->

**System capability:** SystemCapability.Test.UiTest

## Modules to Import

```TypeScript
import { Component, DisplayRotation, Driver, MatchPattern, MouseButton, ON, On, PointerMatrix, ResizeDirection, UIElementInfo, UIEventObserver, UiDirection, UiWindow, WindowMode, Point, WindowFilter, Rect, TouchPadSwipeOptions, InputTextMode, WindowChangeType, ComponentEventType, WindowChangeOptions, ComponentEventOptions, TouchOptions, KeyOptions, PenKey, PenMode, PenKeyOperation, PenKeyOperationOptions } from '@kit.TestKit';
import { UiComponent, UiDriver, BY, By } from '@kit.TestKit';
```

## bundleName

```TypeScript
readonly bundleName: string
```

Bundle name of the application.

**Type:** string

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-UIElementInfo-readonly bundleName: string--><!--Device-UIElementInfo-readonly bundleName: string-End-->

**System capability:** SystemCapability.Test.UiTest

## componentEventType

```TypeScript
readonly componentEventType?: ComponentEventType
```

Component operation event type. If it is not a component operation event, [COMPONENT_UNDEFINED](arkts-test-uitest-componenteventtype-e.md#component_undefined) is returned.

**Type:** [ComponentEventType](arkts-test-uitest-componenteventtype-e.md)

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-UIElementInfo-readonly componentEventType?: ComponentEventType--><!--Device-UIElementInfo-readonly componentEventType?: ComponentEventType-End-->

**System capability:** SystemCapability.Test.UiTest

## componentId

```TypeScript
readonly componentId?: string
```

Component ID. If it is not a component operation event, an empty string is returned.

**Type:** string

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-UIElementInfo-readonly componentId?: string--><!--Device-UIElementInfo-readonly componentId?: string-End-->

**System capability:** SystemCapability.Test.UiTest

## componentRect

```TypeScript
readonly componentRect?: Rect
```

Component border information. If it is not a component operation event, a [Rect](arkts-test-uitest-rect-i.md) object whose attribute values are all **0** is returned.

**Type:** [Rect](arkts-test-uitest-rect-i.md)

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-UIElementInfo-readonly componentRect?: Rect--><!--Device-UIElementInfo-readonly componentRect?: Rect-End-->

**System capability:** SystemCapability.Test.UiTest

## text

```TypeScript
readonly text: string
```

Text information of the component or window.

**Type:** string

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-UIElementInfo-readonly text: string--><!--Device-UIElementInfo-readonly text: string-End-->

**System capability:** SystemCapability.Test.UiTest

## type

```TypeScript
readonly type: string
```

Component or window type.

**Type:** string

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-UIElementInfo-readonly type: string--><!--Device-UIElementInfo-readonly type: string-End-->

**System capability:** SystemCapability.Test.UiTest

## windowChangeType

```TypeScript
readonly windowChangeType?: WindowChangeType
```

Window change event type. If the event is not a window change event, [WINDOW_UNDEFINED](arkts-test-uitest-windowchangetype-e.md#window_undefined) is returned.

**Type:** [WindowChangeType](arkts-test-uitest-windowchangetype-e.md)

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-UIElementInfo-readonly windowChangeType?: WindowChangeType--><!--Device-UIElementInfo-readonly windowChangeType?: WindowChangeType-End-->

**System capability:** SystemCapability.Test.UiTest

## windowId

```TypeScript
readonly windowId?: int
```

ID of the window to which the component belongs. If it is not a component operation event, **-1** is returned.

**Type:** int

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-UIElementInfo-readonly windowId?: int--><!--Device-UIElementInfo-readonly windowId?: int-End-->

**System capability:** SystemCapability.Test.UiTest

