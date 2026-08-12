# AuthParam

Defines the user authentication parameters. This API is used to configure user authentication parameters, including the challenge value, authentication type list, authentication trust level, and authentication result reuse configuration. By properly configuring these parameters, you can meet authentication requirements in different service scenarios.

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

<!--Device-userAuth-interface AuthParam--><!--Device-userAuth-interface AuthParam-End-->

**System capability:** SystemCapability.UserIAM.UserAuth.Core

## Modules to Import

```TypeScript
import { userAuth } from '@kit.UserAuthenticationKit';
```

## credentialIdList

```TypeScript
credentialIdList?: Uint8Array[]
```

List of IDs for credentials to be authenticated. This parameter is passed when only specific credentials, rather than all credentials of the user, need to be authenticated. If not passed or an empty array is passed, all credentials of the user are authenticated by default.

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

ID of the target user to be authenticated. This parameter is passed when a specific user, rather than the currently logged-in user, needs to be authenticated. If not passed, the ID of the currently logged-in user is used by default. The value is a non-negative integer.

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Default:** The ID of the current user. The value is a positive integer greater than or equal to 0.

**Since:** 18

**ArkTS mode:** ArkTS-Dyn since version 18; ArkTS-Sta since version 23.

<!--Device-AuthParam-userId?: int--><!--Device-AuthParam-userId?: int-End-->

**System capability:** SystemCapability.UserIAM.UserAuth.Core

**System API:** This is a system API.

