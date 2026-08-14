# Tuple

Marker interface for tuple types.

**Inheritance/Implementation:** Tuple extends Iterable<Any>

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Deprecated since:** -1

<!--Device-unnamed-export interface Tuple--><!--Device-unnamed-export interface Tuple-End-->

**System capability:** SystemCapability.Utils.Lang

## unsafeGet

```TypeScript
unsafeGet(index: int): Any
```

Get the element at the specified index.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-Tuple-unsafeGet(index: int): Any--><!--Device-Tuple-unsafeGet(index: int): Any-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| index | int | Yes | the index of the element to get. <br>The value should be an integer. |

**Return value:**

| Type | Description |
| --- | --- |
| Any | the element at the specified index. |

## length

```TypeScript
readonly length: int
```

The number of elements in this tuple. The value should be an integer.

**Type:** int

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-Tuple-readonly length: int--><!--Device-Tuple-readonly length: int-End-->

**System capability:** SystemCapability.Utils.Lang

