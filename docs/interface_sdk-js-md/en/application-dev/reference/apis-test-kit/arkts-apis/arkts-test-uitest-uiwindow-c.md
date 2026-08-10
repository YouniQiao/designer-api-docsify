# UiWindow

UiWindow代表了UI界面上的一个窗口，提供窗口属性获取，窗口拖动、调整窗口大小等能力。该类对象可通过{@link Driver#findWindow}接口获取。该类提供的所有方法都使用Promise方式作为异步方法，需使用await方式调用。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-unnamed-declare class UiWindow--><!--Device-unnamed-declare class UiWindow-End-->

**System capability:** SystemCapability.Test.UiTest

## Modules to Import

```TypeScript
import { ResizeDirection, WindowMode, PenMode, PenKeyOperation, Driver, MatchPattern, UiDirection, TouchOptions, ComponentEventType, PointerMatrix, WindowChangeType, Component, ON, PenKey, Rect, InputTextMode, UIEventObserver, WindowFilter, WindowChangeOptions, UiWindow, TouchPadSwipeOptions, Point, KeyOptions, DisplayRotation, UIElementInfo, PenKeyOperationOptions, ComponentEventOptions, MouseButton, On } from 'kits/@kit.TestKit';
```

## close

```TypeScript
close(): Promise<void>
```

将窗口关闭。使用Promise异步回调。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-UiWindow-close(): Promise<void>--><!--Device-UiWindow-close(): Promise<void>-End-->

**System capability:** SystemCapability.Test.UiTest

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise对象。无返回结果的Promise对象。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 17000002 | The API does not support concurrent calls. |
| 17000005 | This operation is not supported. |
| 17000004 | The window or component is invisible or destroyed. |

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

让窗口获焦。使用Promise异步回调。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-UiWindow-focus(): Promise<void>--><!--Device-UiWindow-focus(): Promise<void>-End-->

**System capability:** SystemCapability.Test.UiTest

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise对象，返回无结果的Promise对象。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 17000002 | The API does not support concurrent calls. |
| 17000004 | The window or component is invisible or destroyed. |

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

获取窗口的边框信息。使用Promise异步回调。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-UiWindow-getBounds(): Promise<Rect>--><!--Device-UiWindow-getBounds(): Promise<Rect>-End-->

**System capability:** SystemCapability.Test.UiTest

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;Rect&gt; | Promise对象，返回窗口的边框信息。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 17000002 | The API does not support concurrent calls. |
| 17000004 | The window or component is invisible or destroyed. |

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

获取窗口归属应用的包名信息。使用Promise异步回调。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-UiWindow-getBundleName(): Promise<string>--><!--Device-UiWindow-getBundleName(): Promise<string>-End-->

**System capability:** SystemCapability.Test.UiTest

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;string&gt; | Promise对象，返回窗口归属应用的包名信息。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 17000002 | The API does not support concurrent calls. |
| 17000004 | The window or component is invisible or destroyed. |

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

ArkTS-Dyn:
```TypeScript
getDisplayId(): Promise<number>
```

ArkTS-Sta:
```TypeScript
getDisplayId(): Promise<int>
```

获取窗口所属的屏幕ID。使用Promise异步回调。

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-UiWindow-getDisplayId(): Promise<int>--><!--Device-UiWindow-getDisplayId(): Promise<int>-End-->

**System capability:** SystemCapability.Test.UiTest

**Return value:**

| Type | Description |
| --- | --- |
| ArkTS-Dyn: Promise&lt;number&gt;  <br>ArkTS-Sta：Promise&lt;int&gt; | Promise对象，返回窗口所属的屏幕ID。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 17000002 | The API does not support concurrent calls. |
| 17000004 | The window or component is invisible or destroyed. |

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

获取窗口的标题信息。使用Promise异步回调。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-UiWindow-getTitle(): Promise<string>--><!--Device-UiWindow-getTitle(): Promise<string>-End-->

**System capability:** SystemCapability.Test.UiTest

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;string&gt; | Promise对象，返回窗口的标题信息。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 17000002 | The API does not support concurrent calls. |
| 17000004 | The window or component is invisible or destroyed. |

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

获取窗口的窗口模式信息。使用Promise异步回调。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-UiWindow-getWindowMode(): Promise<WindowMode>--><!--Device-UiWindow-getWindowMode(): Promise<WindowMode>-End-->

**System capability:** SystemCapability.Test.UiTest

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;WindowMode&gt; | Promise对象，返回窗口的窗口模式信息。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 17000002 | The API does not support concurrent calls. |
| 17000004 | The window or component is invisible or destroyed. |

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

判断窗口是否为用户正在交互窗口。使用Promise异步回调。

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-UiWindow-isActive(): Promise<boolean>--><!--Device-UiWindow-isActive(): Promise<boolean>-End-->

**System capability:** SystemCapability.Test.UiTest

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;boolean&gt; | Promise对象，返回窗口对象是否为用户正在交互窗口。true：交互窗口。false：非交互窗口。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 17000002 | The API does not support concurrent calls. |
| 17000004 | The window or component is invisible or destroyed. |

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

判断窗口是否为用户正在交互窗口。使用Promise异步回调。

> **说明：**
> 
> 从API version 9开始支持，从API version 11开始废弃，建议使用[isActive&lt;sup&gt;11+&lt;/sup&gt;](arkts-test-uitest-uiwindow-c.md#isactive)替代。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

**Deprecated since:** 11

**Substitutes:** [UiWindow#isActive](arkts-test-uitest-uiwindow-c.md#isactive)

<!--Device-UiWindow-isActived(): Promise<boolean>--><!--Device-UiWindow-isActived(): Promise<boolean>-End-->

**System capability:** SystemCapability.Test.UiTest

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;boolean&gt; | Promise对象，返回窗口对象是否为用户正在交互窗口。true表示是交互窗口。false表示非交互窗口。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 17000002 | The API does not support concurrent calls. |
| 17000004 | The window or component is invisible or destroyed. |

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

判断窗口是否处于获焦状态。使用Promise异步回调。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-UiWindow-isFocused(): Promise<boolean>--><!--Device-UiWindow-isFocused(): Promise<boolean>-End-->

**System capability:** SystemCapability.Test.UiTest

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;boolean&gt; | Promise对象，返回窗口对象是否获取获焦状态。true：获焦。false：未获焦。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 17000002 | The API does not support concurrent calls. |
| 17000004 | The window or component is invisible or destroyed. |

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

将窗口最大化。使用Promise异步回调。适用于支持窗口最大化操作的窗口。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-UiWindow-maximize(): Promise<void>--><!--Device-UiWindow-maximize(): Promise<void>-End-->

**System capability:** SystemCapability.Test.UiTest

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise对象，返回无结果的Promise对象。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 17000002 | The API does not support concurrent calls. |
| 17000005 | This operation is not supported. |
| 17000004 | The window or component is invisible or destroyed. |

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

将窗口最小化。使用Promise异步回调。适用于支持窗口最小化操作的窗口。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-UiWindow-minimize(): Promise<void>--><!--Device-UiWindow-minimize(): Promise<void>-End-->

**System capability:** SystemCapability.Test.UiTest

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise对象，返回无结果的Promise对象。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 17000002 | The API does not support concurrent calls. |
| 17000005 | This operation is not supported. |
| 17000004 | The window or component is invisible or destroyed. |

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

ArkTS-Dyn:
```TypeScript
moveTo(x: number, y: number): Promise<void>
```

ArkTS-Sta:
```TypeScript
moveTo(x: int, y: int): Promise<void>
```

将窗口移动到目标点。使用Promise异步回调。适用于支持移动的窗口。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-UiWindow-moveTo(x: int, y: int): Promise<void>--><!--Device-UiWindow-moveTo(x: int, y: int): Promise<void>-End-->

**System capability:** SystemCapability.Test.UiTest

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| x | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | 以number的形式传入目标点的横坐标信息，取值范围：大于等于0的整数。 |
| y | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | 以number的形式传入目标点的纵坐标信息，取值范围：大于等于0的整数。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise对象，返回无结果的Promise对象。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 17000002 | The API does not support concurrent calls. |
| 17000005 | This operation is not supported. |
| 17000004 | The window or component is invisible or destroyed. |

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

ArkTS-Dyn:
```TypeScript
resize(wide: number, height: number, direction: ResizeDirection): Promise<void>
```

ArkTS-Sta:
```TypeScript
resize(wide: int, height: int, direction: ResizeDirection): Promise<void>
```

根据传入的宽、高和调整方向来调整窗口的大小。使用Promise异步回调。适用于支持调整大小的窗口。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-UiWindow-resize(wide: int, height: int, direction: ResizeDirection): Promise<void>--><!--Device-UiWindow-resize(wide: int, height: int, direction: ResizeDirection): Promise<void>-End-->

**System capability:** SystemCapability.Test.UiTest

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| wide | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | 以number的形式传入调整后窗口的宽度，取值范围：大于等于0的整数。 |
| height | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | 以number的形式传入调整后窗口的高度，取值范围：大于等于0的整数。 |
| direction | [ResizeDirection](arkts-test-uitest-resizedirection-e.md) | Yes | 以[ResizeDirection](arkts-test-uitest-resizedirection-e.md)的形式传入窗口调整的方向。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise对象，返回无结果的Promise对象。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 17000002 | The API does not support concurrent calls. |
| 17000005 | This operation is not supported. |
| 17000004 | The window or component is invisible or destroyed. |

## resume

```TypeScript
resume(): Promise<void>
```

将窗口恢复到之前的窗口模式。使用Promise异步回调。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-UiWindow-resume(): Promise<void>--><!--Device-UiWindow-resume(): Promise<void>-End-->

**System capability:** SystemCapability.Test.UiTest

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise对象。无返回结果的Promise对象。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 17000002 | The API does not support concurrent calls. |
| 17000005 | This operation is not supported. |
| 17000004 | The window or component is invisible or destroyed. |

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

将窗口模式切换成分屏模式。使用Promise异步回调。适用于支持切换分屏模式的窗口。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-UiWindow-split(): Promise<void>--><!--Device-UiWindow-split(): Promise<void>-End-->

**System capability:** SystemCapability.Test.UiTest

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise对象，返回无结果的Promise对象。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 17000002 | The API does not support concurrent calls. |
| 17000005 | This operation is not supported. |
| 17000004 | The window or component is invisible or destroyed. |

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

