# requestTrace

## Modules to Import

```TypeScript
import { hidebug } from 'kits/@kit.PerformanceAnalysisKit';
```

## requestTrace

```TypeScript
function requestTrace(config: RequestTraceConfig): Promise<string>
```

��ȡ��ǰ���̵�trace��Ϣ������Ӧ��tag��ͼ�񴰿�tag��cpu���Ⱥ�binder�ں���Ϣ��ʹ��Promise�첽�ص����ɼ�trace���ص�.sys�ļ���Ŀ¼�����洢3�ݣ��������ڵ���3��ʱ�ٴε��ýӿڻ��׳�������11400120��

**Since:** 24

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 24.

<!--Device-hidebug-function requestTrace(config: RequestTraceConfig): Promise<string>--><!--Device-hidebug-function requestTrace(config: RequestTraceConfig): Promise<string>-End-->

**System capability:** SystemCapability.HiviewDFX.HiProfiler.HiDebug

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| config | [RequestTraceConfig](arkts-performanceanalysis-hidebug-requesttraceconfig-i.md) | Yes | trace�ɼ�������Ϣ�� |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;string&gt; | Promise���󣬷�����.sys��Ϊ��׺��trace�ļ���Ӧ��ɳ��·���� |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 11400302 | Resource unavailable. |
| 11400104 | Remote service exception. |
| 11400120 | Trace storage limit reached. |

## Examples

```TypeScript
import { hidebug, hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  hidebug.requestTrace({
    identifier: "trace_name",
    bufferSizeKb: 1024,
    durationMs: 1000,
    reserved: 0,
  }).then((tracePath: string) => {
    hilog.info(0x0000, 'hidebug', `tracePath: ${tracePath}`)
  }).catch((err: BusinessError) => {
    hilog.error(0x0000, 'hidebug', `error code: ${err.code}, message: ${err.message}`)
  })
} catch (error) {
  hilog.error(0x0000, 'hidebug', `error code: ${(error as BusinessError).code}, message: ${(error as BusinessError).message}`)
}
```

