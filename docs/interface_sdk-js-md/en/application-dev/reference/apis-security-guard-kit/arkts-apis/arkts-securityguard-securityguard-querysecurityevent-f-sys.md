# querySecurityEvent (System API)

## Modules to Import

```TypeScript
import { securityGuard } from 'securityGuard';
```

## querySecurityEvent

```TypeScript
function querySecurityEvent(rules: Array<SecurityEventRule>, querier: Querier): void
```

Query security event information from security guard.

**Since:** 12

**Required permissions:** ohos.permission.QUERY_SECURITY_EVENT

<!--Device-securityGuard-function querySecurityEvent(rules: Array<SecurityEventRule>, querier: Querier): void--><!--Device-securityGuard-function querySecurityEvent(rules: Array<SecurityEventRule>, querier: Querier): void-End-->

**System capability:** SystemCapability.Security.SecurityGuard

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| rules | Array&lt;[SecurityEventRule](arkts-securityguard-securityguard-securityeventrule-i-sys.md)&gt; | Yes | rule of get security event information. |
| querier | Querier | Yes | callback of receiving the query data. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | invalid parameters. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| [201](../../errorcode-universal.md#201-permission-denied) | check permission fail. |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | non-system application uses the system API. |

