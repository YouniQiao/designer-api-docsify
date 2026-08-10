# getSelectionContent

## Modules to Import

```TypeScript
import { selectionManager } from 'kits/@kit.BasicServicesKit';
```

## getSelectionContent

```TypeScript
function getSelectionContent(): Promise<string>
```

获取选中文本的内容。使用Promise异步回调。需在  
[on('selectionCompleted')](selectionManager.on(type: 'selectionCompleted', callback: Callback&lt;SelectionInfo&gt;))回调中调用，且仅在划词完成事件触发后有效。

**Since:** 24

**ArkTS mode:** ArkTS-Dyn since version 22; ArkTS-Sta since version 24.

<!--Device-selectionManager-function getSelectionContent(): Promise<string>--><!--Device-selectionManager-function getSelectionContent(): Promise<string>-End-->

**System capability:** SystemCapability.SelectionInput.Selection

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;string&gt; | Promise对象，返回当前选中文本的内容。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 33600001 | Selection service exception. |
| 33600004 | The interface is called too frequently. |
| 33600005 | The interface is called at the wrong time. |
| 33600006 | The current application is prohibited from accessing content. |
| 33600007 | The length of selected content is out of range. |
| 33600008 | Getting the selected content times out. |

## Examples

```TypeScript
import { selectionManager } from '@kit.BasicServicesKit';

// Subscribe to the word selection completion event and obtain the selected text in the callback.
selectionManager.on('selectionCompleted', async (info: selectionManager.SelectionInfo) => {
  try {
    // Obtain the content of the selected text.
    let content = await selectionManager.getSelectionContent();
    console.info(`Succeeded in getting selection content: ${content}`);
  } catch (err) {
    console.error(`Failed to get selection content. Error code: ${err.code}, error message: ${err.message}`);
  }
});
```

