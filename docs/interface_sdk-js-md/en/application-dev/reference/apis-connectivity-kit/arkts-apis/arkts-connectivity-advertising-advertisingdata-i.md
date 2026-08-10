# AdvertisingData

广播数据。

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

<!--Device-advertising-interface AdvertisingData--><!--Device-advertising-interface AdvertisingData-End-->

**System capability:** SystemCapability.Communication.NearLink.Base

## Modules to Import

```TypeScript
import { advertising } from 'kits/@kit.ConnectivityKit';
```

## includeDeviceName

```TypeScript
includeDeviceName?: boolean
```

指示是否包含设备名称。默认值： 默认值：false。

**Type:** boolean

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AdvertisingData-includeDeviceName?: boolean--><!--Device-AdvertisingData-includeDeviceName?: boolean-End-->

**System capability:** SystemCapability.Communication.NearLink.Base

## manufacturerData

```TypeScript
manufacturerData?: ManufacturerData[]
```

制造商数据。

**Type:** [ManufacturerData](arkts-connectivity-advertising-manufacturerdata-i.md)[]

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AdvertisingData-manufacturerData?: ManufacturerData[]--><!--Device-AdvertisingData-manufacturerData?: ManufacturerData[]-End-->

**System capability:** SystemCapability.Communication.NearLink.Base

## serviceData

```TypeScript
serviceData?: ServiceData[]
```

服务数据。

**Type:** [ServiceData](arkts-connectivity-advertising-servicedata-i.md)[]

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AdvertisingData-serviceData?: ServiceData[]--><!--Device-AdvertisingData-serviceData?: ServiceData[]-End-->

**System capability:** SystemCapability.Communication.NearLink.Base

## serviceUuids

```TypeScript
serviceUuids?: string[]
```

指定的服务UUID。UUID的长度必须为36，由36位十六进制数字和“-”组成。例如：FFFFFFFF-1234-5678-ABCD-000000001234，表示128位的标识符。

**Type:** string[]

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AdvertisingData-serviceUuids?: string[]--><!--Device-AdvertisingData-serviceUuids?: string[]-End-->

**System capability:** SystemCapability.Communication.NearLink.Base

