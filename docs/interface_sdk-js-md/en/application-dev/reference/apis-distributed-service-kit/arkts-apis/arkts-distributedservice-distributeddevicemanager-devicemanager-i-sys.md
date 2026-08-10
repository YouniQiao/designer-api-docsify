# DeviceManager

设备管理实例，用于获取可信设备和本地设备的相关信息。在调用DeviceManager的方法前，需要先通过createDeviceManager构建一个DeviceManager实例dmInstance。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

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

获取设备图标，使用Promise异步回调。

**Since:** 18

**ArkTS mode:** ArkTS-Dyn since version 18; ArkTS-Sta since version 23.

**Required permissions:** ohos.permission.ACCESS_SERVICE_DM

<!--Device-DeviceManager-getDeviceIconInfo(filterOptions: DeviceIconInfoFilterOptions): Promise<DeviceIconInfo>--><!--Device-DeviceManager-getDeviceIconInfo(filterOptions: DeviceIconInfoFilterOptions): Promise<DeviceIconInfo>-End-->

**System capability:** SystemCapability.DistributedHardware.DeviceManager

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| filterOptions | [DeviceIconInfoFilterOptions](arkts-distributedservice-distributeddevicemanager-deviceiconinfofilteroptions-i-sys.md) | Yes | 查询过程中使用的过滤条件。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;DeviceIconInfo&gt; | Promise实例，返回设备图标信息。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter type; 3. Parameter verification failed; |
| 11600102 | Failed to obtain service. |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 202 | Permission verification failed. A non-system application calls a system API. |
| 11600106 | Get data from cloud fail. |

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

获取符合条件的网络设备ID列表。使用Promise异步回调。

**Since:** 18

**ArkTS mode:** ArkTS-Dyn since version 18; ArkTS-Sta since version 23.

**Required permissions:** ohos.permission.ACCESS_SERVICE_DM

<!--Device-DeviceManager-getDeviceNetworkIdList(filterOptions: NetworkIdQueryFilter): Promise<Array<string>>--><!--Device-DeviceManager-getDeviceNetworkIdList(filterOptions: NetworkIdQueryFilter): Promise<Array<string>>-End-->

**System capability:** SystemCapability.DistributedHardware.DeviceManager

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| filterOptions | [NetworkIdQueryFilter](arkts-distributedservice-distributeddevicemanager-networkidqueryfilter-i-sys.md) | Yes | 查询过程中使用的过滤条件。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;Array&lt;string&gt;&gt; | Promise实例，返回设备网络ID的列表。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Parameter verification failed; |
| 11600102 | Failed to obtain service. |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 202 | Permission verification failed. A non-system application calls a system API. |
| 11600107 | A login account is required. |

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

获取同账号下全部的设备列表，使用Promise异步回调。

**Since:** 15

**ArkTS mode:** ArkTS-Dyn since version 15; ArkTS-Sta since version 23.

**Required permissions:** ohos.permission.ACCESS_SERVICE_DM

<!--Device-DeviceManager-getDeviceProfileInfoList(filterOptions: DeviceProfileInfoFilterOptions): Promise<Array<DeviceProfileInfo>>--><!--Device-DeviceManager-getDeviceProfileInfoList(filterOptions: DeviceProfileInfoFilterOptions): Promise<Array<DeviceProfileInfo>>-End-->

**System capability:** SystemCapability.DistributedHardware.DeviceManager

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| filterOptions | [DeviceProfileInfoFilterOptions](arkts-distributedservice-distributeddevicemanager-deviceprofileinfofilteroptions-i-sys.md) | Yes | 查询过程中使用的过滤条件。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;Array&lt;DeviceProfileInfo&gt;&gt; | Promise实例，返回设备列表。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter type; 3. Parameter verification failed; 4. The size of specified type is greater than 500. |
| 11600102 | Failed to obtain service. |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 202 | Permission verification failed. A non-system application calls a system API. |
| 11600107 | A login account is required. |
| 11600106 | Get data from cloud fail. |

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

根据设备ID查询设备标识。

**Since:** 24

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 24.

**Required permissions:** ohos.permission.DISTRIBUTED_DATASYNC and ohos.permission.ACCESS_SERVICE_DM and ohos.permission.sec.ACCESS_UDID

**Model restriction:** This API can be used only in the stage model.

<!--Device-DeviceManager-getIdentificationByDeviceIds(deviceIds: Array<string>): Array<DeviceIdentification>--><!--Device-DeviceManager-getIdentificationByDeviceIds(deviceIds: Array<string>): Array<DeviceIdentification>-End-->

**System capability:** SystemCapability.DistributedHardware.DeviceManager

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| deviceIds | Array&lt;string&gt; | Yes | 应用程序可以获取的设备ID列表。 |

**Return value:**

| Type | Description |
| --- | --- |
| Array&lt;DeviceIdentification&gt; | DeviceIdentification列表。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 11600101 | Failed to execute the function. |
| 201 | User permission verify failed. |
| 202 | The caller is not a system application. |

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

ArkTS-Dyn:
```TypeScript
getLocalDisplayDeviceName(maxNameLength: number): Promise<string>
```

ArkTS-Sta:
```TypeScript
getLocalDisplayDeviceName(maxNameLength: int): Promise<string>
```

获取本机指定长度（字节数）的显示名，使用Promise异步回调。

**Since:** 18

**ArkTS mode:** ArkTS-Dyn since version 18; ArkTS-Sta since version 23.

**Required permissions:** ohos.permission.ACCESS_SERVICE_DM

<!--Device-DeviceManager-getLocalDisplayDeviceName(maxNameLength: int): Promise<string>--><!--Device-DeviceManager-getLocalDisplayDeviceName(maxNameLength: int): Promise<string>-End-->

**System capability:** SystemCapability.DistributedHardware.DeviceManager

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| maxNameLength | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | 可显示的设备名称长度（字节数），取值范围为[18，100]，为0时表示不限制。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;string&gt; | 指定名称长度最大字节数的本机设备显示名。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter type; 3. Parameter verification failed; |
| 11600102 | Failed to obtain service. |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 202 | Permission verification failed. A non-system application calls a system API. |

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

ArkTS-Dyn:
```TypeScript
getOsTypeByNetworkId(networkId: string): number
```

ArkTS-Sta:
```TypeScript
getOsTypeByNetworkId(networkId: string): int
```

通过设备网络ID查询设备操作系统类型。

**Since:** 26.1.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.1.0.

**Required permissions:** ohos.permission.DISTRIBUTED_DATASYNC and ohos.permission.ACCESS_SERVICE_DM

**Model restriction:** This API can be used only in the stage model.

<!--Device-DeviceManager-getOsTypeByNetworkId(networkId: string): int--><!--Device-DeviceManager-getOsTypeByNetworkId(networkId: string): int-End-->

**System capability:** SystemCapability.DistributedHardware.DeviceManager

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| networkId | string | Yes | The device's network ID |

**Return value:**

| Type | Description |
| --- | --- |
| ArkTS-Dyn: number  <br>ArkTS-Sta：int | Returns the device operating system type. Possible return: 1. 10: Operating system based on OpenHarmony 2. 11: Operating system not based on OpenHarmony 3. -1: Unknown |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 11600102 | Failed to obtain service. |
| 201 | User permission verify failed. |
| 202 | The caller is not a system application. |
| 11600110 | Invalid network ID. |

## off('replyResult')

```TypeScript
off(type: 'replyResult', callback?: Callback<{ param: string; }>): void
```

取消回复UI操作结果回调。使用callback异步回调。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Required permissions:** ohos.permission.ACCESS_SERVICE_DM

<!--Device-DeviceManager-off(type: 'replyResult', callback?: Callback<{ param: string; }>): void--><!--Device-DeviceManager-off(type: 'replyResult', callback?: Callback<{ param: string; }>): void-End-->

**System capability:** SystemCapability.DistributedHardware.DeviceManager

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'replyResult' | Yes | 取消注册的设备管理器 UI 状态回调，固定为replyResult。 |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;{ param: string; }&gt; | No |  |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter type; 3. Parameter verification failed; 4. The size of specified type is greater than 255. |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 202 | Permission verification failed. A non-system application calls a system API. |

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

## offReplyResult

```TypeScript
offReplyResult(callback?: Callback<ReplyResult>): void
```

取消回复UI操作结果回调。使用callback异步回调。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Required permissions:** ohos.permission.ACCESS_SERVICE_DM

<!--Device-DeviceManager-offReplyResult(callback?: Callback<ReplyResult>): void--><!--Device-DeviceManager-offReplyResult(callback?: Callback<ReplyResult>): void-End-->

**System capability:** SystemCapability.DistributedHardware.DeviceManager

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;ReplyResult&gt; | No | 指示要取消注册的设备管理器 UI 状态，返回UI状态。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 202 | Permission verification failed. A non-system application calls a system API. |

## on('replyResult')

```TypeScript
on(type: 'replyResult', callback: Callback<{ param: string; }>): void
```

回复UI操作结果回调。使用callback异步回调。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Required permissions:** ohos.permission.ACCESS_SERVICE_DM

<!--Device-DeviceManager-on(type: 'replyResult', callback: Callback<{ param: string; }>): void--><!--Device-DeviceManager-on(type: 'replyResult', callback: Callback<{ param: string; }>): void-End-->

**System capability:** SystemCapability.DistributedHardware.DeviceManager

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'replyResult' | Yes | 注册的设备管理器 UI 状态回调，以便在状态改变时通知应用，固定为replyResult。 |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;{ param: string; }&gt; | Yes |  |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter type; 3. Parameter verification failed; 4. The size of specified type is greater than 255. |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 202 | Permission verification failed. A non-system application calls a system API. |

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

## onReplyResult

```TypeScript
onReplyResult(callback: Callback<ReplyResult>): void
```

回复UI操作结果回调。使用callback异步回调。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Required permissions:** ohos.permission.ACCESS_SERVICE_DM

<!--Device-DeviceManager-onReplyResult(callback: Callback<ReplyResult>): void--><!--Device-DeviceManager-onReplyResult(callback: Callback<ReplyResult>): void-End-->

**System capability:** SystemCapability.DistributedHardware.DeviceManager

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;ReplyResult&gt; | Yes | 指示要注册的设备管理器 UI 状态回调，返回UI状态。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 202 | Permission verification failed. A non-system application calls a system API. |

## putDeviceProfileInfoList

ArkTS-Dyn:
```TypeScript
putDeviceProfileInfoList(deviceProfileInfoList: Array<DeviceProfileInfo>): Promise<number>
```

ArkTS-Sta:
```TypeScript
putDeviceProfileInfoList(deviceProfileInfoList: Array<DeviceProfileInfo>): Promise<int>
```

业务调用更新设备列表，使用Promise异步回调。

**Since:** 18

**ArkTS mode:** ArkTS-Dyn since version 18; ArkTS-Sta since version 23.

**Required permissions:** ohos.permission.ACCESS_SERVICE_DM

<!--Device-DeviceManager-putDeviceProfileInfoList(deviceProfileInfoList: Array<DeviceProfileInfo>): Promise<int>--><!--Device-DeviceManager-putDeviceProfileInfoList(deviceProfileInfoList: Array<DeviceProfileInfo>): Promise<int>-End-->

**System capability:** SystemCapability.DistributedHardware.DeviceManager

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| deviceProfileInfoList | Array&lt;DeviceProfileInfo&gt; | Yes | 需要更新的设备列表。 |

**Return value:**

| Type | Description |
| --- | --- |
| ArkTS-Dyn: Promise&lt;number&gt;  <br>ArkTS-Sta：Promise&lt;int&gt; | 操作结果，0表示本次调用成功。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter type; 3. Parameter verification failed; 4. The size of specified type is greater than 500. |
| 11600102 | Failed to obtain service. |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 202 | Permission verification failed. A non-system application calls a system API. |

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

ArkTS-Dyn:
```TypeScript
replyUiAction(action: number, actionResult: string): void
```

ArkTS-Sta:
```TypeScript
replyUiAction(action: int, actionResult: string): void
```

回复用户UI操作行为。此接口只能被devicemanager的PIN码hap使用。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

**Required permissions:** ohos.permission.ACCESS_SERVICE_DM

<!--Device-DeviceManager-replyUiAction(action: int, actionResult: string): void--><!--Device-DeviceManager-replyUiAction(action: int, actionResult: string): void-End-->

**System capability:** SystemCapability.DistributedHardware.DeviceManager

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| action | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | 用户操作动作。 &lt;br /&gt;- 0：允许授权。 &lt;br /&gt;- 1：取消授权。 &lt;br /&gt;- 2：授权框用户操作超时。 &lt;br /&gt;- 3：取消pin码框展示。 &lt;br /&gt;- 4：取消pin码输入框展示。 &lt;br /&gt;- 5：pin码输入框确定操作。 |
| actionResult | string | Yes | 表示用户操作结果，长度范围1~255字符。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter type; 3. Parameter verification failed; 4. The size of specified actionResult is greater than 255. |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 202 | Permission verification failed. A non-system application calls a system API. |

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

系统重置还原网络设置时，还原本机设备名。

**Since:** 18

**ArkTS mode:** ArkTS-Dyn since version 18; ArkTS-Sta since version 23.

**Deprecated since:** 24

**Substitutes:** [distributedDeviceManager.DeviceManager.restoreLocalDeviceName](arkts-distributedservice-distributeddevicemanager-devicemanager-i-sys.md#restorelocaldevicename)

**Required permissions:** ohos.permission.ACCESS_SERVICE_DM

<!--Device-DeviceManager-restoreLocalDeivceName(): void--><!--Device-DeviceManager-restoreLocalDeivceName(): void-End-->

**System capability:** SystemCapability.DistributedHardware.DeviceManager

**System API:** This is a system API.

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 11600102 | Failed to obtain the service. |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 202 | Permission verification failed. A non-system application calls a system API. |

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

系统重置还原网络设置时，还原本机设备名。

**Since:** 24

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 24.

**Required permissions:** ohos.permission.ACCESS_SERVICE_DM

**Model restriction:** This API can be used only in the stage model.

<!--Device-DeviceManager-restoreLocalDeviceName(): void--><!--Device-DeviceManager-restoreLocalDeviceName(): void-End-->

**System capability:** SystemCapability.DistributedHardware.DeviceManager

**System API:** This is a system API.

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 11600102 | Failed to obtain the service. |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 202 | Permission verification failed. A non-system application calls a system API. |

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

ArkTS-Dyn:
```TypeScript
setHeartbeatPolicy(policy: StrategyForHeartbeat, delayTime: number): void
```

ArkTS-Sta:
```TypeScript
setHeartbeatPolicy(policy: StrategyForHeartbeat, delayTime: int): void
```

设置心跳广播策略。

**Since:** 15

**ArkTS mode:** ArkTS-Dyn since version 15; ArkTS-Sta since version 23.

**Required permissions:** ohos.permission.ACCESS_SERVICE_DM

<!--Device-DeviceManager-setHeartbeatPolicy(policy: StrategyForHeartbeat, delayTime: int): void--><!--Device-DeviceManager-setHeartbeatPolicy(policy: StrategyForHeartbeat, delayTime: int): void-End-->

**System capability:** SystemCapability.DistributedHardware.DeviceManager

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| policy | [StrategyForHeartbeat](arkts-distributedservice-distributeddevicemanager-strategyforheartbeat-e-sys.md) | Yes | 心跳广播策略。 |
| delayTime | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | 临时关闭心跳广播的时长，单位为：ms，取值范围1000ms到15000ms。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 11600102 | Failed to obtain service. |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 202 | Permission verification failed. A non-system application calls a system API. |

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

ArkTS-Dyn:
```TypeScript
setLocalDeviceName(deviceName: string): Promise<number>
```

ArkTS-Sta:
```TypeScript
setLocalDeviceName(deviceName: string): Promise<int>
```

修改本机设备名称，使用Promise异步回调。

**Since:** 18

**ArkTS mode:** ArkTS-Dyn since version 18; ArkTS-Sta since version 23.

**Required permissions:** ohos.permission.ACCESS_SERVICE_DM

<!--Device-DeviceManager-setLocalDeviceName(deviceName: string): Promise<int>--><!--Device-DeviceManager-setLocalDeviceName(deviceName: string): Promise<int>-End-->

**System capability:** SystemCapability.DistributedHardware.DeviceManager

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| deviceName | string | Yes | 自定义设备名称。字符串长度范围1~255。 |

**Return value:**

| Type | Description |
| --- | --- |
| ArkTS-Dyn: Promise&lt;number&gt;  <br>ArkTS-Sta：Promise&lt;int&gt; | 操作结果，0表示本次调用成功。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter type; 3. Parameter verification failed; |
| 11600102 | Failed to obtain service. |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 202 | Permission verification failed. A non-system application calls a system API. |
| 11600107 | A login account is required. |
| 11600106 | Failed to get data from the cloud. |
| 11600108 | The device name contains non-compliant content. |

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

ArkTS-Dyn:
```TypeScript
setRemoteDeviceName(deviceId: string, deviceName: string): Promise<number>
```

ArkTS-Sta:
```TypeScript
setRemoteDeviceName(deviceId: string, deviceName: string): Promise<int>
```

设置配件设备名称，使用Promise异步回调。

**Since:** 18

**ArkTS mode:** ArkTS-Dyn since version 18; ArkTS-Sta since version 23.

**Required permissions:** ohos.permission.ACCESS_SERVICE_DM

<!--Device-DeviceManager-setRemoteDeviceName(deviceId: string, deviceName: string): Promise<int>--><!--Device-DeviceManager-setRemoteDeviceName(deviceId: string, deviceName: string): Promise<int>-End-->

**System capability:** SystemCapability.DistributedHardware.DeviceManager

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| deviceId | string | Yes | 配件设备的UDID，没有UDID的设备取MAC或SN，优先取SN。 |
| deviceName | string | Yes | 自定义设备名称。字符串长度范围1~255。 |

**Return value:**

| Type | Description |
| --- | --- |
| ArkTS-Dyn: Promise&lt;number&gt;  <br>ArkTS-Sta：Promise&lt;int&gt; | 操作结果，0表示本次调用成功。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter type; 3. Parameter verification failed; |
| 11600102 | Failed to obtain service. |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 202 | Permission verification failed. A non-system application calls a system API. |
| 11600107 | A login account is required. |
| 11600106 | Failed to get data from the cloud. |
| 11600108 | The device name contains non-compliant content. |

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

