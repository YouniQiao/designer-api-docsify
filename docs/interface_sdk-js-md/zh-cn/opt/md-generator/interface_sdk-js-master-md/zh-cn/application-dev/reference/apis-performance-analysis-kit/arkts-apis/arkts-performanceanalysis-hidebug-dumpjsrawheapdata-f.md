# dumpJsRawHeapData

## 导入模块

```TypeScript
```

## dumpJsRawHeapData

```TypeScript
function dumpJsRawHeapData(needGC?: boolean): Promise<string>
```

为当前线程转储虚拟机的原始堆快照，并生成的rawheap格式文件，使用Promise异步回调完成。该文件可通过rawheap-translator工具转化为heapsnapshot格式文件进行解析。 > **注意** > > 系统通过该接口转存快照会消耗大量资源，因此严格限制了调用频率和次数。处理完生成的文件后，请立即删除。 > > 建议在开发者模式下调用该接口，可免除调用配额限制，当设置的开发者选项开关打开并重启设备后即可生效。

**起始版本：** 26.1.0

**原子化服务API：** 从API版本26.1.0开始，该接口支持在原子化服务API中使用。

<!--Device-hidebug-function dumpJsRawHeapData(needGC?: boolean): Promise<string>--><!--Device-hidebug-function dumpJsRawHeapData(needGC?: boolean): Promise<string>-End-->

**系统能力：** SystemCapability.HiviewDFX.HiProfiler.HiDebug

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| needGC | boolean | 否 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;string & gt; |

**错误码：**

| 错误码ID |
| --- |
| [11400109](../errorcode-hiviewdfx-hidebug.md#11400109-等待dump子进程超时) |
| [11400108](../errorcode-hiviewdfx-hidebug.md#11400108-等待dump子进程结束失败) |
| [11400111](../errorcode-hiviewdfx-hidebug.md#11400111-napi接口调用失败) |
| [11400110](../errorcode-hiviewdfx-hidebug.md#11400110-磁盘空间不足) |
| [11400107](../errorcode-hiviewdfx-hidebug.md#11400107-dump子进程fork失败) |
| [11400106](../errorcode-hiviewdfx-hidebug-trace.md#11400106-接口调用配额已超出) |
| [11400113](../errorcode-hiviewdfx-hidebug.md#11400113-创建dump文件失败) |
| [11400112](../errorcode-hiviewdfx-hidebug.md#11400112-重复dump采集) |

**示例**

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

为当前线程转储虚拟机的原始堆快照，并支持清除nodeId缓存。生成的文件为rawheap格式，使用Promise异步回调完成。该文件可通过rawheap-translator工具转化为heapsnapshot格式文件进行解析。 > **注意** > > 系统通过该接口转存快照会消耗大量资源，因此严格限制了调用频率和次数。处理完生成的文件后，请立即删除。 > > 建议在开发者模式下调用该接口，可免除调用配额限制，当设置的开发者选项开关打开并重启设备后即可生效。

**起始版本：** 26.1.0

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.1.0开始，该接口支持在原子化服务API中使用。

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
| Promise & lt;string & gt; |

**错误码：**

| 错误码ID |
| --- |
| [11400109](../errorcode-hiviewdfx-hidebug.md#11400109-等待dump子进程超时) |
| [11400108](../errorcode-hiviewdfx-hidebug.md#11400108-等待dump子进程结束失败) |
| [11400111](../errorcode-hiviewdfx-hidebug.md#11400111-napi接口调用失败) |
| [11400110](../errorcode-hiviewdfx-hidebug.md#11400110-磁盘空间不足) |
| [11400107](../errorcode-hiviewdfx-hidebug.md#11400107-dump子进程fork失败) |
| [11400106](../errorcode-hiviewdfx-hidebug-trace.md#11400106-接口调用配额已超出) |
| [11400113](../errorcode-hiviewdfx-hidebug.md#11400113-创建dump文件失败) |
| [11400112](../errorcode-hiviewdfx-hidebug.md#11400112-重复dump采集) |

**示例**

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

为当前线程或其所属进程生成虚拟机的原始堆快照，并支持清除nodeId缓存，生成的文件为rawheap格式。使用Promise异步回调。文件可通过rawheap-translator工具转换为heapsnapshot格式文件进行解析。 > **注意** > > 系统通过该接口转储快照会消耗大量资源，因此严格限制了调用频率和次数。处理完生成的文件后，请立即删除。 > > 建议在开发者模式下调用该接口，可免除调用配额限制，当设置的开发者选项开关打开并重启设备后即可生效。

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
| Promise & lt;Array & lt;string & gt; & gt; |

**错误码：**

| 错误码ID |
| --- |
| [11400109](../errorcode-hiviewdfx-hidebug.md#11400109-等待dump子进程超时) |
| [11400108](../errorcode-hiviewdfx-hidebug.md#11400108-等待dump子进程结束失败) |
| [11400111](../errorcode-hiviewdfx-hidebug.md#11400111-napi接口调用失败) |
| [11400110](../errorcode-hiviewdfx-hidebug.md#11400110-磁盘空间不足) |
| [11400107](../errorcode-hiviewdfx-hidebug.md#11400107-dump子进程fork失败) |
| [11400106](../errorcode-hiviewdfx-hidebug-trace.md#11400106-接口调用配额已超出) |
| [11400113](../errorcode-hiviewdfx-hidebug.md#11400113-创建dump文件失败) |
| [11400112](../errorcode-hiviewdfx-hidebug.md#11400112-重复dump采集) |

**示例**

```TypeScript
import { hidebug } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

hidebug.dumpJsRawHeapData(true, true, true).then((filePathArray: Array<string>) => {
  console.info(`dumpJsRawHeapData success and generated file path is ${JSON.stringify(filePathArray)}`);
}).catch((error: BusinessError) => {
  console.error(`error code: ${error.code}, error msg: ${error.message}`);
})
```
