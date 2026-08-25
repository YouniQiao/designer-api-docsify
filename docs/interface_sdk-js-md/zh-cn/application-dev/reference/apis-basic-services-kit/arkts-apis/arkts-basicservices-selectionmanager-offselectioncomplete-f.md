# offSelectionComplete

## 导入模块

```TypeScript
import { selectionManager } from '@kit.BasicServicesKit';
```

## offSelectionComplete

```TypeScript
function offSelectionComplete(callback?: Callback<SelectionInfo>): void
```

取消订阅划词完成事件，与[onSelectionComplete](arkts-basicservices-selectionmanager-onselectioncomplete-f.md)搭配使 用。

**起始版本：** 24

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.SelectionInput.Selection

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](arkts-basicservices-base-callback-i.md)&lt;[SelectionInfo](arkts-basicservices-selectionmanager-selectioninfo-i.md)&gt; | 否 |

**示例**

```TypeScript
import selectionManager from '@ohos.selectionInput.selectionManager';

// 定义划词完成事件回调函数，用于订阅和取消订阅
let selectionChangeCallback = (info: selectionManager.SelectionInfo) => {
  console.info(`Enter the callback function.`);
};

// 先订阅划词完成事件回调，为后续取消订阅做准备
selectionManager.onSelectionComplete(selectionChangeCallback);
try {
  // 取消订阅划词完成事件
  selectionManager.offSelectionComplete(selectionChangeCallback);
} catch (err) {
  console.error(`Failed to unregister selectionCompleted. Error code: ${err.code}, error message: ${err.message}`);
}
```
