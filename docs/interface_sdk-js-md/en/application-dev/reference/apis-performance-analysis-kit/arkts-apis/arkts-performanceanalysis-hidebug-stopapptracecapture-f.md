# stopAppTraceCapture

## Modules to Import

```TypeScript
import { hidebug } from 'kits/@kit.PerformanceAnalysisKit';
```

## stopAppTraceCapture

```TypeScript
function stopAppTraceCapture(): void
```

ֹͣӦ��trace�ɼ�������ǰ�����ȵ���`startAppTraceCapture()`������ʼ�ɼ����ر�ǰδ�������ظ��رջᵼ�½ӿ��쳣������startAppTraceCapture�ӿڣ����û�к�������limitSize����������trace�Ĵ�С���ڴ����limitSize��С��ϵͳ�ڲ����Զ�����stopAppTraceCapture���ٴ��ֶ�����stopAppTraceCapture�ͻ��׳�������11400105��

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-hidebug-function stopAppTraceCapture(): void--><!--Device-hidebug-function stopAppTraceCapture(): void-End-->

**System capability:** SystemCapability.HiviewDFX.HiProfiler.HiDebug

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 11400105 | No capture trace running |
| 11400104 | The status of the trace is abnormal |

## Examples

```TypeScript
import { hidebug } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

let tags: number[] = [hidebug.tags.ABILITY_MANAGER, hidebug.tags.ARKUI];
let flag: hidebug.TraceFlag = hidebug.TraceFlag.MAIN_THREAD;
let limitSize: number = 1024 * 1024;
try {
  let fileName: string = hidebug.startAppTraceCapture(tags, flag, limitSize);
  console.info(`fileName = ${fileName}`);
  // code block
  // ...
  // code block
  hidebug.stopAppTraceCapture();
} catch (error) {
  console.error(`error code: ${(error as BusinessError).code}, error msg: ${(error as BusinessError).message}`);
}
```

