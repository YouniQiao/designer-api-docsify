# ControlEvent（系统接口）

Defines a control event.

**起始版本：** 20

**ArkTS模式：** ArkTS-Dyn起始版本为20；ArkTS-Sta起始版本为23。

<!--Device-onScreen-export interface ControlEvent--><!--Device-onScreen-export interface ControlEvent-End-->

**系统能力：** SystemCapability.MultimodalAwareness.OnScreenAwareness

**系统接口：** 此接口为系统接口。

## 导入模块

```TypeScript
import { onScreen } from 'kits/@kit.MultimodalAwarenessKit';
```

## eventType

```TypeScript
eventType: EventType
```

Control event type.

**类型：** [EventType](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-screenlock-eventtype-t-sys.md)

**起始版本：** 20

**ArkTS模式：** ArkTS-Dyn起始版本为20；ArkTS-Sta起始版本为23。

<!--Device-ControlEvent-eventType: EventType--><!--Device-ControlEvent-eventType: EventType-End-->

**系统能力：** SystemCapability.MultimodalAwareness.OnScreenAwareness

**系统接口：** 此接口为系统接口。

## hookId

```TypeScript
hookId?: long
```

Hook ID corresponding to the control event. The hook ID and the session ID can be obtained from   
[PageContent](arkts-multimodalawareness-onscreen-pagecontent-i-sys.md) of a session.

**类型：** ArkTS-Dyn: number  <br>ArkTS-Sta：long

**起始版本：** 20

**ArkTS模式：** ArkTS-Dyn起始版本为20；ArkTS-Sta起始版本为23。

<!--Device-ControlEvent-hookId?: long--><!--Device-ControlEvent-hookId?: long-End-->

**系统能力：** SystemCapability.MultimodalAwareness.OnScreenAwareness

**系统接口：** 此接口为系统接口。

## sessionId

```TypeScript
sessionId: long
```

ID of the session to be operated. The hook ID and the session ID can be obtained from   
[PageContent](arkts-multimodalawareness-onscreen-pagecontent-i-sys.md) of a session.

**类型：** ArkTS-Dyn: number  <br>ArkTS-Sta：long

**起始版本：** 20

**ArkTS模式：** ArkTS-Dyn起始版本为20；ArkTS-Sta起始版本为23。

<!--Device-ControlEvent-sessionId: long--><!--Device-ControlEvent-sessionId: long-End-->

**系统能力：** SystemCapability.MultimodalAwareness.OnScreenAwareness

**系统接口：** 此接口为系统接口。

## windowId

```TypeScript
windowId: int
```

ID of the window to be operated.

**类型：** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**起始版本：** 20

**ArkTS模式：** ArkTS-Dyn起始版本为20；ArkTS-Sta起始版本为23。

<!--Device-ControlEvent-windowId: int--><!--Device-ControlEvent-windowId: int-End-->

**系统能力：** SystemCapability.MultimodalAwareness.OnScreenAwareness

**系统接口：** 此接口为系统接口。

