# dumpJsRawHeapData

## 导入模块

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

**起始版本：** 18

**ArkTS模式：** ArkTS-Dyn起始版本为18；ArkTS-Sta起始版本为26.1.0。

**原子化服务API：** 从API版本18开始，该接口支持在原子化服务API中使用。

<!--Device-hidebug-function dumpJsRawHeapData(needGC?: boolean): Promise<string>--><!--Device-hidebug-function dumpJsRawHeapData(needGC?: boolean): Promise<string>-End-->

**系统能力：** SystemCapability.HiviewDFX.HiProfiler.HiDebug

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| needGC | boolean | 否 | ת���ѿ���ǰ�Ƿ���ҪGC��true����ҪGC��false������GC��Ĭ��ֵ��true�� |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;string&gt; | Promise���󣬷������ɵĿ����ļ�·���� |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 11400109 | Timeout while waiting for the child process to finish. |
| 11400108 | Failed to wait for the child process to finish. |
| 11400111 | Napi interface call exception. |
| 11400110 | Disk remaining space too low. |
| 11400107 | Fork operation failed. |
| 11400106 | Quota exceeded. |
| 11400113 | Failed to create dump file. |
| 11400112 | Repeated data dump. |

## 示例

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

**起始版本：** 24

**ArkTS模式：** ArkTS-Dyn起始版本为24；ArkTS-Sta起始版本为26.1.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本24开始，该接口支持在原子化服务API中使用。

<!--Device-hidebug-function dumpJsRawHeapData(needGC: boolean, needClean: boolean): Promise<string>--><!--Device-hidebug-function dumpJsRawHeapData(needGC: boolean, needClean: boolean): Promise<string>-End-->

**系统能力：** SystemCapability.HiviewDFX.HiProfiler.HiDebug

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| needGC | boolean | 是 | ת���ѿ���ǰ�Ƿ���ҪGC��true����ҪGC��false������ҪGC�� |
| needClean | boolean | 是 | ת���ѿ���ǰ�Ƿ���Ҫ���nodeId��true����Ҫ�����false������Ҫ����� |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;string&gt; | Promise���󣬷������ɵĿ����ļ�·���� |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 11400109 | Timeout while waiting for the child process to finish. |
| 11400108 | Failed to wait for the child process to finish. |
| 11400111 | Napi interface call exception. |
| 11400110 | Disk remaining space too low. |
| 11400107 | Fork operation failed. |
| 11400106 | Quota exceeded. |
| 11400113 | Failed to create dump file. |
| 11400112 | Repeated data dump. |

## 示例

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

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.0.0开始，该接口支持在原子化服务API中使用。

<!--Device-hidebug-function dumpJsRawHeapData(needGC: boolean, needClean: boolean, processDump: boolean): Promise<Array<string>>--><!--Device-hidebug-function dumpJsRawHeapData(needGC: boolean, needClean: boolean, processDump: boolean): Promise<Array<string>>-End-->

**系统能力：** SystemCapability.HiviewDFX.HiProfiler.HiDebug

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| needGC | boolean | 是 | ת���ѿ���ǰ�Ƿ���ҪGC��true����ҪGC��false������ҪGC�� |
| needClean | boolean | 是 | ת���ѿ���ǰ�Ƿ���Ҫ���nodeId��true����Ҫ�����false������Ҫ����� |
| processDump | boolean | 是 | �Ƿ�ת����ǰ�߳��������̵�ԭʼ�ѿ��ա�true��ת����ǰ�߳��������̵�ԭʼ�ѿ��ա� |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;Array&lt;string&gt;&gt; | Promise���󣬷������ɵĿ����ļ�·�����顣 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 11400109 | Timeout while waiting for the child process to finish. |
| 11400108 | Failed to wait for the child process to finish. |
| 11400111 | Napi interface call exception. |
| 11400110 | Disk remaining space too low. |
| 11400107 | Fork operation failed. |
| 11400106 | Quota exceeded. |
| 11400113 | Failed to create dump file. |
| 11400112 | Repeated data dump. |

## 示例

```TypeScript
import { hidebug } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

hidebug.dumpJsRawHeapData(true, true, true).then((filePathArray: Array<string>) => {
  console.info(`dumpJsRawHeapData success and generated file path is ${JSON.stringify(filePathArray)}`);
}).catch((error: BusinessError) => {
  console.error(`error code: ${error.code}, error msg: ${error.message}`);
})
```

