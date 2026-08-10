# UserAuthResultCode

表示返回码的枚举。该枚举定义了用户认证操作可能返回的所有结果码，包括成功码和各类错误码。应用可根据返回码判断认证结果，并采取相应的处理措施。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-userAuth-enum UserAuthResultCode--><!--Device-userAuth-enum UserAuthResultCode-End-->

**System capability:** SystemCapability.UserIAM.UserAuth.Core

## AUTH_TOKEN_CHECK_FAILED

```TypeScript
AUTH_TOKEN_CHECK_FAILED = 12500015
```

AuthToken校验失败。verifyAuthToken系统接口错误码，表示验证的AuthToken完整性校验失败，令牌可能被篡改或损坏。

**Since:** 18

**ArkTS mode:** ArkTS-Dyn since version 18; ArkTS-Sta since version 23.

<!--Device-UserAuthResultCode-AUTH_TOKEN_CHECK_FAILED = 12500015--><!--Device-UserAuthResultCode-AUTH_TOKEN_CHECK_FAILED = 12500015-End-->

**System capability:** SystemCapability.UserIAM.UserAuth.Core

**System API:** This is a system API.

## AUTH_TOKEN_EXPIRED

```TypeScript
AUTH_TOKEN_EXPIRED = 12500016
```

AuthToken已过期。verifyAuthToken系统接口错误码，表示AuthToken的签发时间至发起验证时的时间间隔超过传入的最大有效时长（allowableDuration）。

**Since:** 18

**ArkTS mode:** ArkTS-Dyn since version 18; ArkTS-Sta since version 23.

<!--Device-UserAuthResultCode-AUTH_TOKEN_EXPIRED = 12500016--><!--Device-UserAuthResultCode-AUTH_TOKEN_EXPIRED = 12500016-End-->

**System capability:** SystemCapability.UserIAM.UserAuth.Core

**System API:** This is a system API.

## REUSE_AUTH_RESULT_FAILED

```TypeScript
REUSE_AUTH_RESULT_FAILED = 12500017
```

复用认证结果失败。queryReusableAuthResult系统接口错误码，表示查询可复用的身份认证结果失败，可能原因包括：不存在满足复用条件的认证结果、认证结果已失效或凭据已变更。

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

<!--Device-UserAuthResultCode-REUSE_AUTH_RESULT_FAILED = 12500017--><!--Device-UserAuthResultCode-REUSE_AUTH_RESULT_FAILED = 12500017-End-->

**System capability:** SystemCapability.UserIAM.UserAuth.Core

**System API:** This is a system API.

