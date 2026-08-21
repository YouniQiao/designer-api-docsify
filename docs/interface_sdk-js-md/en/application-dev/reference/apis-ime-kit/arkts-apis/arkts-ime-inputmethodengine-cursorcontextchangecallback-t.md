# CursorContextChangeCallback

```TypeScript
export type CursorContextChangeCallback = (x: double, y: double, height: double) => void
```

@brief The callback of 'cursorContextChange' event.

**Since:** 23

<!--Device-inputMethodEngine-export type CursorContextChangeCallback = (x: double, y: double, height: double) => void--><!--Device-inputMethodEngine-export type CursorContextChangeCallback = (x: double, y: double, height: double) => void-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| x | double | Yes | the left point of the cursor, unit is px. |
| y | double | Yes | the top point of the cursor, unit is px. |
| height | double | Yes | the height of the cursor, unit is px. |

