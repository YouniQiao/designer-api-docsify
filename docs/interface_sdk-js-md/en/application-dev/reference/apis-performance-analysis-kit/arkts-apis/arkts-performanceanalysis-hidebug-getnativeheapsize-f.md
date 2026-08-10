# getNativeHeapSize

## Modules to Import

```TypeScript
import { hidebug } from 'kits/@kit.PerformanceAnalysisKit';
```

## getNativeHeapSize

```TypeScript
function getNativeHeapSize() : bigint
```

��ȡ�ڴ������ͳ�ƵĽ��̳��е���ͨ����ռ�õ����ֽ�����

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

<!--Device-hidebug-function getNativeHeapSize() : bigint--><!--Device-hidebug-function getNativeHeapSize() : bigint-End-->

**System capability:** SystemCapability.HiviewDFX.HiProfiler.HiDebug

**Return value:**

| Type | Description |
| --- | --- |
| bigint | �ڴ������ͳ�ƵĽ��̳��е���ͨ����ռ���ڴ�Ĵ�С����������Ԫ���ݣ�����λΪByte�� |

## Examples

```TypeScript
import { hidebug } from '@kit.PerformanceAnalysisKit';

let nativeHeapSize: bigint = hidebug.getNativeHeapSize();
console.info(`nativeHeapSize = ${nativeHeapSize}`);
```

