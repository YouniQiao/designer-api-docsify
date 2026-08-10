# getVMRuntimeStat

## Modules to Import

```TypeScript
import { hidebug } from 'kits/@kit.PerformanceAnalysisKit';
```

## getVMRuntimeStat

```TypeScript
function getVMRuntimeStat(item: string): long
```

���ݲ�����ȡָ����ϵͳGCͳ����Ϣ��

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-hidebug-function getVMRuntimeStat(item: string): long--><!--Device-hidebug-function getVMRuntimeStat(item: string): long-End-->

**System capability:** SystemCapability.HiviewDFX.HiProfiler.HiDebug

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| item | string | Yes | ����ͳ����Ϣ�����͡��ɻ�ȡ��ͳ����Ϣ�������£� "ark.gc.gc-count"����ǰ�̵߳�GC������ "ark.gc.gc-time"����ǰ�̴߳�����GC�ܺ�ʱ����msΪ��λ�� "ark.gc.gc-bytes-allocated"����ǰ�߳�Ark������ѷ�����ڴ��С����BΪ��λ�� "ark.gc.gc-bytes-freed"����ǰ�߳�GC�ɹ����յ��ڴ棬��BΪ��λ�� "ark.gc.fullgc-longtime-count"����ǰ�̳߳���fullGC������ |

**Return value:**

| Type | Description |
| --- | --- |
| ArkTS-Dyn: number  <br>ArkTS-Sta：long | ϵͳGCͳ����Ϣ�����ݴ���Ĳ�����������Ӧ����Ϣ�� |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Possible causes: 1. Invalid parameter, a string parameter required. 2. Invalid parameter, unknown property. |

## Examples

```TypeScript
import { hidebug } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  console.info(`gc-count: ${hidebug.getVMRuntimeStat('ark.gc.gc-count')}`);
  console.info(`gc-time: ${hidebug.getVMRuntimeStat('ark.gc.gc-time')}`);
  console.info(`gc-bytes-allocated: ${hidebug.getVMRuntimeStat('ark.gc.gc-bytes-allocated')}`);
  console.info(`gc-bytes-freed: ${hidebug.getVMRuntimeStat('ark.gc.gc-bytes-freed')}`);
  console.info(`fullgc-longtime-count: ${hidebug.getVMRuntimeStat('ark.gc.fullgc-longtime-count')}`);
} catch (error) {
  console.error(`error code: ${(error as BusinessError).code}, error msg: ${(error as BusinessError).message}`);
}
```

