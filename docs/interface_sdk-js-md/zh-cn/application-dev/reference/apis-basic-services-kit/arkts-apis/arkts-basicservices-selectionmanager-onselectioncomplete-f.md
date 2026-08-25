# onSelectionComplete

## 导入模块

```TypeScript
import { selectionManager } from '@kit.BasicServicesKit';
```

## onSelectionComplete

```TypeScript
function onSelectionComplete(callback: Callback<SelectionInfo>): void
```

订阅划词完成事件，与[offSelectionComplete](arkts-basicservices-selectionmanager-offselectioncomplete-f.md)搭配 使用取消订阅。

**起始版本：** 24

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.SelectionInput.Selection

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](arkts-basicservices-base-callback-i.md)&lt;[SelectionInfo](arkts-basicservices-selectionmanager-selectioninfo-i.md)&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [33600003](../errorcode-selection.md#33600003-调用接口的应用与系统设置中选择的应用不匹配) |

**示例**

```TypeScript
import selectionManager from '@ohos.selectionInput.selectionManager';

try {
  // 订阅划词完成事件
  selectionManager.onSelectionComplete((info: selectionManager.SelectionInfo) => {
    console.info(`SelectionInfo: ${JSON.stringify(info)}`);
  });
} catch (err) {
  console.error(`Failed to register selectionCompleted callback. Error code: ${err.code}, error message: ${err.message}`);
}
```
