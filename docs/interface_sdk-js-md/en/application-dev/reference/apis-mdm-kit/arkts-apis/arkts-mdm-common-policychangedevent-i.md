# PolicyChangedEvent

策略变更事件。

该接口目前在  
[onAdminPolicyChanged](../../apis-default/arkts-apis/arkts-enterprise-enterpriseadminextensionability-enterpriseadminextensionability-c.md/arkts-enterprise-enterpriseadminextensionability-enterpriseadminextensionability-c.md#onadminpolicychanged)接口中作为回调入参使用。

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

<!--Device-common-export interface PolicyChangedEvent--><!--Device-common-export interface PolicyChangedEvent-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

## Modules to Import

```TypeScript
import { common } from 'kits/@kit.MDMKit';
```

## bundleName

```TypeScript
bundleName: string
```

应用包名。

**Type:** string

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PolicyChangedEvent-bundleName: string--><!--Device-PolicyChangedEvent-bundleName: string-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

## functionName

```TypeScript
functionName: string
```

接口名称。例如调用[setPasswordPolicy](arkts-mdm-securitymanager-setpasswordpolicy-f.md#setpasswordpolicy)接口时，该字段返回值为setPasswordPolicy。

**Type:** string

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PolicyChangedEvent-functionName: string--><!--Device-PolicyChangedEvent-functionName: string-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

## parameters

```TypeScript
parameters: string
```

调用接口时传入的参数值（不包含admin参数），JSON格式字符串。例如调用  
[setPasswordPolicy](arkts-mdm-securitymanager-setpasswordpolicy-f.md#setpasswordpolicy)接口，该字段返回值为{"policy":{"complexityRegex":"^(?=.*[a-zA-Z])(?=.*\\d).{8},\$","validityPeriod":1808309786000,"additionalDescription":"至少8个字符，且包含数字和字母。"}}。

**Type:** string

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PolicyChangedEvent-parameters: string--><!--Device-PolicyChangedEvent-parameters: string-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

## time

```TypeScript
time: number
```

调用接口的时间戳，单位：ms。

**Type:** number

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PolicyChangedEvent-time: number--><!--Device-PolicyChangedEvent-time: number-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

