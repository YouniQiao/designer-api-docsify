# UiWindow

The **UiWindow** class represents a window on the UI and provides APIs for obtaining window attributes, dragging a window, and adjusting the window size.All APIs provided in this class use a promise to return the result and must be invoked using **await**.

**Since:** 9

<!--Device-unnamed-declare class UiWindow--><!--Device-unnamed-declare class UiWindow-End-->

**System capability:** SystemCapability.Test.UiTest

## Modules to Import

```TypeScript
import { ResizeDirection, WindowMode, PenMode, PenKeyOperation, Driver, MatchPattern, UiDirection, TouchOptions, ComponentEventType, PointerMatrix, WindowChangeType, Component, ON, PenKey, Rect, InputTextMode, UIEventObserver, WindowFilter, WindowChangeOptions, UiWindow, TouchPadSwipeOptions, Point, KeyOptions, DisplayRotation, UIElementInfo, PenKeyOperationOptions, ComponentEventOptions, MouseButton, On } from '@kit.TestKit';
```

## close

```TypeScript
close(): Promise<void>
```

Closes a window. This API uses a promise to return the result.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-UiWindow-close(): Promise<void>--><!--Device-UiWindow-close(): Promise<void>-End-->

**System capability:** SystemCapability.Test.UiTest

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [17000002](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-test-kit/errorcode-uitest.md#17000002-api-does-not-support-concurrent-calls) |
| [17000005](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-test-kit/errorcode-uitest.md#17000005-operation-not-supported) |
| [17000004](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-test-kit/errorcode-uitest.md#17000004-target-componentwindow-invisible-or-destroyed) |

## Examples

```TypeScript
// xxx.test.ets
import { Driver, UiWindow } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  let window: UiWindow = await driver.findWindow({ active: true });
  await window.close();
}
```

## focus

```TypeScript
focus(): Promise<void>
```

Focuses a window. This API uses a promise to return the result.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-UiWindow-focus(): Promise<void>--><!--Device-UiWindow-focus(): Promise<void>-End-->

**System capability:** SystemCapability.Test.UiTest

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [17000002](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-test-kit/errorcode-uitest.md#17000002-api-does-not-support-concurrent-calls) |
| [17000004](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-test-kit/errorcode-uitest.md#17000004-target-componentwindow-invisible-or-destroyed) |

## Examples

```TypeScript
// xxx.test.ets
import { Driver, UiWindow } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  let window: UiWindow = await driver.findWindow({ active: true });
  await window.focus();
}
```

## getBounds

```TypeScript
getBounds(): Promise<Rect>
```

Obtains the bounds information of a window. This API uses a promise to return the result.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-UiWindow-getBounds(): Promise<Rect>--><!--Device-UiWindow-getBounds(): Promise<Rect>-End-->

**System capability:** SystemCapability.Test.UiTest

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[Rect](arkts-test-uitest-rect-i.md)&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [17000002](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-test-kit/errorcode-uitest.md#17000002-api-does-not-support-concurrent-calls) |
| [17000004](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-test-kit/errorcode-uitest.md#17000004-target-componentwindow-invisible-or-destroyed) |

## Examples

```TypeScript
// xxx.test.ets
import { Driver, UiWindow } from '@kit.TestKit';

async function demo() {
  // Create a Driver object.
  let driver: Driver = Driver.create();
  // Search for the active window.
  let window: UiWindow = await driver.findWindow({ active: true });
  // Obtain the bounds information of the window.
  let rect = await window.getBounds();
}
```

## getBundleName

```TypeScript
getBundleName(): Promise<string>
```

Obtains the bundle name of the application to which a window belongs. This API uses a promise to return the result.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-UiWindow-getBundleName(): Promise<string>--><!--Device-UiWindow-getBundleName(): Promise<string>-End-->

**System capability:** SystemCapability.Test.UiTest

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;string & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [17000002](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-test-kit/errorcode-uitest.md#17000002-api-does-not-support-concurrent-calls) |
| [17000004](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-test-kit/errorcode-uitest.md#17000004-target-componentwindow-invisible-or-destroyed) |

## Examples

```TypeScript
// xxx.test.ets
import { Driver, UiWindow } from '@kit.TestKit';

async function demo() {
  // Create a Driver object.
  let driver: Driver = Driver.create();
  // Search for the active window.
  let window: UiWindow = await driver.findWindow({ active: true });
  // Obtain the bundle name of the application to which the window belongs.
  let name: string = await window.getBundleName();
}
```

## getDisplayId

```TypeScript
getDisplayId(): Promise<number>
```

Obtains the ID of the display to which a window belongs. This API uses a promise to return the result.

**Since:** 20

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-UiWindow-getDisplayId(): Promise<int>--><!--Device-UiWindow-getDisplayId(): Promise<int>-End-->

**System capability:** SystemCapability.Test.UiTest

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;number & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [17000002](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-test-kit/errorcode-uitest.md#17000002-api-does-not-support-concurrent-calls) |
| [17000004](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-test-kit/errorcode-uitest.md#17000004-target-componentwindow-invisible-or-destroyed) |

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

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-UiWindow-getTitle(): Promise<string>--><!--Device-UiWindow-getTitle(): Promise<string>-End-->

**System capability:** SystemCapability.Test.UiTest

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;string & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [17000002](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-test-kit/errorcode-uitest.md#17000002-api-does-not-support-concurrent-calls) |
| [17000004](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-test-kit/errorcode-uitest.md#17000004-target-componentwindow-invisible-or-destroyed) |

## Examples

```TypeScript
// xxx.test.ets
import { Driver, UiWindow } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  let window: UiWindow = await driver.findWindow({ active: true });
  let title = await window.getTitle();
}
```

## getWindowMode

```TypeScript
getWindowMode(): Promise<WindowMode>
```

Obtains the window mode. This API uses a promise to return the result.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-UiWindow-getWindowMode(): Promise<WindowMode>--><!--Device-UiWindow-getWindowMode(): Promise<WindowMode>-End-->

**System capability:** SystemCapability.Test.UiTest

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[WindowMode](arkts-test-uitest-windowmode-e.md)&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [17000002](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-test-kit/errorcode-uitest.md#17000002-api-does-not-support-concurrent-calls) |
| [17000004](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-test-kit/errorcode-uitest.md#17000004-target-componentwindow-invisible-or-destroyed) |

## Examples

```TypeScript
// xxx.test.ets
import { Driver, UiWindow } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  let window: UiWindow = await driver.findWindow({ active: true });
  let mode = await window.getWindowMode();
}
```

## isActive

```TypeScript
isActive(): Promise<boolean>
```

Checks whether a window is active. This API uses a promise to return the result.

**Since:** 11

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-UiWindow-isActive(): Promise<boolean>--><!--Device-UiWindow-isActive(): Promise<boolean>-End-->

**System capability:** SystemCapability.Test.UiTest

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;boolean & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [17000002](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-test-kit/errorcode-uitest.md#17000002-api-does-not-support-concurrent-calls) |
| [17000004](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-test-kit/errorcode-uitest.md#17000004-target-componentwindow-invisible-or-destroyed) |

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

**Deprecated since:** 11

**Substitutes:** [isActive](#isActive)

<!--Device-UiWindow-isActived(): Promise<boolean>--><!--Device-UiWindow-isActived(): Promise<boolean>-End-->

**System capability:** SystemCapability.Test.UiTest

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;boolean & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [17000002](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-test-kit/errorcode-uitest.md#17000002-api-does-not-support-concurrent-calls) |
| [17000004](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-test-kit/errorcode-uitest.md#17000004-target-componentwindow-invisible-or-destroyed) |

## Examples

```TypeScript
// xxx.test.ets
import { Driver, UiWindow } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  let window: UiWindow = await driver.findWindow({ active: true });
  let focused = await window.isActived();
}
```

## isFocused

```TypeScript
isFocused(): Promise<boolean>
```

Checks whether a window is focused. This API uses a promise to return the result.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-UiWindow-isFocused(): Promise<boolean>--><!--Device-UiWindow-isFocused(): Promise<boolean>-End-->

**System capability:** SystemCapability.Test.UiTest

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;boolean & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [17000002](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-test-kit/errorcode-uitest.md#17000002-api-does-not-support-concurrent-calls) |
| [17000004](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-test-kit/errorcode-uitest.md#17000004-target-componentwindow-invisible-or-destroyed) |

## Examples

```TypeScript
// xxx.test.ets
import { Driver, UiWindow } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  let window: UiWindow = await driver.findWindow({ active: true });
  let focused = await window.isFocused();
}
```

## maximize

```TypeScript
maximize(): Promise<void>
```

Maximizes a window. A window can be resumed to its previous mode using [resume](#resume). This API uses a promise to return the result. This API is applicable to windows that can be maximized.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-UiWindow-maximize(): Promise<void>--><!--Device-UiWindow-maximize(): Promise<void>-End-->

**System capability:** SystemCapability.Test.UiTest

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [17000002](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-test-kit/errorcode-uitest.md#17000002-api-does-not-support-concurrent-calls) |
| [17000005](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-test-kit/errorcode-uitest.md#17000005-operation-not-supported) |
| [17000004](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-test-kit/errorcode-uitest.md#17000004-target-componentwindow-invisible-or-destroyed) |

## Examples

```TypeScript
// xxx.test.ets
import { Driver, UiWindow } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  let window: UiWindow = await driver.findWindow({ active: true });
  await window.maximize();
}
```

## minimize

```TypeScript
minimize(): Promise<void>
```

Minimizes a window. A window can be resumed to its previous mode using [resume](#resume). This API uses a promise to return the result. This API is applicable to windows that can be minimized.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-UiWindow-minimize(): Promise<void>--><!--Device-UiWindow-minimize(): Promise<void>-End-->

**System capability:** SystemCapability.Test.UiTest

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [17000002](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-test-kit/errorcode-uitest.md#17000002-api-does-not-support-concurrent-calls) |
| [17000005](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-test-kit/errorcode-uitest.md#17000005-operation-not-supported) |
| [17000004](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-test-kit/errorcode-uitest.md#17000004-target-componentwindow-invisible-or-destroyed) |

## Examples

```TypeScript
// xxx.test.ets
import { Driver, UiWindow } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  let window: UiWindow = await driver.findWindow({ active: true });
  await window.minimize();
}
```

## moveTo

```TypeScript
moveTo(x: number, y: number): Promise<void>
```

Moves a window to the target point. This API uses a promise to return the result. This API is applicable to moveable windows.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-UiWindow-moveTo(x: int, y: int): Promise<void>--><!--Device-UiWindow-moveTo(x: int, y: int): Promise<void>-End-->

**System capability:** SystemCapability.Test.UiTest

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| x | number | Yes |
| y | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [17000002](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-test-kit/errorcode-uitest.md#17000002-api-does-not-support-concurrent-calls) |
| [17000005](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-test-kit/errorcode-uitest.md#17000005-operation-not-supported) |
| [17000004](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-test-kit/errorcode-uitest.md#17000004-target-componentwindow-invisible-or-destroyed) |

## Examples

```TypeScript
// xxx.test.ets
import { Driver, UiWindow } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  let window: UiWindow = await driver.findWindow({ active: true });
  await window.moveTo(100, 100);
}
```

## resize

```TypeScript
resize(wide: number, height: number, direction: ResizeDirection): Promise<void>
```

Resizes a window based on the specified width, height, and direction. This API uses a promise to return the result. This API is applicable to resizable windows.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-UiWindow-resize(wide: int, height: int, direction: ResizeDirection): Promise<void>--><!--Device-UiWindow-resize(wide: int, height: int, direction: ResizeDirection): Promise<void>-End-->

**System capability:** SystemCapability.Test.UiTest

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| wide | number | Yes |
| height | number | Yes |
| direction | [ResizeDirection](arkts-test-uitest-resizedirection-e.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [17000002](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-test-kit/errorcode-uitest.md#17000002-api-does-not-support-concurrent-calls) |
| [17000005](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-test-kit/errorcode-uitest.md#17000005-operation-not-supported) |
| [17000004](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-test-kit/errorcode-uitest.md#17000004-target-componentwindow-invisible-or-destroyed) |

## resume

```TypeScript
resume(): Promise<void>
```

Resumes a window to its previous mode. This API uses a promise to return the result.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-UiWindow-resume(): Promise<void>--><!--Device-UiWindow-resume(): Promise<void>-End-->

**System capability:** SystemCapability.Test.UiTest

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [17000002](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-test-kit/errorcode-uitest.md#17000002-api-does-not-support-concurrent-calls) |
| [17000005](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-test-kit/errorcode-uitest.md#17000005-operation-not-supported) |
| [17000004](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-test-kit/errorcode-uitest.md#17000004-target-componentwindow-invisible-or-destroyed) |

## Examples

```TypeScript
// xxx.test.ets
import { Driver, UiWindow } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  let window: UiWindow = await driver.findWindow({ active: true });
  await window.resume();
}
```

## split

```TypeScript
split(): Promise<void>
```

Switches to the split-screen mode. A window can be resumed to its previous mode using [resume](#resume). This API uses a promise to return the result. This API is applicable to windows that support screen splitting.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-UiWindow-split(): Promise<void>--><!--Device-UiWindow-split(): Promise<void>-End-->

**System capability:** SystemCapability.Test.UiTest

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [17000002](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-test-kit/errorcode-uitest.md#17000002-api-does-not-support-concurrent-calls) |
| [17000005](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-test-kit/errorcode-uitest.md#17000005-operation-not-supported) |
| [17000004](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-test-kit/errorcode-uitest.md#17000004-target-componentwindow-invisible-or-destroyed) |

## Examples

```TypeScript
// xxx.test.ets
import { Driver, UiWindow } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  let window: UiWindow = await driver.findWindow({ active: true });
  await window.split();
}
```
