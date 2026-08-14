# @ohos.net.policy

Provides interfaces to manage network policy rules.

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Deprecated since:** -1

<!--Device-unnamed-declare namespace policy--><!--Device-unnamed-declare namespace policy-End-->

**System capability:** SystemCapability.Communication.NetManager.Core

## Modules to Import

```TypeScript
import { policy } from 'policy';
```

## Summary

### Functions

| Name | Description |
| --- | --- |
| [getNetAccessPolicy](arkts-network-policy-getnetaccesspolicy-f.md#getNetAccessPolicy) | Query the network access policy of the calling application. |
| [showAppNetPolicySettings](arkts-network-policy-showappnetpolicysettings-f.md#showAppNetPolicySettings) | Open the network settings interface of the application, which is presented in a semi-modal form and can be used to configure the network connection method. This API uses a promise to return the result. |

<!--Del-->
### Functions（系统接口）

| Name | Description |
| --- | --- |
| [getBackgroundPolicyByUid](arkts-network-policy-getbackgroundpolicybyuid-f-sys.md#getBackgroundPolicyByUid) | Get the background network policy for the specified uid. |
| [getBackgroundPolicyByUid](arkts-network-policy-getbackgroundpolicybyuid-f-sys.md#getBackgroundPolicyByUid-(System-API)) | Get the background network policy for the specified uid. |
| [getDeviceIdleTrustlist](arkts-network-policy-getdeviceidletrustlist-f-sys.md#getDeviceIdleTrustlist) | Obtain the list of uids that are allowed to access the Internet in hibernation mode. |
| [getDeviceIdleTrustlist](arkts-network-policy-getdeviceidletrustlist-f-sys.md#getDeviceIdleTrustlist-(System-API)) | Obtain the list of uids that are allowed to access the Internet in hibernation mode. |
| [getNetQuotaPolicies](arkts-network-policy-getnetquotapolicies-f-sys.md#getNetQuotaPolicies) | Get metered network quota policies. |
| [getNetQuotaPolicies](arkts-network-policy-getnetquotapolicies-f-sys.md#getNetQuotaPolicies-(System-API)) | Get metered network quota policies. |
| [getNetworkAccessPolicy](arkts-network-policy-getnetworkaccesspolicy-f-sys.md#getNetworkAccessPolicy) | Query the network access policy of the specified application. |
| [getNetworkAccessPolicy](arkts-network-policy-getnetworkaccesspolicy-f-sys.md#getNetworkAccessPolicy-(System-API)) | Query the network access policy of all applications. |
| [getPolicyByUid](arkts-network-policy-getpolicybyuid-f-sys.md#getPolicyByUid) | Query the policy of the specified UID. |
| [getPolicyByUid](arkts-network-policy-getpolicybyuid-f-sys.md#getPolicyByUid-(System-API)) | Query the policy of the specified UID. |
| [getPowerSaveTrustlist](arkts-network-policy-getpowersavetrustlist-f-sys.md#getPowerSaveTrustlist) | Obtain the list of uids that are allowed to access the Internet in power saving mode. |
| [getPowerSaveTrustlist](arkts-network-policy-getpowersavetrustlist-f-sys.md#getPowerSaveTrustlist-(System-API)) | Obtain the list of uids that are allowed to access the Internet in power saving mode. |
| [getUidsByPolicy](arkts-network-policy-getuidsbypolicy-f-sys.md#getUidsByPolicy) | Query the application UIDs of the specified policy. |
| [getUidsByPolicy](arkts-network-policy-getuidsbypolicy-f-sys.md#getUidsByPolicy-(System-API)) | Query the application UIDs of the specified policy. |
| [isBackgroundAllowed](arkts-network-policy-isbackgroundallowed-f-sys.md#isBackgroundAllowed) | Get the status if applications can use data on background. |
| [isBackgroundAllowed](arkts-network-policy-isbackgroundallowed-f-sys.md#isBackgroundAllowed-(System-API)) | Get the status if applications can use data on background. |
| [isUidNetAllowed](arkts-network-policy-isuidnetallowed-f-sys.md#isUidNetAllowed) | Get the status whether the uid app can access the metered network or non-metered network. |
| [isUidNetAllowed](arkts-network-policy-isuidnetallowed-f-sys.md#isUidNetAllowed-(System-API)) | Get the status whether the uid app can access the metered network or non-metered network. |
| [isUidNetAllowed](arkts-network-policy-isuidnetallowed-f-sys.md#isUidNetAllowed-(System-API)) | Get the status of whether the specified uid can access the specified network. |
| [isUidNetAllowed](arkts-network-policy-isuidnetallowed-f-sys.md#isUidNetAllowed-(System-API)) | Get the status of whether the specified uid can access the specified network. |
| [off_netBackgroundPolicyChange](arkts-network-policy-offnetbackgroundpolicychange-f-sys.md#off_netBackgroundPolicyChange) | Unregister network background policy change listener. |
| [off_netMeteredIfacesChange](arkts-network-policy-offnetmeteredifaceschange-f-sys.md#off_netMeteredIfacesChange) | Unregister metered ifaces change listener. |
| [off_netQuotaPolicyChange](arkts-network-policy-offnetquotapolicychange-f-sys.md#off_netQuotaPolicyChange) | Unregister quota policies change listener. |
| [off_netUidPolicyChange](arkts-network-policy-offnetuidpolicychange-f-sys.md#off_netUidPolicyChange) | Unregister uid policy change listener. |
| [off_netUidRuleChange](arkts-network-policy-offnetuidrulechange-f-sys.md#off_netUidRuleChange) | Unregister uid rule change listener. |
| [on_netBackgroundPolicyChange](arkts-network-policy-onnetbackgroundpolicychange-f-sys.md#on_netBackgroundPolicyChange) | Register network background policy change listener. |
| [on_netMeteredIfacesChange](arkts-network-policy-onnetmeteredifaceschange-f-sys.md#on_netMeteredIfacesChange) | Register metered ifaces change listener. |
| [on_netQuotaPolicyChange](arkts-network-policy-onnetquotapolicychange-f-sys.md#on_netQuotaPolicyChange) | Register quota policies change listener. |
| [on_netUidPolicyChange](arkts-network-policy-onnetuidpolicychange-f-sys.md#on_netUidPolicyChange) | Register uid policy change listener. |
| [on_netUidRuleChange](arkts-network-policy-onnetuidrulechange-f-sys.md#on_netUidRuleChange) | Register uid rule change listener. |
| [resetPolicies](arkts-network-policy-resetpolicies-f-sys.md#resetPolicies) | Reset network policies\rules\quota policies\firewall rules. |
| [resetPolicies](arkts-network-policy-resetpolicies-f-sys.md#resetPolicies-(System-API)) | Reset network policies\rules\quota policies\firewall rules. |
| [restoreAllPolicies](arkts-network-policy-restoreallpolicies-f-sys.md#restoreAllPolicies) | Reset the specified network management policy. |
| [setBackgroundAllowed](arkts-network-policy-setbackgroundallowed-f-sys.md#setBackgroundAllowed) | Control if applications can use data on background. |
| [setBackgroundAllowed](arkts-network-policy-setbackgroundallowed-f-sys.md#setBackgroundAllowed-(System-API)) | Control if applications can use data on background. |
| [setDeviceIdleTrustlist](arkts-network-policy-setdeviceidletrustlist-f-sys.md#setDeviceIdleTrustlist) | Set the list of uids that are allowed to access the Internet in hibernation mode. |
| [setDeviceIdleTrustlist](arkts-network-policy-setdeviceidletrustlist-f-sys.md#setDeviceIdleTrustlist-(System-API)) | Set the list of uids that are allowed to access the Internet in hibernation mode. |
| [setNetQuotaPolicies](arkts-network-policy-setnetquotapolicies-f-sys.md#setNetQuotaPolicies) | Set metered network quota policies. |
| [setNetQuotaPolicies](arkts-network-policy-setnetquotapolicies-f-sys.md#setNetQuotaPolicies-(System-API)) | Set metered network quota policies. |
| [setNetworkAccessPolicy](arkts-network-policy-setnetworkaccesspolicy-f-sys.md#setNetworkAccessPolicy) | Set the policy to access the network of the specified application. |
| [setPolicyByUid](arkts-network-policy-setpolicybyuid-f-sys.md#setPolicyByUid) | Set the policy for the specified UID. |
| [setPolicyByUid](arkts-network-policy-setpolicybyuid-f-sys.md#setPolicyByUid-(System-API)) | Set the policy for the specified UID. |
| [setPowerSaveTrustlist](arkts-network-policy-setpowersavetrustlist-f-sys.md#setPowerSaveTrustlist) | Set the list of uids that are allowed to access the Internet in power saving mode. |
| [setPowerSaveTrustlist](arkts-network-policy-setpowersavetrustlist-f-sys.md#setPowerSaveTrustlist-(System-API)) | Set the list of uids that are allowed to access the Internet in power saving mode. |
| [updateRemindPolicy](arkts-network-policy-updateremindpolicy-f-sys.md#updateRemindPolicy) | Update the policy when the quota reaches the upper limit. |
| [updateRemindPolicy](arkts-network-policy-updateremindpolicy-f-sys.md#updateRemindPolicy-(System-API)) | Update the policy when the quota reaches the upper limit. |
<!--DelEnd-->

### Interfaces

| Name | Description |
| --- | --- |
| [NetAccessPolicy](arkts-network-policy-netaccesspolicy-i.md) | Network policies that limit the specified UID of application to access the network. |
| [UidNetworkAccessPolicy](arkts-network-policy-uidnetworkaccesspolicy-i.md) | Provides the container definition for network access policy key-value pairs. |

<!--Del-->
### Interfaces（系统接口）

| Name | Description |
| --- | --- |
| [NetQuotaPolicy](arkts-network-policy-netquotapolicy-i-sys.md) | Net quota policies, including matching network rule usage periods, restrictions, and warnings. |
| [NetUidPolicyInfo](arkts-network-policy-netuidpolicyinfo-i-sys.md) | Callback function for registering network UID policy changes. |
| [NetUidRuleInfo](arkts-network-policy-netuidruleinfo-i-sys.md) | The interface is used to generate network unique identifiers. |
| [NetworkAccessPolicy](arkts-network-policy-networkaccesspolicy-i-sys.md) | Network policies that limit the specified UID of application to access the network. |
| [NetworkMatchRule](arkts-network-policy-networkmatchrule-i-sys.md) | The matching rules of network quota policies. |
| [QuotaPolicy](arkts-network-policy-quotapolicy-i-sys.md) | Policies that limit network quota. |
<!--DelEnd-->

<!--Del-->
### Enums（系统接口）

| Name | Description |
| --- | --- |
| [LimitAction](arkts-network-policy-limitaction-e-sys.md) | The action when quota policy hit the limit. |
| [NetBackgroundPolicy](arkts-network-policy-netbackgroundpolicy-e-sys.md) | Indicate whether the application can use metered networks in background. |
| [NetUidPolicy](arkts-network-policy-netuidpolicy-e-sys.md) | Uid Specifies the Internet access policy in background mode. |
| [NetUidRule](arkts-network-policy-netuidrule-e-sys.md) | Rules whether an uid can access to a metered or non-metered network. |
| [RemindType](arkts-network-policy-remindtype-e-sys.md) | Specify the remind type, see [updateRemindPolicy](arkts-network-policy-updateremindpolicy-f-sys.md#updateRemindPolicy-(System-API)). |
<!--DelEnd-->

### Types

| Name | Description |
| --- | --- |
| [NetBearType](arkts-network-policy-netbeartype-t.md) | Get network bear type. |

