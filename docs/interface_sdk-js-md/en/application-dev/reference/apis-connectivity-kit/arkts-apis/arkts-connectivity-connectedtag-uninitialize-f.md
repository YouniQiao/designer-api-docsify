# uninitialize

## Modules to Import

```TypeScript
import { connectedTag } from '@kit.ConnectivityKit';
```

## uninitialize

```TypeScript
function uninitialize(): void
```

Uninitializes the active tag resources.

**Since:** 9

**ArkTS mode:** Supports only ArkTS-Dyn, since version 9.

**Required permissions:** ohos.permission.NFC_TAG

**System capability:** SystemCapability.Communication.ConnectedTag

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [3200101](../errorcode-nfc.md#3200101-abnormal-active-nfc-tag-status) |
