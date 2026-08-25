# setHyperSnapEnabled

## Modules to Import

```TypeScript
import { hyperSnapManager } from '@kit.AbilityKit';
```

## setHyperSnapEnabled

```TypeScript
function setHyperSnapEnabled(enableFlag : boolean): void
```

Enables or disables the Hyper Snap performance optimization for the application.When enabled, the system will create a snapshot of the application process at an appropriate time. Subsequent launched resume directly from this snapshot, bypassing the full cold start sequence, resulting in significantly improved application launch performance.  
**Notes:** - The system ultimately determines whether to create or use snapshots based on application compatibility, resource availability, and system policies. Enabling this feature only indicates the application's readiness for optimization. - Hyper Snap is enabled by default for applications meeting system compatibility requirements. - If issues arise after enabling Hyper Snap, disable this feature to revert to standard cold start processes. - Settings persist across reboots.

**Since:** 24

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [enableFlag](../../apis-performance-analysis-kit/arkts-apis/arkts-performanceanalysis-hitracechain-enableflag-f.md) | boolean | Yes |

**Error codes:**

| Error Code ID |
| --- |
| 16000150 |
