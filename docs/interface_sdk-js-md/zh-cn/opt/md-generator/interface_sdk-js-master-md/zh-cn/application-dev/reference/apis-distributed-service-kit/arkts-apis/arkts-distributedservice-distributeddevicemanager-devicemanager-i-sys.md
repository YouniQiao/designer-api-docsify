# DeviceManager

设备管理实例，用于获取可信设备和本地设备的相关信息。在调用DeviceManager的方法前，需要先通过createDeviceManager构建一个DeviceManager实例dmInstance。

**起始版本：** 23

**废弃版本：** -1

<!--Device-distributedDeviceManager-interface DeviceManager--><!--Device-distributedDeviceManager-interface DeviceManager-End-->

**系统能力：** SystemCapability.DistributedHardware.DeviceManager

## getDeviceIconInfo

```TypeScript
getDeviceIconInfo(filterOptions: DeviceIconInfoFilterOptions): Promise<DeviceIconInfo>
```

获取设备图标，使用Promise异步回调。

**起始版本：** 23

**废弃版本：** -1

**需要权限：** ohos.permission.ACCESS_SERVICE_DM

<!--Device-DeviceManager-getDeviceIconInfo(filterOptions: DeviceIconInfoFilterOptions): Promise<DeviceIconInfo>--><!--Device-DeviceManager-getDeviceIconInfo(filterOptions: DeviceIconInfoFilterOptions): Promise<DeviceIconInfo>-End-->

**系统能力：** SystemCapability.DistributedHardware.DeviceManager

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [filterOptions](../../apis-audio-kit/arkts-apis/arkts-audio-audio-audioplaybackcaptureconfig-i.md) | [DeviceIconInfoFilterOptions](arkts-distributedservice-distributeddevicemanager-deviceiconinfofilteroptions-i-sys.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;[DeviceIconInfo](arkts-distributedservice-distributeddevicemanager-deviceiconinfo-i-sys.md)&gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [11600102](../../apis-distributedservice-kit/errorcode-device-manager.md#11600102-获取服务失败) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [11600106](../../apis-distributedservice-kit/errorcode-device-manager.md#11600106-从云端获取数据失败) |

## 示例

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

**起始版本：** 23

**废弃版本：** -1

**需要权限：** ohos.permission.ACCESS_SERVICE_DM

<!--Device-DeviceManager-getDeviceNetworkIdList(filterOptions: NetworkIdQueryFilter): Promise<Array<string>>--><!--Device-DeviceManager-getDeviceNetworkIdList(filterOptions: NetworkIdQueryFilter): Promise<Array<string>>-End-->

**系统能力：** SystemCapability.DistributedHardware.DeviceManager

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [filterOptions](../../apis-audio-kit/arkts-apis/arkts-audio-audio-audioplaybackcaptureconfig-i.md) | [NetworkIdQueryFilter](arkts-distributedservice-distributeddevicemanager-networkidqueryfilter-i-sys.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;Array & lt;string & gt; & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [11600102](../../apis-distributedservice-kit/errorcode-device-manager.md#11600102-获取服务失败) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [11600107](../../apis-distributedservice-kit/errorcode-device-manager.md#11600107-需要登录账号) |

## 示例

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

**起始版本：** 23

**废弃版本：** -1

**需要权限：** ohos.permission.ACCESS_SERVICE_DM

<!--Device-DeviceManager-getDeviceProfileInfoList(filterOptions: DeviceProfileInfoFilterOptions): Promise<Array<DeviceProfileInfo>>--><!--Device-DeviceManager-getDeviceProfileInfoList(filterOptions: DeviceProfileInfoFilterOptions): Promise<Array<DeviceProfileInfo>>-End-->

**系统能力：** SystemCapability.DistributedHardware.DeviceManager

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [filterOptions](../../apis-audio-kit/arkts-apis/arkts-audio-audio-audioplaybackcaptureconfig-i.md) | [DeviceProfileInfoFilterOptions](arkts-distributedservice-distributeddevicemanager-deviceprofileinfofilteroptions-i-sys.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;Array&lt;[DeviceProfileInfo](arkts-distributedservice-distributeddevicemanager-deviceprofileinfo-i-sys.md)&gt;&gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [11600102](../../apis-distributedservice-kit/errorcode-device-manager.md#11600102-获取服务失败) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [11600107](../../apis-distributedservice-kit/errorcode-device-manager.md#11600107-需要登录账号) |
| [11600106](../../apis-distributedservice-kit/errorcode-device-manager.md#11600106-从云端获取数据失败) |

## 示例

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

**起始版本：** 24

**废弃版本：** -1

**需要权限：** ohos.permission.DISTRIBUTED_DATASYNC and ohos.permission.ACCESS_SERVICE_DM and ohos.permission.sec.ACCESS_UDID

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-DeviceManager-getIdentificationByDeviceIds(deviceIds: Array<string>): Array<DeviceIdentification>--><!--Device-DeviceManager-getIdentificationByDeviceIds(deviceIds: Array<string>): Array<DeviceIdentification>-End-->

**系统能力：** SystemCapability.DistributedHardware.DeviceManager

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| deviceIds | Array & lt;string & gt; | 是 |

**返回值：**

| 类型 |
| --- |
| Array&lt;[DeviceIdentification](arkts-distributedservice-distributeddevicemanager-deviceidentification-i-sys.md)&gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [11600101](../../apis-distributedservice-kit/errorcode-device-manager.md#11600101-服务调用异常) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

## 示例

```TypeScript
let idsLists: undefined|Array<distributedDeviceManager.DeviceIdentification> = [];
let deviceIds: Array<string> = [];
try {
  let deviceManager = distributedDeviceManager.createDeviceManager('com.example.myapplication');
  idsLists = deviceManager?.getIdentificationByDeviceIds(deviceIds);
  console.info("Successfully retrieved UDID list");
} catch (error) {
  console.error('Get device UDID failed:', error);
  idsLists = [];
}
```

## getLocalDisplayDeviceName

```TypeScript
getLocalDisplayDeviceName(maxNameLength: number): Promise<string>
```

获取本机指定长度（字节数）的显示名，使用Promise异步回调。

**起始版本：** 23

**废弃版本：** -1

**需要权限：** ohos.permission.ACCESS_SERVICE_DM

<!--Device-DeviceManager-getLocalDisplayDeviceName(maxNameLength: int): Promise<string>--><!--Device-DeviceManager-getLocalDisplayDeviceName(maxNameLength: int): Promise<string>-End-->

**系统能力：** SystemCapability.DistributedHardware.DeviceManager

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| maxNameLength | number | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;string & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [11600102](../../apis-distributedservice-kit/errorcode-device-manager.md#11600102-获取服务失败) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

## 示例

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

通过设备网络ID查询设备操作系统类型。

**起始版本：** 26.1.0

**废弃版本：** -1

**需要权限：** ohos.permission.DISTRIBUTED_DATASYNC and ohos.permission.ACCESS_SERVICE_DM

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-DeviceManager-getOsTypeByNetworkId(networkId: string): int--><!--Device-DeviceManager-getOsTypeByNetworkId(networkId: string): int-End-->

**系统能力：** SystemCapability.DistributedHardware.DeviceManager

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| networkId | string | 是 |

**返回值：**

| 类型 |
| --- |
| number |

**错误码：**

| 错误码ID |
| --- |
| [11600102](../../apis-distributedservice-kit/errorcode-device-manager.md#11600102-获取服务失败) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| 11600110 |

## offReplyResult

```TypeScript
offReplyResult(callback?: Callback<ReplyResult>): void
```

取消回复UI操作结果回调。使用callback异步回调。

**起始版本：** 23

**废弃版本：** -1

**需要权限：** ohos.permission.ACCESS_SERVICE_DM

<!--Device-DeviceManager-offReplyResult(callback?: Callback<ReplyResult>): void--><!--Device-DeviceManager-offReplyResult(callback?: Callback<ReplyResult>): void-End-->

**系统能力：** SystemCapability.DistributedHardware.DeviceManager

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[ReplyResult](arkts-distributedservice-distributeddevicemanager-replyresult-i-sys.md)&gt; | 否 |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

## off_replyResult

```TypeScript
off(type: 'replyResult', callback?: Callback<{ param: string; }>): void
```

取消回复UI操作结果回调。使用callback异步回调。

**起始版本：** 10

**废弃版本：** -1

**需要权限：** ohos.permission.ACCESS_SERVICE_DM

<!--Device-DeviceManager-off(type: 'replyResult', callback?: Callback<{ param: string; }>): void--><!--Device-DeviceManager-off(type: 'replyResult', callback?: Callback<{ param: string; }>): void-End-->

**系统能力：** SystemCapability.DistributedHardware.DeviceManager

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'replyResult' | 是 |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;{ param: string; }&gt; | 否 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

## 示例

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

## onReplyResult

```TypeScript
onReplyResult(callback: Callback<ReplyResult>): void
```

回复UI操作结果回调。使用callback异步回调。

**起始版本：** 23

**废弃版本：** -1

**需要权限：** ohos.permission.ACCESS_SERVICE_DM

<!--Device-DeviceManager-onReplyResult(callback: Callback<ReplyResult>): void--><!--Device-DeviceManager-onReplyResult(callback: Callback<ReplyResult>): void-End-->

**系统能力：** SystemCapability.DistributedHardware.DeviceManager

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[ReplyResult](arkts-distributedservice-distributeddevicemanager-replyresult-i-sys.md)&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

## on_replyResult

```TypeScript
on(type: 'replyResult', callback: Callback<{ param: string; }>): void
```

回复UI操作结果回调。使用callback异步回调。

**起始版本：** 10

**废弃版本：** -1

**需要权限：** ohos.permission.ACCESS_SERVICE_DM

<!--Device-DeviceManager-on(type: 'replyResult', callback: Callback<{ param: string; }>): void--><!--Device-DeviceManager-on(type: 'replyResult', callback: Callback<{ param: string; }>): void-End-->

**系统能力：** SystemCapability.DistributedHardware.DeviceManager

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'replyResult' | 是 |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;{ param: string; }&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

## 示例

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

业务调用更新设备列表，使用Promise异步回调。

**起始版本：** 23

**废弃版本：** -1

**需要权限：** ohos.permission.ACCESS_SERVICE_DM

<!--Device-DeviceManager-putDeviceProfileInfoList(deviceProfileInfoList: Array<DeviceProfileInfo>): Promise<int>--><!--Device-DeviceManager-putDeviceProfileInfoList(deviceProfileInfoList: Array<DeviceProfileInfo>): Promise<int>-End-->

**系统能力：** SystemCapability.DistributedHardware.DeviceManager

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| deviceProfileInfoList | Array&lt;[DeviceProfileInfo](arkts-distributedservice-distributeddevicemanager-deviceprofileinfo-i-sys.md)&gt; | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;number & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [11600102](../../apis-distributedservice-kit/errorcode-device-manager.md#11600102-获取服务失败) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

## 示例

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

回复用户UI操作行为。此接口只能被devicemanager的PIN码hap使用。

**起始版本：** 23

**废弃版本：** -1

**需要权限：** ohos.permission.ACCESS_SERVICE_DM

<!--Device-DeviceManager-replyUiAction(action: int, actionResult: string): void--><!--Device-DeviceManager-replyUiAction(action: int, actionResult: string): void-End-->

**系统能力：** SystemCapability.DistributedHardware.DeviceManager

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| action | number | 是 |
| actionResult | string | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

## 示例

```TypeScript
import { distributedDeviceManager } from '@kit.DistributedServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  /**
   * action = 0 - 允许授权
   * action = 1 - 取消授权
   * action = 2 - 授权框用户操作超时
   * action = 3 - 取消pin码框展示
   * action = 4 - 取消pin码输入框展示
   * action = 5 - pin码输入框确定操作
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

**起始版本：** 23

**废弃版本：** 24

**替代接口：** [restoreLocalDeviceName](#restoreLocalDeviceName)

**需要权限：** ohos.permission.ACCESS_SERVICE_DM

<!--Device-DeviceManager-restoreLocalDeivceName(): void--><!--Device-DeviceManager-restoreLocalDeivceName(): void-End-->

**系统能力：** SystemCapability.DistributedHardware.DeviceManager

**系统接口：** 此接口为系统接口。

**错误码：**

| 错误码ID |
| --- |
| [11600102](../../apis-distributedservice-kit/errorcode-device-manager.md#11600102-获取服务失败) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

## 示例

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

**起始版本：** 24

**废弃版本：** -1

**需要权限：** ohos.permission.ACCESS_SERVICE_DM

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-DeviceManager-restoreLocalDeviceName(): void--><!--Device-DeviceManager-restoreLocalDeviceName(): void-End-->

**系统能力：** SystemCapability.DistributedHardware.DeviceManager

**系统接口：** 此接口为系统接口。

**错误码：**

| 错误码ID |
| --- |
| [11600102](../../apis-distributedservice-kit/errorcode-device-manager.md#11600102-获取服务失败) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

## 示例

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

设置心跳广播策略。

**起始版本：** 23

**废弃版本：** -1

**需要权限：** ohos.permission.ACCESS_SERVICE_DM

<!--Device-DeviceManager-setHeartbeatPolicy(policy: StrategyForHeartbeat, delayTime: int): void--><!--Device-DeviceManager-setHeartbeatPolicy(policy: StrategyForHeartbeat, delayTime: int): void-End-->

**系统能力：** SystemCapability.DistributedHardware.DeviceManager

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| policy | [StrategyForHeartbeat](arkts-distributedservice-distributeddevicemanager-strategyforheartbeat-e-sys.md) | 是 |
| delayTime | number | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [11600102](../../apis-distributedservice-kit/errorcode-device-manager.md#11600102-获取服务失败) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

## 示例

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

修改本机设备名称，使用Promise异步回调。

**起始版本：** 23

**废弃版本：** -1

**需要权限：** ohos.permission.ACCESS_SERVICE_DM

<!--Device-DeviceManager-setLocalDeviceName(deviceName: string): Promise<int>--><!--Device-DeviceManager-setLocalDeviceName(deviceName: string): Promise<int>-End-->

**系统能力：** SystemCapability.DistributedHardware.DeviceManager

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| deviceName | string | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;number & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [11600102](../../apis-distributedservice-kit/errorcode-device-manager.md#11600102-获取服务失败) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [11600107](../../apis-distributedservice-kit/errorcode-device-manager.md#11600107-需要登录账号) |
| [11600106](../../apis-distributedservice-kit/errorcode-device-manager.md#11600106-从云端获取数据失败) |
| [11600108](../../apis-distributedservice-kit/errorcode-device-manager.md#11600108-设备名称含非法信息) |

## 示例

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

设置配件设备名称，使用Promise异步回调。

**起始版本：** 23

**废弃版本：** -1

**需要权限：** ohos.permission.ACCESS_SERVICE_DM

<!--Device-DeviceManager-setRemoteDeviceName(deviceId: string, deviceName: string): Promise<int>--><!--Device-DeviceManager-setRemoteDeviceName(deviceId: string, deviceName: string): Promise<int>-End-->

**系统能力：** SystemCapability.DistributedHardware.DeviceManager

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| deviceId | string | 是 |
| deviceName | string | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;number & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [11600102](../../apis-distributedservice-kit/errorcode-device-manager.md#11600102-获取服务失败) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [11600107](../../apis-distributedservice-kit/errorcode-device-manager.md#11600107-需要登录账号) |
| [11600106](../../apis-distributedservice-kit/errorcode-device-manager.md#11600106-从云端获取数据失败) |
| [11600108](../../apis-distributedservice-kit/errorcode-device-manager.md#11600108-设备名称含非法信息) |

## 示例

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
