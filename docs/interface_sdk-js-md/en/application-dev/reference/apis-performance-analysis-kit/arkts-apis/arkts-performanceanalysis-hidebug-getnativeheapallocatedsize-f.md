# getNativeHeapAllocatedSize

## Modules to Import

```TypeScript
import { hidebug } from 'kits/@kit.PerformanceAnalysisKit';
```

## getNativeHeapAllocatedSize

```TypeScript
function getNativeHeapAllocatedSize() : bigint
```

��ȡ�ڴ������ͳ�ƵĽ��̳��е���ʹ�õ���ͨ����ռ�õ����ֽ�����

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

<!--Device-hidebug-function getNativeHeapAllocatedSize() : bigint--><!--Device-hidebug-function getNativeHeapAllocatedSize() : bigint-End-->

**System capability:** SystemCapability.HiviewDFX.HiProfiler.HiDebug

**Return value:**

| Type | Description |
| --- | --- |
| bigint | �����ڴ������ͳ�ƵĽ��̳��е���ʹ�õ���ͨ����ռ���ڴ��С����λΪByte�� |

## Examples

```TypeScript
import { hidebug } from '@kit.PerformanceAnalysisKit';

let nativeHeapAllocatedSize: bigint = hidebug.getNativeHeapAllocatedSize();
console.info(`nativeHeapAllocatedSize = ${nativeHeapAllocatedSize}`);
```

