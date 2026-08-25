# downloadFile

## Modules to Import

```TypeScript
import { request } from 'kits/@kit.BasicServicesKit';
```

## downloadFile

```TypeScript
function downloadFile(context: BaseContext, config: DownloadConfig, callback: AsyncCallback<DownloadTask>): void
```

Downloads a file. This API uses an asynchronous callback to return the result. HTTP is supported. You can use on('complete'|'pause'|'remove') to obtain the download task state, including task completion, pause, and removal. You can also use on('fail') to obtain the task download error information.

> **NOTE：**&gt;
> For details about how to obtain the context in the example, see
> [Obtaining the Context of UIAbility](../../../application-models/uiability-usage.md#obtaining-the-context-of-uiability)
> .

**Since:** 9

**Required permissions:** ohos.permission.INTERNET

**System capability:** SystemCapability.MiscServices.Download

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| context | [BaseContext](../../apis-ability-kit/arkts-apis/arkts-ability-basecontext-c.md) | Yes |
| config | [DownloadConfig](arkts-basicservices-request-downloadconfig-i.md) | Yes |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;[DownloadTask](arkts-basicservices-request-downloadtask-i.md)&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [13400001](../errorcode-request.md#13400001-file-operation-error) |
| [13400002](../errorcode-request.md#13400002-file-path-error) |
| [13400003](../errorcode-request.md#13400003-service-error) |


## downloadFile

```TypeScript
function downloadFile(context: BaseContext, config: DownloadConfig): Promise<DownloadTask>
```

Downloads a file. This API uses a promise to return the result. HTTP is supported. You can use on('complete'|'pause'|'remove') to obtain the download task state, including task completion, pause, and removal. You can also use on('fail') to obtain the task download error information.

> **NOTE：**&gt;
> For details about how to obtain the context in the example, see
> [Obtaining the Context of UIAbility](../../../application-models/uiability-usage.md#obtaining-the-context-of-uiability)
> .

**Since:** 9

**Required permissions:** ohos.permission.INTERNET

**System capability:** SystemCapability.MiscServices.Download

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| context | [BaseContext](../../apis-ability-kit/arkts-apis/arkts-ability-basecontext-c.md) | Yes |
| config | [DownloadConfig](arkts-basicservices-request-downloadconfig-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[DownloadTask](arkts-basicservices-request-downloadtask-i.md)&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [13400001](../errorcode-request.md#13400001-file-operation-error) |
| [13400002](../errorcode-request.md#13400002-file-path-error) |
| [13400003](../errorcode-request.md#13400003-service-error) |
