# moveMainWindowToTargetDisplay（系统接口）

## 导入模块

```TypeScript
import { window } from 'kits/@kit.ArkUI';
```

## moveMainWindowToTargetDisplay

```TypeScript
function moveMainWindowToTargetDisplay(displayId: number, windowId: number, userId?: number): Promise<void>
```

将指定的主窗口迁移到指定的屏幕上。使用Promise异步回调。  
- 对于[主屏](../../../displaymanager/display-terminology.md#主屏)/  
[扩展屏](../../../displaymanager/display-terminology.md#扩展屏)与 [虚拟屏](../../../displaymanager/display-terminology.md#虚拟屏)之间以及虚拟屏与虚拟屏之间的窗口迁移，仅主窗及其子窗会一起被迁移到对应屏幕上且被抬升，如果存在子窗，最上层可获焦子 窗会获取焦点，否则主窗口获焦。  
- 对于主屏与扩展屏之间的窗口迁移，只会将主窗口迁移到对应屏幕，抬升并获取焦点。  
<!--RP3--><!--RP3End-->

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Window.SessionManager

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| displayId | number | 是 |
| windowId | number | 是 |
| userId | number | 否 |

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
| [1300008](../errorcode-window.md#1300008-显示设备异常) |
| [1300016](../errorcode-window.md#1300016-参数校验错误) |
