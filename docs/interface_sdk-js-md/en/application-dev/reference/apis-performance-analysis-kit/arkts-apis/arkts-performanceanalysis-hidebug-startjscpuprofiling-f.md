# startJsCpuProfiling

## Modules to Import

```TypeScript
import { hidebug } from 'kits/@kit.PerformanceAnalysisKit';
```

## startJsCpuProfiling

```TypeScript
function startJsCpuProfiling(filename : string) : void
```

���������Profiling�������٣�`startJsCpuProfiling(filename: string)`�����ĵ�����Ҫ��`stopJsCpuProfiling()`�����ĵ���һһ��Ӧ���ȿ�����رգ�������ظ��������ظ��رյĵ��÷�ʽ�������ӿڵ����쳣��

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-hidebug-function startJsCpuProfiling(filename : string) : void--><!--Device-hidebug-function startJsCpuProfiling(filename : string) : void-End-->

**System capability:** SystemCapability.HiviewDFX.HiProfiler.HiDebug

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| filename | string | Yes | �û��Զ���Ĳ������������ļ���������Ӧ�õ�`files`Ŀ¼�������Ըò���������json�ļ���string���ȵ����ֵΪ128�� |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | the parameter check failed, Parameter type error |

## Examples

```TypeScript
import { hidebug } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  hidebug.startJsCpuProfiling("cpu_profiling");
  // ...
  hidebug.stopJsCpuProfiling();
} catch (error) {
  console.error(`error code: ${(error as BusinessError).code}, error msg: ${(error as BusinessError).message}`);
}
```

