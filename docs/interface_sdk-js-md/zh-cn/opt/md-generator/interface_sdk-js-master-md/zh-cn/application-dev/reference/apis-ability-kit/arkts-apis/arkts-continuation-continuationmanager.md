# @ohos.continuation.continuationManager

continuationManager模块提供了流转/协同入口管理服务能力，包括连接/取消流转管理服务，注册/解注册设备连接变化监听，拉起设备选择模块，更新连接状态。

**起始版本：** 8

**废弃版本：** 22

**替代接口：** [distributedDeviceManager](../../apis-distributed-service-kit/arkts-apis/arkts-distributeddevicemanager.md#ohosdistributeddevicemanager)

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-unnamed-declare namespace continuationManager--><!--Device-unnamed-declare namespace continuationManager-End-->

**系统能力：** SystemCapability.Ability.DistributedAbilityManager

## 导入模块

```TypeScript
```

## 汇总

### 函数

| 名称 |
| --- |
| [off_deviceConnect](arkts-ability-continuationmanager-offdeviceconnect-f.md#offdeviceconnect) |
| [off_deviceDisconnect](arkts-ability-continuationmanager-offdevicedisconnect-f.md#offdevicedisconnect) |
| [off_deviceSelected](arkts-ability-continuationmanager-offdeviceselected-f.md#offdeviceselected) |
| [off_deviceUnselected](arkts-ability-continuationmanager-offdeviceunselected-f.md#offdeviceunselected) |
| [on_deviceConnect](arkts-ability-continuationmanager-ondeviceconnect-f.md#ondeviceconnect) |
| [on_deviceDisconnect](arkts-ability-continuationmanager-ondevicedisconnect-f.md#ondevicedisconnect) |
| [on_deviceSelected](arkts-ability-continuationmanager-ondeviceselected-f.md#ondeviceselected) |
| [on_deviceUnselected](arkts-ability-continuationmanager-ondeviceunselected-f.md#ondeviceunselected) |
| [register](arkts-ability-continuationmanager-register-f.md#register) |
| [register](arkts-ability-continuationmanager-register-f.md#register) |
| [register](arkts-ability-continuationmanager-register-f.md#register) |
| [registerContinuation](arkts-ability-continuationmanager-registercontinuation-f.md#registercontinuation) |
| [registerContinuation](arkts-ability-continuationmanager-registercontinuation-f.md#registercontinuation) |
| [registerContinuation](arkts-ability-continuationmanager-registercontinuation-f.md#registercontinuation) |
| [startContinuationDeviceManager](arkts-ability-continuationmanager-startcontinuationdevicemanager-f.md#startcontinuationdevicemanager) |
| [startContinuationDeviceManager](arkts-ability-continuationmanager-startcontinuationdevicemanager-f.md#startcontinuationdevicemanager) |
| [startContinuationDeviceManager](arkts-ability-continuationmanager-startcontinuationdevicemanager-f.md#startcontinuationdevicemanager) |
| [startDeviceManager](arkts-ability-continuationmanager-startdevicemanager-f.md#startdevicemanager) |
| [startDeviceManager](arkts-ability-continuationmanager-startdevicemanager-f.md#startdevicemanager) |
| [startDeviceManager](arkts-ability-continuationmanager-startdevicemanager-f.md#startdevicemanager) |
| [unregister](arkts-ability-continuationmanager-unregister-f.md#unregister) |
| [unregister](arkts-ability-continuationmanager-unregister-f.md#unregister) |
| [unregisterContinuation](arkts-ability-continuationmanager-unregistercontinuation-f.md#unregistercontinuation) |
| [unregisterContinuation](arkts-ability-continuationmanager-unregistercontinuation-f.md#unregistercontinuation) |
| [updateConnectStatus](arkts-ability-continuationmanager-updateconnectstatus-f.md#updateconnectstatus) |
| [updateConnectStatus](arkts-ability-continuationmanager-updateconnectstatus-f.md#updateconnectstatus) |
| [updateContinuationState](arkts-ability-continuationmanager-updatecontinuationstate-f.md#updatecontinuationstate) |
| [updateContinuationState](arkts-ability-continuationmanager-updatecontinuationstate-f.md#updatecontinuationstate) |

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
