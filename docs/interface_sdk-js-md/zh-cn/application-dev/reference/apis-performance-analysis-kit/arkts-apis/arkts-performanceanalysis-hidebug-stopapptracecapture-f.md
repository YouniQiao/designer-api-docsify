# stopAppTraceCapture

## 导入模块

```TypeScript
import { hidebug } from 'kits/@kit.PerformanceAnalysisKit';
```

## stopAppTraceCapture

```TypeScript
function stopAppTraceCapture(): void
```

ֹͣӦ��trace�ɼ�������ǰ�����ȵ���`startAppTraceCapture()`������ʼ�ɼ����ر�ǰδ�������ظ��رջᵼ�½ӿ��쳣������startAppTraceCapture�ӿڣ����û�к�������limitSize����������trace�Ĵ�С���ڴ����limitSize��С��ϵͳ�ڲ����Զ�����stopAppTraceCapture���ٴ��ֶ�����stopAppTraceCapture�ͻ��׳�������11400105��

**起始版本：** 12

**ArkTS模式：** ArkTS-Dyn起始版本为12；ArkTS-Sta起始版本为23。

<!--Device-hidebug-function stopAppTraceCapture(): void--><!--Device-hidebug-function stopAppTraceCapture(): void-End-->

**系统能力：** SystemCapability.HiviewDFX.HiProfiler.HiDebug

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 11400105 | No capture trace running |
| 11400104 | The status of the trace is abnormal |

## 示例

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

