# ApplicationInstance

应用实例。

**Since:** 20

**ArkTS mode:** ArkTS-Dyn only, since version 20.

<!--Device-securityManager-export interface ApplicationInstance--><!--Device-securityManager-export interface ApplicationInstance-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

## Modules to Import

```TypeScript
import { securityManager } from 'kits/@kit.MDMKit';
```

## accountId

```TypeScript
accountId: number
```

用户ID，指定具体用户，取值范围：大于等于0。accountId可以通过@ohos.account.osAccount中的  
[getOsAccountLocalId](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-osaccount-accountmanager-i.md/arkts-basicservices-osaccount-accountmanager-i.md#getosaccountlocalid)等接口来获取。

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

应用[唯一标识符](../../apis-ability-kit/arkts-apis/arkts-ability-bundleinfo-signatureinfo-i.md/arkts-ability-bundleinfo-signatureinfo-i.md)，如果应用没有appIdentifier可使用appId代替，可以通过接口  
[bundleManager.getBundleInfo](../../apis-ability-kit/arkts-apis/arkts-ability-bundlemanager-getbundleinfo-f.md/arkts-ability-bundlemanager-getbundleinfo-f.md#getbundleinfo)获取bundleInfo.signatureInfo.appIdentifier和bundleInfo.signatureInfo.appId。

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

表示分身应用的索引，默认值为0。

appIndex为0时，表示主应用。appIndex大于0时，表示指定的分身应用。

**Type:** number

**Since:** 20

**ArkTS mode:** ArkTS-Dyn only, since version 20.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ApplicationInstance-appIndex: number--><!--Device-ApplicationInstance-appIndex: number-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

