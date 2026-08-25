# createWindow

## 导入模块

```TypeScript
import { window } from 'kits/@kit.ArkUI';
```

## createWindow

```TypeScript
function createWindow(config: Configuration, callback: AsyncCallback<Window>): void
```

创建子窗口或者系统窗口，使用callback异步回调。非[自由窗口](../../../windowmanager/window-terminology.md#自由窗口)状态下，子窗口创建后默认是 [沉浸式布局](../../../windowmanager/window-terminology.md#沉浸式布局)。自由窗口状态下，子窗口参数[decorEnabled](arkts-arkui-window-configuration-i.md)为false时，子窗口创建后为沉浸式布局；子窗口参数decorEnabled为true，子窗口 创建后为非沉浸式布局。

**起始版本：** 9

**需要权限：** 
- API版本12+：ohos.permission.SYSTEM_FLOAT_WINDOW

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| config | [Configuration](arkts-arkui-window-configuration-i.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[Window](arkts-arkui-window-window-i.md)&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [1300001](../errorcode-window.md#1300001-重复操作) |
| [1300002](../errorcode-window.md#1300002-窗口状态异常) |
| [1300004](../errorcode-window.md#1300004-无权限操作) |
| [1300006](../errorcode-window.md#1300006-窗口上下文异常) |
| [1300008](../errorcode-window.md#1300008-显示设备异常) |
| [1300009](../errorcode-window.md#1300009-父窗口无效) |


## createWindow

```TypeScript
function createWindow(config: Configuration): Promise<Window>
```

创建子窗口或者系统窗口，使用Promise异步回调。非[自由窗口](../../../windowmanager/window-terminology.md#自由窗口)状态下，子窗口创建后默认是 [沉浸式布局](../../../windowmanager/window-terminology.md#沉浸式布局)。自由窗口状态下，子窗口参数[decorEnabled](arkts-arkui-window-configuration-i.md)为false时，子窗口创建后为沉浸式布局；子窗口参数decorEnabled为true，子窗口 创建后为非沉浸式布局。

**起始版本：** 9

**需要权限：** 
- API版本12+：ohos.permission.SYSTEM_FLOAT_WINDOW

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| config | [Configuration](arkts-arkui-window-configuration-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;[Window](arkts-arkui-window-window-i.md)&gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [1300001](../errorcode-window.md#1300001-重复操作) |
| [1300002](../errorcode-window.md#1300002-窗口状态异常) |
| [1300004](../errorcode-window.md#1300004-无权限操作) |
| [1300006](../errorcode-window.md#1300006-窗口上下文异常) |
| [1300008](../errorcode-window.md#1300008-显示设备异常) |
| [1300009](../errorcode-window.md#1300009-父窗口无效) |
