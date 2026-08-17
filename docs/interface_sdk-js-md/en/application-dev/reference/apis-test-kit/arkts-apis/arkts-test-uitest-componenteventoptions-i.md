# ComponentEventOptions

Describes the extended configuration of component operation event listening, which is used to specify the listening process configuration and event filtering conditions.

**Since:** 23

<!--Device-unnamed-declare interface ComponentEventOptions--><!--Device-unnamed-declare interface ComponentEventOptions-End-->

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

## on

```TypeScript
on?: On
```

Attribute requirements of the target component to listen for. By default, all components are listened for. **Note：**: Only components with specified attributes can be listened for. Components with relative positions such as **On.isBefore**, **On.isAfter**, and **On.within** cannot be listened for.

**Type:** [On](arkts-test-uitest-on-c.md)

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-ComponentEventOptions-on?: On--><!--Device-ComponentEventOptions-on?: On-End-->

**System capability:** SystemCapability.Test.UiTest

## timeout

```TypeScript
timeout?: int
```

Listening timeout interval, in milliseconds. The value is an integer greater than or equal to 500. The default value is **10000**. If the value is out of range, an error code is thrown.

**Type:** int

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-ComponentEventOptions-timeout?: int--><!--Device-ComponentEventOptions-timeout?: int-End-->

**System capability:** SystemCapability.Test.UiTest

