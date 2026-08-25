# runCmd (System API)

## Modules to Import

```TypeScript
import { process } from '@kit.ArkTS';
```

## runCmd

```TypeScript
function runCmd(
    command: string,
    options?: ConditionType
  ): ChildProcess
```

Returns a child process object and spawns a new ChildProcess to run the command.

**Since:** 7

**ArkTS mode:** Supports only ArkTS-Dyn, since version 7.

**System capability:** SystemCapability.Utils.Lang

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| command | string | Yes |
| options | [ConditionType](arkts-arkts-process-conditiontype-i-sys.md) | No |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| [ChildProcess](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-childprocess-childprocess-c.md) |
