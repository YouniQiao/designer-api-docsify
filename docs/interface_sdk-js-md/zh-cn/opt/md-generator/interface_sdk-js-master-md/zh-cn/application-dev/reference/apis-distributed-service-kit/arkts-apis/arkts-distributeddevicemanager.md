# @ohos.distributedDeviceManager

本模块提供分布式设备管理能力。 应用可调用接口实现如下功能： - 注册和解除注册设备上下线变化监听。 - 发现周边不可信设备。 - 认证和取消认证设备。 - 查询可信设备列表。 - 查询本地设备信息，包括设备名称，设备类型和设备标识等。

**起始版本：** 23

<!--Device-unnamed-declare namespace distributedDeviceManager--><!--Device-unnamed-declare namespace distributedDeviceManager-End-->

**系统能力：** SystemCapability.DistributedHardware.DeviceManager

## 导入模块

```TypeScript
```

## 汇总

### 函数

| 名称 |
| --- |
| [createDeviceManager](arkts-distributedservice-distributeddevicemanager-createdevicemanager-f.md#createdevicemanager) |
| [releaseDeviceManager](arkts-distributedservice-distributeddevicemanager-releasedevicemanager-f.md#releasedevicemanager) |

### 接口

| 名称 |
| --- |
| [BindTargetResult](arkts-distributedservice-distributeddevicemanager-bindtargetresult-i.md) |
| [DeviceBasicInfo](arkts-distributedservice-distributeddevicemanager-devicebasicinfo-i.md) |
| [DeviceManager](arkts-distributedservice-distributeddevicemanager-devicemanager-i.md) |
| [DeviceNameChangeResult](arkts-distributedservice-distributeddevicemanager-devicenamechangeresult-i.md) |
| [DeviceStateChangeResult](arkts-distributedservice-distributeddevicemanager-devicestatechangeresult-i.md) |
| [DiscoveryFailureResult](arkts-distributedservice-distributeddevicemanager-discoveryfailureresult-i.md) |
| [DiscoverySuccessResult](arkts-distributedservice-distributeddevicemanager-discoverysuccessresult-i.md) |
| [ServiceDieData](arkts-distributedservice-distributeddevicemanager-servicediedata-i.md) |

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
| [ReplyResult](arkts-distributedservice-distributeddevicemanager-replyresult-i-sys.md) |
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
