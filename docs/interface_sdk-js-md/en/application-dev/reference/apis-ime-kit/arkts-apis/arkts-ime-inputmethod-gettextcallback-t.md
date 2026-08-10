# GetTextCallback

```TypeScript
export type GetTextCallback = (length: int) => string
```

'getLeftTextOfCursor' 或 'getRightTextOfCursor' 事件的回调函数。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-inputMethod-export type GetTextCallback = (length: int) => string--><!--Device-inputMethod-export type GetTextCallback = (length: int) => string-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| length | int | Yes | 文本的长度。 |

**Return value:**

| Type | Description |
| --- | --- |
| string | represents the text in edit box. |

