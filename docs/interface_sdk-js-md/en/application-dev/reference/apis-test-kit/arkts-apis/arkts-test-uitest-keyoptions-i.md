# KeyOptions

Represents the options for key operations.

**Since:** 26.0.0

<!--Device-unnamed-declare interface KeyOptions--><!--Device-unnamed-declare interface KeyOptions-End-->

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

## key1

```TypeScript
key1?: int
```

The first keyCode to press during the operation. If not set, no key event will be injected. Setting only key2 without key1 will result in a BusinessError 17000007.

**Type:** int

**Since:** 26.0.0

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-KeyOptions-key1?: int--><!--Device-KeyOptions-key1?: int-End-->

**System capability:** SystemCapability.Test.UiTest

## key2

```TypeScript
key2?: int
```

The second KeyCode to press during the operation. If not set, no key event will be injected. Setting only key2 without key1 will result in a BusinessError 17000007.

**Type:** int

**Since:** 26.0.0

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-KeyOptions-key2?: int--><!--Device-KeyOptions-key2?: int-End-->

**System capability:** SystemCapability.Test.UiTest

