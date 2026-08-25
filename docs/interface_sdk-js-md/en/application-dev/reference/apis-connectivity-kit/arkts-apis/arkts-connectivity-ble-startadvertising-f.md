# startAdvertising

## Modules to Import

```TypeScript
import { ble } from 'kits/@kit.ConnectivityKit';
```

## startAdvertising

```TypeScript
function startAdvertising(setting: AdvertiseSetting, advData: AdvertiseData, advResponse?: AdvertiseData): void
```

Starts BLE advertising.  
- If only [includeDeviceName](arkts-connectivity-ble-advertisedata-i.md#includedevicename) is set to true,  
the local name will be carried in the broadcast packet.  
- If only [advertiseName](arkts-connectivity-ble-advertisedata-i.md#advertisename) is set,  
its value will be used as a custom name and carried in the broadcast packet.  
- If [includeDeviceName](arkts-connectivity-ble-advertisedata-i.md#includedevicename) is set to true and [advertiseName](arkts-connectivity-ble-advertisedata-i.md#advertisename) is specified,  
the [advertiseName](arkts-connectivity-ble-advertisedata-i.md#advertisename) property will take effect.  
- To set [advertiseName](arkts-connectivity-ble-advertisedata-i.md#advertisename),  
ensure that ohos.permission.MANAGE_BLUETOOTH_ADVERTISER_NAME has been added.

**Since:** 10

**Required permissions:** 
- API version 23+: ohos.permission.ACCESS_BLUETOOTH or (ohos.permission.ACCESS_BLUETOOTH and ohos.permission.MANAGE_BLUETOOTH_ADVERTISER_NAME)
- API version 10 - 22: ohos.permission.ACCESS_BLUETOOTH

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Communication.Bluetooth.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| setting | [AdvertiseSetting](arkts-connectivity-ble-advertisesetting-i.md) | Yes |
| advData | [AdvertiseData](arkts-connectivity-ble-advertisedata-i.md) | Yes |
| advResponse | [AdvertiseData](arkts-connectivity-ble-advertisedata-i.md) | No |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| 2900001 |
| 2900003 |
| 2900010 |
| 2900099 |
| 2902054 |


## startAdvertising

```TypeScript
function startAdvertising(advertisingParams: AdvertisingParams, callback: AsyncCallback<number>): void
```

Starts BLE advertising. The API returns a advertising ID. The ID can be used to temporarily enable or disable this advertising using the API [enableAdvertising](arkts-connectivity-ble-enableadvertising-f.md) or [disableAdvertising](arkts-connectivity-ble-disableadvertising-f.md). To completely stop the advertising corresponding to the ID, invoke the API [stopAdvertising](arkts-connectivity-ble-stopadvertising-f.md) with ID.  
- If only [includeDeviceName](arkts-connectivity-ble-advertisedata-i.md#includedevicename) is set to true,  
the local name will be carried in the broadcast packet.  
- If only [advertiseName](arkts-connectivity-ble-advertisedata-i.md#advertisename) is set,  
its value will be used as a custom name and carried in the broadcast packet.  
- If [includeDeviceName](arkts-connectivity-ble-advertisedata-i.md#includedevicename) is set to true and [advertiseName](arkts-connectivity-ble-advertisedata-i.md#advertisename) is specified,  
the [advertiseName](arkts-connectivity-ble-advertisedata-i.md#advertisename) property will take effect.  
- To set [advertiseName](arkts-connectivity-ble-advertisedata-i.md#advertisename),  
ensure that ohos.permission.MANAGE_BLUETOOTH_ADVERTISER_NAME has been added.

**Since:** 11

**Required permissions:** 
- API version 23+: ohos.permission.ACCESS_BLUETOOTH or (ohos.permission.ACCESS_BLUETOOTH and ohos.permission.MANAGE_BLUETOOTH_ADVERTISER_NAME)
- API version 11 - 22: ohos.permission.ACCESS_BLUETOOTH

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Communication.Bluetooth.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| advertisingParams | [AdvertisingParams](arkts-connectivity-advertising-advertisingparams-i.md) | Yes |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;number&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| 2900001 |
| 2900003 |
| 2900010 |
| 2900099 |
| 2902054 |


## startAdvertising

```TypeScript
function startAdvertising(advertisingParams: AdvertisingParams): Promise<number>
```

Starts BLE advertising. The API returns a advertising ID. The ID can be used to temporarily enable or disable this advertising using the API [enableAdvertising](arkts-connectivity-ble-enableadvertising-f.md) or [disableAdvertising](arkts-connectivity-ble-disableadvertising-f.md). To completely stop the advertising corresponding to the ID, invoke the API [stopAdvertising](arkts-connectivity-ble-stopadvertising-f.md) with ID.  
- If only [includeDeviceName](arkts-connectivity-ble-advertisedata-i.md#includedevicename) is set to true,  
the local name will be carried in the broadcast packet.  
- If only [advertiseName](arkts-connectivity-ble-advertisedata-i.md#advertisename) is set,  
its value will be used as a custom name and carried in the broadcast packet.  
- If [includeDeviceName](arkts-connectivity-ble-advertisedata-i.md#includedevicename) is set to true and [advertiseName](arkts-connectivity-ble-advertisedata-i.md#advertisename) is specified,  
the [advertiseName](arkts-connectivity-ble-advertisedata-i.md#advertisename) property will take effect.  
- To set [advertiseName](arkts-connectivity-ble-advertisedata-i.md#advertisename),  
ensure that ohos.permission.MANAGE_BLUETOOTH_ADVERTISER_NAME has been added.

**Since:** 11

**Required permissions:** 
- API version 23+: ohos.permission.ACCESS_BLUETOOTH or (ohos.permission.ACCESS_BLUETOOTH and ohos.permission.MANAGE_BLUETOOTH_ADVERTISER_NAME)
- API version 11 - 22: ohos.permission.ACCESS_BLUETOOTH

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Communication.Bluetooth.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| advertisingParams | [AdvertisingParams](arkts-connectivity-advertising-advertisingparams-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;number & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| 2900001 |
| 2900003 |
| 2900010 |
| 2900099 |
| 2902054 |
