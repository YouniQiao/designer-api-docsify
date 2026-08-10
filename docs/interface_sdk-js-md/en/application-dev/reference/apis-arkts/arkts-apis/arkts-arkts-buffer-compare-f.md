# compare

## Modules to Import

```TypeScript
import { buffer } from 'kits/@kit.ArkTS';
```

## compare

```TypeScript
function compare(buf1: Buffer | Uint8Array, buf2: Buffer | Uint8Array): -1 | 0 | 1
```

返回两个Buffer或Uint8Array对象的比较结果，通常用于对Buffer或Uint8Array对象数组进行排序。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-buffer-function compare(buf1: Buffer | Uint8Array, buf2: Buffer | Uint8Array): -1 | 0 | 1--><!--Device-buffer-function compare(buf1: Buffer | Uint8Array, buf2: Buffer | Uint8Array): -1 | 0 | 1-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| buf1 | [Buffer](arkts-arkts-buffer-buffer-c.md) \| Uint8Array | Yes | 待比较的第一个Buffer或Uint8Array实例。 |
| buf2 | [Buffer](arkts-arkts-buffer-buffer-c.md) \| Uint8Array | Yes | 待比较的第二个Buffer或Uint8Array实例。 |

**Return value:**

| Type | Description |
| --- | --- |
| -1 | 如果buf1与buf2相同，则返回0。 &lt;br/&gt;如果排序时buf1位于buf2之后，则返回1。 &lt;br/&gt;如果排序时buf1位于buf2之前，则返回-1。 |

## Examples

```TypeScript
import { buffer } from '@kit.ArkTS';

let buf1 = buffer.from('1234');
let buf2 = buffer.from('0123');
let res = buffer.compare(buf1, buf2);

console.info(Number(res).toString());
// Output: 1
```


## compare

```TypeScript
function compare(buf1: Buffer | Uint8Array, buf2: Buffer | Uint8Array): int
```

返回两个Buffer或Uint8Array对象的比较结果，通常用于对Buffer或Uint8Array对象数组进行排序。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-buffer-function compare(buf1: Buffer | Uint8Array, buf2: Buffer | Uint8Array): int--><!--Device-buffer-function compare(buf1: Buffer | Uint8Array, buf2: Buffer | Uint8Array): int-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| buf1 | [Buffer](arkts-arkts-buffer-buffer-c.md) \| Uint8Array | Yes | 待比较的第一个Buffer或Uint8Array实例。 |
| buf2 | [Buffer](arkts-arkts-buffer-buffer-c.md) \| Uint8Array | Yes | 待比较的第二个Buffer或Uint8Array实例。 |

**Return value:**

| Type | Description |
| --- | --- |
| int | 如果buf1与buf2相同，则返回0。&lt;br/&gt;如果排序时buf1位于buf2之后，则返回1。&lt;br/&gt;如果排序时buf1位于buf2之前，则返回-1。 |

