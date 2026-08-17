# UIElementInfo

Provides information about the UI event.

**Since:** 23

<!--Device-unnamed-declare interface UIElementInfo--><!--Device-unnamed-declare interface UIElementInfo-End-->

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

Component operation event type. If it is not a component operation event, [COMPONENT_UNDEFINED](arkts-test-uitest-componenteventtype-e.md#componentundefined) is returned.

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

Component border information. If it is not a component operation event, a [Rect](arkts-test-uitest-rect-i.md#rect) object whose attribute values are all **0** is returned.

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

Window change event type. If the event is not a window change event, [WINDOW_UNDEFINED](arkts-test-uitest-windowchangetype-e.md#windowundefined) is returned.

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

