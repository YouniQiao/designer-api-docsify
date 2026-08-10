# UserAuthResult

用户认证结果。认证通过时，返回认证类型和认证通过的令牌信息；认证不通过时，返回相应的错误码。该接口用于描述认证完成后的结果信息，应用可通过[IAuthCallback](arkts-userauthentication-userauth-iauthcallback-i.md)的onResult回调获取此结果。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

<!--Device-userAuth-interface UserAuthResult--><!--Device-userAuth-interface UserAuthResult-End-->

**System capability:** SystemCapability.UserIAM.UserAuth.Core

## Modules to Import

```TypeScript
import { userAuth } from 'kits/@kit.UserAuthenticationKit';
```

## authType

```TypeScript
authType?: UserAuthType
```

认证通过时，返回实际使用的认证类型。当[AuthParam](arkts-userauthentication-userauth-authparam-i.md)的authType指定了多种认证类型时，此字段标识用户实际选择并完成认证的类型。

**Type:** [UserAuthType](arkts-userauthentication-userauth-userauthtype-e.md)

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-UserAuthResult-authType?: UserAuthType--><!--Device-UserAuthResult-authType?: UserAuthType-End-->

**System capability:** SystemCapability.UserIAM.UserAuth.Core

## enrolledState

```TypeScript
enrolledState?: EnrolledState
```

认证通过时，返回注册凭据的状态。包含当前认证类型的凭据摘要和数量。应用可通过对比此值与之前保存的值，判断用户凭据是否发生变化。若启用了认证结果复用且之前认证使用的凭据已被删除（人脸或指纹），返回的enrolledState中credentialCount和credentialDigest均为0。

**Type:** [EnrolledState](arkts-userauthentication-userauth-enrolledstate-i.md)

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-UserAuthResult-enrolledState?: EnrolledState--><!--Device-UserAuthResult-enrolledState?: EnrolledState-End-->

**System capability:** SystemCapability.UserIAM.UserAuth.Core

## result

```TypeScript
result: int
```

用户认证结果。若成功返回SUCCESS(12500000)，若失败返回相应错误码。错误码包括：

- FAIL(12500001)：认证不通过。  
- CANCELED(12500003)：认证取消。  
- TIMEOUT(12500004)：认证超时。  
- LOCKED(12500009)：认证器锁定。  
- NOT_ENROLLED(12500010)：未注册凭据。  
- PIN_EXPIRED(12500013)：锁屏密码过期。

完整错误码列表参见[UserAuthResultCode](arkts-userauthentication-userauth-userauthresultcode-e.md)。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-UserAuthResult-result: int--><!--Device-UserAuthResult-result: int-End-->

**System capability:** SystemCapability.UserIAM.UserAuth.Core

## token

```TypeScript
token?: Uint8Array
```

认证通过时，返回认证通过的令牌信息。令牌最大长度为1024字节，包含用户身份认证的凭证，可用于后续的安全操作验证（如支付确认、敏感数据访问等）。令牌中包含认证时的挑战值，业务可通过验证挑战值来防止重放攻击。

**Type:** Uint8Array

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-UserAuthResult-token?: Uint8Array--><!--Device-UserAuthResult-token?: Uint8Array-End-->

**System capability:** SystemCapability.UserIAM.UserAuth.Core

