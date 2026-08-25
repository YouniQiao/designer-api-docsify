# copy (System API)

## Modules to Import

```TypeScript
import { logLibrary } from 'kits/@kit.PerformanceAnalysisKit';
```

## copy

```TypeScript
function copy(logType: string, logName: string, dest: string): Promise<void>
```

Copies log files of the specified type to the target application directory. This API uses a promise to return the result.

**Since:** 10

**Required permissions:** ohos.permission.READ_HIVIEW_SYSTEM

**System capability:** SystemCapability.HiviewDFX.Hiview.LogLibrary

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| logType | string | Yes |
| logName | string | Yes |
| dest | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [21300001](../errorcode-loglibrary-sys.md#21300001-specified-file-not-exist) |


## copy

```TypeScript
function copy(logType: string, logName: string, dest: string, callback: AsyncCallback<void>): void
```

Copies log files of the specified type to the target application directory. This API uses an asynchronous callback to return the result.

**Since:** 10

**Required permissions:** ohos.permission.READ_HIVIEW_SYSTEM

**System capability:** SystemCapability.HiviewDFX.Hiview.LogLibrary

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| logType | string | Yes |
| logName | string | Yes |
| dest | string | Yes |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [21300001](../errorcode-loglibrary-sys.md#21300001-specified-file-not-exist) |
