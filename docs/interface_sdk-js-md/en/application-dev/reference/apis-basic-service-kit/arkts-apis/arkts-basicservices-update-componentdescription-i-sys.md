# ComponentDescription (System API)

组件描述文件。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-update-export interface ComponentDescription--><!--Device-update-export interface ComponentDescription-End-->

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

组件标识，用于唯一标识升级包中的组件。

使用场景：在获取版本描述信息(getNewVersionDescription)时需要传入componentId以获取对应组件的描述内容；在展示版本详情时可通过componentId区分不同组件。

获取方式：从版本检查结果的versionComponents数组中获取对应组件的componentId字段。

**Type:** string

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-ComponentDescription-componentId: string--><!--Device-ComponentDescription-componentId: string-End-->

**System capability:** SystemCapability.Update.UpdateService

**System API:** This is a system API.

## descriptionInfo

```TypeScript
descriptionInfo: DescriptionInfo
```

描述文件信息。

**Type:** [DescriptionInfo](arkts-basicservices-update-descriptioninfo-i-sys.md)

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-ComponentDescription-descriptionInfo: DescriptionInfo--><!--Device-ComponentDescription-descriptionInfo: DescriptionInfo-End-->

**System capability:** SystemCapability.Update.UpdateService

**System API:** This is a system API.

