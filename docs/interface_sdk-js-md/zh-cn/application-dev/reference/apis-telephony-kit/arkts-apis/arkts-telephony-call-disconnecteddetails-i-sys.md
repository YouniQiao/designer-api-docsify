# DisconnectedDetails（系统接口）

Indicates the cause of a call disconnection.

**起始版本：** 9

**ArkTS模式：** ArkTS-Dyn起始版本为9；ArkTS-Sta起始版本为23。

<!--Device-call-export interface DisconnectedDetails--><!--Device-call-export interface DisconnectedDetails-End-->

**系统能力：** SystemCapability.Telephony.CallManager

**系统接口：** 此接口为系统接口。

## 导入模块

```TypeScript
import { call } from 'kits/@kit.TelephonyKit';
```

## message

```TypeScript
message: string
```

Indicates the message for ending the call.

**类型：** string

**起始版本：** 9

**ArkTS模式：** ArkTS-Dyn起始版本为9；ArkTS-Sta起始版本为23。

<!--Device-DisconnectedDetails-message: string--><!--Device-DisconnectedDetails-message: string-End-->

**系统能力：** SystemCapability.Telephony.CallManager

**系统接口：** 此接口为系统接口。

## reason

```TypeScript
reason: DisconnectedReason
```

Indicates the reason for ending the call.

**类型：** [DisconnectedReason](../../apis-connectivity-kit/arkts-apis/arkts-connectivity-wifimanager-disconnectedreason-e-sys.md)

**起始版本：** 9

**ArkTS模式：** ArkTS-Dyn起始版本为9；ArkTS-Sta起始版本为23。

<!--Device-DisconnectedDetails-reason: DisconnectedReason--><!--Device-DisconnectedDetails-reason: DisconnectedReason-End-->

**系统能力：** SystemCapability.Telephony.CallManager

**系统接口：** 此接口为系统接口。

