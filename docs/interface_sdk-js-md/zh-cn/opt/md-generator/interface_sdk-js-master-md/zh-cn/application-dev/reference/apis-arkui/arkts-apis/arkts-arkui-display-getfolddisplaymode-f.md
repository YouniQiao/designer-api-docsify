# getFoldDisplayMode

## getFoldDisplayMode

```TypeScript
function getFoldDisplayMode(): FoldDisplayMode
```

获取可折叠设备当前的显示模式。

**起始版本：** 10

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-display-function getFoldDisplayMode(): FoldDisplayMode--><!--Device-display-function getFoldDisplayMode(): FoldDisplayMode-End-->

**系统能力：** SystemCapability.Window.SessionManager

**返回值：**

| 类型 |
| --- |
| [FoldDisplayMode](arkts-arkui-display-folddisplaymode-e.md) |

**错误码：**

| 错误码ID |
| --- |
| [1400003](../errorcode-display.md#1400003-系统服务工作异常) |

## 示例

```TypeScript
let data: display.FoldDisplayMode = display.getFoldDisplayMode();
console.info(`Succeeded in obtaining fold display mode. Data: ${data}`);
```
