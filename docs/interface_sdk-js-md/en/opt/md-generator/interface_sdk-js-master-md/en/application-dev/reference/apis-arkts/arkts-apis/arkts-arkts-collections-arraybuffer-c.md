# ArrayBuffer

Underlying data structure of the ArkTS TypedArray ([Int8Array](arkts-collections.md#@arkts.collections), [Uint8Array](arkts-collections.md#@arkts.collections), [Int16Array](arkts-collections.md#@arkts.collections), [Uint16Array](arkts-collections.md#@arkts.collections), [Int32Array](arkts-collections.md#@arkts.collections), [Uint32Array](arkts-collections.md#@arkts.collections), [Uint8ClampedArray](arkts-collections.md#@arkts.collections), and [Float32Array](arkts-collections.md#@arkts.collections)). > **NOTE：**> > - This module can be imported only to ArkTS files (with the file name extension .ets). > **Decorator**: \@Sendable

**Since:** 12

**Deprecated since:** -1

<!--Device-collections-class ArrayBuffer--><!--Device-collections-class ArrayBuffer-End-->

**System capability:** SystemCapability.Utils.Lang

## Modules to Import

```TypeScript
import { collections } from '@kit.ArkTS';
```

## constructor

```TypeScript
constructor(byteLength: number)
```

A constructor used to create an ArkTS ArrayBuffer of a given length.

**Since:** 12

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-ArrayBuffer-constructor(byteLength: number)--><!--Device-ArrayBuffer-constructor(byteLength: number)-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [byteLength](#byteLength) | number | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [10200012](../errorcode-utils.md#10200012-constructor-calling-failure) |

## slice

```TypeScript
slice(begin: number, end?: number): ArrayBuffer
```

Selects a range of elements in this ArkTS ArrayBuffer to create an ArkTS ArrayBuffer.

**Since:** 12

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-ArrayBuffer-slice(begin: number, end?: number): ArrayBuffer--><!--Device-ArrayBuffer-slice(begin: number, end?: number): ArrayBuffer-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| begin | number | Yes |
| end | number | No |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| ArrayBuffer |

**Error codes:**

| Error Code ID |
| --- |
| [10200011](../errorcode-utils.md#10200011-passed-thisobject-is-not-an-instance-of-the-containers-class) |
| [10200201](../errorcode-utils.md#10200201-concurrent-modification-error) |

## byteLength

```TypeScript
readonly byteLength: number
```

Number of bytes occupied by the buffer.

**Type:** number

**Since:** 12

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-ArrayBuffer-readonly byteLength: number--><!--Device-ArrayBuffer-readonly byteLength: number-End-->

**System capability:** SystemCapability.Utils.Lang
