# alloc

## Modules to Import

```TypeScript
import { fastbuffer } from 'kits/@kit.ArkTS';
```

## alloc

```TypeScript
function alloc(size: number, fill?: string | FastBuffer | number, encoding?: BufferEncoding): FastBuffer
```

创建指定字节长度的FastBuffer对象并初始化。调用后，FastBuffer对象的每个字节将被填充为指定的fill值，未指定fill时默认填充为0。

**Since:** 20

**ArkTS mode:** ArkTS-Dyn only, since version 20.

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-fastbuffer-function alloc(size: number, fill?: string | FastBuffer | number, encoding?: BufferEncoding): FastBuffer--><!--Device-fastbuffer-function alloc(size: number, fill?: string | FastBuffer | number, encoding?: BufferEncoding): FastBuffer-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| size | number | Yes | 指定的FastBuffer对象长度，单位：字节。取值范围：0 <= size <= UINT32_MAX。 |
| fill | string \| FastBuffer \| number | No | 填充至新缓冲区的值，默认值：0。 |
| encoding | [BufferEncoding](arkts-arkts-fastbuffer-bufferencoding-t.md) | No | 编码格式（当`fill`为string时，才有意义）。默认值：'utf8'。传入无法识别的encoding会抛出TypeError。 |

**Return value:**

| Type | Description |
| --- | --- |
| [FastBuffer](arkts-arkts-fastbuffer-fastbuffer-c.md) | 返回一个FastBuffer对象。 |

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

