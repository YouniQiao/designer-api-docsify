# GattServer

Manages GATT server. Before calling an Gatt server method, you must use [createGattServer](arkts-connectivity-ble-creategattserver-f.md) to create an GattServer instance.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [GattServer](arkts-connectivity-bluetoothmanager-gattserver-i.md)

**System capability:** SystemCapability.Communication.Bluetooth.Core

## Modules to Import

```TypeScript
import { bluetooth } from 'kits/@kit.ConnectivityKit';
```

## addService

```TypeScript
addService(service: GattService): boolean
```

Adds a specified service to be hosted. The added service and its characteristics are provided by the local device.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [addService](arkts-connectivity-bluetoothmanager-gattserver-i.md#addservice)

**Required permissions:** ohos.permission.USE_BLUETOOTH

**System capability:** SystemCapability.Communication.Bluetooth.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [service](../../apis-calendar-kit/arkts-apis/arkts-calendar-calendarmanager-event-i.md) | [GattService](arkts-connectivity-bluetoothmanager-gattservice-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

## close

```TypeScript
close(): void
```

Closes this {@code GattServer} object and unregisters its callbacks.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [close](arkts-connectivity-bluetoothmanager-gattserver-i.md#close)

**Required permissions:** ohos.permission.USE_BLUETOOTH

**System capability:** SystemCapability.Communication.Bluetooth.Core

## notifyCharacteristicChanged

```TypeScript
notifyCharacteristicChanged(deviceId: string, notifyCharacteristic: NotifyCharacteristic): boolean
```

Sends a notification of a change in a specified local characteristic.This method should be called for every BLE peripheral device that has requested notifications.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [notifyCharacteristicChanged](arkts-connectivity-bluetoothmanager-gattserver-i.md#notifycharacteristicchanged)

**Required permissions:** ohos.permission.USE_BLUETOOTH

**System capability:** SystemCapability.Communication.Bluetooth.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| deviceId | string | Yes |
| notifyCharacteristic | [NotifyCharacteristic](arkts-connectivity-ble-notifycharacteristic-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

## off('characteristicRead')

```TypeScript
off(type: 'characteristicRead', callback?: Callback<CharacteristicReadReq>): void
```

Unsubscribe characteristic read event.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** characteristicRead

**Required permissions:** ohos.permission.USE_BLUETOOTH

**System capability:** SystemCapability.Communication.Bluetooth.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'characteristicRead' | Yes |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[CharacteristicReadReq](arkts-connectivity-bluetooth-characteristicreadreq-i.md)&gt; | No |

## off('characteristicWrite')

```TypeScript
off(type: 'characteristicWrite', callback?: Callback<CharacteristicWriteReq>): void
```

Unsubscribe characteristic write event.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** characteristicWrite

**Required permissions:** ohos.permission.USE_BLUETOOTH

**System capability:** SystemCapability.Communication.Bluetooth.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'characteristicWrite' | Yes |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[CharacteristicWriteReq](arkts-connectivity-bluetooth-characteristicwritereq-i.md)&gt; | No |

## off('descriptorRead')

```TypeScript
off(type: 'descriptorRead', callback?: Callback<DescriptorReadReq>): void
```

Unsubscribe descriptor read event.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** descriptorRead

**Required permissions:** ohos.permission.USE_BLUETOOTH

**System capability:** SystemCapability.Communication.Bluetooth.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'descriptorRead' | Yes |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[DescriptorReadReq](arkts-connectivity-bluetooth-descriptorreadreq-i.md)&gt; | No |

## off('descriptorWrite')

```TypeScript
off(type: 'descriptorWrite', callback?: Callback<DescriptorWriteReq>): void
```

Unsubscribe descriptor write event.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** descriptorWrite

**Required permissions:** ohos.permission.USE_BLUETOOTH

**System capability:** SystemCapability.Communication.Bluetooth.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'descriptorWrite' | Yes |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[DescriptorWriteReq](arkts-connectivity-bluetooth-descriptorwritereq-i.md)&gt; | No |

## off('connectStateChange')

```TypeScript
off(type: 'connectStateChange', callback?: Callback<BLEConnectChangedState>): void
```

Unsubscribe server connection state changed event.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** connectStateChange

**Required permissions:** ohos.permission.USE_BLUETOOTH

**System capability:** SystemCapability.Communication.Bluetooth.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'connectStateChange' | Yes |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;BLEConnectChangedState&gt; | No |

## on('characteristicRead')

```TypeScript
on(type: 'characteristicRead', callback: Callback<CharacteristicReadReq>): void
```

Subscribe characteristic read event.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** characteristicRead

**Required permissions:** ohos.permission.USE_BLUETOOTH

**System capability:** SystemCapability.Communication.Bluetooth.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'characteristicRead' | Yes |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[CharacteristicReadReq](arkts-connectivity-bluetooth-characteristicreadreq-i.md)&gt; | Yes |

## on('characteristicWrite')

```TypeScript
on(type: 'characteristicWrite', callback: Callback<CharacteristicWriteReq>): void
```

Subscribe characteristic write event.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** characteristicWrite

**Required permissions:** ohos.permission.USE_BLUETOOTH

**System capability:** SystemCapability.Communication.Bluetooth.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'characteristicWrite' | Yes |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[CharacteristicWriteReq](arkts-connectivity-bluetooth-characteristicwritereq-i.md)&gt; | Yes |

## on('descriptorRead')

```TypeScript
on(type: 'descriptorRead', callback: Callback<DescriptorReadReq>): void
```

Subscribe descriptor read event.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** descriptorRead

**Required permissions:** ohos.permission.USE_BLUETOOTH

**System capability:** SystemCapability.Communication.Bluetooth.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'descriptorRead' | Yes |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[DescriptorReadReq](arkts-connectivity-bluetooth-descriptorreadreq-i.md)&gt; | Yes |

## on('descriptorWrite')

```TypeScript
on(type: 'descriptorWrite', callback: Callback<DescriptorWriteReq>): void
```

Subscribe descriptor write event.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** descriptorWrite

**Required permissions:** ohos.permission.USE_BLUETOOTH

**System capability:** SystemCapability.Communication.Bluetooth.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'descriptorWrite' | Yes |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[DescriptorWriteReq](arkts-connectivity-bluetooth-descriptorwritereq-i.md)&gt; | Yes |

## on('connectStateChange')

```TypeScript
on(type: 'connectStateChange', callback: Callback<BLEConnectChangedState>): void
```

Subscribe server connection state changed event.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** connectStateChange

**Required permissions:** ohos.permission.USE_BLUETOOTH

**System capability:** SystemCapability.Communication.Bluetooth.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'connectStateChange' | Yes |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;BLEConnectChangedState&gt; | Yes |

## removeService

```TypeScript
removeService(serviceUuid: string): boolean
```

Removes a specified service from the list of GATT services provided by this device.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [removeService](arkts-connectivity-bluetoothmanager-gattserver-i.md#removeservice)

**Required permissions:** ohos.permission.USE_BLUETOOTH

**System capability:** SystemCapability.Communication.Bluetooth.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| serviceUuid | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

## sendResponse

```TypeScript
sendResponse(serverResponse: ServerResponse): boolean
```

Sends a response to a specified read or write request to a given BLE peripheral device.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [sendResponse](arkts-connectivity-bluetoothmanager-gattserver-i.md#sendresponse)

**Required permissions:** ohos.permission.USE_BLUETOOTH

**System capability:** SystemCapability.Communication.Bluetooth.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| serverResponse | [ServerResponse](arkts-connectivity-ssap-serverresponse-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

## startAdvertising

```TypeScript
startAdvertising(setting: AdvertiseSetting, advData: AdvertiseData, advResponse?: AdvertiseData): void
```

Starts BLE advertising.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [startAdvertising](arkts-connectivity-bluetoothmanager-gattserver-i.md#startadvertising)

**Required permissions:** ohos.permission.DISCOVER_BLUETOOTH

**System capability:** SystemCapability.Communication.Bluetooth.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| setting | [AdvertiseSetting](arkts-connectivity-ble-advertisesetting-i.md) | Yes |
| advData | [AdvertiseData](arkts-connectivity-ble-advertisedata-i.md) | Yes |
| advResponse | [AdvertiseData](arkts-connectivity-ble-advertisedata-i.md) | No |

## stopAdvertising

```TypeScript
stopAdvertising(): void
```

Stops BLE advertising.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [stopAdvertising](arkts-connectivity-bluetoothmanager-gattserver-i.md#stopadvertising)

**Required permissions:** ohos.permission.DISCOVER_BLUETOOTH

**System capability:** SystemCapability.Communication.Bluetooth.Core
