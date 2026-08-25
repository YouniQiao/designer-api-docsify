# from

## Modules to Import

```TypeScript
import { buffer } from 'kits/@kit.ArkTS';
```

## from

```TypeScript
function from(array: number[]): Buffer
```

Creates a **Buffer** object with the specified array.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| array | number[] | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| Buffer |


## from

```TypeScript
function from(arrayBuffer: ArrayBuffer | SharedArrayBuffer, byteOffset?: number, length?: number): Buffer
```

Creates a **Buffer** object of the specified length that shares memory with ArrayBuffer.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [arrayBuffer](arkts-arkts-buffer-blob-c.md) | ArrayBuffer \| SharedArrayBuffer | Yes |
| byteOffset | number | No |
| length | number | No |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| Buffer |

**Error codes:**

| Error Code ID |
| --- |
| [10200001](../errorcode-utils.md#10200001-value-out-of-range) |


## from

```TypeScript
function from(buffer: Buffer | Uint8Array): Buffer
```

Copies the data of a passed **Buffer** object to create a new **Buffer** object and returns the new one. Creates a **Buffer** object based on the memory of a passed **Uint8Array** object and returns the new object, maintaining the memory association of the data.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [buffer](arkts-buffer.md) | Buffer \| Uint8Array | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| Buffer |


## from

```TypeScript
function from(object: Object, offsetOrEncoding: number | string, length: number): Buffer
```

Creates a **Buffer** object based on the specified object.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| object | Object | Yes |
| offsetOrEncoding | number \| string | Yes |
| length | number | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| Buffer |


## from

```TypeScript
function from(string: String, encoding?: BufferEncoding): Buffer
```

Creates a **Buffer** object based on a string in the given encoding format.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| string | String | Yes |
| encoding | BufferEncoding | No |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| Buffer |
