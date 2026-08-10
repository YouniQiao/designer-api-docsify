# SelectionChangeCallback

```TypeScript
export type SelectionChangeCallback = (oldBegin: int, oldEnd: int, newBegin: int, newEnd: int) => void
```

文本选择范围变化（selectionChange）事件的回调函数类型，用于定义该事件触发时执行的回调函数格式。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-inputMethodEngine-export type SelectionChangeCallback = (oldBegin: int, oldEnd: int, newBegin: int, newEnd: int) => void--><!--Device-inputMethodEngine-export type SelectionChangeCallback = (oldBegin: int, oldEnd: int, newBegin: int, newEnd: int) => void-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| oldBegin | int | Yes | oldBegin为变化前被选中文本的起始下标。 |
| oldEnd | int | Yes | oldEnd为变化前被选中文本的终止下标。 |
| newBegin | int | Yes | newBegin为变化后被选中文本的起始下标。 |
| newEnd | int | Yes | newEnd为变化后被选中文本的终止下标。 |

