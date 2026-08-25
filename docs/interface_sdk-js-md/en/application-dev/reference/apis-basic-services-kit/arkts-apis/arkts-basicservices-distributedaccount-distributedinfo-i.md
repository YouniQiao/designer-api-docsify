# DistributedInfo

Represents the distributed information about an OS account.

**Since:** 7

**ArkTS mode:** ArkTS-Dyn since version 7; ArkTS-Sta since version 23.

**System capability:** SystemCapability.Account.OsAccount

## Modules to Import

```TypeScript
import { distributedAccount } from '@kit.BasicServicesKit';
```

## avatar

```TypeScript
avatar?: string
```

Avatar of the distributed account. By default, no value is passed in.

**Type:** string

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**System capability:** SystemCapability.Account.OsAccount

## event

```TypeScript
event: string
```

Login state of the distributed account. The state can be login, logout, token invalid, or logoff, which correspond to the following strings respectively:  
- Ohos.account.event.LOGIN  
- Ohos.account.event.LOGOUT  
- Ohos.account.event.TOKEN_INVALID  
- Ohos.account.event.LOGOFF

**Type:** string

**Since:** 7

**ArkTS mode:** ArkTS-Dyn since version 7; ArkTS-Sta since version 23.

**System capability:** SystemCapability.Account.OsAccount

## id

```TypeScript
id: string
```

UID of the distributed account. It must be a non-null string.

**Type:** string

**Since:** 7

**ArkTS mode:** ArkTS-Dyn since version 7; ArkTS-Sta since version 23.

**System capability:** SystemCapability.Account.OsAccount

## name

```TypeScript
name: string
```

Name of the distributed account. It must be a non-null string.

**Type:** string

**Since:** 7

**ArkTS mode:** ArkTS-Dyn since version 7; ArkTS-Sta since version 23.

**System capability:** SystemCapability.Account.OsAccount

## nickname

```TypeScript
nickname?: string
```

Nickname of the distributed account. By default, no value is passed in.

**Type:** string

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**System capability:** SystemCapability.Account.OsAccount

## scalableData

```TypeScript
scalableData?: object
```

Additional information about the distributed account, in the form of KV pairs. This parameter is left empty by default.

**Type:** object

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

**System capability:** SystemCapability.Account.OsAccount

## status

```TypeScript
readonly status?: DistributedAccountStatus
```

Status of the distributed account. The value is of the enumerated type. The default status is unlogged.

**Type:** [DistributedAccountStatus](arkts-basicservices-distributedaccount-distributedaccountstatus-e.md)

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

**System capability:** SystemCapability.Account.OsAccount
