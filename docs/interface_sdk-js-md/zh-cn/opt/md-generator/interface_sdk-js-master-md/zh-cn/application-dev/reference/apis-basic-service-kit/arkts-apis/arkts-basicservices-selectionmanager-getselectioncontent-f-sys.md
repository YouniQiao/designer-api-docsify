# getSelectionContent（系统接口）

## getSelectionContent

```TypeScript
function getSelectionContent(): Promise<string>
```

获取选中文本的内容。使用Promise异步回调。需在 [on('selectionCompleted')](arkts-basicservices-selectionmanager-onselectioncompleted-f-sys.md#on_selectionCompleted) 回调中调用，且仅在划词完成事件触发后有效。

**起始版本：** 24

**废弃版本：** -1

<!--Device-selectionManager-function getSelectionContent(): Promise<string>--><!--Device-selectionManager-function getSelectionContent(): Promise<string>-End-->

**系统能力：** SystemCapability.SelectionInput.Selection

**系统接口：** 此接口为系统接口。

**返回值：**

| 类型 |
| --- |
| Promise & lt;string & gt; |

**错误码：**

| 错误码ID |
| --- |
| [33600001](../../apis-basic-services-kit/errorcode-selection.md#33600001-划词服务调用异常) |
| [33600004](../../apis-basic-services-kit/errorcode-selection.md#33600004-该接口被调用过于频繁) |
| [33600005](../../apis-basic-services-kit/errorcode-selection.md#33600005-接口调用时机错误) |
| [33600006](../../apis-basic-services-kit/errorcode-selection.md#33600006-当前应用禁止获取内容) |
| [33600007](../../apis-basic-services-kit/errorcode-selection.md#33600007-划词内容长度超出范围) |
| [33600008](../../apis-basic-services-kit/errorcode-selection.md#33600008-获取选中内容超时) |

## 示例

```TypeScript
import { selectionManager } from '@kit.BasicServicesKit';

// 订阅划词完成事件，在回调中获取选中文本
selectionManager.on('selectionCompleted', async (info: selectionManager.SelectionInfo) => {
  try {
    // 获取选中文本内容
    let content = await selectionManager.getSelectionContent();
    console.info(`Succeeded in getting selection content: ${content}`);
  } catch (err) {
    console.error(`Failed to get selection content. Error code: ${err.code}, error message: ${err.message}`);
  }
});
```
