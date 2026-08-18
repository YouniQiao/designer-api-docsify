# ControlEvent (System API)

Defines a control event.

**Since:** 23

<!--Device-onScreen-export interface ControlEvent--><!--Device-onScreen-export interface ControlEvent-End-->

**System capability:** SystemCapability.MultimodalAwareness.OnScreenAwareness

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { onScreen } from '@kit.MultimodalAwarenessKit';
```

## eventType

```TypeScript
eventType: EventType
```

Control event type.

**Type:** EventType

**Since:** 23

<!--Device-ControlEvent-eventType: EventType--><!--Device-ControlEvent-eventType: EventType-End-->

**System capability:** SystemCapability.MultimodalAwareness.OnScreenAwareness

**System API:** This is a system API.

## hookId

```TypeScript
hookId?: long
```

Hook ID corresponding to the control event. The hook ID and the session ID can be obtained from [PageContent](arkts-multimodalawareness-onscreen-pagecontent-i-sys.md#pagecontent-system-api) of a session.

**Type:** long

**Since:** 23

<!--Device-ControlEvent-hookId?: long--><!--Device-ControlEvent-hookId?: long-End-->

**System capability:** SystemCapability.MultimodalAwareness.OnScreenAwareness

**System API:** This is a system API.

## sessionId

```TypeScript
sessionId: long
```

ID of the session to be operated. The hook ID and the session ID can be obtained from [PageContent](arkts-multimodalawareness-onscreen-pagecontent-i-sys.md#pagecontent-system-api) of a session.

**Type:** long

**Since:** 23

<!--Device-ControlEvent-sessionId: long--><!--Device-ControlEvent-sessionId: long-End-->

**System capability:** SystemCapability.MultimodalAwareness.OnScreenAwareness

**System API:** This is a system API.

## windowId

```TypeScript
windowId: int
```

ID of the window to be operated.

**Type:** int

**Since:** 23

<!--Device-ControlEvent-windowId: int--><!--Device-ControlEvent-windowId: int-End-->

**System capability:** SystemCapability.MultimodalAwareness.OnScreenAwareness

**System API:** This is a system API.

