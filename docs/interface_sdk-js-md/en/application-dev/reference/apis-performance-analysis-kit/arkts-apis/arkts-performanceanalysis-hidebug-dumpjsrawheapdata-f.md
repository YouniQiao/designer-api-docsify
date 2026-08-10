# dumpJsRawHeapData

## Modules to Import

```TypeScript
import { hidebug } from 'kits/@kit.PerformanceAnalysisKit';
```

## dumpJsRawHeapData

```TypeScript
function dumpJsRawHeapData(needGC?: boolean): Promise<string>
```

Ϊ��ǰ�߳�ת���������ԭʼ�ѿ��գ������ɵ�rawheap��ʽ�ļ���ʹ��Promise�첽�ص���ɡ����ļ���ͨ��rawheap-translator����ת��Ϊheapsnapshot��ʽ�ļ����н�����

> **ע��**
> 
> ϵͳͨ���ýӿ�ת����ջ����Ĵ�����Դ������ϸ������˵���Ƶ�ʺʹ��������������ɵ��ļ���������ɾ����
> 
> �����ڿ�����ģʽ�µ��øýӿڣ����������������ƣ������õĿ�����ѡ��ش򿪲������豸�󼴿���Ч��

**Since:** 18

**ArkTS mode:** ArkTS-Dyn since version 18; ArkTS-Sta since version 26.1.0.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-hidebug-function dumpJsRawHeapData(needGC?: boolean): Promise<string>--><!--Device-hidebug-function dumpJsRawHeapData(needGC?: boolean): Promise<string>-End-->

**System capability:** SystemCapability.HiviewDFX.HiProfiler.HiDebug

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| needGC | boolean | No | ת���ѿ���ǰ�Ƿ���ҪGC��true����ҪGC��false������GC��Ĭ��ֵ��true�� |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;string&gt; | Promise���󣬷������ɵĿ����ļ�·���� |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 11400109 | Timeout while waiting for the child process to finish. |
| 11400108 | Failed to wait for the child process to finish. |
| 11400111 | Napi interface call exception. |
| 11400110 | Disk remaining space too low. |
| 11400107 | Fork operation failed. |
| 11400106 | Quota exceeded. |
| 11400113 | Failed to create dump file. |
| 11400112 | Repeated data dump. |

## Examples

```TypeScript
import { hidebug } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';
hidebug.dumpJsRawHeapData().then((filePath: string) => {
  console.info(`dumpJsRawHeapData success and generated file path is ${filePath}`)
}).catch((error: BusinessError) => {
  console.error(`error code: ${error.code}, error msg: ${error.message}`);
})
```


## dumpJsRawHeapData

```TypeScript
function dumpJsRawHeapData(needGC: boolean, needClean: boolean): Promise<string>
```

Ϊ��ǰ�߳�ת���������ԭʼ�ѿ��գ���֧�����nodeId���档���ɵ��ļ�Ϊrawheap��ʽ��ʹ��Promise�첽�ص���ɡ����ļ���ͨ��rawheap-translator����ת��Ϊheapsnapshot��ʽ�ļ����н�����

> **ע��**
> 
> ϵͳͨ���ýӿ�ת����ջ����Ĵ�����Դ������ϸ������˵���Ƶ�ʺʹ��������������ɵ��ļ���������ɾ����
> 
> �����ڿ�����ģʽ�µ��øýӿڣ����������������ƣ������õĿ�����ѡ��ش򿪲������豸�󼴿���Ч��

**Since:** 24

**ArkTS mode:** ArkTS-Dyn since version 24; ArkTS-Sta since version 26.1.0.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 24.

<!--Device-hidebug-function dumpJsRawHeapData(needGC: boolean, needClean: boolean): Promise<string>--><!--Device-hidebug-function dumpJsRawHeapData(needGC: boolean, needClean: boolean): Promise<string>-End-->

**System capability:** SystemCapability.HiviewDFX.HiProfiler.HiDebug

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| needGC | boolean | Yes | ת���ѿ���ǰ�Ƿ���ҪGC��true����ҪGC��false������ҪGC�� |
| needClean | boolean | Yes | ת���ѿ���ǰ�Ƿ���Ҫ���nodeId��true����Ҫ�����false������Ҫ����� |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;string&gt; | Promise���󣬷������ɵĿ����ļ�·���� |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 11400109 | Timeout while waiting for the child process to finish. |
| 11400108 | Failed to wait for the child process to finish. |
| 11400111 | Napi interface call exception. |
| 11400110 | Disk remaining space too low. |
| 11400107 | Fork operation failed. |
| 11400106 | Quota exceeded. |
| 11400113 | Failed to create dump file. |
| 11400112 | Repeated data dump. |

## Examples

```TypeScript
import { hidebug } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

hidebug.dumpJsRawHeapData(true, true).then((filePath: string) => {
  console.info(`dumpJsRawHeapData success and generated file path is ${filePath}`);
}).catch((error: BusinessError) => {
  console.error(`error code: ${error.code}, error msg: ${error.message}`);
})
```


## dumpJsRawHeapData

```TypeScript
function dumpJsRawHeapData(needGC: boolean, needClean: boolean, processDump: boolean): Promise<Array<string>>
```

Ϊ��ǰ�̻߳����������������������ԭʼ�ѿ��գ���֧�����nodeId���棬���ɵ��ļ�Ϊrawheap��ʽ��ʹ��Promise�첽�ص����ļ���ͨ��rawheap-translator����ת��Ϊheapsnapshot��ʽ�ļ����н�����

> **ע��**
> 
> ϵͳͨ���ýӿ�ת�����ջ����Ĵ�����Դ������ϸ������˵���Ƶ�ʺʹ��������������ɵ��ļ���������ɾ����
> 
> �����ڿ�����ģʽ�µ��øýӿڣ����������������ƣ������õĿ�����ѡ��ش򿪲������豸�󼴿���Ч��

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-hidebug-function dumpJsRawHeapData(needGC: boolean, needClean: boolean, processDump: boolean): Promise<Array<string>>--><!--Device-hidebug-function dumpJsRawHeapData(needGC: boolean, needClean: boolean, processDump: boolean): Promise<Array<string>>-End-->

**System capability:** SystemCapability.HiviewDFX.HiProfiler.HiDebug

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| needGC | boolean | Yes | ת���ѿ���ǰ�Ƿ���ҪGC��true����ҪGC��false������ҪGC�� |
| needClean | boolean | Yes | ת���ѿ���ǰ�Ƿ���Ҫ���nodeId��true����Ҫ�����false������Ҫ����� |
| processDump | boolean | Yes | �Ƿ�ת����ǰ�߳��������̵�ԭʼ�ѿ��ա�true��ת����ǰ�߳��������̵�ԭʼ�ѿ��ա� |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;Array&lt;string&gt;&gt; | Promise���󣬷������ɵĿ����ļ�·�����顣 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 11400109 | Timeout while waiting for the child process to finish. |
| 11400108 | Failed to wait for the child process to finish. |
| 11400111 | Napi interface call exception. |
| 11400110 | Disk remaining space too low. |
| 11400107 | Fork operation failed. |
| 11400106 | Quota exceeded. |
| 11400113 | Failed to create dump file. |
| 11400112 | Repeated data dump. |

## Examples

```TypeScript
import { hidebug } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

hidebug.dumpJsRawHeapData(true, true, true).then((filePathArray: Array<string>) => {
  console.info(`dumpJsRawHeapData success and generated file path is ${JSON.stringify(filePathArray)}`);
}).catch((error: BusinessError) => {
  console.error(`error code: ${error.code}, error msg: ${error.message}`);
})
```

