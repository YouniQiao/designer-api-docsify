# @ohos.distributedDeviceManager

本模块提供分布式设备管理能力，包括设备的发现、认证、状态监听和信息查询等功能。设备管理基于设备信任模型， 通过发现周边设备并进行认证绑定来建立可信连接，已认证的可信设备可用于分布式业务。应用可调用接口实现如下功能：  
- 注册和解除注册设备上下线变化监听。  
- 发现周边不可信设备。  
- 认证和取消认证设备。  
- 查询可信设备列表。  
- 查询本地设备信息，包括设备名称，设备类型和设备标识等。

> **说明：**&gt;
> 本模块首批接口从API version 10开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

**起始版本：** 10

**系统能力：** SystemCapability.DistributedHardware.DeviceManager

## 导入模块

```TypeScript
import { distributedDeviceManager } from 'kits/@kit.DistributedServiceKit';
```

## 汇总

### 函数

| 名称 |
| --- |
| [createDeviceManager](arkts-distributedservice-distributeddevicemanager-createdevicemanager-f.md) |
| [releaseDeviceManager](arkts-distributedservice-distributeddevicemanager-releasedevicemanager-f.md) |

### 接口

| 名称 |
| --- |
| [DeviceBasicInfo](arkts-distributedservice-distributeddevicemanager-devicebasicinfo-i.md) |
| [DeviceManager](arkts-distributedservice-distributeddevicemanager-devicemanager-i.md) |

<!--Del-->
### 接口（系统接口）

| 名称 |
| --- |
| [DeviceIconInfo](arkts-distributedservice-distributeddevicemanager-deviceiconinfo-i-sys.md) |
| [DeviceIconInfoFilterOptions](arkts-distributedservice-distributeddevicemanager-deviceiconinfofilteroptions-i-sys.md) |
| [DeviceIdentification](arkts-distributedservice-distributeddevicemanager-deviceidentification-i-sys.md) |
| [DeviceManager](arkts-distributedservice-distributeddevicemanager-devicemanager-i-sys.md) |
| [DeviceProfileInfo](arkts-distributedservice-distributeddevicemanager-deviceprofileinfo-i-sys.md) |
| [DeviceProfileInfoFilterOptions](arkts-distributedservice-distributeddevicemanager-deviceprofileinfofilteroptions-i-sys.md) |
| [NetworkIdQueryFilter](arkts-distributedservice-distributeddevicemanager-networkidqueryfilter-i-sys.md) |
| [ServiceProfileInfo](arkts-distributedservice-distributeddevicemanager-serviceprofileinfo-i-sys.md) |
<!--DelEnd-->

### 枚举

| 名称 |
| --- |
| [DeviceStateChange](arkts-distributedservice-distributeddevicemanager-devicestatechange-e.md) |

<!--Del-->
### 枚举（系统接口）

| 名称 |
| --- |
| [StrategyForHeartbeat](arkts-distributedservice-distributeddevicemanager-strategyforheartbeat-e-sys.md) |
<!--DelEnd-->
