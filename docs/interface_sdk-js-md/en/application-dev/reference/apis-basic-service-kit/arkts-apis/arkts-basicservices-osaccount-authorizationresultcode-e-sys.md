# AuthorizationResultCode (System API)

表示授权结果码的枚举。

**Since:** 24

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 24.

<!--Device-osAccount-enum AuthorizationResultCode--><!--Device-osAccount-enum AuthorizationResultCode-End-->

**System capability:** SystemCapability.Account.OsAccount

**System API:** This is a system API.

## AUTHORIZATION_SUCCESS

```TypeScript
AUTHORIZATION_SUCCESS = 0
```

表示授权成功。

**Since:** 24

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AuthorizationResultCode-AUTHORIZATION_SUCCESS = 0--><!--Device-AuthorizationResultCode-AUTHORIZATION_SUCCESS = 0-End-->

**System capability:** SystemCapability.Account.OsAccount

**System API:** This is a system API.

## AUTHORIZATION_CANCELED

```TypeScript
AUTHORIZATION_CANCELED = 12300301
```

表示授权已取消。

**Since:** 24

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AuthorizationResultCode-AUTHORIZATION_CANCELED = 12300301--><!--Device-AuthorizationResultCode-AUTHORIZATION_CANCELED = 12300301-End-->

**System capability:** SystemCapability.Account.OsAccount

**System API:** This is a system API.

## AUTHORIZATION_INTERACTION_NOT_ALLOWED

```TypeScript
AUTHORIZATION_INTERACTION_NOT_ALLOWED = 12300302
```

表示服务因不允许用户交互而拒绝授权。

可能原因：

1. 调用者位于后台；2. isInteractionAllowed选项的值为false；3. 指定的交互上下文无效。

**Since:** 24

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AuthorizationResultCode-AUTHORIZATION_INTERACTION_NOT_ALLOWED = 12300302--><!--Device-AuthorizationResultCode-AUTHORIZATION_INTERACTION_NOT_ALLOWED = 12300302-End-->

**System capability:** SystemCapability.Account.OsAccount

**System API:** This is a system API.

## AUTHORIZATION_DENIED

```TypeScript
AUTHORIZATION_DENIED = 12300303
```

表示因不符合授权规则，如账号类型不是管理员、设备类型不支持等原因而拒绝授权。

**Since:** 24

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AuthorizationResultCode-AUTHORIZATION_DENIED = 12300303--><!--Device-AuthorizationResultCode-AUTHORIZATION_DENIED = 12300303-End-->

**System capability:** SystemCapability.Account.OsAccount

**System API:** This is a system API.

## AUTHORIZATION_SERVICE_BUSY

```TypeScript
AUTHORIZATION_SERVICE_BUSY = 12300304
```

表示服务忙碌。

可能原因：正在处理其他授权。

**Since:** 24

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AuthorizationResultCode-AUTHORIZATION_SERVICE_BUSY = 12300304--><!--Device-AuthorizationResultCode-AUTHORIZATION_SERVICE_BUSY = 12300304-End-->

**System capability:** SystemCapability.Account.OsAccount

**System API:** This is a system API.

