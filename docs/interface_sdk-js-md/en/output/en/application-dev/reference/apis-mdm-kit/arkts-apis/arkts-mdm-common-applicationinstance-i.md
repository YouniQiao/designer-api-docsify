# ApplicationInstance

Defines application instance data. It is used as an input parameter in the [addUserNonStopApps]\_\_\_JSDOC\_LINK\_DESC\_USD\_0\_\_\_, [removeUserNonStopApps]\_\_\_JSDOC\_LINK\_DESC\_USD\_1\_\_\_, [addFreezeExemptedApps]\_\_\_JSDOC\_LINK\_DESC\_USD\_2\_\_\_, and [removeFreezeExemptedApps]\_\_\_JSDOC\_LINK\_DESC\_USD\_3\_\_\_ APIs.

**Since:** 22

**ArkTS mode:** ArkTS-Dyn only, since version 22.

<!--Device-common-export interface ApplicationInstance--><!--Device-common-export interface ApplicationInstance-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

## accountId

```TypeScript
accountId: number
```

Account ID. The value is an integer greater than or equal to 0. You can obtain the account ID by calling the [getOsAccountLocalId]\_\_\_JSDOC\_LINK\_DESC\_USD\_0\_\_\_ API.

**Type:** number

**Since:** 22

**ArkTS mode:** ArkTS-Dyn only, since version 22.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ApplicationInstance-accountId: number--><!--Device-ApplicationInstance-accountId: number-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

## appIdentifier

```TypeScript
appIdentifier: string
```

[Unique identifier]\_\_\_JSDOC\_LINK\_DESC\_USD\_0\_\_\_ of an application. You can call the [bundleManager.getBundleInfo]\_\_\_JSDOC\_LINK\_DESC\_USD\_1\_\_\_ API to obtain **bundleInfo.signatureInfo.appIdentifier**.

**Type:** string

**Since:** 22

**ArkTS mode:** ArkTS-Dyn only, since version 22.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ApplicationInstance-appIdentifier: string--><!--Device-ApplicationInstance-appIdentifier: string-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

## appIndex

```TypeScript
appIndex: number
```

Index of the application clone. The value is an integer greater than or equal to 0. You can obtain the index by calling the [getAppCloneIdentity]\_\_\_JSDOC\_LINK\_DESC\_USD\_0\_\_\_ API.

**Type:** number

**Since:** 22

**ArkTS mode:** ArkTS-Dyn only, since version 22.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ApplicationInstance-appIndex: number--><!--Device-ApplicationInstance-appIndex: number-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

