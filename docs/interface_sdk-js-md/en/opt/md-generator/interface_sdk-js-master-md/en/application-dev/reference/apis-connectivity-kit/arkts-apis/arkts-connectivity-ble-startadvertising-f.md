# startAdvertising

## Modules to Import

```TypeScript
import { ble } from '@kit.ConnectivityKit';
```

## startAdvertising

```TypeScript
function startAdvertising(setting: AdvertiseSetting, advData: AdvertiseData, advResponse?: AdvertiseData): void
```

Starts BLE advertising. - If only [includeDeviceName](arkts-connectivity-ble-advertisedata-i.md#includeDeviceName) is set to true, the local name will be carried in the broadcast packet. - If only [advertiseName](arkts-connectivity-ble-advertisedata-i.md#advertiseName) is set, its value will be used as a custom name and carried in the broadcast packet. - If [includeDeviceName](arkts-connectivity-ble-advertisedata-i.md#includeDeviceName) is set to true and [advertiseName](arkts-connectivity-ble-advertisedata-i.md#advertiseName) is specified, the [advertiseName](arkts-connectivity-ble-advertisedata-i.md#advertiseName) property will take effect. - To set [advertiseName](arkts-connectivity-ble-advertisedata-i.md#advertiseName), ensure that ohos.permission.MANAGE_BLUETOOTH_ADVERTISER_NAME has been added.

**Since:** 23

**Deprecated since:** -1

**Required permissions:** 
- API version 23+: ohos.permission.ACCESS_BLUETOOTH or (ohos.permission.ACCESS_BLUETOOTH and ohos.permission.MANAGE_BLUETOOTH_ADVERTISER_NAME)
- API version 10 - 22: ohos.permission.ACCESS_BLUETOOTH

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-ble-function startAdvertising(setting: AdvertiseSetting, advData: AdvertiseData, advResponse?: AdvertiseData): void--><!--Device-ble-function startAdvertising(setting: AdvertiseSetting, advData: AdvertiseData, advResponse?: AdvertiseData): void-End-->

**System capability:** SystemCapability.Communication.Bluetooth.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| setting | [AdvertiseSetting](arkts-connectivity-ble-advertisesetting-i.md) | Yes |
| advData | [AdvertiseData](arkts-connectivity-bluetoothmanager-advertisedata-i.md) | Yes |
| advResponse | [AdvertiseData](arkts-connectivity-bluetoothmanager-advertisedata-i.md) | No |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| 2900010 |
| [201](../../errorcode-universal.md#201-permission-denied) |
| 2902054 |
| 2900001 |
| 2900003 |
| 2900099 |

## Examples

```TypeScript
let manufactureValueBuffer = new Uint8Array(4);
manufactureValueBuffer[0] = 1;
manufactureValueBuffer[1] = 2;
manufactureValueBuffer[2] = 3;
manufactureValueBuffer[3] = 4;

let serviceValueBuffer = new Uint8Array(4);
serviceValueBuffer[0] = 4;
serviceValueBuffer[1] = 6;
serviceValueBuffer[2] = 7;
serviceValueBuffer[3] = 8;
console.info('manufactureValueBuffer = '+ JSON.stringify(manufactureValueBuffer));
console.info('serviceValueBuffer = '+ JSON.stringify(serviceValueBuffer));
try {
    let setting: ble.AdvertiseSetting = {
        interval:150,
        txPower:0,
        connectable:true
    };
    let manufactureDataUnit: ble.ManufactureData = {
        manufactureId:4567,
        manufactureValue:manufactureValueBuffer.buffer
    };
    let serviceDataUnit: ble.ServiceData = {
        serviceUuid:"00001888-0000-1000-8000-00805f9b34fb",
        serviceValue:serviceValueBuffer.buffer
    };
    let advData: ble.AdvertiseData = {
        serviceUuids:["00001888-0000-1000-8000-00805f9b34fb"],
        manufactureData:[manufactureDataUnit],
        serviceData:[serviceDataUnit],
        advertiseName:"testName" // You need to apply for the ohos.permission.MANAGE_BLUETOOTH_ADVERTISER_NAME permission.
    };
    let advResponse: ble.AdvertiseData = {
        serviceUuids:["00001888-0000-1000-8000-00805f9b34fb"],
        manufactureData:[manufactureDataUnit],
        serviceData:[serviceDataUnit],
        advertiseName:"testName" // You need to apply for the ohos.permission.MANAGE_BLUETOOTH_ADVERTISER_NAME permission.
    };
    ble.startAdvertising(setting, advData ,advResponse);
} catch (err) {
    console.error(`errCode: ${err.code}, errMessage: ${err.message}`);
}
```


## startAdvertising

```TypeScript
function startAdvertising(advertisingParams: AdvertisingParams, callback: AsyncCallback<number>): void
```

Starts BLE advertising. The API returns a advertising ID. The ID can be used to temporarily enable or disable this advertising using the API [enableAdvertising](arkts-connectivity-ble-enableadvertising-f.md#enableAdvertising) or [disableAdvertising](arkts-connectivity-ble-disableadvertising-f.md#disableAdvertising). To completely stop the advertising corresponding to the ID, invoke the API [stopAdvertising](arkts-connectivity-ble-stopadvertising-f.md#stopAdvertising) with ID. - If only [includeDeviceName](arkts-connectivity-ble-advertisedata-i.md#includeDeviceName) is set to true, the local name will be carried in the broadcast packet. - If only [advertiseName](arkts-connectivity-ble-advertisedata-i.md#advertiseName) is set, its value will be used as a custom name and carried in the broadcast packet. - If [includeDeviceName](arkts-connectivity-ble-advertisedata-i.md#includeDeviceName) is set to true and [advertiseName](arkts-connectivity-ble-advertisedata-i.md#advertiseName) is specified, the [advertiseName](arkts-connectivity-ble-advertisedata-i.md#advertiseName) property will take effect. - To set [advertiseName](arkts-connectivity-ble-advertisedata-i.md#advertiseName), ensure that ohos.permission.MANAGE_BLUETOOTH_ADVERTISER_NAME has been added.

**Since:** 23

**Deprecated since:** -1

**Required permissions:** 
- API version 23+: ohos.permission.ACCESS_BLUETOOTH or (ohos.permission.ACCESS_BLUETOOTH and ohos.permission.MANAGE_BLUETOOTH_ADVERTISER_NAME)
- API version 11 - 22: ohos.permission.ACCESS_BLUETOOTH

**Model restriction:** This API can be used only in the stage model.

<!--Device-ble-function startAdvertising(advertisingParams: AdvertisingParams, callback: AsyncCallback<int>): void--><!--Device-ble-function startAdvertising(advertisingParams: AdvertisingParams, callback: AsyncCallback<int>): void-End-->

**System capability:** SystemCapability.Communication.Bluetooth.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| advertisingParams | [AdvertisingParams](arkts-connectivity-ble-advertisingparams-i.md) | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;number&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| 2900010 |
| [201](../../errorcode-universal.md#201-permission-denied) |
| 2902054 |
| 2900001 |
| 2900003 |
| 2900099 |

## Examples

```TypeScript
let manufactureValueBuffer = new Uint8Array(4);
manufactureValueBuffer[0] = 1;
manufactureValueBuffer[1] = 2;
manufactureValueBuffer[2] = 3;
manufactureValueBuffer[3] = 4;

let serviceValueBuffer = new Uint8Array(4);
serviceValueBuffer[0] = 4;
serviceValueBuffer[1] = 6;
serviceValueBuffer[2] = 7;
serviceValueBuffer[3] = 8;
console.info('manufactureValueBuffer = '+ JSON.stringify(manufactureValueBuffer));
console.info('serviceValueBuffer = '+ JSON.stringify(serviceValueBuffer));
try {
    let setting: ble.AdvertiseSetting = {
        interval:150,
        txPower:0,
        connectable:true,
    };
    let manufactureDataUnit: ble.ManufactureData = {
        manufactureId:4567,
        manufactureValue:manufactureValueBuffer.buffer
    };
    let serviceDataUnit: ble.ServiceData = {
        serviceUuid:"00001888-0000-1000-8000-00805f9b34fb",
        serviceValue:serviceValueBuffer.buffer
    };
    let advData: ble.AdvertiseData = {
        serviceUuids:["00001888-0000-1000-8000-00805f9b34fb"],
        manufactureData:[manufactureDataUnit],
        serviceData:[serviceDataUnit],
        advertiseName:"testName" // You need to apply for the ohos.permission.MANAGE_BLUETOOTH_ADVERTISER_NAME permission.
    };
    let advResponse: ble.AdvertiseData = {
        serviceUuids:["00001888-0000-1000-8000-00805f9b34fb"],
        manufactureData:[manufactureDataUnit],
        serviceData:[serviceDataUnit],
        advertiseName:"testName" // You need to apply for the ohos.permission.MANAGE_BLUETOOTH_ADVERTISER_NAME permission.
    };
    let advertisingParams: ble.AdvertisingParams = {
        advertisingSettings: setting,
        advertisingData: advData,
        advertisingResponse: advResponse,
        duration: 0
    }
    let advHandle = 0xFF;
    ble.startAdvertising(advertisingParams, (err, outAdvHandle) => {
        if (err) {
            return;
        } else {
            advHandle = outAdvHandle;
            console.info("advHandle: " + advHandle);
        }
    });
} catch (err) {
    console.error(`errCode: ${err.code}, errMessage: ${err.message}`);
}
```


## startAdvertising

```TypeScript
function startAdvertising(advertisingParams: AdvertisingParams): Promise<number>
```

Starts BLE advertising. The API returns a advertising ID. The ID can be used to temporarily enable or disable this advertising using the API [enableAdvertising](arkts-connectivity-ble-enableadvertising-f.md#enableAdvertising) or [disableAdvertising](arkts-connectivity-ble-disableadvertising-f.md#disableAdvertising). To completely stop the advertising corresponding to the ID, invoke the API [stopAdvertising](arkts-connectivity-ble-stopadvertising-f.md#stopAdvertising) with ID. - If only [includeDeviceName](arkts-connectivity-ble-advertisedata-i.md#includeDeviceName) is set to true, the local name will be carried in the broadcast packet. - If only [advertiseName](arkts-connectivity-ble-advertisedata-i.md#advertiseName) is set, its value will be used as a custom name and carried in the broadcast packet. - If [includeDeviceName](arkts-connectivity-ble-advertisedata-i.md#includeDeviceName) is set to true and [advertiseName](arkts-connectivity-ble-advertisedata-i.md#advertiseName) is specified, the [advertiseName](arkts-connectivity-ble-advertisedata-i.md#advertiseName) property will take effect. - To set [advertiseName](arkts-connectivity-ble-advertisedata-i.md#advertiseName), ensure that ohos.permission.MANAGE_BLUETOOTH_ADVERTISER_NAME has been added.

**Since:** 23

**Deprecated since:** -1

**Required permissions:** 
- API version 23+: ohos.permission.ACCESS_BLUETOOTH or (ohos.permission.ACCESS_BLUETOOTH and ohos.permission.MANAGE_BLUETOOTH_ADVERTISER_NAME)
- API version 11 - 22: ohos.permission.ACCESS_BLUETOOTH

**Model restriction:** This API can be used only in the stage model.

<!--Device-ble-function startAdvertising(advertisingParams: AdvertisingParams): Promise<int>--><!--Device-ble-function startAdvertising(advertisingParams: AdvertisingParams): Promise<int>-End-->

**System capability:** SystemCapability.Communication.Bluetooth.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| advertisingParams | [AdvertisingParams](arkts-connectivity-ble-advertisingparams-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;number & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| 2900010 |
| [201](../../errorcode-universal.md#201-permission-denied) |
| 2902054 |
| 2900001 |
| 2900003 |
| 2900099 |

## Examples

```TypeScript
let manufactureValueBuffer = new Uint8Array(4);
manufactureValueBuffer[0] = 1;
manufactureValueBuffer[1] = 2;
manufactureValueBuffer[2] = 3;
manufactureValueBuffer[3] = 4;

let serviceValueBuffer = new Uint8Array(4);
serviceValueBuffer[0] = 4;
serviceValueBuffer[1] = 6;
serviceValueBuffer[2] = 7;
serviceValueBuffer[3] = 8;
console.info('manufactureValueBuffer = '+ JSON.stringify(manufactureValueBuffer));
console.info('serviceValueBuffer = '+ JSON.stringify(serviceValueBuffer));
try {
    let setting: ble.AdvertiseSetting = {
        interval:150,
        txPower:0,
        connectable:true
    };
    let manufactureDataUnit: ble.ManufactureData = {
        manufactureId:4567,
        manufactureValue:manufactureValueBuffer.buffer
    };
    let serviceDataUnit: ble.ServiceData = {
        serviceUuid:"00001888-0000-1000-8000-00805f9b34fb",
        serviceValue:serviceValueBuffer.buffer
    };
    let advData: ble.AdvertiseData = {
        serviceUuids:["00001888-0000-1000-8000-00805f9b34fb"],
        manufactureData:[manufactureDataUnit],
        serviceData:[serviceDataUnit],
        advertiseName:"testName" // You need to apply for the ohos.permission.MANAGE_BLUETOOTH_ADVERTISER_NAME permission.
    };
    let advResponse: ble.AdvertiseData = {
        serviceUuids:["00001888-0000-1000-8000-00805f9b34fb"],
        manufactureData:[manufactureDataUnit],
        serviceData:[serviceDataUnit],
        advertiseName:"testName" // You need to apply for the ohos.permission.MANAGE_BLUETOOTH_ADVERTISER_NAME permission.
    };
    let advertisingParams: ble.AdvertisingParams = {
        advertisingSettings: setting,
        advertisingData: advData,
        advertisingResponse: advResponse,
        duration: 0
    }
    let advHandle = 0xFF;
    ble.startAdvertising(advertisingParams)
        .then(outAdvHandle => {
            advHandle = outAdvHandle;
    });
} catch (err) {
    console.error(`errCode: ${err.code}, errMessage: ${err.message}`);
}
```
