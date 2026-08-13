# create

## Modules to Import

```TypeScript
import { request } from '@kit.BasicServicesKit';
```

## create

```TypeScript
function create(context: BaseContext, config: Config, callback: AsyncCallback<Task>): void
```

Creates an upload or download task and adds it to the queue. This API uses an asynchronous callback to return the result. HTTP/HTTPS is supported. > **NOTE：**> > For details about how to obtain the context in the example, see > [Obtaining the Context of UIAbility](../../../application-models/uiability-usage.md#obtaining-the-context-of-uiability) > .

**Since:** 23

**Deprecated since:** -1

**Required permissions:** ohos.permission.INTERNET

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-agent-function create(context: BaseContext, config: Config, callback: AsyncCallback<Task>): void--><!--Device-agent-function create(context: BaseContext, config: Config, callback: AsyncCallback<Task>): void-End-->

**System capability:** SystemCapability.Request.FileTransferAgent

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| context | [BaseContext](../../apis-ability-kit/arkts-apis/arkts-ability-basecontext-c.md) | Yes |
| config | [Config](arkts-basicservices-agent-config-i.md) | Yes |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;Task&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [21900004](../../apis-basic-services-kit/errorcode-request.md#21900004-application-task-queue-full) |
| [21900005](../../apis-basic-services-kit/errorcode-request.md#21900005-task-mode-error) |
| [13400001](../../apis-basic-services-kit/errorcode-request.md#13400001-file-operation-error) |
| [13400003](../../apis-basic-services-kit/errorcode-request.md#13400003-service-error) |


## create

```TypeScript
function create(context: BaseContext, config: Config): Promise<Task>
```

Creates an upload or download task and adds it to the queue. This API uses a promise to return the result. HTTP/ HTTPS is supported. > **NOTE：**> > For details about how to obtain the context in the example, see > [Obtaining the Context of UIAbility](../../../application-models/uiability-usage.md#obtaining-the-context-of-uiability) > .

**Since:** 23

**Deprecated since:** -1

**Required permissions:** ohos.permission.INTERNET

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-agent-function create(context: BaseContext, config: Config): Promise<Task>--><!--Device-agent-function create(context: BaseContext, config: Config): Promise<Task>-End-->

**System capability:** SystemCapability.Request.FileTransferAgent

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| context | [BaseContext](../../apis-ability-kit/arkts-apis/arkts-ability-basecontext-c.md) | Yes |
| config | [Config](arkts-basicservices-agent-config-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;Task & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [21900004](../../apis-basic-services-kit/errorcode-request.md#21900004-application-task-queue-full) |
| [21900005](../../apis-basic-services-kit/errorcode-request.md#21900005-task-mode-error) |
| [13400001](../../apis-basic-services-kit/errorcode-request.md#13400001-file-operation-error) |
| [13400003](../../apis-basic-services-kit/errorcode-request.md#13400003-service-error) |
