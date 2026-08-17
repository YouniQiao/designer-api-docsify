# enableNfc

## Modules to Import

```TypeScript
import { nfcController } from 'nfcController';
```

## enableNfc

```TypeScript
function enableNfc(): void
```

Enables NFC. This API can be called only by system applications

**Since:** 23

**Required permissions:** ohos.permission.MANAGE_SECURE_SETTINGS

<!--Device-nfcController-function enableNfc(): void--><!--Device-nfcController-function enableNfc(): void-End-->

**System capability:** SystemCapability.Communication.NFC.Core

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [801](../../errorcode-universal.md#801-api-not-supported) | Capability not supported. |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. |
| [3100101](../errorcode-nfc.md#3100101-nfc-switch-error) | The NFC state is abnormal in the service. |

