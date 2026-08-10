# VersionComponent (System API)

版本组件。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-update-export interface VersionComponent--><!--Device-update-export interface VersionComponent-End-->

**System capability:** SystemCapability.Update.UpdateService

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { update } from 'kits/@kit.BasicServicesKit';
```

## componentId

```TypeScript
componentId: string
```

组件标识，用于唯一标识升级包中的组件。从版本检查结果的versionComponents数组中获取，用于后续描述信息查询或组件信息展示等场景。

**Type:** string

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-VersionComponent-componentId: string--><!--Device-VersionComponent-componentId: string-End-->

**System capability:** SystemCapability.Update.UpdateService

**System API:** This is a system API.

## componentType

```TypeScript
componentType: ComponentType
```

组件类型。

**Type:** [ComponentType](arkts-basicservices-update-componenttype-e-sys.md)

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-VersionComponent-componentType: ComponentType--><!--Device-VersionComponent-componentType: ComponentType-End-->

**System capability:** SystemCapability.Update.UpdateService

**System API:** This is a system API.

## descriptionInfo

```TypeScript
descriptionInfo: DescriptionInfo
```

描述文件信息.

**Type:** [DescriptionInfo](arkts-basicservices-update-descriptioninfo-i-sys.md)

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-VersionComponent-descriptionInfo: DescriptionInfo--><!--Device-VersionComponent-descriptionInfo: DescriptionInfo-End-->

**System capability:** SystemCapability.Update.UpdateService

**System API:** This is a system API.

## displayVersion

```TypeScript
displayVersion: string
```

显示版本号。

**Type:** string

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-VersionComponent-displayVersion: string--><!--Device-VersionComponent-displayVersion: string-End-->

**System capability:** SystemCapability.Update.UpdateService

**System API:** This is a system API.

## effectiveMode

```TypeScript
effectiveMode: EffectiveMode
```

生效模式，取值原则：COLD为冷升级，需重启设备生效；LIVE为热升级，无需重启即可生效；LIVE_AND_COLD为融合升级，结合两者特性。

**Type:** [EffectiveMode](arkts-basicservices-update-effectivemode-e-sys.md)

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-VersionComponent-effectiveMode: EffectiveMode--><!--Device-VersionComponent-effectiveMode: EffectiveMode-End-->

**System capability:** SystemCapability.Update.UpdateService

**System API:** This is a system API.

## innerVersion

```TypeScript
innerVersion: string
```

版本号。

**Type:** string

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-VersionComponent-innerVersion: string--><!--Device-VersionComponent-innerVersion: string-End-->

**System capability:** SystemCapability.Update.UpdateService

**System API:** This is a system API.

## otaMode

```TypeScript
otaMode?: OtaMode
```

升级模式。当需要指定特定的升级模式时传入此参数，适用于存储空间受限、快速升级或A/B分区设备等特殊场景。取值原则：REGULAR_OTA为正常升级，适用于大多数常规升级场景；STREAM_OTA为流式升级，适用于存储空间受限或需要快速升级的场景；AB_REGULAR_OTA为AB正常升级，适用于A/B分区设备；AB_STREAM_OTA为AB流式升级，适用于A/B分区设备。不传入时默认为REGULAR_OTA，使用正常升级模式。

**Type:** [OtaMode](arkts-basicservices-update-otamode-e-sys.md)

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

<!--Device-VersionComponent-otaMode?: OtaMode--><!--Device-VersionComponent-otaMode?: OtaMode-End-->

**System capability:** SystemCapability.Update.UpdateService

**System API:** This is a system API.

## size

```TypeScript
size: int
```

升级包大小，单位为B，取值范围[0, +∞]。超出范围时抛出异常。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-VersionComponent-size: int--><!--Device-VersionComponent-size: int-End-->

**System capability:** SystemCapability.Update.UpdateService

**System API:** This is a system API.

## upgradeAction

```TypeScript
upgradeAction: UpgradeAction
```

升级方式，取值原则：UPGRADE为差分包，适用于增量升级场景；RECOVERY为修复包，适用于系统故障修复场景。

**Type:** [UpgradeAction](arkts-basicservices-update-upgradeaction-e-sys.md)

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-VersionComponent-upgradeAction: UpgradeAction--><!--Device-VersionComponent-upgradeAction: UpgradeAction-End-->

**System capability:** SystemCapability.Update.UpdateService

**System API:** This is a system API.

