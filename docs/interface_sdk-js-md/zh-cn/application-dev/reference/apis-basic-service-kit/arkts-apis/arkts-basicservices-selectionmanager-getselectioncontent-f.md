# getSelectionContent

## 导入模块

```TypeScript
import { selectionManager } from 'kits/@kit.BasicServicesKit';
```

## getSelectionContent

```TypeScript
function getSelectionContent(): Promise<string>
```

获取选中文本的内容。使用Promise异步回调。需在  
[on('selectionCompleted')](selectionManager.on(type: 'selectionCompleted', callback: Callback&lt;SelectionInfo&gt;))回调中调用，且仅在划词完成事件触发后有效。

**起始版本：** 24

**ArkTS模式：** ArkTS-Dyn起始版本为22；ArkTS-Sta起始版本为24。

<!--Device-selectionManager-function getSelectionContent(): Promise<string>--><!--Device-selectionManager-function getSelectionContent(): Promise<string>-End-->

**系统能力：** SystemCapability.SelectionInput.Selection

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;string&gt; | Promise对象，返回当前选中文本的内容。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 33600001 | Selection service exception. |
| 33600004 | The interface is called too frequently. |
| 33600005 | The interface is called at the wrong time. |
| 33600006 | The current application is prohibited from accessing content. |
| 33600007 | The length of selected content is out of range. |
| 33600008 | Getting the selected content times out. |

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

