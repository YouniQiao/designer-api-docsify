# BusinessType (System API)

升级业务类型。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-update-export interface BusinessType--><!--Device-update-export interface BusinessType-End-->

**System capability:** SystemCapability.Update.UpdateService

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { update } from 'kits/@kit.BasicServicesKit';
```

## subType

```TypeScript
subType: BusinessSubType
```

升级类型，用于指定升级的目标对象。

使用场景：系统根据升级类型选择相应的升级包和升级流程。

可选值：FIRMWARE（固件升级，用于升级系统固件而非应用）。

建议：系统固件升级场景使用FIRMWARE，应用升级场景使用其他类型。

**Type:** [BusinessSubType](arkts-basicservices-update-businesssubtype-e-sys.md)

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-BusinessType-subType: BusinessSubType--><!--Device-BusinessType-subType: BusinessSubType-End-->

**System capability:** SystemCapability.Update.UpdateService

**System API:** This is a system API.

## vendor

```TypeScript
vendor: BusinessVendor
```

供应商类型，用于标识升级包的来源厂商。

使用场景：系统根据供应商类型选择对应的升级包管理服务器和验证策略。

可选值：PUBLIC（开源厂商，适用于开源版本的升级场景）。

建议根据实际升级包来源选择对应类型，开源版本升级时使用PUBLIC。

**Type:** [BusinessVendor](arkts-basicservices-update-businessvendor-e-sys.md)

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-BusinessType-vendor: BusinessVendor--><!--Device-BusinessType-vendor: BusinessVendor-End-->

**System capability:** SystemCapability.Update.UpdateService

**System API:** This is a system API.

