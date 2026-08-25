# updateConnectStatus

## 导入模块

```TypeScript
import { continuationManager } from 'kits/@kit.AbilityKit';
```

## updateConnectStatus

```TypeScript
function updateConnectStatus(
    token: number,
    deviceId: string,
    status: DeviceConnectState,
    callback: AsyncCallback<void>
  ): void
```

通知设备选择模块，更新当前的连接状态，使用AsyncCallback方式作为异步方法。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [getAvailableDeviceListSync](../../apis-distributed-service-kit/arkts-apis/arkts-distributedservice-distributeddevicemanager-devicemanager-i.md#getavailabledevicelistsync)

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Ability.DistributedAbilityManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| token | number | 是 |
| deviceId | string | 是 |
| status | [DeviceConnectState](arkts-ability-continuationmanager-deviceconnectstate-e.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |


## updateConnectStatus

```TypeScript
function updateConnectStatus(token: number, deviceId: string, status: DeviceConnectState): Promise<void>
```

通知设备选择模块，更新当前的连接状态，使用Promise方式作为异步方法。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [getAvailableDeviceListSync](../../apis-distributed-service-kit/arkts-apis/arkts-distributedservice-distributeddevicemanager-devicemanager-i.md#getavailabledevicelistsync)

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Ability.DistributedAbilityManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| token | number | 是 |
| deviceId | string | 是 |
| status | [DeviceConnectState](arkts-ability-continuationmanager-deviceconnectstate-e.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |
