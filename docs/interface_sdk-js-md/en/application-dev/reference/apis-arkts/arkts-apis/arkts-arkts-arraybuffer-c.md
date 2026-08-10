# ArrayBuffer

JS ArrayBuffer API-compatible class.Used to represent a generic, fixed-length raw binary data buffer.

**Since:** 24

**ArkTS mode:** ArkTS-Sta only, since version 24.

<!--Device-unnamed-export class ArrayBuffer--><!--Device-unnamed-export class ArrayBuffer-End-->

**System capability:** SystemCapability.Utils.Lang

## at

```TypeScript
public at(pos: int): byte
```

Returns the byte at the specified index.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ArrayBuffer-public at(pos: int): byte--><!--Device-ArrayBuffer-public at(pos: int): byte-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| pos | int | Yes | The position in the buffer. &lt;br&gt;The value should be an integer. |

**Return value:**

| Type | Description |
| --- | --- |
| byte | The byte value. |

## atomicAddI16

```TypeScript
public atomicAddI16(index: int, byteOffset: int, value: short): long
```

Atomically adds a value to the element at the specified index.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ArrayBuffer-public atomicAddI16(index: int, byteOffset: int, value: short): long--><!--Device-ArrayBuffer-public atomicAddI16(index: int, byteOffset: int, value: short): long-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| index | int | Yes | The index to access. &lt;br&gt;The value must be an integer greater than or equal to 0. |
| byteOffset | int | Yes | The byte offset within the ArrayBuffer (unit: byte). &lt;br&gt;The value must be an integer greater than or equal to 0. |
| value | short | Yes | The value to add. |

**Return value:**

| Type | Description |
| --- | --- |
| long | The value after the operation. |

## atomicAddI32

```TypeScript
public atomicAddI32(index: int, byteOffset: int, value: int): long
```

Atomically adds a value to the element at the specified index.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ArrayBuffer-public atomicAddI32(index: int, byteOffset: int, value: int): long--><!--Device-ArrayBuffer-public atomicAddI32(index: int, byteOffset: int, value: int): long-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| index | int | Yes | The index to access. &lt;br&gt;The value must be an integer greater than or equal to 0. |
| byteOffset | int | Yes | The byte offset within the ArrayBuffer (unit: byte). &lt;br&gt;The value must be an integer greater than or equal to 0. |
| value | int | Yes | The value to add. &lt;br&gt;The value should be an integer. |

**Return value:**

| Type | Description |
| --- | --- |
| long | The value after the operation. |

## atomicAddI64

```TypeScript
public atomicAddI64(index: int, byteOffset: int, value: long): long
```

Atomically adds a value to the element at the specified index.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ArrayBuffer-public atomicAddI64(index: int, byteOffset: int, value: long): long--><!--Device-ArrayBuffer-public atomicAddI64(index: int, byteOffset: int, value: long): long-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| index | int | Yes | The index to access. &lt;br&gt;The value must be an integer greater than or equal to 0. |
| byteOffset | int | Yes | The byte offset within the ArrayBuffer (unit: byte). &lt;br&gt;The value must be an integer greater than or equal to 0. |
| value | long | Yes | The value to add. |

**Return value:**

| Type | Description |
| --- | --- |
| long | The value after the operation. |

## atomicAddI8

```TypeScript
public atomicAddI8(index: int, byteOffset: int, value: byte): long
```

Atomically adds a value to the element at the specified index.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ArrayBuffer-public atomicAddI8(index: int, byteOffset: int, value: byte): long--><!--Device-ArrayBuffer-public atomicAddI8(index: int, byteOffset: int, value: byte): long-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| index | int | Yes | The index to access. &lt;br&gt;The value must be an integer greater than or equal to 0. |
| byteOffset | int | Yes | The byte offset within the ArrayBuffer (unit: byte). &lt;br&gt;The value must be an integer greater than or equal to 0. |
| value | byte | Yes | The value to add. |

**Return value:**

| Type | Description |
| --- | --- |
| long | The value after the operation. |

## atomicAddU16

```TypeScript
public atomicAddU16(index: int, byteOffset: int, value: short): long
```

Atomically adds a value to the element at the specified index.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ArrayBuffer-public atomicAddU16(index: int, byteOffset: int, value: short): long--><!--Device-ArrayBuffer-public atomicAddU16(index: int, byteOffset: int, value: short): long-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| index | int | Yes | The index to access. &lt;br&gt;The value must be an integer greater than or equal to 0. |
| byteOffset | int | Yes | The byte offset within the ArrayBuffer (unit: byte). &lt;br&gt;The value must be an integer greater than or equal to 0. |
| value | short | Yes | The value to add. |

**Return value:**

| Type | Description |
| --- | --- |
| long | The value after the operation. |

## atomicAddU32

```TypeScript
public atomicAddU32(index: int, byteOffset: int, value: int): long
```

Atomically adds a value to the element at the specified index.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ArrayBuffer-public atomicAddU32(index: int, byteOffset: int, value: int): long--><!--Device-ArrayBuffer-public atomicAddU32(index: int, byteOffset: int, value: int): long-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| index | int | Yes | The index to access. &lt;br&gt;The value must be an integer greater than or equal to 0. |
| byteOffset | int | Yes | The byte offset within the ArrayBuffer (unit: byte). &lt;br&gt;The value must be an integer greater than or equal to 0. |
| value | int | Yes | The value to add. &lt;br&gt;The value should be an integer. |

**Return value:**

| Type | Description |
| --- | --- |
| long | The value after the operation. |

## atomicAddU64

```TypeScript
public atomicAddU64(index: int, byteOffset: int, value: long): long
```

Atomically adds a value to the element at the specified index.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ArrayBuffer-public atomicAddU64(index: int, byteOffset: int, value: long): long--><!--Device-ArrayBuffer-public atomicAddU64(index: int, byteOffset: int, value: long): long-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| index | int | Yes | The index to access. &lt;br&gt;The value must be an integer greater than or equal to 0. |
| byteOffset | int | Yes | The byte offset within the ArrayBuffer (unit: byte). &lt;br&gt;The value must be an integer greater than or equal to 0. |
| value | long | Yes | The value to add. |

**Return value:**

| Type | Description |
| --- | --- |
| long | The value after the operation. |

## atomicAddU8

```TypeScript
public atomicAddU8(index: int, byteOffset: int, value: byte): long
```

Atomically adds a value to the element at the specified index.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ArrayBuffer-public atomicAddU8(index: int, byteOffset: int, value: byte): long--><!--Device-ArrayBuffer-public atomicAddU8(index: int, byteOffset: int, value: byte): long-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| index | int | Yes | The index to access. &lt;br&gt;The value must be an integer greater than or equal to 0. |
| byteOffset | int | Yes | The byte offset within the ArrayBuffer (unit: byte). &lt;br&gt;The value must be an integer greater than or equal to 0. |
| value | byte | Yes | The value to add. |

**Return value:**

| Type | Description |
| --- | --- |
| long | The value after the operation. |

## atomicAndI16

```TypeScript
public atomicAndI16(index: int, byteOffset: int, value: short): long
```

Atomically performs a bitwise AND operation on the element at the specified index.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ArrayBuffer-public atomicAndI16(index: int, byteOffset: int, value: short): long--><!--Device-ArrayBuffer-public atomicAndI16(index: int, byteOffset: int, value: short): long-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| index | int | Yes | The index to access. &lt;br&gt;The value must be an integer greater than or equal to 0. |
| byteOffset | int | Yes | The byte offset within the ArrayBuffer (unit: byte). &lt;br&gt;The value must be an integer greater than or equal to 0. |
| value | short | Yes | The value to AND with. |

**Return value:**

| Type | Description |
| --- | --- |
| long | The value after the operation. |

## atomicAndI32

```TypeScript
public atomicAndI32(index: int, byteOffset: int, value: int): long
```

Atomically performs a bitwise AND operation on the element at the specified index.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ArrayBuffer-public atomicAndI32(index: int, byteOffset: int, value: int): long--><!--Device-ArrayBuffer-public atomicAndI32(index: int, byteOffset: int, value: int): long-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| index | int | Yes | The index to access. &lt;br&gt;The value must be an integer greater than or equal to 0. |
| byteOffset | int | Yes | The byte offset within the ArrayBuffer (unit: byte). &lt;br&gt;The value must be an integer greater than or equal to 0. |
| value | int | Yes | The value to AND with. &lt;br&gt;The value should be an integer. |

**Return value:**

| Type | Description |
| --- | --- |
| long | The value after the operation. |

## atomicAndI64

```TypeScript
public atomicAndI64(index: int, byteOffset: int, value: long): long
```

Atomically performs a bitwise AND operation on the element at the specified index.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ArrayBuffer-public atomicAndI64(index: int, byteOffset: int, value: long): long--><!--Device-ArrayBuffer-public atomicAndI64(index: int, byteOffset: int, value: long): long-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| index | int | Yes | The index to access. &lt;br&gt;The value must be an integer greater than or equal to 0. |
| byteOffset | int | Yes | The byte offset within the ArrayBuffer (unit: byte). &lt;br&gt;The value must be an integer greater than or equal to 0. |
| value | long | Yes | The value to AND with. |

**Return value:**

| Type | Description |
| --- | --- |
| long | The value after the operation. |

## atomicAndI8

```TypeScript
public atomicAndI8(index: int, byteOffset: int, value: byte): long
```

Atomically performs a bitwise AND operation on the element at the specified index.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ArrayBuffer-public atomicAndI8(index: int, byteOffset: int, value: byte): long--><!--Device-ArrayBuffer-public atomicAndI8(index: int, byteOffset: int, value: byte): long-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| index | int | Yes | The index to access. &lt;br&gt;The value must be an integer greater than or equal to 0. |
| byteOffset | int | Yes | The byte offset within the ArrayBuffer (unit: byte). &lt;br&gt;The value must be an integer greater than or equal to 0. |
| value | byte | Yes | The value to AND with. |

**Return value:**

| Type | Description |
| --- | --- |
| long | The value after the operation. |

## atomicAndU16

```TypeScript
public atomicAndU16(index: int, byteOffset: int, value: short): long
```

Atomically performs a bitwise AND operation on the element at the specified index.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ArrayBuffer-public atomicAndU16(index: int, byteOffset: int, value: short): long--><!--Device-ArrayBuffer-public atomicAndU16(index: int, byteOffset: int, value: short): long-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| index | int | Yes | The index to access. &lt;br&gt;The value must be an integer greater than or equal to 0. |
| byteOffset | int | Yes | The byte offset within the ArrayBuffer (unit: byte). &lt;br&gt;The value must be an integer greater than or equal to 0. |
| value | short | Yes | The value to AND with. |

**Return value:**

| Type | Description |
| --- | --- |
| long | The value after the operation. |

## atomicAndU32

```TypeScript
public atomicAndU32(index: int, byteOffset: int, value: int): long
```

Atomically performs a bitwise AND operation on the element at the specified index.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ArrayBuffer-public atomicAndU32(index: int, byteOffset: int, value: int): long--><!--Device-ArrayBuffer-public atomicAndU32(index: int, byteOffset: int, value: int): long-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| index | int | Yes | The index to access. &lt;br&gt;The value must be an integer greater than or equal to 0. |
| byteOffset | int | Yes | The byte offset within the ArrayBuffer (unit: byte). &lt;br&gt;The value must be an integer greater than or equal to 0. |
| value | int | Yes | The value to AND with. &lt;br&gt;The value should be an integer. |

**Return value:**

| Type | Description |
| --- | --- |
| long | The value after the operation. |

## atomicAndU64

```TypeScript
public atomicAndU64(index: int, byteOffset: int, value: long): long
```

Atomically performs a bitwise AND operation on the element at the specified index.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ArrayBuffer-public atomicAndU64(index: int, byteOffset: int, value: long): long--><!--Device-ArrayBuffer-public atomicAndU64(index: int, byteOffset: int, value: long): long-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| index | int | Yes | The index to access. &lt;br&gt;The value must be an integer greater than or equal to 0. |
| byteOffset | int | Yes | The byte offset within the ArrayBuffer (unit: byte). &lt;br&gt;The value must be an integer greater than or equal to 0. |
| value | long | Yes | The value to AND with. |

**Return value:**

| Type | Description |
| --- | --- |
| long | The value after the operation. |

## atomicAndU8

```TypeScript
public atomicAndU8(index: int, byteOffset: int, value: byte): long
```

Atomically performs a bitwise AND operation on the element at the specified index.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ArrayBuffer-public atomicAndU8(index: int, byteOffset: int, value: byte): long--><!--Device-ArrayBuffer-public atomicAndU8(index: int, byteOffset: int, value: byte): long-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| index | int | Yes | The index to access. &lt;br&gt;The value must be an integer greater than or equal to 0. |
| byteOffset | int | Yes | The byte offset within the ArrayBuffer (unit: byte). &lt;br&gt;The value must be an integer greater than or equal to 0. |
| value | byte | Yes | The value to AND with. |

**Return value:**

| Type | Description |
| --- | --- |
| long | The value after the operation. |

## atomicCompareExchangeI16

```TypeScript
public atomicCompareExchangeI16(index: int, byteOffset: int, expectedValue: short, replacementValue: short): long
```

Atomically compares and exchanges the value at the specified index.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ArrayBuffer-public atomicCompareExchangeI16(index: int, byteOffset: int, expectedValue: short, replacementValue: short): long--><!--Device-ArrayBuffer-public atomicCompareExchangeI16(index: int, byteOffset: int, expectedValue: short, replacementValue: short): long-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| index | int | Yes | The index to access. &lt;br&gt;The value must be an integer greater than or equal to 0. |
| byteOffset | int | Yes | The byte offset within the ArrayBuffer (unit: byte). &lt;br&gt;The value must be an integer greater than or equal to 0. |
| expectedValue | short | Yes | The expected value. |
| replacementValue | short | Yes | The replacement value. |

**Return value:**

| Type | Description |
| --- | --- |
| long | The value after the operation. |

## atomicCompareExchangeI32

```TypeScript
public atomicCompareExchangeI32(index: int, byteOffset: int, expectedValue: int, replacementValue: int): long
```

Atomically compares and exchanges the value at the specified index.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ArrayBuffer-public atomicCompareExchangeI32(index: int, byteOffset: int, expectedValue: int, replacementValue: int): long--><!--Device-ArrayBuffer-public atomicCompareExchangeI32(index: int, byteOffset: int, expectedValue: int, replacementValue: int): long-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| index | int | Yes | The index to access. &lt;br&gt;The value must be an integer greater than or equal to 0. |
| byteOffset | int | Yes | The byte offset within the ArrayBuffer (unit: byte). &lt;br&gt;The value must be an integer greater than or equal to 0. |
| expectedValue | int | Yes | The expected value. &lt;br&gt;The value should be an integer. |
| replacementValue | int | Yes | The replacement value. &lt;br&gt;The value should be an integer. |

**Return value:**

| Type | Description |
| --- | --- |
| long | The value after the operation. |

## atomicCompareExchangeI64

```TypeScript
public atomicCompareExchangeI64(index: int, byteOffset: int, expectedValue: long, replacementValue: long): long
```

Atomically compares and exchanges the value at the specified index.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ArrayBuffer-public atomicCompareExchangeI64(index: int, byteOffset: int, expectedValue: long, replacementValue: long): long--><!--Device-ArrayBuffer-public atomicCompareExchangeI64(index: int, byteOffset: int, expectedValue: long, replacementValue: long): long-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| index | int | Yes | The index to access. &lt;br&gt;The value must be an integer greater than or equal to 0. |
| byteOffset | int | Yes | The byte offset within the ArrayBuffer (unit: byte). &lt;br&gt;The value must be an integer greater than or equal to 0. |
| expectedValue | long | Yes | The expected value. |
| replacementValue | long | Yes | The replacement value. |

**Return value:**

| Type | Description |
| --- | --- |
| long | The value after the operation. |

## atomicCompareExchangeI8

```TypeScript
public atomicCompareExchangeI8(index: int, byteOffset: int, expectedValue: byte, replacementValue: byte): long
```

Atomically compares and exchanges the value at the specified index.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ArrayBuffer-public atomicCompareExchangeI8(index: int, byteOffset: int, expectedValue: byte, replacementValue: byte): long--><!--Device-ArrayBuffer-public atomicCompareExchangeI8(index: int, byteOffset: int, expectedValue: byte, replacementValue: byte): long-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| index | int | Yes | The index to access. &lt;br&gt;The value must be an integer greater than or equal to 0. |
| byteOffset | int | Yes | The byte offset within the ArrayBuffer (unit: byte). &lt;br&gt;The value must be an integer greater than or equal to 0. |
| expectedValue | byte | Yes | The expected value. |
| replacementValue | byte | Yes | The replacement value. |

**Return value:**

| Type | Description |
| --- | --- |
| long | The value after the operation. |

## atomicCompareExchangeU16

```TypeScript
public atomicCompareExchangeU16(index: int, byteOffset: int, expectedValue: short, replacementValue: short): long
```

Atomically compares and exchanges the value at the specified index.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ArrayBuffer-public atomicCompareExchangeU16(index: int, byteOffset: int, expectedValue: short, replacementValue: short): long--><!--Device-ArrayBuffer-public atomicCompareExchangeU16(index: int, byteOffset: int, expectedValue: short, replacementValue: short): long-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| index | int | Yes | The index to access. &lt;br&gt;The value must be an integer greater than or equal to 0. |
| byteOffset | int | Yes | The byte offset within the ArrayBuffer (unit: byte). &lt;br&gt;The value must be an integer greater than or equal to 0. |
| expectedValue | short | Yes | The expected value. |
| replacementValue | short | Yes | The replacement value. |

**Return value:**

| Type | Description |
| --- | --- |
| long | The value after the operation. |

## atomicCompareExchangeU32

```TypeScript
public atomicCompareExchangeU32(index: int, byteOffset: int, expectedValue: int, replacementValue: int): long
```

Atomically compares and exchanges the value at the specified index.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ArrayBuffer-public atomicCompareExchangeU32(index: int, byteOffset: int, expectedValue: int, replacementValue: int): long--><!--Device-ArrayBuffer-public atomicCompareExchangeU32(index: int, byteOffset: int, expectedValue: int, replacementValue: int): long-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| index | int | Yes | The index to access. &lt;br&gt;The value must be an integer greater than or equal to 0. |
| byteOffset | int | Yes | The byte offset within the ArrayBuffer (unit: byte). &lt;br&gt;The value must be an integer greater than or equal to 0. |
| expectedValue | int | Yes | The expected value. &lt;br&gt;The value should be an integer. |
| replacementValue | int | Yes | The replacement value. &lt;br&gt;The value should be an integer. |

**Return value:**

| Type | Description |
| --- | --- |
| long | The value after the operation. |

## atomicCompareExchangeU64

```TypeScript
public atomicCompareExchangeU64(index: int, byteOffset: int, expectedValue: long, replacementValue: long): long
```

Atomically compares and exchanges the value at the specified index.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ArrayBuffer-public atomicCompareExchangeU64(index: int, byteOffset: int, expectedValue: long, replacementValue: long): long--><!--Device-ArrayBuffer-public atomicCompareExchangeU64(index: int, byteOffset: int, expectedValue: long, replacementValue: long): long-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| index | int | Yes | The index to access. &lt;br&gt;The value must be an integer greater than or equal to 0. |
| byteOffset | int | Yes | The byte offset within the ArrayBuffer (unit: byte). &lt;br&gt;The value must be an integer greater than or equal to 0. |
| expectedValue | long | Yes | The expected value. |
| replacementValue | long | Yes | The replacement value. |

**Return value:**

| Type | Description |
| --- | --- |
| long | The value after the operation. |

## atomicCompareExchangeU8

```TypeScript
public atomicCompareExchangeU8(index: int, byteOffset: int, expectedValue: byte, replacementValue: byte): long
```

Atomically compares and exchanges the value at the specified index.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ArrayBuffer-public atomicCompareExchangeU8(index: int, byteOffset: int, expectedValue: byte, replacementValue: byte): long--><!--Device-ArrayBuffer-public atomicCompareExchangeU8(index: int, byteOffset: int, expectedValue: byte, replacementValue: byte): long-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| index | int | Yes | The index to access. &lt;br&gt;The value must be an integer greater than or equal to 0. |
| byteOffset | int | Yes | The byte offset within the ArrayBuffer (unit: byte). &lt;br&gt;The value must be an integer greater than or equal to 0. |
| expectedValue | byte | Yes | The expected value. |
| replacementValue | byte | Yes | The replacement value. |

**Return value:**

| Type | Description |
| --- | --- |
| long | The value after the operation. |

## atomicExchangeI16

```TypeScript
public atomicExchangeI16(index: int, byteOffset: int, value: short): long
```

Atomically exchanges the value at the specified index.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ArrayBuffer-public atomicExchangeI16(index: int, byteOffset: int, value: short): long--><!--Device-ArrayBuffer-public atomicExchangeI16(index: int, byteOffset: int, value: short): long-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| index | int | Yes | The index to access. &lt;br&gt;The value must be an integer greater than or equal to 0. |
| byteOffset | int | Yes | The byte offset within the ArrayBuffer (unit: byte). &lt;br&gt;The value must be an integer greater than or equal to 0. |
| value | short | Yes | The value to exchange. |

**Return value:**

| Type | Description |
| --- | --- |
| long | The value after the operation. |

## atomicExchangeI32

```TypeScript
public atomicExchangeI32(index: int, byteOffset: int, value: int): long
```

Atomically exchanges the value at the specified index.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ArrayBuffer-public atomicExchangeI32(index: int, byteOffset: int, value: int): long--><!--Device-ArrayBuffer-public atomicExchangeI32(index: int, byteOffset: int, value: int): long-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| index | int | Yes | The index to access. &lt;br&gt;The value must be an integer greater than or equal to 0. |
| byteOffset | int | Yes | The byte offset within the ArrayBuffer (unit: byte). &lt;br&gt;The value must be an integer greater than or equal to 0. |
| value | int | Yes | The value to exchange. &lt;br&gt;The value should be an integer. |

**Return value:**

| Type | Description |
| --- | --- |
| long | The value after the operation. |

## atomicExchangeI64

```TypeScript
public atomicExchangeI64(index: int, byteOffset: int, value: long): long
```

Atomically exchanges the value at the specified index.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ArrayBuffer-public atomicExchangeI64(index: int, byteOffset: int, value: long): long--><!--Device-ArrayBuffer-public atomicExchangeI64(index: int, byteOffset: int, value: long): long-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| index | int | Yes | The index to access. &lt;br&gt;The value must be an integer greater than or equal to 0. |
| byteOffset | int | Yes | The byte offset within the ArrayBuffer (unit: byte). &lt;br&gt;The value must be an integer greater than or equal to 0. |
| value | long | Yes | The value to exchange. |

**Return value:**

| Type | Description |
| --- | --- |
| long | The value after the operation. |

## atomicExchangeI8

```TypeScript
public atomicExchangeI8(index: int, byteOffset: int, value: byte): long
```

Atomically exchanges the value at the specified index.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ArrayBuffer-public atomicExchangeI8(index: int, byteOffset: int, value: byte): long--><!--Device-ArrayBuffer-public atomicExchangeI8(index: int, byteOffset: int, value: byte): long-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| index | int | Yes | The index to access. &lt;br&gt;The value must be an integer greater than or equal to 0. |
| byteOffset | int | Yes | The byte offset within the ArrayBuffer (unit: byte). &lt;br&gt;The value must be an integer greater than or equal to 0. |
| value | byte | Yes | The value to exchange. |

**Return value:**

| Type | Description |
| --- | --- |
| long | The value after the operation. |

## atomicExchangeU16

```TypeScript
public atomicExchangeU16(index: int, byteOffset: int, value: short): long
```

Atomically exchanges the value at the specified index.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ArrayBuffer-public atomicExchangeU16(index: int, byteOffset: int, value: short): long--><!--Device-ArrayBuffer-public atomicExchangeU16(index: int, byteOffset: int, value: short): long-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| index | int | Yes | The index to access. &lt;br&gt;The value must be an integer greater than or equal to 0. |
| byteOffset | int | Yes | The byte offset within the ArrayBuffer (unit: byte). &lt;br&gt;The value must be an integer greater than or equal to 0. |
| value | short | Yes | The value to exchange. |

**Return value:**

| Type | Description |
| --- | --- |
| long | The value after the operation. |

## atomicExchangeU32

```TypeScript
public atomicExchangeU32(index: int, byteOffset: int, value: int): long
```

Atomically exchanges the value at the specified index.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ArrayBuffer-public atomicExchangeU32(index: int, byteOffset: int, value: int): long--><!--Device-ArrayBuffer-public atomicExchangeU32(index: int, byteOffset: int, value: int): long-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| index | int | Yes | The index to access. &lt;br&gt;The value must be an integer greater than or equal to 0. |
| byteOffset | int | Yes | The byte offset within the ArrayBuffer (unit: byte). &lt;br&gt;The value must be an integer greater than or equal to 0. |
| value | int | Yes | The value to exchange. &lt;br&gt;The value should be an integer. |

**Return value:**

| Type | Description |
| --- | --- |
| long | The value after the operation. |

## atomicExchangeU64

```TypeScript
public atomicExchangeU64(index: int, byteOffset: int, value: long): long
```

Atomically exchanges the value at the specified index.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ArrayBuffer-public atomicExchangeU64(index: int, byteOffset: int, value: long): long--><!--Device-ArrayBuffer-public atomicExchangeU64(index: int, byteOffset: int, value: long): long-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| index | int | Yes | The index to access. &lt;br&gt;The value must be an integer greater than or equal to 0. |
| byteOffset | int | Yes | The byte offset within the ArrayBuffer (unit: byte). &lt;br&gt;The value must be an integer greater than or equal to 0. |
| value | long | Yes | The value to exchange. |

**Return value:**

| Type | Description |
| --- | --- |
| long | The value after the operation. |

## atomicExchangeU8

```TypeScript
public atomicExchangeU8(index: int, byteOffset: int, value: byte): long
```

Atomically exchanges the value at the specified index.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ArrayBuffer-public atomicExchangeU8(index: int, byteOffset: int, value: byte): long--><!--Device-ArrayBuffer-public atomicExchangeU8(index: int, byteOffset: int, value: byte): long-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| index | int | Yes | The index to access. &lt;br&gt;The value must be an integer greater than or equal to 0. |
| byteOffset | int | Yes | The byte offset within the ArrayBuffer (unit: byte). &lt;br&gt;The value must be an integer greater than or equal to 0. |
| value | byte | Yes | The value to exchange. |

**Return value:**

| Type | Description |
| --- | --- |
| long | The value after the operation. |

## atomicLoadI16

```TypeScript
public atomicLoadI16(index: int, byteOffset: int): long
```

Atomically loads the value at the specified index.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ArrayBuffer-public atomicLoadI16(index: int, byteOffset: int): long--><!--Device-ArrayBuffer-public atomicLoadI16(index: int, byteOffset: int): long-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| index | int | Yes | The index to access. &lt;br&gt;The value must be an integer greater than or equal to 0. |
| byteOffset | int | Yes | The byte offset within the ArrayBuffer (unit: byte). &lt;br&gt;The value must be an integer greater than or equal to 0. |

**Return value:**

| Type | Description |
| --- | --- |
| long | The value after the operation. |

## atomicLoadI32

```TypeScript
public atomicLoadI32(index: int, byteOffset: int): long
```

Atomically loads the value at the specified index.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ArrayBuffer-public atomicLoadI32(index: int, byteOffset: int): long--><!--Device-ArrayBuffer-public atomicLoadI32(index: int, byteOffset: int): long-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| index | int | Yes | The index to access. &lt;br&gt;The value must be an integer greater than or equal to 0. |
| byteOffset | int | Yes | The byte offset within the ArrayBuffer (unit: byte). &lt;br&gt;The value must be an integer greater than or equal to 0. |

**Return value:**

| Type | Description |
| --- | --- |
| long | The value after the operation. |

## atomicLoadI64

```TypeScript
public atomicLoadI64(index: int, byteOffset: int): long
```

Atomically loads the value at the specified index.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ArrayBuffer-public atomicLoadI64(index: int, byteOffset: int): long--><!--Device-ArrayBuffer-public atomicLoadI64(index: int, byteOffset: int): long-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| index | int | Yes | The index to access. &lt;br&gt;The value must be an integer greater than or equal to 0. |
| byteOffset | int | Yes | The byte offset within the ArrayBuffer (unit: byte). &lt;br&gt;The value must be an integer greater than or equal to 0. |

**Return value:**

| Type | Description |
| --- | --- |
| long | The value after the operation. |

## atomicLoadI8

```TypeScript
public atomicLoadI8(index: int, byteOffset: int): long
```

Atomically loads the value at the specified index.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ArrayBuffer-public atomicLoadI8(index: int, byteOffset: int): long--><!--Device-ArrayBuffer-public atomicLoadI8(index: int, byteOffset: int): long-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| index | int | Yes | The index to access. &lt;br&gt;The value must be an integer greater than or equal to 0. |
| byteOffset | int | Yes | The byte offset within the ArrayBuffer (unit: byte). &lt;br&gt;The value must be an integer greater than or equal to 0. |

**Return value:**

| Type | Description |
| --- | --- |
| long | The value after the operation. |

## atomicLoadU16

```TypeScript
public atomicLoadU16(index: int, byteOffset: int): long
```

Atomically loads the value at the specified index.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ArrayBuffer-public atomicLoadU16(index: int, byteOffset: int): long--><!--Device-ArrayBuffer-public atomicLoadU16(index: int, byteOffset: int): long-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| index | int | Yes | The index to access. &lt;br&gt;The value must be an integer greater than or equal to 0. |
| byteOffset | int | Yes | The byte offset within the ArrayBuffer (unit: byte). &lt;br&gt;The value must be an integer greater than or equal to 0. |

**Return value:**

| Type | Description |
| --- | --- |
| long | The value after the operation. |

## atomicLoadU32

```TypeScript
public atomicLoadU32(index: int, byteOffset: int): long
```

Atomically loads the value at the specified index.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ArrayBuffer-public atomicLoadU32(index: int, byteOffset: int): long--><!--Device-ArrayBuffer-public atomicLoadU32(index: int, byteOffset: int): long-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| index | int | Yes | The index to access. &lt;br&gt;The value must be an integer greater than or equal to 0. |
| byteOffset | int | Yes | The byte offset within the ArrayBuffer (unit: byte). &lt;br&gt;The value must be an integer greater than or equal to 0. |

**Return value:**

| Type | Description |
| --- | --- |
| long | The value after the operation. |

## atomicLoadU64

```TypeScript
public atomicLoadU64(index: int, byteOffset: int): long
```

Atomically loads the value at the specified index.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ArrayBuffer-public atomicLoadU64(index: int, byteOffset: int): long--><!--Device-ArrayBuffer-public atomicLoadU64(index: int, byteOffset: int): long-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| index | int | Yes | The index to access. &lt;br&gt;The value must be an integer greater than or equal to 0. |
| byteOffset | int | Yes | The byte offset within the ArrayBuffer (unit: byte). &lt;br&gt;The value must be an integer greater than or equal to 0. |

**Return value:**

| Type | Description |
| --- | --- |
| long | The value after the operation. |

## atomicLoadU8

```TypeScript
public atomicLoadU8(index: int, byteOffset: int): long
```

Atomically loads the value at the specified index.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ArrayBuffer-public atomicLoadU8(index: int, byteOffset: int): long--><!--Device-ArrayBuffer-public atomicLoadU8(index: int, byteOffset: int): long-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| index | int | Yes | The index to access. &lt;br&gt;The value must be an integer greater than or equal to 0. |
| byteOffset | int | Yes | The byte offset within the ArrayBuffer (unit: byte). &lt;br&gt;The value must be an integer greater than or equal to 0. |

**Return value:**

| Type | Description |
| --- | --- |
| long | The value after the operation. |

## atomicOrI16

```TypeScript
public atomicOrI16(index: int, byteOffset: int, value: short): long
```

Atomically performs a bitwise OR operation on the element at the specified index.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ArrayBuffer-public atomicOrI16(index: int, byteOffset: int, value: short): long--><!--Device-ArrayBuffer-public atomicOrI16(index: int, byteOffset: int, value: short): long-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| index | int | Yes | The index to access. &lt;br&gt;The value must be an integer greater than or equal to 0. |
| byteOffset | int | Yes | The byte offset within the ArrayBuffer (unit: byte). &lt;br&gt;The value must be an integer greater than or equal to 0. |
| value | short | Yes | The value to OR with. |

**Return value:**

| Type | Description |
| --- | --- |
| long | The value after the operation. |

## atomicOrI32

```TypeScript
public atomicOrI32(index: int, byteOffset: int, value: int): long
```

Atomically performs a bitwise OR operation on the element at the specified index.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ArrayBuffer-public atomicOrI32(index: int, byteOffset: int, value: int): long--><!--Device-ArrayBuffer-public atomicOrI32(index: int, byteOffset: int, value: int): long-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| index | int | Yes | The index to access. &lt;br&gt;The value must be an integer greater than or equal to 0. |
| byteOffset | int | Yes | The byte offset within the ArrayBuffer (unit: byte). &lt;br&gt;The value must be an integer greater than or equal to 0. |
| value | int | Yes | The value to OR with. &lt;br&gt;The value should be an integer. |

**Return value:**

| Type | Description |
| --- | --- |
| long | The value after the operation. |

## atomicOrI64

```TypeScript
public atomicOrI64(index: int, byteOffset: int, value: long): long
```

Atomically performs a bitwise OR operation on the element at the specified index.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ArrayBuffer-public atomicOrI64(index: int, byteOffset: int, value: long): long--><!--Device-ArrayBuffer-public atomicOrI64(index: int, byteOffset: int, value: long): long-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| index | int | Yes | The index to access. &lt;br&gt;The value must be an integer greater than or equal to 0. |
| byteOffset | int | Yes | The byte offset within the ArrayBuffer (unit: byte). &lt;br&gt;The value must be an integer greater than or equal to 0. |
| value | long | Yes | The value to OR with. |

**Return value:**

| Type | Description |
| --- | --- |
| long | The value after the operation. |

## atomicOrI8

```TypeScript
public atomicOrI8(index: int, byteOffset: int, value: byte): long
```

Atomically performs a bitwise OR operation on the element at the specified index.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ArrayBuffer-public atomicOrI8(index: int, byteOffset: int, value: byte): long--><!--Device-ArrayBuffer-public atomicOrI8(index: int, byteOffset: int, value: byte): long-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| index | int | Yes | The index to access. &lt;br&gt;The value must be an integer greater than or equal to 0. |
| byteOffset | int | Yes | The byte offset within the ArrayBuffer (unit: byte). &lt;br&gt;The value must be an integer greater than or equal to 0. |
| value | byte | Yes | The value to OR with. |

**Return value:**

| Type | Description |
| --- | --- |
| long | The value after the operation. |

## atomicOrU16

```TypeScript
public atomicOrU16(index: int, byteOffset: int, value: short): long
```

Atomically performs a bitwise OR operation on the element at the specified index.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ArrayBuffer-public atomicOrU16(index: int, byteOffset: int, value: short): long--><!--Device-ArrayBuffer-public atomicOrU16(index: int, byteOffset: int, value: short): long-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| index | int | Yes | The index to access. &lt;br&gt;The value must be an integer greater than or equal to 0. |
| byteOffset | int | Yes | The byte offset within the ArrayBuffer (unit: byte). &lt;br&gt;The value must be an integer greater than or equal to 0. |
| value | short | Yes | The value to OR with. |

**Return value:**

| Type | Description |
| --- | --- |
| long | The value after the operation. |

## atomicOrU32

```TypeScript
public atomicOrU32(index: int, byteOffset: int, value: int): long
```

Atomically performs a bitwise OR operation on the element at the specified index.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ArrayBuffer-public atomicOrU32(index: int, byteOffset: int, value: int): long--><!--Device-ArrayBuffer-public atomicOrU32(index: int, byteOffset: int, value: int): long-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| index | int | Yes | The index to access. &lt;br&gt;The value must be an integer greater than or equal to 0. |
| byteOffset | int | Yes | The byte offset within the ArrayBuffer (unit: byte). &lt;br&gt;The value must be an integer greater than or equal to 0. |
| value | int | Yes | The value to OR with. &lt;br&gt;The value should be an integer. |

**Return value:**

| Type | Description |
| --- | --- |
| long | The value after the operation. |

## atomicOrU64

```TypeScript
public atomicOrU64(index: int, byteOffset: int, value: long): long
```

Atomically performs a bitwise OR operation on the element at the specified index.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ArrayBuffer-public atomicOrU64(index: int, byteOffset: int, value: long): long--><!--Device-ArrayBuffer-public atomicOrU64(index: int, byteOffset: int, value: long): long-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| index | int | Yes | The index to access. &lt;br&gt;The value must be an integer greater than or equal to 0. |
| byteOffset | int | Yes | The byte offset within the ArrayBuffer (unit: byte). &lt;br&gt;The value must be an integer greater than or equal to 0. |
| value | long | Yes | The value to OR with. |

**Return value:**

| Type | Description |
| --- | --- |
| long | The value after the operation. |

## atomicOrU8

```TypeScript
public atomicOrU8(index: int, byteOffset: int, value: byte): long
```

Atomically performs a bitwise OR operation on the element at the specified index.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ArrayBuffer-public atomicOrU8(index: int, byteOffset: int, value: byte): long--><!--Device-ArrayBuffer-public atomicOrU8(index: int, byteOffset: int, value: byte): long-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| index | int | Yes | The index to access. &lt;br&gt;The value must be an integer greater than or equal to 0. |
| byteOffset | int | Yes | The byte offset within the ArrayBuffer (unit: byte). &lt;br&gt;The value must be an integer greater than or equal to 0. |
| value | byte | Yes | The value to OR with. |

**Return value:**

| Type | Description |
| --- | --- |
| long | The value after the operation. |

## atomicStoreI16

```TypeScript
public atomicStoreI16(index: int, byteOffset: int, value: short): long
```

Atomically stores a value at the specified index.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ArrayBuffer-public atomicStoreI16(index: int, byteOffset: int, value: short): long--><!--Device-ArrayBuffer-public atomicStoreI16(index: int, byteOffset: int, value: short): long-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| index | int | Yes | The index to access. &lt;br&gt;The value must be an integer greater than or equal to 0. |
| byteOffset | int | Yes | The byte offset within the ArrayBuffer (unit: byte). &lt;br&gt;The value must be an integer greater than or equal to 0. |
| value | short | Yes | The value to store. |

**Return value:**

| Type | Description |
| --- | --- |
| long | The stored value. |

## atomicStoreI32

```TypeScript
public atomicStoreI32(index: int, byteOffset: int, value: int): long
```

Atomically stores a value at the specified index.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ArrayBuffer-public atomicStoreI32(index: int, byteOffset: int, value: int): long--><!--Device-ArrayBuffer-public atomicStoreI32(index: int, byteOffset: int, value: int): long-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| index | int | Yes | The index to access. &lt;br&gt;The value must be an integer greater than or equal to 0. |
| byteOffset | int | Yes | The byte offset within the ArrayBuffer (unit: byte). &lt;br&gt;The value must be an integer greater than or equal to 0. |
| value | int | Yes | The value to store. &lt;br&gt;The value should be an integer. |

**Return value:**

| Type | Description |
| --- | --- |
| long | The stored value. |

## atomicStoreI64

```TypeScript
public atomicStoreI64(index: int, byteOffset: int, value: long): long
```

Atomically stores a value at the specified index.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ArrayBuffer-public atomicStoreI64(index: int, byteOffset: int, value: long): long--><!--Device-ArrayBuffer-public atomicStoreI64(index: int, byteOffset: int, value: long): long-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| index | int | Yes | The index to access. &lt;br&gt;The value must be an integer greater than or equal to 0. |
| byteOffset | int | Yes | The byte offset within the ArrayBuffer (unit: byte). &lt;br&gt;The value must be an integer greater than or equal to 0. |
| value | long | Yes | The value to store. |

**Return value:**

| Type | Description |
| --- | --- |
| long | The stored value. |

## atomicStoreI8

```TypeScript
public atomicStoreI8(index: int, byteOffset: int, value: byte): long
```

Atomically stores a value at the specified index.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ArrayBuffer-public atomicStoreI8(index: int, byteOffset: int, value: byte): long--><!--Device-ArrayBuffer-public atomicStoreI8(index: int, byteOffset: int, value: byte): long-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| index | int | Yes | The index to access. &lt;br&gt;The value must be an integer greater than or equal to 0. |
| byteOffset | int | Yes | The byte offset within the ArrayBuffer (unit: byte). &lt;br&gt;The value must be an integer greater than or equal to 0. |
| value | byte | Yes | The value to store. |

**Return value:**

| Type | Description |
| --- | --- |
| long | The stored value. |

## atomicStoreU16

```TypeScript
public atomicStoreU16(index: int, byteOffset: int, value: short): long
```

Atomically stores a value at the specified index.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ArrayBuffer-public atomicStoreU16(index: int, byteOffset: int, value: short): long--><!--Device-ArrayBuffer-public atomicStoreU16(index: int, byteOffset: int, value: short): long-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| index | int | Yes | The index to access. &lt;br&gt;The value must be an integer greater than or equal to 0. |
| byteOffset | int | Yes | The byte offset within the ArrayBuffer (unit: byte). &lt;br&gt;The value must be an integer greater than or equal to 0. |
| value | short | Yes | The value to store. |

**Return value:**

| Type | Description |
| --- | --- |
| long | The stored value. |

## atomicStoreU32

```TypeScript
public atomicStoreU32(index: int, byteOffset: int, value: int): long
```

Atomically stores a value at the specified index.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ArrayBuffer-public atomicStoreU32(index: int, byteOffset: int, value: int): long--><!--Device-ArrayBuffer-public atomicStoreU32(index: int, byteOffset: int, value: int): long-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| index | int | Yes | The index to access. &lt;br&gt;The value must be an integer greater than or equal to 0. |
| byteOffset | int | Yes | The byte offset within the ArrayBuffer (unit: byte). &lt;br&gt;The value must be an integer greater than or equal to 0. |
| value | int | Yes | The value to store. &lt;br&gt;The value should be an integer. |

**Return value:**

| Type | Description |
| --- | --- |
| long | The stored value. |

## atomicStoreU64

```TypeScript
public atomicStoreU64(index: int, byteOffset: int, value: long): long
```

Atomically stores a value at the specified index.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ArrayBuffer-public atomicStoreU64(index: int, byteOffset: int, value: long): long--><!--Device-ArrayBuffer-public atomicStoreU64(index: int, byteOffset: int, value: long): long-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| index | int | Yes | The index to access. &lt;br&gt;The value must be an integer greater than or equal to 0. |
| byteOffset | int | Yes | The byte offset within the ArrayBuffer (unit: byte). &lt;br&gt;The value must be an integer greater than or equal to 0. |
| value | long | Yes | The value to store. |

**Return value:**

| Type | Description |
| --- | --- |
| long | The stored value. |

## atomicStoreU8

```TypeScript
public atomicStoreU8(index: int, byteOffset: int, value: byte): long
```

Atomically stores a value at the specified index.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ArrayBuffer-public atomicStoreU8(index: int, byteOffset: int, value: byte): long--><!--Device-ArrayBuffer-public atomicStoreU8(index: int, byteOffset: int, value: byte): long-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| index | int | Yes | The index to access. &lt;br&gt;The value must be an integer greater than or equal to 0. |
| byteOffset | int | Yes | The byte offset within the ArrayBuffer (unit: byte). &lt;br&gt;The value must be an integer greater than or equal to 0. |
| value | byte | Yes | The value to store. |

**Return value:**

| Type | Description |
| --- | --- |
| long | The stored value. |

## atomicSubI16

```TypeScript
public atomicSubI16(index: int, byteOffset: int, value: short): long
```

Atomically subtracts a value from the element at the specified index.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ArrayBuffer-public atomicSubI16(index: int, byteOffset: int, value: short): long--><!--Device-ArrayBuffer-public atomicSubI16(index: int, byteOffset: int, value: short): long-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| index | int | Yes | The index to access. &lt;br&gt;The value must be an integer greater than or equal to 0. |
| byteOffset | int | Yes | The byte offset within the ArrayBuffer (unit: byte). &lt;br&gt;The value must be an integer greater than or equal to 0. |
| value | short | Yes | The value to subtract. |

**Return value:**

| Type | Description |
| --- | --- |
| long | The value after the operation. |

## atomicSubI32

```TypeScript
public atomicSubI32(index: int, byteOffset: int, value: int): long
```

Atomically subtracts a value from the element at the specified index.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ArrayBuffer-public atomicSubI32(index: int, byteOffset: int, value: int): long--><!--Device-ArrayBuffer-public atomicSubI32(index: int, byteOffset: int, value: int): long-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| index | int | Yes | The index to access. &lt;br&gt;The value must be an integer greater than or equal to 0. |
| byteOffset | int | Yes | The byte offset within the ArrayBuffer (unit: byte). &lt;br&gt;The value must be an integer greater than or equal to 0. |
| value | int | Yes | The value to subtract. &lt;br&gt;The value should be an integer. |

**Return value:**

| Type | Description |
| --- | --- |
| long | The value after the operation. |

## atomicSubI64

```TypeScript
public atomicSubI64(index: int, byteOffset: int, value: long): long
```

Atomically subtracts a value from the element at the specified index.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ArrayBuffer-public atomicSubI64(index: int, byteOffset: int, value: long): long--><!--Device-ArrayBuffer-public atomicSubI64(index: int, byteOffset: int, value: long): long-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| index | int | Yes | The index to access. &lt;br&gt;The value must be an integer greater than or equal to 0. |
| byteOffset | int | Yes | The byte offset within the ArrayBuffer (unit: byte). &lt;br&gt;The value must be an integer greater than or equal to 0. |
| value | long | Yes | The value to subtract. |

**Return value:**

| Type | Description |
| --- | --- |
| long | The value after the operation. |

## atomicSubI8

```TypeScript
public atomicSubI8(index: int, byteOffset: int, value: byte): long
```

Atomically subtracts a value from the element at the specified index.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ArrayBuffer-public atomicSubI8(index: int, byteOffset: int, value: byte): long--><!--Device-ArrayBuffer-public atomicSubI8(index: int, byteOffset: int, value: byte): long-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| index | int | Yes | The index to access. &lt;br&gt;The value must be an integer greater than or equal to 0. |
| byteOffset | int | Yes | The byte offset within the ArrayBuffer (unit: byte). &lt;br&gt;The value must be an integer greater than or equal to 0. |
| value | byte | Yes | The value to subtract. |

**Return value:**

| Type | Description |
| --- | --- |
| long | The value after the operation. |

## atomicSubU16

```TypeScript
public atomicSubU16(index: int, byteOffset: int, value: short): long
```

Atomically subtracts a value from the element at the specified index.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ArrayBuffer-public atomicSubU16(index: int, byteOffset: int, value: short): long--><!--Device-ArrayBuffer-public atomicSubU16(index: int, byteOffset: int, value: short): long-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| index | int | Yes | The index to access. &lt;br&gt;The value must be an integer greater than or equal to 0. |
| byteOffset | int | Yes | The byte offset within the ArrayBuffer (unit: byte). &lt;br&gt;The value must be an integer greater than or equal to 0. |
| value | short | Yes | The value to subtract. |

**Return value:**

| Type | Description |
| --- | --- |
| long | The value after the operation. |

## atomicSubU32

```TypeScript
public atomicSubU32(index: int, byteOffset: int, value: int): long
```

Atomically subtracts a value from the element at the specified index.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ArrayBuffer-public atomicSubU32(index: int, byteOffset: int, value: int): long--><!--Device-ArrayBuffer-public atomicSubU32(index: int, byteOffset: int, value: int): long-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| index | int | Yes | The index to access. &lt;br&gt;The value must be an integer greater than or equal to 0. |
| byteOffset | int | Yes | The byte offset within the ArrayBuffer (unit: byte). &lt;br&gt;The value must be an integer greater than or equal to 0. |
| value | int | Yes | The value to subtract. &lt;br&gt;The value should be an integer. |

**Return value:**

| Type | Description |
| --- | --- |
| long | The value after the operation. |

## atomicSubU64

```TypeScript
public atomicSubU64(index: int, byteOffset: int, value: long): long
```

Atomically subtracts a value from the element at the specified index.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ArrayBuffer-public atomicSubU64(index: int, byteOffset: int, value: long): long--><!--Device-ArrayBuffer-public atomicSubU64(index: int, byteOffset: int, value: long): long-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| index | int | Yes | The index to access. &lt;br&gt;The value must be an integer greater than or equal to 0. |
| byteOffset | int | Yes | The byte offset within the ArrayBuffer (unit: byte). &lt;br&gt;The value must be an integer greater than or equal to 0. |
| value | long | Yes | The value to subtract. |

**Return value:**

| Type | Description |
| --- | --- |
| long | The value after the operation. |

## atomicSubU8

```TypeScript
public atomicSubU8(index: int, byteOffset: int, value: byte): long
```

Atomically subtracts a value from the element at the specified index.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ArrayBuffer-public atomicSubU8(index: int, byteOffset: int, value: byte): long--><!--Device-ArrayBuffer-public atomicSubU8(index: int, byteOffset: int, value: byte): long-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| index | int | Yes | The index to access. &lt;br&gt;The value must be an integer greater than or equal to 0. |
| byteOffset | int | Yes | The byte offset within the ArrayBuffer (unit: byte). &lt;br&gt;The value must be an integer greater than or equal to 0. |
| value | byte | Yes | The value to subtract. |

**Return value:**

| Type | Description |
| --- | --- |
| long | The value after the operation. |

## atomicXorI16

```TypeScript
public atomicXorI16(index: int, byteOffset: int, value: short): long
```

Atomically performs a bitwise XOR operation on the element at the specified index.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ArrayBuffer-public atomicXorI16(index: int, byteOffset: int, value: short): long--><!--Device-ArrayBuffer-public atomicXorI16(index: int, byteOffset: int, value: short): long-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| index | int | Yes | The index to access. &lt;br&gt;The value must be an integer greater than or equal to 0. |
| byteOffset | int | Yes | The byte offset within the ArrayBuffer (unit: byte). &lt;br&gt;The value must be an integer greater than or equal to 0. |
| value | short | Yes | The value to XOR with. |

**Return value:**

| Type | Description |
| --- | --- |
| long | The value after the operation. |

## atomicXorI32

```TypeScript
public atomicXorI32(index: int, byteOffset: int, value: int): long
```

Atomically performs a bitwise XOR operation on the element at the specified index.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ArrayBuffer-public atomicXorI32(index: int, byteOffset: int, value: int): long--><!--Device-ArrayBuffer-public atomicXorI32(index: int, byteOffset: int, value: int): long-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| index | int | Yes | The index to access. &lt;br&gt;The value must be an integer greater than or equal to 0. |
| byteOffset | int | Yes | The byte offset within the ArrayBuffer (unit: byte). &lt;br&gt;The value must be an integer greater than or equal to 0. |
| value | int | Yes | The value to XOR with. &lt;br&gt;The value should be an integer. |

**Return value:**

| Type | Description |
| --- | --- |
| long | The value after the operation. |

## atomicXorI64

```TypeScript
public atomicXorI64(index: int, byteOffset: int, value: long): long
```

Atomically performs a bitwise XOR operation on the element at the specified index.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ArrayBuffer-public atomicXorI64(index: int, byteOffset: int, value: long): long--><!--Device-ArrayBuffer-public atomicXorI64(index: int, byteOffset: int, value: long): long-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| index | int | Yes | The index to access. &lt;br&gt;The value must be an integer greater than or equal to 0. |
| byteOffset | int | Yes | The byte offset within the ArrayBuffer (unit: byte). &lt;br&gt;The value must be an integer greater than or equal to 0. |
| value | long | Yes | The value to XOR with. |

**Return value:**

| Type | Description |
| --- | --- |
| long | The value after the operation. |

## atomicXorI8

```TypeScript
public atomicXorI8(index: int, byteOffset: int, value: byte): long
```

Atomically performs a bitwise XOR operation on the element at the specified index.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ArrayBuffer-public atomicXorI8(index: int, byteOffset: int, value: byte): long--><!--Device-ArrayBuffer-public atomicXorI8(index: int, byteOffset: int, value: byte): long-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| index | int | Yes | The index to access. &lt;br&gt;The value must be an integer greater than or equal to 0. |
| byteOffset | int | Yes | The byte offset within the ArrayBuffer (unit: byte). &lt;br&gt;The value must be an integer greater than or equal to 0. |
| value | byte | Yes | The value to XOR with. |

**Return value:**

| Type | Description |
| --- | --- |
| long | The value after the operation. |

## atomicXorU16

```TypeScript
public atomicXorU16(index: int, byteOffset: int, value: short): long
```

Atomically performs a bitwise XOR operation on the element at the specified index.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ArrayBuffer-public atomicXorU16(index: int, byteOffset: int, value: short): long--><!--Device-ArrayBuffer-public atomicXorU16(index: int, byteOffset: int, value: short): long-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| index | int | Yes | The index to access. &lt;br&gt;The value must be an integer greater than or equal to 0. |
| byteOffset | int | Yes | The byte offset within the ArrayBuffer (unit: byte). &lt;br&gt;The value must be an integer greater than or equal to 0. |
| value | short | Yes | The value to XOR with. |

**Return value:**

| Type | Description |
| --- | --- |
| long | The value after the operation. |

## atomicXorU32

```TypeScript
public atomicXorU32(index: int, byteOffset: int, value: int): long
```

Atomically performs a bitwise XOR operation on the element at the specified index.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ArrayBuffer-public atomicXorU32(index: int, byteOffset: int, value: int): long--><!--Device-ArrayBuffer-public atomicXorU32(index: int, byteOffset: int, value: int): long-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| index | int | Yes | The index to access. &lt;br&gt;The value must be an integer greater than or equal to 0. |
| byteOffset | int | Yes | The byte offset within the ArrayBuffer (unit: byte). &lt;br&gt;The value must be an integer greater than or equal to 0. |
| value | int | Yes | The value to XOR with. &lt;br&gt;The value should be an integer. |

**Return value:**

| Type | Description |
| --- | --- |
| long | The value after the operation. |

## atomicXorU64

```TypeScript
public atomicXorU64(index: int, byteOffset: int, value: long): long
```

Atomically performs a bitwise XOR operation on the element at the specified index.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ArrayBuffer-public atomicXorU64(index: int, byteOffset: int, value: long): long--><!--Device-ArrayBuffer-public atomicXorU64(index: int, byteOffset: int, value: long): long-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| index | int | Yes | The index to access. &lt;br&gt;The value must be an integer greater than or equal to 0. |
| byteOffset | int | Yes | The byte offset within the ArrayBuffer (unit: byte). &lt;br&gt;The value must be an integer greater than or equal to 0. |
| value | long | Yes | The value to XOR with. |

**Return value:**

| Type | Description |
| --- | --- |
| long | The value after the operation. |

## atomicXorU8

```TypeScript
public atomicXorU8(index: int, byteOffset: int, value: byte): long
```

Atomically performs a bitwise XOR operation on the element at the specified index.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ArrayBuffer-public atomicXorU8(index: int, byteOffset: int, value: byte): long--><!--Device-ArrayBuffer-public atomicXorU8(index: int, byteOffset: int, value: byte): long-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| index | int | Yes | The index to access. &lt;br&gt;The value must be an integer greater than or equal to 0. |
| byteOffset | int | Yes | The byte offset within the ArrayBuffer (unit: byte). &lt;br&gt;The value must be an integer greater than or equal to 0. |
| value | byte | Yes | The value to XOR with. |

**Return value:**

| Type | Description |
| --- | --- |
| long | The value after the operation. |

## bytesLength

```TypeScript
public static bytesLength(text: string, encoding: string): int
```

Returns the byte length of a string in a given encoding.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ArrayBuffer-public static bytesLength(text: string, encoding: string): int--><!--Device-ArrayBuffer-public static bytesLength(text: string, encoding: string): int-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| text | string | Yes | Source string. |
| encoding | string | Yes | Encoding type. |

**Return value:**

| Type | Description |
| --- | --- |
| int | Calculated byte length. |

## constructor

```TypeScript
constructor(length: int, maxByteLength?: int)
```

Creates an ArrayBuffer with size equal to the length parameter.

**Since:** 24

**ArkTS mode:** ArkTS-Sta only, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ArrayBuffer-constructor(length: int, maxByteLength?: int)--><!--Device-ArrayBuffer-constructor(length: int, maxByteLength?: int)-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| length | int | Yes | The size of the ArrayBuffer in bytes. &lt;br&gt;The value must be an integer greater than or equal to 0. |
| maxByteLength | int | No | Optional maximum size the ArrayBuffer can be resized to. &lt;br&gt;The value must be an integer greater than or equal to 0. |

## constructor

```TypeScript
public constructor(length: double, maxByteLength?: double)
```

Creates an ArrayBuffer with size equal to the length parameter.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ArrayBuffer-public constructor(length: double, maxByteLength?: double)--><!--Device-ArrayBuffer-public constructor(length: double, maxByteLength?: double)-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| length | double | Yes | The size of the ArrayBuffer in bytes. &lt;br&gt;The value must be greater than or equal to 0. |
| maxByteLength | double | No | Optional maximum size the ArrayBuffer can be resized to. &lt;br&gt;The value must be greater than or equal to 0. |

## from

```TypeScript
public static from(arr: FixedArray<byte>): ArrayBuffer
```

Creates a new ArrayBuffer from an array of bytes.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ArrayBuffer-public static from(arr: FixedArray<byte>): ArrayBuffer--><!--Device-ArrayBuffer-public static from(arr: FixedArray<byte>): ArrayBuffer-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| arr | FixedArray&lt;byte&gt; | Yes | Source byte array. |

**Return value:**

| Type | Description |
| --- | --- |
| ArrayBuffer | The new ArrayBuffer. |

## from

```TypeScript
public static from(u8arr: Uint8Array): ArrayBuffer
```

Creates a new ArrayBuffer from a Uint8Array.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ArrayBuffer-public static from(u8arr: Uint8Array): ArrayBuffer--><!--Device-ArrayBuffer-public static from(u8arr: Uint8Array): ArrayBuffer-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| u8arr | Uint8Array | Yes | Source typed array. |

**Return value:**

| Type | Description |
| --- | --- |
| ArrayBuffer | The new ArrayBuffer. |

## from

```TypeScript
public static from(array: double[]): ArrayBuffer
```

Creates a new ArrayBuffer from an array of numbers.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ArrayBuffer-public static from(array: double[]): ArrayBuffer--><!--Device-ArrayBuffer-public static from(array: double[]): ArrayBuffer-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| array | double[] | Yes | Source number array. |

**Return value:**

| Type | Description |
| --- | --- |
| ArrayBuffer | The new ArrayBuffer. |

## from

```TypeScript
public static from(str: string, encoding: string): ArrayBuffer
```

Creates a new ArrayBuffer from a string with specific encoding.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ArrayBuffer-public static from(str: string, encoding: string): ArrayBuffer--><!--Device-ArrayBuffer-public static from(str: string, encoding: string): ArrayBuffer-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| str | string | Yes | Source string. |
| encoding | string | Yes | String encoding (e.g., "utf8"). |

**Return value:**

| Type | Description |
| --- | --- |
| ArrayBuffer | The new ArrayBuffer. |

## from

```TypeScript
public static from(buff: ArrayBuffer, byteOffset: int, length: int): ArrayBuffer
```

Creates a new ArrayBuffer from a segment of an existing ArrayBuffer.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ArrayBuffer-public static from(buff: ArrayBuffer, byteOffset: int, length: int): ArrayBuffer--><!--Device-ArrayBuffer-public static from(buff: ArrayBuffer, byteOffset: int, length: int): ArrayBuffer-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| buff | ArrayBuffer | Yes | Source buffer. |
| byteOffset | int | Yes | Start offset in source. &lt;br&gt;The value should be an integer. |
| length | int | Yes | Number of bytes to copy. &lt;br&gt;The value should be an integer. |

**Return value:**

| Type | Description |
| --- | --- |
| ArrayBuffer | The new ArrayBuffer. |

## from

```TypeScript
public static from(buffer: ArrayBuffer, byteOffset?: double, length?: double): ArrayBuffer
```

Creates a new ArrayBuffer from a segment of an existing ArrayBuffer with number parameters.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ArrayBuffer-public static from(buffer: ArrayBuffer, byteOffset?: double, length?: double): ArrayBuffer--><!--Device-ArrayBuffer-public static from(buffer: ArrayBuffer, byteOffset?: double, length?: double): ArrayBuffer-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| buffer | ArrayBuffer | Yes | Source buffer. |
| byteOffset | double | No | Start offset. |
| length | double | No | Byte length. |

**Return value:**

| Type | Description |
| --- | --- |
| ArrayBuffer | The new ArrayBuffer. |

## fromObject

```TypeScript
public static fromObject(obj: Object, byteOffsetOrEncoding: int | string, length: int): ArrayBuffer
```

Creates a new ArrayBuffer from an object.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ArrayBuffer-public static fromObject(obj: Object, byteOffsetOrEncoding: int | string, length: int): ArrayBuffer--><!--Device-ArrayBuffer-public static fromObject(obj: Object, byteOffsetOrEncoding: int | string, length: int): ArrayBuffer-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| obj | Object | Yes | Source object (string or ArrayBuffer). |
| byteOffsetOrEncoding | int \| string | Yes | Byte offset or encoding string. |
| length | int | Yes | Length to copy. &lt;br&gt;The value should be an integer. |

**Return value:**

| Type | Description |
| --- | --- |
| ArrayBuffer | The new ArrayBuffer. |

## getByteLength

```TypeScript
public getByteLength(): int
```

Returns the length of the ArrayBuffer in bytes.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ArrayBuffer-public getByteLength(): int--><!--Device-ArrayBuffer-public getByteLength(): int-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| int | The byte length. |

## isView

```TypeScript
public static isView(obj: Object): boolean
```

Checks if the passed object is one of the ArrayBuffer views.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ArrayBuffer-public static isView(obj: Object): boolean--><!--Device-ArrayBuffer-public static isView(obj: Object): boolean-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| obj | Object | Yes | The object to check. |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | Returns true if the object is a view; otherwise false. |

## resize

```TypeScript
public resize(newLen : int): void
```

Resizes the ArrayBuffer to the specified length.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ArrayBuffer-public resize(newLen : int): void--><!--Device-ArrayBuffer-public resize(newLen : int): void-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| newLen | int | Yes | The new byte length. &lt;br&gt;The value must be an integer greater than or equal to 0. |

## set

```TypeScript
public set(pos: int, val: byte): void
```

Sets the byte value at the specified index.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ArrayBuffer-public set(pos: int, val: byte): void--><!--Device-ArrayBuffer-public set(pos: int, val: byte): void-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| pos | int | Yes | The position in the buffer. &lt;br&gt;The value should be an integer. |
| val | byte | Yes | The byte value to set. |

## slice

```TypeScript
public slice(begin: int, end?: int): ArrayBuffer
```

Creates a new ArrayBuffer with a copy of bytes in the range [begin, end).

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ArrayBuffer-public slice(begin: int, end?: int): ArrayBuffer--><!--Device-ArrayBuffer-public slice(begin: int, end?: int): ArrayBuffer-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| begin | int | Yes | An inclusive index to start copying from. &lt;br&gt;The value should be an integer. |
| end | int | No | An exclusive index to stop copying. &lt;br&gt;The value should be an integer. |

**Return value:**

| Type | Description |
| --- | --- |
| ArrayBuffer | The new ArrayBuffer. |

## slice

```TypeScript
public slice(begin: double, end?: double): ArrayBuffer
```

Creates a new ArrayBuffer with a copy of bytes in the range [begin, end).

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ArrayBuffer-public slice(begin: double, end?: double): ArrayBuffer--><!--Device-ArrayBuffer-public slice(begin: double, end?: double): ArrayBuffer-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| begin | double | Yes | An inclusive index to start copying from. |
| end | double | No | An exclusive index to stop copying. |

**Return value:**

| Type | Description |
| --- | --- |
| ArrayBuffer | The new ArrayBuffer. |

## stringify

```TypeScript
public static stringify(buffer: ArrayBuffer, encoding: string, start: int, end: int): string
```

Converts a segment of an ArrayBuffer to a string.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ArrayBuffer-public static stringify(buffer: ArrayBuffer, encoding: string, start: int, end: int): string--><!--Device-ArrayBuffer-public static stringify(buffer: ArrayBuffer, encoding: string, start: int, end: int): string-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| buffer | ArrayBuffer | Yes | Source buffer. |
| encoding | string | Yes | Encoding to use. |
| start | int | Yes | Start index. &lt;br&gt;The value should be an integer. |
| end | int | Yes | End index. &lt;br&gt;The value should be an integer. |

**Return value:**

| Type | Description |
| --- | --- |
| string | Decoded string. |

## toString

```TypeScript
public toString(): string
```

Returns the string representation of the ArrayBuffer.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ArrayBuffer-public toString(): string--><!--Device-ArrayBuffer-public toString(): string-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| string | The string representation of the ArrayBuffer. |

## byteLength

```TypeScript
get byteLength(): int
```

Read-only property for the byte length of the ArrayBuffer.

**Type:** int

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ArrayBuffer-get byteLength(): int--><!--Device-ArrayBuffer-get byteLength(): int-End-->

**System capability:** SystemCapability.Utils.Lang

## detached

```TypeScript
get detached(): boolean
```

Returns true if the ArrayBuffer has been detached.

**Type:** boolean

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ArrayBuffer-get detached(): boolean--><!--Device-ArrayBuffer-get detached(): boolean-End-->

**System capability:** SystemCapability.Utils.Lang

## resizable

```TypeScript
get resizable(): boolean
```

Returns true if the ArrayBuffer can be resized.

**Type:** boolean

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ArrayBuffer-get resizable(): boolean--><!--Device-ArrayBuffer-get resizable(): boolean-End-->

**System capability:** SystemCapability.Utils.Lang

