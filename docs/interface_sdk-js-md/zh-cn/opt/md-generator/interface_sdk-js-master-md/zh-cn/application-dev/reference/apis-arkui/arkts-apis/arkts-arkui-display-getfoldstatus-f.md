# getFoldStatus

## getFoldStatus

```TypeScript
function getFoldStatus(): FoldStatus
```

获取可折叠设备当前的折叠状态。

**起始版本：** 23

**废弃版本：** -1

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-display-function getFoldStatus(): FoldStatus--><!--Device-display-function getFoldStatus(): FoldStatus-End-->

**系统能力：** SystemCapability.Window.SessionManager

**返回值：**

| 类型 |
| --- |
| [FoldStatus](arkts-arkui-foldstatus-e.md) |

**错误码：**

| 错误码ID |
| --- |
| [1400003](../errorcode-display.md#1400003-系统服务工作异常) |

## 示例

```TypeScript
let data: display.FoldStatus = display.getFoldStatus();
console.info(`Succeeded in obtaining fold status. Data: ${data}`);
```
