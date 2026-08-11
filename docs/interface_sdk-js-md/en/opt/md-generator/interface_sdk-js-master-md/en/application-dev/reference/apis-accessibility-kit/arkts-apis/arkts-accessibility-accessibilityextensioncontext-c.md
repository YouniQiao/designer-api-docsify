# AccessibilityExtensionContext

The accessibility extension context. Used to configure, query information, and inject gestures.

**Inheritance/Implementation:** AccessibilityExtensionContext extends [ExtensionContext](../../apis-ability-kit/arkts-apis/arkts-ability-extensioncontext-c.md/arkts-ability-extensioncontext-c.md)

**Since:** 9

<!--Device-unnamed-declare class AccessibilityExtensionContext extends ExtensionContext--><!--Device-unnamed-declare class AccessibilityExtensionContext extends ExtensionContext-End-->

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
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;AccessibilityElement&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [9300003](../errorcode-accessibility.md#9300003-no-accessibility-permission-to-perform-the-operation) |

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
| Promise&lt;AccessibilityElement&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [9300003](../errorcode-accessibility.md#9300003-no-accessibility-permission-to-perform-the-operation) |

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
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;AccessibilityElement&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [9300003](../errorcode-accessibility.md#9300003-no-accessibility-permission-to-perform-the-operation) |

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
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;AccessibilityElement&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [9300003](../errorcode-accessibility.md#9300003-no-accessibility-permission-to-perform-the-operation) |

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
| Promise&lt;AccessibilityElement&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [9300003](../errorcode-accessibility.md#9300003-no-accessibility-permission-to-perform-the-operation) |

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
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;AccessibilityElement&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [9300003](../errorcode-accessibility.md#9300003-no-accessibility-permission-to-perform-the-operation) |

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
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;AccessibilityElement&gt;&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [9300003](../errorcode-accessibility.md#9300003-no-accessibility-permission-to-perform-the-operation) |

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
| Promise&lt;Array&lt;AccessibilityElement&gt;&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [9300003](../errorcode-accessibility.md#9300003-no-accessibility-permission-to-perform-the-operation) |

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
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;AccessibilityElement&gt;&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [9300003](../errorcode-accessibility.md#9300003-no-accessibility-permission-to-perform-the-operation) |

## injectGesture

```TypeScript
injectGesture(gesturePath: GesturePath, callback: AsyncCallback<void>): void
```

Injects a gesture. This API uses an asynchronous callback to return the result.

**Since:** 9

**Deprecated since:** 10

**Substitutes:** [AccessibilityExtensionContext.injectGestureSync](arkts-accessibility-accessibilityextensioncontext-c.md#injectgesturesync)

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
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [9300003](../errorcode-accessibility.md#9300003-no-accessibility-permission-to-perform-the-operation) |

## injectGesture

```TypeScript
injectGesture(gesturePath: GesturePath): Promise<void>
```

Injects a gesture. This API uses a promise to return the result.

**Since:** 9

**Deprecated since:** 10

**Substitutes:** [AccessibilityExtensionContext.injectGestureSync](arkts-accessibility-accessibilityextensioncontext-c.md#injectgesturesync)

<!--Device-AccessibilityExtensionContext-injectGesture(gesturePath: GesturePath): Promise<void>--><!--Device-AccessibilityExtensionContext-injectGesture(gesturePath: GesturePath): Promise<void>-End-->

**System capability:** SystemCapability.BarrierFree.Accessibility.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| gesturePath | [GesturePath](arkts-accessibility-accessibility-gesturepath-gesturepath-c.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;void&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [9300003](../errorcode-accessibility.md#9300003-no-accessibility-permission-to-perform-the-operation) |

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
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [9300003](../errorcode-accessibility.md#9300003-no-accessibility-permission-to-perform-the-operation) |

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
| targetNames | Array&lt;string&gt; | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |

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
| targetNames | Array&lt;string&gt; | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;void&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
