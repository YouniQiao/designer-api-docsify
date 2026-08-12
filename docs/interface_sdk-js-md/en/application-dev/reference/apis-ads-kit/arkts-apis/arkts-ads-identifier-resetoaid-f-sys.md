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

**ArkTS mode:** ArkTS-Dyn only, since version 10.

<!--Device-identifier-function resetOAID(): void--><!--Device-identifier-function resetOAID(): void-End-->

**System capability:** SystemCapability.Advertising.OAID

**System API:** This is a system API.

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [17300002](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-ads-kit/errorcode-oaid.md#17300002-not-in-the-trust-list) | Not in the trust list.<br>**Applicable version:** 12 and later |
| [17300001](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-ads-kit/errorcode-oaid.md#17300001-system-internal-error) | System internal error. |
| [202](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Permission verification failed. A non-system application calls a system API.<br>**Applicable version:** 12 and later |

## Examples

```TypeScript
import { identifier } from '@kit.AdsKit';

identifier.resetOAID();
```

