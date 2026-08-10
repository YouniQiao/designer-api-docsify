# CallStateInfo

Indicates call state and number.

**起始版本：** 11

**ArkTS模式：** ArkTS-Dyn起始版本为11；ArkTS-Sta起始版本为23。

<!--Device-observer-export interface CallStateInfo--><!--Device-observer-export interface CallStateInfo-End-->

**系统能力：** SystemCapability.Telephony.StateRegistry

## 导入模块

```TypeScript
import { observer } from 'kits/@kit.TelephonyKit';
```

## number

```TypeScript
number: string
```

Indicates call number.

**类型：** string

**起始版本：** 11

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为11。

<!--Device-CallStateInfo-number: string--><!--Device-CallStateInfo-number: string-End-->

**系统能力：** SystemCapability.Telephony.StateRegistry

## state

```TypeScript
state: CallState
```

Indicates call state.

**类型：** [CallState](arkts-telephony-call-callstate-e.md)

**起始版本：** 11

**ArkTS模式：** ArkTS-Dyn起始版本为11；ArkTS-Sta起始版本为23。

<!--Device-CallStateInfo-state: CallState--><!--Device-CallStateInfo-state: CallState-End-->

**系统能力：** SystemCapability.Telephony.StateRegistry

## teleNumber

```TypeScript
teleNumber: string
```

Indicates call number.

**类型：** string

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

<!--Device-CallStateInfo-teleNumber: string--><!--Device-CallStateInfo-teleNumber: string-End-->

**系统能力：** SystemCapability.Telephony.StateRegistry

