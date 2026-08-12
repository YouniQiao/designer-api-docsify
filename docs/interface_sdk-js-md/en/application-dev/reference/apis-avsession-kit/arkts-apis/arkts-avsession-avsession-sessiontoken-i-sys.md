# SessionToken (System API)

Session token. Used to judge the legitimacy of the session.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-avSession-interface SessionToken--><!--Device-avSession-interface SessionToken-End-->

**System capability:** SystemCapability.Multimedia.AVSession.Manager

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { avSession } from '@kit.AVSessionKit';
```

## pid

```TypeScript
pid?: long
```

Process id of session

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：long

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Required permissions:** ohos.permission.MANAGE_MEDIA_RESOURCES

<!--Device-SessionToken-pid?: long--><!--Device-SessionToken-pid?: long-End-->

**System capability:** SystemCapability.Multimedia.AVSession.Manager

**System API:** This is a system API.

## sessionId

```TypeScript
sessionId: string
```

The unique session id of the avsession object

**Type:** string

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Required permissions:** ohos.permission.MANAGE_MEDIA_RESOURCES

<!--Device-SessionToken-sessionId: string--><!--Device-SessionToken-sessionId: string-End-->

**System capability:** SystemCapability.Multimedia.AVSession.Manager

**System API:** This is a system API.

## uid

```TypeScript
uid?: long
```

User id

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：long

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Required permissions:** ohos.permission.MANAGE_MEDIA_RESOURCES

<!--Device-SessionToken-uid?: long--><!--Device-SessionToken-uid?: long-End-->

**System capability:** SystemCapability.Multimedia.AVSession.Manager

**System API:** This is a system API.

