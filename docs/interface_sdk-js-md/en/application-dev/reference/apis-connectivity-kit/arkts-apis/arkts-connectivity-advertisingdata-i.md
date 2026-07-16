# AdvertisingData

Describes the advertising data.

**Since:** 26.0.0

<!--Device-advertising-interface AdvertisingData--><!--Device-advertising-interface AdvertisingData-End-->

**System capability:** SystemCapability.Communication.NearLink.Base

## Modules to Import

```TypeScript
import { advertising } from '@kit.ConnectivityKit';
```

## includeDeviceName

```TypeScript
includeDeviceName?: boolean
```

Indicates whether the device name will be included.Default value: false.

**Type:** boolean

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-AdvertisingData-includeDeviceName?: boolean--><!--Device-AdvertisingData-includeDeviceName?: boolean-End-->

**System capability:** SystemCapability.Communication.NearLink.Base

## manufacturerData

```TypeScript
manufacturerData?: ManufacturerData[]
```

The specified manufacturer data.

**Type:** ManufacturerData[]

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-AdvertisingData-manufacturerData?: ManufacturerData[]--><!--Device-AdvertisingData-manufacturerData?: ManufacturerData[]-End-->

**System capability:** SystemCapability.Communication.NearLink.Base

## serviceData

```TypeScript
serviceData?: ServiceData[]
```

The specified service data.

**Type:** ServiceData[]

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-AdvertisingData-serviceData?: ServiceData[]--><!--Device-AdvertisingData-serviceData?: ServiceData[]-End-->

**System capability:** SystemCapability.Communication.NearLink.Base

## serviceUuids

```TypeScript
serviceUuids?: string[]
```

The specified service UUIDs.The length of each UUID must be 36, The value consists of 36 hexadecimal digits and hyphens (-),for example, FFFFFFFF-1234-5678-ABCD-000000001234, indicating a 128-bit identifier.

**Type:** string[]

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-AdvertisingData-serviceUuids?: string[]--><!--Device-AdvertisingData-serviceUuids?: string[]-End-->

**System capability:** SystemCapability.Communication.NearLink.Base

