# dumpJsHeapData

## dumpJsHeapData

```TypeScript
function dumpJsHeapData(filename : string) : void
```

�����������ת����

> **ע��**
> 
> ����������ѵ��������ʱ���Ҹýӿ�Ϊͬ���ӿڣ����鲻Ҫ���ϼܰ汾�е��øýӿڣ��Ա���Ӧ�ö�����Ӱ���û����顣

**起始版本：** 9

<!--Device-hidebug-function dumpJsHeapData(filename : string) : void--><!--Device-hidebug-function dumpJsHeapData(filename : string) : void-End-->

**系统能力：** SystemCapability.HiviewDFX.HiProfiler.HiDebug

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| filename | string | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |

## 示例

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

**起始版本：** 24

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本24开始，该接口支持在原子化服务API中使用。

<!--Device-hidebug-function dumpJsHeapData(filename: string, needClean: boolean): void--><!--Device-hidebug-function dumpJsHeapData(filename: string, needClean: boolean): void-End-->

**系统能力：** SystemCapability.HiviewDFX.HiProfiler.HiDebug

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| filename | string | 是 |
| needClean | boolean | 是 |

## 示例

```TypeScript
import { hidebug } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  hidebug.dumpJsHeapData("heapData", true);
} catch (error) {
  console.error(`error code: ${(error as BusinessError).code}, error msg: ${(error as BusinessError).message}`);
}
```
