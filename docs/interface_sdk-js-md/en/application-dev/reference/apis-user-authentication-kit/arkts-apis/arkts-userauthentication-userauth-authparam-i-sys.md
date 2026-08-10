# AuthParam

用户认证相关参数。该接口用于配置用户认证的各项参数，包括挑战值、认证类型列表、认证信任等级、认证结果复用配置等。通过合理配置这些参数，可以满足不同业务场景下的认证需求。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

<!--Device-userAuth-interface AuthParam--><!--Device-userAuth-interface AuthParam-End-->

**System capability:** SystemCapability.UserIAM.UserAuth.Core

## Modules to Import

```TypeScript
import { userAuth } from 'kits/@kit.UserAuthenticationKit';
```

## credentialIdList

```TypeScript
credentialIdList?: Uint8Array[]
```

凭据ID列表，用于指定需要认证的凭据。当需要只认证特定凭据而非用户的所有凭据时传入此参数；若不传入或传入空数组，则默认认证该用户的所有凭据。

**Type:** Uint8Array[]

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AuthParam-credentialIdList?: Uint8Array[]--><!--Device-AuthParam-credentialIdList?: Uint8Array[]-End-->

**System capability:** SystemCapability.UserIAM.UserAuth.Core

**System API:** This is a system API.

## userId

```TypeScript
userId?: int
```

待认证的目标用户ID，用于指定需要认证的用户。当需要认证特定用户而非当前登录用户时传入此参数；若不传入则默认使用当前登录用户的ID。取值为非负整数。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Default:** The ID of the current user. The value is a positive integer greater than or equal to 0.

**Since:** 18

**ArkTS mode:** ArkTS-Dyn since version 18; ArkTS-Sta since version 23.

<!--Device-AuthParam-userId?: int--><!--Device-AuthParam-userId?: int-End-->

**System capability:** SystemCapability.UserIAM.UserAuth.Core

**System API:** This is a system API.

