# findWindow

## findWindow

```TypeScript
function findWindow(name: string): Window
```

查找指定名称对应的窗口。

**起始版本：** 23

**废弃版本：** -1

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-window-function findWindow(name: string): Window--><!--Device-window-function findWindow(name: string): Window-End-->

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| name | string | 是 |

**返回值：**

| 类型 |
| --- |
| [Window](arkts-arkui-window-window-i.md) |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [1300002](../errorcode-window.md#1300002-窗口状态异常) |

## 示例

```TypeScript
let windowClass: window.Window | undefined = undefined;
try {
  windowClass = window.findWindow('test');
} catch (exception) {
  console.error(`Failed to find the Window. Cause code: ${exception.code}, message: ${exception.message}`);
}
```
