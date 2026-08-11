# Blob

Process data as blob type

**Since:** 9

<!--Device-buffer-class Blob--><!--Device-buffer-class Blob-End-->

**System capability:** SystemCapability.Utils.Lang

## Modules to Import

```TypeScript
import { buffer } from 'kits/@kit.ArkTS';
```

## arrayBuffer

```TypeScript
arrayBuffer(): Promise<ArrayBuffer>
```

Puts the **Blob** data into an **ArrayBuffer** object. This API uses a promise to return the result.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Blob-arrayBuffer(): Promise<ArrayBuffer>--><!--Device-Blob-arrayBuffer(): Promise<ArrayBuffer>-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| [Type](#type) |
| --- |
| Promise&lt;ArrayBuffer&gt; |

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

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Blob-constructor(sources: string[] | ArrayBuffer[] | TypedArray[] | DataView[] | Blob[], options?: Object)--><!--Device-Blob-constructor(sources: string[] | ArrayBuffer[] | TypedArray[] | DataView[] | Blob[], options?: Object)-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](#type) | Mandatory |
| --- | --- | --- |
| sources | string[] \| ArrayBuffer[] \| TypedArray[] \| DataView[] \| [Blob[]](arkts-arkts-buffer-blob-c.md) | Yes |
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

## slice

```TypeScript
slice(start?: number, end?: number, type?: string): Blob
```

Creates and returns a **Blob** object that contains specified data from this **Blob** object.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Blob-slice(start?: int, end?: int, type?: string): Blob--><!--Device-Blob-slice(start?: int, end?: int, type?: string): Blob-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](#type) | Mandatory |
| --- | --- | --- |
| start | number | No |
| end | number | No |
| [type](#type) | string | No |

**Return value:**

| [Type](#type) |
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

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Blob-text(): Promise<string>--><!--Device-Blob-text(): Promise<string>-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| [Type](#type) |
| --- |
| Promise&lt;string&gt; |

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

## size

```TypeScript
get size(): number
```

Total size of the Blob instance, in bytes.

**Type:** number

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Blob-get size(): int--><!--Device-Blob-get size(): int-End-->

**System capability:** SystemCapability.Utils.Lang

## type

```TypeScript
get type(): string
```

Type of the data in the Blob instance.

**Type:** string

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Blob-get type(): string--><!--Device-Blob-get type(): string-End-->

**System capability:** SystemCapability.Utils.Lang
