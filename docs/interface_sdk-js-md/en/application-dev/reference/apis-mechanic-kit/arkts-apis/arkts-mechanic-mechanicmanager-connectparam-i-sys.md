# ConnectParam (System API)

连接参数定义

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

<!--Device-mechanicManager-export interface ConnectParam--><!--Device-mechanicManager-export interface ConnectParam-End-->

**System capability:** SystemCapability.Mechanic.Core

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { mechanicManager } from 'kits/@kit.MechanicKit';
```

## custdata

```TypeScript
custdata: string
```

发现设备时携带的数据数据必须符合以下格式：|类型|值|类型|值|。每个特定类型的value'len是预定义的长度支持的类型和版本如下表所示。  
-----------------------------------------------------------------  
类型|值|值len |api级别  
-----------------------------------------------------------------  
0x01 |三轴重力传感器值| 3Byte |26.0.0  
-----------------------------------------------------------------  
0x02|MAC地址第1字节偏移|1字节|26.0.0  
-----------------------------------------------------------------  
0x03 |配对广播|1字节|26.0.0  
-----------------------------------------------------------------  
0x04 |目标设备标识|4字节|26.0.0  
-----------------------------------------------------------------。

**Type:** string

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ConnectParam-custdata: string--><!--Device-ConnectParam-custdata: string-End-->

**System capability:** SystemCapability.Mechanic.Core

**System API:** This is a system API.

## deviceName

```TypeScript
deviceName?: string
```

具身设备名称。

**Type:** string

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ConnectParam-deviceName?: string--><!--Device-ConnectParam-deviceName?: string-End-->

**System capability:** SystemCapability.Mechanic.Core

**System API:** This is a system API.

## identifier

```TypeScript
identifier?: int
```

当前设备标识。取值限定为整数。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ConnectParam-identifier?: int--><!--Device-ConnectParam-identifier?: int-End-->

**System capability:** SystemCapability.Mechanic.Core

**System API:** This is a system API.

