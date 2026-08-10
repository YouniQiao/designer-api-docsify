# @ohos.bluetooth.opp

Provides methods to accessing bluetooth OPP(OBEX OBJECT PUSH Profile)-related capabilities.

**起始版本：** 16

**ArkTS模式：** ArkTS-Dyn起始版本为16；ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-unnamed-declare namespace opp--><!--Device-unnamed-declare namespace opp-End-->

**系统能力：** SystemCapability.Communication.Bluetooth.Core

## 导入模块

```TypeScript
import { opp } from 'kits/@kit.ConnectivityKit';
```

## 汇总

<!--Del-->
### 函数（系统接口）

| 名称 | 说明 |
| --- | --- |
| [createOppServerProfile](arkts-connectivity-opp-createoppserverprofile-f-sys.md#createoppserverprofile) | create the instance of OPP server profile. |
<!--DelEnd-->

<!--Del-->
### 接口（系统接口）

| 名称 | 说明 |
| --- | --- |
| [FileHolder](arkts-connectivity-opp-fileholder-i-sys.md) | Describes the file info for transfer |
| [OppServerProfile](arkts-connectivity-opp-oppserverprofile-i-sys.md) | Manager OPP server profile. |
| [OppTransferInformation](arkts-connectivity-opp-opptransferinformation-i-sys.md) | Describes the transferred file information. |
<!--DelEnd-->

<!--Del-->
### 枚举（系统接口）

| 名称 | 说明 |
| --- | --- |
| [DirectionType](arkts-connectivity-opp-directiontype-e-sys.md) | Enum for file transfer direction. |
| [TransferResult](arkts-connectivity-opp-transferresult-e-sys.md) | Enum for the file transfer result. |
| [TransferStatus](arkts-connectivity-opp-transferstatus-e-sys.md) | Enum for the file transfer status. |
<!--DelEnd-->

