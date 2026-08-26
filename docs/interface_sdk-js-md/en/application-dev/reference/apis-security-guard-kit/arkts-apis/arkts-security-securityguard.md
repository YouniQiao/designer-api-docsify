# @ohos.security.securityGuard(This module provides the capabilities to security guard.)

Provides security event management and security model management. Based on event information, you will be able to analyze the running status of devices.@namespace securityGuard

**Since:** 12

**System capability:** SystemCapability.Security.SecurityGuard

**System API:** This is a system API.

## Modules to Import

```TypeScript
import securityGuard from '@kit.SecurityGuardKit';
```

## Summary

<!--Del-->
### Functions(System API)

| Name | Description |
| --- | --- |
| [getModelResult(This module provides the capabilities to security guard.)](arkts-securityguard-securityguard-getmodelresult-f-sys.md) | Request security model result from security guard. |
| off(This module provides the capabilities to security guard.) | Unsubscribe the security event. |
| on(This module provides the capabilities to security guard.) | Subscribe the security event. |
| [querySecurityEvent(This module provides the capabilities to security guard.)](arkts-securityguard-securityguard-querysecurityevent-f-sys.md) | Query security event information from security guard. |
| [reportSecurityEvent(This module provides the capabilities to security guard.)](arkts-securityguard-securityguard-reportsecurityevent-f-sys.md) | Report security information to the security guard. |
| [startSecurityEventCollector(This module provides the capabilities to security guard.)](arkts-securityguard-securityguard-startsecurityeventcollector-f-sys.md) | start the collector to collect data |
| [stopSecurityEventCollector(This module provides the capabilities to security guard.)](arkts-securityguard-securityguard-stopsecurityeventcollector-f-sys.md) | stop the collector. |
| [updatePolicyFile(This module provides the capabilities to security guard.)](arkts-securityguard-securityguard-updatepolicyfile-f-sys.md) | Update the policy file. |
<!--DelEnd-->

<!--Del-->
### Interfaces(System API)

| Name | Description |
| --- | --- |
| [CollectorRule(This module provides the capabilities to security guard.)](arkts-securityguard-securityguard-collectorrule-i-sys.md) | Provides the conditions of Collector. |
| [ModelResult(This module provides the capabilities to security guard.)](arkts-securityguard-securityguard-modelresult-i-sys.md) | Provides the ModelResult type. |
| [ModelRule(This module provides the capabilities to security guard.)](arkts-securityguard-securityguard-modelrule-i-sys.md) | Provides the ModelRule type. |
| [PolicyFile(This module provides the capabilities to security guard.)](arkts-securityguard-securityguard-policyfile-i-sys.md) | Provides policy file information.@interface PolicyFile |
| [Querier(This module provides the capabilities to security guard.)](arkts-securityguard-securityguard-querier-i-sys.md) | Definition callback of receiving the query data.@interface Querier |
| [SecurityEvent(This module provides the capabilities to security guard.)](arkts-securityguard-securityguard-securityevent-i-sys.md) | Provides the SecurityEvent type, including the event id, version info, report content. |
| [SecurityEventInfo(This module provides the capabilities to security guard.)](arkts-securityguard-securityguard-securityeventinfo-i-sys.md) | Provides the conditions of on/off.@interface SecurityEventInfo |
| [SecurityEventRule(This module provides the capabilities to security guard.)](arkts-securityguard-securityguard-securityeventrule-i-sys.md) | Provides the conditions of querySecurityEvent.@interface SecurityEventRule |
<!--DelEnd-->
