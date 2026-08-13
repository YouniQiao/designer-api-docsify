# createDeviceManager (System API)

## Modules to Import

```TypeScript
import { deviceManager } from '@kit.DistributedServiceKit';
```

## createDeviceManager

```TypeScript
function createDeviceManager(bundleName: string, callback: AsyncCallback<DeviceManager>): void
```

Creates a **DeviceManager** instance.

**Since:** 7

**Deprecated since:** 11

**Substitutes:** [createDeviceManager](arkts-distributedservice-distributeddevicemanager-createdevicemanager-f.md#createDeviceManager)

<!--Device-deviceManager-function createDeviceManager(bundleName: string, callback: AsyncCallback<DeviceManager>): void--><!--Device-deviceManager-function createDeviceManager(bundleName: string, callback: AsyncCallback<DeviceManager>): void-End-->

**System capability:** SystemCapability.DistributedHardware.DeviceManager

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| bundleName | string | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;DeviceManager&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## Examples

```TypeScript
import deviceManager from '@ohos.distributedHardware.deviceManager';
import { BusinessError } from '@ohos.base';

let dmInstance: deviceManager.DeviceManager | null = null;
try {
  deviceManager.createDeviceManager("ohos.samples.jshelloworld", (err: BusinessError, data: deviceManager.DeviceManager) => {
    if (err) { 
      console.error("createDeviceManager errCode:" + err.code + ",errMessage:" + err.message);
      return;
    }
    console.info("createDeviceManager success");
    dmInstance = data;
  });
} catch(err) {
  let e: BusinessError = err as BusinessError;
  console.error("createDeviceManager errCode:" + e.code + ",errMessage:" + e.message);
}
```
