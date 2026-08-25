# Window

当前窗口实例，窗口管理器管理的基本单元。下列API示例中都需先使用 [getLastWindow()](arkts-arkui-window-getlastwindow-f.md)、 [createWindow()](arkts-arkui-window-createwindow-f.md)、 [findWindow()](arkts-arkui-window-findwindow-f.md)中的任一方法获取到Window实例（windowClass），再通过此实例调用对应方法。

**起始版本：** 6

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

## 导入模块

```TypeScript
import { window } from 'kits/@kit.ArkUI';
```

## attachLayoutToParentWindow

```TypeScript
attachLayoutToParentWindow(anchorInfo?: WindowAnchorInfo, attachOptions?: SubWindowAttachOptions): Promise<void>
```

设置一级子窗与主窗保持相对位置不变。使用Promise异步回调。该相对位置通过子窗与主窗之间的锚点偏移量表示，子窗和主窗使用的窗口锚点相同。

> **说明：**&gt;
> - 只支持一级子窗调用该接口，子窗需处于自由悬浮窗口模式（即窗口模式为window.WindowStatusType.FLOATING）。&gt;
> - 当子窗调用该接口后，立即使其显示位置跟随主窗并保持相对位置不变，并且可以监听主窗大小及模式切换。除非调用
> [detachLayoutToParentWindow()](#detachlayouttoparentwindow)接口解绑，否则效果将持续。&gt;
> - 当子窗调用该接口后，再调用
> [moveWindowTo()](arkts-arkui-window-window-i.md#movewindowto)、
> [maximize()](arkts-arkui-window-window-i.md#maximize)、
> [setFollowParentWindowLayoutEnabled()](arkts-arkui-window-window-i.md#setfollowparentwindowlayoutenabled)等修改窗
> 口位置的接口，或通过鼠标/触摸操作对子窗进行拖拽移动、拖拽缩放时将不生效。

**起始版本：** 24

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Window.SessionManager

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| anchorInfo | [WindowAnchorInfo](arkts-arkui-window-windowanchorinfo-i-sys.md) | 否 |
| attachOptions | [SubWindowAttachOptions](arkts-arkui-window-subwindowattachoptions-i-sys.md) | 否 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [1300002](../errorcode-window.md#1300002-窗口状态异常) |
| [1300003](../errorcode-window.md#1300003-系统服务工作异常) |
| [1300004](../errorcode-window.md#1300004-无权限操作) |
| [1300010](../errorcode-window.md#1300010-当前窗口模式不支持该操作) |

## bindDialogTarget

```TypeScript
bindDialogTarget(token: rpc.RemoteObject, deathCallback: Callback<void>): Promise<void>
```

绑定模态窗口与目标窗口，成功绑定后，目标窗口不能响应用户操作。同时添加目标窗口销毁监听，使用Promise异步回调。

**起始版本：** 9

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| token | rpc.RemoteObject | 是 |
| deathCallback | [Callback](arkts-arkui-window-callback-i.md)&lt;void&gt; | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [1300002](../errorcode-window.md#1300002-窗口状态异常) |
| [1300003](../errorcode-window.md#1300003-系统服务工作异常) |

## bindDialogTarget

```TypeScript
bindDialogTarget(token: rpc.RemoteObject, deathCallback: Callback<void>, callback: AsyncCallback<void>): void
```

绑定模态窗口与目标窗口，成功绑定后，目标窗口不能响应用户操作。同时添加目标窗口销毁监听，使用callback异步回调。

**起始版本：** 9

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| token | rpc.RemoteObject | 是 |
| deathCallback | [Callback](arkts-arkui-window-callback-i.md)&lt;void&gt; | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [1300002](../errorcode-window.md#1300002-窗口状态异常) |
| [1300003](../errorcode-window.md#1300003-系统服务工作异常) |

## bindDialogTarget

```TypeScript
bindDialogTarget(requestInfo: dialogRequest.RequestInfo, deathCallback: Callback<void>): Promise<void>
```

绑定模态窗口与目标窗口，成功绑定后，目标窗口不能响应用户操作。同时添加目标窗口销毁监听，使用Promise异步回调。

**起始版本：** 9

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| requestInfo | dialogRequest.RequestInfo | 是 |
| deathCallback | [Callback](arkts-arkui-window-callback-i.md)&lt;void&gt; | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [1300002](../errorcode-window.md#1300002-窗口状态异常) |
| [1300003](../errorcode-window.md#1300003-系统服务工作异常) |

## bindDialogTarget

```TypeScript
bindDialogTarget(requestInfo: dialogRequest.RequestInfo, deathCallback: Callback<void>, callback: AsyncCallback<void>): void
```

绑定模态窗口与目标窗口，成功绑定后，目标窗口不能响应用户操作。同时添加目标窗口销毁监听，使用callback异步回调。

**起始版本：** 9

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| requestInfo | dialogRequest.RequestInfo | 是 |
| deathCallback | [Callback](arkts-arkui-window-callback-i.md)&lt;void&gt; | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [1300002](../errorcode-window.md#1300002-窗口状态异常) |
| [1300003](../errorcode-window.md#1300003-系统服务工作异常) |

## detachLayoutToParentWindow

```TypeScript
detachLayoutToParentWindow(): Promise<void>
```

解除一级子窗与主窗保持相对位置不变的协同关系。使用Promise异步回调。

> **说明：**&gt;
> - 子窗调用接口时需保持子窗处于协同状态。&gt;
> - 调用接口解除协同后，子窗将保持协同时的位置，可对子窗进行拖拽以修改子窗大小和位置。&gt;
> - 解除协同后，调用
> [moveWindowTo()](arkts-arkui-window-window-i.md#movewindowto)、
> [maximize()](arkts-arkui-window-window-i.md#maximize)、
> [setFollowParentWindowLayoutEnabled()](arkts-arkui-window-window-i.md#setfollowparentwindowlayoutenabled)修改窗口
> 位置的接口，或通过鼠标/触摸操作对子窗进行拖拽移动、拖拽缩放时将生效。

**起始版本：** 24

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Window.SessionManager

**系统接口：** 此接口为系统接口。

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [1300002](../errorcode-window.md#1300002-窗口状态异常) |
| [1300003](../errorcode-window.md#1300003-系统服务工作异常) |
| [1300004](../errorcode-window.md#1300004-无权限操作) |
| [1300010](../errorcode-window.md#1300010-当前窗口模式不支持该操作) |

## getRotationLocked

```TypeScript
getRotationLocked(): boolean
```

仅支持[系统窗口](../../../windowmanager/window-terminology.md#系统窗口)获取当前旋转锁定状态。非系统窗口调用返回1300029错误码。

**起始版本：** 22

**系统能力：** SystemCapability.Window.SessionManager

**系统接口：** 此接口为系统接口。

**返回值：**

| 类型 |
| --- |
| boolean |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [1300002](../errorcode-window.md#1300002-窗口状态异常) |
| [1300003](../errorcode-window.md#1300003-系统服务工作异常) |
| 1300029 |

## getTransitionController

```TypeScript
getTransitionController(): TransitionController
```

获取窗口属性转换控制器。

**起始版本：** 9

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**系统接口：** 此接口为系统接口。

**返回值：**

| 类型 |
| --- |
| [TransitionController](arkts-arkui-window-transitioncontroller-i-sys.md) |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [1300002](../errorcode-window.md#1300002-窗口状态异常) |
| [1300004](../errorcode-window.md#1300004-无权限操作) |

## hide

```TypeScript
hide (callback: AsyncCallback<void>): void
```

隐藏当前窗口，使用callback异步回调，仅支持系统窗口与应用子窗口。

**起始版本：** 7

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [1300002](../errorcode-window.md#1300002-窗口状态异常) |

## hide

```TypeScript
hide(): Promise<void>
```

隐藏当前窗口，使用Promise异步回调，仅支持系统窗口与应用子窗口。

**起始版本：** 7

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**系统接口：** 此接口为系统接口。

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [1300002](../errorcode-window.md#1300002-窗口状态异常) |

## hideNonSystemFloatingWindows

```TypeScript
hideNonSystemFloatingWindows(shouldHide: boolean, callback: AsyncCallback<void>): void
```

设置是否隐藏非系统级悬浮窗口（[windowType](arkts-arkui-window-windowtype-e.md)类型为TYPE_FLOAT），使用callback异步回调。非系统级悬浮窗口是指非系统应用创建的悬浮窗口。默认情况下，一个系统应用主窗口可以与非系统级悬浮窗口共同显示，即该主窗口可以被上层的非系统级悬浮窗口遮挡，如果设置为true，则所有的非系统级悬浮窗口都会被隐藏，此时该主窗口就不会 被上层的非系统级悬浮窗口遮挡。

**起始版本：** 11

**系统能力：** SystemCapability.Window.SessionManager

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| shouldHide | boolean | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [1300002](../errorcode-window.md#1300002-窗口状态异常) |
| [1300003](../errorcode-window.md#1300003-系统服务工作异常) |
| [1300004](../errorcode-window.md#1300004-无权限操作) |

## hideNonSystemFloatingWindows

```TypeScript
hideNonSystemFloatingWindows(shouldHide: boolean): Promise<void>
```

设置是否隐藏非系统级悬浮窗口（[windowType](arkts-arkui-window-windowtype-e.md)类型为TYPE_FLOAT），使用Promise异步回调。非系统级悬浮窗口是指非系统应用创建的悬浮窗口。默认情况下，一个系统应用主窗口可以与非系统级悬浮窗口共同显示，即该主窗口可以被上层的非系统级悬浮窗口遮挡，如果设置为true，则所有的非系统级悬浮窗口都会被隐藏，此时该主窗口就不会 被上层的非系统级悬浮窗口遮挡。

**起始版本：** 11

**系统能力：** SystemCapability.Window.SessionManager

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| shouldHide | boolean | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [1300002](../errorcode-window.md#1300002-窗口状态异常) |
| [1300003](../errorcode-window.md#1300003-系统服务工作异常) |
| [1300004](../errorcode-window.md#1300004-无权限操作) |

## hideWithAnimation

```TypeScript
hideWithAnimation(callback: AsyncCallback<void>): void
```

隐藏当前窗口，过程中播放动画，使用callback异步回调，仅支持系统窗口。

**起始版本：** 9

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [1300002](../errorcode-window.md#1300002-窗口状态异常) |
| [1300003](../errorcode-window.md#1300003-系统服务工作异常) |
| [1300004](../errorcode-window.md#1300004-无权限操作) |

## hideWithAnimation

```TypeScript
hideWithAnimation(): Promise<void>
```

隐藏当前窗口，过程中播放动画，使用Promise异步回调，仅支持系统窗口。

**起始版本：** 9

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**系统接口：** 此接口为系统接口。

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [1300002](../errorcode-window.md#1300002-窗口状态异常) |
| [1300003](../errorcode-window.md#1300003-系统服务工作异常) |
| [1300004](../errorcode-window.md#1300004-无权限操作) |

## isMainWindowFullScreenAcrossDisplays

```TypeScript
isMainWindowFullScreenAcrossDisplays(): Promise<boolean>
```

判断当前窗口的主窗口是否是跨多块屏幕使用全屏模式显示，使用Promise异步回调，仅支持主窗口与应用子窗口。

**起始版本：** 20

**系统能力：** SystemCapability.Window.SessionManager

**系统接口：** 此接口为系统接口。

**返回值：**

| 类型 |
| --- |
| Promise & lt;boolean & gt; |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [1300002](../errorcode-window.md#1300002-窗口状态异常) |
| [1300003](../errorcode-window.md#1300003-系统服务工作异常) |
| [1300004](../errorcode-window.md#1300004-无权限操作) |

## off('mainWindowFullScreenAcrossDisplaysChanged')

```TypeScript
off(type: 'mainWindowFullScreenAcrossDisplaysChanged', callback?: Callback<boolean>): void
```

取消监听本窗口的主窗口跨多块屏幕使用全屏模式显示的状态变化事件。

**起始版本：** 20

**系统能力：** SystemCapability.Window.SessionManager

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'mainWindowFullScreenAcrossDisplaysChanged' | 是 |
| callback | [Callback](arkts-arkui-window-callback-i.md)&lt;boolean&gt; | 否 |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [1300002](../errorcode-window.md#1300002-窗口状态异常) |
| [1300003](../errorcode-window.md#1300003-系统服务工作异常) |
| [1300004](../errorcode-window.md#1300004-无权限操作) |

## on('mainWindowFullScreenAcrossDisplaysChanged')

```TypeScript
on(type: 'mainWindowFullScreenAcrossDisplaysChanged', callback: Callback<boolean>): void
```

监听本窗口的主窗口跨多块屏幕使用全屏模式显示的状态变化事件。

**起始版本：** 20

**系统能力：** SystemCapability.Window.SessionManager

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'mainWindowFullScreenAcrossDisplaysChanged' | 是 |
| callback | [Callback](arkts-arkui-window-callback-i.md)&lt;boolean&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [1300002](../errorcode-window.md#1300002-窗口状态异常) |
| [1300003](../errorcode-window.md#1300003-系统服务工作异常) |
| [1300004](../errorcode-window.md#1300004-无权限操作) |

## opacity

```TypeScript
opacity(opacity: number): void
```

设置窗口不透明度。仅支持在[自定义系统窗口的显示与隐藏动画](../../../windowmanager/system-window-stage-sys.md#自定义系统窗口的显示与隐藏动画)中使用。

**起始版本：** 9

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [opacity](#opacity) | number | 是 |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [1300002](../errorcode-window.md#1300002-窗口状态异常) |
| [1300004](../errorcode-window.md#1300004-无权限操作) |

## raiseAboveTarget

```TypeScript
raiseAboveTarget(windowId: number, callback: AsyncCallback<void>): void
```

将同一个主窗口下的子窗口抬升到目标子窗口之上。使用callback异步回调。使用该接口需要确保要抬升的子窗口和目标子窗口都已创建完成，分别调用 [showWindow()](arkts-arkui-window-window-i.md#showwindow)并执行完毕。

**起始版本：** 10

**系统能力：** SystemCapability.Window.SessionManager

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| windowId | number | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [1300002](../errorcode-window.md#1300002-窗口状态异常) |
| [1300003](../errorcode-window.md#1300003-系统服务工作异常) |
| [1300004](../errorcode-window.md#1300004-无权限操作) |
| [1300009](../errorcode-window.md#1300009-父窗口无效) |

## raiseAboveTarget

```TypeScript
raiseAboveTarget(windowId: number): Promise<void>
```

将同一个主窗下的子窗口提升到目标子窗口之上。使用Promise异步回调。使用该接口需要确保要抬升的子窗口和目标子窗口都已创建完成，分别调用 [showWindow()](arkts-arkui-window-window-i.md#showwindow)并执行完毕。

**起始版本：** 10

**系统能力：** SystemCapability.Window.SessionManager

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| windowId | number | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [1300002](../errorcode-window.md#1300002-窗口状态异常) |
| [1300003](../errorcode-window.md#1300003-系统服务工作异常) |
| [1300004](../errorcode-window.md#1300004-无权限操作) |
| [1300009](../errorcode-window.md#1300009-父窗口无效) |

## raiseMainWindowAboveTarget

```TypeScript
raiseMainWindowAboveTarget(windowId: number): Promise<void>
```

将主窗口的层级调整至同应用下的另一个主窗口之上，子窗口的层级会跟随所属主窗口变动。使用Promise异步回调。仅支持系统应用主窗口调用。传入目标主窗口的id，调用窗口和目标窗口需满足：同应用进程、显示在同一物理屏、层级低于锁屏、非置顶主窗、非模态主窗且无模应用子窗。  
- 应用主窗口或者它的子窗口如果是焦点窗口，此主窗口调用该接口降低层级后则自动失焦，由当前层级最高的应用窗口获焦。  
- 应用主窗口调用该接口调整层级后超过当前焦点窗口，则被抬升主窗口及其子窗口中，层级最高的窗口自动获焦；应用主窗口调用该接口调整层级后未超过当前焦点窗口，则焦点不做转移。

**起始版本：** 20

**系统能力：** SystemCapability.Window.SessionManager

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| windowId | number | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [1300002](../errorcode-window.md#1300002-窗口状态异常) |
| [1300003](../errorcode-window.md#1300003-系统服务工作异常) |
| [1300004](../errorcode-window.md#1300004-无权限操作) |
| [1300016](../errorcode-window.md#1300016-参数校验错误) |

## raiseToAppTop

```TypeScript
raiseToAppTop(callback: AsyncCallback<void>): void
```

提升应用子窗口到应用顶层。使用callback异步回调。使用该接口需要先创建子窗口，并确保该子窗口调用[showWindow()](arkts-arkui-window-window-i.md#showwindow) 并执行完毕。

**起始版本：** 10

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [1300002](../errorcode-window.md#1300002-窗口状态异常) |
| [1300003](../errorcode-window.md#1300003-系统服务工作异常) |
| [1300004](../errorcode-window.md#1300004-无权限操作) |
| [1300009](../errorcode-window.md#1300009-父窗口无效) |

## requestFocus

```TypeScript
requestFocus(isFocused: boolean): Promise<void>
```

支持当前窗口主动请求获焦/失焦，使用Promise异步回调。调用成功即返回，该接口返回值不代表最终获焦/失焦生效结果。可使用 on('windowEvent') 监听窗口获焦/失焦状态。获焦请求发送后，窗口获焦结果受到窗口可获焦属性及窗口可见状态的限制。获焦成功的窗口需满足以下约束：1.窗口支持获焦；2.窗口可见（窗口已显示，未销毁且未退至后台）。失焦请求发送后，窗口无条件失焦。

**起始版本：** 13

**系统能力：** SystemCapability.Window.SessionManager

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| isFocused | boolean | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [1300002](../errorcode-window.md#1300002-窗口状态异常) |
| [1300003](../errorcode-window.md#1300003-系统服务工作异常) |

## rotate

```TypeScript
rotate(rotateOptions: RotateOptions): void
```

设置窗口旋转参数。仅支持在[自定义系统窗口的显示与隐藏动画](../../../windowmanager/system-window-stage-sys.md#自定义系统窗口的显示与隐藏动画)中使用。

**起始版本：** 9

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| rotateOptions | [RotateOptions](../arkts-components/arkts-arkui-rotateoptions-i.md) | 是 |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [1300002](../errorcode-window.md#1300002-窗口状态异常) |
| [1300004](../errorcode-window.md#1300004-无权限操作) |

## scale

```TypeScript
scale(scaleOptions: ScaleOptions): void
```

设置窗口缩放参数。仅支持在[自定义系统窗口的显示与隐藏动画](../../../windowmanager/system-window-stage-sys.md#自定义系统窗口的显示与隐藏动画)中使用。

**起始版本：** 9

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| scaleOptions | [ScaleOptions](../arkts-components/arkts-arkui-scaleoptions-i.md) | 是 |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [1300002](../errorcode-window.md#1300002-窗口状态异常) |
| [1300004](../errorcode-window.md#1300004-无权限操作) |

## setBackdropBlur

```TypeScript
setBackdropBlur(radius: number): void
```

设置窗口背景模糊。窗口背景是指窗口覆盖的下层区域，与窗口大小相同。需要通过[setWindowBackgroundColor](arkts-arkui-window-window-i.md#setwindowbackgroundcolor)将窗口内容背景设置成透明，否则无法看到模糊效果。

**起始版本：** 9

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| radius | number | 是 |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [1300002](../errorcode-window.md#1300002-窗口状态异常) |
| [1300004](../errorcode-window.md#1300004-无权限操作) |

## setBackdropBlurStyle

```TypeScript
setBackdropBlurStyle(blurStyle: BlurStyle): void
```

设置窗口背景模糊类型。

**起始版本：** 9

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [blurStyle](../arkts-components/arkts-arkui-sheetoptions-i.md) | [BlurStyle](../arkts-components/arkts-arkui-blurstyle-e.md) | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [1300002](../errorcode-window.md#1300002-窗口状态异常) |
| [1300004](../errorcode-window.md#1300004-无权限操作) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

## setBlur

```TypeScript
setBlur(radius: number): void
```

设置窗口模糊。

**起始版本：** 9

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| radius | number | 是 |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [1300002](../errorcode-window.md#1300002-窗口状态异常) |
| [1300004](../errorcode-window.md#1300004-无权限操作) |

## setCornerRadius

```TypeScript
setCornerRadius(cornerRadius: number): void
```

设置窗口圆角半径。

**起始版本：** 9

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| cornerRadius | number | 是 |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [1300002](../errorcode-window.md#1300002-窗口状态异常) |
| [1300004](../errorcode-window.md#1300004-无权限操作) |

## setDefaultDensityEnabled

```TypeScript
setDefaultDensityEnabled(enabled: boolean): void
```

设置窗口是否使用所在屏幕的系统默认Density。Stage模型下，该接口需要在 [loadContent()](arkts-arkui-window-window-i.md#loadcontent) 或[setUIContent()](arkts-arkui-window-window-i.md#setuicontent)调用生效 后使用。不调用此接口进行设置，则表示不使用系统默认Density。当存在同时使用该接口、 [setDefaultDensityEnabled(true)](../../../reference/apis-arkui/arkts-apis-window-WindowStage.md#setdefaultdensityenabled12) 和[setCustomDensity](../../../reference/apis-arkui/arkts-apis-window-WindowStage.md#setcustomdensity)时，以最后调用的设置 效果为准。

**起始版本：** 20

**系统能力：** SystemCapability.Window.SessionManager

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| enabled | boolean | 是 |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [1300002](../errorcode-window.md#1300002-窗口状态异常) |

## setForbidSplitMove

```TypeScript
setForbidSplitMove(isForbidSplitMove: boolean, callback: AsyncCallback<void>): void
```

设置主窗口在分屏模式下是否被禁止移动，使用callback异步回调。

**起始版本：** 9

**废弃版本：** 26.0.0

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| isForbidSplitMove | boolean | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [1300002](../errorcode-window.md#1300002-窗口状态异常) |
| [1300003](../errorcode-window.md#1300003-系统服务工作异常) |

## setForbidSplitMove

```TypeScript
setForbidSplitMove(isForbidSplitMove: boolean): Promise<void>
```

设置主窗口在分屏模式下是否被禁止移动，使用Promise异步回调。

**起始版本：** 9

**废弃版本：** 26.0.0

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| isForbidSplitMove | boolean | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [1300002](../errorcode-window.md#1300002-窗口状态异常) |
| [1300003](../errorcode-window.md#1300003-系统服务工作异常) |

## setHandwritingFlag

```TypeScript
setHandwritingFlag(enable: boolean): Promise<void>
```

为当前窗口添加或移除手写标志，添加该标志后窗口只响应手写笔事件，不响应触屏事件。使用Promise异步回调。

**起始版本：** 12

**系统能力：** SystemCapability.Window.SessionManager

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| enable | boolean | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [1300002](../errorcode-window.md#1300002-窗口状态异常) |
| [1300003](../errorcode-window.md#1300003-系统服务工作异常) |

## setMainWindowRaiseByClickEnabled

```TypeScript
setMainWindowRaiseByClickEnabled(enable: boolean): Promise<void>
```

禁止/使能主窗口点击抬升功能。使用Promise异步回调。点击主窗口时，默认会抬升主窗口及其子窗口。调用此接口禁止主窗口点击抬升后（即传入false），点击主窗口时不会将其及子窗口进行抬升，保持原有状态不变；点击子窗口时，主窗口会连同子窗口一起被抬升。

**起始版本：** 23

**系统能力：** SystemCapability.Window.SessionManager

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| enable | boolean | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [1300002](../errorcode-window.md#1300002-窗口状态异常) |
| [1300003](../errorcode-window.md#1300003-系统服务工作异常) |
| [1300004](../errorcode-window.md#1300004-无权限操作) |

## setRaiseByClickEnabled

```TypeScript
setRaiseByClickEnabled(enable: boolean, callback: AsyncCallback<void>): void
```

禁止/使能子窗口点击抬升功能。使用callback异步回调。通常来说，点击一个子窗口，会将该子窗口显示到最上方，如果设置为false，那么点击子窗口的时候，不会将该子窗口显示到最上方，而是保持不变。使用该接口需要先创建子窗口，并确保该子窗口调用[showWindow()](arkts-arkui-window-window-i.md#showwindow) 并执行完毕。

**起始版本：** 10

**系统能力：** SystemCapability.Window.SessionManager

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| enable | boolean | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [1300002](../errorcode-window.md#1300002-窗口状态异常) |
| [1300003](../errorcode-window.md#1300003-系统服务工作异常) |
| [1300004](../errorcode-window.md#1300004-无权限操作) |
| [1300009](../errorcode-window.md#1300009-父窗口无效) |

## setRotationLocked

```TypeScript
setRotationLocked(locked: boolean): Promise<void>
```

仅支持[系统窗口](../../../windowmanager/window-terminology.md#系统窗口)设置旋转锁定，锁定后系统窗口显示方向不变，未锁定时系统窗口显示方向受主窗口显示方向、旋转锁定按钮、 sensor旋转影响。非系统窗口调用返回1300029错误码。使用Promise异步回调。

> **说明：**&gt;
> - 如果在锁定期间主窗口通过
> [setPreferredOrientation()](arkts-arkui-window-window-i.md#setpreferredorientation)
> 设置显示方向属性，则解除旋转锁定后该窗口在前台还原最后一次的方向请求。&gt;
> - 如果在锁定期间系统窗口通过
> [setPreferredOrientation()](arkts-arkui-window-window-i.md#setpreferredorientation)
> 设置显示方向属性，则解除旋转锁定后该窗口在前台且层级最高时还原最后一次的方向请求。低层级窗口通过setRotationLocked设置旋转锁定不会影响高层级系统窗口调用
> [setPreferredOrientation()](arkts-arkui-window-window-i.md#setpreferredorientation)
> 设置显示方向。&gt;
> - 如果在锁定期间sensor方向发生了变化，则解除旋转锁定后还原到最后一次的sensor方向。&gt;
> - 如果在锁定期间应用调用
> [setOrientation()](arkts-arkui-screen-screen-i-sys.md#setorientation)
> 设置屏幕方向，忽略该次屏幕方向设置。&gt;
> - 解除锁定时，根据主窗口的显示方向属性
> [setPreferredOrientation()](arkts-arkui-window-window-i.md#setpreferredorientation)
> 、sensor方向等决定应用显示方向，具体见[窗口旋转简介](../../../windowmanager/window-rotation.md#窗口旋转简介)。&gt;
> - 不影响应用[module.json5配置文件中的abilities标签](../../../quick-start/module-configuration-file.md#abilities标签)
> orientation属性设置的启动方向。

**起始版本：** 22

**系统能力：** SystemCapability.Window.SessionManager

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| locked | boolean | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [1300002](../errorcode-window.md#1300002-窗口状态异常) |
| [1300003](../errorcode-window.md#1300003-系统服务工作异常) |
| 1300029 |

## setShadow

```TypeScript
setShadow(radius: number, color?: string, offsetX?: number, offsetY?: number): void
```

设置窗口边缘阴影。

**起始版本：** 9

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| radius | number | 是 |
| color | string | 否 |
| offsetX | number | 否 |
| offsetY | number | 否 |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [1300002](../errorcode-window.md#1300002-窗口状态异常) |
| [1300004](../errorcode-window.md#1300004-无权限操作) |

## setSingleFrameComposerEnabled

```TypeScript
setSingleFrameComposerEnabled(enable: boolean): Promise<void>
```

禁止/使能单帧合成渲染节点的功能。使用Promise异步回调。单帧合成渲染节点的功能主要用于跟手性要求较高的场景，使能该功能之后可以降低渲染节点的上屏延时。通过setSingleFrameComposerEnabled接口，如果enable设置为true，则使能单帧合成渲染节点的功能，否 则禁止单帧合成渲染节点的功能。

**起始版本：** 11

**系统能力：** SystemCapability.Window.SessionManager

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| enable | boolean | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [1300002](../errorcode-window.md#1300002-窗口状态异常) |

## setSnapshotSkip

```TypeScript
setSnapshotSkip(isSkip: boolean): void
```

截屏、录屏或投屏是否忽略当前窗口。此接口一般用于禁止截屏、录屏或投屏的场景。若要实现窗口始终在前台忽略截屏、录屏或投屏，在窗口从后台回到前台时，需要通过 on('windowEvent') 监听窗口生命周期变化，在后台状态时设置为false，而在前台状态时设置为true。

**起始版本：** 9

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| isSkip | boolean | 是 |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [1300002](../errorcode-window.md#1300002-窗口状态异常) |

## setTitleButtonVisible

```TypeScript
setTitleButtonVisible(isMaximizeVisible: boolean, isMinimizeVisible: boolean, isSplitVisible: boolean): void
```

设置主窗标题栏上的最大化、最小化、分屏按钮是否可见。仅对在当前场景下可见的标题栏按钮（最大化、最小化、分屏）生效。

**起始版本：** 12

**系统能力：** SystemCapability.Window.SessionManager

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| isMaximizeVisible | boolean | 是 |
| isMinimizeVisible | boolean | 是 |
| isSplitVisible | boolean | 是 |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [1300002](../errorcode-window.md#1300002-窗口状态异常) |
| [1300004](../errorcode-window.md#1300004-无权限操作) |

## setTopmost

```TypeScript
setTopmost(isTopmost: boolean): Promise<void>
```

系统应用主窗口调用，实现将窗口置于所有应用窗口之上不被遮挡，使用Promise异步回调。

**起始版本：** 12

**系统能力：** SystemCapability.Window.SessionManager

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [isTopmost](arkts-arkui-window-subwindowoptions-i-sys.md) | boolean | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [1300002](../errorcode-window.md#1300002-窗口状态异常) |
| [1300003](../errorcode-window.md#1300003-系统服务工作异常) |
| [1300004](../errorcode-window.md#1300004-无权限操作) |

## setWakeUpScreen

```TypeScript
setWakeUpScreen(wakeUp: boolean): void
```

唤醒屏幕。

**起始版本：** 9

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| wakeUp | boolean | 是 |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [1300002](../errorcode-window.md#1300002-窗口状态异常) |
| [1300003](../errorcode-window.md#1300003-系统服务工作异常) |

## setWaterMarkFlag

```TypeScript
setWaterMarkFlag(enable: boolean, callback: AsyncCallback<void>): void
```

为当前窗口添加或删除安全水印标志，使用callback异步回调。

**起始版本：** 10

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| enable | boolean | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [1300002](../errorcode-window.md#1300002-窗口状态异常) |
| [1300003](../errorcode-window.md#1300003-系统服务工作异常) |
| [1300008](../errorcode-window.md#1300008-显示设备异常) |

## setWaterMarkFlag

```TypeScript
setWaterMarkFlag(enable: boolean): Promise<void>
```

为当前窗口添加或删除安全水印标志，使用Promise异步回调。

**起始版本：** 10

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| enable | boolean | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [1300002](../errorcode-window.md#1300002-窗口状态异常) |
| [1300003](../errorcode-window.md#1300003-系统服务工作异常) |
| [1300008](../errorcode-window.md#1300008-显示设备异常) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

## setWindowMode

```TypeScript
setWindowMode(mode: WindowMode): Promise<void>
```

设置主窗口模式，使用Promise异步回调。

**起始版本：** 9

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| mode | [WindowMode](../../apis-test-kit/arkts-apis/arkts-test-uitest-windowmode-e.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [1300002](../errorcode-window.md#1300002-窗口状态异常) |
| [1300003](../errorcode-window.md#1300003-系统服务工作异常) |

## setWindowMode

```TypeScript
setWindowMode(mode: WindowMode, callback: AsyncCallback<void>): void
```

设置主窗口模式，使用callback异步回调。

**起始版本：** 9

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| mode | [WindowMode](../../apis-test-kit/arkts-apis/arkts-test-uitest-windowmode-e.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [1300002](../errorcode-window.md#1300002-窗口状态异常) |
| [1300003](../errorcode-window.md#1300003-系统服务工作异常) |

## setWindowType

```TypeScript
setWindowType(type: WindowType): Promise<void>
```

设置窗口类型，使用Promise异步回调。

**起始版本：** 7

**废弃版本：** 9

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | [WindowType](../../apis-accessibility-kit/arkts-apis/arkts-accessibility-windowtype-t.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

## setWindowType

```TypeScript
setWindowType(type: WindowType, callback: AsyncCallback<void>): void
```

设置窗口类型，使用callback异步回调。

**起始版本：** 7

**废弃版本：** 9

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | [WindowType](../../apis-accessibility-kit/arkts-apis/arkts-accessibility-windowtype-t.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

## showWithAnimation

```TypeScript
showWithAnimation(callback: AsyncCallback<void>): void
```

显示当前窗口，过程中播放动画，使用callback异步回调，仅支持系统窗口。

**起始版本：** 9

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [1300002](../errorcode-window.md#1300002-窗口状态异常) |
| [1300003](../errorcode-window.md#1300003-系统服务工作异常) |
| [1300004](../errorcode-window.md#1300004-无权限操作) |

## showWithAnimation

```TypeScript
showWithAnimation(): Promise<void>
```

显示当前窗口，过程中播放动画，使用Promise异步回调，仅支持系统窗口。

**起始版本：** 9

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**系统接口：** 此接口为系统接口。

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [1300002](../errorcode-window.md#1300002-窗口状态异常) |
| [1300003](../errorcode-window.md#1300003-系统服务工作异常) |
| [1300004](../errorcode-window.md#1300004-无权限操作) |

## translate

```TypeScript
translate(translateOptions: TranslateOptions): void
```

设置窗口平移参数。仅支持在[自定义系统窗口的显示与隐藏动画](../../../windowmanager/system-window-stage-sys.md#自定义系统窗口的显示与隐藏动画)中使用。

**起始版本：** 9

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| translateOptions | [TranslateOptions](../arkts-components/arkts-arkui-translateoptions-i.md) | 是 |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [1300002](../errorcode-window.md#1300002-窗口状态异常) |
| [1300004](../errorcode-window.md#1300004-无权限操作) |
