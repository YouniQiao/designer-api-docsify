# startDeviceManager

## startDeviceManager

```TypeScript
function startDeviceManager(token: number, callback: AsyncCallback<void>): void
```

拉起设备选择模块，可显示组网内可选择设备列表信息，无过滤条件，使用AsyncCallback方式作为异步方法。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [@ohos.distributedDeviceManager:distributedDeviceManager.DeviceManager.startDiscovering](../../apis-distributed-service-kit/arkts-apis/arkts-distributedservice-distributeddevicemanager-devicemanager-i.md/arkts-distributedservice-distributeddevicemanager-devicemanager-i.md#startdiscovering)(discoverParam:

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-continuationManager-function startDeviceManager(token: number, callback: AsyncCallback<void>): void--><!--Device-continuationManager-function startDeviceManager(token: number, callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.Ability.DistributedAbilityManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| token | number | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

## 示例

```TypeScript
import { continuationManager } from '@kit.AbilityKit';

let token: number = 1;
continuationManager.startDeviceManager(token, (err) => {
  if (err.code != 0) {
    console.error('startDeviceManager failed, cause: ' + JSON.stringify(err));
    return;
  }
  console.info('startDeviceManager finished. ');
});
```


## startDeviceManager

```TypeScript
function startDeviceManager(token: number, options: ContinuationExtraParams, callback: AsyncCallback<void>): void
```

拉起设备选择模块，可显示组网内可选择设备列表信息，使用AsyncCallback方式作为异步方法。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [@ohos.distributedDeviceManager:distributedDeviceManager.DeviceManager.startDiscovering](../../apis-distributed-service-kit/arkts-apis/arkts-distributedservice-distributeddevicemanager-devicemanager-i.md/arkts-distributedservice-distributeddevicemanager-devicemanager-i.md#startdiscovering)(discoverParam:

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-continuationManager-function startDeviceManager(token: number, options: ContinuationExtraParams, callback: AsyncCallback<void>): void--><!--Device-continuationManager-function startDeviceManager(token: number, options: ContinuationExtraParams, callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.Ability.DistributedAbilityManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| token | number | 是 |
| options | [ContinuationExtraParams](arkts-ability-continuationextraparams-continuationextraparams-i.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

## 示例

```TypeScript
import { continuationManager } from '@kit.AbilityKit';

let token: number = 1;
continuationManager.startDeviceManager(
  token,
  {
    deviceType: ["00E"]
  },
  (err) => {
    if (err.code != 0) {
      console.error('startDeviceManager failed, cause: ' + JSON.stringify(err));
      return;
    }
    console.info('startDeviceManager finished. ');
});
```


## startDeviceManager

```TypeScript
function startDeviceManager(token: number, options?: ContinuationExtraParams): Promise<void>
```

拉起设备选择模块，可显示组网内可选择设备列表信息，使用Promise方式作为异步方法。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [@ohos.distributedDeviceManager:distributedDeviceManager.DeviceManager.startDiscovering](../../apis-distributed-service-kit/arkts-apis/arkts-distributedservice-distributeddevicemanager-devicemanager-i.md/arkts-distributedservice-distributeddevicemanager-devicemanager-i.md#startdiscovering)(discoverParam:

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-continuationManager-function startDeviceManager(token: number, options?: ContinuationExtraParams): Promise<void>--><!--Device-continuationManager-function startDeviceManager(token: number, options?: ContinuationExtraParams): Promise<void>-End-->

**系统能力：** SystemCapability.Ability.DistributedAbilityManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| token | number | 是 |
| options | [ContinuationExtraParams](arkts-ability-continuationextraparams-continuationextraparams-i.md) | 否 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;void&gt; |

## 示例

```TypeScript
import { continuationManager } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let token: number = -1;
continuationManager.startDeviceManager(
  token,
  {
    deviceType: ["00E"]
  }).then(() => {
    console.info('startDeviceManager finished. ');
  }).catch((err: BusinessError) => {
    console.error('startDeviceManager failed, cause: ' + JSON.stringify(err));
});
```
