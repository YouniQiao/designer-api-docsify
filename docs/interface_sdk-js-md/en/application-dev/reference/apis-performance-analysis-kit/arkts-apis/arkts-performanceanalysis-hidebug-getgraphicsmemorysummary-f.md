# getGraphicsMemorySummary

## Modules to Import

```TypeScript
import { hidebug } from 'kits/@kit.PerformanceAnalysisKit';
```

## getGraphicsMemorySummary

```TypeScript
function getGraphicsMemorySummary(interval?: int): Promise<GraphicsMemorySummary>
```

��ȡӦ���Դ����ݣ�ʹ��Promise�����첽�ص���

**Since:** 21

**ArkTS mode:** ArkTS-Dyn since version 21; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 21.

<!--Device-hidebug-function getGraphicsMemorySummary(interval?: int): Promise<GraphicsMemorySummary>--><!--Device-hidebug-function getGraphicsMemorySummary(interval?: int): Promise<GraphicsMemorySummary>-End-->

**System capability:** SystemCapability.HiviewDFX.HiProfiler.HiDebug

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| interval | ArkTS-Dyn: number  <br>ArkTS-Sta：int | No | �Դ����ݻ���ֵ��Чʱ�䣬��λΪ�롣Ĭ��ֵ��300��ȡֵ��ΧΪ[2-3600]��������ֵ����ȡֵ��Χʱ����ʹ��Ĭ��ֵ�� ���Դ����ݻ���ֵ����ʱ�䳬����ֵʱ����ȡ�����Դ����ݲ����»���ֵ������ֱ�ӻ�ȡ����ֵ�� ȡֵ��ΧΪȫ�������� |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;GraphicsMemorySummary&gt; | promise���󣬷���Ӧ���Դ����ݡ� |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 11400104 | Failed to get the application memory due to a remote exception. |

## Examples

```TypeScript
import { hidebug } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

hidebug.getGraphicsMemorySummary().then((ret: hidebug.GraphicsMemorySummary) => {
  console.info(`get graphicsMemory gl: ${ret.gl} graph: ${ret.graph}.`)
}).catch((error: BusinessError) => {
  console.error(`error code: ${error.code}, error msg: ${error.message}.`);
})
```

