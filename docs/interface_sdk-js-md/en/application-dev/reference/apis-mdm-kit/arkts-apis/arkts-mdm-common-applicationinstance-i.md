# ApplicationInstance

Defines application instance data.

It is used as an input parameter in the  
[addUserNonStopApps](arkts-mdm-applicationmanager-addusernonstopapps-f.md#addusernonstopapps),  
[removeUserNonStopApps](arkts-mdm-applicationmanager-removeusernonstopapps-f.md#removeusernonstopapps),  
[addFreezeExemptedApps](arkts-mdm-applicationmanager-addfreezeexemptedapps-f.md#addfreezeexemptedapps), and  
[removeFreezeExemptedApps](arkts-mdm-applicationmanager-removefreezeexemptedapps-f.md#removefreezeexemptedapps)APIs.

**Since:** 22

**ArkTS mode:** ArkTS-Dyn only, since version 22.

<!--Device-common-export interface ApplicationInstance--><!--Device-common-export interface ApplicationInstance-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

## Modules to Import

```TypeScript
import { common } from 'kits/@kit.MDMKit';
```

## accountId

```TypeScript
accountId: number
```

Account ID. The value is an integer greater than or equal to 0.You can obtain the account ID by calling the  
[getOsAccountLocalId](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-osaccount-accountmanager-i.md/arkts-basicservices-osaccount-accountmanager-i.md#getosaccountlocalid) API.

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

[Unique identifier](../../apis-ability-kit/arkts-apis/arkts-ability-bundleinfo-signatureinfo-i.md/arkts-ability-bundleinfo-signatureinfo-i.md) of an application. You can call the  
[bundleManager.getBundleInfo](../../apis-ability-kit/arkts-apis/arkts-ability-bundlemanager-getbundleinfo-f.md/arkts-ability-bundlemanager-getbundleinfo-f.md#getbundleinfo) API to obtain  
**bundleInfo.signatureInfo.appIdentifier**.

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

Index of the application clone. The value is an integer greater than or equal to 0.

You can obtain the index by calling the  
[getAppCloneIdentity](../../apis-ability-kit/arkts-apis/arkts-ability-bundlemanager-getappcloneidentity-f.md/arkts-ability-bundlemanager-getappcloneidentity-f.md#getappcloneidentity) API.

**Type:** number

**Since:** 22

**ArkTS mode:** ArkTS-Dyn only, since version 22.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ApplicationInstance-appIndex: number--><!--Device-ApplicationInstance-appIndex: number-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

