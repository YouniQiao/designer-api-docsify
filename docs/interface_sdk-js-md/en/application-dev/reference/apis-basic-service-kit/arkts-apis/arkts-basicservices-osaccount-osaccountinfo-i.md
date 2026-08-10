# OsAccountInfo

表示系统账号信息。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn since version 7; ArkTS-Sta since version 23.

<!--Device-osAccount-interface OsAccountInfo--><!--Device-osAccount-interface OsAccountInfo-End-->

**System capability:** SystemCapability.Account.OsAccount

## Modules to Import

```TypeScript
import { osAccount } from 'kits/@kit.BasicServicesKit';
```

## constraints

```TypeScript
constraints: Array<string>
```

系统账号[约束](../../../reference/apis-basic-services-kit/js-apis-osAccount.md#系统账号约束列表)，默认为空。

**Type:** Array&lt;string&gt;

**Since:** 7

**ArkTS mode:** ArkTS-Dyn since version 7; ArkTS-Sta since version 23.

<!--Device-OsAccountInfo-constraints: Array<string>--><!--Device-OsAccountInfo-constraints: Array<string>-End-->

**System capability:** SystemCapability.Account.OsAccount

## createTime

```TypeScript
createTime: long
```

系统账号创建时间，以Unix时间戳格式表示，单位为s。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：long

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

<!--Device-OsAccountInfo-createTime: long--><!--Device-OsAccountInfo-createTime: long-End-->

**System capability:** SystemCapability.Account.OsAccount

## distributedInfo

```TypeScript
distributedInfo: distributedAccount.DistributedInfo
```

分布式账号信息，默认为空。

**Type:** distributedAccount.DistributedInfo

**Since:** 7

**ArkTS mode:** ArkTS-Dyn since version 7; ArkTS-Sta since version 23.

<!--Device-OsAccountInfo-distributedInfo: distributedAccount.DistributedInfo--><!--Device-OsAccountInfo-distributedInfo: distributedAccount.DistributedInfo-End-->

**System capability:** SystemCapability.Account.OsAccount

## domainInfo

```TypeScript
domainInfo: DomainAccountInfo
```

域账号信息，默认为空。

**Type:** [DomainAccountInfo](arkts-basicservices-osaccount-domainaccountinfo-i.md)

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

<!--Device-OsAccountInfo-domainInfo: DomainAccountInfo--><!--Device-OsAccountInfo-domainInfo: DomainAccountInfo-End-->

**System capability:** SystemCapability.Account.OsAccount

## isActivated

```TypeScript
isActivated: boolean
```

系统账号是否激活。true表示指定账号已激活；false表示指定账号未激活。

**Type:** boolean

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

<!--Device-OsAccountInfo-isActivated: boolean--><!--Device-OsAccountInfo-isActivated: boolean-End-->

**System capability:** SystemCapability.Account.OsAccount

## isActived

```TypeScript
isActived: boolean
```

系统账号激活状态。true表示指定账号处于激活状态；false表示指定账号处于未激活状态。

**说明：**从API version 7开始支持，从API version 11开始废弃，建议使用isActivated。

**Type:** boolean

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Deprecated since:** 11

**Substitutes:** [osAccount.OsAccountInfo.isActivated](arkts-basicservices-osaccount-osaccountinfo-i.md#isactivated)

<!--Device-OsAccountInfo-isActived: boolean--><!--Device-OsAccountInfo-isActived: boolean-End-->

**System capability:** SystemCapability.Account.OsAccount

## isCreateCompleted

```TypeScript
isCreateCompleted: boolean
```

系统账号创建是否完整。true表示指定账号已创建完整；false表示指定账号未创建完整。

**Type:** boolean

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

<!--Device-OsAccountInfo-isCreateCompleted: boolean--><!--Device-OsAccountInfo-isCreateCompleted: boolean-End-->

**System capability:** SystemCapability.Account.OsAccount

## isUnlocked

```TypeScript
isUnlocked: boolean
```

账号是否已解锁（EL2级别目录是否解密）。true表示指定账号已解锁；false表示指定账号未解锁。

**Type:** boolean

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

<!--Device-OsAccountInfo-isUnlocked: boolean--><!--Device-OsAccountInfo-isUnlocked: boolean-End-->

**System capability:** SystemCapability.Account.OsAccount

## isVerified

```TypeScript
isVerified: boolean
```

账号是否验证。true表示指定账号已验证；false表示指定账号未验证。

**说明：**从API version 7开始支持，从API version 11开始废弃，建议使用isUnlocked。

**Type:** boolean

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Deprecated since:** 11

**Substitutes:** [osAccount.OsAccountInfo.isUnlocked](arkts-basicservices-osaccount-osaccountinfo-i.md#isunlocked)

<!--Device-OsAccountInfo-isVerified: boolean--><!--Device-OsAccountInfo-isVerified: boolean-End-->

**System capability:** SystemCapability.Account.OsAccount

## lastLoginTime

```TypeScript
lastLoginTime: long
```

系统账号最后一次登录时间，以Unix时间戳格式表示，单位为s。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：long

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

<!--Device-OsAccountInfo-lastLoginTime: long--><!--Device-OsAccountInfo-lastLoginTime: long-End-->

**System capability:** SystemCapability.Account.OsAccount

## localId

```TypeScript
localId: int
```

系统账号ID。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 7

**ArkTS mode:** ArkTS-Dyn since version 7; ArkTS-Sta since version 23.

<!--Device-OsAccountInfo-localId: int--><!--Device-OsAccountInfo-localId: int-End-->

**System capability:** SystemCapability.Account.OsAccount

## localName

```TypeScript
localName: string
```

系统账号名称。

**Type:** string

**Since:** 7

**ArkTS mode:** ArkTS-Dyn since version 7; ArkTS-Sta since version 23.

<!--Device-OsAccountInfo-localName: string--><!--Device-OsAccountInfo-localName: string-End-->

**System capability:** SystemCapability.Account.OsAccount

## photo

```TypeScript
photo: string
```

系统账号头像，默认为空。

**Type:** string

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

<!--Device-OsAccountInfo-photo: string--><!--Device-OsAccountInfo-photo: string-End-->

**System capability:** SystemCapability.Account.OsAccount

## serialNumber

```TypeScript
serialNumber: long
```

系统账号SN码。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：long

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

<!--Device-OsAccountInfo-serialNumber: long--><!--Device-OsAccountInfo-serialNumber: long-End-->

**System capability:** SystemCapability.Account.OsAccount

## type

```TypeScript
type: OsAccountType
```

系统账号类型。

**Type:** [OsAccountType](arkts-basicservices-osaccount-osaccounttype-e.md)

**Since:** 7

**ArkTS mode:** ArkTS-Dyn since version 7; ArkTS-Sta since version 23.

<!--Device-OsAccountInfo-type: OsAccountType--><!--Device-OsAccountInfo-type: OsAccountType-End-->

**System capability:** SystemCapability.Account.OsAccount

