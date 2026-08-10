# AVCallState

通话状态相关属性。

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

<!--Device-avSession-interface AVCallState--><!--Device-avSession-interface AVCallState-End-->

**System capability:** SystemCapability.Multimedia.AVSession.Core

## Modules to Import

```TypeScript
import { avSession } from 'kits/@kit.AVSessionKit';
```

## muted

```TypeScript
muted: boolean
```

表示通话mic是否静音。 true表示是静音，false表示不是静音。

**Type:** boolean

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AVCallState-muted: boolean--><!--Device-AVCallState-muted: boolean-End-->

**System capability:** SystemCapability.Multimedia.AVSession.Core

## state

```TypeScript
state: CallState
```

当前通话状态。

**Type:** [CallState](../../apis-telephony-kit/arkts-apis/arkts-telephony-call-callstate-e.md)

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AVCallState-state: CallState--><!--Device-AVCallState-state: CallState-End-->

**System capability:** SystemCapability.Multimedia.AVSession.Core

