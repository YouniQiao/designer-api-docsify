# Blob

Process data as blob type

**Since:** 23

**Deprecated since:** -1

<!--Device-buffer-class Blob--><!--Device-buffer-class Blob-End-->

**System capability:** SystemCapability.Utils.Lang

## Modules to Import

```TypeScript
import { buffer } from '@kit.ArkTS';
```

## arrayBuffer

```TypeScript
arrayBuffer(): Promise<ArrayBuffer>
```

Puts the **Blob** data into an **ArrayBuffer** object. This API uses a promise to return the result.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Blob-arrayBuffer(): Promise<ArrayBuffer>--><!--Device-Blob-arrayBuffer(): Promise<ArrayBuffer>-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;ArrayBuffer & gt; |

## Examples

```TypeScript
import { buffer } from '@kit.ArkTS';

let blob: buffer.Blob = new buffer.Blob(['a', 'b', 'c']);
let pro = blob.arrayBuffer();
pro.then((val: ArrayBuffer) => {
  let uint8Array: Uint8Array = new Uint8Array(val);
  console.info(uint8Array.toString());
  // Output: 97,98,99
});
```

## constructor

```TypeScript
constructor(sources: string[] | ArrayBuffer[] | TypedArray[] | DataView[] | Blob[], options?: Object)
```

A constructor used to create a **Blob** object.

**Since:** 9

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Blob-constructor(sources: string[] | ArrayBuffer[] | TypedArray[] | DataView[] | Blob[], options?: Object)--><!--Device-Blob-constructor(sources: string[] | ArrayBuffer[] | TypedArray[] | DataView[] | Blob[], options?: Object)-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| sources | string[] \| ArrayBuffer[] \| TypedArray[] \| DataView[] \| [Blob](arkts-arkts-buffer-blob-c.md)[] | Yes |
| options | Object | No |

## Examples

```TypeScript
import { buffer } from '@kit.ArkTS';

let blob: buffer.Blob  = new buffer.Blob(['a', 'b', 'c']);

class option {
  endings: string = "";
  type: string = "";
}
let o1: option = {endings:'native', type: 'MIME'}
let blob1: buffer.Blob = new buffer.Blob(['a', 'b', 'c'], o1);
```

## constructor

```TypeScript
constructor(sources: ArrayUnionType, options?: BlobOptions)
```

Creates a new Blob object containing a concatenation of the given sources.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-Blob-constructor(sources: ArrayUnionType, options?: BlobOptions)--><!--Device-Blob-constructor(sources: ArrayUnionType, options?: BlobOptions)-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| sources | [ArrayUnionType](arkts-arkts-buffer-arrayuniontype-t.md) | Yes |
| options | [BlobOptions](arkts-arkts-buffer-bloboptions-i.md) | No |

## slice

```TypeScript
slice(start?: number, end?: number, type?: string): Blob
```

Creates and returns a **Blob** object that contains specified data from this **Blob** object.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Blob-slice(start?: int, end?: int, type?: string): Blob--><!--Device-Blob-slice(start?: int, end?: int, type?: string): Blob-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| start | number | No |
| end | number | No |
| type | string | No |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| [Blob](arkts-arkts-buffer-blob-c.md) |

## Examples

```TypeScript
import { buffer } from '@kit.ArkTS';

let blob: buffer.Blob = new buffer.Blob(['a', 'b', 'c']);
let blob2 = blob.slice(0, 2);
let blob3 = blob.slice(0, 2, "MIME");
console.info("type:", blob3.type); // type: MIME
```

## text

```TypeScript
text(): Promise<string>
```

Decodes data using UTF-8 and returns a string. This API uses a promise to return the result.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Blob-text(): Promise<string>--><!--Device-Blob-text(): Promise<string>-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;string & gt; |

## Examples

```TypeScript
import { buffer } from '@kit.ArkTS';

let blob: buffer.Blob = new buffer.Blob(['a', 'b', 'c']);
let pro = blob.text();
pro.then((val: string) => {
  console.info(val);
  // Output: abc
});
```
