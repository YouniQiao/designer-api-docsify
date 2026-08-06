# @ohos.enterprise.browser(Browser Management)

The **browser** module provides browser management, including setting, canceling, and obtaining browser policies. It is applicable to scenarios such as enterprise device management, employee online behavior management, and security compliance audit.

Browser policies are a collection of rules and settings that govern how a browser behaves, ensuring security,compliance, performance optimization, and a consistent user experience.
    **NOTE**  
    
    The APIs of this module can be called only by a device administrator application that is enabled. For details, see  
    \_\_\_MD\_LINK\_DESC\_USD\_0\_\_\_.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 10.

<!--Device-unnamed-declare namespace browser--><!--Device-unnamed-declare namespace browser-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

## Summary

### Functions

| Name | Description |
| --- | --- |
| [getManagedBrowserPolicy](arkts-mdm-browser-getmanagedbrowserpolicy-f.md#getmanagedbrowserpolicy) | Obtains the policy of a specified browser based on the application bundle name. This API is applicable to scenarios where the current browser policy configuration needs to be queried, for example, displaying policy details in an enterprise device administrator application and verifying whether a policy has taken effect. |
| [getPolicies](arkts-mdm-browser-getpolicies-f.md#getpolicies) | Obtains the policy of the specified browser. This API uses an asynchronous callback to return the result. |
| [getPolicies](arkts-mdm-browser-getpolicies-f.md#getpolicies-1) | Obtains the policy of the specified browser. This API uses a promise to return the result. |
| [getPoliciesSync](arkts-mdm-browser-getpoliciessync-f.md#getpoliciessync) | Obtains the browser policy by app ID. |
| [getPoliciesSync](arkts-mdm-browser-getpoliciessync-f.md#getpoliciessync-1) | Obtains the policy set for a specified browser based on **appid**. This API is applicable to scenarios where the current browser policy configuration needs to be queried, for example, displaying policy details in an enterprise device administrator application and verifying whether a policy has taken effect. |
| [getSelfManagedBrowserPolicy](arkts-mdm-browser-getselfmanagedbrowserpolicy-f.md#getselfmanagedbrowserpolicy) | Obtains the browser policy of the current device. |
| [getSelfManagedBrowserPolicyVersion](arkts-mdm-browser-getselfmanagedbrowserpolicyversion-f.md#getselfmanagedbrowserpolicyversion) | Obtains the browser policy version of the current device. |
| [setManagedBrowserPolicy](arkts-mdm-browser-setmanagedbrowserpolicy-f.md#setmanagedbrowserpolicy) | Sets a browser policy for a specified browser. This API is applicable to scenarios where an enterprise needs to manage employees' browser behavior in a unified manner, such as configuring browser security policies. After the setting is successful, the system common event  \_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_MD\_\_\_ESCAPED\_UNDERSCORE\_\_\_LINK\_\_\_ESCAPED\_UNDERSCORE\_\_\_DESC\_\_\_ESCAPED\_UNDERSCORE\_\_\_USD\_\_\_ESCAPED\_UNDERSCORE\_\_\_0\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_is released. |
| [setPolicies](arkts-mdm-browser-setpolicies-f.md#setpolicies) | Sets the browsing policy for a specified browser. This API uses an asynchronous callback to return the result. |
| [setPolicies](arkts-mdm-browser-setpolicies-f.md#setpolicies-1) | Sets the browsing policy for a specified browser. This API uses a promise to return the result. |
| [setPolicySync](arkts-mdm-browser-setpolicysync-f.md#setpolicysync) | Sets a browser sub-policy for a specified browser. This API is applicable to scenarios where an enterprise needs to manage employees' browser behavior in a unified manner. |

