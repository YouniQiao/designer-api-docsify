# concat

## Modules to Import

```TypeScript
import { fastbuffer } from 'kits/@kit.ArkTS';
```

## concat

```TypeScript
function concat(list: FastBuffer[] | Uint8Array[], totalLength?: number): FastBuffer
```

将数组中指定字节长度的内容复制并拼接后，返回新的FastBuffer对象。

当数组中所有对象的长度总和大于totalLength时，返回结果的长度将被截断为totalLength。

当数组中所有对象的长度总和小于totalLength时，返回结果的多余部分将会被填充为0。

**Since:** 20

**ArkTS mode:** ArkTS-Dyn only, since version 20.

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-fastbuffer-function concat(list: FastBuffer[] | Uint8Array[], totalLength?: number): FastBuffer--><!--Device-fastbuffer-function concat(list: FastBuffer[] | Uint8Array[], totalLength?: number): FastBuffer-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| list | FastBuffer[] \| Uint8Array[] | Yes | 待拼接的FastBuffer或Uint8Array实例数组，数组中所有对象的内容将被依次复制到新的FastBuffer对象中。 |
| totalLength | number | No | 需要复制的总字节长度，默认值为数组中所有对象的长度总和。取值范围：0 <= totalLength <= UINT32_MAX。 |

**Return value:**

| Type | Description |
| --- | --- |
| [FastBuffer](arkts-arkts-fastbuffer-fastbuffer-c.md) | 返回新的FastBuffer对象。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 10200001 | Range error. Possible causes: The value of the parameter is not within the specified range. |

## Examples

```TypeScript
import { fastbuffer } from '@kit.ArkTS';

let buf1 = fastbuffer.from("1234");
let buf2 = fastbuffer.from("abcd");
let buf = fastbuffer.concat([buf1, buf2]);
console.info(buf.toString('hex'));
// Output: 3132333461626364
```

