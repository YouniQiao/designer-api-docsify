# dumpJsRawHeapData

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

**原子化服务API：** 从API版本18开始，该接口支持在原子化服务API中使用。

<!--Device-hidebug-function dumpJsRawHeapData(needGC?: boolean): Promise<string>--><!--Device-hidebug-function dumpJsRawHeapData(needGC?: boolean): Promise<string>-End-->

**系统能力：** SystemCapability.HiviewDFX.HiProfiler.HiDebug

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| needGC | boolean | 否 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;string&gt; |

**错误码：**

| 错误码ID |
| --- |
| [11400109](../errorcode-hiviewdfx-hidebug.md#11400109-等待dump子进程超时) |
| [11400108](../errorcode-hiviewdfx-hidebug.md#11400108-等待dump子进程结束失败) |
| [11400111](../errorcode-hiviewdfx-hidebug.md#11400111-napi接口调用失败) |
| [11400110](../errorcode-hiviewdfx-hidebug.md#11400110-磁盘空间不足) |
| [11400107](../errorcode-hiviewdfx-hidebug.md#11400107-dump子进程fork失败) |
| [11400106](../errorcode-hiviewdfx-hidebug.md#11400106-配额超限) |
| [11400113](../errorcode-hiviewdfx-hidebug.md#11400113-创建dump文件失败) |
| [11400112](../errorcode-hiviewdfx-hidebug.md#11400112-重复dump采集) |

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

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本24开始，该接口支持在原子化服务API中使用。

<!--Device-hidebug-function dumpJsRawHeapData(needGC: boolean, needClean: boolean): Promise<string>--><!--Device-hidebug-function dumpJsRawHeapData(needGC: boolean, needClean: boolean): Promise<string>-End-->

**系统能力：** SystemCapability.HiviewDFX.HiProfiler.HiDebug

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| needGC | boolean | 是 |
| needClean | boolean | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;string&gt; |

**错误码：**

| 错误码ID |
| --- |
| [11400109](../errorcode-hiviewdfx-hidebug.md#11400109-等待dump子进程超时) |
| [11400108](../errorcode-hiviewdfx-hidebug.md#11400108-等待dump子进程结束失败) |
| [11400111](../errorcode-hiviewdfx-hidebug.md#11400111-napi接口调用失败) |
| [11400110](../errorcode-hiviewdfx-hidebug.md#11400110-磁盘空间不足) |
| [11400107](../errorcode-hiviewdfx-hidebug.md#11400107-dump子进程fork失败) |
| [11400106](../errorcode-hiviewdfx-hidebug.md#11400106-配额超限) |
| [11400113](../errorcode-hiviewdfx-hidebug.md#11400113-创建dump文件失败) |
| [11400112](../errorcode-hiviewdfx-hidebug.md#11400112-重复dump采集) |

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

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.0.0开始，该接口支持在原子化服务API中使用。

<!--Device-hidebug-function dumpJsRawHeapData(needGC: boolean, needClean: boolean, processDump: boolean): Promise<Array<string>>--><!--Device-hidebug-function dumpJsRawHeapData(needGC: boolean, needClean: boolean, processDump: boolean): Promise<Array<string>>-End-->

**系统能力：** SystemCapability.HiviewDFX.HiProfiler.HiDebug

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| needGC | boolean | 是 |
| needClean | boolean | 是 |
| processDump | boolean | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;Array&lt;string&gt;&gt; |

**错误码：**

| 错误码ID |
| --- |
| [11400109](../errorcode-hiviewdfx-hidebug.md#11400109-等待dump子进程超时) |
| [11400108](../errorcode-hiviewdfx-hidebug.md#11400108-等待dump子进程结束失败) |
| [11400111](../errorcode-hiviewdfx-hidebug.md#11400111-napi接口调用失败) |
| [11400110](../errorcode-hiviewdfx-hidebug.md#11400110-磁盘空间不足) |
| [11400107](../errorcode-hiviewdfx-hidebug.md#11400107-dump子进程fork失败) |
| [11400106](../errorcode-hiviewdfx-hidebug.md#11400106-配额超限) |
| [11400113](../errorcode-hiviewdfx-hidebug.md#11400113-创建dump文件失败) |
| [11400112](../errorcode-hiviewdfx-hidebug.md#11400112-重复dump采集) |

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
