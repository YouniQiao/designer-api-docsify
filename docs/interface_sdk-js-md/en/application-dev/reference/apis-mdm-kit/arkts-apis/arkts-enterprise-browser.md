# @ohos.enterprise.browser(Browser Management)

The **browser** module provides browser management, including setting, canceling, and obtaining browser policies. It is applicable to scenarios such as enterprise device management, employee online behavior management, and security compliance audit.Browser policies are a collection of rules and settings that govern how a browser behaves, ensuring security, compliance, performance optimization, and a consistent user experience.

> **NOTE：**
> 
> The APIs of this module can be called only by a device administrator application that is enabled. For details, see
> [MDM Kit Development](../../../mdm/mdm-kit-guide.md).

**Since:** 12

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

## Modules to Import

```TypeScript
import browser from '@kit.MDMKit';
```

## Summary

### Functions

| Name | Description |
| --- | --- |
| [getManagedBrowserPolicy(Browser Management)](arkts-mdm-browser-getmanagedbrowserpolicy-f.md) | Obtains the policy of a specified browser based on the application bundle name. This API is applicable to scenarios where the current browser policy configuration needs to be queried, for example, displaying policy details in an enterprise device administrator application and verifying whether a policy has taken effect. |
| [getPoliciesSync(Browser Management)](arkts-mdm-browser-getpoliciessync-f.md) | Obtains the browser policy by app ID. |
| [getPoliciesSync(Browser Management)](arkts-mdm-browser-getpoliciessync-f.md) | Obtains the policy set for a specified browser based on **appid**. This API is applicable to scenarios where the current browser policy configuration needs to be queried, for example, displaying policy details in an enterprise device administrator application and verifying whether a policy has taken effect. |
| [getSelfManagedBrowserPolicy(Browser Management)](arkts-mdm-browser-getselfmanagedbrowserpolicy-f.md) | Obtains the browser policy of the current device. |
| [getSelfManagedBrowserPolicyVersion(Browser Management)](arkts-mdm-browser-getselfmanagedbrowserpolicyversion-f.md) | Obtains the browser policy version of the current device. |
| [setManagedBrowserPolicy(Browser Management)](arkts-mdm-browser-setmanagedbrowserpolicy-f.md) | Sets a browser policy for a specified browser. This API is applicable to scenarios where an enterprise needs to manage employees' browser behavior in a unified manner, such as configuring browser security policies. After the setting is successful, the system common event [COMMON_EVENT_MANAGED_BROWSER_POLICY_CHANGED](../../../reference/apis-basic-services-kit/common_event/commonEventManager-definitions.md#common_event_managed_browser_policy_changed) is released. |
| [setPolicySync(Browser Management)](arkts-mdm-browser-setpolicysync-f.md) | Sets a browser sub-policy for a specified browser. This API is applicable to scenarios where an enterprise needs to manage employees' browser behavior in a unified manner. |

<!--Del-->
### Functions(System API)

| Name | Description |
| --- | --- |
| [getPolicies(Browser Management)](arkts-mdm-browser-getpolicies-f-sys.md) | Obtains the policy of the specified browser. This API uses an asynchronous callback to return the result. |
| [getPolicies(Browser Management)](arkts-mdm-browser-getpolicies-f-sys.md) | Obtains the policy of the specified browser. This API uses a promise to return the result. |
| [setPolicies(Browser Management)](arkts-mdm-browser-setpolicies-f-sys.md) | Sets the browsing policy for a specified browser. This API uses an asynchronous callback to return the result. |
| [setPolicies(Browser Management)](arkts-mdm-browser-setpolicies-f-sys.md) | Sets the browsing policy for a specified browser. This API uses a promise to return the result. |
<!--DelEnd-->
