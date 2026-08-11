# resetProcessPriority

## Modules to Import

```TypeScript
import { backgroundProcessManager } from 'kits/@kit.BackgroundTasksKit';
```

## resetProcessPriority

```TypeScript
function resetProcessPriority(pid: number): Promise<void>
```

Unsuppresses the child process. In this case, the child process follows the scheduling policy of the main process. If the scheduling policy of the main process changes, for example, from the background to the foreground, the child process changes with the main process. The effect is the same as calling **resetProcessPriority**.

**Since:** 17

<!--Device-backgroundProcessManager-function resetProcessPriority(pid: int): Promise<void>--><!--Device-backgroundProcessManager-function resetProcessPriority(pid: int): Promise<void>-End-->

**System capability:** SystemCapability.Resourceschedule.BackgroundProcessManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| pid | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;void&gt; |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { backgroundProcessManager } from '@kit.BackgroundTasksKit';

let childProcessPid = 33333;
try {
    backgroundProcessManager.resetProcessPriority(childProcessPid); 
} catch (error) {
    console.error(`resetProcessPriority failed, errCode: ${(error as BusinessError).code}, message: ${(error as BusinessError).message}`);
}
```
