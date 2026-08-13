# GattServer

Manages GATT server. Before calling an Gatt server method, you must use [createGattServer](arkts-connectivity-ble-creategattserver-f.md#createGattServer) to create an GattServer instance.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [GattServer](arkts-connectivity-bluetoothmanager-gattserver-i.md#GattServer)

<!--Device-bluetooth-interface GattServer--><!--Device-bluetooth-interface GattServer-End-->

**System capability:** SystemCapability.Communication.Bluetooth.Core

## Modules to Import

```TypeScript
import { bluetooth } from '@kit.ConnectivityKit';
```

## addService

```TypeScript
addService(service: GattService): boolean
```

Adds a specified service to be hosted. The added service and its characteristics are provided by the local device.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [addService](arkts-connectivity-bluetoothmanager-gattserver-i.md#addService)

**Required permissions:** ohos.permission.USE_BLUETOOTH

<!--Device-GattServer-addService(service: GattService): boolean--><!--Device-GattServer-addService(service: GattService): boolean-End-->

**System capability:** SystemCapability.Communication.Bluetooth.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [service](../../apis-calendar-kit/arkts-apis/arkts-calendar-calendarmanager-event-i.md) | [GattService](arkts-connectivity-bluetooth-gattservice-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

## Examples

```TypeScript
// Create descriptors.
let descriptors : Array<bluetooth.BLEDescriptor> = [];
let arrayBuffer = new ArrayBuffer(8);
let descV = new Uint8Array(arrayBuffer);
descV[0] = 11;
let descriptor : bluetooth.BLEDescriptor = {serviceUuid: '00001810-0000-1000-8000-00805F9B34FB',
  characteristicUuid: '00001820-0000-1000-8000-00805F9B34FB',
  descriptorUuid: '00002902-0000-1000-8000-00805F9B34FB', descriptorValue: arrayBuffer};
descriptors[0] = descriptor;

// Create characteristics.
let characteristics : Array<bluetooth.BLECharacteristic> = [];
let arrayBufferC = new ArrayBuffer(8);
let cccV = new Uint8Array(arrayBufferC);
cccV[0] = 1;
let characteristic : bluetooth.BLECharacteristic = {serviceUuid: '00001810-0000-1000-8000-00805F9B34FB',
  characteristicUuid: '00001820-0000-1000-8000-00805F9B34FB', characteristicValue: arrayBufferC, descriptors:descriptors};
let characteristicN : bluetooth.BLECharacteristic = {serviceUuid: '00001810-0000-1000-8000-00805F9B34FB',
  characteristicUuid: '00001821-0000-1000-8000-00805F9B34FB', characteristicValue: arrayBufferC, descriptors:descriptors};
characteristics[0] = characteristic;

// Create a gattService instance.
let gattService : bluetooth.GattService = {serviceUuid:'00001810-0000-1000-8000-00805F9B34FB', isPrimary: true, characteristics:characteristics, includeServices:[]};

let gattServer : bluetooth.GattServer = bluetooth.BLE.createGattServer();
let ret : boolean = gattServer.addService(gattService);
if (ret) {
   console.info("add service successfully");
} else {
   console.error("add service failed");
}
```

## close

```TypeScript
close(): void
```

Closes this {@code GattServer} object and unregisters its callbacks.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [close](arkts-connectivity-bluetoothmanager-gattserver-i.md#close)

**Required permissions:** ohos.permission.USE_BLUETOOTH

<!--Device-GattServer-close(): void--><!--Device-GattServer-close(): void-End-->

**System capability:** SystemCapability.Communication.Bluetooth.Core

## Examples

```TypeScript
let server : bluetooth.GattServer = bluetooth.BLE.createGattServer();
server.close();
```

## notifyCharacteristicChanged

```TypeScript
notifyCharacteristicChanged(deviceId: string, notifyCharacteristic: NotifyCharacteristic): boolean
```

Sends a notification of a change in a specified local characteristic. This method should be called for every BLE peripheral device that has requested notifications.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [notifyCharacteristicChanged](arkts-connectivity-bluetoothmanager-gattserver-i.md#notifyCharacteristicChanged)

**Required permissions:** ohos.permission.USE_BLUETOOTH

<!--Device-GattServer-notifyCharacteristicChanged(deviceId: string, notifyCharacteristic: NotifyCharacteristic): boolean--><!--Device-GattServer-notifyCharacteristicChanged(deviceId: string, notifyCharacteristic: NotifyCharacteristic): boolean-End-->

**System capability:** SystemCapability.Communication.Bluetooth.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| deviceId | string | Yes |
| notifyCharacteristic | [NotifyCharacteristic](arkts-connectivity-bluetoothmanager-notifycharacteristic-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

## Examples

```TypeScript
// Create descriptors.
let descriptors : Array<bluetooth.BLEDescriptor> = [];
let arrayBuffer = new ArrayBuffer(8);
let descV = new Uint8Array(arrayBuffer);
descV[0] = 11;
let descriptor : bluetooth.BLEDescriptor = {serviceUuid: '00001810-0000-1000-8000-00805F9B34FB',
  characteristicUuid: '00001820-0000-1000-8000-00805F9B34FB',
  descriptorUuid: '00002902-0000-1000-8000-00805F9B34FB', descriptorValue: arrayBuffer};
descriptors[0] = descriptor;
let arrayBufferC = new ArrayBuffer(8);
let characteristic : bluetooth.BLECharacteristic = {serviceUuid: '00001810-0000-1000-8000-00805F9B34FB',
  characteristicUuid: '00001820-0000-1000-8000-00805F9B34FB', characteristicValue: arrayBufferC, descriptors:descriptors};
let notifyCharacteristic : bluetooth.NotifyCharacteristic = {serviceUuid: '00001810-0000-1000-8000-00805F9B34FB',
  characteristicUuid: '00001821-0000-1000-8000-00805F9B34FB', characteristicValue: characteristic.characteristicValue, confirm: false};
let server : bluetooth.GattServer = bluetooth.BLE.createGattServer();
server.notifyCharacteristicChanged('XX:XX:XX:XX:XX:XX', notifyCharacteristic);
```

## off_characteristicRead

```TypeScript
off(type: 'characteristicRead', callback?: Callback<CharacteristicReadReq>): void
```

Unsubscribe characteristic read event.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** characteristicRead

**Required permissions:** ohos.permission.USE_BLUETOOTH

<!--Device-GattServer-off(type: 'characteristicRead', callback?: Callback<CharacteristicReadReq>): void--><!--Device-GattServer-off(type: 'characteristicRead', callback?: Callback<CharacteristicReadReq>): void-End-->

**System capability:** SystemCapability.Communication.Bluetooth.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'characteristicRead' | Yes |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[CharacteristicReadReq](arkts-connectivity-bluetooth-characteristicreadreq-i.md)&gt; | No |

## Examples

```TypeScript
let gattServer : bluetooth.GattServer = bluetooth.BLE.createGattServer();
gattServer.off("characteristicRead");
```

## off_characteristicWrite

```TypeScript
off(type: 'characteristicWrite', callback?: Callback<CharacteristicWriteReq>): void
```

Unsubscribe characteristic write event.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** characteristicWrite

**Required permissions:** ohos.permission.USE_BLUETOOTH

<!--Device-GattServer-off(type: 'characteristicWrite', callback?: Callback<CharacteristicWriteReq>): void--><!--Device-GattServer-off(type: 'characteristicWrite', callback?: Callback<CharacteristicWriteReq>): void-End-->

**System capability:** SystemCapability.Communication.Bluetooth.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'characteristicWrite' | Yes |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[CharacteristicWriteReq](arkts-connectivity-bluetooth-characteristicwritereq-i.md)&gt; | No |

## Examples

```TypeScript
let gattServer : bluetooth.GattServer = bluetooth.BLE.createGattServer();
gattServer.off("characteristicWrite");
```

## off_connectStateChange

```TypeScript
off(type: 'connectStateChange', callback?: Callback<BLEConnectChangedState>): void
```

Unsubscribe server connection state changed event.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** connectStateChange

**Required permissions:** ohos.permission.USE_BLUETOOTH

<!--Device-GattServer-off(type: 'connectStateChange', callback?: Callback<BLEConnectChangedState>): void--><!--Device-GattServer-off(type: 'connectStateChange', callback?: Callback<BLEConnectChangedState>): void-End-->

**System capability:** SystemCapability.Communication.Bluetooth.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'connectStateChange' | Yes |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;BLEConnectChangedState&gt; | No |

## Examples

```TypeScript
let gattServer : bluetooth.GattServer = bluetooth.BLE.createGattServer();
gattServer.off("connectStateChange");
```

## off_descriptorRead

```TypeScript
off(type: 'descriptorRead', callback?: Callback<DescriptorReadReq>): void
```

Unsubscribe descriptor read event.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** descriptorRead

**Required permissions:** ohos.permission.USE_BLUETOOTH

<!--Device-GattServer-off(type: 'descriptorRead', callback?: Callback<DescriptorReadReq>): void--><!--Device-GattServer-off(type: 'descriptorRead', callback?: Callback<DescriptorReadReq>): void-End-->

**System capability:** SystemCapability.Communication.Bluetooth.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'descriptorRead' | Yes |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[DescriptorReadReq](arkts-connectivity-bluetooth-descriptorreadreq-i.md)&gt; | No |

## Examples

```TypeScript
let gattServer : bluetooth.GattServer = bluetooth.BLE.createGattServer();
gattServer.off("descriptorRead");
```

## off_descriptorWrite

```TypeScript
off(type: 'descriptorWrite', callback?: Callback<DescriptorWriteReq>): void
```

Unsubscribe descriptor write event.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** descriptorWrite

**Required permissions:** ohos.permission.USE_BLUETOOTH

<!--Device-GattServer-off(type: 'descriptorWrite', callback?: Callback<DescriptorWriteReq>): void--><!--Device-GattServer-off(type: 'descriptorWrite', callback?: Callback<DescriptorWriteReq>): void-End-->

**System capability:** SystemCapability.Communication.Bluetooth.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'descriptorWrite' | Yes |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[DescriptorWriteReq](arkts-connectivity-bluetooth-descriptorwritereq-i.md)&gt; | No |

## Examples

```TypeScript
let gattServer : bluetooth.GattServer = bluetooth.BLE.createGattServer();
gattServer.off("descriptorWrite");
```

## on_characteristicRead

```TypeScript
on(type: 'characteristicRead', callback: Callback<CharacteristicReadReq>): void
```

Subscribe characteristic read event.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** characteristicRead

**Required permissions:** ohos.permission.USE_BLUETOOTH

<!--Device-GattServer-on(type: 'characteristicRead', callback: Callback<CharacteristicReadReq>): void--><!--Device-GattServer-on(type: 'characteristicRead', callback: Callback<CharacteristicReadReq>): void-End-->

**System capability:** SystemCapability.Communication.Bluetooth.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'characteristicRead' | Yes |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[CharacteristicReadReq](arkts-connectivity-bluetooth-characteristicreadreq-i.md)&gt; | Yes |

## Examples

```TypeScript
let arrayBufferCCC = new ArrayBuffer(8);
let cccValue = new Uint8Array(arrayBufferCCC);
cccValue[0] = 1;
function ReadCharacteristicReq(CharacteristicReadReq : bluetooth.CharacteristicReadReq) {
  let deviceId : string = CharacteristicReadReq.deviceId;
  let transId : number = CharacteristicReadReq.transId;
  let offset : number = CharacteristicReadReq.offset;
  let characteristicUuid : string = CharacteristicReadReq.characteristicUuid;

  let serverResponse : bluetooth.ServerResponse = {deviceId: deviceId, transId: transId, status: 0, 
  offset: offset, value:arrayBufferCCC};

  let ret : boolean = gattServer.sendResponse(serverResponse);
  if (ret) {
    console.info('bluetooth sendResponse successfully');
  } else {
    console.error('bluetooth sendResponse failed');
  }
}

let gattServer : bluetooth.GattServer = bluetooth.BLE.createGattServer();
gattServer.on("characteristicRead", ReadCharacteristicReq);
```

## on_characteristicWrite

```TypeScript
on(type: 'characteristicWrite', callback: Callback<CharacteristicWriteReq>): void
```

Subscribe characteristic write event.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** characteristicWrite

**Required permissions:** ohos.permission.USE_BLUETOOTH

<!--Device-GattServer-on(type: 'characteristicWrite', callback: Callback<CharacteristicWriteReq>): void--><!--Device-GattServer-on(type: 'characteristicWrite', callback: Callback<CharacteristicWriteReq>): void-End-->

**System capability:** SystemCapability.Communication.Bluetooth.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'characteristicWrite' | Yes |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[CharacteristicWriteReq](arkts-connectivity-bluetooth-characteristicwritereq-i.md)&gt; | Yes |

## Examples

```TypeScript
let arrayBufferCCC = new ArrayBuffer(8);
let cccValue = new Uint8Array(arrayBufferCCC);
function WriteCharacteristicReq(CharacteristicWriteReq : bluetooth.CharacteristicWriteReq) {
  let deviceId : string = CharacteristicWriteReq.deviceId;
  let transId : number = CharacteristicWriteReq.transId;
  let offset : number = CharacteristicWriteReq.offset;
  let isPrep : boolean = CharacteristicWriteReq.isPrep;
  let needRsp : boolean = CharacteristicWriteReq.needRsp;
  let value =  new Uint8Array(arrayBufferCCC);
  let characteristicUuid : string = CharacteristicWriteReq.characteristicUuid;

  cccValue.set(new Uint8Array(value));
  let serverResponse : bluetooth.ServerResponse = {deviceId: deviceId, transId: transId, status: 0, 
  offset: offset, value:arrayBufferCCC};

  let ret : boolean = gattServer.sendResponse(serverResponse);
  if (ret) {
    console.info('bluetooth sendResponse successfully');
  } else {
    console.error('bluetooth sendResponse failed');
  }
}

let gattServer : bluetooth.GattServer = bluetooth.BLE.createGattServer();
gattServer.on("characteristicWrite", WriteCharacteristicReq);
```

## on_connectStateChange

```TypeScript
on(type: 'connectStateChange', callback: Callback<BLEConnectChangedState>): void
```

Subscribe server connection state changed event.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** connectStateChange

**Required permissions:** ohos.permission.USE_BLUETOOTH

<!--Device-GattServer-on(type: 'connectStateChange', callback: Callback<BLEConnectChangedState>): void--><!--Device-GattServer-on(type: 'connectStateChange', callback: Callback<BLEConnectChangedState>): void-End-->

**System capability:** SystemCapability.Communication.Bluetooth.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'connectStateChange' | Yes |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;BLEConnectChangedState&gt; | Yes |

## Examples

```TypeScript
function Connected(BLEConnectChangedState : bluetooth.BLEConnectChangedState) {
  let deviceId : string = BLEConnectChangedState.deviceId;
  let status : bluetooth.ProfileConnectionState = BLEConnectChangedState.state;
}

let gattServer : bluetooth.GattServer = bluetooth.BLE.createGattServer();
gattServer.on("connectStateChange", Connected);
```

## on_descriptorRead

```TypeScript
on(type: 'descriptorRead', callback: Callback<DescriptorReadReq>): void
```

Subscribe descriptor read event.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** descriptorRead

**Required permissions:** ohos.permission.USE_BLUETOOTH

<!--Device-GattServer-on(type: 'descriptorRead', callback: Callback<DescriptorReadReq>): void--><!--Device-GattServer-on(type: 'descriptorRead', callback: Callback<DescriptorReadReq>): void-End-->

**System capability:** SystemCapability.Communication.Bluetooth.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'descriptorRead' | Yes |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[DescriptorReadReq](arkts-connectivity-bluetooth-descriptorreadreq-i.md)&gt; | Yes |

## Examples

```TypeScript
let arrayBufferDesc = new ArrayBuffer(8);
let descValue = new Uint8Array(arrayBufferDesc);
descValue[0] = 1;
function ReadDescriptorReq(DescriptorReadReq : bluetooth.DescriptorReadReq) {
  let deviceId : string = DescriptorReadReq.deviceId;
  let transId : number = DescriptorReadReq.transId;
  let offset : number = DescriptorReadReq.offset;
  let descriptorUuid : string = DescriptorReadReq.descriptorUuid;

  let serverResponse : bluetooth.ServerResponse = {deviceId: deviceId, transId: transId, status: 0, 
  offset: offset, value:arrayBufferDesc};

  let ret : boolean = gattServer.sendResponse(serverResponse);
  if (ret) {
    console.info('bluetooth sendResponse successfully');
  } else {
    console.error('bluetooth sendResponse failed');
  }
}

let gattServer : bluetooth.GattServer = bluetooth.BLE.createGattServer();
gattServer.on("descriptorRead", ReadDescriptorReq);
```

## on_descriptorWrite

```TypeScript
on(type: 'descriptorWrite', callback: Callback<DescriptorWriteReq>): void
```

Subscribe descriptor write event.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** descriptorWrite

**Required permissions:** ohos.permission.USE_BLUETOOTH

<!--Device-GattServer-on(type: 'descriptorWrite', callback: Callback<DescriptorWriteReq>): void--><!--Device-GattServer-on(type: 'descriptorWrite', callback: Callback<DescriptorWriteReq>): void-End-->

**System capability:** SystemCapability.Communication.Bluetooth.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'descriptorWrite' | Yes |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[DescriptorWriteReq](arkts-connectivity-bluetooth-descriptorwritereq-i.md)&gt; | Yes |

## Examples

```TypeScript
let arrayBufferDesc = new ArrayBuffer(8);
let descValue = new Uint8Array(arrayBufferDesc);
function WriteDescriptorReq(DescriptorWriteReq : bluetooth.DescriptorWriteReq) {
  let deviceId : string = DescriptorWriteReq.deviceId;
  let transId : number = DescriptorWriteReq.transId;
  let offset : number = DescriptorWriteReq.offset;
  let isPrep : boolean = DescriptorWriteReq.isPrep;
  let needRsp : boolean = DescriptorWriteReq.needRsp;
  let value = new Uint8Array(arrayBufferDesc);
  let descriptorUuid : string = DescriptorWriteReq.descriptorUuid;

  descValue.set(new Uint8Array(value));
  let serverResponse : bluetooth.ServerResponse = {deviceId: deviceId, transId: transId, status: 0, offset: offset, value:arrayBufferDesc};

  let ret : boolean = gattServer.sendResponse(serverResponse);
  if (ret) {
    console.info('bluetooth sendResponse successfully');
  } else {
    console.error('bluetooth sendResponse failed');
  }
}

let gattServer : bluetooth.GattServer = bluetooth.BLE.createGattServer();
gattServer.on("descriptorWrite", WriteDescriptorReq);
```

## removeService

```TypeScript
removeService(serviceUuid: string): boolean
```

Removes a specified service from the list of GATT services provided by this device.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [removeService](arkts-connectivity-bluetoothmanager-gattserver-i.md#removeService)

**Required permissions:** ohos.permission.USE_BLUETOOTH

<!--Device-GattServer-removeService(serviceUuid: string): boolean--><!--Device-GattServer-removeService(serviceUuid: string): boolean-End-->

**System capability:** SystemCapability.Communication.Bluetooth.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| serviceUuid | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

## Examples

```TypeScript
let server : bluetooth.GattServer = bluetooth.BLE.createGattServer();
server.removeService('00001810-0000-1000-8000-00805F9B34FB');
```

## sendResponse

```TypeScript
sendResponse(serverResponse: ServerResponse): boolean
```

Sends a response to a specified read or write request to a given BLE peripheral device.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [sendResponse](arkts-connectivity-bluetoothmanager-gattserver-i.md#sendResponse)

**Required permissions:** ohos.permission.USE_BLUETOOTH

<!--Device-GattServer-sendResponse(serverResponse: ServerResponse): boolean--><!--Device-GattServer-sendResponse(serverResponse: ServerResponse): boolean-End-->

**System capability:** SystemCapability.Communication.Bluetooth.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| serverResponse | [ServerResponse](arkts-connectivity-bluetoothmanager-serverresponse-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

## Examples

```TypeScript
/* send response */
let arrayBufferCCC = new ArrayBuffer(8);
let cccValue = new Uint8Array(arrayBufferCCC);
cccValue[0] = 1;
let serverResponse : bluetooth.ServerResponse = {
    "deviceId": "XX:XX:XX:XX:XX:XX",
    "transId": 0,
    "status": 0,
    "offset": 0,
    "value": arrayBufferCCC,
};

let gattServer : bluetooth.GattServer = bluetooth.BLE.createGattServer();
let ret : boolean = gattServer.sendResponse(serverResponse);
if (ret) {
  console.info('bluetooth sendResponse successfully');
} else {
  console.error('bluetooth sendResponse failed');
}
```

## startAdvertising

```TypeScript
startAdvertising(setting: AdvertiseSetting, advData: AdvertiseData, advResponse?: AdvertiseData): void
```

Starts BLE advertising.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [startAdvertising](arkts-connectivity-bluetoothmanager-gattserver-i.md#startAdvertising)

**Required permissions:** ohos.permission.DISCOVER_BLUETOOTH

<!--Device-GattServer-startAdvertising(setting: AdvertiseSetting, advData: AdvertiseData, advResponse?: AdvertiseData): void--><!--Device-GattServer-startAdvertising(setting: AdvertiseSetting, advData: AdvertiseData, advResponse?: AdvertiseData): void-End-->

**System capability:** SystemCapability.Communication.Bluetooth.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| setting | [AdvertiseSetting](arkts-connectivity-ble-advertisesetting-i.md) | Yes |
| advData | [AdvertiseData](arkts-connectivity-bluetoothmanager-advertisedata-i.md) | Yes |
| advResponse | [AdvertiseData](arkts-connectivity-bluetoothmanager-advertisedata-i.md) | No |

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
let gattServer : bluetooth.GattServer = bluetooth.BLE.createGattServer();
let setting : bluetooth.AdvertiseSetting = {
    interval:150,
    txPower:60,
    connectable:true,
}

let manufactureData : bluetooth.ManufactureData = {
    manufactureId:4567,
    manufactureValue:manufactureValueBuffer.buffer
}

let serviceData : bluetooth.ServiceData = {
    serviceUuid:"00001888-0000-1000-8000-00805f9b34fb",
    serviceValue:serviceValueBuffer.buffer
}

let advData : bluetooth.AdvertiseData = {
    serviceUuids:["00001889-0000-1000-8000-00805f9b34fb"],
    manufactureData:[manufactureData],
    serviceData:[serviceData],
}

let advResponse : bluetooth.AdvertiseData = {
    serviceUuids:["00001889-0000-1000-8000-00805f9b34fb"],
    manufactureData:[manufactureData],
    serviceData:[serviceData],
}
gattServer.startAdvertising(setting, advData, advResponse);
```

## stopAdvertising

```TypeScript
stopAdvertising(): void
```

Stops BLE advertising.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [stopAdvertising](arkts-connectivity-bluetoothmanager-gattserver-i.md#stopAdvertising)

**Required permissions:** ohos.permission.DISCOVER_BLUETOOTH

<!--Device-GattServer-stopAdvertising(): void--><!--Device-GattServer-stopAdvertising(): void-End-->

**System capability:** SystemCapability.Communication.Bluetooth.Core

## Examples

```TypeScript
let server : bluetooth.GattServer = bluetooth.BLE.createGattServer();
server.stopAdvertising();
```
