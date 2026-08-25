# BluetoothScanInfo（系统接口）

蓝牙扫描信息。

**起始版本：** 10

**ArkTS模式：** ArkTS-Dyn起始版本为10；ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Location.Location.Core

**系统接口：** 此接口为系统接口。

## 导入模块

```TypeScript
import { geoLocationManager } from '@kit.LocationKit';
```

## deviceName

```TypeScript
deviceName: string
```

蓝牙设备名称。

**类型：** string

**起始版本：** 10

**ArkTS模式：** ArkTS-Dyn起始版本为10；ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Location.Location.Core

**系统接口：** 此接口为系统接口。

## macAddress

```TypeScript
macAddress: string
```

蓝牙设备的MAC地址。

**类型：** string

**起始版本：** 10

**ArkTS模式：** ArkTS-Dyn起始版本为10；ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Location.Location.Core

**系统接口：** 此接口为系统接口。

## rssi

```TypeScript
rssi: int
```

蓝牙设备的信号强度(dBm)。

**类型：** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**起始版本：** 10

**ArkTS模式：** ArkTS-Dyn起始版本为10；ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Location.Location.Core

**系统接口：** 此接口为系统接口。

## timestamp

```TypeScript
timestamp: long
```

时间戳，单位微秒。

**类型：** ArkTS-Dyn: number  <br>ArkTS-Sta：long

**起始版本：** 10

**ArkTS模式：** ArkTS-Dyn起始版本为10；ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Location.Location.Core

**系统接口：** 此接口为系统接口。
