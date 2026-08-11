# @ohos.net.policy

Provides interfaces to manage network policy rules.

**Since:** 10

<!--Device-unnamed-declare namespace policy--><!--Device-unnamed-declare namespace policy-End-->

**System capability:** SystemCapability.Communication.NetManager.Core

## Modules to Import

```TypeScript
import { policy } from 'kits/@kit.NetworkKit';
```

## Summary

### Functions

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [getNetAccessPolicy](arkts-network-policy-getnetaccesspolicy-f.md#getnetaccesspolicy) |
| [showAppNetPolicySettings](arkts-network-policy-showappnetpolicysettings-f.md#showappnetpolicysettings) |

<!--Del-->
### Functions（系统接口）

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [getBackgroundPolicyByUid](arkts-network-policy-getbackgroundpolicybyuid-f-sys.md#getbackgroundpolicybyuid) |
| [getBackgroundPolicyByUid](arkts-network-policy-getbackgroundpolicybyuid-f-sys.md#getbackgroundpolicybyuid-1) |
| [getDeviceIdleTrustlist](arkts-network-policy-getdeviceidletrustlist-f-sys.md#getdeviceidletrustlist) |
| [getDeviceIdleTrustlist](arkts-network-policy-getdeviceidletrustlist-f-sys.md#getdeviceidletrustlist-1) |
| [getNetQuotaPolicies](arkts-network-policy-getnetquotapolicies-f-sys.md#getnetquotapolicies) |
| [getNetQuotaPolicies](arkts-network-policy-getnetquotapolicies-f-sys.md#getnetquotapolicies-1) |
| [getNetworkAccessPolicy](arkts-network-policy-getnetworkaccesspolicy-f-sys.md#getnetworkaccesspolicy) |
| [getNetworkAccessPolicy](arkts-network-policy-getnetworkaccesspolicy-f-sys.md#getnetworkaccesspolicy-1) |
| [getPolicyByUid](arkts-network-policy-getpolicybyuid-f-sys.md#getpolicybyuid) |
| [getPolicyByUid](arkts-network-policy-getpolicybyuid-f-sys.md#getpolicybyuid-1) |
| [getPowerSaveTrustlist](arkts-network-policy-getpowersavetrustlist-f-sys.md#getpowersavetrustlist) |
| [getPowerSaveTrustlist](arkts-network-policy-getpowersavetrustlist-f-sys.md#getpowersavetrustlist-1) |
| [getUidsByPolicy](arkts-network-policy-getuidsbypolicy-f-sys.md#getuidsbypolicy) |
| [getUidsByPolicy](arkts-network-policy-getuidsbypolicy-f-sys.md#getuidsbypolicy-1) |
| [isBackgroundAllowed](arkts-network-policy-isbackgroundallowed-f-sys.md#isbackgroundallowed) |
| [isBackgroundAllowed](arkts-network-policy-isbackgroundallowed-f-sys.md#isbackgroundallowed-1) |
| [isUidNetAllowed](arkts-network-policy-isuidnetallowed-f-sys.md#isuidnetallowed) |
| [isUidNetAllowed](arkts-network-policy-isuidnetallowed-f-sys.md#isuidnetallowed-1) |
| [isUidNetAllowed](arkts-network-policy-isuidnetallowed-f-sys.md#isuidnetallowed-2) |
| [isUidNetAllowed](arkts-network-policy-isuidnetallowed-f-sys.md#isuidnetallowed-3) |
| [off](arkts-network-policy-off-f-sys.md#off) |
| [off](arkts-network-policy-off-f-sys.md#off-1) |
| [off](arkts-network-policy-off-f-sys.md#off-2) |
| [off](arkts-network-policy-off-f-sys.md#off-3) |
| [off](arkts-network-policy-off-f-sys.md#off-4) |
| [on](arkts-network-policy-on-f-sys.md#on) |
| [on](arkts-network-policy-on-f-sys.md#on-1) |
| [on](arkts-network-policy-on-f-sys.md#on-2) |
| [on](arkts-network-policy-on-f-sys.md#on-3) |
| [on](arkts-network-policy-on-f-sys.md#on-4) |
| [resetPolicies](arkts-network-policy-resetpolicies-f-sys.md#resetpolicies) |
| [resetPolicies](arkts-network-policy-resetpolicies-f-sys.md#resetpolicies-1) |
| [restoreAllPolicies](arkts-network-policy-restoreallpolicies-f-sys.md#restoreallpolicies) |
| [setBackgroundAllowed](arkts-network-policy-setbackgroundallowed-f-sys.md#setbackgroundallowed) |
| [setBackgroundAllowed](arkts-network-policy-setbackgroundallowed-f-sys.md#setbackgroundallowed-1) |
| [setDeviceIdleTrustlist](arkts-network-policy-setdeviceidletrustlist-f-sys.md#setdeviceidletrustlist) |
| [setDeviceIdleTrustlist](arkts-network-policy-setdeviceidletrustlist-f-sys.md#setdeviceidletrustlist-1) |
| [setNetQuotaPolicies](arkts-network-policy-setnetquotapolicies-f-sys.md#setnetquotapolicies) |
| [setNetQuotaPolicies](arkts-network-policy-setnetquotapolicies-f-sys.md#setnetquotapolicies-1) |
| [setNetworkAccessPolicy](arkts-network-policy-setnetworkaccesspolicy-f-sys.md#setnetworkaccesspolicy) |
| [setPolicyByUid](arkts-network-policy-setpolicybyuid-f-sys.md#setpolicybyuid) |
| [setPolicyByUid](arkts-network-policy-setpolicybyuid-f-sys.md#setpolicybyuid-1) |
| [setPowerSaveTrustlist](arkts-network-policy-setpowersavetrustlist-f-sys.md#setpowersavetrustlist) |
| [setPowerSaveTrustlist](arkts-network-policy-setpowersavetrustlist-f-sys.md#setpowersavetrustlist-1) |
| [updateRemindPolicy](arkts-network-policy-updateremindpolicy-f-sys.md#updateremindpolicy) |
| [updateRemindPolicy](arkts-network-policy-updateremindpolicy-f-sys.md#updateremindpolicy-1) |
<!--DelEnd-->

### Interfaces

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [NetAccessPolicy](arkts-network-policy-netaccesspolicy-i.md) |

<!--Del-->
### Interfaces（系统接口）

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [NetQuotaPolicy](arkts-network-policy-netquotapolicy-i-sys.md) |
| [NetUidPolicyInfo](arkts-network-policy-netuidpolicyinfo-i-sys.md) |
| [NetUidRuleInfo](arkts-network-policy-netuidruleinfo-i-sys.md) |
| [NetworkAccessPolicy](arkts-network-policy-networkaccesspolicy-i-sys.md) |
| [NetworkMatchRule](arkts-network-policy-networkmatchrule-i-sys.md) |
| [QuotaPolicy](arkts-network-policy-quotapolicy-i-sys.md) |
| [UidNetworkAccessPolicy](arkts-network-policy-uidnetworkaccesspolicy-i-sys.md) |
<!--DelEnd-->

<!--Del-->
### Enums（系统接口）

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [LimitAction](arkts-network-policy-limitaction-e-sys.md) |
| [NetBackgroundPolicy](arkts-network-policy-netbackgroundpolicy-e-sys.md) |
| [NetUidPolicy](arkts-network-policy-netuidpolicy-e-sys.md) |
| [NetUidRule](arkts-network-policy-netuidrule-e-sys.md) |
| [RemindType](arkts-network-policy-remindtype-e-sys.md) |
<!--DelEnd-->

### Types

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [NetBearType](arkts-network-policy-netbeartype-t.md) |
