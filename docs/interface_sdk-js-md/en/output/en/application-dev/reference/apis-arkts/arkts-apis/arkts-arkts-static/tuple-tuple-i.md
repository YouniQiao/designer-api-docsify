# Tuple

Marker interface for tuple types.

**Inheritance/Implementation:** Tuple extends [Iterable<Any>](Iterable<Any>)

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

<!--Device-unnamed-export interface Tuple extends Iterable<Any>--><!--Device-unnamed-export interface Tuple extends Iterable<Any>-End-->

**System capability:** SystemCapability.Utils.Lang

## unsafeGet

```TypeScript
unsafeGet(index: int): Any
```

Get the element at the specified index.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Tuple-unsafeGet(index: int): Any--><!--Device-Tuple-unsafeGet(index: int): Any-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| index | int | Yes | the index of the element to get.\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_HTML\_\_\_ESCAPED\_UNDERSCORE\_\_\_TAG\_\_\_ESCAPED\_UNDERSCORE\_\_\_DESC\_\_\_ESCAPED\_UNDERSCORE\_\_\_USD\_\_\_ESCAPED\_UNDERSCORE\_\_\_0\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_The value should be an integer. |

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

**Model restriction:** This API can be used only in the stage model.

<!--Device-Tuple-readonly length: int--><!--Device-Tuple-readonly length: int-End-->

**System capability:** SystemCapability.Utils.Lang

