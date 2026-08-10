# OtaUpdatePolicy

升级策略。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

<!--Device-systemManager-export interface OtaUpdatePolicy--><!--Device-systemManager-export interface OtaUpdatePolicy-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

## Modules to Import

```TypeScript
import { systemManager } from 'kits/@kit.MDMKit';
```

## delayUpdateTime

```TypeScript
delayUpdateTime?: number
```

表示延迟升级时间（单位：小时）。

**Type:** number

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Model restriction:** This API can be used only in the stage model.

<!--Device-OtaUpdatePolicy-delayUpdateTime?: number--><!--Device-OtaUpdatePolicy-delayUpdateTime?: number-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

## disableSystemOtaUpdate

```TypeScript
disableSystemOtaUpdate?: boolean
```

表示是否禁用在公网环境下升级。true表示禁用公网升级，false表示不禁用公网升级。如果作为  
[systemManager.setOtaUpdatePolicy](arkts-mdm-systemmanager-setotaupdatepolicy-f.md#setotaupdatepolicy)的入参，该字段可缺省，缺省时保持当前配置不变。当前配置可通过  
[systemManager.getOtaUpdatePolicy](arkts-mdm-systemmanager-getotaupdatepolicy-f.md#getotaupdatepolicy)接口获取。禁用公网升级后，可以采用内网升级。

**Type:** boolean

**Since:** 20

**ArkTS mode:** ArkTS-Dyn only, since version 20.

**Model restriction:** This API can be used only in the stage model.

<!--Device-OtaUpdatePolicy-disableSystemOtaUpdate?: boolean--><!--Device-OtaUpdatePolicy-disableSystemOtaUpdate?: boolean-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

## installEndTime

```TypeScript
installEndTime?: number
```

表示指定安装窗口结束时间（时间戳）。

**Type:** number

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Model restriction:** This API can be used only in the stage model.

<!--Device-OtaUpdatePolicy-installEndTime?: number--><!--Device-OtaUpdatePolicy-installEndTime?: number-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

## installStartTime

```TypeScript
installStartTime?: number
```

表示指定安装窗口起始时间（时间戳）。

**Type:** number

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Model restriction:** This API can be used only in the stage model.

<!--Device-OtaUpdatePolicy-installStartTime?: number--><!--Device-OtaUpdatePolicy-installStartTime?: number-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

## latestUpdateTime

```TypeScript
latestUpdateTime?: number
```

表示最晚升级时间（时间戳）。

**Type:** number

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Model restriction:** This API can be used only in the stage model.

<!--Device-OtaUpdatePolicy-latestUpdateTime?: number--><!--Device-OtaUpdatePolicy-latestUpdateTime?: number-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

## policyType

```TypeScript
policyType: PolicyType
```

表示升级策略类型。

**Type:** [PolicyType](../../apis-core-file-kit/arkts-apis/arkts-corefile-fileshare-policytype-e.md)

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Model restriction:** This API can be used only in the stage model.

<!--Device-OtaUpdatePolicy-policyType: PolicyType--><!--Device-OtaUpdatePolicy-policyType: PolicyType-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

## version

```TypeScript
version: string
```

表示待升级软件版本号。

**Type:** string

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Model restriction:** This API can be used only in the stage model.

<!--Device-OtaUpdatePolicy-version: string--><!--Device-OtaUpdatePolicy-version: string-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

