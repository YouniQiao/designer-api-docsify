# on

## Modules to Import

```TypeScript
import { selectionManager } from 'kits/@kit.BasicServicesKit';
```

## on('selectionCompleted')

```TypeScript
function on(type: 'selectionCompleted', callback: Callback<SelectionInfo>): void
```

订阅划词完成事件，与  
[off('selectionCompleted')](selectionManager.off(type: 'selectionCompleted', callback?: Callback&lt;SelectionInfo&gt;))搭配使用取消订阅。

**Since:** 24

**ArkTS mode:** ArkTS-Dyn only, since version 20.

<!--Device-selectionManager-function on(type: 'selectionCompleted', callback: Callback<SelectionInfo>): void--><!--Device-selectionManager-function on(type: 'selectionCompleted', callback: Callback<SelectionInfo>): void-End-->

**System capability:** SystemCapability.SelectionInput.Selection

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'selectionCompleted' | Yes | 设置监听类型，固定取值为'selectionCompleted'。 |
| callback | [Callback](arkts-basicservices-base-callback-i.md)&lt;SelectionInfo&gt; | Yes | 回调函数，返回划词事件信息[SelectionInfo](arkts-basicservices-selectionmanager-selectioninfo-i.md)。该回 调仅在用户通过鼠标或触控板选中文本（双击/三击/滑动）后按下Ctrl键时触发。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 33600003 | The application calling the API does not match the application selected in the system settings. |

## Examples

```TypeScript
import { selectionManager } from '@kit.BasicServicesKit';

try {
  // Subscribe to the word selection completion event.
  selectionManager.on('selectionCompleted', (info: selectionManager.SelectionInfo) => {
    console.info('Enter the callback function.');
  });
} catch (err) {
  console.error(`Failed to register selectionCompleted callback. Error code: ${err.code}, error message: ${err.message}`);
}
```

