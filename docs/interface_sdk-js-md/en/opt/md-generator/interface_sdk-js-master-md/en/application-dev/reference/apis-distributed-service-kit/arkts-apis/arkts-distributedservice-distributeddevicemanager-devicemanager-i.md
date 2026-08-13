# DeviceManager

Provides APIs to obtain information about trusted devices and local devices. Before calling any API in **DeviceManager**, you must use **createDeviceManager** to create a **DeviceManager** instance, for example, **dmInstance**.

**Since:** 23

**Deprecated since:** -1

<!--Device-distributedDeviceManager-interface DeviceManager--><!--Device-distributedDeviceManager-interface DeviceManager-End-->

**System capability:** SystemCapability.DistributedHardware.DeviceManager

## Modules to Import

```TypeScript
import { distributedDeviceManager } from '@kit.DistributedServiceKit';
```

## bindTarget

```TypeScript
bindTarget(deviceId: string, bindParam: { [key: string]: Object; }, callback: AsyncCallback<{deviceId: string;}>): void
```

Binds a device. This API uses an asynchronous callback to return the result.

**Since:** 10

**Deprecated since:** -1

**Required permissions:** ohos.permission.DISTRIBUTED_DATASYNC

<!--Device-DeviceManager-bindTarget(deviceId: string, bindParam: { [key: string]: Object; }, callback: AsyncCallback<{deviceId: string;}>): void--><!--Device-DeviceManager-bindTarget(deviceId: string, bindParam: { [key: string]: Object; }, callback: AsyncCallback<{deviceId: string;}>): void-End-->

**System capability:** SystemCapability.DistributedHardware.DeviceManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| deviceId | string | Yes |
| bindParam | { [key: string]: Object; } | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;{deviceId: string;}&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [11600101](../../apis-distributedservice-kit/errorcode-device-manager.md#11600101-service-invoking-exception) |
| [11600103](../../apis-distributedservice-kit/errorcode-device-manager.md#11600103-authentication-unavailable) |
| [201](../../errorcode-universal.md#201-permission-denied) |

## Examples

```TypeScript
import { distributedDeviceManager } from '@kit.DistributedServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

class Data {
  deviceId: string = '';
}

// Information about the device to authenticate. The information can be obtained from the device discovery result.
let deviceId = 'XXXXXXXX';
let bindParam: Record<string, string | number> = {
  'bindType': 1, // Authentication type. The value 1 means PIN authentication.
  'targetPkgName': 'xxxx',
  'appName': 'xxxx',
  'appOperation': 'xxxx',
  'customDescription': 'xxxx'
};

try {
  let dmInstance = distributedDeviceManager.createDeviceManager('ohos.samples.jsHelloWorld');
  dmInstance.bindTarget(deviceId, bindParam, (err: BusinessError, data: Data) => {
    if (err) {
      console.error('bindTarget errCode:' + err.code + ',errMessage:' + err.message);
      return;
    }
    console.info('bindTarget result:' + JSON.stringify(data));
  });
} catch (err) {
  let e: BusinessError = err as BusinessError;
  console.error('bindTarget errCode:' + e.code + ',errMessage:' + e.message);
}
```

## bindTarget

```TypeScript
bindTarget(deviceId: string, bindParam: Record<string, number | string>, callback: AsyncCallback<BindTargetResult>): void
```

Binds a device. This API uses an asynchronous callback to return the result.

**Since:** 23

**Deprecated since:** -1

**Required permissions:** ohos.permission.DISTRIBUTED_DATASYNC

<!--Device-DeviceManager-bindTarget(deviceId: string, bindParam: Record<string, int | string>, callback: AsyncCallback<BindTargetResult>): void--><!--Device-DeviceManager-bindTarget(deviceId: string, bindParam: Record<string, int | string>, callback: AsyncCallback<BindTargetResult>): void-End-->

**System capability:** SystemCapability.DistributedHardware.DeviceManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| deviceId | string | Yes |
| bindParam | [Record](../../apis-na/arkts-apis/arkts-na-record-t.md)&lt;string, number \| string & gt; | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[BindTargetResult](arkts-distributedservice-distributeddevicemanager-bindtargetresult-i.md)&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [11600101](../../apis-distributedservice-kit/errorcode-device-manager.md#11600101-service-invoking-exception) |
| [11600103](../../apis-distributedservice-kit/errorcode-device-manager.md#11600103-authentication-unavailable) |
| [201](../../errorcode-universal.md#201-permission-denied) |

## getAvailableDeviceList

```TypeScript
getAvailableDeviceList(callback: AsyncCallback<Array<DeviceBasicInfo>>): void
```

Obtains all trusted devices. This API uses an asynchronous callback to return the result.

**Since:** 23

**Deprecated since:** -1

**Required permissions:** ohos.permission.DISTRIBUTED_DATASYNC

<!--Device-DeviceManager-getAvailableDeviceList(callback: AsyncCallback<Array<DeviceBasicInfo>>): void--><!--Device-DeviceManager-getAvailableDeviceList(callback: AsyncCallback<Array<DeviceBasicInfo>>): void-End-->

**System capability:** SystemCapability.DistributedHardware.DeviceManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;[DeviceBasicInfo](arkts-distributedservice-distributeddevicemanager-devicebasicinfo-i.md)&gt;&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [11600101](../../apis-distributedservice-kit/errorcode-device-manager.md#11600101-service-invoking-exception) |
| [201](../../errorcode-universal.md#201-permission-denied) |

## Examples

```TypeScript
import { distributedDeviceManager } from '@kit.DistributedServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let dmInstance = distributedDeviceManager.createDeviceManager('ohos.samples.jsHelloWorld');
  dmInstance.getAvailableDeviceList((err: BusinessError, data: Array<distributedDeviceManager.DeviceBasicInfo>) => {
    if (err) {
      console.error('getAvailableDeviceList errCode:' + err.code + ',errMessage:' + err.message);
      return;
    }
    console.info('get available device info: ' + JSON.stringify(data));
  });
} catch (err) {
  let e: BusinessError = err as BusinessError;
  console.error('getAvailableDeviceList errCode:' + e.code + ',errMessage:' + e.message);
}
```

## getAvailableDeviceList

```TypeScript
getAvailableDeviceList(): Promise<Array<DeviceBasicInfo>>
```

Obtains all trusted devices. This API uses a promise to return the result.

**Since:** 23

**Deprecated since:** -1

**Required permissions:** ohos.permission.DISTRIBUTED_DATASYNC

<!--Device-DeviceManager-getAvailableDeviceList(): Promise<Array<DeviceBasicInfo>>--><!--Device-DeviceManager-getAvailableDeviceList(): Promise<Array<DeviceBasicInfo>>-End-->

**System capability:** SystemCapability.DistributedHardware.DeviceManager

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;Array&lt;[DeviceBasicInfo](arkts-distributedservice-distributeddevicemanager-devicebasicinfo-i.md)&gt;&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [11600101](../../apis-distributedservice-kit/errorcode-device-manager.md#11600101-service-invoking-exception) |
| [201](../../errorcode-universal.md#201-permission-denied) |

## Examples

```TypeScript
import { distributedDeviceManager } from '@kit.DistributedServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

let dmInstance = distributedDeviceManager.createDeviceManager('ohos.samples.jsHelloWorld');
dmInstance.getAvailableDeviceList().then((data: Array<distributedDeviceManager.DeviceBasicInfo>) => {
  console.info('get available device info: ' + JSON.stringify(data));
  }).catch((err: BusinessError) => {
    console.error('getAvailableDeviceList errCode:' + err.code + ',errMessage:' + err.message);
});
```

## getAvailableDeviceListSync

```TypeScript
getAvailableDeviceListSync(): Array<DeviceBasicInfo>
```

Obtains all trusted devices synchronously.

**Since:** 23

**Deprecated since:** -1

**Required permissions:** ohos.permission.DISTRIBUTED_DATASYNC

<!--Device-DeviceManager-getAvailableDeviceListSync(): Array<DeviceBasicInfo>--><!--Device-DeviceManager-getAvailableDeviceListSync(): Array<DeviceBasicInfo>-End-->

**System capability:** SystemCapability.DistributedHardware.DeviceManager

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Array&lt;[DeviceBasicInfo](arkts-distributedservice-distributeddevicemanager-devicebasicinfo-i.md)&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [11600101](../../apis-distributedservice-kit/errorcode-device-manager.md#11600101-service-invoking-exception) |
| [201](../../errorcode-universal.md#201-permission-denied) |

## Examples

```TypeScript
import { distributedDeviceManager } from '@kit.DistributedServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let dmInstance = distributedDeviceManager.createDeviceManager('ohos.samples.jsHelloWorld');
  let deviceInfoList: Array<distributedDeviceManager.DeviceBasicInfo> = dmInstance.getAvailableDeviceListSync();
} catch (err) {
  let e: BusinessError = err as BusinessError;
  console.error('getAvailableDeviceListSync errCode:' + e.code + ',errMessage:' + e.message);
}
```

## getDeviceName

```TypeScript
getDeviceName(networkId: string): string
```

Obtains the device name based on the network ID of the specified device.

**Since:** 23

**Deprecated since:** -1

**Required permissions:** ohos.permission.DISTRIBUTED_DATASYNC

<!--Device-DeviceManager-getDeviceName(networkId: string): string--><!--Device-DeviceManager-getDeviceName(networkId: string): string-End-->

**System capability:** SystemCapability.DistributedHardware.DeviceManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| networkId | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| string |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [11600101](../../apis-distributedservice-kit/errorcode-device-manager.md#11600101-service-invoking-exception) |
| [201](../../errorcode-universal.md#201-permission-denied) |

## Examples

```TypeScript
import { distributedDeviceManager } from '@kit.DistributedServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  // Network ID of the device, which can be obtained from the trusted device list.
  let networkId = 'xxxxxxx';
  let dmInstance = distributedDeviceManager.createDeviceManager('ohos.samples.jsHelloWorld');
  let deviceName: string = dmInstance.getDeviceName(networkId);
  console.info('device name: ' + JSON.stringify(deviceName)); 
} catch (err) {
  let e: BusinessError = err as BusinessError;
  console.error('getDeviceName errCode:' + e.code + ',errMessage:' + e.message);
}
```

## getDeviceType

```TypeScript
getDeviceType(networkId: string): number
```

Obtains the device type based on the network ID of the specified device.

**Since:** 23

**Deprecated since:** -1

**Required permissions:** ohos.permission.DISTRIBUTED_DATASYNC

<!--Device-DeviceManager-getDeviceType(networkId: string): int--><!--Device-DeviceManager-getDeviceType(networkId: string): int-End-->

**System capability:** SystemCapability.DistributedHardware.DeviceManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| networkId | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [11600101](../../apis-distributedservice-kit/errorcode-device-manager.md#11600101-service-invoking-exception) |
| [201](../../errorcode-universal.md#201-permission-denied) |

## Examples

```TypeScript
import { distributedDeviceManager } from '@kit.DistributedServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  // Network ID of the device, which can be obtained from the trusted device list.
  let networkId = 'xxxxxxx';
  let dmInstance = distributedDeviceManager.createDeviceManager('ohos.samples.jsHelloWorld');
  let deviceType: number = dmInstance.getDeviceType(networkId);
  console.info('device type: ' + JSON.stringify(deviceType)); 
} catch (err) {
  let e: BusinessError = err as BusinessError;
  console.error('getDeviceType errCode:' + e.code + ',errMessage:' + e.message);
}
```

## getLocalDeviceId

```TypeScript
getLocalDeviceId(): string
```

Obtains the local device ID. The value is the result of obfuscating the udid-hash (hash value of the UDID), **appid**, and salt using the SHA-256 algorithm.

**Since:** 23

**Deprecated since:** -1

**Required permissions:** ohos.permission.DISTRIBUTED_DATASYNC

<!--Device-DeviceManager-getLocalDeviceId(): string--><!--Device-DeviceManager-getLocalDeviceId(): string-End-->

**System capability:** SystemCapability.DistributedHardware.DeviceManager

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| string |

**Error codes:**

| Error Code ID |
| --- |
| [11600101](../../apis-distributedservice-kit/errorcode-device-manager.md#11600101-service-invoking-exception) |
| [201](../../errorcode-universal.md#201-permission-denied) |

## Examples

```TypeScript
import { distributedDeviceManager } from '@kit.DistributedServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let dmInstance = distributedDeviceManager.createDeviceManager('ohos.samples.jsHelloWorld');
  let deviceId: string = dmInstance.getLocalDeviceId();
  console.info('local device id: ' + JSON.stringify(deviceId));
} catch (err) {
  let e: BusinessError = err as BusinessError;
  console.error('getLocalDeviceId errCode:' + e.code + ',errMessage:' + e.message);
}
```

## getLocalDeviceName

```TypeScript
getLocalDeviceName(): string
```

Obtains the local device name.

**Since:** 23

**Deprecated since:** -1

**Required permissions:** ohos.permission.DISTRIBUTED_DATASYNC

<!--Device-DeviceManager-getLocalDeviceName(): string--><!--Device-DeviceManager-getLocalDeviceName(): string-End-->

**System capability:** SystemCapability.DistributedHardware.DeviceManager

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| string |

**Error codes:**

| Error Code ID |
| --- |
| [11600101](../../apis-distributedservice-kit/errorcode-device-manager.md#11600101-service-invoking-exception) |
| [201](../../errorcode-universal.md#201-permission-denied) |

## Examples

```TypeScript
import { distributedDeviceManager } from '@kit.DistributedServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let dmInstance = distributedDeviceManager.createDeviceManager('ohos.samples.jsHelloWorld');
  let deviceName: string = dmInstance.getLocalDeviceName();
  console.info('local device name: ' + JSON.stringify(deviceName));
} catch (err) {
  let e: BusinessError = err as BusinessError;
  console.error('getLocalDeviceName errCode:' + e.code + ',errMessage:' + e.message);
}
```

## getLocalDeviceNetworkId

```TypeScript
getLocalDeviceNetworkId(): string
```

Obtains the network ID of the local device.

**Since:** 23

**Deprecated since:** -1

**Required permissions:** ohos.permission.DISTRIBUTED_DATASYNC

<!--Device-DeviceManager-getLocalDeviceNetworkId(): string--><!--Device-DeviceManager-getLocalDeviceNetworkId(): string-End-->

**System capability:** SystemCapability.DistributedHardware.DeviceManager

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| string |

**Error codes:**

| Error Code ID |
| --- |
| [11600101](../../apis-distributedservice-kit/errorcode-device-manager.md#11600101-service-invoking-exception) |
| [201](../../errorcode-universal.md#201-permission-denied) |

## Examples

```TypeScript
import { distributedDeviceManager } from '@kit.DistributedServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let dmInstance = distributedDeviceManager.createDeviceManager('ohos.samples.jsHelloWorld');
  let deviceNetworkId: string = dmInstance.getLocalDeviceNetworkId();
  console.info('local device networkId: ' + JSON.stringify(deviceNetworkId));
} catch (err) {
  let e: BusinessError = err as BusinessError;
  console.error('getLocalDeviceNetworkId errCode:' + e.code + ',errMessage:' + e.message);
}
```

## getLocalDeviceType

```TypeScript
getLocalDeviceType(): number
```

Obtains the local device type.

**Since:** 23

**Deprecated since:** -1

**Required permissions:** ohos.permission.DISTRIBUTED_DATASYNC

<!--Device-DeviceManager-getLocalDeviceType(): int--><!--Device-DeviceManager-getLocalDeviceType(): int-End-->

**System capability:** SystemCapability.DistributedHardware.DeviceManager

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number |

**Error codes:**

| Error Code ID |
| --- |
| [11600101](../../apis-distributedservice-kit/errorcode-device-manager.md#11600101-service-invoking-exception) |
| [201](../../errorcode-universal.md#201-permission-denied) |

## Examples

```TypeScript
import { distributedDeviceManager } from '@kit.DistributedServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let dmInstance = distributedDeviceManager.createDeviceManager('ohos.samples.jsHelloWorld');
  let deviceType: number = dmInstance.getLocalDeviceType();
  console.info('local device type: ' + JSON.stringify(deviceType));
} catch (err) {
  let e: BusinessError = err as BusinessError;
  console.error('getLocalDeviceType errCode:' + e.code + ',errMessage:' + e.message);
}
```

## offDeviceNameChange

```TypeScript
offDeviceNameChange(callback?: Callback<DeviceNameChangeResult>): void
```

UnRegister the device name change result callback.

**Since:** 23

**Deprecated since:** -1

**Required permissions:** ohos.permission.DISTRIBUTED_DATASYNC

<!--Device-DeviceManager-offDeviceNameChange(callback?: Callback<DeviceNameChangeResult>): void--><!--Device-DeviceManager-offDeviceNameChange(callback?: Callback<DeviceNameChangeResult>): void-End-->

**System capability:** SystemCapability.DistributedHardware.DeviceManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[DeviceNameChangeResult](arkts-distributedservice-distributeddevicemanager-devicenamechangeresult-i.md)&gt; | No |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |

## offDeviceStateChange

```TypeScript
offDeviceStateChange(callback?: Callback<DeviceStateChangeResult>): void
```

UnRegister device state callback based on the application bundle name.

**Since:** 23

**Deprecated since:** -1

**Required permissions:** ohos.permission.DISTRIBUTED_DATASYNC

<!--Device-DeviceManager-offDeviceStateChange(callback?: Callback<DeviceStateChangeResult>): void--><!--Device-DeviceManager-offDeviceStateChange(callback?: Callback<DeviceStateChangeResult>): void-End-->

**System capability:** SystemCapability.DistributedHardware.DeviceManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[DeviceStateChangeResult](arkts-distributedservice-distributeddevicemanager-devicestatechangeresult-i.md)&gt; | No |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |

## offDiscoverFailure

```TypeScript
offDiscoverFailure(callback?: Callback<DiscoveryFailureResult>): void
```

UnRegister the device discovery result callback.

**Since:** 23

**Deprecated since:** -1

**Required permissions:** ohos.permission.DISTRIBUTED_DATASYNC

<!--Device-DeviceManager-offDiscoverFailure(callback?: Callback<DiscoveryFailureResult>): void--><!--Device-DeviceManager-offDiscoverFailure(callback?: Callback<DiscoveryFailureResult>): void-End-->

**System capability:** SystemCapability.DistributedHardware.DeviceManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[DiscoveryFailureResult](arkts-distributedservice-distributeddevicemanager-discoveryfailureresult-i.md)&gt; | No |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |

## offDiscoverSuccess

```TypeScript
offDiscoverSuccess(callback?: Callback<DiscoverySuccessResult>): void
```

UnRegister the device discovery result callback.

**Since:** 23

**Deprecated since:** -1

**Required permissions:** ohos.permission.DISTRIBUTED_DATASYNC

<!--Device-DeviceManager-offDiscoverSuccess(callback?: Callback<DiscoverySuccessResult>): void--><!--Device-DeviceManager-offDiscoverSuccess(callback?: Callback<DiscoverySuccessResult>): void-End-->

**System capability:** SystemCapability.DistributedHardware.DeviceManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[DiscoverySuccessResult](arkts-distributedservice-distributeddevicemanager-discoverysuccessresult-i.md)&gt; | No |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |

## offServiceDie

```TypeScript
offServiceDie(callback?: Callback<ServiceDieData>): void
```

UnRegister the service error callback.

**Since:** 23

**Deprecated since:** -1

**Required permissions:** ohos.permission.DISTRIBUTED_DATASYNC

<!--Device-DeviceManager-offServiceDie(callback?: Callback<ServiceDieData>): void--><!--Device-DeviceManager-offServiceDie(callback?: Callback<ServiceDieData>): void-End-->

**System capability:** SystemCapability.DistributedHardware.DeviceManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[ServiceDieData](arkts-distributedservice-distributeddevicemanager-servicediedata-i.md)&gt; | No |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |

## off_deviceNameChange

```TypeScript
off(type: 'deviceNameChange', callback?: Callback<{ deviceName: string; }>): void
```

Unsubscribes from the device name changes. This API uses an asynchronous callback to return the result.

**Since:** 10

**Deprecated since:** -1

**Required permissions:** ohos.permission.DISTRIBUTED_DATASYNC

<!--Device-DeviceManager-off(type: 'deviceNameChange', callback?: Callback<{ deviceName: string; }>): void--><!--Device-DeviceManager-off(type: 'deviceNameChange', callback?: Callback<{ deviceName: string; }>): void-End-->

**System capability:** SystemCapability.DistributedHardware.DeviceManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'deviceNameChange' | Yes |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;{ deviceName: string; }&gt; | No |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [201](../../errorcode-universal.md#201-permission-denied) |

## Examples

```TypeScript
import { distributedDeviceManager } from '@kit.DistributedServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

class Data {
  deviceName: string = '';
}

try {
  let dmInstance = distributedDeviceManager.createDeviceManager('ohos.samples.jsHelloWorld');
  dmInstance.off('deviceNameChange', (data: Data) => {
    console.info('deviceNameChange' + JSON.stringify(data));
  });
} catch (err) {
  let e: BusinessError = err as BusinessError;
  console.error('deviceNameChange errCode:' + e.code + ',errMessage:' + e.message);
}
```

## off_deviceStateChange

```TypeScript
off(type: 'deviceStateChange', callback?: Callback<{ action: DeviceStateChange; device: DeviceBasicInfo; }>): void
```

Unsubscribes from the device state changes. This API uses an asynchronous callback to return the result.

**Since:** 10

**Deprecated since:** -1

**Required permissions:** ohos.permission.DISTRIBUTED_DATASYNC

<!--Device-DeviceManager-off(type: 'deviceStateChange', callback?: Callback<{ action: DeviceStateChange; device: DeviceBasicInfo; }>): void--><!--Device-DeviceManager-off(type: 'deviceStateChange', callback?: Callback<{ action: DeviceStateChange; device: DeviceBasicInfo; }>): void-End-->

**System capability:** SystemCapability.DistributedHardware.DeviceManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'deviceStateChange' | Yes |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;{ action: DeviceStateChange; device: DeviceBasicInfo; }&gt; | No |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [201](../../errorcode-universal.md#201-permission-denied) |

## Examples

```TypeScript
import { distributedDeviceManager } from '@kit.DistributedServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

class Data {
  action: distributedDeviceManager.DeviceStateChange = 0;
  device: distributedDeviceManager.DeviceBasicInfo = {
    deviceId: '',
    deviceName: '',
    deviceType: '',
    networkId: ''
  };
}

try {
  let dmInstance = distributedDeviceManager.createDeviceManager('ohos.samples.jsHelloWorld');
  dmInstance.off('deviceStateChange', (data: Data) => {
    console.info('deviceStateChange' + JSON.stringify(data));
  });
} catch (err) {
  let e: BusinessError = err as BusinessError;
  console.error('deviceStateChange errCode:' + e.code + ',errMessage:' + e.message);
}
```

## off_discoverFailure

```TypeScript
off(type: 'discoverFailure', callback?: Callback<{ reason: number; }>): void
```

Unsubscribes from the **'discoverFailure'** event. This API uses an asynchronous callback to return the result.

**Since:** 10

**Deprecated since:** -1

**Required permissions:** ohos.permission.DISTRIBUTED_DATASYNC

<!--Device-DeviceManager-off(type: 'discoverFailure', callback?: Callback<{ reason: int; }>): void--><!--Device-DeviceManager-off(type: 'discoverFailure', callback?: Callback<{ reason: int; }>): void-End-->

**System capability:** SystemCapability.DistributedHardware.DeviceManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'discoverFailure' | Yes |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;{ reason: number; }&gt; | No |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [201](../../errorcode-universal.md#201-permission-denied) |

## Examples

```TypeScript
import { distributedDeviceManager } from '@kit.DistributedServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

class Data {
  reason: number = 0;
}

try {
  let dmInstance = distributedDeviceManager.createDeviceManager('ohos.samples.jsHelloWorld');
  dmInstance.off('discoverFailure', (data: Data) => {
    console.info('discoverFailure' + JSON.stringify(data));
  });
} catch (err) {
  let e: BusinessError = err as BusinessError;
  console.error('discoverFailure errCode:' + e.code + ',errMessage:' + e.message);
}
```

## off_discoverSuccess

```TypeScript
off(type: 'discoverSuccess', callback?: Callback<{ device: DeviceBasicInfo; }>): void
```

Unsubscribes from the **'discoverSuccess'** event. This API uses an asynchronous callback to return the result.

**Since:** 10

**Deprecated since:** -1

**Required permissions:** ohos.permission.DISTRIBUTED_DATASYNC

<!--Device-DeviceManager-off(type: 'discoverSuccess', callback?: Callback<{ device: DeviceBasicInfo; }>): void--><!--Device-DeviceManager-off(type: 'discoverSuccess', callback?: Callback<{ device: DeviceBasicInfo; }>): void-End-->

**System capability:** SystemCapability.DistributedHardware.DeviceManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'discoverSuccess' | Yes |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;{ device: DeviceBasicInfo; }&gt; | No |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [201](../../errorcode-universal.md#201-permission-denied) |

## Examples

```TypeScript
import { distributedDeviceManager } from '@kit.DistributedServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

class Data {
  device: distributedDeviceManager.DeviceBasicInfo = {
    deviceId: '',
    deviceName: '',
    deviceType: '',
    networkId: ''
  };
}

try {
  let dmInstance = distributedDeviceManager.createDeviceManager('ohos.samples.jsHelloWorld');
  dmInstance.off('discoverSuccess', (data: Data) => {
    console.info('discoverSuccess' + JSON.stringify(data));
  });
} catch (err) {
  let e: BusinessError = err as BusinessError;
  console.error('discoverSuccess errCode:' + e.code + ',errMessage:' + e.message);
}
```

## off_serviceDie

```TypeScript
off(type: 'serviceDie', callback?: Callback<{}>): void
```

Unsubscribes from the dead events of the **DeviceManager** service. This API uses an asynchronous callback to return the result.

**Since:** 10

**Deprecated since:** -1

**Required permissions:** ohos.permission.DISTRIBUTED_DATASYNC

<!--Device-DeviceManager-off(type: 'serviceDie', callback?: Callback<{}>): void--><!--Device-DeviceManager-off(type: 'serviceDie', callback?: Callback<{}>): void-End-->

**System capability:** SystemCapability.DistributedHardware.DeviceManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'serviceDie' | Yes |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;{}&gt; | No |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [201](../../errorcode-universal.md#201-permission-denied) |

## Examples

```TypeScript
import { distributedDeviceManager } from '@kit.DistributedServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let dmInstance = distributedDeviceManager.createDeviceManager('ohos.samples.jsHelloWorld');
  dmInstance.off('serviceDie', () => {
    console.info('serviceDie off');
  });
} catch (err) {
  let e: BusinessError = err as BusinessError;
  console.error('serviceDie errCode:' + e.code + ',errMessage:' + e.message);
}
```

## onDeviceNameChange

```TypeScript
onDeviceNameChange(callback: Callback<DeviceNameChangeResult>): void
```

Register a device name change callback so that the application can be notified when discovery success.

**Since:** 23

**Deprecated since:** -1

**Required permissions:** ohos.permission.DISTRIBUTED_DATASYNC

<!--Device-DeviceManager-onDeviceNameChange(callback: Callback<DeviceNameChangeResult>): void--><!--Device-DeviceManager-onDeviceNameChange(callback: Callback<DeviceNameChangeResult>): void-End-->

**System capability:** SystemCapability.DistributedHardware.DeviceManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[DeviceNameChangeResult](arkts-distributedservice-distributeddevicemanager-devicenamechangeresult-i.md)&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |

## onDeviceStateChange

```TypeScript
onDeviceStateChange(callback: Callback<DeviceStateChangeResult>): void
```

Register a device state callback so that the application can be notified upon device state changes based on the application bundle name.

**Since:** 23

**Deprecated since:** -1

**Required permissions:** ohos.permission.DISTRIBUTED_DATASYNC

<!--Device-DeviceManager-onDeviceStateChange(callback: Callback<DeviceStateChangeResult>): void--><!--Device-DeviceManager-onDeviceStateChange(callback: Callback<DeviceStateChangeResult>): void-End-->

**System capability:** SystemCapability.DistributedHardware.DeviceManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[DeviceStateChangeResult](arkts-distributedservice-distributeddevicemanager-devicestatechangeresult-i.md)&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |

## onDiscoverFailure

```TypeScript
onDiscoverFailure(callback: Callback<DiscoveryFailureResult>): void
```

Register a device discovery result callback so that the application can be notified when discover failed.

**Since:** 23

**Deprecated since:** -1

**Required permissions:** ohos.permission.DISTRIBUTED_DATASYNC

<!--Device-DeviceManager-onDiscoverFailure(callback: Callback<DiscoveryFailureResult>): void--><!--Device-DeviceManager-onDiscoverFailure(callback: Callback<DiscoveryFailureResult>): void-End-->

**System capability:** SystemCapability.DistributedHardware.DeviceManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[DiscoveryFailureResult](arkts-distributedservice-distributeddevicemanager-discoveryfailureresult-i.md)&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |

## onDiscoverSuccess

```TypeScript
onDiscoverSuccess(callback: Callback<DiscoverySuccessResult>): void
```

Register a device discovery result callback so that the application can be notified when discovery success.

**Since:** 23

**Deprecated since:** -1

**Required permissions:** ohos.permission.DISTRIBUTED_DATASYNC

<!--Device-DeviceManager-onDiscoverSuccess(callback: Callback<DiscoverySuccessResult>): void--><!--Device-DeviceManager-onDiscoverSuccess(callback: Callback<DiscoverySuccessResult>): void-End-->

**System capability:** SystemCapability.DistributedHardware.DeviceManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[DiscoverySuccessResult](arkts-distributedservice-distributeddevicemanager-discoverysuccessresult-i.md)&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |

## onServiceDie

```TypeScript
onServiceDie(callback: Callback<ServiceDieData>): void
```

Register a serviceError callback so that the application can be notified when devicemanager service died

**Since:** 23

**Deprecated since:** -1

**Required permissions:** ohos.permission.DISTRIBUTED_DATASYNC

<!--Device-DeviceManager-onServiceDie(callback: Callback<ServiceDieData>): void--><!--Device-DeviceManager-onServiceDie(callback: Callback<ServiceDieData>): void-End-->

**System capability:** SystemCapability.DistributedHardware.DeviceManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[ServiceDieData](arkts-distributedservice-distributeddevicemanager-servicediedata-i.md)&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |

## on_deviceNameChange

```TypeScript
on(type: 'deviceNameChange', callback: Callback<{ deviceName: string; }>): void
```

Subscribes to device name changes. The application will be notified when the name of a device is changed. This API uses an asynchronous callback to return the result.

**Since:** 10

**Deprecated since:** -1

**Required permissions:** ohos.permission.DISTRIBUTED_DATASYNC

<!--Device-DeviceManager-on(type: 'deviceNameChange', callback: Callback<{ deviceName: string; }>): void--><!--Device-DeviceManager-on(type: 'deviceNameChange', callback: Callback<{ deviceName: string; }>): void-End-->

**System capability:** SystemCapability.DistributedHardware.DeviceManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'deviceNameChange' | Yes |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;{ deviceName: string; }&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [201](../../errorcode-universal.md#201-permission-denied) |

## Examples

```TypeScript
import { distributedDeviceManager } from '@kit.DistributedServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

class Data {
  deviceName: string = '';
}

try {
  let dmInstance = distributedDeviceManager.createDeviceManager('ohos.samples.jsHelloWorld');
  dmInstance.on('deviceNameChange', (data: Data) => {
    console.info('deviceNameChange on:' + JSON.stringify(data));
  });
} catch (err) {
  let e: BusinessError = err as BusinessError;
  console.error('deviceNameChange errCode:' + e.code + ',errMessage:' + e.message);
}
```

## on_deviceStateChange

```TypeScript
on(type: 'deviceStateChange', callback: Callback<{ action: DeviceStateChange; device: DeviceBasicInfo; }>): void
```

Subscribes to the device state changes. The application (identified by the bundle name) will be notified when the device state changes. This API uses an asynchronous callback to return the result.

**Since:** 10

**Deprecated since:** -1

**Required permissions:** ohos.permission.DISTRIBUTED_DATASYNC

<!--Device-DeviceManager-on(type: 'deviceStateChange', callback: Callback<{ action: DeviceStateChange; device: DeviceBasicInfo; }>): void--><!--Device-DeviceManager-on(type: 'deviceStateChange', callback: Callback<{ action: DeviceStateChange; device: DeviceBasicInfo; }>): void-End-->

**System capability:** SystemCapability.DistributedHardware.DeviceManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'deviceStateChange' | Yes |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;{ action: DeviceStateChange; device: DeviceBasicInfo; }&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [201](../../errorcode-universal.md#201-permission-denied) |

## Examples

```TypeScript
import { distributedDeviceManager } from '@kit.DistributedServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

class Data {
  action: distributedDeviceManager.DeviceStateChange = 0;
  device: distributedDeviceManager.DeviceBasicInfo = {
    deviceId: '',
    deviceName: '',
    deviceType: '',
    networkId: ''
  };
}

try {
  let dmInstance = distributedDeviceManager.createDeviceManager('ohos.samples.jsHelloWorld');
  dmInstance.on('deviceStateChange', (data: Data) => {
    console.info('deviceStateChange on:' + JSON.stringify(data));
  });
} catch (err) {
  let e: BusinessError = err as BusinessError;
  console.error('deviceStateChange errCode:' + e.code + ',errMessage:' + e.message);
}
```

## on_discoverFailure

```TypeScript
on(type: 'discoverFailure', callback: Callback<{ reason: number; }>): void
```

Subscribes to the **'discoverFailure'** event. The application will be notified when a device fails to be discovered. This API uses an asynchronous callback to return the result.

**Since:** 10

**Deprecated since:** -1

**Required permissions:** ohos.permission.DISTRIBUTED_DATASYNC

<!--Device-DeviceManager-on(type: 'discoverFailure', callback: Callback<{ reason: int; }>): void--><!--Device-DeviceManager-on(type: 'discoverFailure', callback: Callback<{ reason: int; }>): void-End-->

**System capability:** SystemCapability.DistributedHardware.DeviceManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'discoverFailure' | Yes |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;{ reason: number; }&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [201](../../errorcode-universal.md#201-permission-denied) |

## Examples

```TypeScript
import { distributedDeviceManager } from '@kit.DistributedServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

class Data {
  reason: number = 0;
}

try {
  let dmInstance = distributedDeviceManager.createDeviceManager('ohos.samples.jsHelloWorld');
  dmInstance.on('discoverFailure', (data: Data) => {
    console.info('discoverFailure on:' + JSON.stringify(data));
  });
} catch (err) {
  let e: BusinessError = err as BusinessError;
  console.error('discoverFailure errCode:' + e.code + ',errMessage:' + e.message);
}
```

## on_discoverSuccess

```TypeScript
on(type: 'discoverSuccess', callback: Callback<{ device: DeviceBasicInfo; }>): void
```

Subscribes to the **'discoverSuccess'** event. The application will be notified when a device is successfully discovered. This API uses an asynchronous callback to return the result.

**Since:** 10

**Deprecated since:** -1

**Required permissions:** ohos.permission.DISTRIBUTED_DATASYNC

<!--Device-DeviceManager-on(type: 'discoverSuccess', callback: Callback<{ device: DeviceBasicInfo; }>): void--><!--Device-DeviceManager-on(type: 'discoverSuccess', callback: Callback<{ device: DeviceBasicInfo; }>): void-End-->

**System capability:** SystemCapability.DistributedHardware.DeviceManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'discoverSuccess' | Yes |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;{ device: DeviceBasicInfo; }&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [201](../../errorcode-universal.md#201-permission-denied) |

## Examples

```TypeScript
import { distributedDeviceManager } from '@kit.DistributedServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

class Data {
  device: distributedDeviceManager.DeviceBasicInfo = {
    deviceId: '',
    deviceName: '',
    deviceType: '',
    networkId: ''
  };
}

try {
  let dmInstance = distributedDeviceManager.createDeviceManager('ohos.samples.jsHelloWorld');
  dmInstance.on('discoverSuccess', (data: Data) => {
    console.info('discoverSuccess:' + JSON.stringify(data));
  });
} catch (err) {
  let e: BusinessError = err as BusinessError;
  console.error('discoverSuccess errCode:' + e.code + ',errMessage:' + e.message);
}
```

## on_serviceDie

```TypeScript
on(type: 'serviceDie', callback?: Callback<{}>): void
```

Subscribes to the dead events of the **DeviceManager** service. The application will be notified when the **DeviceManager** service is terminated unexpectedly. This API uses an asynchronous callback to return the result.

**Since:** 10

**Deprecated since:** -1

**Required permissions:** ohos.permission.DISTRIBUTED_DATASYNC

<!--Device-DeviceManager-on(type: 'serviceDie', callback?: Callback<{}>): void--><!--Device-DeviceManager-on(type: 'serviceDie', callback?: Callback<{}>): void-End-->

**System capability:** SystemCapability.DistributedHardware.DeviceManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'serviceDie' | Yes |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;{}&gt; | No |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [201](../../errorcode-universal.md#201-permission-denied) |

## Examples

```TypeScript
import { distributedDeviceManager } from '@kit.DistributedServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let dmInstance = distributedDeviceManager.createDeviceManager('ohos.samples.jsHelloWorld');
  dmInstance.on('serviceDie', () => {
    console.info('serviceDie on');
  });
} catch (err) {
  let e: BusinessError = err as BusinessError;
  console.error('serviceDie errCode:' + e.code + ',errMessage:' + e.message);
}
```

## startDiscovering

```TypeScript
startDiscovering(discoverParam: { [key: string]: Object; }, filterOptions?: { [key: string]: Object; }): void
```

Starts to discover devices nearby. The discovery process takes 2 minutes. A maximum of 99 devices can be discovered. In Wi-Fi scenarios, only the devices in the same LAN can be discovered.

**Since:** 10

**Deprecated since:** -1

**Required permissions:** ohos.permission.DISTRIBUTED_DATASYNC

<!--Device-DeviceManager-startDiscovering(discoverParam: { [key: string]: Object; }, filterOptions?: { [key: string]: Object; }): void--><!--Device-DeviceManager-startDiscovering(discoverParam: { [key: string]: Object; }, filterOptions?: { [key: string]: Object; }): void-End-->

**System capability:** SystemCapability.DistributedHardware.DeviceManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| discoverParam | { [key: string]: Object; } | Yes |
| [filterOptions](../../apis-audio-kit/arkts-apis/arkts-audio-audio-audioplaybackcaptureconfig-i.md) | { [key: string]: Object; } | No |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [11600101](../../apis-distributedservice-kit/errorcode-device-manager.md#11600101-service-invoking-exception) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [11600104](../../apis-distributedservice-kit/errorcode-device-manager.md#11600104-discovery-unavailable) |

## Examples

```TypeScript
import { distributedDeviceManager } from '@kit.DistributedServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

interface DiscoverParam {
  discoverTargetType: number;
}

interface FilterOptions {
  availableStatus: number;
  discoverDistance: number;
  authenticationStatus: number;
  authorizationType: number;
}

let discoverParam: Record<string, number> = {
  'discoverTargetType': 1
};
let filterOptions: Record<string, number> = {
  'availableStatus': 0
};

try {
  let dmInstance = distributedDeviceManager.createDeviceManager('ohos.samples.jsHelloWorld');
  dmInstance.startDiscovering(discoverParam, filterOptions); // When devices are discovered, discoverSuccess is called to notify the application.
} catch (err) {
  let e: BusinessError = err as BusinessError;
  console.error('startDiscovering errCode:' + e.code + ',errMessage:' + e.message);
}
```

## startDiscovering

```TypeScript
startDiscovering(discoverParam: Record<string, number | string>, filterOptions?: Record<string, number | string>): void
```

Starts to discover devices nearby. The discovery process takes 2 minutes. A maximum of 99 devices can be discovered. In Wi-Fi scenarios, only the devices in the same LAN can be discovered.

**Since:** 23

**Deprecated since:** -1

**Required permissions:** ohos.permission.DISTRIBUTED_DATASYNC

<!--Device-DeviceManager-startDiscovering(discoverParam: Record<string, int | string>, filterOptions?: Record<string, int | string>): void--><!--Device-DeviceManager-startDiscovering(discoverParam: Record<string, int | string>, filterOptions?: Record<string, int | string>): void-End-->

**System capability:** SystemCapability.DistributedHardware.DeviceManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| discoverParam | [Record](../../apis-na/arkts-apis/arkts-na-record-t.md)&lt;string, number \| string & gt; | Yes |
| [filterOptions](../../apis-audio-kit/arkts-apis/arkts-audio-audio-audioplaybackcaptureconfig-i.md) | [Record](../../apis-na/arkts-apis/arkts-na-record-t.md)&lt;string, number \| string & gt; | No |

**Error codes:**

| Error Code ID |
| --- |
| [11600101](../../apis-distributedservice-kit/errorcode-device-manager.md#11600101-service-invoking-exception) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [11600104](../../apis-distributedservice-kit/errorcode-device-manager.md#11600104-discovery-unavailable) |

## stopDiscovering

```TypeScript
stopDiscovering(): void
```

Stops device discovery.

**Since:** 23

**Deprecated since:** -1

**Required permissions:** ohos.permission.DISTRIBUTED_DATASYNC

<!--Device-DeviceManager-stopDiscovering(): void--><!--Device-DeviceManager-stopDiscovering(): void-End-->

**System capability:** SystemCapability.DistributedHardware.DeviceManager

**Error codes:**

| Error Code ID |
| --- |
| [11600101](../../apis-distributedservice-kit/errorcode-device-manager.md#11600101-service-invoking-exception) |
| [201](../../errorcode-universal.md#201-permission-denied) |

## Examples

```TypeScript
import { distributedDeviceManager } from '@kit.DistributedServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let dmInstance = distributedDeviceManager.createDeviceManager('ohos.samples.jsHelloWorld');
  dmInstance.stopDiscovering();
} catch (err) {
  let e: BusinessError = err as BusinessError;
  console.error('stopDiscovering errCode:' + e.code + ',errMessage:' + e.message);
}
```

## unbindTarget

```TypeScript
unbindTarget(deviceId: string): void
```

Unbinds a device.

**Since:** 23

**Deprecated since:** -1

**Required permissions:** ohos.permission.DISTRIBUTED_DATASYNC

<!--Device-DeviceManager-unbindTarget(deviceId: string): void--><!--Device-DeviceManager-unbindTarget(deviceId: string): void-End-->

**System capability:** SystemCapability.DistributedHardware.DeviceManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| deviceId | string | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [11600101](../../apis-distributedservice-kit/errorcode-device-manager.md#11600101-service-invoking-exception) |
| [201](../../errorcode-universal.md#201-permission-denied) |

## Examples

```TypeScript
import { distributedDeviceManager } from '@kit.DistributedServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let deviceId = 'XXXXXXXX';
  let dmInstance = distributedDeviceManager.createDeviceManager('ohos.samples.jsHelloWorld');
  dmInstance.unbindTarget(deviceId);
} catch (err) {
  let e: BusinessError = err as BusinessError;
  console.error('unbindTarget errCode:' + e.code + ',errMessage:' + e.message);
}
```
