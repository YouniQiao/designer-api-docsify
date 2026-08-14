# PenKeyOperationOptions

Pen key operation options.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Deprecated since:** -1

<!--Device-unnamed-declare interface PenKeyOperationOptions--><!--Device-unnamed-declare interface PenKeyOperationOptions-End-->

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

## point

```TypeScript
point?: Point
```

The coordinate point for air mouse mode operations. Required when key is AIR_MOUSE in air mouse mode.

**Type:** [Point](arkts-test-uitest-point-i.md)

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-PenKeyOperationOptions-point?: Point--><!--Device-PenKeyOperationOptions-point?: Point-End-->

**System capability:** SystemCapability.Test.UiTest

