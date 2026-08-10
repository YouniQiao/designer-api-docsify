# dumpJsHeapData

## Modules to Import

```TypeScript
import { hidebug } from 'kits/@kit.PerformanceAnalysisKit';
```

## dumpJsHeapData

```TypeScript
function dumpJsHeapData(filename : string) : void
```

�����������ת����

> **ע��**
> 
> ����������ѵ��������ʱ���Ҹýӿ�Ϊͬ���ӿڣ����鲻Ҫ���ϼܰ汾�е��øýӿڣ��Ա���Ӧ�ö�����Ӱ���û����顣

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 26.1.0.

<!--Device-hidebug-function dumpJsHeapData(filename : string) : void--><!--Device-hidebug-function dumpJsHeapData(filename : string) : void-End-->

**System capability:** SystemCapability.HiviewDFX.HiProfiler.HiDebug

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| filename | string | Yes | �û��Զ���������������ת��������ļ���������Ӧ�õ�`files`Ŀ¼�������Ըò���������heapsnapshot�ļ���string���ȵ����ֵΪ128�ֽڡ� |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | the parameter check failed, Parameter type error |

## Examples

```TypeScript
import { hidebug } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  hidebug.dumpJsHeapData("heapData");
} catch (error) {
  console.error(`error code: ${(error as BusinessError).code}, error msg: ${(error as BusinessError).message}`);
}
```


## dumpJsHeapData

```TypeScript
function dumpJsHeapData(filename: string, needClean: boolean): void
```

�����������ת����֧�����nodeId���档

> **ע��**
> 
> ����������ѵ��������ʱ���Ҹýӿ�Ϊͬ���ӿڣ����鲻Ҫ���ϼܰ汾�е��øýӿڣ��Ա���Ӧ�ö�����Ӱ���û����顣

**Since:** 24

**ArkTS mode:** ArkTS-Dyn since version 24; ArkTS-Sta since version 26.1.0.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 24.

<!--Device-hidebug-function dumpJsHeapData(filename: string, needClean: boolean): void--><!--Device-hidebug-function dumpJsHeapData(filename: string, needClean: boolean): void-End-->

**System capability:** SystemCapability.HiviewDFX.HiProfiler.HiDebug

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| filename | string | Yes | �û��Զ�����������ת���ļ���������Ӧ�õ�filesĿ¼������fileName.heapsnapshot��ʽ�ļ���string���ȵ����ֵΪ128�ֽڡ� |
| needClean | boolean | Yes | ת���ѿ���ǰ�Ƿ���Ҫ���nodeId���档true����Ҫ�����false������Ҫ����� |

## Examples

```TypeScript
import { hidebug } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  hidebug.dumpJsHeapData("heapData", true);
} catch (error) {
  console.error(`error code: ${(error as BusinessError).code}, error msg: ${(error as BusinessError).message}`);
}
```

