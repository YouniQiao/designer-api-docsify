# SignalInformation

网络信号强度信息对象。

**起始版本：** 6

**ArkTS模式：** ArkTS-Dyn起始版本为6；ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Telephony.CoreService

## 导入模块

```TypeScript
import { radio } from '@kit.TelephonyKit';
```

## dBm

```TypeScript
dBm: int
```

网络信号强度，范围为[-140, 140]，超出范围返回错误。

**类型：** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**起始版本：** 9

**ArkTS模式：** ArkTS-Dyn起始版本为9；ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Telephony.CoreService

## signalLevel

```TypeScript
signalLevel: int
```

网络信号强度等级，范围为[0, 5]，超出范围返回错误。

**类型：** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**起始版本：** 6

**ArkTS模式：** ArkTS-Dyn起始版本为6；ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Telephony.CoreService

## signalType

```TypeScript
signalType: NetworkType
```

网络信号强度类型。

**类型：** NetworkType

**起始版本：** 6

**ArkTS模式：** ArkTS-Dyn起始版本为6；ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Telephony.CoreService
