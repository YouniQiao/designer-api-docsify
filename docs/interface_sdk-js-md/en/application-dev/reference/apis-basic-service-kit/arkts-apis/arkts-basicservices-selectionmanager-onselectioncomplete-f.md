# onSelectionComplete

## Modules to Import

```TypeScript
import { selectionManager } from 'kits/@kit.BasicServicesKit';
```

## onSelectionComplete

```TypeScript
function onSelectionComplete(callback: Callback<SelectionInfo>): void
```

订阅划词完成事件，与[offSelectionComplete](selectionManager.offSelectionComplete(callback?: Callback&lt;SelectionInfo&gt;))搭配使用取消订阅。

**Since:** 24

**ArkTS mode:** ArkTS-Sta only, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-selectionManager-function onSelectionComplete(callback: Callback<SelectionInfo>): void--><!--Device-selectionManager-function onSelectionComplete(callback: Callback<SelectionInfo>): void-End-->

**System capability:** SystemCapability.SelectionInput.Selection

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](arkts-basicservices-base-callback-i.md)&lt;SelectionInfo&gt; | Yes | 回调函数，返回划词事件信息[SelectionInfo](arkts-basicservices-selectionmanager-selectioninfo-i.md)。该回 调仅在用户通过鼠标或触控板选中文本（双击/三击/滑动）后按下Ctrl键时触发。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 33600003 | The application calling the API does not match the application selected in the system settings. |

