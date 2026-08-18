# Blob

Process data as blob type

**Since:** 23

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

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Blob-arrayBuffer(): Promise<ArrayBuffer>--><!--Device-Blob-arrayBuffer(): Promise<ArrayBuffer>-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;ArrayBuffer&gt; |  |

**Examples**

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

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| sources | string[] \| ArrayBuffer[] \| TypedArray[] \| DataView[] \| [Blob](arkts-arkts-buffer-blob-c.md)[] | Yes | Data sources of the **Blob** object. |
| options | Object | No | options:<br>- **endings**: specifies how the terminator **'\n'** is output. The value can be **'native'** or **'transparent'**. **'native'** means that the terminator follows the system. **'transparent'** means that the terminator stored in the **Blob** object remains unchanged. The default value is **'transparent'**.<br>- **type**: type of the data in the **Blob** object. This type represents the MIME type of the data. However, it is not used for type format validation. The default value is **''**. |

**Examples**

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

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-Blob-constructor(sources: ArrayUnionType, options?: BlobOptions)--><!--Device-Blob-constructor(sources: ArrayUnionType, options?: BlobOptions)-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| sources | [ArrayUnionType](arkts-arkts-buffer-arrayuniontype-t.md) | Yes | The sources to store within the Blob |
| options | [BlobOptions](arkts-arkts-buffer-bloboptions-i.md) | No | Blob options {endings: string, type: string} endings: One of either 'transparent' or 'native'. type: The Blob content-type |

## slice

```TypeScript
slice(start?: int, end?: int, type?: string): Blob
```

Creates and returns a **Blob** object that contains specified data from this **Blob** object.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Blob-slice(start?: int, end?: int, type?: string): Blob--><!--Device-Blob-slice(start?: int, end?: int, type?: string): Blob-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| start | int | No | Offset to the start position of data. The default value is **0**. |
| end | int | No | Offset to the end position of data. The default value is the data length in the original **Blob** object. |
| type | string | No | Type of the data in the new **Blob** object. The default value is **''**. |

**Return value:**

| Type | Description |
| --- | --- |
| [Blob](arkts-arkts-buffer-blob-c.md) |  |

**Examples**

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

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Blob-text(): Promise<string>--><!--Device-Blob-text(): Promise<string>-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;string&gt; |  |

**Examples**

```TypeScript
import { buffer } from '@kit.ArkTS';

let blob: buffer.Blob = new buffer.Blob(['a', 'b', 'c']);
let pro = blob.text();
pro.then((val: string) => {
  console.info(val);
  // Output: abc
});
```

