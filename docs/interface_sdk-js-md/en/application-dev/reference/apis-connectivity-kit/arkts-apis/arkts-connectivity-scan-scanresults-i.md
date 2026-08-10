# ScanResults

扫描结果的内容。

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

<!--Device-scan-interface ScanResults--><!--Device-scan-interface ScanResults-End-->

**System capability:** SystemCapability.Communication.NearLink.Base

## Modules to Import

```TypeScript
import { scan } from 'kits/@kit.ConnectivityKit';
```

## address

```TypeScript
address: string
```

远端设备的地址。长度为17，由十六进制数字和冒号组成，例如：11:22:33:AA:BB:FF。

**Type:** string

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ScanResults-address: string--><!--Device-ScanResults-address: string-End-->

**System capability:** SystemCapability.Communication.NearLink.Base

## data

```TypeScript
data: ArrayBuffer
```

原始数据。

**Type:** ArrayBuffer

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ScanResults-data: ArrayBuffer--><!--Device-ScanResults-data: ArrayBuffer-End-->

**System capability:** SystemCapability.Communication.NearLink.Base

## deviceClass

```TypeScript
deviceClass?: nearlinkConstant.DeviceClass
```

设备类型。

**Type:** nearlinkConstant.DeviceClass

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ScanResults-deviceClass?: nearlinkConstant.DeviceClass--><!--Device-ScanResults-deviceClass?: nearlinkConstant.DeviceClass-End-->

**System capability:** SystemCapability.Communication.NearLink.Base

## deviceName

```TypeScript
deviceName: string
```

外围设备的设备名称。最大长度为26。

**Type:** string

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ScanResults-deviceName: string--><!--Device-ScanResults-deviceName: string-End-->

**System capability:** SystemCapability.Communication.NearLink.Base

## isConnectable

```TypeScript
isConnectable: boolean
```

广播是否可连接。

**Type:** boolean

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ScanResults-isConnectable: boolean--><!--Device-ScanResults-isConnectable: boolean-End-->

**System capability:** SystemCapability.Communication.NearLink.Base

## rssi

```TypeScript
rssi: int
```

外围设备的RSSI。单位为： 分贝毫瓦，取值范围为全体整数，取值为127时表示无效值。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ScanResults-rssi: int--><!--Device-ScanResults-rssi: int-End-->

**System capability:** SystemCapability.Communication.NearLink.Base

