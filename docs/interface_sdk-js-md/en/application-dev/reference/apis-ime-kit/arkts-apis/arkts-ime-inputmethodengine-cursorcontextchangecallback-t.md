# CursorContextChangeCallback

```TypeScript
export type CursorContextChangeCallback = (x: double, y: double, height: double) => void
```

光标上下文变化（cursorContextChange）事件的回调函数类型，用于定义该事件触发时执行的回调函数格式。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-inputMethodEngine-export type CursorContextChangeCallback = (x: double, y: double, height: double) => void--><!--Device-inputMethodEngine-export type CursorContextChangeCallback = (x: double, y: double, height: double) => void-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| x | double | Yes | x为光标上端的x坐标值，单位为px |
| y | double | Yes | y为光标上端的y坐标值，单位为px。 |
| height | double | Yes | height为光标的高度值，单位为px。 |

