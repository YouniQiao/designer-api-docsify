# Comparable

Can be implemented by any type that supports comparison.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

<!--Device-unnamed-export interface Comparable<in T>--><!--Device-unnamed-export interface Comparable<in T>-End-->

**System capability:** SystemCapability.Utils.Lang

## compareTo

```TypeScript
compareTo(to: T): int
```

Compares this instance to other object, treated as a `T`.The result is less than 0 if this instance lesser than provided object 0 if they are equal and greater than 0 otherwise.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Comparable-compareTo(to: T): int--><!--Device-Comparable-compareTo(to: T): int-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| to | T | Yes | the object to compare. |

**Return value:**

| Type | Description |
| --- | --- |
| int | the comparison result. |

