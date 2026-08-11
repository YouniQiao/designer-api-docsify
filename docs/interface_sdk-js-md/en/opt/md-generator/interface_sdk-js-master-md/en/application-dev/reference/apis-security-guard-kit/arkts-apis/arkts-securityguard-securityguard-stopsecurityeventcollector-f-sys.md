# stopSecurityEventCollector (System API)

## Modules to Import

```TypeScript
import { securityGuard } from 'kits/@kit.SecurityGuardKit';
```

## stopSecurityEventCollector

```TypeScript
function stopSecurityEventCollector(rule: CollectorRule): void
```

stop the collector.

**Since:** 12

**Required permissions:** ohos.permission.QUERY_SECURITY_EVENT

<!--Device-securityGuard-function stopSecurityEventCollector(rule: CollectorRule): void--><!--Device-securityGuard-function stopSecurityEventCollector(rule: CollectorRule): void-End-->

**System capability:** SystemCapability.Security.SecurityGuard

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| rule | [CollectorRule](arkts-securityguard-securityguard-collectorrule-i-sys.md) | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
