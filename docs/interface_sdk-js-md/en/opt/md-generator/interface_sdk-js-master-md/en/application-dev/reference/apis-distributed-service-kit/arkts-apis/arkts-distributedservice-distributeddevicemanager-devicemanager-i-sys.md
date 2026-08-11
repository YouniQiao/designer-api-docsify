# DeviceManager

Provides APIs to obtain information about trusted devices and local devices. Before calling any API in  
**DeviceManager**, you must use **createDeviceManager** to create a **DeviceManager** instance, for example,  
**dmInstance**.

**Since:** 10

<!--Device-distributedDeviceManager-interface DeviceManager--><!--Device-distributedDeviceManager-interface DeviceManager-End-->

**System capability:** SystemCapability.DistributedHardware.DeviceManager

## Modules to Import

```TypeScript
import { distributedDeviceManager } from 'kits/@kit.DistributedServiceKit';
```

## getDeviceIconInfo

```TypeScript
getDeviceIconInfo(filterOptions: DeviceIconInfoFilterOptions): Promise<DeviceIconInfo>
```

Obtains the device icon. This API uses a promise to return the result.

**Since:** 18

**Required permissions:** ohos.permission.ACCESS_SERVICE_DM

<!--Device-DeviceManager-getDeviceIconInfo(filterOptions: DeviceIconInfoFilterOptions): Promise<DeviceIconInfo>--><!--Device-DeviceManager-getDeviceIconInfo(filterOptions: DeviceIconInfoFilterOptions): Promise<DeviceIconInfo>-End-->

**System capability:** SystemCapability.DistributedHardware.DeviceManager

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| filterOptions | [DeviceIconInfoFilterOptions](arkts-distributedservice-distributeddevicemanager-deviceiconinfofilteroptions-i-sys.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;DeviceIconInfo&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [11600102](../../apis-distributedservice-kit/errorcode-device-manager.md#11600102-failed-to-obtain-the-service) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [11600106](../../apis-distributedservice-kit/errorcode-device-manager.md#11600106-failed-to-obtain-data-from-the-cloud) |

## Examples

```TypeScript
import { distributedDeviceManager } from '@kit.DistributedServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let dmInstance = distributedDeviceManager.createDeviceManager('ohos.samples.jsHelloWorld');
  let productIds:Array<string> = ['M0D2', 'M0D3', 'M0D5', 'M0AB', 'M0BD', 'M0E9', 'M0BC', 'M0EA'];
  let options:distributedDeviceManager.DeviceIconInfoFilterOptions = {
    productId: 'P14U',
    imageType: 'ID',
    specName: 'lg',
  };
  if (productIds.indexOf(options.productId) != -1) {
    options.internalModel = '';
  } else {
    options.subProductId = '';
  }
  dmInstance.getDeviceIconInfo(options).then((data: distributedDeviceManager.DeviceIconInfo) => {
    console.info('getDeviceIconInfo' + JSON.stringify(data));
  }).catch((e : BusinessError) => {
    console.error('getDeviceIconInfo errCode:' + e.code + ',errMessage:' + e.message);
  });
} catch (err) {
  let e: BusinessError = err as BusinessError;
  console.error('getDeviceIconInfo errCode:' + e.code + ',errMessage:' + e.message);
}
```

## getDeviceNetworkIdList

```TypeScript
getDeviceNetworkIdList(filterOptions: NetworkIdQueryFilter): Promise<Array<string>>
```

Obtains the list of network devices according to the specified filter options.

**Since:** 18

**Required permissions:** ohos.permission.ACCESS_SERVICE_DM

<!--Device-DeviceManager-getDeviceNetworkIdList(filterOptions: NetworkIdQueryFilter): Promise<Array<string>>--><!--Device-DeviceManager-getDeviceNetworkIdList(filterOptions: NetworkIdQueryFilter): Promise<Array<string>>-End-->

**System capability:** SystemCapability.DistributedHardware.DeviceManager

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| filterOptions | [NetworkIdQueryFilter](arkts-distributedservice-distributeddevicemanager-networkidqueryfilter-i-sys.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;Array&lt;string&gt;&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [11600102](../../apis-distributedservice-kit/errorcode-device-manager.md#11600102-failed-to-obtain-the-service) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [11600107](../../apis-distributedservice-kit/errorcode-device-manager.md#11600107-login-account-required) |

## Examples

```TypeScript
import { distributedDeviceManager } from '@kit.DistributedServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let queryFiler: distributedDeviceManager.NetworkIdQueryFilter = {
    wiseDeviceId: '',
    onlineStatus: 1,
  }
  let dmInstance = distributedDeviceManager.createDeviceManager('ohos.samples.jsHelloWorld');
  dmInstance.getDeviceNetworkIdList(queryFiler).then((data:Array<string>) => {
    console.info('getDeviceNetworkIdList name:' + JSON.stringify(data));
  }).catch((e: BusinessError) => {
    console.error('getDeviceNetworkIdList errCode:' + e.code + ',errMessage:' + e.message);
  })
} catch (err) {
  let e: BusinessError = err as BusinessError;
  console.error('getDeviceNetworkIdList errCode:' + e.code + ',errMessage:' + e.message);
}
```

## getDeviceProfileInfoList

```TypeScript
getDeviceProfileInfoList(filterOptions: DeviceProfileInfoFilterOptions): Promise<Array<DeviceProfileInfo>>
```

Obtains the list of devices under the same account. This API uses a promise to return the result.

**Since:** 15

**Required permissions:** ohos.permission.ACCESS_SERVICE_DM

<!--Device-DeviceManager-getDeviceProfileInfoList(filterOptions: DeviceProfileInfoFilterOptions): Promise<Array<DeviceProfileInfo>>--><!--Device-DeviceManager-getDeviceProfileInfoList(filterOptions: DeviceProfileInfoFilterOptions): Promise<Array<DeviceProfileInfo>>-End-->

**System capability:** SystemCapability.DistributedHardware.DeviceManager

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| filterOptions | [DeviceProfileInfoFilterOptions](arkts-distributedservice-distributeddevicemanager-deviceprofileinfofilteroptions-i-sys.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;Array&lt;DeviceProfileInfo&gt;&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [11600102](../../apis-distributedservice-kit/errorcode-device-manager.md#11600102-failed-to-obtain-the-service) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [11600107](../../apis-distributedservice-kit/errorcode-device-manager.md#11600107-login-account-required) |
| [11600106](../../apis-distributedservice-kit/errorcode-device-manager.md#11600106-failed-to-obtain-data-from-the-cloud) |

## Examples

```TypeScript
import { distributedDeviceManager } from '@kit.DistributedServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let dmInstance = distributedDeviceManager.createDeviceManager('ohos.samples.jsHelloWorld');
  dmInstance.getDeviceProfileInfoList({"isCloud": false}).then((data: Array<distributedDeviceManager.DeviceProfileInfo>) => {
    console.info('getDeviceProfileInfoList' + JSON.stringify(data));
  }).catch((e: BusinessError) => {
    console.error('getDeviceProfileInfoList errCode:' + e.code + ',errMessage:' + e.message);
  });
} catch (err) {
  let e: BusinessError = err as BusinessError;
  console.error('getDeviceProfileInfoList errCode:' + e.code + ',errMessage:' + e.message);
}
```

## getIdentificationByDeviceIds

```TypeScript
getIdentificationByDeviceIds(deviceIds: Array<string>): Array<DeviceIdentification>
```

Query device identification by device IDs.

**Since:** 24

**Required permissions:** ohos.permission.DISTRIBUTED_DATASYNC and ohos.permission.ACCESS_SERVICE_DM and ohos.permission.sec.ACCESS_UDID

**Model restriction:** This API can be used only in the stage model.

<!--Device-DeviceManager-getIdentificationByDeviceIds(deviceIds: Array<string>): Array<DeviceIdentification>--><!--Device-DeviceManager-getIdentificationByDeviceIds(deviceIds: Array<string>): Array<DeviceIdentification>-End-->

**System capability:** SystemCapability.DistributedHardware.DeviceManager

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| deviceIds | Array&lt;string&gt; | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Array&lt;DeviceIdentification&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [11600101](../../apis-distributedservice-kit/errorcode-device-manager.md#11600101-service-invoking-exception) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## Examples

```TypeScript
import { distributedDeviceManager } from '@kit.DistributedServiceKit'
private idsLists: undefined|Array<distributedDeviceManager.DeviceIdentification> = [];
getDeviceUdids(deviceIds: Array<string>): void {
  let deviceManager: distributedDeviceManager.DeviceManager | null = null;
  try {
    deviceManager = distributedDeviceManager.createDeviceManager('com.example.myapplication');
    this.idsLists = deviceManager?.getIdentificationByDeviceIds(deviceIds);
    console.info("Successfully retrieved UDID list");
  } catch (error) {
    console.error('Get device UDID failed:', error);
    this.idsLists = [];
  } finally {
    if (deviceManager) {
      try {
        distributedDeviceManager.releaseDeviceManager(deviceManager);
        console.info("deviceManager released successfully");
      } catch (releaseError) {
        console.error('Release device manager failed:', releaseError);
      }
    }
  }
}
```

## getLocalDisplayDeviceName

```TypeScript
getLocalDisplayDeviceName(maxNameLength: number): Promise<string>
```

Obtains the local device's display name with the specified length. This API uses a promise to return the result.

**Since:** 18

**Required permissions:** ohos.permission.ACCESS_SERVICE_DM

<!--Device-DeviceManager-getLocalDisplayDeviceName(maxNameLength: int): Promise<string>--><!--Device-DeviceManager-getLocalDisplayDeviceName(maxNameLength: int): Promise<string>-End-->

**System capability:** SystemCapability.DistributedHardware.DeviceManager

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| maxNameLength | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;string&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [11600102](../../apis-distributedservice-kit/errorcode-device-manager.md#11600102-failed-to-obtain-the-service) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## Examples

```TypeScript
import { distributedDeviceManager } from '@kit.DistributedServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let dmInstance = distributedDeviceManager.createDeviceManager('ohos.samples.jsHelloWorld');
  let maxNameLength:number = 21;
  dmInstance.getLocalDisplayDeviceName(maxNameLength).then((data:string)=>{
    console.info('getLocalDisplayDeviceName name:' + JSON.stringify(data));
  }).catch((e: BusinessError)=>{
    console.error('getLocalDisplayDeviceName errCode:' + e.code + ',errMessage:' + e.message);
  });
} catch (err) {
  let e: BusinessError = err as BusinessError;
  console.error('getLocalDisplayDeviceName errCode:' + e.code + ',errMessage:' + e.message);
}
```

## getOsTypeByNetworkId

```TypeScript
getOsTypeByNetworkId(networkId: string): number
```

Query the device operating system type by device network ID.

**Since:** 26.1.0

**Required permissions:** ohos.permission.DISTRIBUTED_DATASYNC and ohos.permission.ACCESS_SERVICE_DM

**Model restriction:** This API can be used only in the stage model.

<!--Device-DeviceManager-getOsTypeByNetworkId(networkId: string): int--><!--Device-DeviceManager-getOsTypeByNetworkId(networkId: string): int-End-->

**System capability:** SystemCapability.DistributedHardware.DeviceManager

**System API:** This is a system API.

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
| [11600102](../../apis-distributedservice-kit/errorcode-device-manager.md#11600102-failed-to-obtain-the-service) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| 11600110 |

## off('replyResult')

```TypeScript
off(type: 'replyResult', callback?: Callback<{ param: string; }>): void
```

Unsubscribes from the reply to the UI operation result.

**Since:** 10

**Required permissions:** ohos.permission.ACCESS_SERVICE_DM

<!--Device-DeviceManager-off(type: 'replyResult', callback?: Callback<{ param: string; }>): void--><!--Device-DeviceManager-off(type: 'replyResult', callback?: Callback<{ param: string; }>): void-End-->

**System capability:** SystemCapability.DistributedHardware.DeviceManager

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'replyResult' | Yes |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;{ param: string; }&gt; | No |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## Examples

```TypeScript
import { distributedDeviceManager } from '@kit.DistributedServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let dmInstance = distributedDeviceManager.createDeviceManager('ohos.samples.jsHelloWorld');
  dmInstance.off('replyResult');
} catch (err) {
  let e: BusinessError = err as BusinessError;
  console.error('replyResult errCode:' + e.code + ',errMessage:' + e.message);
}
```

## on('replyResult')

```TypeScript
on(type: 'replyResult', callback: Callback<{ param: string; }>): void
```

Subscribes to the reply to the UI operation result.

**Since:** 10

**Required permissions:** ohos.permission.ACCESS_SERVICE_DM

<!--Device-DeviceManager-on(type: 'replyResult', callback: Callback<{ param: string; }>): void--><!--Device-DeviceManager-on(type: 'replyResult', callback: Callback<{ param: string; }>): void-End-->

**System capability:** SystemCapability.DistributedHardware.DeviceManager

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'replyResult' | Yes |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;{ param: string; }&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## Examples

```TypeScript
import { distributedDeviceManager } from '@kit.DistributedServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

class Data {
  param: string = '';
}

interface TmpStr {
  verifyFailed: boolean;
}

try {
  let dmInstance = distributedDeviceManager.createDeviceManager('ohos.samples.jsHelloWorld');
  dmInstance.on('replyResult', (data: Data) => {
    console.info('replyResult executed, dialog closed' + JSON.stringify(data));
    let tmpStr: TmpStr = JSON.parse(data.param);
    let isShow = tmpStr.verifyFailed;
    console.info('replyResult executed, dialog closed' + isShow);
  });
} catch (err) {
  let e: BusinessError = err as BusinessError;
  console.error('replyResult errCode:' + e.code + ',errMessage:' + e.message);
}
```

## putDeviceProfileInfoList

```TypeScript
putDeviceProfileInfoList(deviceProfileInfoList: Array<DeviceProfileInfo>): Promise<number>
```

Updates the device list. This API uses a promise to return the result.

**Since:** 18

**Required permissions:** ohos.permission.ACCESS_SERVICE_DM

<!--Device-DeviceManager-putDeviceProfileInfoList(deviceProfileInfoList: Array<DeviceProfileInfo>): Promise<int>--><!--Device-DeviceManager-putDeviceProfileInfoList(deviceProfileInfoList: Array<DeviceProfileInfo>): Promise<int>-End-->

**System capability:** SystemCapability.DistributedHardware.DeviceManager

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| deviceProfileInfoList | Array&lt;DeviceProfileInfo&gt; | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;number&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [11600102](../../apis-distributedservice-kit/errorcode-device-manager.md#11600102-failed-to-obtain-the-service) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## Examples

```TypeScript
import { distributedDeviceManager } from '@kit.DistributedServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let dmInstance = distributedDeviceManager.createDeviceManager('ohos.samples.jsHelloWorld');
  let deviceProfileInfoList:Array<distributedDeviceManager.DeviceProfileInfo> = [];
  dmInstance.putDeviceProfileInfoList(deviceProfileInfoList).then((data:number) => {
    console.info('put device profile info:' + JSON.stringify(data));
  }).catch((e: BusinessError) => {
    console.error('putDeviceProfileInfoList errCode:' + e.code + ',errMessage:' + e.message);
  });
} catch (err) {
  let e: BusinessError = err as BusinessError;
  console.error('putDeviceProfileInfoList errCode:' + e.code + ',errMessage:' + e.message);
}
```

## replyUiAction

```TypeScript
replyUiAction(action: number, actionResult: string): void
```

Replies to the user's UI operation. This API can be used only by the PIN HAP of the **deviceManager**.

**Since:** 10

**Required permissions:** ohos.permission.ACCESS_SERVICE_DM

<!--Device-DeviceManager-replyUiAction(action: int, actionResult: string): void--><!--Device-DeviceManager-replyUiAction(action: int, actionResult: string): void-End-->

**System capability:** SystemCapability.DistributedHardware.DeviceManager

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| action | number | Yes |
| actionResult | string | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## Examples

```TypeScript
import { distributedDeviceManager } from '@kit.DistributedServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  /**
   * action = 0 - Grant the permission.
   * action = 1 - Revoke the permission.
   * action = 2 - Time out the user operation in the permission request dialog.
   * action = 3 - Cancel the display of the PIN box.
   * action = 4 - Cancel the display of the PIN input box.
   * action = 5 - Confirm the input in the PIN input box.
   */
  let operation = 0;
  let dmInstance = distributedDeviceManager.createDeviceManager('ohos.samples.jsHelloWorld');
  dmInstance.replyUiAction(operation, 'extra');
} catch (err) {
  let e: BusinessError = err as BusinessError;
  console.error('replyUiAction errCode:' + e.code + ',errMessage:' + e.message);
}
```

## restoreLocalDeivceName

```TypeScript
restoreLocalDeivceName(): void
```

Restores the local device name by resetting the network settings.

**Since:** 18

**Deprecated since:** 24

**Substitutes:** [distributedDeviceManager.DeviceManager.restoreLocalDeviceName](arkts-distributedservice-distributeddevicemanager-devicemanager-i-sys.md#restorelocaldevicename)

**Required permissions:** ohos.permission.ACCESS_SERVICE_DM

<!--Device-DeviceManager-restoreLocalDeivceName(): void--><!--Device-DeviceManager-restoreLocalDeivceName(): void-End-->

**System capability:** SystemCapability.DistributedHardware.DeviceManager

**System API:** This is a system API.

**Error codes:**

| Error Code ID |
| --- |
| [11600102](../../apis-distributedservice-kit/errorcode-device-manager.md#11600102-failed-to-obtain-the-service) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## Examples

```TypeScript
import { distributedDeviceManager } from '@kit.DistributedServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let dmInstance = distributedDeviceManager.createDeviceManager('ohos.samples.jsHelloWorld');
  dmInstance.restoreLocalDeivceName();
} catch (err) {
  let e: BusinessError = err as BusinessError;
  console.error('restoreLocalDeivceName errCode:' + e.code + ',errMessage:' + e.message);
}
```

## restoreLocalDeviceName

```TypeScript
restoreLocalDeviceName(): void
```

Restores the local device name.

**Since:** 24

**Required permissions:** ohos.permission.ACCESS_SERVICE_DM

**Model restriction:** This API can be used only in the stage model.

<!--Device-DeviceManager-restoreLocalDeviceName(): void--><!--Device-DeviceManager-restoreLocalDeviceName(): void-End-->

**System capability:** SystemCapability.DistributedHardware.DeviceManager

**System API:** This is a system API.

**Error codes:**

| Error Code ID |
| --- |
| [11600102](../../apis-distributedservice-kit/errorcode-device-manager.md#11600102-failed-to-obtain-the-service) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## Examples

```TypeScript
import { distributedDeviceManager } from '@kit.DistributedServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let dmInstance = distributedDeviceManager.createDeviceManager('ohos.samples.jsHelloWorld');
  dmInstance.restoreLocalDeviceName();
} catch (err) {
  let e: BusinessError = err as BusinessError;
  console.error('restoreLocalDeviceName errCode:' + e.code + ',errMessage:' + e.message);
}
```

## setHeartbeatPolicy

```TypeScript
setHeartbeatPolicy(policy: StrategyForHeartbeat, delayTime: number): void
```

Sets the heartbeat broadcast policy.

**Since:** 15

**Required permissions:** ohos.permission.ACCESS_SERVICE_DM

<!--Device-DeviceManager-setHeartbeatPolicy(policy: StrategyForHeartbeat, delayTime: int): void--><!--Device-DeviceManager-setHeartbeatPolicy(policy: StrategyForHeartbeat, delayTime: int): void-End-->

**System capability:** SystemCapability.DistributedHardware.DeviceManager

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| policy | [StrategyForHeartbeat](arkts-distributedservice-distributeddevicemanager-strategyforheartbeat-e-sys.md) | Yes |
| delayTime | number | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [11600102](../../apis-distributedservice-kit/errorcode-device-manager.md#11600102-failed-to-obtain-the-service) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## Examples

```TypeScript
import { distributedDeviceManager } from '@kit.DistributedServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let policy = distributedDeviceManager.StrategyForHeartbeat.TEMP_STOP_HEARTBEAT;
  let delayTime = 1000;
  let dmInstance = distributedDeviceManager.createDeviceManager('ohos.samples.jsHelloWorld');
  dmInstance.setHeartbeatPolicy(policy, delayTime);
} catch (err) {
  let e: BusinessError = err as BusinessError;
  console.error('setHeartbeatPolicy errCode:' + e.code + ',errMessage:' + e.message);
}
```

## setLocalDeviceName

```TypeScript
setLocalDeviceName(deviceName: string): Promise<number>
```

Sets the local device name. This API uses a promise to return the result.

**Since:** 18

**Required permissions:** ohos.permission.ACCESS_SERVICE_DM

<!--Device-DeviceManager-setLocalDeviceName(deviceName: string): Promise<int>--><!--Device-DeviceManager-setLocalDeviceName(deviceName: string): Promise<int>-End-->

**System capability:** SystemCapability.DistributedHardware.DeviceManager

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| deviceName | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;number&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [11600102](../../apis-distributedservice-kit/errorcode-device-manager.md#11600102-failed-to-obtain-the-service) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [11600107](../../apis-distributedservice-kit/errorcode-device-manager.md#11600107-login-account-required) |
| [11600106](../../apis-distributedservice-kit/errorcode-device-manager.md#11600106-failed-to-obtain-data-from-the-cloud) |
| [11600108](../../apis-distributedservice-kit/errorcode-device-manager.md#11600108-unlawful-information-in-device-name) |

## Examples

```TypeScript
import { distributedDeviceManager } from '@kit.DistributedServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let dmInstance = distributedDeviceManager.createDeviceManager('ohos.samples.jsHelloWorld');
  let deviceName:string = 'xxx';
  dmInstance.setLocalDeviceName(deviceName).then((data:number)=>{
    console.info('setLocalDeviceName name:' + JSON.stringify(data));
  }).catch((e: BusinessError)=>{
    console.error('setLocalDeviceName errCode:' + e.code + ',errMessage:' + e.message);
  });
} catch (err) {
  let e: BusinessError = err as BusinessError;
  console.error('setLocalDeviceName errCode:' + e.code + ',errMessage:' + e.message);
}
```

## setRemoteDeviceName

```TypeScript
setRemoteDeviceName(deviceId: string, deviceName: string): Promise<number>
```

Sets the remote device name. This API uses a promise to return the result.

**Since:** 18

**Required permissions:** ohos.permission.ACCESS_SERVICE_DM

<!--Device-DeviceManager-setRemoteDeviceName(deviceId: string, deviceName: string): Promise<int>--><!--Device-DeviceManager-setRemoteDeviceName(deviceId: string, deviceName: string): Promise<int>-End-->

**System capability:** SystemCapability.DistributedHardware.DeviceManager

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| deviceId | string | Yes |
| deviceName | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;number&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [11600102](../../apis-distributedservice-kit/errorcode-device-manager.md#11600102-failed-to-obtain-the-service) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [11600107](../../apis-distributedservice-kit/errorcode-device-manager.md#11600107-login-account-required) |
| [11600106](../../apis-distributedservice-kit/errorcode-device-manager.md#11600106-failed-to-obtain-data-from-the-cloud) |
| [11600108](../../apis-distributedservice-kit/errorcode-device-manager.md#11600108-unlawful-information-in-device-name) |

## Examples

```TypeScript
import { distributedDeviceManager } from '@kit.DistributedServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let dmInstance = distributedDeviceManager.createDeviceManager('ohos.samples.jsHelloWorld');
  let deviceId:string = 'xxx';
  let deviceName:string = 'xxx';
  dmInstance.setRemoteDeviceName(deviceId, deviceName).then((data:number)=>{
    console.info('setRemoteDeviceName name:' + JSON.stringify(data));
  }).catch((e: BusinessError)=>{
    console.error('setRemoteDeviceName errCode:' + e.code + ',errMessage:' + e.message);
  });
} catch (err) {
  let e: BusinessError = err as BusinessError;
  console.error('setRemoteDeviceName errCode:' + e.code + ',errMessage:' + e.message);
}
```
