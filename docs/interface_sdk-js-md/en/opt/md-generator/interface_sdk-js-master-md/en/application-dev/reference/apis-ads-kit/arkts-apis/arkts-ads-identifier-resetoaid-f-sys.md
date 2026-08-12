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

<!--Device-identifier-function resetOAID(): void--><!--Device-identifier-function resetOAID(): void-End-->

**System capability:** SystemCapability.Advertising.OAID

**System API:** This is a system API.

**Error codes:**

| Error Code ID |
| --- |
| [17300002](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-oaid.md#17300002-not-in-the-trust-list) |
| [17300001](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-oaid.md#17300001-system-internal-error) |
| [202](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## Examples

```TypeScript
import { identifier } from '@kit.AdsKit';

identifier.resetOAID();
```
