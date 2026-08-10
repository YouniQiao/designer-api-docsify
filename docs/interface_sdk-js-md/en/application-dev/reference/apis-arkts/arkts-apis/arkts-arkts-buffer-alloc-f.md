# alloc

## Modules to Import

```TypeScript
import { buffer } from 'kits/@kit.ArkTS';
```

## alloc

```TypeScript
function alloc(size: int, fill?: string | Buffer | int | double | long, encoding?: BufferEncoding): Buffer
```

创建指定字节长度的Buffer对象，并使用指定值进行初始化填充（默认填充0）。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-buffer-function alloc(size: int, fill?: string | Buffer | int | double | long, encoding?: BufferEncoding): Buffer--><!--Device-buffer-function alloc(size: int, fill?: string | Buffer | int | double | long, encoding?: BufferEncoding): Buffer-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| size | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | 指定的Buffer对象长度，单位：字节。取值为正整数，最大值为2^32-1，即4294967295。 |
| fill | ArkTS-Dyn: string \| Buffer \| number \| number \| number  <br>ArkTS-Sta：string \| Buffer \| int \| double \| long | No | 填充至新缓冲区的值。默认值：0。<br>**Since:** 9 - 10 |
| encoding | [BufferEncoding](arkts-arkts-fastbuffer-bufferencoding-t.md) | No | 编码格式（当fill为string时，才有意义）。默认值：'utf8'。 |

**Return value:**

| Type | Description |
| --- | --- |
| [Buffer](arkts-arkts-buffer-buffer-c.md) | 返回一个Buffer对象。 |

