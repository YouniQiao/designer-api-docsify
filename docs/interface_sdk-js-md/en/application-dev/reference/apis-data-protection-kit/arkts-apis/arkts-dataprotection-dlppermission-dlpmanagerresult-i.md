# DLPManagerResult

Represents information about the trigger of the DLP manager application.

**Since:** 11

<!--Device-dlpPermission-export interface DLPManagerResult--><!--Device-dlpPermission-export interface DLPManagerResult-End-->

**System capability:** SystemCapability.Security.DataLossPrevention

## Modules to Import

```TypeScript
import { dlpPermission } from '@kit.DataProtectionKit';
```

## resultCode

```TypeScript
resultCode: number
```

Result code returned after the DLP manager application is started and exits. The value ranges from 0 to 3.

**Type:** number

**Since:** 11

**Model restriction:** This API can be used only in the stage model.

<!--Device-DLPManagerResult-resultCode: number--><!--Device-DLPManagerResult-resultCode: number-End-->

**System capability:** SystemCapability.Security.DataLossPrevention

## want

```TypeScript
want: Want
```

Data returned after the DLP manager application is started and exits.

**Type:** Want

**Since:** 11

**Model restriction:** This API can be used only in the stage model.

<!--Device-DLPManagerResult-want: Want--><!--Device-DLPManagerResult-want: Want-End-->

**System capability:** SystemCapability.Security.DataLossPrevention

