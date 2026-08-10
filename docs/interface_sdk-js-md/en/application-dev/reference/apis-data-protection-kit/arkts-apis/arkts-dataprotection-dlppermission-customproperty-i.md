# CustomProperty

表示自定义策略。

**Since:** 21

**ArkTS mode:** ArkTS-Dyn only, since version 20.

<!--Device-dlpPermission-export interface CustomProperty--><!--Device-dlpPermission-export interface CustomProperty-End-->

**System capability:** SystemCapability.Security.DataLossPrevention

## Modules to Import

```TypeScript
import { dlpPermission } from 'kits/@kit.DataProtectionKit';
```

## enterprise

```TypeScript
enterprise: string
```

表示企业定制策略的JSON字符串。长度不超过2&lt;sup&gt;22&lt;/sup&gt;字节，超出此范围抛出错误码401。

**Type:** string

**Since:** 21

**ArkTS mode:** ArkTS-Dyn only, since version 20.

<!--Device-CustomProperty-enterprise: string--><!--Device-CustomProperty-enterprise: string-End-->

**System capability:** SystemCapability.Security.DataLossPrevention

## options

```TypeScript
options?: DlpFileQueryOptions
```

企业DLP文件的查询选项，默认为空。

**Type:** [DlpFileQueryOptions](arkts-dataprotection-dlppermission-dlpfilequeryoptions-i.md)

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CustomProperty-options?: DlpFileQueryOptions--><!--Device-CustomProperty-options?: DlpFileQueryOptions-End-->

**System capability:** SystemCapability.Security.DataLossPrevention

