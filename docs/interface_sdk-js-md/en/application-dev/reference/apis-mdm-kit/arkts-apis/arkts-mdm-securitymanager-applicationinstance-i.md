# ApplicationInstance

Application instance

**Since:** 20

**ArkTS mode:** ArkTS-Dyn only, since version 20.

<!--Device-securityManager-export interface ApplicationInstance--><!--Device-securityManager-export interface ApplicationInstance-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

## accountId

```TypeScript
accountId: number
```

User ID, which must be greater than or equal to 0. You can call  
[getOsAccountLocalId]\_\_\_JSDOC\_LINK\_DESC\_USD\_0\_\_\_ of  
**@ohos.account.osAccount** to obtain the user ID.

**Type:** number

**Since:** 20

**ArkTS mode:** ArkTS-Dyn only, since version 20.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ApplicationInstance-accountId: number--><!--Device-ApplicationInstance-accountId: number-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

## appIdentifier

```TypeScript
appIdentifier: string
```

The [unique identifier]\_\_\_JSDOC\_LINK\_DESC\_USD\_0\_\_\_ of an application. If an application does not have **appIdentifier**, **appId** can be used instead. Both **bundleInfo.signatureInfo.appIdentifier** and  
**bundleInfo.signatureInfo.appId** can be obtained via the  
[bundleManager.getBundleInfo]\_\_\_JSDOC\_LINK\_DESC\_USD\_1\_\_\_ API.

**Type:** string

**Since:** 20

**ArkTS mode:** ArkTS-Dyn only, since version 20.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ApplicationInstance-appIdentifier: string--><!--Device-ApplicationInstance-appIdentifier: string-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

## appIndex

```TypeScript
appIndex: number
```

Index of the application clone. The default value is **0**.

If **appIndex** is set to **0**, the main application is used. If **appIndex** is set to a value greater than 0,the application clone with the specified index is used.

**Type:** number

**Since:** 20

**ArkTS mode:** ArkTS-Dyn only, since version 20.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ApplicationInstance-appIndex: number--><!--Device-ApplicationInstance-appIndex: number-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

