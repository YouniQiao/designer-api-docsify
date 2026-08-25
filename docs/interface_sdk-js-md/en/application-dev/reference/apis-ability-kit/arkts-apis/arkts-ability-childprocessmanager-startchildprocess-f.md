# startChildProcess

## Modules to Import

```TypeScript
import { childProcessManager } from 'kits/@kit.AbilityKit';
```

## startChildProcess

```TypeScript
function startChildProcess(srcEntry: string, startMode: StartMode): Promise<number>
```

Starts an [ArkTS child process](../../../application-models/ability-terminology.md#arkts-child-process). This API uses a promise to return the result. This API can be properly called on PCs/2-in-1 devices and tablets. If it is called on other devices, error code 160 00061 is returned.

> **NOTE：**&gt;
> If the child process is created successfully, its PID is returned, and its
> [ChildProcess.onStart](arkts-ability-app-ability-childprocess-childprocess-c.md#onstart) function is executed. Once the
> function is done, the child process is automatically destroyed.&gt;
> The child process started by calling this API does not support asynchronous ArkTS API calls. It supports only
> synchronous ArkTS API calls.

**Since:** 11

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [srcEntry](arkts-ability-insightintentdriver-subintentinfoforconfiguration-i-sys.md) | string | Yes |
| startMode | [StartMode](arkts-ability-childprocessmanager-startmode-e.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;number & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [16000050](../errorcode-ability.md#16000050-internal-error) |
| [16000061](../errorcode-ability.md#16000061-unsupported-operation) |
| [16000062](../errorcode-ability.md#16000062-too-many-child-processes) |


## startChildProcess

```TypeScript
function startChildProcess(srcEntry: string, startMode: StartMode, callback: AsyncCallback<number>): void
```

Starts an [ArkTS child process](../../../application-models/ability-terminology.md#arkts-child-process). This API uses an asynchronous callback to return the result. This API can be properly called on PCs/2-in-1 devices and tablets. If it is called on other devices, error code 160 00061 is returned.

> **NOTE：**&gt;
> If the child process is created successfully, its PID is returned, and its
> [ChildProcess.onStart](arkts-ability-app-ability-childprocess-childprocess-c.md#onstart) function is executed. Once the
> function is done, the child process is automatically destroyed.&gt;
> The child process started by calling this API does not support asynchronous ArkTS API calls. It supports only
> synchronous ArkTS API calls.

**Since:** 11

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [srcEntry](arkts-ability-insightintentdriver-subintentinfoforconfiguration-i-sys.md) | string | Yes |
| startMode | [StartMode](arkts-ability-childprocessmanager-startmode-e.md) | Yes |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;number&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [16000050](../errorcode-ability.md#16000050-internal-error) |
| [16000061](../errorcode-ability.md#16000061-unsupported-operation) |
| [16000062](../errorcode-ability.md#16000062-too-many-child-processes) |
