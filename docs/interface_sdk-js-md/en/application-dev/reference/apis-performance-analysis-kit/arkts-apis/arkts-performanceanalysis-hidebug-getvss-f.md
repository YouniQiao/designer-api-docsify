# getVss

## Modules to Import

```TypeScript
import { hidebug } from 'kits/@kit.PerformanceAnalysisKit';
```

## getVss

```TypeScript
function getVss(): bigint
```

��ȡӦ�ý���ռ�õ������ڴ��С���ӿ�ʵ�ַ�ʽ����ȡ/proc/{pid}/statm�ڵ��е�sizeֵ���ڴ�ҳ������vss = size * ҳ��С��4KB/ҳ����

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

<!--Device-hidebug-function getVss(): bigint--><!--Device-hidebug-function getVss(): bigint-End-->

**System capability:** SystemCapability.HiviewDFX.HiProfiler.HiDebug

**Return value:**

| Type | Description |
| --- | --- |
| bigint | ����Ӧ�ý���ռ�õ������ڴ��С����λΪKB�� |

## Examples

```TypeScript
import { hidebug } from '@kit.PerformanceAnalysisKit';

let vss: bigint = hidebug.getVss();
console.info(`vss = ${vss}`);
```

