# getPrivateDirty

## Modules to Import

```TypeScript
import { hidebug } from 'kits/@kit.PerformanceAnalysisKit';
```

## getPrivateDirty

```TypeScript
function getPrivateDirty() : bigint
```

��ȡ���̵�˽�����ڴ��С����ȡ/proc/{pid}/smaps_rollup�е�Private_Dirtyֵ��

> **ע��**
> 
> ����/proc/{pid}/smaps_rollup�Ķ�ȡ��ʱ�ϳ������鲻Ҫ�����߳���ʹ�øýӿڣ���ͨ��@ohos.taskpool��@ohos.worker�����첽�߳��Ա���Ӧ�ó��ֿ��١�

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-hidebug-function getPrivateDirty() : bigint--><!--Device-hidebug-function getPrivateDirty() : bigint-End-->

**System capability:** SystemCapability.HiviewDFX.HiProfiler.HiDebug

**Return value:**

| Type | Description |
| --- | --- |
| bigint | ���ؽ��̵�˽�����ڴ��С����λΪKB�� |

## Examples

```TypeScript
import { hidebug } from '@kit.PerformanceAnalysisKit';

let privateDirty: bigint = hidebug.getPrivateDirty();
console.info(`privateDirty = ${privateDirty}`);
```

