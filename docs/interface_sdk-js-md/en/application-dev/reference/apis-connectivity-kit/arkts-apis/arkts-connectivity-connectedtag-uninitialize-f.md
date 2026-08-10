# uninitialize

## Modules to Import

```TypeScript
import { connectedTag } from 'kits/@kit.ConnectivityKit';
```

## uninitialize

```TypeScript
function uninitialize(): void
```

Uninitializes the connected NFC tag.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

**Required permissions:** ohos.permission.NFC_TAG

<!--Device-connectedTag-function uninitialize(): void--><!--Device-connectedTag-function uninitialize(): void-End-->

**System capability:** SystemCapability.Communication.ConnectedTag

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 801 | Capability not supported. |
| 3200101 | Connected NFC tag running state is abnormal in service. |
| 201 | Permission denied. |

