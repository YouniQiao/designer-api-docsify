# ArrayBuffer

Underlying data structure of the ArkTS TypedArray ([Int8Array](./arkts/@arkts.collections:collections),  
[Uint8Array](./arkts/@arkts.collections:collections),  
[Int16Array](./arkts/@arkts.collections:collections),  
[Uint16Array](./arkts/@arkts.collections:collections),  
[Int32Array](./arkts/@arkts.collections:collections),  
[Uint32Array](./arkts/@arkts.collections:collections),  
[Uint8ClampedArray](./arkts/@arkts.collections:collections), and  
[Float32Array](./arkts/@arkts.collections:collections)).

> **NOTE：**
> 
> - This module can be imported only to ArkTS files (with the file name extension .ets).
> **Decorator**: \@Sendable

**Since:** 12

**Decorator:** @Sendable

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

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-ArrayBuffer-constructor(byteLength: number)--><!--Device-ArrayBuffer-constructor(byteLength: number)-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [byteLength](#bytelength) | number | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [10200012](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-arkts/errorcode-utils.md#10200012-constructor-calling-failure) |

## slice

```TypeScript
slice(begin: number, end?: number): ArrayBuffer
```

Selects a range of elements in this ArkTS ArrayBuffer to create an ArkTS ArrayBuffer.

**Since:** 12

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
| [10200011](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-arkts/errorcode-utils.md#10200011-passed-thisobject-is-not-an-instance-of-the-containers-class) |
| [10200201](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-arkts/errorcode-utils.md#10200201-concurrent-modification-error) |

## byteLength

```TypeScript
readonly byteLength: number
```

Number of bytes occupied by the buffer.

**Type:** number

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-ArrayBuffer-readonly byteLength: number--><!--Device-ArrayBuffer-readonly byteLength: number-End-->

**System capability:** SystemCapability.Utils.Lang
