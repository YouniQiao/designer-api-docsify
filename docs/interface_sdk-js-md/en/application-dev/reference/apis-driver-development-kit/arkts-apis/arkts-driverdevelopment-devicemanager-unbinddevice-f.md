# unbindDevice

## Modules to Import

```TypeScript
import { deviceManager } from 'kits/@kit.DriverDevelopmentKit';
```

## unbindDevice

```TypeScript
function unbindDevice(deviceId: number, callback: AsyncCallback<number>): void
```

Unbinds a peripheral device.

**Since:** 10

**Deprecated since:** 19

**Substitutes:** [unbindDriverWithDeviceId](arkts-driverdevelopment-devicemanager-unbinddriverwithdeviceid-f.md)(deviceId: long)

**Required permissions:** ohos.permission.ACCESS_EXTENSIONAL_DEVICE_DRIVER

**System capability:** SystemCapability.Driver.ExternalDevice

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| deviceId | number | Yes |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;number&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [22900001](../errorcode-deviceManager.md#22900001-externaldevicemanager-service-exception-or-bustype-parameter-error) |


## unbindDevice

```TypeScript
function unbindDevice(deviceId: number): Promise<number>
```

Unbinds a peripheral device. This API uses a promise to return the result.

**Since:** 10

**Deprecated since:** 19

**Substitutes:** [unbindDriverWithDeviceId](arkts-driverdevelopment-devicemanager-unbinddriverwithdeviceid-f.md)(deviceId: long)

**Required permissions:** ohos.permission.ACCESS_EXTENSIONAL_DEVICE_DRIVER

**System capability:** SystemCapability.Driver.ExternalDevice

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| deviceId | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;number & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [22900001](../errorcode-deviceManager.md#22900001-externaldevicemanager-service-exception-or-bustype-parameter-error) |
