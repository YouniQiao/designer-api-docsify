# PasswordPolicy

设备锁屏口令策略。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-securityManager-export interface PasswordPolicy--><!--Device-securityManager-export interface PasswordPolicy-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

## Modules to Import

```TypeScript
import { securityManager } from 'kits/@kit.MDMKit';
```

## additionalDescription

```TypeScript
additionalDescription?: string
```

口令复杂度描述文本，例如：密码中必须包含字母、数字、特殊字符，至少8个字符，最多30个字符。

**Type:** string

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PasswordPolicy-additionalDescription?: string--><!--Device-PasswordPolicy-additionalDescription?: string-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

## complexityRegex

```TypeScript
complexityRegex?: string
```

口令复杂度正则表达式。

**Type:** string

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PasswordPolicy-complexityRegex?: string--><!--Device-PasswordPolicy-complexityRegex?: string-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

## passwordAlgs

```TypeScript
passwordAlgs?: PasswordAlgs
```

处理口令数据使用的加密算法。设置后，PC/2in1设备上将原始口令处理成口令凭据会使用该参数指定的加密算法，其他设备无效果。

**Type:** [PasswordAlgs](arkts-mdm-securitymanager-passwordalgs-e.md)

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PasswordPolicy-passwordAlgs?: PasswordAlgs--><!--Device-PasswordPolicy-passwordAlgs?: PasswordAlgs-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

## validityPeriod

```TypeScript
validityPeriod?: long
```

密码有效期（单位：毫秒）。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：long

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PasswordPolicy-validityPeriod?: long--><!--Device-PasswordPolicy-validityPeriod?: long-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

