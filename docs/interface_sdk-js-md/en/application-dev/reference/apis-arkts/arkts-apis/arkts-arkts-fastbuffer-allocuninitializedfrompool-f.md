# allocUninitializedFromPool

## Modules to Import

```TypeScript
import { fastbuffer } from 'kits/@kit.ArkTS';
```

## allocUninitializedFromPool

```TypeScript
function allocUninitializedFromPool(size: number): FastBuffer
```

从缓冲池中创建指定大小未初始化的FastBuffer对象。调用[fill](arkts-arkts-fastbuffer-fastbuffer-c.md#fill)函数初始化该对象。

**Since:** 20

**ArkTS mode:** ArkTS-Dyn only, since version 20.

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-fastbuffer-function allocUninitializedFromPool(size: number): FastBuffer--><!--Device-fastbuffer-function allocUninitializedFromPool(size: number): FastBuffer-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| size | number | Yes | 指定的FastBuffer对象长度，单位：字节。取值范围：0 <= size <= UINT32_MAX。 |

**Return value:**

| Type | Description |
| --- | --- |
| [FastBuffer](arkts-arkts-fastbuffer-fastbuffer-c.md) | 未初始化的FastBuffer实例。 |

## Examples

```TypeScript
import { fastbuffer } from '@kit.ArkTS';

let buf = fastbuffer.allocUninitializedFromPool(10);
buf.fill(0);
// "buf":[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
```

