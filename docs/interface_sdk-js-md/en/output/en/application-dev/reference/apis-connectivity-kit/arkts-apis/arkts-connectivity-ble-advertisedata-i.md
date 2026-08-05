# AdvertiseData

Describes the advertising data.

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

<!--Device-ble-interface AdvertiseData--><!--Device-ble-interface AdvertiseData-End-->

**System capability:** SystemCapability.Communication.Bluetooth.Core

## advertiseName

```TypeScript
advertiseName?: string
```

Indicates the local name data type in the advertisement packet. If both the property and \_\_\_JSDOC\_LINK\_DESC\_USD\_0\_\_\_ property are used together, the \_\_\_JSDOC\_LINK\_DESC\_USD\_1\_\_\_ property will ultimately take effect.

**Type:** string

**Since:** 23

**ArkTS mode:** ArkTS-Dyn since version 23; ArkTS-Sta since version 26.0.0.

**Required permissions:** ohos.permission.MANAGE_BLUETOOTH_ADVERTISER_NAME

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-AdvertiseData-advertiseName?: string--><!--Device-AdvertiseData-advertiseName?: string-End-->

**System capability:** SystemCapability.Communication.Bluetooth.Core

## includeDeviceName

```TypeScript
includeDeviceName?: boolean
```

Indicates whether the device name will be included in the advertisement packet.

**Type:** boolean

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AdvertiseData-includeDeviceName?: boolean--><!--Device-AdvertiseData-includeDeviceName?: boolean-End-->

**System capability:** SystemCapability.Communication.Bluetooth.Core

## includeTxPower

```TypeScript
includeTxPower?: boolean
```

Indicates whether the tx power will be included in the advertisement packet.

**Type:** boolean

**Since:** 18

**ArkTS mode:** ArkTS-Dyn since version 18; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-AdvertiseData-includeTxPower?: boolean--><!--Device-AdvertiseData-includeTxPower?: boolean-End-->

**System capability:** SystemCapability.Communication.Bluetooth.Core

## manufactureData

```TypeScript
manufactureData: Array<ManufactureData>
```

The specified manufacturer data list to this advertisement

**Type:** Array&lt;ManufactureData&gt;

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AdvertiseData-manufactureData: Array<ManufactureData>--><!--Device-AdvertiseData-manufactureData: Array<ManufactureData>-End-->

**System capability:** SystemCapability.Communication.Bluetooth.Core

## serviceData

```TypeScript
serviceData: Array<ServiceData>
```

The specified service data list to this advertisement

**Type:** Array&lt;ServiceData&gt;

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AdvertiseData-serviceData: Array<ServiceData>--><!--Device-AdvertiseData-serviceData: Array<ServiceData>-End-->

**System capability:** SystemCapability.Communication.Bluetooth.Core

## serviceUuids

```TypeScript
serviceUuids: Array<string>
```

The specified service UUID list to this advertisement

**Type:** Array&lt;string&gt;

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AdvertiseData-serviceUuids: Array<string>--><!--Device-AdvertiseData-serviceUuids: Array<string>-End-->

**System capability:** SystemCapability.Communication.Bluetooth.Core

