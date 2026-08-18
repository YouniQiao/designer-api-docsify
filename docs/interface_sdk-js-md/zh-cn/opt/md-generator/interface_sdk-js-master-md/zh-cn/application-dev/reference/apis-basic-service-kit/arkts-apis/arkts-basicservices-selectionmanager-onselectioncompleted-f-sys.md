# on_selectionCompleted（系统接口）

## 导入模块

```TypeScript
```

## on_selectionCompleted

```TypeScript
function on(type: 'selectionCompleted', callback: Callback<SelectionInfo>): void
```

订阅划词完成事件，与 [off('selectionCompleted')](arkts-basicservices-selectionmanager-offselectioncompleted-f-sys.md#offselectioncompleted) 搭配使用取消订阅。

**起始版本：** 20

<!--Device-selectionManager-function on(type: 'selectionCompleted', callback: Callback<SelectionInfo>): void--><!--Device-selectionManager-function on(type: 'selectionCompleted', callback: Callback<SelectionInfo>): void-End-->

**系统能力：** SystemCapability.SelectionInput.Selection

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'selectionCompleted' | 是 |
| callback | [Callback](arkts-basicservices-base-callback-i.md)&lt;[SelectionInfo](arkts-basicservices-selectionmanager-selectioninfo-i-sys.md)&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [33600003](../../apis-basic-services-kit/errorcode-selection.md#33600003-调用接口的应用与系统设置中选择的应用不匹配) |

**示例**

```TypeScript
import { selectionManager } from '@kit.BasicServicesKit';

try {
  // 订阅划词完成事件
  selectionManager.on('selectionCompleted', (info: selectionManager.SelectionInfo) => {
    console.info('Enter the callback function.');
  });
} catch (err) {
  console.error(`Failed to register selectionCompleted callback. Error code: ${err.code}, error message: ${err.message}`);
}
```
