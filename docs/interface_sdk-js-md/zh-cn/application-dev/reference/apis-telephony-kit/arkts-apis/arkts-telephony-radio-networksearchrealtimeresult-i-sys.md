# NetworkSearchRealTimeResult（系统接口）

Indicates the results of manual network scan

**起始版本：** 23

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为23。

<!--Device-radio-export interface NetworkSearchRealTimeResult--><!--Device-radio-export interface NetworkSearchRealTimeResult-End-->

**系统能力：** SystemCapability.Telephony.CoreService

**系统接口：** 此接口为系统接口。

## 导入模块

```TypeScript
import { radio } from 'kits/@kit.TelephonyKit';
```

## isFinish

```TypeScript
isFinish: boolean
```

Indicates whether the network search was stop.

**类型：** boolean

**起始版本：** 23

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为23。

<!--Device-NetworkSearchRealTimeResult-isFinish: boolean--><!--Device-NetworkSearchRealTimeResult-isFinish: boolean-End-->

**系统能力：** SystemCapability.Telephony.CoreService

**系统接口：** 此接口为系统接口。

## networkInfos

```TypeScript
networkInfos: Array<NetworkInformation>
```

the network search results.

**类型：** Array&lt;NetworkInformation&gt;

**起始版本：** 23

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为23。

<!--Device-NetworkSearchRealTimeResult-networkInfos: Array<NetworkInformation>--><!--Device-NetworkSearchRealTimeResult-networkInfos: Array<NetworkInformation>-End-->

**系统能力：** SystemCapability.Telephony.CoreService

**系统接口：** 此接口为系统接口。

