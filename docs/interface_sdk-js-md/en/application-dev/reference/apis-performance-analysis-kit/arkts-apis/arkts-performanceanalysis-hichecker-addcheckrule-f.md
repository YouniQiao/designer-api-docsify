# addCheckRule

## Modules to Import

```TypeScript
import { hichecker } from 'kits/@kit.PerformanceAnalysisKit';
```

## addCheckRule

```TypeScript
function addCheckRule(rule: bigint) : void
```

Adds one or more check rules. HiChecker detects unexpected operations or gives feedback based on the added rules. You can use **grep HiChecker** to check for the application running information in the hilog.

**Since:** 9

**System capability:** SystemCapability.HiviewDFX.HiChecker

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| rule | bigint | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
