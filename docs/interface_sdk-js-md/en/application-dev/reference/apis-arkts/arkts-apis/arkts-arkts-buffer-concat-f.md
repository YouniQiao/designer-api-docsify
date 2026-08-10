# concat

## Modules to Import

```TypeScript
import { buffer } from 'kits/@kit.ArkTS';
```

## concat

```TypeScript
function concat(list: Buffer[] | Uint8Array[], totalLength?: int): Buffer
```

将数组中的内容复制（默认复制全部内容，或复制指定字节长度）到新的Buffer对象中并返回。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-buffer-function concat(list: Buffer[] | Uint8Array[], totalLength?: int): Buffer--><!--Device-buffer-function concat(list: Buffer[] | Uint8Array[], totalLength?: int): Buffer-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| list | Buffer[] \| Uint8Array[] | Yes | Buffer或Uint8Array实例数组，用于拼接合并创建新的Buffer对象。 |
| totalLength | ArkTS-Dyn: number  <br>ArkTS-Sta：int | No | 需要复制的总字节长度，默认值为0。 |

**Return value:**

| Type | Description |
| --- | --- |
| [Buffer](arkts-arkts-buffer-buffer-c.md) | 返回新的Buffer对象。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 10200001 | The value of "length" is out of range. It must be >= 0 and <= uint32 max. Received value is: [length] |

## Examples

```TypeScript
import { buffer } from '@kit.ArkTS';

let buf1 = buffer.from("1234");
let buf2 = buffer.from("abcd");
let buf = buffer.concat([buf1, buf2]);
console.info(buf.toString('hex'));
// Output: 3132333461626364
```

