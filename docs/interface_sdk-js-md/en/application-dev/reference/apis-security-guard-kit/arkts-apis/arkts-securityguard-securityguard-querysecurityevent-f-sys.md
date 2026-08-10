# querySecurityEvent (System API)

## Modules to Import

```TypeScript
import { securityGuard } from 'kits/@kit.SecurityGuardKit';
```

## querySecurityEvent

```TypeScript
function querySecurityEvent(rules: Array<SecurityEventRule>, querier: Querier): void
```

Query security event information from security guard.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Required permissions:** ohos.permission.QUERY_SECURITY_EVENT

<!--Device-securityGuard-function querySecurityEvent(rules: Array<SecurityEventRule>, querier: Querier): void--><!--Device-securityGuard-function querySecurityEvent(rules: Array<SecurityEventRule>, querier: Querier): void-End-->

**System capability:** SystemCapability.Security.SecurityGuard

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| rules | Array&lt;SecurityEventRule&gt; | Yes | rule of get security event information. |
| querier | [Querier](arkts-securityguard-securityguard-querier-i-sys.md) | Yes | callback of receiving the query data. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | invalid parameters. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 201 | check permission fail. |
| 202 | non-system application uses the system API. |

