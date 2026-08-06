# OsAccountSwitchEventData (System API)

Defines the event that indicates the start or end of a foreground-background OS account switchover.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-osAccount-interface OsAccountSwitchEventData--><!--Device-osAccount-interface OsAccountSwitchEventData-End-->

**System capability:** SystemCapability.Account.OsAccount

**System API:** This is a system API.

## displayId

```TypeScript
displayId?: long
```

ID of the logical display where the switchover occurs. The default value is **0**.

**Type:** long

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-OsAccountSwitchEventData-displayId?: long--><!--Device-OsAccountSwitchEventData-displayId?: long-End-->

**System capability:** SystemCapability.Account.OsAccount

**System API:** This is a system API.

## fromAccountId

```TypeScript
fromAccountId: int
```

ID of the source OS account.

**Type:** int

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-OsAccountSwitchEventData-fromAccountId: int--><!--Device-OsAccountSwitchEventData-fromAccountId: int-End-->

**System capability:** SystemCapability.Account.OsAccount

**System API:** This is a system API.

## toAccountId

```TypeScript
toAccountId: int
```

ID of the target OS account.

**Type:** int

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-OsAccountSwitchEventData-toAccountId: int--><!--Device-OsAccountSwitchEventData-toAccountId: int-End-->

**System capability:** SystemCapability.Account.OsAccount

**System API:** This is a system API.

