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

> **NOTE：**&gt;
> This API is resource-consuming. Therefore, the calling frequency and times are strictly limited. You need to
> delete the files immediately after processing them.&gt;
> You are advised to enable **Developer options** before calling this API, so that the calling quota is not
> limited. The setting takes effect after the device is restarted.

**Since:** 18

**Atomic service API:** This API can be used in atomic services since API version 18.

**System capability:** SystemCapability.HiviewDFX.HiProfiler.HiDebug

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| needGC | boolean | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;string & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [11400106](../errorcode-hiviewdfx-hidebug-trace.md#11400106-api-call-quota-exceeded) |
| [11400107](../errorcode-hiviewdfx-hidebug.md#11400107-failed-to-fork-the-child-dump-process) |
| [11400108](../errorcode-hiviewdfx-hidebug.md#11400108-failed-to-wait-for-the-child-dump-process-to-finish) |
| [11400109](../errorcode-hiviewdfx-hidebug.md#11400109-waiting-for-the-child-dump-process-times-out) |
| [11400110](../errorcode-hiviewdfx-hidebug.md#11400110-insufficient-disk-space) |
| [11400111](../errorcode-hiviewdfx-hidebug.md#11400111-failed-to-call-the-node-api) |
| [11400112](../errorcode-hiviewdfx-hidebug.md#11400112-repeated-data-dump) |
| [11400113](../errorcode-hiviewdfx-hidebug.md#11400113-failed-to-create-a-dump-file) |


## dumpJsRawHeapData

```TypeScript
function dumpJsRawHeapData(needGC: boolean, needClean: boolean): Promise<string>
```

Dumps the original heap snapshot of the VM for the current thread and clears the **nodeId** cache. The generated file is in the rawheap format. This API uses a promise to return the result. The file can be converted into a heapsnapshot file using rawheap-translator for parsing.

> **NOTE：**&gt;
> This API is resource-consuming. Therefore, the calling frequency and times are strictly limited. You need to
> delete the files immediately after processing them.&gt;
> You are advised to enable **Developer options** before calling this API, so that the calling quota is not
> limited. The setting takes effect after the device is restarted.

**Since:** 24

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 24.

**System capability:** SystemCapability.HiviewDFX.HiProfiler.HiDebug

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| needGC | boolean | Yes |
| needClean | boolean | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;string & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [11400106](../errorcode-hiviewdfx-hidebug-trace.md#11400106-api-call-quota-exceeded) |
| [11400107](../errorcode-hiviewdfx-hidebug.md#11400107-failed-to-fork-the-child-dump-process) |
| [11400108](../errorcode-hiviewdfx-hidebug.md#11400108-failed-to-wait-for-the-child-dump-process-to-finish) |
| [11400109](../errorcode-hiviewdfx-hidebug.md#11400109-waiting-for-the-child-dump-process-times-out) |
| [11400110](../errorcode-hiviewdfx-hidebug.md#11400110-insufficient-disk-space) |
| [11400111](../errorcode-hiviewdfx-hidebug.md#11400111-failed-to-call-the-node-api) |
| [11400112](../errorcode-hiviewdfx-hidebug.md#11400112-repeated-data-dump) |
| [11400113](../errorcode-hiviewdfx-hidebug.md#11400113-failed-to-create-a-dump-file) |


## dumpJsRawHeapData

```TypeScript
function dumpJsRawHeapData(needGC: boolean, needClean: boolean, processDump: boolean): Promise<Array<string>>
```

Dumps the original heap snapshot of the VM for the current thread or the process to which the current thread belongs, clears the nodeId cache, and generates a .rawheap file. This API uses a promise to return the result. The file can be converted into a heapsnapshot file using rawheap-translator for parsing.

> **NOTE：**&gt;
> This API is resource-consuming. Therefore, the calling frequency and times are strictly limited. You need to
> delete the files immediately after processing them.&gt;
> You are advised to enable **Developer options** before calling this API, so that the calling quota is not
> limited. The setting takes effect after the device is restarted.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

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
| Promise & lt;Array & lt;string & gt; & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [11400106](../errorcode-hiviewdfx-hidebug-trace.md#11400106-api-call-quota-exceeded) |
| [11400107](../errorcode-hiviewdfx-hidebug.md#11400107-failed-to-fork-the-child-dump-process) |
| [11400108](../errorcode-hiviewdfx-hidebug.md#11400108-failed-to-wait-for-the-child-dump-process-to-finish) |
| [11400109](../errorcode-hiviewdfx-hidebug.md#11400109-waiting-for-the-child-dump-process-times-out) |
| [11400110](../errorcode-hiviewdfx-hidebug.md#11400110-insufficient-disk-space) |
| [11400111](../errorcode-hiviewdfx-hidebug.md#11400111-failed-to-call-the-node-api) |
| [11400112](../errorcode-hiviewdfx-hidebug.md#11400112-repeated-data-dump) |
| [11400113](../errorcode-hiviewdfx-hidebug.md#11400113-failed-to-create-a-dump-file) |
