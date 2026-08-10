# getPss

## Modules to Import

```TypeScript
import { hidebug } from 'kits/@kit.PerformanceAnalysisKit';
```

## getPss

```TypeScript
function getPss() : bigint
```

��ȡӦ�ý���ʵ��ʹ�õ������ڴ��С���ӿ�ʵ�ַ�ʽ����ȡ/proc/{pid}/smaps_rollup�ڵ��е�Pss��SwapPssֵ����͡�

> **ע��**
> 
> ����/proc/{pid}/smaps_rollup�Ķ�ȡ��ʱ�ϳ������鲻Ҫ�����߳���ʹ�øýӿڣ���ͨ��@ohos.taskpool��@ohos.worker�����첽�߳��Ա���Ӧ�ó��ֿ��١�

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

<!--Device-hidebug-function getPss() : bigint--><!--Device-hidebug-function getPss() : bigint-End-->

**System capability:** SystemCapability.HiviewDFX.HiProfiler.HiDebug

**Return value:**

| Type | Description |
| --- | --- |
| bigint | ����Ӧ�ý���ʵ��ʹ�õ������ڴ��С����λΪKB�� |

## Examples

```TypeScript
import { hidebug } from '@kit.PerformanceAnalysisKit';

let pss: bigint = hidebug.getPss();
console.info(`pss = ${pss}`);
```

