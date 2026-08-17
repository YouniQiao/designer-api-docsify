# TouchOptions

Common options for touch operations.

**Since:** 26.0.0

<!--Device-unnamed-declare interface TouchOptions--><!--Device-unnamed-declare interface TouchOptions-End-->

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

## duration

```TypeScript
duration?: int
```

Duration of the operation in milliseconds. <br>Value range: The value should be >= 1500 <br>Unit: ms <br>Default value: 1500

**Type:** int

**Since:** 26.0.0

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-TouchOptions-duration?: int--><!--Device-TouchOptions-duration?: int-End-->

**System capability:** SystemCapability.Test.UiTest

## pressure

```TypeScript
pressure?: double
```

Pressure value of the touch. The value range is [0, 1]. The default value is **0**. If the value is **null** or **undefined**, the default value is used. If the value is out of the value range, the 17000007 error code is thrown.

**Type:** double

**Since:** 26.0.0

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-TouchOptions-pressure?: double--><!--Device-TouchOptions-pressure?: double-End-->

**System capability:** SystemCapability.Test.UiTest

## speed

```TypeScript
speed?: int
```

Speed of touch action. <br>Value range:[200, 40000] <br>Unit: px/s. <br>If the value is out of range or null/undefined, the default value 600 is used. <br>Default value: 600

**Type:** int

**Since:** 26.0.0

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-TouchOptions-speed?: int--><!--Device-TouchOptions-speed?: int-End-->

**System capability:** SystemCapability.Test.UiTest

