# UiWindow

The **UiWindow** class represents a window on the UI and provides APIs for obtaining window attributes, dragging a window, and adjusting the window size. All APIs provided in this class use a promise to return the result and must be invoked using **await**.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-unnamed-declare class UiWindow--><!--Device-unnamed-declare class UiWindow-End-->

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

## close

```TypeScript
close(): Promise<void>
```

Closes a window. This API uses a promise to return the result.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-UiWindow-close(): Promise<void>--><!--Device-UiWindow-close(): Promise<void>-End-->

**System capability:** SystemCapability.Test.UiTest

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [17000002](../errorcode-uitest.md#17000002-api-does-not-support-concurrent-calls) | The API does not support concurrent calls. |
| [17000005](../errorcode-uitest.md#17000005-operation-not-supported) | This operation is not supported. |
| [17000004](../errorcode-uitest.md#17000004-target-componentwindow-invisible-or-destroyed) | The window or component is invisible or destroyed. |

## Examples

```TypeScript
// xxx.test.ets
import { Driver, UiWindow } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  let window: UiWindow = await driver.findWindow({ actived: true });
  await window.close();
}
```

## focus

```TypeScript
focus(): Promise<void>
```

Focuses a window. This API uses a promise to return the result.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-UiWindow-focus(): Promise<void>--><!--Device-UiWindow-focus(): Promise<void>-End-->

**System capability:** SystemCapability.Test.UiTest

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [17000002](../errorcode-uitest.md#17000002-api-does-not-support-concurrent-calls) | The API does not support concurrent calls. |
| [17000004](../errorcode-uitest.md#17000004-target-componentwindow-invisible-or-destroyed) | The window or component is invisible or destroyed. |

## Examples

```TypeScript
// xxx.test.ets
import { Driver, UiWindow } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  let window: UiWindow = await driver.findWindow({ actived: true });
  await window.focus();
}
```

## getBounds

```TypeScript
getBounds(): Promise<Rect>
```

Obtains the bounds information of a window. This API uses a promise to return the result.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-UiWindow-getBounds(): Promise<Rect>--><!--Device-UiWindow-getBounds(): Promise<Rect>-End-->

**System capability:** SystemCapability.Test.UiTest

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;[Rect](arkts-test-uitest-rect-i.md)&gt; | Promise used to return the window border information. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [17000002](../errorcode-uitest.md#17000002-api-does-not-support-concurrent-calls) | The API does not support concurrent calls. |
| [17000004](../errorcode-uitest.md#17000004-target-componentwindow-invisible-or-destroyed) | The window or component is invisible or destroyed. |

## Examples

```TypeScript
// xxx.test.ets
import { Driver, UiWindow } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  let window: UiWindow = await driver.findWindow({ actived: true });
  let rect = await window.getBounds();
}
```

## getBundleName

```TypeScript
getBundleName(): Promise<string>
```

Obtains the bundle name of the application to which a window belongs. This API uses a promise to return the result.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-UiWindow-getBundleName(): Promise<string>--><!--Device-UiWindow-getBundleName(): Promise<string>-End-->

**System capability:** SystemCapability.Test.UiTest

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;string&gt; | Promise used to return the bundle name of the application to which the window belongs. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [17000002](../errorcode-uitest.md#17000002-api-does-not-support-concurrent-calls) | The API does not support concurrent calls. |
| [17000004](../errorcode-uitest.md#17000004-target-componentwindow-invisible-or-destroyed) | The window or component is invisible or destroyed. |

## Examples

```TypeScript
// xxx.test.ets
import { Driver, UiWindow } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  let window: UiWindow = await driver.findWindow({ actived: true });
  let name: string = await window.getBundleName();
}
```

## getDisplayId

```TypeScript
getDisplayId(): Promise<int>
```

Obtains the ID of the display to which a window belongs. This API uses a promise to return the result.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-UiWindow-getDisplayId(): Promise<int>--><!--Device-UiWindow-getDisplayId(): Promise<int>-End-->

**System capability:** SystemCapability.Test.UiTest

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;int&gt; | Promise used to return the ID of the display to which the window belongs. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [17000002](../errorcode-uitest.md#17000002-api-does-not-support-concurrent-calls) | The API does not support concurrent calls. |
| [17000004](../errorcode-uitest.md#17000004-target-componentwindow-invisible-or-destroyed) | The window or component is invisible or destroyed. |

## Examples

```TypeScript
// xxx.test.ets
import { UiWindow, Driver } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  let window: UiWindow = await driver.findWindow({ active: true });
  let id = await window.getDisplayId();
}
```

## getTitle

```TypeScript
getTitle(): Promise<string>
```

Obtains the window title. This API uses a promise to return the result.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-UiWindow-getTitle(): Promise<string>--><!--Device-UiWindow-getTitle(): Promise<string>-End-->

**System capability:** SystemCapability.Test.UiTest

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;string&gt; | Promise used to return the window title. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [17000002](../errorcode-uitest.md#17000002-api-does-not-support-concurrent-calls) | The API does not support concurrent calls. |
| [17000004](../errorcode-uitest.md#17000004-target-componentwindow-invisible-or-destroyed) | The window or component is invisible or destroyed. |

## Examples

```TypeScript
// xxx.test.ets
import { Driver, UiWindow } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  let window: UiWindow = await driver.findWindow({ actived: true });
  let title = await window.getTitle();
}
```

## getWindowMode

```TypeScript
getWindowMode(): Promise<WindowMode>
```

Obtains the window mode. This API uses a promise to return the result.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-UiWindow-getWindowMode(): Promise<WindowMode>--><!--Device-UiWindow-getWindowMode(): Promise<WindowMode>-End-->

**System capability:** SystemCapability.Test.UiTest

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;[WindowMode](arkts-test-uitest-windowmode-e.md)&gt; | Promise used to return the window mode information. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [17000002](../errorcode-uitest.md#17000002-api-does-not-support-concurrent-calls) | The API does not support concurrent calls. |
| [17000004](../errorcode-uitest.md#17000004-target-componentwindow-invisible-or-destroyed) | The window or component is invisible or destroyed. |

## Examples

```TypeScript
// xxx.test.ets
import { Driver, UiWindow } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  let window: UiWindow = await driver.findWindow({ actived: true });
  let mode = await window.getWindowMode();
}
```

## isActive

```TypeScript
isActive(): Promise<boolean>
```

Checks whether a window is active. This API uses a promise to return the result.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-UiWindow-isActive(): Promise<boolean>--><!--Device-UiWindow-isActive(): Promise<boolean>-End-->

**System capability:** SystemCapability.Test.UiTest

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;boolean&gt; | Promise used to return whether the window is active. The value **true** indicates that the window is active, and **false** indicates the opposite. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [17000002](../errorcode-uitest.md#17000002-api-does-not-support-concurrent-calls) | The API does not support concurrent calls. |
| [17000004](../errorcode-uitest.md#17000004-target-componentwindow-invisible-or-destroyed) | The window or component is invisible or destroyed. |

## Examples

```TypeScript
// xxx.test.ets
import { Driver, UiWindow } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  let window: UiWindow = await driver.findWindow({ active: true });
  let focused = await window.isActive();
}
```

## isActived

```TypeScript
isActived(): Promise<boolean>
```

Checks whether a window is active. This API uses a promise to return the result.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

**Deprecated since:** 11

**Substitutes:** [isActive](#isActive)

<!--Device-UiWindow-isActived(): Promise<boolean>--><!--Device-UiWindow-isActived(): Promise<boolean>-End-->

**System capability:** SystemCapability.Test.UiTest

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;boolean&gt; | Promise used to return whether the window is active. The value **true** indicates that the window is active, and **false** indicates the opposite. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [17000002](../errorcode-uitest.md#17000002-api-does-not-support-concurrent-calls) | The API does not support concurrent calls. |
| [17000004](../errorcode-uitest.md#17000004-target-componentwindow-invisible-or-destroyed) | The window or component is invisible or destroyed. |

## Examples

```TypeScript
// xxx.test.ets
import { Driver, UiWindow } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  let window: UiWindow = await driver.findWindow({ actived: true });
  let focused = await window.isActived();
}
```

## isFocused

```TypeScript
isFocused(): Promise<boolean>
```

Checks whether a window is focused. This API uses a promise to return the result.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-UiWindow-isFocused(): Promise<boolean>--><!--Device-UiWindow-isFocused(): Promise<boolean>-End-->

**System capability:** SystemCapability.Test.UiTest

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;boolean&gt; | Promise used to return the result of whether the window is focused. The value **true** indicates that the component is focused, and **false** indicates the opposite. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [17000002](../errorcode-uitest.md#17000002-api-does-not-support-concurrent-calls) | The API does not support concurrent calls. |
| [17000004](../errorcode-uitest.md#17000004-target-componentwindow-invisible-or-destroyed) | The window or component is invisible or destroyed. |

## Examples

```TypeScript
// xxx.test.ets
import { Driver, UiWindow } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  let window: UiWindow = await driver.findWindow({ actived: true });
  let focused = await window.isFocused();
}
```

## maximize

```TypeScript
maximize(): Promise<void>
```

Maximizes a window. A window can be resumed to its previous mode using [resume](#resume). This API uses a promise to return the result. This API is applicable to windows that can be maximized.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-UiWindow-maximize(): Promise<void>--><!--Device-UiWindow-maximize(): Promise<void>-End-->

**System capability:** SystemCapability.Test.UiTest

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [17000002](../errorcode-uitest.md#17000002-api-does-not-support-concurrent-calls) | The API does not support concurrent calls. |
| [17000005](../errorcode-uitest.md#17000005-operation-not-supported) | This operation is not supported. |
| [17000004](../errorcode-uitest.md#17000004-target-componentwindow-invisible-or-destroyed) | The window or component is invisible or destroyed. |

## Examples

```TypeScript
// xxx.test.ets
import { Driver, UiWindow } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  let window: UiWindow = await driver.findWindow({ actived: true });
  await window.maximize();
}
```

## minimize

```TypeScript
minimize(): Promise<void>
```

Minimizes a window. A window can be resumed to its previous mode using [resume](#resume). This API uses a promise to return the result. This API is applicable to windows that can be minimized.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-UiWindow-minimize(): Promise<void>--><!--Device-UiWindow-minimize(): Promise<void>-End-->

**System capability:** SystemCapability.Test.UiTest

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [17000002](../errorcode-uitest.md#17000002-api-does-not-support-concurrent-calls) | The API does not support concurrent calls. |
| [17000005](../errorcode-uitest.md#17000005-operation-not-supported) | This operation is not supported. |
| [17000004](../errorcode-uitest.md#17000004-target-componentwindow-invisible-or-destroyed) | The window or component is invisible or destroyed. |

## Examples

```TypeScript
// xxx.test.ets
import { Driver, UiWindow } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  let window: UiWindow = await driver.findWindow({ actived: true });
  await window.minimize();
}
```

## moveTo

```TypeScript
moveTo(x: int, y: int): Promise<void>
```

Moves a window to the target point. This API uses a promise to return the result. This API is applicable to moveable windows.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-UiWindow-moveTo(x: int, y: int): Promise<void>--><!--Device-UiWindow-moveTo(x: int, y: int): Promise<void>-End-->

**System capability:** SystemCapability.Test.UiTest

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| x | int | Yes | Horizontal coordinate of the target point, in pixels. The value is an integer greater than or equal to 0. If the value is out of range, error code 401 is thrown. |
| y | int | Yes | Vertical coordinate of the target point, in pixels. The value is an integer greater than or equal to 0. If the value is out of range, error code 401 is thrown. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| [17000002](../errorcode-uitest.md#17000002-api-does-not-support-concurrent-calls) | The API does not support concurrent calls. |
| [17000005](../errorcode-uitest.md#17000005-operation-not-supported) | This operation is not supported. |
| [17000004](../errorcode-uitest.md#17000004-target-componentwindow-invisible-or-destroyed) | The window or component is invisible or destroyed. |

## Examples

```TypeScript
// xxx.test.ets
import { Driver, UiWindow } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  let window: UiWindow = await driver.findWindow({ actived: true });
  await window.moveTo(100, 100);
}
```

## resize

```TypeScript
resize(wide: int, height: int, direction: ResizeDirection): Promise<void>
```

Resizes a window based on the specified width, height, and direction. This API uses a promise to return the result. This API is applicable to resizable windows.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-UiWindow-resize(wide: int, height: int, direction: ResizeDirection): Promise<void>--><!--Device-UiWindow-resize(wide: int, height: int, direction: ResizeDirection): Promise<void>-End-->

**System capability:** SystemCapability.Test.UiTest

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| wide | int | Yes | Width of the adjusted window, in pixels. The value is an integer greater than or equal to 0. If the value is out of range, error code 401 is thrown. |
| height | int | Yes | Height of the adjusted window, in pixels. The value is an integer greater than or equal to 0. If the value is out of range, error code 401 is thrown. |
| direction | [ResizeDirection](arkts-test-uitest-resizedirection-e.md) | Yes | Resize direction. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| [17000002](../errorcode-uitest.md#17000002-api-does-not-support-concurrent-calls) | The API does not support concurrent calls. |
| [17000005](../errorcode-uitest.md#17000005-operation-not-supported) | This operation is not supported. |
| [17000004](../errorcode-uitest.md#17000004-target-componentwindow-invisible-or-destroyed) | The window or component is invisible or destroyed. |

## Examples

```TypeScript
// xxx.test.ets
import { Driver, ResizeDirection, UiWindow } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  let window: UiWindow = await driver.findWindow({ actived: true });
  await window.resize(100, 100, ResizeDirection.LEFT);
}
```

## resume

```TypeScript
resume(): Promise<void>
```

Resumes a window to its previous mode. This API uses a promise to return the result.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-UiWindow-resume(): Promise<void>--><!--Device-UiWindow-resume(): Promise<void>-End-->

**System capability:** SystemCapability.Test.UiTest

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [17000002](../errorcode-uitest.md#17000002-api-does-not-support-concurrent-calls) | The API does not support concurrent calls. |
| [17000005](../errorcode-uitest.md#17000005-operation-not-supported) | This operation is not supported. |
| [17000004](../errorcode-uitest.md#17000004-target-componentwindow-invisible-or-destroyed) | The window or component is invisible or destroyed. |

## Examples

```TypeScript
// xxx.test.ets
import { Driver, UiWindow } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  let window: UiWindow = await driver.findWindow({ actived: true });
  await window.resume();
}
```

## split

```TypeScript
split(): Promise<void>
```

Switches to the split-screen mode. A window can be resumed to its previous mode using [resume](#resume). This API uses a promise to return the result. This API is applicable to windows that support screen splitting.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-UiWindow-split(): Promise<void>--><!--Device-UiWindow-split(): Promise<void>-End-->

**System capability:** SystemCapability.Test.UiTest

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [17000002](../errorcode-uitest.md#17000002-api-does-not-support-concurrent-calls) | The API does not support concurrent calls. |
| [17000005](../errorcode-uitest.md#17000005-operation-not-supported) | This operation is not supported. |
| [17000004](../errorcode-uitest.md#17000004-target-componentwindow-invisible-or-destroyed) | The window or component is invisible or destroyed. |

## Examples

```TypeScript
// xxx.test.ets
import { Driver, UiWindow } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  let window: UiWindow = await driver.findWindow({ actived: true });
  await window.split();
}
```

