# UpgradeInfo (System API)

升级信息。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-update-export interface UpgradeInfo--><!--Device-update-export interface UpgradeInfo-End-->

**System capability:** SystemCapability.Update.UpdateService

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { update } from 'kits/@kit.BasicServicesKit';
```

## businessType

```TypeScript
businessType: BusinessType
```

升级业务类型。

**Type:** [BusinessType](arkts-basicservices-update-businesstype-i-sys.md)

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-UpgradeInfo-businessType: BusinessType--><!--Device-UpgradeInfo-businessType: BusinessType-End-->

**System capability:** SystemCapability.Update.UpdateService

**System API:** This is a system API.

## upgradeApp

```TypeScript
upgradeApp: string
```

调用方包名，用于标识调用此升级接口的应用身份。格式为com.xxx.xxx.xxx，由点号分隔的多段组成。长度范围[1，255]，单位：字符，每段长度范围[1，64]，单位：字符，仅支持字母、数字和点号。每段必须以字母开头，不能包含连续点号或以点号开头结尾。超出范围或格式错误时抛出异常。

**Type:** string

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-UpgradeInfo-upgradeApp: string--><!--Device-UpgradeInfo-upgradeApp: string-End-->

**System capability:** SystemCapability.Update.UpdateService

**System API:** This is a system API.

