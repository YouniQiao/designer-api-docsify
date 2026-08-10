# CellInformation

Obtains current cell information.

**起始版本：** 8

**ArkTS模式：** ArkTS-Dyn起始版本为8；ArkTS-Sta起始版本为23。

<!--Device-radio-export interface CellInformation--><!--Device-radio-export interface CellInformation-End-->

**系统能力：** SystemCapability.Telephony.CoreService

## 导入模块

```TypeScript
import { radio } from 'kits/@kit.TelephonyKit';
```

## networkType

```TypeScript
networkType: NetworkType
```

Obtains the network type of the serving cell.

An application can call this method to determine the network type that the child class uses.

**类型：** [NetworkType](../../apis-background-tasks-kit/arkts-apis/arkts-backgroundtasks-workscheduler-networktype-e.md)

**起始版本：** 8

**ArkTS模式：** ArkTS-Dyn起始版本为8；ArkTS-Sta起始版本为23。

<!--Device-CellInformation-networkType: NetworkType--><!--Device-CellInformation-networkType: NetworkType-End-->

**系统能力：** SystemCapability.Telephony.CoreService

## signalInformation

```TypeScript
signalInformation: SignalInformation
```

An abstract method of the parent class whose implementation depends on the child classes.Returned child class objects vary according to the network type.Returns child class objects specific to the network type.

**类型：** [SignalInformation](arkts-telephony-radio-signalinformation-i.md)

**起始版本：** 8

**ArkTS模式：** ArkTS-Dyn起始版本为8；ArkTS-Sta起始版本为23。

<!--Device-CellInformation-signalInformation: SignalInformation--><!--Device-CellInformation-signalInformation: SignalInformation-End-->

**系统能力：** SystemCapability.Telephony.CoreService

