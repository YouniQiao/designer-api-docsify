# exit

## Modules to Import

```TypeScript
import { process } from 'kits/@kit.ArkTS';
```

## exit

```TypeScript
function exit(code: number): void
```

Terminates this process.Exercise caution when using this API. After this API is called, the application exits. If the input parameter is not 0, data loss or exceptions may occur.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [exit](arkts-arkts-process-processmanager-c.md#exit)

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| code | number | Yes |
