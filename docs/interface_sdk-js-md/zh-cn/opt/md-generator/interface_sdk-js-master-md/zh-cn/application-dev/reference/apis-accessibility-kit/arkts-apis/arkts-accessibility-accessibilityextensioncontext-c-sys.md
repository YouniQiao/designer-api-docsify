# AccessibilityExtensionContext

辅助功能扩展的上下文环境，用来配置辅助应用关注信息类型、查询节点信息、手势注入等。

**继承/实现关系：** AccessibilityExtensionContext extends [ExtensionContext](../../apis-ability-kit/arkts-apis/arkts-ability-extensioncontext-c.md/arkts-ability-extensioncontext-c.md)

**起始版本：** 9

<!--Device-unnamed-declare class AccessibilityExtensionContext extends ExtensionContext--><!--Device-unnamed-declare class AccessibilityExtensionContext extends ExtensionContext-End-->

**系统能力：** SystemCapability.BarrierFree.Accessibility.Core

## getAccessibilityFocusedElement

```TypeScript
getAccessibilityFocusedElement(): Promise<AccessibilityElement>
```

获取当前获得焦点的元素。使用Promise异步回调。

**起始版本：** 20

**需要权限：** ohos.permission.ACCESSIBILITY_EXTENSION_ABILITY

<!--Device-AccessibilityExtensionContext-getAccessibilityFocusedElement(): Promise<AccessibilityElement>--><!--Device-AccessibilityExtensionContext-getAccessibilityFocusedElement(): Promise<AccessibilityElement>-End-->

**系统能力：** SystemCapability.BarrierFree.Accessibility.Core

**系统接口：** 此接口为系统接口。

**返回值：**

| 类型 |
| --- |
| Promise&lt;AccessibilityElement&gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [9300006](../errorcode-accessibility.md#9300006-目标应用和无障碍服务建立连接失败) |
| [9300003](../errorcode-accessibility.md#9300003-不具备执行该操作的无障碍权限) |

## getAccessibilityWindowsSync

```TypeScript
getAccessibilityWindowsSync(displayId?: number): Array<AccessibilityElement>
```

获取窗口列表。

**起始版本：** 20

**需要权限：** ohos.permission.ACCESSIBILITY_EXTENSION_ABILITY

<!--Device-AccessibilityExtensionContext-getAccessibilityWindowsSync(displayId?: long): Array<AccessibilityElement>--><!--Device-AccessibilityExtensionContext-getAccessibilityWindowsSync(displayId?: long): Array<AccessibilityElement>-End-->

**系统能力：** SystemCapability.BarrierFree.Accessibility.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| displayId | number | 否 |

**返回值：**

| 类型 |
| --- |
| Array&lt;AccessibilityElement&gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [9300003](../errorcode-accessibility.md#9300003-不具备执行该操作的无障碍权限) |

## getDefaultFocusedElementIds

```TypeScript
getDefaultFocusedElementIds(windowId: number): Promise<Array<number>>
```

提供查询应用自定义默认焦点的能力。使用Promise异步回调。

**起始版本：** 18

<!--Device-AccessibilityExtensionContext-getDefaultFocusedElementIds(windowId: int): Promise<Array<long>>--><!--Device-AccessibilityExtensionContext-getDefaultFocusedElementIds(windowId: int): Promise<Array<long>>-End-->

**系统能力：** SystemCapability.BarrierFree.Accessibility.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| windowId | number | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;Array&lt;number&gt;&gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [9300003](../errorcode-accessibility.md#9300003-不具备执行该操作的无障碍权限) |

## getElements

```TypeScript
getElements(windowId: number, elementId?: number): Promise<Array<AccessibilityElement>>
```

提供批量查询节点的能力。使用Promise异步回调。

**起始版本：** 18

<!--Device-AccessibilityExtensionContext-getElements(windowId: int, elementId?: long): Promise<Array<AccessibilityElement>>--><!--Device-AccessibilityExtensionContext-getElements(windowId: int, elementId?: long): Promise<Array<AccessibilityElement>>-End-->

**系统能力：** SystemCapability.BarrierFree.Accessibility.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| windowId | number | 是 |
| elementId | number | 否 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;Array&lt;AccessibilityElement&gt;&gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [9300003](../errorcode-accessibility.md#9300003-不具备执行该操作的无障碍权限) |

## getRootInActiveWindow

```TypeScript
getRootInActiveWindow(windowId?: number): Promise<AccessibilityElement>
```

获取活动窗口根元素。使用Promise异步回调。

**起始版本：** 20

**需要权限：** ohos.permission.ACCESSIBILITY_EXTENSION_ABILITY

<!--Device-AccessibilityExtensionContext-getRootInActiveWindow(windowId?: int): Promise<AccessibilityElement>--><!--Device-AccessibilityExtensionContext-getRootInActiveWindow(windowId?: int): Promise<AccessibilityElement>-End-->

**系统能力：** SystemCapability.BarrierFree.Accessibility.Core

**系统接口：** 此接口为系统接口。

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
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [9300006](../errorcode-accessibility.md#9300006-目标应用和无障碍服务建立连接失败) |
| [9300003](../errorcode-accessibility.md#9300003-不具备执行该操作的无障碍权限) |

## holdRunningLockSync

```TypeScript
holdRunningLockSync(): void
```

持有RunningLock锁，持锁后，屏幕不会自动灭屏。

**起始版本：** 20

**需要权限：** ohos.permission.ACCESSIBILITY_EXTENSION_ABILITY

<!--Device-AccessibilityExtensionContext-holdRunningLockSync(): void--><!--Device-AccessibilityExtensionContext-holdRunningLockSync(): void-End-->

**系统能力：** SystemCapability.BarrierFree.Accessibility.Core

**系统接口：** 此接口为系统接口。

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

## notifyDisconnect

```TypeScript
notifyDisconnect(): void
```

通知无障碍服务可以关闭该无障碍扩展服务。

此函数需要与注册预关闭接口  
[on('preDisconnect')](AccessibilityExtensionContext#on(type: 'preDisconnect', callback: Callback&lt;void&gt;))配合使用，如果没有调用过注册预关闭函数，直接调用此函数不生效。

**起始版本：** 20

**需要权限：** ohos.permission.ACCESSIBILITY_EXTENSION_ABILITY

<!--Device-AccessibilityExtensionContext-notifyDisconnect(): void--><!--Device-AccessibilityExtensionContext-notifyDisconnect(): void-End-->

**系统能力：** SystemCapability.BarrierFree.Accessibility.Core

**系统接口：** 此接口为系统接口。

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

## off('preDisconnect')

```TypeScript
off(type: 'preDisconnect', callback?: Callback<void>): void
```

取消已经向无障碍服务注册的预关闭回调函数，无障碍服务关闭该扩展服务前不再执行该回调。使用callback异步回调。

**起始版本：** 20

**需要权限：** ohos.permission.ACCESSIBILITY_EXTENSION_ABILITY

<!--Device-AccessibilityExtensionContext-off(type: 'preDisconnect', callback?: Callback<void>): void--><!--Device-AccessibilityExtensionContext-off(type: 'preDisconnect', callback?: Callback<void>): void-End-->

**系统能力：** SystemCapability.BarrierFree.Accessibility.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'preDisconnect' | 是 |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;void&gt; | 否 |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

## on('preDisconnect')

```TypeScript
on(type: 'preDisconnect', callback: Callback<void>): void
```

向无障碍服务注册回调函数，在无障碍服务关闭该无障碍扩展服务前会执行该回调函数。使用callback异步回调。

此注册函数需要与[notifyDisconnect](arkts-accessibility-accessibilityextensioncontext-c-sys.md#notifydisconnect)配合使用，如果不调用  
[notifyDisconnect](arkts-accessibility-accessibilityextensioncontext-c-sys.md#notifydisconnect)，则默认等待30秒后，无障碍扩展服务会自动关闭。

**起始版本：** 20

**需要权限：** ohos.permission.ACCESSIBILITY_EXTENSION_ABILITY

<!--Device-AccessibilityExtensionContext-on(type: 'preDisconnect', callback: Callback<void>): void--><!--Device-AccessibilityExtensionContext-on(type: 'preDisconnect', callback: Callback<void>): void-End-->

**系统能力：** SystemCapability.BarrierFree.Accessibility.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'preDisconnect' | 是 |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

## startAbility

```TypeScript
startAbility(want: Want): Promise<void>
```

提供拉起前台页面的能力。使用Promise异步回调。

**起始版本：** 12

<!--Device-AccessibilityExtensionContext-startAbility(want: Want): Promise<void>--><!--Device-AccessibilityExtensionContext-startAbility(want: Want): Promise<void>-End-->

**系统能力：** SystemCapability.BarrierFree.Accessibility.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| want | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;void&gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |
| [201](../../errorcode-universal.md#201-权限校验失败) |

## unholdRunningLockSync

```TypeScript
unholdRunningLockSync(): void
```

释放RunningLock锁，恢复自动灭屏。

**起始版本：** 20

**需要权限：** ohos.permission.ACCESSIBILITY_EXTENSION_ABILITY

<!--Device-AccessibilityExtensionContext-unholdRunningLockSync(): void--><!--Device-AccessibilityExtensionContext-unholdRunningLockSync(): void-End-->

**系统能力：** SystemCapability.BarrierFree.Accessibility.Core

**系统接口：** 此接口为系统接口。

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
