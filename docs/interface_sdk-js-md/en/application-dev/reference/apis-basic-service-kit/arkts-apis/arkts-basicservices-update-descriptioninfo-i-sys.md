# DescriptionInfo (System API)

版本描述文件信息。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-update-export interface DescriptionInfo--><!--Device-update-export interface DescriptionInfo-End-->

**System capability:** SystemCapability.Update.UpdateService

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { update } from 'kits/@kit.BasicServicesKit';
```

## content

```TypeScript
content: string
```

描述文件内容。

**Type:** string

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-DescriptionInfo-content: string--><!--Device-DescriptionInfo-content: string-End-->

**System capability:** SystemCapability.Update.UpdateService

**System API:** This is a system API.

## descriptionType

```TypeScript
descriptionType: DescriptionType
```

描述文件类型，取值原则：CONTENT为内容，适用于描述内容较短或需要即时展示的场景；URI为链接，适用于描述内容较长或需要从外部资源获取的场景。应根据描述内容长度和展示方式选择。

**Type:** [DescriptionType](arkts-basicservices-update-descriptiontype-e-sys.md)

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-DescriptionInfo-descriptionType: DescriptionType--><!--Device-DescriptionInfo-descriptionType: DescriptionType-End-->

**System capability:** SystemCapability.Update.UpdateService

**System API:** This is a system API.

