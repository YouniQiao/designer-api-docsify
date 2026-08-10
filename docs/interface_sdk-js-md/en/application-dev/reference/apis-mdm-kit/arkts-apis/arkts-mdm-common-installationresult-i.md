# InstallationResult

应用安装结果。

该对象目前在  
[EnterpriseAdminExtensionAbility.onMarketAppInstallResult](../../apis-default/arkts-apis/arkts-enterprise-enterpriseadminextensionability-enterpriseadminextensionability-c.md/arkts-enterprise-enterpriseadminextensionability-enterpriseadminextensionability-c.md#onmarketappinstallresult)作为回调入参使用。

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

应用安装结果消息。

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

应用安装结果码。SUCCESS表示应用安装成功，应用可正常使用；FAIL表示应用安装失败，应用不可用。

**Type:** [Result](../../apis-arkdata/arkts-apis/arkts-arkdata-relationalstore-result-i.md)

**Since:** 22

**ArkTS mode:** ArkTS-Dyn only, since version 22.

**Model restriction:** This API can be used only in the stage model.

<!--Device-InstallationResult-result: Result--><!--Device-InstallationResult-result: Result-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

