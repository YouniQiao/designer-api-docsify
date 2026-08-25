# @ohos.distributedHardware.deviceManager

本模块能力已更新至新模块。建议使用新模块的接口进行开发，参见 [@ohos.distributedDeviceManager](arkts-distributeddevicemanager.md)。 本模块提供分布式设备管理能力。 系统应用可调用接口实现如下功能：  
- 注册和解除注册设备上下线变化监听。 - 发现周边不可信设备。 - 认证和取消认证设备。 - 查询可信设备列表。 - 查询本地设备信息，包括设备名称，设备类型和设备标识。 - 发布设备发现。

**起始版本：** 7

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为7。

**废弃版本：** 11

**替代接口：** [distributedDeviceManager](arkts-distributeddevicemanager.md)

**系统能力：** SystemCapability.DistributedHardware.DeviceManager

## 导入模块

```TypeScript
import { deviceManager } from '@kit.DistributedServiceKit';
```

## 汇总

<!--Del-->
### 函数（系统接口）

| 名称 |
| --- |
| [createDeviceManager](arkts-distributedservice-devicemanager-createdevicemanager-f-sys.md) |
<!--DelEnd-->

<!--Del-->
### 接口（系统接口）

| 名称 |
| --- |
| [AuthInfo](arkts-distributedservice-devicemanager-authinfo-i-sys.md) |
| [AuthParam](arkts-distributedservice-devicemanager-authparam-i-sys.md) |
| [DeviceInfo](arkts-distributedservice-devicemanager-deviceinfo-i-sys.md) |
| [DeviceManager](arkts-distributedservice-devicemanager-devicemanager-i-sys.md) |
| [PublishInfo](arkts-distributedservice-devicemanager-publishinfo-i-sys.md) |
| [SubscribeInfo](arkts-distributedservice-devicemanager-subscribeinfo-i-sys.md) |
<!--DelEnd-->

<!--Del-->
### 枚举（系统接口）

| 名称 |
| --- |
| [AuthForm](arkts-distributedservice-devicemanager-authform-e-sys.md) |
| [DeviceStateChangeAction](arkts-distributedservice-devicemanager-devicestatechangeaction-e-sys.md) |
| [DeviceType](arkts-distributedservice-devicemanager-devicetype-e-sys.md) |
| [DiscoverMode](arkts-distributedservice-devicemanager-discovermode-e-sys.md) |
| [ExchangeFreq](arkts-distributedservice-devicemanager-exchangefreq-e-sys.md) |
| [ExchangeMedium](arkts-distributedservice-devicemanager-exchangemedium-e-sys.md) |
| [SubscribeCap](arkts-distributedservice-devicemanager-subscribecap-e-sys.md) |
<!--DelEnd-->
