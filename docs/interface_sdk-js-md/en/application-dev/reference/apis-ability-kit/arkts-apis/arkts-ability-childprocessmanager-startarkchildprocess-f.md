# startArkChildProcess

## Modules to Import

```TypeScript
import { childProcessManager } from 'kits/@kit.AbilityKit';
```

## startArkChildProcess

```TypeScript
function startArkChildProcess(srcEntry: string, args: ChildProcessArgs, options?: ChildProcessOptions): Promise<number>
```

Starts an [ArkTS child process](../../../application-models/ability-terminology.md#arkts-child-process). This API uses a promise to return the result. This API can be properly called on PCs/2-in-1 devices and tablets. If it is called on other devices, error code 801 is returned.

> **NOTE：**&gt;
> The child process started by calling this API does not inherit the resources of the parent process. If the child
> process is created successfully, its PID is returned, and its
> [ChildProcess.onStart](arkts-ability-app-ability-childprocess-childprocess-c.md#onstart) function is executed. After the
> function is done, the child process is not automatically destroyed. Instead, it must be destroyed by calling
> [process.abort](../../apis-arkts/arkts-apis/arkts-arkts-process-abort-f.md). After the process that calls this API is destroyed, the
> created child process is also destroyed.

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [srcEntry](arkts-ability-insightintentdriver-subintentinfoforconfiguration-i-sys.md) | string | Yes |
| [args](../../apis-arkdata/arkts-apis/arkts-arkdata-relationalstore-sqlinfo-i.md) | [ChildProcessArgs](arkts-ability-app-ability-childprocessargs-childprocessargs-i.md) | Yes |
| options | [ChildProcessOptions](arkts-ability-app-ability-childprocessoptions-childprocessoptions-i.md) | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;number & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [16000050](../errorcode-ability.md#16000050-internal-error) |
| [16000061](../errorcode-ability.md#16000061-unsupported-operation) |
| [16000062](../errorcode-ability.md#16000062-too-many-child-processes) |
