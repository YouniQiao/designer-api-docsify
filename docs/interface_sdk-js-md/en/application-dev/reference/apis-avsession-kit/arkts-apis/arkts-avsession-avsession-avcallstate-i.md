# AVCallState

Used to indicate the call state of the current call.

**Since:** 11

<!--Device-avSession-interface AVCallState--><!--Device-avSession-interface AVCallState-End-->

**System capability:** SystemCapability.Multimedia.AVSession.Core

## Modules to Import

```TypeScript
import { avSession } from '@kit.AVSessionKit';
```

## muted

```TypeScript
muted: boolean
```

Current muted status.

**Type:** boolean

**Since:** 11

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AVCallState-muted: boolean--><!--Device-AVCallState-muted: boolean-End-->

**System capability:** SystemCapability.Multimedia.AVSession.Core

## state

```TypeScript
state: CallState
```

Current call state. See {@link CallState}

**Type:** CallState

**Since:** 11

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AVCallState-state: CallState--><!--Device-AVCallState-state: CallState-End-->

**System capability:** SystemCapability.Multimedia.AVSession.Core

