# shiftAppWindowFocus

## 导入模块

```TypeScript
import { window } from 'kits/@kit.ArkUI';
```

## shiftAppWindowFocus

```TypeScript
function shiftAppWindowFocus(sourceWindowId: number, targetWindowId: number): Promise<void>
```

在同应用内将窗口焦点从源窗口转移到目标窗口，仅支持应用主窗、子窗范围内的焦点转移。使用Promise异步回调。目标窗口需确保具有获得焦点的能力（可通过 [setWindowFocusable()](arkts-arkui-window-window-i.md#setwindowfocusable) 设置），并确保调用[showWindow()](arkts-arkui-window-window-i.md#showwindow)成功且执行完毕。

> **说明：**&gt;
> 在调用shiftAppWindowFocus()前，建议确保目标窗口已调用
> [loadContent()](arkts-arkui-window-window-i.md#loadcontent)
> 或[setUIContent()](arkts-arkui-window-window-i.md#setuicontent)并生效，
> 否则可能会导致不可见窗口获取焦点，造成功能异常或影响用户体验。

**起始版本：** 11

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Window.SessionManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| sourceWindowId | number | 是 |
| targetWindowId | number | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [1300002](../errorcode-window.md#1300002-窗口状态异常) |
| [1300003](../errorcode-window.md#1300003-系统服务工作异常) |
| [1300004](../errorcode-window.md#1300004-无权限操作) |
