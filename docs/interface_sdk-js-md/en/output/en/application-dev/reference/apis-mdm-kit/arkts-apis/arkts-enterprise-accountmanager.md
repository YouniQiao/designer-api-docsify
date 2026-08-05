# @ohos.enterprise.accountManager

This module provides device account management capabilities, including forbidding the creation of local accounts. > **NOTE** > > The APIs of this module can be called only by a device administrator application that is enabled. For details, see > \_\_\_MD\_LINK\_DESC\_USD\_0\_\_\_.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 10.

<!--Device-unnamed-declare namespace accountManager--><!--Device-unnamed-declare namespace accountManager-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

## Summary

### Functions

| Name | Description |
| --- | --- |
| [activateOsAccount](arkts-mdm-accountmanager-activateosaccount-f.md#activateosaccount) | Switches the system account. Currently, this API is supported only on phones and tablets, and can only switch between normal system accounts created via [createNormalOsAccount]\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_JSDOC\_\_\_ESCAPED\_UNDERSCORE\_\_\_LINK\_\_\_ESCAPED\_UNDERSCORE\_\_\_DESC\_\_\_ESCAPED\_UNDERSCORE\_\_\_USD\_\_\_ESCAPED\_UNDERSCORE\_\_\_0\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_ and the default system account (ID: 100). |
| [addOsAccount](arkts-mdm-accountmanager-addosaccount-f.md#addosaccount) | Adds an account in the background. |
| [addOsAccountAsync](arkts-mdm-accountmanager-addosaccountasync-f.md#addosaccountasync) | Adds an account in the background. This API uses a promise to return the result. This API is applicable to scenarios where enterprises need to create accounts in batches or remotely manage accounts. Accounts can be created without user interaction, improving management efficiency. |
| [createNormalOsAccount](arkts-mdm-accountmanager-createnormalosaccount-f.md#createnormalosaccount) | Creates a normal system account. A maximum of two normal system accounts ( [osAccount.OsAccountType]\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_JSDOC\_\_\_ESCAPED\_UNDERSCORE\_\_\_LINK\_\_\_ESCAPED\_UNDERSCORE\_\_\_DESC\_\_\_ESCAPED\_UNDERSCORE\_\_\_USD\_\_\_ESCAPED\_UNDERSCORE\_\_\_0\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_) can be created. |
| [disallowAddLocalAccount](arkts-mdm-accountmanager-disallowaddlocalaccount-f.md#disallowaddlocalaccount) | Forbids the creation of local accounts on the device. This API uses an asynchronous callback to return the result. |
| [disallowAddLocalAccount](arkts-mdm-accountmanager-disallowaddlocalaccount-f.md#disallowaddlocalaccount-1) | Forbids the creation of local accounts on the device. This API uses a promise to return the result. |
| [disallowAddOsAccountByUser](arkts-mdm-accountmanager-disallowaddosaccountbyuser-f.md#disallowaddosaccountbyuser) | Disallows a user to add accounts. |
| [disallowOsAccountAddition](arkts-mdm-accountmanager-disallowosaccountaddition-f.md#disallowosaccountaddition) | Users are not allowed to add accounts. After the API is successfully called, the system forbids the specified user or all users from adding new accounts. This API is applicable to enterprise device management scenarios, such as preventing employees from creating local accounts and enhancing device security management. |
| [getDomainAccountPolicy](arkts-mdm-accountmanager-getdomainaccountpolicy-f.md#getdomainaccountpolicy) | Obtains the domain account policy. This API is applicable to enterprise management scenarios, such as querying the current domain account policy configuration and auditing policy compliance. |
| [isAddOsAccountByUserDisallowed](arkts-mdm-accountmanager-isaddosaccountbyuserdisallowed-f.md#isaddosaccountbyuserdisallowed) | Queries whether to disallow a user to add accounts. |
| [isOsAccountAdditionDisallowed](arkts-mdm-accountmanager-isosaccountadditiondisallowed-f.md#isosaccountadditiondisallowed) | Queries whether a user is not allowed to add an account. |
| [isOsAccountAdditionDisallowed](arkts-mdm-accountmanager-isosaccountadditiondisallowed-f.md#isosaccountadditiondisallowed-1) | Queries whether a user is not allowed to add an account. This API is applicable to enterprise audit and compliance check scenarios, helping administrators confirm the execution of account policies. |
| [removeOsAccount](arkts-mdm-accountmanager-removeosaccount-f.md#removeosaccount) | Removes a system account. Currently, this API is supported only on phones and tablets. It can remove normal system accounts (of the normal type) created via [createNormalOsAccount]\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_JSDOC\_\_\_ESCAPED\_UNDERSCORE\_\_\_LINK\_\_\_ESCAPED\_UNDERSCORE\_\_\_DESC\_\_\_ESCAPED\_UNDERSCORE\_\_\_USD\_\_\_ESCAPED\_UNDERSCORE\_\_\_0\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_ and system accounts (of the admin, normal, and guest types) created via [addOsAccountAsync]\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_JSDOC\_\_\_ESCAPED\_UNDERSCORE\_\_\_LINK\_\_\_ESCAPED\_UNDERSCORE\_\_\_DESC\_\_\_ESCAPED\_UNDERSCORE\_\_\_USD\_\_\_ESCAPED\_UNDERSCORE\_\_\_1\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_. The default system account (ID: 100) cannot be removed. |
| [setDomainAccountPolicy](arkts-mdm-accountmanager-setdomainaccountpolicy-f.md#setdomainaccountpolicy) | Sets the domain account policy. |

### Interfaces

| Name | Description |
| --- | --- |
| [DomainAccountPolicy](arkts-mdm-accountmanager-domainaccountpolicy-i.md) | Domain account policy. |

