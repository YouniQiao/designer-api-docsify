# ArrayLike

Represents an object that has a length property and can be indexed.

**Inheritance/Implementation:** ArrayLike extends Iterable<T>

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta since version 26.0.0.

<!--Device-unnamed-export interface ArrayLike--><!--Device-unnamed-export interface ArrayLike-End-->

**System capability:** SystemCapability.Utils.Lang

## Modules to Import

```TypeScript
```

## $_get

```TypeScript
$_get(index: int): T
```

Gets the element at the specified index.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ArrayLike-$_get(index: int): T--><!--Device-ArrayLike-$_get(index: int): T-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| index | int | Yes | The zero-based index of the element to get. <br>The value should be an integer. |

**Return value:**

| Type | Description |
| --- | --- |
| T | The element at the specified index. |

