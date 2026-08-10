# getNativeHeapFreeSize

## Modules to Import

```TypeScript
import { hidebug } from 'kits/@kit.PerformanceAnalysisKit';
```

## getNativeHeapFreeSize

```TypeScript
function getNativeHeapFreeSize() : bigint
```

��ȡ�ڴ������ͳ�ƵĽ��̳��еĿ��е���ͨ����ռ�õ����ֽ�����

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

<!--Device-hidebug-function getNativeHeapFreeSize() : bigint--><!--Device-hidebug-function getNativeHeapFreeSize() : bigint-End-->

**System capability:** SystemCapability.HiviewDFX.HiProfiler.HiDebug

**Return value:**

| Type | Description |
| --- | --- |
| bigint | �����ڴ������ͳ�ƵĽ��̳��еĿ��е���ͨ����ռ���ڴ��С����λΪByte�� |

## Examples

```TypeScript
import { hidebug } from '@kit.PerformanceAnalysisKit';

let nativeHeapFreeSize: bigint = hidebug.getNativeHeapFreeSize();
console.info(`nativeHeapFreeSize = ${nativeHeapFreeSize}`);
```

