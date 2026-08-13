# AccessibilityExtensionContext

The accessibility extension context. Used to configure, query information, and inject gestures.

**Inheritance/Implementation:** AccessibilityExtensionContext extends ExtensionContext

**Since:** 23

**Deprecated since:** -1

<!--Device-unnamed-declare class AccessibilityExtensionContext--><!--Device-unnamed-declare class AccessibilityExtensionContext-End-->

**System capability:** SystemCapability.BarrierFree.Accessibility.Core

## getFocusElement

```TypeScript
getFocusElement(isAccessibilityFocus: boolean, callback: AsyncCallback<AccessibilityElement>): void
```

Obtains the focus element. This API uses an asynchronous callback to return the result.

**Since:** 9

**Deprecated since:** 12

<!--Device-AccessibilityExtensionContext-getFocusElement(isAccessibilityFocus: boolean, callback: AsyncCallback<AccessibilityElement>): void--><!--Device-AccessibilityExtensionContext-getFocusElement(isAccessibilityFocus: boolean, callback: AsyncCallback<AccessibilityElement>): void-End-->

**System capability:** SystemCapability.BarrierFree.Accessibility.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| isAccessibilityFocus | boolean | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[AccessibilityElement](arkts-accessibility-accessibilityextensioncontext-accessibilityelement-i.md)&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [9300003](../errorcode-accessibility.md#9300003-no-accessibility-permission-to-perform-the-operation) |

## Examples

```TypeScript
import { AccessibilityElement } from '@kit.AccessibilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let isAccessibilityFocus = true;
let rootElement: AccessibilityElement;

axContext.getFocusElement(isAccessibilityFocus, (err: BusinessError, data: AccessibilityElement)=> {
  if (err && err.code) {
    console.error(`failed to get focus element, Code is ${err.code}, message is ${err.message}`);
    return;
  }
  rootElement = data;
  console.info(`succeeded in getting focus element, ${JSON.stringify(data)}`);
});
```

## getFocusElement

```TypeScript
getFocusElement(isAccessibilityFocus?: boolean): Promise<AccessibilityElement>
```

Obtains the focus element. This API uses a promise to return the result.

**Since:** 9

**Deprecated since:** 12

<!--Device-AccessibilityExtensionContext-getFocusElement(isAccessibilityFocus?: boolean): Promise<AccessibilityElement>--><!--Device-AccessibilityExtensionContext-getFocusElement(isAccessibilityFocus?: boolean): Promise<AccessibilityElement>-End-->

**System capability:** SystemCapability.BarrierFree.Accessibility.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| isAccessibilityFocus | boolean | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[AccessibilityElement](arkts-accessibility-accessibilityextensioncontext-accessibilityelement-i.md)&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [9300003](../errorcode-accessibility.md#9300003-no-accessibility-permission-to-perform-the-operation) |

## Examples

```TypeScript
import { AccessibilityElement } from '@kit.AccessibilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let rootElement: AccessibilityElement;

axContext.getFocusElement().then((data: AccessibilityElement) => {
  rootElement = data;
  console.info(`succeeded in getting focus element,${JSON.stringify(data)}`);
}).catch((err: BusinessError) => {
  console.error(`failed to get focus element, Code is ${err.code}, message is ${err.message}`);
})
```

## getFocusElement

```TypeScript
getFocusElement(callback: AsyncCallback<AccessibilityElement>): void
```

Obtains the focus element. This API uses an asynchronous callback to return the result.

**Since:** 9

**Deprecated since:** 12

<!--Device-AccessibilityExtensionContext-getFocusElement(callback: AsyncCallback<AccessibilityElement>): void--><!--Device-AccessibilityExtensionContext-getFocusElement(callback: AsyncCallback<AccessibilityElement>): void-End-->

**System capability:** SystemCapability.BarrierFree.Accessibility.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[AccessibilityElement](arkts-accessibility-accessibilityextensioncontext-accessibilityelement-i.md)&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [9300003](../errorcode-accessibility.md#9300003-no-accessibility-permission-to-perform-the-operation) |

## Examples

```TypeScript
import { AccessibilityElement } from '@kit.AccessibilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let rootElement: AccessibilityElement;

axContext.getFocusElement((err: BusinessError, data: AccessibilityElement) => {
  if (err && err.code) {
    console.error(`failed to get focus element, Code is ${err.code}, message is ${err.message}`);
    return;
  }
  rootElement = data;
  console.info(`succeeded in getting focus element, ${JSON.stringify(data)}`);
});
```

## getWindowRootElement

```TypeScript
getWindowRootElement(windowId: number, callback: AsyncCallback<AccessibilityElement>): void
```

Obtains the root element of a window. This API uses an asynchronous callback to return the result.

**Since:** 9

**Deprecated since:** 12

<!--Device-AccessibilityExtensionContext-getWindowRootElement(windowId: int, callback: AsyncCallback<AccessibilityElement>): void--><!--Device-AccessibilityExtensionContext-getWindowRootElement(windowId: int, callback: AsyncCallback<AccessibilityElement>): void-End-->

**System capability:** SystemCapability.BarrierFree.Accessibility.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| windowId | number | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[AccessibilityElement](arkts-accessibility-accessibilityextensioncontext-accessibilityelement-i.md)&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [9300003](../errorcode-accessibility.md#9300003-no-accessibility-permission-to-perform-the-operation) |

## Examples

```TypeScript
import { AccessibilityElement } from '@kit.AccessibilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let windowId = 10;
let rootElement: AccessibilityElement;

axContext.getWindowRootElement(windowId, (err: BusinessError, data: AccessibilityElement) => {
  if (err && err.code) {
    console.error(`failed to get root element of the window, Code is ${err.code}, message is ${err.message}`);
    return;
  }
  rootElement = data;
  console.info(`succeeded in getting root element of the window, ${JSON.stringify(data)}`);
});
```

## getWindowRootElement

```TypeScript
getWindowRootElement(windowId?: number): Promise<AccessibilityElement>
```

Obtains the root element of a window. This API uses a promise to return the result.

**Since:** 9

**Deprecated since:** 12

<!--Device-AccessibilityExtensionContext-getWindowRootElement(windowId?: int): Promise<AccessibilityElement>--><!--Device-AccessibilityExtensionContext-getWindowRootElement(windowId?: int): Promise<AccessibilityElement>-End-->

**System capability:** SystemCapability.BarrierFree.Accessibility.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| windowId | number | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[AccessibilityElement](arkts-accessibility-accessibilityextensioncontext-accessibilityelement-i.md)&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [9300003](../errorcode-accessibility.md#9300003-no-accessibility-permission-to-perform-the-operation) |

## Examples

```TypeScript
import { AccessibilityElement } from '@kit.AccessibilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let rootElement: AccessibilityElement;

axContext.getWindowRootElement().then((data: AccessibilityElement) => {
  rootElement = data;
  console.info(`succeeded in getting root element of the window, ${JSON.stringify(data)}`);
}).catch((err: BusinessError) => {
  console.error(`failed to get root element of the window, Code is ${err.code}, message is ${err.message}`);
});
```

## getWindowRootElement

```TypeScript
getWindowRootElement(callback: AsyncCallback<AccessibilityElement>): void
```

Obtains the root element of a window. This API uses an asynchronous callback to return the result.

**Since:** 9

**Deprecated since:** 12

<!--Device-AccessibilityExtensionContext-getWindowRootElement(callback: AsyncCallback<AccessibilityElement>): void--><!--Device-AccessibilityExtensionContext-getWindowRootElement(callback: AsyncCallback<AccessibilityElement>): void-End-->

**System capability:** SystemCapability.BarrierFree.Accessibility.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[AccessibilityElement](arkts-accessibility-accessibilityextensioncontext-accessibilityelement-i.md)&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [9300003](../errorcode-accessibility.md#9300003-no-accessibility-permission-to-perform-the-operation) |

## Examples

```TypeScript
import { AccessibilityElement } from '@kit.AccessibilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let rootElement: AccessibilityElement;

axContext.getWindowRootElement((err: BusinessError, data: AccessibilityElement) => {
  if (err && err.code) {
    console.error(`failed to get root element of the window, Code is ${err.code}, message is ${err.message}`);
    return;
  }
  rootElement = data;
  console.info(`succeeded in getting root element of the window, ${JSON.stringify(data)}`);
});
```

## getWindows

```TypeScript
getWindows(displayId: number, callback: AsyncCallback<Array<AccessibilityElement>>): void
```

Obtains the list of windows on a display. This API uses an asynchronous callback to return the result.

**Since:** 9

**Deprecated since:** 12

<!--Device-AccessibilityExtensionContext-getWindows(displayId: long, callback: AsyncCallback<Array<AccessibilityElement>>): void--><!--Device-AccessibilityExtensionContext-getWindows(displayId: long, callback: AsyncCallback<Array<AccessibilityElement>>): void-End-->

**System capability:** SystemCapability.BarrierFree.Accessibility.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| displayId | number | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;[AccessibilityElement](arkts-accessibility-accessibilityextensioncontext-accessibilityelement-i.md)&gt;&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [9300003](../errorcode-accessibility.md#9300003-no-accessibility-permission-to-perform-the-operation) |

## Examples

```TypeScript
import { AccessibilityElement } from '@kit.AccessibilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let displayId = 10;
axContext.getWindows(displayId, (err: BusinessError, data: AccessibilityElement[]) => {
  if (err && err.code) {
    console.error(`failed to get windows, Code is ${err.code}, message is ${err.message}`);
    return;
  }
  console.info(`succeeded in getting windows, ${JSON.stringify(data)}`);
});
```

## getWindows

```TypeScript
getWindows(displayId?: number): Promise<Array<AccessibilityElement>>
```

Obtains the list of windows on a display. This API uses a promise to return the result.

**Since:** 9

**Deprecated since:** 12

<!--Device-AccessibilityExtensionContext-getWindows(displayId?: long): Promise<Array<AccessibilityElement>>--><!--Device-AccessibilityExtensionContext-getWindows(displayId?: long): Promise<Array<AccessibilityElement>>-End-->

**System capability:** SystemCapability.BarrierFree.Accessibility.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| displayId | number | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;Array&lt;[AccessibilityElement](arkts-accessibility-accessibilityextensioncontext-accessibilityelement-i.md)&gt;&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [9300003](../errorcode-accessibility.md#9300003-no-accessibility-permission-to-perform-the-operation) |

## Examples

```TypeScript
import { AccessibilityElement } from '@kit.AccessibilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

axContext.getWindows().then((data: AccessibilityElement[]) => {
  console.info(`succeeded in getting windows, ${JSON.stringify(data)}`);
}).catch((err: BusinessError) => {
  console.error(`failed to get windows, Code is ${err.code}, message is ${err.message}`);
});
```

## getWindows

```TypeScript
getWindows(callback: AsyncCallback<Array<AccessibilityElement>>): void
```

Obtains the list of windows on a display. This API uses an asynchronous callback to return the result.

**Since:** 9

**Deprecated since:** 12

<!--Device-AccessibilityExtensionContext-getWindows(callback: AsyncCallback<Array<AccessibilityElement>>): void--><!--Device-AccessibilityExtensionContext-getWindows(callback: AsyncCallback<Array<AccessibilityElement>>): void-End-->

**System capability:** SystemCapability.BarrierFree.Accessibility.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;[AccessibilityElement](arkts-accessibility-accessibilityextensioncontext-accessibilityelement-i.md)&gt;&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [9300003](../errorcode-accessibility.md#9300003-no-accessibility-permission-to-perform-the-operation) |

## Examples

```TypeScript
import { AccessibilityElement } from '@kit.AccessibilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

axContext.getWindows((err: BusinessError, data: AccessibilityElement[]) => {
  if (err && err.code) {
    console.error(`failed to get windows, Code is ${err.code}, message is ${err.message}`);
    return;
  }
  console.info(`succeeded in getting windows, ${JSON.stringify(data)}`);
});
```

## injectGesture

```TypeScript
injectGesture(gesturePath: GesturePath, callback: AsyncCallback<void>): void
```

Injects a gesture. This API uses an asynchronous callback to return the result.

**Since:** 9

**Deprecated since:** 10

**Substitutes:** [injectGestureSync](#injectGestureSync)

<!--Device-AccessibilityExtensionContext-injectGesture(gesturePath: GesturePath, callback: AsyncCallback<void>): void--><!--Device-AccessibilityExtensionContext-injectGesture(gesturePath: GesturePath, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.BarrierFree.Accessibility.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| gesturePath | [GesturePath](arkts-accessibility-accessibility-gesturepath-gesturepath-c.md) | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [9300003](../errorcode-accessibility.md#9300003-no-accessibility-permission-to-perform-the-operation) |

## Examples

```TypeScript
import { GesturePath, GesturePoint } from '@kit.AccessibilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let gesturePath: GesturePath = new GesturePath(100);
for (let i = 0; i < 10; i++) {
  let gesturePoint = new GesturePoint(100, i * 200);
  gesturePath.points.push(gesturePoint);
}
axContext.injectGesture(gesturePath, (err: BusinessError) => {
  if (err) {
    console.error(`failed to inject gesture, Code is ${err.code}, message is ${err.message}`);
    return;
  }
  console.info(`Succeeded in injecting gesture,gesturePath is ${gesturePath}`);
});
```

## injectGesture

```TypeScript
injectGesture(gesturePath: GesturePath): Promise<void>
```

Injects a gesture. This API uses a promise to return the result.

**Since:** 9

**Deprecated since:** 10

**Substitutes:** [injectGestureSync](#injectGestureSync)

<!--Device-AccessibilityExtensionContext-injectGesture(gesturePath: GesturePath): Promise<void>--><!--Device-AccessibilityExtensionContext-injectGesture(gesturePath: GesturePath): Promise<void>-End-->

**System capability:** SystemCapability.BarrierFree.Accessibility.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| gesturePath | [GesturePath](arkts-accessibility-accessibility-gesturepath-gesturepath-c.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [9300003](../errorcode-accessibility.md#9300003-no-accessibility-permission-to-perform-the-operation) |

## Examples

```TypeScript
import { GesturePath, GesturePoint } from '@kit.AccessibilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let gesturePath: GesturePath = new GesturePath(100);

for (let i = 0; i < 10; i++) {
  let gesturePoint = new GesturePoint(100, i * 200);
  gesturePath.points.push(gesturePoint);
}
axContext.injectGesture(gesturePath).then(() => {
  console.info(`Succeeded in injecting gesture,gesturePath is ${gesturePath}`);
}).catch((err: BusinessError) => {
  console.error(`failed to inject gesture, Code is ${err.code}, message is ${err.message}`);
});
```

## injectGestureSync

```TypeScript
injectGestureSync(gesturePath: GesturePath): void
```

Injects a gesture.

**Since:** 10

**Deprecated since:** 12

<!--Device-AccessibilityExtensionContext-injectGestureSync(gesturePath: GesturePath): void--><!--Device-AccessibilityExtensionContext-injectGestureSync(gesturePath: GesturePath): void-End-->

**System capability:** SystemCapability.BarrierFree.Accessibility.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| gesturePath | [GesturePath](arkts-accessibility-accessibility-gesturepath-gesturepath-c.md) | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [9300003](../errorcode-accessibility.md#9300003-no-accessibility-permission-to-perform-the-operation) |

## Examples

```TypeScript
import { GesturePath, GesturePoint } from '@kit.AccessibilityKit';

let gesturePath: GesturePath = new GesturePath(100);
for (let i = 0; i < 10; i++) {
  let gesturePoint = new GesturePoint(100, i * 200);
  gesturePath.points.push(gesturePoint);
}
axContext.injectGestureSync(gesturePath);
```

## setTargetBundleName

```TypeScript
setTargetBundleName(targetNames: Array<string>, callback: AsyncCallback<void>): void
```

Sets the concerned target bundle. This API uses an asynchronous callback to return the result.

**Since:** 9

**Deprecated since:** 12

<!--Device-AccessibilityExtensionContext-setTargetBundleName(targetNames: Array<string>, callback: AsyncCallback<void>): void--><!--Device-AccessibilityExtensionContext-setTargetBundleName(targetNames: Array<string>, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.BarrierFree.Accessibility.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| targetNames | Array & lt;string & gt; | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let targetNames = ['com.ohos.xyz'];
try {
  axContext.setTargetBundleName(targetNames, (err: BusinessError) => {
    if (err && err.code) {
      console.error(`failed to set target bundle names, Code is ${err.code}, message is ${err.message}`);
      return;
    }
    console.info(`succeeded in setting target bundle names, targetNames is ${targetNames}`);
  });
} catch (error) {
  console.error(`failed to set target bundle names, Because ${JSON.stringify(error)}`);
}
```

## setTargetBundleName

```TypeScript
setTargetBundleName(targetNames: Array<string>): Promise<void>
```

Sets the concerned target bundle. This API uses a promise to return the result.

**Since:** 9

**Deprecated since:** 12

<!--Device-AccessibilityExtensionContext-setTargetBundleName(targetNames: Array<string>): Promise<void>--><!--Device-AccessibilityExtensionContext-setTargetBundleName(targetNames: Array<string>): Promise<void>-End-->

**System capability:** SystemCapability.BarrierFree.Accessibility.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| targetNames | Array & lt;string & gt; | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let targetNames = ['com.ohos.xyz'];
axContext.setTargetBundleName(targetNames).then(() => {
  console.info(`succeeded in setting target bundle names, targetNames is ${targetNames}`);
}).catch((err: BusinessError) => {
  console.error(`failed to set target bundle names, Code is ${err.code}, message is ${err.message}`);
})
```
