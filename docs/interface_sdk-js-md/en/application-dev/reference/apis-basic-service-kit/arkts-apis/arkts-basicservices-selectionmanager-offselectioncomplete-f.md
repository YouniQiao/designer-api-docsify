# offSelectionComplete

## Modules to Import

```TypeScript
import { selectionManager } from 'kits/@kit.BasicServicesKit';
```

## offSelectionComplete

```TypeScript
function offSelectionComplete(callback?: Callback<SelectionInfo>): void
```

取消订阅划词完成事件，与[onSelectionComplete](selectionManager.onSelectionComplete(callback: Callback&lt;SelectionInfo&gt;))搭配使用。

**Since:** 24

**ArkTS mode:** ArkTS-Sta only, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-selectionManager-function offSelectionComplete(callback?: Callback<SelectionInfo>): void--><!--Device-selectionManager-function offSelectionComplete(callback?: Callback<SelectionInfo>): void-End-->

**System capability:** SystemCapability.SelectionInput.Selection

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](arkts-basicservices-base-callback-i.md)&lt;SelectionInfo&gt; | No | 需要取消的回调函数（即之前通过onSelectionComplete方法订阅时的回调实例）。参数不填写时，取消订阅对应的所有回调事件。 |

