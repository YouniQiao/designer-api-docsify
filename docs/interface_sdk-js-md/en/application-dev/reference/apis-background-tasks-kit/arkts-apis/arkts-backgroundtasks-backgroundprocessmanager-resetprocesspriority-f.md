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

**System capability:** SystemCapability.Resourceschedule.BackgroundProcessManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| pid | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |
