# @ohos.net.policy

Provides interfaces to manage network policy rules.

**Since:** 10

**Deprecated since:** -1

<!--Device-unnamed-declare namespace policy--><!--Device-unnamed-declare namespace policy-End-->

**System capability:** SystemCapability.Communication.NetManager.Core

## Modules to Import

```TypeScript
import { policy } from '@kit.NetworkKit';
```

## Summary

### Functions

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [getNetAccessPolicy](arkts-network-policy-getnetaccesspolicy-f.md#getNetAccessPolicy) |
| [showAppNetPolicySettings](arkts-network-policy-showappnetpolicysettings-f.md#showAppNetPolicySettings) |

<!--Del-->
### Functions（系统接口）

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [getBackgroundPolicyByUid](arkts-network-policy-getbackgroundpolicybyuid-f-sys.md#getBackgroundPolicyByUid-(System-API)) |
| [getBackgroundPolicyByUid](arkts-network-policy-getbackgroundpolicybyuid-f-sys.md#getBackgroundPolicyByUid-(System-API)) |
| [getDeviceIdleTrustlist](arkts-network-policy-getdeviceidletrustlist-f-sys.md#getDeviceIdleTrustlist-(System-API)) |
| [getDeviceIdleTrustlist](arkts-network-policy-getdeviceidletrustlist-f-sys.md#getDeviceIdleTrustlist-(System-API)) |
| [getNetQuotaPolicies](arkts-network-policy-getnetquotapolicies-f-sys.md#getNetQuotaPolicies-(System-API)) |
| [getNetQuotaPolicies](arkts-network-policy-getnetquotapolicies-f-sys.md#getNetQuotaPolicies-(System-API)) |
| [getNetworkAccessPolicy](arkts-network-policy-getnetworkaccesspolicy-f-sys.md#getNetworkAccessPolicy-(System-API)) |
| [getNetworkAccessPolicy](arkts-network-policy-getnetworkaccesspolicy-f-sys.md#getNetworkAccessPolicy-(System-API)) |
| [getPolicyByUid](arkts-network-policy-getpolicybyuid-f-sys.md#getPolicyByUid-(System-API)) |
| [getPolicyByUid](arkts-network-policy-getpolicybyuid-f-sys.md#getPolicyByUid-(System-API)) |
| [getPowerSaveTrustlist](arkts-network-policy-getpowersavetrustlist-f-sys.md#getPowerSaveTrustlist-(System-API)) |
| [getPowerSaveTrustlist](arkts-network-policy-getpowersavetrustlist-f-sys.md#getPowerSaveTrustlist-(System-API)) |
| [getUidsByPolicy](arkts-network-policy-getuidsbypolicy-f-sys.md#getUidsByPolicy-(System-API)) |
| [getUidsByPolicy](arkts-network-policy-getuidsbypolicy-f-sys.md#getUidsByPolicy-(System-API)) |
| [isBackgroundAllowed](arkts-network-policy-isbackgroundallowed-f-sys.md#isBackgroundAllowed-(System-API)) |
| [isBackgroundAllowed](arkts-network-policy-isbackgroundallowed-f-sys.md#isBackgroundAllowed-(System-API)) |
| [isUidNetAllowed](arkts-network-policy-isuidnetallowed-f-sys.md#isUidNetAllowed-(System-API)) |
| [isUidNetAllowed](arkts-network-policy-isuidnetallowed-f-sys.md#isUidNetAllowed-(System-API)) |
| [isUidNetAllowed](arkts-network-policy-isuidnetallowed-f-sys.md#isUidNetAllowed-(System-API)) |
| [isUidNetAllowed](arkts-network-policy-isuidnetallowed-f-sys.md#isUidNetAllowed-(System-API)) |
| [off_netBackgroundPolicyChange](arkts-network-policy-offnetbackgroundpolicychange-f-sys.md#off_netBackgroundPolicyChange) |
| [off_netMeteredIfacesChange](arkts-network-policy-offnetmeteredifaceschange-f-sys.md#off_netMeteredIfacesChange) |
| [off_netQuotaPolicyChange](arkts-network-policy-offnetquotapolicychange-f-sys.md#off_netQuotaPolicyChange) |
| [off_netUidPolicyChange](arkts-network-policy-offnetuidpolicychange-f-sys.md#off_netUidPolicyChange) |
| [off_netUidRuleChange](arkts-network-policy-offnetuidrulechange-f-sys.md#off_netUidRuleChange) |
| [on_netBackgroundPolicyChange](arkts-network-policy-onnetbackgroundpolicychange-f-sys.md#on_netBackgroundPolicyChange) |
| [on_netMeteredIfacesChange](arkts-network-policy-onnetmeteredifaceschange-f-sys.md#on_netMeteredIfacesChange) |
| [on_netQuotaPolicyChange](arkts-network-policy-onnetquotapolicychange-f-sys.md#on_netQuotaPolicyChange) |
| [on_netUidPolicyChange](arkts-network-policy-onnetuidpolicychange-f-sys.md#on_netUidPolicyChange) |
| [on_netUidRuleChange](arkts-network-policy-onnetuidrulechange-f-sys.md#on_netUidRuleChange) |
| [resetPolicies](arkts-network-policy-resetpolicies-f-sys.md#resetPolicies-(System-API)) |
| [resetPolicies](arkts-network-policy-resetpolicies-f-sys.md#resetPolicies-(System-API)) |
| [restoreAllPolicies](arkts-network-policy-restoreallpolicies-f-sys.md#restoreAllPolicies-(System-API)) |
| [setBackgroundAllowed](arkts-network-policy-setbackgroundallowed-f-sys.md#setBackgroundAllowed-(System-API)) |
| [setBackgroundAllowed](arkts-network-policy-setbackgroundallowed-f-sys.md#setBackgroundAllowed-(System-API)) |
| [setDeviceIdleTrustlist](arkts-network-policy-setdeviceidletrustlist-f-sys.md#setDeviceIdleTrustlist-(System-API)) |
| [setDeviceIdleTrustlist](arkts-network-policy-setdeviceidletrustlist-f-sys.md#setDeviceIdleTrustlist-(System-API)) |
| [setNetQuotaPolicies](arkts-network-policy-setnetquotapolicies-f-sys.md#setNetQuotaPolicies-(System-API)) |
| [setNetQuotaPolicies](arkts-network-policy-setnetquotapolicies-f-sys.md#setNetQuotaPolicies-(System-API)) |
| [setNetworkAccessPolicy](arkts-network-policy-setnetworkaccesspolicy-f-sys.md#setNetworkAccessPolicy-(System-API)) |
| [setPolicyByUid](arkts-network-policy-setpolicybyuid-f-sys.md#setPolicyByUid-(System-API)) |
| [setPolicyByUid](arkts-network-policy-setpolicybyuid-f-sys.md#setPolicyByUid-(System-API)) |
| [setPowerSaveTrustlist](arkts-network-policy-setpowersavetrustlist-f-sys.md#setPowerSaveTrustlist-(System-API)) |
| [setPowerSaveTrustlist](arkts-network-policy-setpowersavetrustlist-f-sys.md#setPowerSaveTrustlist-(System-API)) |
| [updateRemindPolicy](arkts-network-policy-updateremindpolicy-f-sys.md#updateRemindPolicy-(System-API)) |
| [updateRemindPolicy](arkts-network-policy-updateremindpolicy-f-sys.md#updateRemindPolicy-(System-API)) |
<!--DelEnd-->

### Interfaces

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [NetAccessPolicy](arkts-network-policy-netaccesspolicy-i.md) |
| [UidNetworkAccessPolicy](arkts-network-policy-uidnetworkaccesspolicy-i.md) |

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
