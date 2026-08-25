# FloatViewController

标准悬浮窗控制器实例。用于启动、停止标准悬浮窗以及注册回调等操作。下列API示例中都需先使用[floatView.create()](arkts-arkui-floatview-create-f.md)方法获取到标准悬浮窗控制器实例（即floatViewController），再通过此实例调用对应方法。

**起始版本：** 26.0.0

**系统能力：** SystemCapability.Window.SessionManager

## 导入模块

```TypeScript
import { floatView } from 'kits/@kit.ArkUI';
```

## getWindowProperties

```TypeScript
getWindowProperties(): FloatViewProperties
```

获取标准悬浮窗窗口的属性。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Window.SessionManager

**返回值：**

| 类型 |
| --- |
| [FloatViewProperties](arkts-arkui-floatview-floatviewproperties-i.md) |

**错误码：**

| 错误码ID |
| --- |
| [1300002](../errorcode-window.md#1300002-窗口状态异常) |
| [1300031](../errorcode-window.md#1300031-闪控窗状态不支持该操作) |

## offLimitsChange

```TypeScript
offLimitsChange(callback?: Callback<FloatViewLimits>): void
```

取消标准悬浮窗限制变化的监听事件。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Window.SessionManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[FloatViewLimits](arkts-arkui-floatview-floatviewlimits-i.md)&gt; | 否 |

**错误码：**

| 错误码ID |
| --- |
| [1300002](../errorcode-window.md#1300002-窗口状态异常) |

## offRectChange

```TypeScript
offRectChange(callback?: Callback<FloatViewRectChangeInfo>): void
```

取消标准悬浮窗矩形区域变化的监听事件。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Window.SessionManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[FloatViewRectChangeInfo](arkts-arkui-floatview-floatviewrectchangeinfo-i.md)&gt; | 否 |

**错误码：**

| 错误码ID |
| --- |
| [1300002](../errorcode-window.md#1300002-窗口状态异常) |

## offStateChange

```TypeScript
offStateChange(callback?: Callback<FloatViewStateChangeInfo>): void
```

取消标准悬浮窗状态变化的监听事件。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Window.SessionManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[FloatViewStateChangeInfo](arkts-arkui-floatview-floatviewstatechangeinfo-i.md)&gt; | 否 |

**错误码：**

| 错误码ID |
| --- |
| [1300002](../errorcode-window.md#1300002-窗口状态异常) |

## onLimitsChange

```TypeScript
onLimitsChange(callback: Callback<FloatViewLimits>): void
```

注册标准悬浮窗限制变化的监听事件，当限制规格变化时触发回调，例如设备折叠或者展开。不再使用时，取消监听以避免内存泄漏。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Window.SessionManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[FloatViewLimits](arkts-arkui-floatview-floatviewlimits-i.md)&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [1300002](../errorcode-window.md#1300002-窗口状态异常) |
| [1300030](../errorcode-window.md#1300030-重复操作闪控窗) |

## onRectChange

```TypeScript
onRectChange(callback: Callback<FloatViewRectChangeInfo>): void
```

注册标准悬浮窗矩形区域（位置和大小）变化的监听事件。不再使用时，取消监听以避免内存泄漏。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Window.SessionManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[FloatViewRectChangeInfo](arkts-arkui-floatview-floatviewrectchangeinfo-i.md)&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [1300002](../errorcode-window.md#1300002-窗口状态异常) |
| [1300030](../errorcode-window.md#1300030-重复操作闪控窗) |

## onStateChange

```TypeScript
onStateChange(callback: Callback<FloatViewStateChangeInfo>): void
```

注册标准悬浮窗状态变化的监听事件。不再使用时，取消监听以避免内存泄漏。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Window.SessionManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[FloatViewStateChangeInfo](arkts-arkui-floatview-floatviewstatechangeinfo-i.md)&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [1300002](../errorcode-window.md#1300002-窗口状态异常) |
| [1300030](../errorcode-window.md#1300030-重复操作闪控窗) |

## restoreMainWindow

```TypeScript
restoreMainWindow(wantParameters?: Record<string, Object>): Promise<void>
```

恢复标准悬浮窗的主窗口到前台显示。如果主窗口已处于前台时调用，将抬升主窗口层级。此接口只能在标准悬浮窗窗口被点击后使用。当主窗口处于PAUSED生命周期或处于多任务状态时，调用接口将抛出错误码1300032。使用Promise 异步回调。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Window.SessionManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [wantParameters](../../apis-notification-kit/arkts-apis/arkts-notification-notificationrequest-notificationparameters-i.md) | Record & lt;string, Object & gt; | 否 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [1300002](../errorcode-window.md#1300002-窗口状态异常) |
| [1300003](../errorcode-window.md#1300003-系统服务工作异常) |
| [1300031](../errorcode-window.md#1300031-闪控窗状态不支持该操作) |
| [1300032](../errorcode-window.md#1300032-恢复主窗口失败) |

## setFloatViewVisibilityInApp

```TypeScript
setFloatViewVisibilityInApp(isVisible: boolean): Promise<void>
```

设置应用在前台时标准悬浮窗窗口是否可见。使用Promise异步回调。创建标准悬浮窗后未调用此接口前，默认其在应用处于前台时为可见状态。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Window.SessionManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| isVisible | boolean | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [1300002](../errorcode-window.md#1300002-窗口状态异常) |
| [1300003](../errorcode-window.md#1300003-系统服务工作异常) |

## setUIContext

```TypeScript
setUIContext(path: string, storage?: LocalStorage): Promise<void>
```

根据当前工程中指定的页面路径为标准悬浮窗加载具体页面内容，通过LocalStorage传递状态属性至加载页面。使用Promise异步回调。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Window.SessionManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| path | string | 是 |
| storage | [LocalStorage](arkts-arkui-localstorage-c.md) | 否 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [1300002](../errorcode-window.md#1300002-窗口状态异常) |
| [1300016](../errorcode-window.md#1300016-参数校验错误) |

## setUIContextByName

```TypeScript
setUIContextByName(name: string, storage?: LocalStorage): Promise<void>
```

根据指定路由页面名称为当前窗口加载[命名路由](../../../ui/arkts-routing.md#命名路由)页面，通过LocalStorage传递状态属性至加载页面，使用Promise异步回调。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Window.SessionManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| name | string | 是 |
| storage | [LocalStorage](arkts-arkui-localstorage-c.md) | 否 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [1300002](../errorcode-window.md#1300002-窗口状态异常) |
| [1300016](../errorcode-window.md#1300016-参数校验错误) |

## setWindowSize

```TypeScript
setWindowSize(size: window.Size): Promise<void>
```

设置标准悬浮窗窗口大小。建议先调用[getFloatViewLimits](arkts-arkui-floatview-getfloatviewlimits-f.md)接口获取推荐的宽高范围和宽高比范围，再根据推荐值调用本接口。窗口实际大小变化可通 过[onRectChange](#onrectchange)接口监 听。使用Promise异步回调。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Window.SessionManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| size | window.Size | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [1300002](../errorcode-window.md#1300002-窗口状态异常) |
| [1300003](../errorcode-window.md#1300003-系统服务工作异常) |
| [1300016](../errorcode-window.md#1300016-参数校验错误) |

## start

```TypeScript
start(): Promise<void>
```

启动标准悬浮窗窗口。接口返回不表示start流程结束，需要通过 [onStateChange](#onstatechange)接 口监听到STARTED回调时判断启动成功。建议在调用[setUIContext()](#setuicontext)或 [setUIContextByName()](#setuicontextbyname)后调用start()。使用Promise异步回调。

**起始版本：** 26.0.0

**需要权限：** ohos.permission.FLOAT_VIEW

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Window.SessionManager

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [1300002](../errorcode-window.md#1300002-窗口状态异常) |
| [1300003](../errorcode-window.md#1300003-系统服务工作异常) |
| [1300030](../errorcode-window.md#1300030-重复操作闪控窗) |
| [1300031](../errorcode-window.md#1300031-闪控窗状态不支持该操作) |
| [1300033](../errorcode-window.md#1300033-启动闪控窗失败) |
| [1300034](../errorcode-window.md#1300034-闪控窗与其他悬浮窗口操作冲突) |

## stop

```TypeScript
stop(): Promise<void>
```

停止标准悬浮窗窗口。接口返回不表示stop流程结束，需要通过 [onStateChange](#onstatechange)接 口监听到STOPPED回调时判断停止成功。使用Promise异步回调。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Window.SessionManager

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [1300002](../errorcode-window.md#1300002-窗口状态异常) |
| [1300003](../errorcode-window.md#1300003-系统服务工作异常) |
| [1300030](../errorcode-window.md#1300030-重复操作闪控窗) |
| [1300031](../errorcode-window.md#1300031-闪控窗状态不支持该操作) |

## switchTemplate

```TypeScript
switchTemplate(templateProperty: TemplateProperty): Promise<void>
```

切换标准悬浮窗的模板并改变其窗口尺寸。建议先调用[getFloatViewLimits](arkts-arkui-floatview-getfloatviewlimits-f.md)接口获取目标模板类型推荐的宽高范围和宽高比范围，再根据推荐值调用本 接口。窗口实际大小变化可通过 [onRectChange](#onrectchange)接口监听 。使用Promise异步回调。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Window.SessionManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| templateProperty | [TemplateProperty](arkts-arkui-floatview-templateproperty-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [1300002](../errorcode-window.md#1300002-窗口状态异常) |
| [1300003](../errorcode-window.md#1300003-系统服务工作异常) |
| [1300016](../errorcode-window.md#1300016-参数校验错误) |
