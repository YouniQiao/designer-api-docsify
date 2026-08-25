# off（系统接口）

## 导入模块

```TypeScript
import { window } from 'kits/@kit.ArkUI';
```

## off('systemBarTintChange')

```TypeScript
function off(type: 'systemBarTintChange', callback?: Callback<SystemBarTintState>): void
```

关闭状态栏、导航栏属性变化的监听。

**起始版本：** 8

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'systemBarTintChange' | 是 |
| callback | [Callback](arkts-arkui-window-callback-i.md)&lt;[SystemBarTintState](arkts-arkui-window-systembartintstate-i-sys.md)&gt; | 否 |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |


## off('gestureNavigationEnabledChange')

```TypeScript
function off(type: 'gestureNavigationEnabledChange', callback?: Callback<boolean>): void
```

移除手势导航启用状态变化的监听。

**起始版本：** 10

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'gestureNavigationEnabledChange' | 是 |
| callback | [Callback](arkts-arkui-window-callback-i.md)&lt;boolean&gt; | 否 |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [1300002](../errorcode-window.md#1300002-窗口状态异常) |
| [1300003](../errorcode-window.md#1300003-系统服务工作异常) |


## off('waterMarkFlagChange')

```TypeScript
function off(type: 'waterMarkFlagChange', callback?: Callback<boolean>): void
```

移除水印启用状态变化的监听。

**起始版本：** 10

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'waterMarkFlagChange' | 是 |
| callback | [Callback](arkts-arkui-window-callback-i.md)&lt;boolean&gt; | 否 |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [1300002](../errorcode-window.md#1300002-窗口状态异常) |
| [1300003](../errorcode-window.md#1300003-系统服务工作异常) |
