# SimStateData

Indicates SIM card type and status.

**起始版本：** 7

**ArkTS模式：** ArkTS-Dyn起始版本为7；ArkTS-Sta起始版本为23。

<!--Device-observer-export interface SimStateData--><!--Device-observer-export interface SimStateData-End-->

**系统能力：** SystemCapability.Telephony.StateRegistry

## 导入模块

```TypeScript
import { observer } from 'kits/@kit.TelephonyKit';
```

## reason

```TypeScript
reason: LockReason
```

Indicates the SIM card lock type.

**类型：** [LockReason](arkts-telephony-observer-lockreason-e.md)

**起始版本：** 8

**ArkTS模式：** ArkTS-Dyn起始版本为8；ArkTS-Sta起始版本为23。

<!--Device-SimStateData-reason: LockReason--><!--Device-SimStateData-reason: LockReason-End-->

**系统能力：** SystemCapability.Telephony.StateRegistry

## state

```TypeScript
state: SimState
```

Indicates the SIM card states.

**类型：** [SimState](arkts-telephony-sim-simstate-e.md)

**起始版本：** 7

**ArkTS模式：** ArkTS-Dyn起始版本为7；ArkTS-Sta起始版本为23。

<!--Device-SimStateData-state: SimState--><!--Device-SimStateData-state: SimState-End-->

**系统能力：** SystemCapability.Telephony.StateRegistry

## type

```TypeScript
type: CardType
```

Indicates the SIM card type.

**类型：** [CardType](../../apis-connectivity-kit/arkts-apis/arkts-connectivity-cardemulation-cardtype-e.md)

**起始版本：** 7

**ArkTS模式：** ArkTS-Dyn起始版本为7；ArkTS-Sta起始版本为23。

<!--Device-SimStateData-type: CardType--><!--Device-SimStateData-type: CardType-End-->

**系统能力：** SystemCapability.Telephony.StateRegistry

