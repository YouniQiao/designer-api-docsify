# reportSecurityEvent (System API)

## Modules to Import

```TypeScript
import { securityGuard } from '@kit.SecurityGuardKit';
```

## reportSecurityEvent

```TypeScript
function reportSecurityEvent(securityEvent: SecurityEvent): void
```

Report security information to the security guard.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Required permissions:** ohos.permission.REPORT_SECURITY_EVENT

<!--Device-securityGuard-function reportSecurityEvent(securityEvent: SecurityEvent): void--><!--Device-securityGuard-function reportSecurityEvent(securityEvent: SecurityEvent): void-End-->

**System capability:** SystemCapability.Security.SecurityGuard

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| securityEvent | [SecurityEvent](arkts-securityguard-securityguard-securityevent-i-sys.md) | Yes | indicates the information to be reported. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | invalid parameters. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| [201](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/errorcode-universal.md#201-permission-denied) | check permission fail. |
| [202](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | non-system application uses the system API. |

