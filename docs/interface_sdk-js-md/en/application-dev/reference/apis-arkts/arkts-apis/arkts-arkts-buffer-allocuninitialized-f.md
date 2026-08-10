# allocUninitialized

## Modules to Import

```TypeScript
import { buffer } from 'kits/@kit.ArkTS';
```

## allocUninitialized

```TypeScript
function allocUninitialized(size: int): Buffer
```

创建指定大小未初始化的Buffer对象。内存不从缓冲池分配，适用于需要创建较大Buffer或希望精确控制内存分配的场景，如一次性分配较大内存区域（避免缓冲池可能导致的内存碎片累积和缓存性能损耗）。创建的Buffer的内容未知，需要使用[fill](arkts-arkts-buffer-buffer-c.md#fill)函数来初始化Buffer对象。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-buffer-function allocUninitialized(size: int): Buffer--><!--Device-buffer-function allocUninitialized(size: int): Buffer-End-->

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

let buf = buffer.allocUninitialized(10);
buf.fill(0);
console.info(JSON.stringify(buf)); // {"type":"Buffer","data":[0,0,0,0,0,0,0,0,0,0]}
```

