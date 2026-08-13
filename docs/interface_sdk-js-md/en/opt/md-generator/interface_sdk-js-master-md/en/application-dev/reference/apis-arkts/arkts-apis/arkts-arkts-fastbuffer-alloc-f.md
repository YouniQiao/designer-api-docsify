# alloc

## Modules to Import

```TypeScript
import { fastbuffer } from '@kit.ArkTS';
```

## alloc

```TypeScript
function alloc(size: number, fill?: string | FastBuffer | number, encoding?: BufferEncoding): FastBuffer
```

Allocates a new FastBuffer for a fixed size bytes. If fill is undefined, the FastBuffer will be zero-filled.

**Since:** 20

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-fastbuffer-function alloc(size: number, fill?: string | FastBuffer | number, encoding?: BufferEncoding): FastBuffer--><!--Device-fastbuffer-function alloc(size: number, fill?: string | FastBuffer | number, encoding?: BufferEncoding): FastBuffer-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| size | number | Yes |
| fill | string \| [FastBuffer](arkts-arkts-fastbuffer-fastbuffer-c.md) \| number | No |
| encoding | [BufferEncoding](arkts-arkts-fastbuffer-bufferencoding-t.md) | No |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| [FastBuffer](arkts-arkts-fastbuffer-fastbuffer-c.md) |

## Examples

```TypeScript
import { fastbuffer } from '@kit.ArkTS';

let buf1 = fastbuffer.alloc(5);
let buf2 = fastbuffer.alloc(5, 'a');
let buf3 = fastbuffer.alloc(11, 'aGVsbG8gd29ybGQ=', 'base64');
console.info(buf2.toString());
// Output: aaaaa
console.info(buf3.toString());
// Output: hello world
```
