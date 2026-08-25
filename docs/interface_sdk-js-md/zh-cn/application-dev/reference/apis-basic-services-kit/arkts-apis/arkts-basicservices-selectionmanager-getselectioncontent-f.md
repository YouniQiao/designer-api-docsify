# getSelectionContent

## 导入模块

```TypeScript
import { selectionManager } from 'kits/@kit.BasicServicesKit';
```

## getSelectionContent

```TypeScript
function getSelectionContent(): Promise<string>
```

获取选中文本的内容。使用Promise异步回调。需在 on('selectionCompleted') 回调中调用，且仅在划词完成事件触发后有效。

**起始版本：** 24

**系统能力：** SystemCapability.SelectionInput.Selection

**返回值：**

| 类型 |
| --- |
| Promise & lt;string & gt; |

**错误码：**

| 错误码ID |
| --- |
| [33600001](../errorcode-selection.md#33600001-划词服务调用异常) |
| [33600004](../errorcode-selection.md#33600004-该接口被调用过于频繁) |
| [33600005](../errorcode-selection.md#33600005-接口调用时机错误) |
| [33600006](../errorcode-selection.md#33600006-当前应用禁止获取内容) |
| [33600007](../errorcode-selection.md#33600007-划词内容长度超出范围) |
| [33600008](../errorcode-selection.md#33600008-获取选中内容超时) |
