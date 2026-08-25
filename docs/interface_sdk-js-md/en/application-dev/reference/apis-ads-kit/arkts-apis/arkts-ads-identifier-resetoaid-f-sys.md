# resetOAID (System API)

## Modules to Import

```TypeScript
import { identifier } from '@kit.AdsKit';
```

## resetOAID

```TypeScript
function resetOAID(): void
```

Resets the OAID.

**Since:** 10

**ArkTS mode:** Supports only ArkTS-Dyn, since version 10.

**System capability:** SystemCapability.Advertising.OAID

**System API:** This is a system API.

**Error codes:**

| Error Code ID |
| --- |
| [17300001](../errorcode-oaid.md#17300001-system-internal-error) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [17300002](../errorcode-oaid.md#17300002-not-in-the-trust-list) |

**Examples**

```TypeScript
import { identifier } from '@kit.AdsKit';

identifier.resetOAID();
```
