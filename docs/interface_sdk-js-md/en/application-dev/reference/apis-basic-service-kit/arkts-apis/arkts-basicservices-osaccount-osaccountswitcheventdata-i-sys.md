# OsAccountSwitchEventData (System API)

表示系统账号前后台开始切换和结束切换事件的数据结构。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-osAccount-interface OsAccountSwitchEventData--><!--Device-osAccount-interface OsAccountSwitchEventData-End-->

**System capability:** SystemCapability.Account.OsAccount

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { osAccount } from 'kits/@kit.BasicServicesKit';
```

## displayId

```TypeScript
displayId?: long
```

切换事件发生的逻辑屏ID，默认值为0。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：long

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-OsAccountSwitchEventData-displayId?: long--><!--Device-OsAccountSwitchEventData-displayId?: long-End-->

**System capability:** SystemCapability.Account.OsAccount

**System API:** This is a system API.

## fromAccountId

```TypeScript
fromAccountId: int
```

切换来源系统账号ID。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-OsAccountSwitchEventData-fromAccountId: int--><!--Device-OsAccountSwitchEventData-fromAccountId: int-End-->

**System capability:** SystemCapability.Account.OsAccount

**System API:** This is a system API.

## toAccountId

```TypeScript
toAccountId: int
```

切换目标系统账号ID。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-OsAccountSwitchEventData-toAccountId: int--><!--Device-OsAccountSwitchEventData-toAccountId: int-End-->

**System capability:** SystemCapability.Account.OsAccount

**System API:** This is a system API.

