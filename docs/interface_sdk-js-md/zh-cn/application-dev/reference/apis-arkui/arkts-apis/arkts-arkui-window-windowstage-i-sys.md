# WindowStage

窗口管理器。管理各个基本窗口单元，即[Window](arkts-arkui-window-n.md)实例。下列API示例中都需在[onWindowStageCreate()](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-uiability-uiability-c.md#onwindowstagecreate)函数中使用WindowStage 的实例调用对应方法。

**起始版本：** 9

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

## 导入模块

```TypeScript
import { window } from 'kits/@kit.ArkUI';
```

## disableWindowDecor

```TypeScript
disableWindowDecor(): void
```

禁止窗口装饰。禁止窗口装饰后，当主窗口进入全屏沉浸状态时，此时鼠标Hover到上方窗口标题栏热区上会显示悬浮标题栏。若想禁用悬浮标题栏显示，请使用 [setTitleAndDockHoverShown()](arkts-arkui-window-window-i.md#settitleanddockhovershown)接口。

**起始版本：** 9

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**系统接口：** 此接口为系统接口。

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [1300002](../errorcode-window.md#1300002-窗口状态异常) |
| [1300005](../errorcode-window.md#1300005-windowstage异常) |

## setImageForRecent

```TypeScript
setImageForRecent(imageResource: number | image.PixelMap, value: ImageFit): Promise<void>
```

设置应用在多任务中和Dock栏悬停时显示的图片，使用Promise异步回调。  
> **说明：**&gt;
> 调用该接口前，建议先通过loadContent方法或者setUIContent
> 方法完成页面加载。如果应用窗口未完成页面加载就直接调用该接口，功能将不会生效。此时多任务中只显示应用启动页。

**起始版本：** 22

**需要权限：** 
- API版本26.0.0+：ohos.permission.MANAGE_RECENT_SNAPSHOT

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Window.SessionManager

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| imageResource | number \| image.PixelMap | 是 |
| value | [ImageFit](arkts-arkui-imagefit-e.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [1300002](../errorcode-window.md#1300002-窗口状态异常) |
| [1300003](../errorcode-window.md#1300003-系统服务工作异常) |
| [1300016](../errorcode-window.md#1300016-参数校验错误) |

## setImageForRecent

```TypeScript
setImageForRecent(imgResourceId: number, value: ImageFit): Promise<void>
```

设置应用在多任务中和Dock栏悬停时显示的图片，使用Promise异步回调。  
> **说明：**&gt;
> 调用该接口前，建议先通过loadContent方法或者setUIContent
> 方法完成页面加载。如果应用窗口未完成页面加载就直接调用该接口，功能将不会生效。此时多任务中只显示应用启动页。

**起始版本：** 19

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Window.SessionManager

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| imgResourceId | number | 是 |
| value | [ImageFit](arkts-arkui-imagefit-e.md) | 是 |

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
| [1300016](../errorcode-window.md#1300016-参数校验错误) |

## setShowOnLockScreen

```TypeScript
setShowOnLockScreen(showOnLockScreen: boolean): void
```

设置应用显示在锁屏之上。

**起始版本：** 9

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| showOnLockScreen | boolean | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [1300002](../errorcode-window.md#1300002-窗口状态异常) |
| [1300005](../errorcode-window.md#1300005-windowstage异常) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
