# uninitialize

## Modules to Import

```TypeScript
import { connectedTag } from '@kit.ConnectivityKit';
```

## uninitialize

```TypeScript
function uninitialize(): void
```

Uninitializes the connected NFC tag.

**Since:** 9

**Required permissions:** ohos.permission.NFC_TAG

<!--Device-connectedTag-function uninitialize(): void--><!--Device-connectedTag-function uninitialize(): void-End-->

**System capability:** SystemCapability.Communication.ConnectedTag

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [801](../../errorcode-universal.md#801-api-not-supported) | Capability not supported. |
| [3200101](../errorcode-nfc.md#3200101-abnormal-active-nfc-tag-status) | Connected NFC tag running state is abnormal in service. |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. |

