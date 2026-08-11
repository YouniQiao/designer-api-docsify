# AccessibilityExtensionContext

辅助功能扩展的上下文环境，用来配置辅助应用关注信息类型、查询节点信息、手势注入等。

**继承/实现关系：** AccessibilityExtensionContext extends [ExtensionContext](../../apis-ability-kit/arkts-apis/arkts-ability-extensioncontext-c.md/arkts-ability-extensioncontext-c.md)

**起始版本：** 9

<!--Device-unnamed-declare class AccessibilityExtensionContext extends ExtensionContext--><!--Device-unnamed-declare class AccessibilityExtensionContext extends ExtensionContext-End-->

**系统能力：** SystemCapability.BarrierFree.Accessibility.Core

## getFocusElement

```TypeScript
getFocusElement(isAccessibilityFocus: boolean, callback: AsyncCallback<AccessibilityElement>): void
```

获取焦点元素, 使用callback异步回调。

**起始版本：** 9

**废弃版本：** 12

<!--Device-AccessibilityExtensionContext-getFocusElement(isAccessibilityFocus: boolean, callback: AsyncCallback<AccessibilityElement>): void--><!--Device-AccessibilityExtensionContext-getFocusElement(isAccessibilityFocus: boolean, callback: AsyncCallback<AccessibilityElement>): void-End-->

**系统能力：** SystemCapability.BarrierFree.Accessibility.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| isAccessibilityFocus | boolean | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;AccessibilityElement&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |
| [9300003](../errorcode-accessibility.md#9300003-不具备执行该操作的无障碍权限) |

## getFocusElement

```TypeScript
getFocusElement(isAccessibilityFocus?: boolean): Promise<AccessibilityElement>
```

获取焦点元素, 使用Promise异步回调。

**起始版本：** 9

**废弃版本：** 12

<!--Device-AccessibilityExtensionContext-getFocusElement(isAccessibilityFocus?: boolean): Promise<AccessibilityElement>--><!--Device-AccessibilityExtensionContext-getFocusElement(isAccessibilityFocus?: boolean): Promise<AccessibilityElement>-End-->

**系统能力：** SystemCapability.BarrierFree.Accessibility.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| isAccessibilityFocus | boolean | 否 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;AccessibilityElement&gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |
| [9300003](../errorcode-accessibility.md#9300003-不具备执行该操作的无障碍权限) |

## getFocusElement

```TypeScript
getFocusElement(callback: AsyncCallback<AccessibilityElement>): void
```

获取焦点元素, 使用callback异步回调。

**起始版本：** 9

**废弃版本：** 12

<!--Device-AccessibilityExtensionContext-getFocusElement(callback: AsyncCallback<AccessibilityElement>): void--><!--Device-AccessibilityExtensionContext-getFocusElement(callback: AsyncCallback<AccessibilityElement>): void-End-->

**系统能力：** SystemCapability.BarrierFree.Accessibility.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;AccessibilityElement&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |
| [9300003](../errorcode-accessibility.md#9300003-不具备执行该操作的无障碍权限) |

## getWindowRootElement

```TypeScript
getWindowRootElement(windowId: number, callback: AsyncCallback<AccessibilityElement>): void
```

获取指定窗口的根节点元素, 使用callback异步回调。

**起始版本：** 9

**废弃版本：** 12

<!--Device-AccessibilityExtensionContext-getWindowRootElement(windowId: int, callback: AsyncCallback<AccessibilityElement>): void--><!--Device-AccessibilityExtensionContext-getWindowRootElement(windowId: int, callback: AsyncCallback<AccessibilityElement>): void-End-->

**系统能力：** SystemCapability.BarrierFree.Accessibility.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| windowId | number | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;AccessibilityElement&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |
| [9300003](../errorcode-accessibility.md#9300003-不具备执行该操作的无障碍权限) |

## getWindowRootElement

```TypeScript
getWindowRootElement(windowId?: number): Promise<AccessibilityElement>
```

获取指定窗口的根节点元素, 使用Promise异步回调。

**起始版本：** 9

**废弃版本：** 12

<!--Device-AccessibilityExtensionContext-getWindowRootElement(windowId?: int): Promise<AccessibilityElement>--><!--Device-AccessibilityExtensionContext-getWindowRootElement(windowId?: int): Promise<AccessibilityElement>-End-->

**系统能力：** SystemCapability.BarrierFree.Accessibility.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| windowId | number | 否 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;AccessibilityElement&gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |
| [9300003](../errorcode-accessibility.md#9300003-不具备执行该操作的无障碍权限) |

## getWindowRootElement

```TypeScript
getWindowRootElement(callback: AsyncCallback<AccessibilityElement>): void
```

获取指定窗口的根节点元素, 使用callback异步回调。

**起始版本：** 9

**废弃版本：** 12

<!--Device-AccessibilityExtensionContext-getWindowRootElement(callback: AsyncCallback<AccessibilityElement>): void--><!--Device-AccessibilityExtensionContext-getWindowRootElement(callback: AsyncCallback<AccessibilityElement>): void-End-->

**系统能力：** SystemCapability.BarrierFree.Accessibility.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;AccessibilityElement&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |
| [9300003](../errorcode-accessibility.md#9300003-不具备执行该操作的无障碍权限) |

## getWindows

```TypeScript
getWindows(displayId: number, callback: AsyncCallback<Array<AccessibilityElement>>): void
```

获取指定屏幕中的所有窗口，使用callback异步回调。

**起始版本：** 9

**废弃版本：** 12

<!--Device-AccessibilityExtensionContext-getWindows(displayId: long, callback: AsyncCallback<Array<AccessibilityElement>>): void--><!--Device-AccessibilityExtensionContext-getWindows(displayId: long, callback: AsyncCallback<Array<AccessibilityElement>>): void-End-->

**系统能力：** SystemCapability.BarrierFree.Accessibility.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| displayId | number | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;AccessibilityElement&gt;&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |
| [9300003](../errorcode-accessibility.md#9300003-不具备执行该操作的无障碍权限) |

## getWindows

```TypeScript
getWindows(displayId?: number): Promise<Array<AccessibilityElement>>
```

获取指定屏幕中的所有窗口，使用Promise异步回调。

**起始版本：** 9

**废弃版本：** 12

<!--Device-AccessibilityExtensionContext-getWindows(displayId?: long): Promise<Array<AccessibilityElement>>--><!--Device-AccessibilityExtensionContext-getWindows(displayId?: long): Promise<Array<AccessibilityElement>>-End-->

**系统能力：** SystemCapability.BarrierFree.Accessibility.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| displayId | number | 否 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;Array&lt;AccessibilityElement&gt;&gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |
| [9300003](../errorcode-accessibility.md#9300003-不具备执行该操作的无障碍权限) |

## getWindows

```TypeScript
getWindows(callback: AsyncCallback<Array<AccessibilityElement>>): void
```

获取指定屏幕中的所有窗口，使用callback异步回调。

**起始版本：** 9

**废弃版本：** 12

<!--Device-AccessibilityExtensionContext-getWindows(callback: AsyncCallback<Array<AccessibilityElement>>): void--><!--Device-AccessibilityExtensionContext-getWindows(callback: AsyncCallback<Array<AccessibilityElement>>): void-End-->

**系统能力：** SystemCapability.BarrierFree.Accessibility.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;AccessibilityElement&gt;&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |
| [9300003](../errorcode-accessibility.md#9300003-不具备执行该操作的无障碍权限) |

## injectGesture

```TypeScript
injectGesture(gesturePath: GesturePath, callback: AsyncCallback<void>): void
```

注入手势，使用callback异步回调。

**起始版本：** 9

**废弃版本：** 10

**替代接口：** [AccessibilityExtensionContext.injectGestureSync](arkts-accessibility-accessibilityextensioncontext-c.md#injectgesturesync)

<!--Device-AccessibilityExtensionContext-injectGesture(gesturePath: GesturePath, callback: AsyncCallback<void>): void--><!--Device-AccessibilityExtensionContext-injectGesture(gesturePath: GesturePath, callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.BarrierFree.Accessibility.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| gesturePath | [GesturePath](arkts-accessibility-accessibility-gesturepath-gesturepath-c.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |
| [9300003](../errorcode-accessibility.md#9300003-不具备执行该操作的无障碍权限) |

## injectGesture

```TypeScript
injectGesture(gesturePath: GesturePath): Promise<void>
```

注入手势，使用Promise异步回调。

**起始版本：** 9

**废弃版本：** 10

**替代接口：** [AccessibilityExtensionContext.injectGestureSync](arkts-accessibility-accessibilityextensioncontext-c.md#injectgesturesync)

<!--Device-AccessibilityExtensionContext-injectGesture(gesturePath: GesturePath): Promise<void>--><!--Device-AccessibilityExtensionContext-injectGesture(gesturePath: GesturePath): Promise<void>-End-->

**系统能力：** SystemCapability.BarrierFree.Accessibility.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| gesturePath | [GesturePath](arkts-accessibility-accessibility-gesturepath-gesturepath-c.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;void&gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |
| [9300003](../errorcode-accessibility.md#9300003-不具备执行该操作的无障碍权限) |

## injectGestureSync

```TypeScript
injectGestureSync(gesturePath: GesturePath): void
```

注入手势。

**起始版本：** 10

**废弃版本：** 12

<!--Device-AccessibilityExtensionContext-injectGestureSync(gesturePath: GesturePath): void--><!--Device-AccessibilityExtensionContext-injectGestureSync(gesturePath: GesturePath): void-End-->

**系统能力：** SystemCapability.BarrierFree.Accessibility.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| gesturePath | [GesturePath](arkts-accessibility-accessibility-gesturepath-gesturepath-c.md) | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |
| [9300003](../errorcode-accessibility.md#9300003-不具备执行该操作的无障碍权限) |

## setTargetBundleName

```TypeScript
setTargetBundleName(targetNames: Array<string>, callback: AsyncCallback<void>): void
```

设置关注的目标包名，使用callback异步回调。

**起始版本：** 9

**废弃版本：** 12

<!--Device-AccessibilityExtensionContext-setTargetBundleName(targetNames: Array<string>, callback: AsyncCallback<void>): void--><!--Device-AccessibilityExtensionContext-setTargetBundleName(targetNames: Array<string>, callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.BarrierFree.Accessibility.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| targetNames | Array&lt;string&gt; | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |

## setTargetBundleName

```TypeScript
setTargetBundleName(targetNames: Array<string>): Promise<void>
```

设置关注的目标包名，使用Promise异步回调。

**起始版本：** 9

**废弃版本：** 12

<!--Device-AccessibilityExtensionContext-setTargetBundleName(targetNames: Array<string>): Promise<void>--><!--Device-AccessibilityExtensionContext-setTargetBundleName(targetNames: Array<string>): Promise<void>-End-->

**系统能力：** SystemCapability.BarrierFree.Accessibility.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| targetNames | Array&lt;string&gt; | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;void&gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |
