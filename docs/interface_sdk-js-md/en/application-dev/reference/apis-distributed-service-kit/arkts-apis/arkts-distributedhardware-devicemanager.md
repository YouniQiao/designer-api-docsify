# @ohos.distributedHardware.deviceManager

本模块能力已更新至新模块。建议使用新模块的接口进行开发，参见  
[@ohos.distributedDeviceManager](arkts-distributeddevicemanager.md)。本模块提供分布式设备管理能力。系统应用可调用接口实现如下功能：

- 注册和解除注册设备上下线变化监听。  
- 发现周边不可信设备。  
- 认证和取消认证设备。  
- 查询可信设备列表。  
- 查询本地设备信息，包括设备名称，设备类型和设备标识。  
- 发布设备发现。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 11

**Substitutes:** [@ohos.distributedDeviceManager:distributedDeviceManager](arkts-distributeddevicemanager.md)

<!--Device-unnamed-declare namespace deviceManager--><!--Device-unnamed-declare namespace deviceManager-End-->

**System capability:** SystemCapability.DistributedHardware.DeviceManager

## Modules to Import

```TypeScript
import { deviceManager } from 'kits/@kit.DistributedServiceKit';
```

## Summary

<!--Del-->
### Functions（系统接口）

| Name | Description |
| --- | --- |
| [createDeviceManager](arkts-distributedservice-devicemanager-createdevicemanager-f-sys.md#createdevicemanager) | 创建一个设备管理器实例。 |
<!--DelEnd-->

<!--Del-->
### Interfaces（系统接口）

| Name | Description |
| --- | --- |
| [AuthInfo](arkts-distributedservice-devicemanager-authinfo-i-sys.md) | 认证信息。 |
| [AuthParam](arkts-distributedservice-devicemanager-authparam-i-sys.md) | 认证参数。 |
| [DeviceInfo](arkts-distributedservice-devicemanager-deviceinfo-i-sys.md) | 设备信息。 |
| [DeviceManager](arkts-distributedservice-devicemanager-devicemanager-i-sys.md) | 设备管理实例，用于获取可信设备和本地设备的相关信息。在调用DeviceManager的方法前，需要先通过createDeviceManager构建一个DeviceManager实例dmInstance。 |
| [PublishInfo](arkts-distributedservice-devicemanager-publishinfo-i-sys.md) | 发布设备参数 |
| [SubscribeInfo](arkts-distributedservice-devicemanager-subscribeinfo-i-sys.md) | 发现信息。 |
<!--DelEnd-->

<!--Del-->
### Enums（系统接口）

| Name | Description |
| --- | --- |
| [AuthForm](arkts-distributedservice-devicemanager-authform-e-sys.md) | 表示设备认证类型的枚举类。 |
| [DeviceStateChangeAction](arkts-distributedservice-devicemanager-devicestatechangeaction-e-sys.md) | 表示设备状态变化的枚举。 |
| [DeviceType](arkts-distributedservice-devicemanager-devicetype-e-sys.md) | 表示设备类型的枚举类。 |
| [DiscoverMode](arkts-distributedservice-devicemanager-discovermode-e-sys.md) | 表示发现模式的枚举。 |
| [ExchangeFreq](arkts-distributedservice-devicemanager-exchangefreq-e-sys.md) | 表示发现频率的枚举。 |
| [ExchangeMedium](arkts-distributedservice-devicemanager-exchangemedium-e-sys.md) | 表示发现类型的枚举。 |
| [SubscribeCap](arkts-distributedservice-devicemanager-subscribecap-e-sys.md) | 表示发现能力的枚举。 |
<!--DelEnd-->

