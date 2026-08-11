# getDataSummary（系统接口）

## getDataSummary

```TypeScript
function getDataSummary(): Array<Summary>
```

获取所有拖拽对象的摘要。

**起始版本：** 11

<!--Device-dragInteraction-function getDataSummary(): Array<Summary>--><!--Device-dragInteraction-function getDataSummary(): Array<Summary>-End-->

**系统能力：** SystemCapability.Msdp.DeviceStatus.Drag

**系统接口：** 此接口为系统接口。

**返回值：**

| 类型 |
| --- |
| Array&lt;Summary&gt; |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

## 示例

```TypeScript
let summary: Array<dragInteraction.Summary> = dragInteraction.getDataSummary();
console.info(`Drag interaction summary: ${summary}`);
```
