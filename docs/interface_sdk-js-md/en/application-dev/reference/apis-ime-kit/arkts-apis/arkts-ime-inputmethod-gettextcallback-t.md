# GetTextCallback

```TypeScript
export type GetTextCallback = (length: int) => string
```

The callback of 'getLeftTextOfCursor' or 'getRightTextOfCursor' event.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-inputMethod-export type GetTextCallback = (length: int) => string--><!--Device-inputMethod-export type GetTextCallback = (length: int) => string-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| length | int | Yes | the length of text.  |

**Return value:**

| Type | Description |
| --- | --- |
| string | represents the text in edit box.  |

