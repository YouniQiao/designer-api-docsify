# dumpJsRawHeapData

## Modules to Import

```TypeScript
import { hidebug } from 'kits/@kit.PerformanceAnalysisKit';
```

## dumpJsRawHeapData

```TypeScript
function dumpJsRawHeapData(needGC?: boolean): Promise<string>
```

Dumps the original heap snapshot of the VM for the current thread and generates a .rawheap file. This API uses a promise to return the result. The file can be converted into a heapsnapshot file using rawheap-translator for parsing.

> **NOTE：**
> 
> This API is resource-consuming. Therefore, the calling frequency and times are strictly limited. You need to
> delete the files immediately after processing them.
> 
> This API is valid only when the **Developer options** is enabled.

**Since:** 18

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-hidebug-function dumpJsRawHeapData(needGC?: boolean): Promise<string>--><!--Device-hidebug-function dumpJsRawHeapData(needGC?: boolean): Promise<string>-End-->

**System capability:** SystemCapability.HiviewDFX.HiProfiler.HiDebug

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| needGC | boolean | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;string&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [11400109](../errorcode-hiviewdfx-hidebug.md#11400109-waiting-for-the-child-dump-process-times-out) |
| [11400108](../errorcode-hiviewdfx-hidebug.md#11400108-failed-to-wait-for-the-child-dump-process-to-finish) |
| [11400111](../errorcode-hiviewdfx-hidebug.md#11400111-failed-to-call-the-nodeapi) |
| [11400110](../errorcode-hiviewdfx-hidebug.md#11400110-insufficient-disk-space) |
| [11400107](../errorcode-hiviewdfx-hidebug.md#11400107-failed-to-fork-the-child-dump-process) |
| [11400106](../errorcode-hiviewdfx-hidebug.md#11400106-quota-exceeded) |
| [11400113](../errorcode-hiviewdfx-hidebug.md#11400113-failed-to-create-a-dump-file) |
| [11400112](../errorcode-hiviewdfx-hidebug.md#11400112-repeated-data-dump) |

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

Dumps the original heap snapshot of the VM for the current thread. The API uses a promise to return the path of the.rawheap file. You can use rawheap-translator to convert the generated file into a .heapsnapshot file for parsing.The generated file will be stored in a folder within the application directory. However, since this file is usually large, the system imposes restrictions on the frequency and number of calls to this function. Consequently, you might fail to obtain the dump file due to quota limitations. These failures will persist until the quota is regularly refreshed by the system. Therefore, it is advisable to delete the file immediately after you have finished processing it. Moreover, it is recommended that you use this function in the gray - release version.

**Since:** 24

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 24.

<!--Device-hidebug-function dumpJsRawHeapData(needGC: boolean, needClean: boolean): Promise<string>--><!--Device-hidebug-function dumpJsRawHeapData(needGC: boolean, needClean: boolean): Promise<string>-End-->

**System capability:** SystemCapability.HiviewDFX.HiProfiler.HiDebug

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| needGC | boolean | Yes |
| needClean | boolean | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;string&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [11400109](../errorcode-hiviewdfx-hidebug.md#11400109-waiting-for-the-child-dump-process-times-out) |
| [11400108](../errorcode-hiviewdfx-hidebug.md#11400108-failed-to-wait-for-the-child-dump-process-to-finish) |
| [11400111](../errorcode-hiviewdfx-hidebug.md#11400111-failed-to-call-the-nodeapi) |
| [11400110](../errorcode-hiviewdfx-hidebug.md#11400110-insufficient-disk-space) |
| [11400107](../errorcode-hiviewdfx-hidebug.md#11400107-failed-to-fork-the-child-dump-process) |
| [11400106](../errorcode-hiviewdfx-hidebug.md#11400106-quota-exceeded) |
| [11400113](../errorcode-hiviewdfx-hidebug.md#11400113-failed-to-create-a-dump-file) |
| [11400112](../errorcode-hiviewdfx-hidebug.md#11400112-repeated-data-dump) |

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

Dump the raw heap snapshot of the JavaScript Virtual Machine for the current thread.

The generated file will be stored in a folder within the application directory. However, since this file is usually large, the system imposes restrictions on the frequency and number of calls to this function. Consequently, you might fail to obtain the dump file due to quota limitations. These failures will persist until the quota is regularly refreshed by the system. Therefore, it is advisable to delete the file immediately after you have finished processing it. Moreover, it is recommended that you use this function in the gray - release version.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-hidebug-function dumpJsRawHeapData(needGC: boolean, needClean: boolean, processDump: boolean): Promise<Array<string>>--><!--Device-hidebug-function dumpJsRawHeapData(needGC: boolean, needClean: boolean, processDump: boolean): Promise<Array<string>>-End-->

**System capability:** SystemCapability.HiviewDFX.HiProfiler.HiDebug

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| needGC | boolean | Yes |
| needClean | boolean | Yes |
| processDump | boolean | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;Array&lt;string&gt;&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [11400109](../errorcode-hiviewdfx-hidebug.md#11400109-waiting-for-the-child-dump-process-times-out) |
| [11400108](../errorcode-hiviewdfx-hidebug.md#11400108-failed-to-wait-for-the-child-dump-process-to-finish) |
| [11400111](../errorcode-hiviewdfx-hidebug.md#11400111-failed-to-call-the-nodeapi) |
| [11400110](../errorcode-hiviewdfx-hidebug.md#11400110-insufficient-disk-space) |
| [11400107](../errorcode-hiviewdfx-hidebug.md#11400107-failed-to-fork-the-child-dump-process) |
| [11400106](../errorcode-hiviewdfx-hidebug.md#11400106-quota-exceeded) |
| [11400113](../errorcode-hiviewdfx-hidebug.md#11400113-failed-to-create-a-dump-file) |
| [11400112](../errorcode-hiviewdfx-hidebug.md#11400112-repeated-data-dump) |

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
