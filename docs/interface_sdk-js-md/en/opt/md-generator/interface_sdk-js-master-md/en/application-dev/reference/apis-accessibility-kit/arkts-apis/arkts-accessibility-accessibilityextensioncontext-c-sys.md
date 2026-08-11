# AccessibilityExtensionContext

The accessibility extension context. Used to configure, query information, and inject gestures.

**Inheritance/Implementation:** AccessibilityExtensionContext extends [ExtensionContext](../../apis-ability-kit/arkts-apis/arkts-ability-extensioncontext-c.md/arkts-ability-extensioncontext-c.md)

**Since:** 9

<!--Device-unnamed-declare class AccessibilityExtensionContext extends ExtensionContext--><!--Device-unnamed-declare class AccessibilityExtensionContext extends ExtensionContext-End-->

**System capability:** SystemCapability.BarrierFree.Accessibility.Core

## addAccessibilityVirtualNodes

```TypeScript
addAccessibilityVirtualNodes(elementId: number, windowId: number, nodes: Array<AccessibilityVirtualNode>): Promise<OperateVirtualNodeResult>
```

Add accessibility virtual nodes.

**Since:** 26.0.0

**Required permissions:** ohos.permission.ACCESSIBILITY_EXTENSION_ABILITY

**Model restriction:** This API can be used only in the stage model.

<!--Device-AccessibilityExtensionContext-addAccessibilityVirtualNodes(elementId: long, windowId: int, nodes: Array<AccessibilityVirtualNode>): Promise<OperateVirtualNodeResult>--><!--Device-AccessibilityExtensionContext-addAccessibilityVirtualNodes(elementId: long, windowId: int, nodes: Array<AccessibilityVirtualNode>): Promise<OperateVirtualNodeResult>-End-->

**System capability:** SystemCapability.BarrierFree.Accessibility.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| elementId | number | Yes |
| windowId | number | Yes |
| nodes | Array&lt;AccessibilityVirtualNode&gt; | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[OperateVirtualNodeResult](arkts-accessibility-accessibility-operatevirtualnoderesult-e-sys.md)&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [9300000](../errorcode-accessibility.md#9300000-accessibility-system-service-abnormal) |

## getAccessibilityFocusedElement

```TypeScript
getAccessibilityFocusedElement(): Promise<AccessibilityElement>
```

Obtains the element that is currently focused. This API uses a promise to return the result.

**Since:** 20

**Required permissions:** ohos.permission.ACCESSIBILITY_EXTENSION_ABILITY

<!--Device-AccessibilityExtensionContext-getAccessibilityFocusedElement(): Promise<AccessibilityElement>--><!--Device-AccessibilityExtensionContext-getAccessibilityFocusedElement(): Promise<AccessibilityElement>-End-->

**System capability:** SystemCapability.BarrierFree.Accessibility.Core

**System API:** This is a system API.

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;AccessibilityElement&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [9300006](../errorcode-accessibility.md#9300006-failed-to-connect-the-target-app-and-accessibility-service) |
| [9300003](../errorcode-accessibility.md#9300003-no-accessibility-permission-to-perform-the-operation) |

## getAccessibilityWindowsSync

```TypeScript
getAccessibilityWindowsSync(displayId?: number): Array<AccessibilityElement>
```

Obtains the accessibility windows.

**Since:** 20

**Required permissions:** ohos.permission.ACCESSIBILITY_EXTENSION_ABILITY

<!--Device-AccessibilityExtensionContext-getAccessibilityWindowsSync(displayId?: long): Array<AccessibilityElement>--><!--Device-AccessibilityExtensionContext-getAccessibilityWindowsSync(displayId?: long): Array<AccessibilityElement>-End-->

**System capability:** SystemCapability.BarrierFree.Accessibility.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| displayId | number | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Array&lt;AccessibilityElement&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [9300003](../errorcode-accessibility.md#9300003-no-accessibility-permission-to-perform-the-operation) |

## getDefaultFocusedElementIds

```TypeScript
getDefaultFocusedElementIds(windowId: number): Promise<Array<number>>
```

Obtains the custom default focuses of an application. This API uses a promise to return the result.

**Since:** 18

<!--Device-AccessibilityExtensionContext-getDefaultFocusedElementIds(windowId: int): Promise<Array<long>>--><!--Device-AccessibilityExtensionContext-getDefaultFocusedElementIds(windowId: int): Promise<Array<long>>-End-->

**System capability:** SystemCapability.BarrierFree.Accessibility.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| windowId | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;Array&lt;number&gt;&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [9300003](../errorcode-accessibility.md#9300003-no-accessibility-permission-to-perform-the-operation) |

## getElements

```TypeScript
getElements(windowId: number, elementId?: number): Promise<Array<AccessibilityElement>>
```

Obtains node elements in batches. This API uses a promise to return the result.

**Since:** 18

<!--Device-AccessibilityExtensionContext-getElements(windowId: int, elementId?: long): Promise<Array<AccessibilityElement>>--><!--Device-AccessibilityExtensionContext-getElements(windowId: int, elementId?: long): Promise<Array<AccessibilityElement>>-End-->

**System capability:** SystemCapability.BarrierFree.Accessibility.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| windowId | number | Yes |
| elementId | number | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;Array&lt;AccessibilityElement&gt;&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [9300003](../errorcode-accessibility.md#9300003-no-accessibility-permission-to-perform-the-operation) |

## getRootInActiveWindow

```TypeScript
getRootInActiveWindow(windowId?: number): Promise<AccessibilityElement>
```

Obtains the root element of an active window. This API uses a promise to return the result.

**Since:** 20

**Required permissions:** ohos.permission.ACCESSIBILITY_EXTENSION_ABILITY

<!--Device-AccessibilityExtensionContext-getRootInActiveWindow(windowId?: int): Promise<AccessibilityElement>--><!--Device-AccessibilityExtensionContext-getRootInActiveWindow(windowId?: int): Promise<AccessibilityElement>-End-->

**System capability:** SystemCapability.BarrierFree.Accessibility.Core

**System API:** This is a system API.

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
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [9300006](../errorcode-accessibility.md#9300006-failed-to-connect-the-target-app-and-accessibility-service) |
| [9300003](../errorcode-accessibility.md#9300003-no-accessibility-permission-to-perform-the-operation) |

## holdRunningLockSync

```TypeScript
holdRunningLockSync(): void
```

Holds the running lock. After the lock is held, the screen will not turn off automatically.

**Since:** 20

**Required permissions:** ohos.permission.ACCESSIBILITY_EXTENSION_ABILITY

<!--Device-AccessibilityExtensionContext-holdRunningLockSync(): void--><!--Device-AccessibilityExtensionContext-holdRunningLockSync(): void-End-->

**System capability:** SystemCapability.BarrierFree.Accessibility.Core

**System API:** This is a system API.

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## notifyDisconnect

```TypeScript
notifyDisconnect(): void
```

Notifies the accessibility service that the accessibility extension service can be disconnected.

This API must be used together with the   
[on('preDisconnect')](AccessibilityExtensionContext#on(type: 'preDisconnect', callback: Callback&lt;void&gt;)) API.If the **on('preDisconnect')** API is not called, this API does not take effect.

**Since:** 20

**Required permissions:** ohos.permission.ACCESSIBILITY_EXTENSION_ABILITY

<!--Device-AccessibilityExtensionContext-notifyDisconnect(): void--><!--Device-AccessibilityExtensionContext-notifyDisconnect(): void-End-->

**System capability:** SystemCapability.BarrierFree.Accessibility.Core

**System API:** This is a system API.

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## off('preDisconnect')

```TypeScript
off(type: 'preDisconnect', callback?: Callback<void>): void
```

Unsubscribes from the pre-disconnection event of the accessibility extension service. This API is not called until the accessibility extension service is disconnected. This API uses an asynchronous callback to return the result.

**Since:** 20

**Required permissions:** ohos.permission.ACCESSIBILITY_EXTENSION_ABILITY

<!--Device-AccessibilityExtensionContext-off(type: 'preDisconnect', callback?: Callback<void>): void--><!--Device-AccessibilityExtensionContext-off(type: 'preDisconnect', callback?: Callback<void>): void-End-->

**System capability:** SystemCapability.BarrierFree.Accessibility.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'preDisconnect' | Yes |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;void&gt; | No |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## on('preDisconnect')

```TypeScript
on(type: 'preDisconnect', callback: Callback<void>): void
```

Subscribes to the pre-disconnection event of the accessibility extension service. This API is called when the accessibility extension service is about to be disconnected. This API uses an asynchronous callback to return the result.

Used together with [notifyDisconnect](arkts-accessibility-accessibilityextensioncontext-c-sys.md#notifydisconnect); otherwise, the accessibility extension service is automatically disconnected 30 seconds later by default.

**Since:** 20

**Required permissions:** ohos.permission.ACCESSIBILITY_EXTENSION_ABILITY

<!--Device-AccessibilityExtensionContext-on(type: 'preDisconnect', callback: Callback<void>): void--><!--Device-AccessibilityExtensionContext-on(type: 'preDisconnect', callback: Callback<void>): void-End-->

**System capability:** SystemCapability.BarrierFree.Accessibility.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'preDisconnect' | Yes |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## removeAccessibilityVirtualNodes

```TypeScript
removeAccessibilityVirtualNodes(elementId: number, windowId: number): Promise<OperateVirtualNodeResult>
```

Remove accessibility virtual nodes.

**Since:** 26.0.0

**Required permissions:** ohos.permission.ACCESSIBILITY_EXTENSION_ABILITY

**Model restriction:** This API can be used only in the stage model.

<!--Device-AccessibilityExtensionContext-removeAccessibilityVirtualNodes(elementId: long, windowId: int): Promise<OperateVirtualNodeResult>--><!--Device-AccessibilityExtensionContext-removeAccessibilityVirtualNodes(elementId: long, windowId: int): Promise<OperateVirtualNodeResult>-End-->

**System capability:** SystemCapability.BarrierFree.Accessibility.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| elementId | number | Yes |
| windowId | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[OperateVirtualNodeResult](arkts-accessibility-accessibility-operatevirtualnoderesult-e-sys.md)&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [9300000](../errorcode-accessibility.md#9300000-accessibility-system-service-abnormal) |

## startAbility

```TypeScript
startAbility(want: Want): Promise<void>
```

Starts the foreground page. This API uses a promise to return the result.

**Since:** 12

<!--Device-AccessibilityExtensionContext-startAbility(want: Want): Promise<void>--><!--Device-AccessibilityExtensionContext-startAbility(want: Want): Promise<void>-End-->

**System capability:** SystemCapability.BarrierFree.Accessibility.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| want | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;void&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [201](../../errorcode-universal.md#201-permission-denied) |

## unholdRunningLockSync

```TypeScript
unholdRunningLockSync(): void
```

Releases the running lock. After the lock is released, the screen will automatically turn off.

**Since:** 20

**Required permissions:** ohos.permission.ACCESSIBILITY_EXTENSION_ABILITY

<!--Device-AccessibilityExtensionContext-unholdRunningLockSync(): void--><!--Device-AccessibilityExtensionContext-unholdRunningLockSync(): void-End-->

**System capability:** SystemCapability.BarrierFree.Accessibility.Core

**System API:** This is a system API.

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## updateAccessibilityElementProperty

```TypeScript
updateAccessibilityElementProperty(elementId: number, windowId: number, node: AccessibilityVirtualNode): Promise<OperateVirtualNodeResult>
```

Update accessibility element property.

**Since:** 26.0.0

**Required permissions:** ohos.permission.ACCESSIBILITY_EXTENSION_ABILITY

**Model restriction:** This API can be used only in the stage model.

<!--Device-AccessibilityExtensionContext-updateAccessibilityElementProperty(elementId: long, windowId: int, node: AccessibilityVirtualNode): Promise<OperateVirtualNodeResult>--><!--Device-AccessibilityExtensionContext-updateAccessibilityElementProperty(elementId: long, windowId: int, node: AccessibilityVirtualNode): Promise<OperateVirtualNodeResult>-End-->

**System capability:** SystemCapability.BarrierFree.Accessibility.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| elementId | number | Yes |
| windowId | number | Yes |
| node | [AccessibilityVirtualNode](arkts-accessibility-accessibilityvirtualnode-t-sys.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[OperateVirtualNodeResult](arkts-accessibility-accessibility-operatevirtualnoderesult-e-sys.md)&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [9300000](../errorcode-accessibility.md#9300000-accessibility-system-service-abnormal) |
