# Equivalent

```TypeScript
export type Equivalent<T> = (oldV: T, newV: T) => boolean
```

Determine whether two values are equal.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export type Equivalent<T> = (oldV: T, newV: T) => boolean--><!--Device-unnamed-export type Equivalent<T> = (oldV: T, newV: T) => boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| oldV | T | Yes | the old value  |
| newV | T | Yes | the new value  |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | - Returns the comparison result between old value and new value, if they are equal, return true; otherwise, return false.  |

