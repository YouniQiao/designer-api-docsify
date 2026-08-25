# @ohos.continuation.continuationManager

continuationManager模块提供了流转/协同入口管理服务能力，包括连接/取消流转管理服务，注册/解注册设备连接变化监听，拉起设备选择模块，更新连接状态。

**起始版本：** 8

**废弃版本：** 22

**替代接口：** [distributedDeviceManager](../../apis-distributed-service-kit/arkts-apis/arkts-distributeddevicemanager.md)

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Ability.DistributedAbilityManager

## 导入模块

```TypeScript
import { continuationManager } from 'kits/@kit.AbilityKit';
```

## 汇总

### 函数

| 名称 |
| --- |
| [off](arkts-ability-continuationmanager-off-f.md#offdeviceselected) |
| [off](arkts-ability-continuationmanager-off-f.md#offdeviceunselected) |
| [off](arkts-ability-continuationmanager-off-f.md#offdeviceconnect) |
| [off](arkts-ability-continuationmanager-off-f.md#offdevicedisconnect) |
| [on](arkts-ability-continuationmanager-on-f.md#ondeviceselected) |
| [on](arkts-ability-continuationmanager-on-f.md#ondeviceunselected) |
| [on](arkts-ability-continuationmanager-on-f.md#ondeviceconnect) |
| [on](arkts-ability-continuationmanager-on-f.md#ondevicedisconnect) |
| [register](arkts-ability-continuationmanager-register-f.md) |
| [register](arkts-ability-continuationmanager-register-f.md) |
| [register](arkts-ability-continuationmanager-register-f.md) |
| [registerContinuation](arkts-ability-continuationmanager-registercontinuation-f.md) |
| [registerContinuation](arkts-ability-continuationmanager-registercontinuation-f.md) |
| [registerContinuation](arkts-ability-continuationmanager-registercontinuation-f.md) |
| [startContinuationDeviceManager](arkts-ability-continuationmanager-startcontinuationdevicemanager-f.md) |
| [startContinuationDeviceManager](arkts-ability-continuationmanager-startcontinuationdevicemanager-f.md) |
| [startContinuationDeviceManager](arkts-ability-continuationmanager-startcontinuationdevicemanager-f.md) |
| [startDeviceManager](arkts-ability-continuationmanager-startdevicemanager-f.md) |
| [startDeviceManager](arkts-ability-continuationmanager-startdevicemanager-f.md) |
| [startDeviceManager](arkts-ability-continuationmanager-startdevicemanager-f.md) |
| [unregister](arkts-ability-continuationmanager-unregister-f.md) |
| [unregister](arkts-ability-continuationmanager-unregister-f.md) |
| [unregisterContinuation](arkts-ability-continuationmanager-unregistercontinuation-f.md) |
| [unregisterContinuation](arkts-ability-continuationmanager-unregistercontinuation-f.md) |
| [updateConnectStatus](arkts-ability-continuationmanager-updateconnectstatus-f.md) |
| [updateConnectStatus](arkts-ability-continuationmanager-updateconnectstatus-f.md) |
| [updateContinuationState](arkts-ability-continuationmanager-updatecontinuationstate-f.md) |
| [updateContinuationState](arkts-ability-continuationmanager-updatecontinuationstate-f.md) |

### 枚举

| 名称 |
| --- |
| [ContinuationMode](arkts-ability-continuationmanager-continuationmode-e.md) |
| [DeviceConnectState](arkts-ability-continuationmanager-deviceconnectstate-e.md) |

### 类型

| 名称 |
| --- |
| [ContinuationExtraParams](arkts-ability-continuationmanager-continuationextraparams-t.md) |
| [ContinuationResult](arkts-ability-continuationmanager-continuationresult-t.md) |
