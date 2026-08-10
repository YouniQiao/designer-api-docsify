# DomainAccountInfo

表示域账号信息。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

<!--Device-osAccount-interface DomainAccountInfo--><!--Device-osAccount-interface DomainAccountInfo-End-->

**System capability:** SystemCapability.Account.OsAccount

## Modules to Import

```TypeScript
import { osAccount } from 'kits/@kit.BasicServicesKit';
```

## accountName

```TypeScript
accountName: string
```

域账号名。

**Type:** string

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

<!--Device-DomainAccountInfo-accountName: string--><!--Device-DomainAccountInfo-accountName: string-End-->

**System capability:** SystemCapability.Account.OsAccount

## additionalInfo

```TypeScript
additionalInfo?: Record<string, Object>
```

域账号附加信息。

此接口仅可在Stage模型下使用。

**Type:** [Record](../../apis-default/arkts-apis/arkts-record-t.md)&lt;string, Object&gt;

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DomainAccountInfo-additionalInfo?: Record<string, Object>--><!--Device-DomainAccountInfo-additionalInfo?: Record<string, Object>-End-->

**System capability:** SystemCapability.Account.OsAccount

## domain

```TypeScript
domain: string
```

域名。

**Type:** string

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

<!--Device-DomainAccountInfo-domain: string--><!--Device-DomainAccountInfo-domain: string-End-->

**System capability:** SystemCapability.Account.OsAccount

## serverConfigId

```TypeScript
serverConfigId?: string
```

域账号配置ID，默认为空字符串。

**Type:** string

**Since:** 18

**ArkTS mode:** ArkTS-Dyn since version 18; ArkTS-Sta since version 23.

<!--Device-DomainAccountInfo-serverConfigId?: string--><!--Device-DomainAccountInfo-serverConfigId?: string-End-->

**System capability:** SystemCapability.Account.OsAccount

