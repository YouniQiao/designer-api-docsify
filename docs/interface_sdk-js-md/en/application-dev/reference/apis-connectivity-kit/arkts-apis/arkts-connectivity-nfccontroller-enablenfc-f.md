# enableNfc

## Modules to Import

```TypeScript
import { nfcController } from 'kits/@kit.ConnectivityKit';
```

## enableNfc

```TypeScript
function enableNfc(): void
```

Enables NFC.This API can be called only by system applications

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Required permissions:** ohos.permission.MANAGE_SECURE_SETTINGS

<!--Device-nfcController-function enableNfc(): void--><!--Device-nfcController-function enableNfc(): void-End-->

**System capability:** SystemCapability.Communication.NFC.Core

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 801 | Capability not supported. |
| 201 | Permission denied. |
| 3100101 | The NFC state is abnormal in the service. |

