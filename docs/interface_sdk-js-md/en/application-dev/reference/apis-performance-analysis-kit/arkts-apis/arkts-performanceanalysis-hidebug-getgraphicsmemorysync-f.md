# getGraphicsMemorySync

## Modules to Import

```TypeScript
import { hidebug } from 'kits/@kit.PerformanceAnalysisKit';
```

## getGraphicsMemorySync

```TypeScript
function getGraphicsMemorySync(): int
```

ʹ��ͬ����ʽ��ȡӦ���Դ��ܴ�С��gl + graph����

> **ע��**
> 
> ���ڸýӿ��漰��ο����ͨ�ţ����ʱ���ܴﵽ�뼶��Ϊ�˱��������������⣬���鲻Ҫ�����̵߳��øýӿڣ��Ƽ�ʹ���첽�ӿ�`getGraphicsMemory`��

**Since:** 14

**ArkTS mode:** ArkTS-Dyn since version 14; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 14.

<!--Device-hidebug-function getGraphicsMemorySync(): int--><!--Device-hidebug-function getGraphicsMemorySync(): int-End-->

**System capability:** SystemCapability.HiviewDFX.HiProfiler.HiDebug

**Return value:**

| Type | Description |
| --- | --- |
| ArkTS-Dyn: number  <br>ArkTS-Sta：int | Ӧ���Դ��ܴ�С����λΪKB�� |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 11400104 | Failed to get the application memory due to a remote exception. |

## Examples

```TypeScript
import { hidebug } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  console.info(`graphicsMemory: ${hidebug.getGraphicsMemorySync()}`)
} catch (error) {
  console.error(`error code: ${(error as BusinessError).code}, error msg: ${(error as BusinessError).message}`);
}
```

