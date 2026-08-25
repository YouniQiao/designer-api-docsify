# DeviceManager

设备管理实例，是分布式设备管理方法的调用入口，提供设备发现、设备认证、状态监听和信息查询等能力。 在调用DeviceManager的方法前，需要先通过createDeviceManager构建一个DeviceManager实例dmInstance。

**起始版本：** 10

**ArkTS模式：** ArkTS-Dyn起始版本为10；ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.DistributedHardware.DeviceManager

## 导入模块

```TypeScript
import { distributedDeviceManager } from '@kit.DistributedServiceKit';
```

## getDeviceIconInfo

```TypeScript
getDeviceIconInfo(filterOptions: DeviceIconInfoFilterOptions): Promise<DeviceIconInfo>
```

获取设备图标，使用Promise异步回调。

**起始版本：** 18

**ArkTS模式：** ArkTS-Dyn起始版本为18；ArkTS-Sta起始版本为23。

**需要权限：** ohos.permission.ACCESS_SERVICE_DM

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
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [11600102](../errorcode-device-manager.md#11600102-获取服务失败) |
| [11600106](../errorcode-device-manager.md#11600106-从云端获取数据失败) |

**示例**

ArkTS-Dyn示例：

```TypeScript
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
  }).catch((err: BusinessError) => {
    let e: BusinessError = err as BusinessError;
    console.error(`getDeviceIconInfo errCode: ${e.code}, errMessage: ${e.message}`);
  });
} catch (err) {
  let e: BusinessError = err as BusinessError;
  console.error(`getDeviceIconInfo errCode: ${e.code}, errMessage: ${e.message}`);
}
```

ArkTS-Sta示例：

```TypeScript
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
  }).catch((err) => {
    let e: BusinessError = err as BusinessError;
    console.error(`getDeviceIconInfo errCode: ${e.code}, errMessage: ${e.message}`);
  });
} catch (err) {
  let e: BusinessError = err as BusinessError;
  console.error(`getDeviceIconInfo errCode: ${e.code}, errMessage: ${e.message}`);
}
```

## getDeviceNetworkIdList

```TypeScript
getDeviceNetworkIdList(filterOptions: NetworkIdQueryFilter): Promise<Array<string>>
```

获取符合条件的网络设备ID列表。使用Promise异步回调。

**起始版本：** 18

**ArkTS模式：** ArkTS-Dyn起始版本为18；ArkTS-Sta起始版本为23。

**需要权限：** ohos.permission.ACCESS_SERVICE_DM

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
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [11600102](../errorcode-device-manager.md#11600102-获取服务失败) |
| [11600107](../errorcode-device-manager.md#11600107-需要登录账号) |

**示例**

ArkTS-Dyn示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let queryFiler: distributedDeviceManager.NetworkIdQueryFilter = {
    wiseDeviceId: '',
    onlineStatus: 1,
  }
  let dmInstance = distributedDeviceManager.createDeviceManager('ohos.samples.jsHelloWorld');
  dmInstance.getDeviceNetworkIdList(queryFiler).then((data:Array<string>) => {
    console.info('getDeviceNetworkIdList name:' + JSON.stringify(data));
  }).catch((err: BusinessError) => {
    let e: BusinessError = err as BusinessError;
    console.error(`getDeviceNetworkIdList errCode: ${e.code}, errMessage: ${e.message}`);
  })
} catch (err) {
  let e: BusinessError = err as BusinessError;
  console.error(`getDeviceNetworkIdList errCode: ${e.code}, errMessage: ${e.message}`);
}
```

ArkTS-Sta示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let queryFiler: distributedDeviceManager.NetworkIdQueryFilter = {
    wiseDeviceId: '',
    onlineStatus: 1,
  }
  let dmInstance = distributedDeviceManager.createDeviceManager('ohos.samples.jsHelloWorld');
  dmInstance.getDeviceNetworkIdList(queryFiler).then((data:Array<string>) => {
    console.info('getDeviceNetworkIdList name:' + JSON.stringify(data));
  }).catch((err) => {
    let e: BusinessError = err as BusinessError;
    console.error(`getDeviceNetworkIdList errCode: ${e.code}, errMessage: ${e.message}`);
  })
} catch (err) {
  let e: BusinessError = err as BusinessError;
  console.error(`getDeviceNetworkIdList errCode: ${e.code}, errMessage: ${e.message}`);
}
```

## getDeviceProfileInfoList

```TypeScript
getDeviceProfileInfoList(filterOptions: DeviceProfileInfoFilterOptions): Promise<Array<DeviceProfileInfo>>
```

获取同账号下全部的设备列表，使用Promise异步回调。

**起始版本：** 15

**ArkTS模式：** ArkTS-Dyn起始版本为15；ArkTS-Sta起始版本为23。

**需要权限：** ohos.permission.ACCESS_SERVICE_DM

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
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [11600102](../errorcode-device-manager.md#11600102-获取服务失败) |
| [11600106](../errorcode-device-manager.md#11600106-从云端获取数据失败) |
| [11600107](../errorcode-device-manager.md#11600107-需要登录账号) |

**示例**

ArkTS-Dyn示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let dmInstance = distributedDeviceManager.createDeviceManager('ohos.samples.jsHelloWorld');
  dmInstance.getDeviceProfileInfoList({"isCloud": false}).then((data: Array<distributedDeviceManager.DeviceProfileInfo>) => {
    console.info('getDeviceProfileInfoList' + JSON.stringify(data));
  }).catch((err: BusinessError) => {
    let e: BusinessError = err as BusinessError;
    console.error(`getDeviceProfileInfoList errCode: ${e.code}, errMessage: ${e.message}`);
  });
} catch (err) {
  let e: BusinessError = err as BusinessError;
  console.error(`getDeviceProfileInfoList errCode: ${e.code}, errMessage: ${e.message}`);
}
```

ArkTS-Sta示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let dmInstance = distributedDeviceManager.createDeviceManager('ohos.samples.jsHelloWorld');
  dmInstance.getDeviceProfileInfoList({"isCloud": false}).then((data: Array<distributedDeviceManager.DeviceProfileInfo>) => {
    console.info('getDeviceProfileInfoList' + JSON.stringify(data));
  }).catch((err) => {
    let e: BusinessError = err as BusinessError;
    console.error(`getDeviceProfileInfoList errCode: ${e.code}, errMessage: ${e.message}`);
  });
} catch (err) {
  let e: BusinessError = err as BusinessError;
  console.error(`getDeviceProfileInfoList errCode: ${e.code}, errMessage: ${e.message}`);
}
```

## getIdentificationByDeviceIds

```TypeScript
getIdentificationByDeviceIds(deviceIds: Array<string>): Array<DeviceIdentification>
```

根据设备ID查询设备标识。

**起始版本：** 24

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为24。

**需要权限：** ohos.permission.DISTRIBUTED_DATASYNC and ohos.permission.ACCESS_SERVICE_DM and ohos.permission.sec.ACCESS_UDID

**模型约束：** 此接口仅可在Stage模型下使用。

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
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [11600101](../errorcode-device-manager.md#11600101-服务调用异常) |

**示例**

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

ArkTS-Dyn:
```TypeScript
getLocalDisplayDeviceName(maxNameLength: number): Promise<string>
```

ArkTS-Sta:
```TypeScript
getLocalDisplayDeviceName(maxNameLength: int): Promise<string>
```

获取本机指定长度（字节数）的显示名，使用Promise异步回调。

**起始版本：** 18

**ArkTS模式：** ArkTS-Dyn起始版本为18；ArkTS-Sta起始版本为23。

**需要权限：** ohos.permission.ACCESS_SERVICE_DM

**系统能力：** SystemCapability.DistributedHardware.DeviceManager

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| maxNameLength | ArkTS-Dyn: number<br>ArkTS-Sta：int | 是 |

**返回值：**

| 类型 |
| --- |
| string |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [11600102](../errorcode-device-manager.md#11600102-获取服务失败) |

**示例**

ArkTS-Dyn示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let dmInstance = distributedDeviceManager.createDeviceManager('ohos.samples.jsHelloWorld');
  let maxNameLength:number = 21;
  dmInstance.getLocalDisplayDeviceName(maxNameLength).then((data:string)=>{
    console.info('getLocalDisplayDeviceName name:' + JSON.stringify(data));
  }).catch((e: BusinessError)=>{
    console.error(`getLocalDisplayDeviceName errCode: ${e.code}, errMessage: ${e.message}`);
  });
} catch (err) {
  let e: BusinessError = err as BusinessError;
  console.error(`getLocalDisplayDeviceName errCode: ${e.code}, errMessage: ${e.message}`);
}
```

ArkTS-Sta示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let dmInstance = distributedDeviceManager.createDeviceManager('ohos.samples.jsHelloWorld');
  let maxNameLength: int = 21;
  dmInstance.getLocalDisplayDeviceName(maxNameLength).then((data: string) => {
    console.info('getLocalDisplayDeviceName name:' + JSON.stringify(data));
  }).catch((err) => {
    let e: BusinessError = err as BusinessError;
    console.error(`getLocalDisplayDeviceName errCode: ${e.code}, errMessage: ${e.message}`);
  });
} catch (err) {
  let e: BusinessError = err as BusinessError;
  console.error(`getLocalDisplayDeviceName errCode: ${e.code}, errMessage: ${e.message}`);
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

**起始版本：** 26.1.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.1.0。

**需要权限：** ohos.permission.DISTRIBUTED_DATASYNC and ohos.permission.ACCESS_SERVICE_DM

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.DistributedHardware.DeviceManager

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| networkId | string | 是 |

**返回值：**

| 类型 |
| --- |
| ArkTS-Dyn: number<br>ArkTS-Sta：int |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [11600102](../errorcode-device-manager.md#11600102-获取服务失败) |
| [11600110](../errorcode-device-manager.md#11600110-无效的网络id) |

**示例**

ArkTS-Dyn示例：

```TypeScript
import { distributedDeviceManager } from '@kit.DistributedServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let dmInstance = distributedDeviceManager.createDeviceManager('ohos.samples.jsHelloWorld');
  let networkId: string = 'test_network_id';
  let osType: number = dmInstance.getOsTypeByNetworkId(networkId);
  console.info(`getOsTypeByNetworkId result: ${osType}`);
} catch (err) {
  let e: BusinessError = err as BusinessError;
  console.error(`getOsTypeByNetworkId errCode: ${e.code}, errMessage: ${e.message}`);
}
```

ArkTS-Sta示例：

```TypeScript
import { distributedDeviceManager } from '@kit.DistributedServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let dmInstance = distributedDeviceManager.createDeviceManager('ohos.samples.jsHelloWorld');
  let networkId: string = 'test_network_id';
  let osType: int = dmInstance.getOsTypeByNetworkId(networkId);
  console.info(`getOsTypeByNetworkId result: ${osType}`);
} catch (err) {
  let e = err as Error;
  console.error(`getOsTypeByNetworkId errCode: ${e.code}, errMessage: ${e.message}`);
}
```

## off('replyResult')

```TypeScript
off(type: 'replyResult', callback?: Callback<{ param: string; }>): void
```

取消回复UI操作结果回调。使用callback异步回调。

**起始版本：** 10

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为10。

**需要权限：** ohos.permission.ACCESS_SERVICE_DM

**系统能力：** SystemCapability.DistributedHardware.DeviceManager

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'replyResult' | 是 |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;{ param: string; }&gt; | 否 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

**示例**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let dmInstance = distributedDeviceManager.createDeviceManager('ohos.samples.jsHelloWorld');
  dmInstance.off('replyResult');
} catch (err) {
  let e: BusinessError = err as BusinessError;
  console.error(`replyResult errCode: ${e.code}, errMessage: ${e.message}`);
}
```

## offReplyResult

```TypeScript
offReplyResult(callback?: Callback<ReplyResult>): void
```

取消回复UI操作结果回调。使用callback异步回调。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**需要权限：** ohos.permission.ACCESS_SERVICE_DM

**系统能力：** SystemCapability.DistributedHardware.DeviceManager

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[ReplyResult](arkts-distributedservice-distributeddevicemanager-replyresult-i-sys.md)&gt; | 否 |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

**示例**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let dmInstance = distributedDeviceManager.createDeviceManager('ohos.samples.jsHelloWorld');
  dmInstance.offReplyResult();
} catch (err) {
  let e: BusinessError = err as BusinessError;
  console.error(`offReplyResult errCode: ${e.code}, errMessage: ${e.message}`);
}
```

## on('replyResult')

```TypeScript
on(type: 'replyResult', callback: Callback<{ param: string; }>): void
```

回复UI操作结果回调。使用callback异步回调。

**起始版本：** 10

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为10。

**需要权限：** ohos.permission.ACCESS_SERVICE_DM

**系统能力：** SystemCapability.DistributedHardware.DeviceManager

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'replyResult' | 是 |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;{ param: string; }&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

**示例**

```TypeScript
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
  console.error(`replyResult errCode: ${e.code}, errMessage: ${e.message}`);
}
```

## onReplyResult

```TypeScript
onReplyResult(callback: Callback<ReplyResult>): void
```

回复UI操作结果回调。使用callback异步回调。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**需要权限：** ohos.permission.ACCESS_SERVICE_DM

**系统能力：** SystemCapability.DistributedHardware.DeviceManager

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[ReplyResult](arkts-distributedservice-distributeddevicemanager-replyresult-i-sys.md)&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

**示例**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let dmInstance = distributedDeviceManager.createDeviceManager('ohos.samples.jsHelloWorld');
  dmInstance.onReplyResult((data: distributedDeviceManager.ReplyResult) => {
    console.info('onReplyResult executed, data: ' + JSON.stringify(data));
  });
} catch (err) {
  let e: BusinessError = err as BusinessError;
  console.error(`onReplyResult errCode: ${e.code}, errMessage: ${e.message}`);
}
```

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

**起始版本：** 18

**ArkTS模式：** ArkTS-Dyn起始版本为18；ArkTS-Sta起始版本为23。

**需要权限：** ohos.permission.ACCESS_SERVICE_DM

**系统能力：** SystemCapability.DistributedHardware.DeviceManager

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| deviceProfileInfoList | Array&lt;[DeviceProfileInfo](arkts-distributedservice-distributeddevicemanager-deviceprofileinfo-i-sys.md)&gt; | 是 |

**返回值：**

| 类型 |
| --- |
| ArkTS-Dyn: Promise & lt;number & gt;<br>ArkTS-Sta：Promise & lt;int & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [11600102](../errorcode-device-manager.md#11600102-获取服务失败) |

**示例**

ArkTS-Dyn示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let dmInstance = distributedDeviceManager.createDeviceManager('ohos.samples.jsHelloWorld');
  let deviceProfileInfoList:Array<distributedDeviceManager.DeviceProfileInfo> = [];
  dmInstance.putDeviceProfileInfoList(deviceProfileInfoList).then((data:number) => {
    console.info('put device profile info:' + JSON.stringify(data));
  }).catch((e: BusinessError) => {
    console.error(`putDeviceProfileInfoList errCode: ${e.code}, errMessage: ${e.message}`);
  });
} catch (err) {
  let e: BusinessError = err as BusinessError;
  console.error(`putDeviceProfileInfoList errCode: ${e.code}, errMessage: ${e.message}`);
}
```

ArkTS-Sta示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let dmInstance = distributedDeviceManager.createDeviceManager('ohos.samples.jsHelloWorld');
  let deviceProfileInfoList: Array<distributedDeviceManager.DeviceProfileInfo> = [];
  dmInstance.putDeviceProfileInfoList(deviceProfileInfoList).then((data: int) => {
    console.info('put device profile info:' + JSON.stringify(data));
  }).catch((err) => {
    let e: BusinessError = err as BusinessError;
    console.error(`putDeviceProfileInfoList errCode: ${e.code}, errMessage: ${e.message}`);
  });
} catch (err) {
  let e: BusinessError = err as BusinessError;
  console.error(`putDeviceProfileInfoList errCode: ${e.code}, errMessage: ${e.message}`);
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

**起始版本：** 10

**ArkTS模式：** ArkTS-Dyn起始版本为10；ArkTS-Sta起始版本为23。

**需要权限：** ohos.permission.ACCESS_SERVICE_DM

**系统能力：** SystemCapability.DistributedHardware.DeviceManager

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| action | ArkTS-Dyn: number<br>ArkTS-Sta：int | 是 |
| actionResult | string | 是 |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |

**示例**

ArkTS-Dyn示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

try {
  /*
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
  console.error(`replyUiAction errCode: ${e.code}, errMessage: ${e.message}`);
}
```

ArkTS-Sta示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

try {
  /*
   * action = 0 - 允许授权
   * action = 1 - 取消授权
   * action = 2 - 授权框用户操作超时
   * action = 3 - 取消pin码框展示
   * action = 4 - 取消pin码输入框展示
   * action = 5 - pin码输入框确定操作
   */
  let operation : int = 0;
  let dmInstance = distributedDeviceManager.createDeviceManager('ohos.samples.jsHelloWorld');
  dmInstance.replyUiAction(operation, 'extra');
} catch (err) {
  let e: BusinessError = err as BusinessError;
  console.error(`replyUiAction errCode: ${e.code}, errMessage: ${e.message}`);
}
```

## restoreLocalDeivceName

```TypeScript
restoreLocalDeivceName(): void
```

系统重置还原网络设置时，还原本机设备名。

**起始版本：** 18

**ArkTS模式：** ArkTS-Dyn起始版本为18；ArkTS-Sta起始版本为23。

**废弃版本：** 24

**替代接口：** [restoreLocalDeviceName](#restorelocaldevicename)

**需要权限：** ohos.permission.ACCESS_SERVICE_DM

**系统能力：** SystemCapability.DistributedHardware.DeviceManager

**系统接口：** 此接口为系统接口。

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [11600102](../errorcode-device-manager.md#11600102-获取服务失败) |

**示例**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let dmInstance = distributedDeviceManager.createDeviceManager('ohos.samples.jsHelloWorld');
  dmInstance.restoreLocalDeivceName();
} catch (err) {
  let e: BusinessError = err as BusinessError;
  console.error(`restoreLocalDeivceName errCode: ${e.code}, errMessage: ${e.message}`);
}
```

## restoreLocalDeviceName

```TypeScript
restoreLocalDeviceName(): void
```

系统重置还原网络设置时，还原本机设备名。

**起始版本：** 24

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为24。

**需要权限：** ohos.permission.ACCESS_SERVICE_DM

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.DistributedHardware.DeviceManager

**系统接口：** 此接口为系统接口。

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [11600102](../errorcode-device-manager.md#11600102-获取服务失败) |

**示例**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let dmInstance = distributedDeviceManager.createDeviceManager('ohos.samples.jsHelloWorld');
  dmInstance.restoreLocalDeviceName();
} catch (err) {
  let e: BusinessError = err as BusinessError;
  console.error(`restoreLocalDeviceName errCode: ${e.code}, errMessage: ${e.message}`);
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

**起始版本：** 15

**ArkTS模式：** ArkTS-Dyn起始版本为15；ArkTS-Sta起始版本为23。

**需要权限：** ohos.permission.ACCESS_SERVICE_DM

**系统能力：** SystemCapability.DistributedHardware.DeviceManager

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| policy | [StrategyForHeartbeat](arkts-distributedservice-distributeddevicemanager-strategyforheartbeat-e-sys.md) | 是 |
| delayTime | ArkTS-Dyn: number<br>ArkTS-Sta：int | 是 |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [11600102](../errorcode-device-manager.md#11600102-获取服务失败) |

**示例**

ArkTS-Dyn示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let policy = distributedDeviceManager.StrategyForHeartbeat.TEMP_STOP_HEARTBEAT;
  let delayTime = 1000;
  let dmInstance = distributedDeviceManager.createDeviceManager('ohos.samples.jsHelloWorld');
  dmInstance.setHeartbeatPolicy(policy, delayTime);
} catch (err) {
  let e: BusinessError = err as BusinessError;
  console.error(`setHeartbeatPolicy errCode: ${e.code}, errMessage: ${e.message}`);
}
```

ArkTS-Sta示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let policy: distributedDeviceManager.StrategyForHeartbeat =
    distributedDeviceManager.StrategyForHeartbeat.TEMP_STOP_HEARTBEAT;
  let delayTime: int = 1000;
  let dmInstance = distributedDeviceManager.createDeviceManager('ohos.samples.jsHelloWorld');
  dmInstance.setHeartbeatPolicy(policy, delayTime);
} catch (err) {
  let e: BusinessError = err as BusinessError;
  console.error(`setHeartbeatPolicy errCode: ${e.code}, errMessage: ${e.message}`);
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

**起始版本：** 18

**ArkTS模式：** ArkTS-Dyn起始版本为18；ArkTS-Sta起始版本为23。

**需要权限：** ohos.permission.ACCESS_SERVICE_DM

**系统能力：** SystemCapability.DistributedHardware.DeviceManager

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| deviceName | string | 是 |

**返回值：**

| 类型 |
| --- |
| ArkTS-Dyn: Promise & lt;number & gt;<br>ArkTS-Sta：Promise & lt;int & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [11600102](../errorcode-device-manager.md#11600102-获取服务失败) |
| [11600106](../errorcode-device-manager.md#11600106-从云端获取数据失败) |
| [11600107](../errorcode-device-manager.md#11600107-需要登录账号) |
| [11600108](../errorcode-device-manager.md#11600108-设备名称含非法信息) |

**示例**

ArkTS-Dyn示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let dmInstance = distributedDeviceManager.createDeviceManager('ohos.samples.jsHelloWorld');
  let deviceName:string = 'xxx';
  dmInstance.setLocalDeviceName(deviceName).then((data:number)=>{
    console.info('setLocalDeviceName name:' + JSON.stringify(data));
  }).catch((e: BusinessError)=>{
    console.error(`setLocalDeviceName errCode: ${e.code}, errMessage: ${e.message}`);
  });
} catch (err) {
  let e: BusinessError = err as BusinessError;
  console.error(`setLocalDeviceName errCode: ${e.code}, errMessage: ${e.message}`);
}
```

ArkTS-Sta示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let dmInstance = distributedDeviceManager.createDeviceManager('ohos.samples.jsHelloWorld');
  let deviceName: string = 'xxx';
  dmInstance.setLocalDeviceName(deviceName).then((data: int) => {
    console.info('setLocalDeviceName name:' + JSON.stringify(data));
  }).catch((err) => {
    let e: BusinessError = err as BusinessError;
    console.error(`setLocalDeviceName errCode: ${e.code}, errMessage: ${e.message}`);
  });
} catch (err) {
  let e: BusinessError = err as BusinessError;
  console.error(`setLocalDeviceName errCode: ${e.code}, errMessage: ${e.message}`);
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

**起始版本：** 18

**ArkTS模式：** ArkTS-Dyn起始版本为18；ArkTS-Sta起始版本为23。

**需要权限：** ohos.permission.ACCESS_SERVICE_DM

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
| ArkTS-Dyn: Promise & lt;number & gt;<br>ArkTS-Sta：Promise & lt;int & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [11600102](../errorcode-device-manager.md#11600102-获取服务失败) |
| [11600106](../errorcode-device-manager.md#11600106-从云端获取数据失败) |
| [11600107](../errorcode-device-manager.md#11600107-需要登录账号) |
| [11600108](../errorcode-device-manager.md#11600108-设备名称含非法信息) |

**示例**

ArkTS-Dyn示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let dmInstance = distributedDeviceManager.createDeviceManager('ohos.samples.jsHelloWorld');
  let deviceId:string = 'xxx';
  let deviceName:string = 'xxx';
  dmInstance.setRemoteDeviceName(deviceId, deviceName).then((data:number)=>{
    console.info('setRemoteDeviceName name:' + JSON.stringify(data));
  }).catch((e: BusinessError)=>{
    console.error(`setRemoteDeviceName errCode: ${e.code}, errMessage: ${e.message}`);
  });
} catch (err) {
  let e: BusinessError = err as BusinessError;
  console.error(`setRemoteDeviceName errCode: ${e.code}, errMessage: ${e.message}`);
}
```

ArkTS-Sta示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let dmInstance = distributedDeviceManager.createDeviceManager('ohos.samples.jsHelloWorld');
  let deviceId: string = 'xxx';
  let deviceName: string = 'xxx';
  dmInstance.setRemoteDeviceName(deviceId, deviceName).then((data: int) => {
    console.info('setRemoteDeviceName name:' + JSON.stringify(data));
  }).catch((err) => {
    let e: BusinessError = err as BusinessError;
    console.error(`setRemoteDeviceName errCode: ${e.code}, errMessage: ${e.message}`);
  });
} catch (err) {
  let e: BusinessError = err as BusinessError;
  console.error(`setRemoteDeviceName errCode: ${e.code}, errMessage: ${e.message}`);
}
```
