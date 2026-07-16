# ScanResults

Describes the contents of the scan results.

**Since:** 26.0.0

<!--Device-scan-interface ScanResults--><!--Device-scan-interface ScanResults-End-->

**System capability:** SystemCapability.Communication.NearLink.Base

## Modules to Import

```TypeScript
import { scan } from '@kit.ConnectivityKit';
```

## address

```TypeScript
address: string
```

Address of the remote device.The length is 17, and the value consists of hexadecimal digits and colons (:), for example, 11:22:33:AA:BB:FF.

**Type:** string

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-ScanResults-address: string--><!--Device-ScanResults-address: string-End-->

**System capability:** SystemCapability.Communication.NearLink.Base

## data

```TypeScript
data: ArrayBuffer
```

The raw data.

**Type:** ArrayBuffer

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-ScanResults-data: ArrayBuffer--><!--Device-ScanResults-data: ArrayBuffer-End-->

**System capability:** SystemCapability.Communication.NearLink.Base

## deviceClass

```TypeScript
deviceClass?: nearlinkConstant.DeviceClass
```

Indicates the device class.

**Type:** nearlinkConstant.DeviceClass

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-ScanResults-deviceClass?: nearlinkConstant.DeviceClass--><!--Device-ScanResults-deviceClass?: nearlinkConstant.DeviceClass-End-->

**System capability:** SystemCapability.Communication.NearLink.Base

## deviceName

```TypeScript
deviceName: string
```

Device name of the remote device.

**Type:** string

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-ScanResults-deviceName: string--><!--Device-ScanResults-deviceName: string-End-->

**System capability:** SystemCapability.Communication.NearLink.Base

## isConnectable

```TypeScript
isConnectable: boolean
```

Indicates whether the remote device is connectable.

**Type:** boolean

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-ScanResults-isConnectable: boolean--><!--Device-ScanResults-isConnectable: boolean-End-->

**System capability:** SystemCapability.Communication.NearLink.Base

## rssi

```TypeScript
rssi: number
```

RSSI of the remote device.Unit: dBm. The value is an integer within [-128,127], and the value 127 indicates an invalid RSSI.

**Type:** number

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-ScanResults-rssi: int--><!--Device-ScanResults-rssi: int-End-->

**System capability:** SystemCapability.Communication.NearLink.Base

