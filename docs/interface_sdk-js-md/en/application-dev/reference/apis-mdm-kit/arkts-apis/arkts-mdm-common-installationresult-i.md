# InstallationResult

An object that holds the application installation result.

This object is used as a callback parameter in  
[EnterpriseAdminExtensionAbility.onMarketAppInstallResult](arkts-mdm-enterprise-enterpriseadminextensionability-enterpriseadminextensionability-c.md#onmarketappinstallresult).

**Since:** 22

**ArkTS mode:** ArkTS-Dyn only, since version 22.

<!--Device-common-export interface InstallationResult--><!--Device-common-export interface InstallationResult-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

## Modules to Import

```TypeScript
import { common } from 'kits/@kit.MDMKit';
```

## message

```TypeScript
message: string
```

Application installation result message.

**Type:** string

**Since:** 22

**ArkTS mode:** ArkTS-Dyn only, since version 22.

**Model restriction:** This API can be used only in the stage model.

<!--Device-InstallationResult-message: string--><!--Device-InstallationResult-message: string-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

## result

```TypeScript
result: Result
```

Application installation result. **SUCCESS** indicates that the application is successfully installed and can be properly used. **FAIL** indicates that the application fails to be installed and is unavailable.

**Type:** [Result](../../apis-arkdata/arkts-apis/arkts-arkdata-relationalstore-result-i.md)

**Since:** 22

**ArkTS mode:** ArkTS-Dyn only, since version 22.

**Model restriction:** This API can be used only in the stage model.

<!--Device-InstallationResult-result: Result--><!--Device-InstallationResult-result: Result-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

