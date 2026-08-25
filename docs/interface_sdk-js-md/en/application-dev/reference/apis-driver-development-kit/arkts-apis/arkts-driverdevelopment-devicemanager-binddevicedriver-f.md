# bindDeviceDriver

## Modules to Import

```TypeScript
import { deviceManager } from 'kits/@kit.DriverDevelopmentKit';
```

## bindDeviceDriver

```TypeScript
function bindDeviceDriver(deviceId: number, onDisconnect: AsyncCallback<number>,
    callback: AsyncCallback<RemoteDeviceDriver>): void
```

Binds a peripheral device based on the device information returned by **queryDevices()**. You need to use [deviceManager.queryDevices()](arkts-driverdevelopment-devicemanager-querydevices-f.md) to obtain the peripheral device information and device.

**Since:** 11

**Deprecated since:** 19

**Substitutes:** [bindDriverWithDeviceId](arkts-driverdevelopment-devicemanager-binddriverwithdeviceid-f.md)(deviceId: long, onDisconnect: AsyncCallback&lt;long&gt;)

**Required permissions:** ohos.permission.ACCESS_EXTENSIONAL_DEVICE_DRIVER

**System capability:** SystemCapability.Driver.ExternalDevice

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| deviceId | number | Yes |
| onDisconnect | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;number&gt; | Yes |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[RemoteDeviceDriver](arkts-driverdevelopment-devicemanager-remotedevicedriver-i.md)&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [22900001](../errorcode-deviceManager.md#22900001-externaldevicemanager-service-exception-or-bustype-parameter-error) |


## bindDeviceDriver

```TypeScript
function bindDeviceDriver(deviceId: number, onDisconnect: AsyncCallback<number>): Promise<RemoteDeviceDriver>
```

Binds a peripheral device based on the device information returned by **queryDevices()**. This API uses a promise to return the result. You need to use [deviceManager.queryDevices](arkts-driverdevelopment-devicemanager-querydevices-f.md) to obtain the peripheral device information and device.

**Since:** 11

**Deprecated since:** 19

**Substitutes:** [bindDriverWithDeviceId](arkts-driverdevelopment-devicemanager-binddriverwithdeviceid-f.md)(deviceId: long, onDisconnect: AsyncCallback&lt;long&gt;)

**Required permissions:** ohos.permission.ACCESS_EXTENSIONAL_DEVICE_DRIVER

**System capability:** SystemCapability.Driver.ExternalDevice

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| deviceId | number | Yes |
| onDisconnect | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;number&gt; | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[RemoteDeviceDriver](arkts-driverdevelopment-devicemanager-remotedevicedriver-i.md)&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [22900001](../errorcode-deviceManager.md#22900001-externaldevicemanager-service-exception-or-bustype-parameter-error) |
