# startNativeChildProcess

## Modules to Import

```TypeScript
import { childProcessManager } from 'kits/@kit.AbilityKit';
```

## startNativeChildProcess

```TypeScript
function startNativeChildProcess(entryPoint: string, args: ChildProcessArgs, options?: ChildProcessOptions): Promise<number>
```

Starts a [native child process](../../../application-models/ability-terminology.md#native-child-process). This API uses a promise to return the result. This API can be properly called on PCs/2-in-1 devices and tablets. If it is called on other devices, error code 801 is returned.

> **NOTE：**&gt;
> The child process started by calling this API does not inherit the resources of the parent process. After the
> child process is created, its PID is returned, the dynamic link library file specified in the parameters is
> loaded, and the entry function of the child process is executed. Once the entry function is done, the child
> process is automatically destroyed. After the process that calls this API is destroyed, the created child process
> is also destroyed.

**Since:** 13

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [entryPoint](../../apis-arkui/arkts-components/arkts-arkui-dynamicoptions-i-sys.md) | string | Yes |
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
