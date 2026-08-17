# InputTextMode

Describes the text input mode.

**Since:** 23

<!--Device-unnamed-declare interface InputTextMode--><!--Device-unnamed-declare interface InputTextMode-End-->

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

## addition

```TypeScript
addition?: boolean
```

Whether to input text in addition mode. The value **true** means to input text in addition mode, and **false** means the opposite. Default value: **false**

**Type:** boolean

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-InputTextMode-addition?: boolean--><!--Device-InputTextMode-addition?: boolean-End-->

**System capability:** SystemCapability.Test.UiTest

## paste

```TypeScript
paste?: boolean
```

Whether to copy and paste text. The value **true** means to copy and paste text, and **false** means to type text. Default value: **false** **Note：**: If the input text contains Chinese characters, special characters, or the text length exceeds 200 characters, the text is copied and pasted regardless of the value of this parameter.

**Type:** boolean

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-InputTextMode-paste?: boolean--><!--Device-InputTextMode-paste?: boolean-End-->

**System capability:** SystemCapability.Test.UiTest

