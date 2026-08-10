# getExemptedApps（系统接口）

## 导入模块

```TypeScript
import { deviceStandby } from 'kits/@kit.BackgroundTasksKit';
```

## getExemptedApps

```TypeScript
function getExemptedApps(resourceTypes: int, callback: AsyncCallback<Array<ExemptedAppInfo>>): void
```

获取进入待机模式的应用名单，使用Callback异步回调。

**起始版本：** 10

**ArkTS模式：** ArkTS-Dyn起始版本为10；ArkTS-Sta起始版本为23。

**需要权限：** ohos.permission.DEVICE_STANDBY_EXEMPTION

<!--Device-deviceStandby-function getExemptedApps(resourceTypes: int, callback: AsyncCallback<Array<ExemptedAppInfo>>): void--><!--Device-deviceStandby-function getExemptedApps(resourceTypes: int, callback: AsyncCallback<Array<ExemptedAppInfo>>): void-End-->

**系统能力：** SystemCapability.ResourceSchedule.DeviceStandby

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| resourceTypes | ArkTS-Dyn: number  <br>ArkTS-Sta：int | 是 | 资源类型，类型具体说明请参考[ResourceType](arkts-backgroundtasks-devicestandby-resourcetype-e-sys.md)。 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;ExemptedAppInfo&gt;&gt; | 是 | 豁免应用信息。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 9800004 | Failed to get device standby service. Possible cause: A necessary system service is not ready. |
| 9800001 | Memory operation failed. |
| 9800003 | Failed to complete inner transaction. |
| 9800002 | Failed to write data into parcel. Possible reasons: 1. Invalid parameters. |
| 201 | Permission denied. |
| 202 | Not System App. |
| 18700001 | Caller information verification failed. |

## 示例

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { deviceStandby } from '@kit.BackgroundTasksKit';

let resourceTypes: deviceStandby.ResourceType  = deviceStandby.ResourceType.TIMER | deviceStandby.ResourceType.NETWORK;
deviceStandby.getExemptedApps(resourceTypes, (err: BusinessError, res: Array<deviceStandby.ExemptedAppInfo>) => {
  if (err) {
    console.error('DEVICE_STANDBY getExemptedApps callback failed. code is: ' + err.code + ',message is: ' + err.message);
  } else {
    console.info('DEVICE_STANDBY getExemptedApps callback success.');
    for (let i = 0; i < res.length; i++) {
      console.info('DEVICE_STANDBY getExemptedApps callback result ' + JSON.stringify(res[i]));
    }
  }
});
```


## getExemptedApps

```TypeScript
function getExemptedApps(resourceTypes: int): Promise<Array<ExemptedAppInfo>>
```

获取进入待机模式的应用名单，使用Promise异步回调。

**起始版本：** 10

**ArkTS模式：** ArkTS-Dyn起始版本为10；ArkTS-Sta起始版本为23。

**需要权限：** ohos.permission.DEVICE_STANDBY_EXEMPTION

<!--Device-deviceStandby-function getExemptedApps(resourceTypes: int): Promise<Array<ExemptedAppInfo>>--><!--Device-deviceStandby-function getExemptedApps(resourceTypes: int): Promise<Array<ExemptedAppInfo>>-End-->

**系统能力：** SystemCapability.ResourceSchedule.DeviceStandby

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| resourceTypes | ArkTS-Dyn: number  <br>ArkTS-Sta：int | 是 | 资源类型，类型具体说明请参考[ResourceType](arkts-backgroundtasks-devicestandby-resourcetype-e-sys.md)。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;Array&lt;ExemptedAppInfo&gt;&gt; | 豁免应用信息。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 9800004 | Failed to get device standby service. Possible cause: A necessary system service is not ready. |
| 9800001 | Memory operation failed. |
| 9800003 | Failed to complete inner transaction. |
| 9800002 | Failed to write data into parcel. Possible reasons: 1. Invalid parameters. |
| 201 | Permission denied. |
| 202 | Not System App. |
| 18700001 | Caller information verification failed. |

## 示例

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { deviceStandby } from '@kit.BackgroundTasksKit';

let resourceTypes: deviceStandby.ResourceType = deviceStandby.ResourceType.TIMER | deviceStandby.ResourceType.NETWORK;
deviceStandby.getExemptedApps(resourceTypes).then( (res: Array<deviceStandby.ExemptedAppInfo>) => {
  console.info('DEVICE_STANDBY getExemptedApps promise success.');
  for (let i = 0; i < res.length; i++) {
    console.info('DEVICE_STANDBY getExemptedApps promise result ' + JSON.stringify(res[i]));
  }
}).catch( (err: BusinessError) => {
  console.error('DEVICE_STANDBY getExemptedApps promise failed. code is: ' + err.code + ',message is: ' + err.message);
});
```

