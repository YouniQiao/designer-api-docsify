# AuthIntent (System API)

表示认证意图的枚举。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-osAccount-enum AuthIntent--><!--Device-osAccount-enum AuthIntent-End-->

**System capability:** SystemCapability.Account.OsAccount

**System API:** This is a system API.

## UNLOCK

```TypeScript
UNLOCK = 1
```

解锁意图。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-AuthIntent-UNLOCK = 1--><!--Device-AuthIntent-UNLOCK = 1-End-->

**System capability:** SystemCapability.Account.OsAccount

**System API:** This is a system API.

## SILENT_AUTH

```TypeScript
SILENT_AUTH = 2
```

静默认证意图。

**Since:** 14

**ArkTS mode:** ArkTS-Dyn since version 14; ArkTS-Sta since version 23.

<!--Device-AuthIntent-SILENT_AUTH = 2--><!--Device-AuthIntent-SILENT_AUTH = 2-End-->

**System capability:** SystemCapability.Account.OsAccount

**System API:** This is a system API.

## QUESTION_AUTH

```TypeScript
QUESTION_AUTH = 3
```

密保问题认证意图。

**Since:** 14

**ArkTS mode:** ArkTS-Dyn since version 14; ArkTS-Sta since version 23.

<!--Device-AuthIntent-QUESTION_AUTH = 3--><!--Device-AuthIntent-QUESTION_AUTH = 3-End-->

**System capability:** SystemCapability.Account.OsAccount

**System API:** This is a system API.

## ABANDONED_PIN_AUTH

```TypeScript
ABANDONED_PIN_AUTH = 4
```

废弃PIN码认证意图。用户修改锁屏密码后，旧的PIN码被废弃。废弃PIN存在期间，用户如果忘记密码可以通过废弃PIN认证通过后重置锁屏密码。

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

<!--Device-AuthIntent-ABANDONED_PIN_AUTH = 4--><!--Device-AuthIntent-ABANDONED_PIN_AUTH = 4-End-->

**System capability:** SystemCapability.Account.OsAccount

**System API:** This is a system API.

