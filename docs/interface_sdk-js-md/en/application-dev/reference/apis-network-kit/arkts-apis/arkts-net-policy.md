# @ohos.net.policy(Network Policy Management)

The **policy** module provides APIs for managing network policies, which allow you to use firewall technology to control and manage the data traffic used.

**Since:** 10

**ArkTS mode:** Supports only ArkTS-Dyn, since version 10.

**System capability:** SystemCapability.Communication.NetManager.Core

## Modules to Import

```TypeScript
import { policy } from '@kit.NetworkKit';
```

## Summary

### Functions

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [getNetAccessPolicy(Network Policy Management)](arkts-network-policy-getnetaccesspolicy-f.md) |
| [showAppNetPolicySettings(Network Policy Management)](arkts-network-policy-showappnetpolicysettings-f.md) |

<!--Del-->
### Functions(System API)

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [getBackgroundPolicyByUid(Network Policy Management)](arkts-network-policy-getbackgroundpolicybyuid-f-sys.md) |
| [getBackgroundPolicyByUid(Network Policy Management)](arkts-network-policy-getbackgroundpolicybyuid-f-sys.md) |
| [getDeviceIdleTrustlist(Network Policy Management)](arkts-network-policy-getdeviceidletrustlist-f-sys.md) |
| [getDeviceIdleTrustlist(Network Policy Management)](arkts-network-policy-getdeviceidletrustlist-f-sys.md) |
| [getNetQuotaPolicies(Network Policy Management)](arkts-network-policy-getnetquotapolicies-f-sys.md) |
| [getNetQuotaPolicies(Network Policy Management)](arkts-network-policy-getnetquotapolicies-f-sys.md) |
| [getNetworkAccessPolicy(Network Policy Management)](arkts-network-policy-getnetworkaccesspolicy-f-sys.md) |
| [getNetworkAccessPolicy(Network Policy Management)](arkts-network-policy-getnetworkaccesspolicy-f-sys.md) |
| [getPolicyByUid(Network Policy Management)](arkts-network-policy-getpolicybyuid-f-sys.md) |
| [getPolicyByUid(Network Policy Management)](arkts-network-policy-getpolicybyuid-f-sys.md) |
| [getPowerSaveTrustlist(Network Policy Management)](arkts-network-policy-getpowersavetrustlist-f-sys.md) |
| [getPowerSaveTrustlist(Network Policy Management)](arkts-network-policy-getpowersavetrustlist-f-sys.md) |
| [getUidsByPolicy(Network Policy Management)](arkts-network-policy-getuidsbypolicy-f-sys.md) |
| [getUidsByPolicy(Network Policy Management)](arkts-network-policy-getuidsbypolicy-f-sys.md) |
| [isBackgroundAllowed(Network Policy Management)](arkts-network-policy-isbackgroundallowed-f-sys.md) |
| [isBackgroundAllowed(Network Policy Management)](arkts-network-policy-isbackgroundallowed-f-sys.md) |
| [isUidNetAllowed(Network Policy Management)](arkts-network-policy-isuidnetallowed-f-sys.md) |
| [isUidNetAllowed(Network Policy Management)](arkts-network-policy-isuidnetallowed-f-sys.md) |
| [isUidNetAllowed(Network Policy Management)](arkts-network-policy-isuidnetallowed-f-sys.md) |
| [isUidNetAllowed(Network Policy Management)](arkts-network-policy-isuidnetallowed-f-sys.md) |
| [off(Network Policy Management)](arkts-network-policy-off-f-sys.md#offnetuidpolicychange) |
| [off(Network Policy Management)](arkts-network-policy-off-f-sys.md#offnetuidrulechange) |
| [off(Network Policy Management)](arkts-network-policy-off-f-sys.md#offnetmeteredifaceschange) |
| [off(Network Policy Management)](arkts-network-policy-off-f-sys.md#offnetquotapolicychange) |
| [off(Network Policy Management)](arkts-network-policy-off-f-sys.md#offnetbackgroundpolicychange) |
| [on(Network Policy Management)](arkts-network-policy-on-f-sys.md#onnetuidpolicychange) |
| [on(Network Policy Management)](arkts-network-policy-on-f-sys.md#onnetuidrulechange) |
| [on(Network Policy Management)](arkts-network-policy-on-f-sys.md#onnetmeteredifaceschange) |
| [on(Network Policy Management)](arkts-network-policy-on-f-sys.md#onnetquotapolicychange) |
| [on(Network Policy Management)](arkts-network-policy-on-f-sys.md#onnetbackgroundpolicychange) |
| [resetPolicies(Network Policy Management)](arkts-network-policy-resetpolicies-f-sys.md) |
| [resetPolicies(Network Policy Management)](arkts-network-policy-resetpolicies-f-sys.md) |
| [restoreAllPolicies(Network Policy Management)](arkts-network-policy-restoreallpolicies-f-sys.md) |
| [setBackgroundAllowed(Network Policy Management)](arkts-network-policy-setbackgroundallowed-f-sys.md) |
| [setBackgroundAllowed(Network Policy Management)](arkts-network-policy-setbackgroundallowed-f-sys.md) |
| [setDeviceIdleTrustlist(Network Policy Management)](arkts-network-policy-setdeviceidletrustlist-f-sys.md) |
| [setDeviceIdleTrustlist(Network Policy Management)](arkts-network-policy-setdeviceidletrustlist-f-sys.md) |
| [setNetQuotaPolicies(Network Policy Management)](arkts-network-policy-setnetquotapolicies-f-sys.md) |
| [setNetQuotaPolicies(Network Policy Management)](arkts-network-policy-setnetquotapolicies-f-sys.md) |
| [setNetworkAccessPolicy(Network Policy Management)](arkts-network-policy-setnetworkaccesspolicy-f-sys.md) |
| [setPolicyByUid(Network Policy Management)](arkts-network-policy-setpolicybyuid-f-sys.md) |
| [setPolicyByUid(Network Policy Management)](arkts-network-policy-setpolicybyuid-f-sys.md) |
| [setPowerSaveTrustlist(Network Policy Management)](arkts-network-policy-setpowersavetrustlist-f-sys.md) |
| [setPowerSaveTrustlist(Network Policy Management)](arkts-network-policy-setpowersavetrustlist-f-sys.md) |
| [updateRemindPolicy(Network Policy Management)](arkts-network-policy-updateremindpolicy-f-sys.md) |
| [updateRemindPolicy(Network Policy Management)](arkts-network-policy-updateremindpolicy-f-sys.md) |
<!--DelEnd-->

### Interfaces

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [NetAccessPolicy(Network Policy Management)](arkts-network-policy-netaccesspolicy-i.md) |

<!--Del-->
### Interfaces(System API)

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [NetQuotaPolicy(Network Policy Management)](arkts-network-policy-netquotapolicy-i-sys.md) |
| [NetUidPolicyInfo(Network Policy Management)](arkts-network-policy-netuidpolicyinfo-i-sys.md) |
| [NetUidRuleInfo(Network Policy Management)](arkts-network-policy-netuidruleinfo-i-sys.md) |
| [NetworkAccessPolicy(Network Policy Management)](arkts-network-policy-networkaccesspolicy-i-sys.md) |
| [NetworkMatchRule(Network Policy Management)](arkts-network-policy-networkmatchrule-i-sys.md) |
| [QuotaPolicy(Network Policy Management)](arkts-network-policy-quotapolicy-i-sys.md) |
| [UidNetworkAccessPolicy(Network Policy Management)](arkts-network-policy-uidnetworkaccesspolicy-i-sys.md) |
<!--DelEnd-->

<!--Del-->
### Enums(System API)

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [LimitAction(Network Policy Management)](arkts-network-policy-limitaction-e-sys.md) |
| [NetBackgroundPolicy(Network Policy Management)](arkts-network-policy-netbackgroundpolicy-e-sys.md) |
| [NetUidPolicy(Network Policy Management)](arkts-network-policy-netuidpolicy-e-sys.md) |
| [NetUidRule(Network Policy Management)](arkts-network-policy-netuidrule-e-sys.md) |
| [RemindType(Network Policy Management)](arkts-network-policy-remindtype-e-sys.md) |
<!--DelEnd-->

### Types

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [NetBearType(Network Policy Management)](arkts-network-policy-netbeartype-t.md) |
