# allocUninitializedFromPool

## Modules to Import

```TypeScript
import { buffer } from 'kits/@kit.ArkTS';
```

## allocUninitializedFromPool

```TypeScript
function allocUninitializedFromPool(size: int): Buffer
```

创建指定大小未初始化的Buffer对象。内存从缓冲池分配，缓冲池为预分配的内存区域，适用于创建较小Buffer时减少频繁内存分配的开销，提升性能。对于需要独立内存的场景，建议使用[allocUninitialized](arkts-arkts-buffer-allocuninitialized-f.md#allocuninitialized)。创建的Buffer内容未知，需要使用[fill](arkts-arkts-buffer-buffer-c.md#fill)函数来初始化Buffer对象。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-buffer-function allocUninitializedFromPool(size: int): Buffer--><!--Device-buffer-function allocUninitializedFromPool(size: int): Buffer-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| size | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | 指定的Buffer对象长度，单位：字节。 |

**Return value:**

| Type | Description |
| --- | --- |
| [Buffer](arkts-arkts-buffer-buffer-c.md) | 未初始化的Buffer实例。 |

## Examples

```TypeScript
import { buffer, JSON } from '@kit.ArkTS';

let buf = buffer.allocUninitializedFromPool(10);
buf.fill(0);
console.info(JSON.stringify(buf)); // {"type":"Buffer","data":[0,0,0,0,0,0,0,0,0,0]}
```

