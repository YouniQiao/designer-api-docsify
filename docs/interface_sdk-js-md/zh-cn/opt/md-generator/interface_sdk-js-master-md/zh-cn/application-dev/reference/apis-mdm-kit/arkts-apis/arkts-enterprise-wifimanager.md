# @ohos.enterprise.wifiManager

本模块提供企业设备Wi-Fi管理能力，包括查询Wi-Fi开启状态、配置Wi-Fi连接、管理Wi-Fi名单等。 **使用场景**： - 企业设备批量配置Wi-Fi连接，简化设备初始化流程 - 控制设备可连接的Wi-Fi网络，实现网络访问合规管理 - 管理企业设备的Wi-Fi开关，统一网络策略 **功能收益**： - 提高企业网络管理效率，减少IT运维成本 - 确保设备仅连接安全的Wi-Fi网络，降低安全风险 - 实现网络策略统一管控，满足企业合规要求 > **说明：** > > 本模块接口仅对设备管理应用开放，且调用接口前需激活设备管理应用，具体请参考[MDM Kit开发指南](../../../mdm/mdm-kit-guide.md)。 > > 全局通用限制类策略由restrictions统一提供，若要全局禁用Wi-Fi，请参考 > [@ohos.enterprise.restrictions（限制类策略）](arkts-enterprise-restrictions.md#ohosenterpriserestrictions)。

**起始版本：** 10

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-unnamed-declare namespace wifiManager--><!--Device-unnamed-declare namespace wifiManager-End-->

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**系统接口：** 此接口为系统接口。

## 导入模块

```TypeScript
```

## 汇总

### 函数

| 名称 |
| --- |
| [addAllowedWifiList](arkts-mdm-wifimanager-addallowedwifilist-f.md#addallowedwifilist) |
| [addDisallowedWifiList](arkts-mdm-wifimanager-adddisallowedwifilist-f.md#adddisallowedwifilist) |
| [getAllowedWifiList](arkts-mdm-wifimanager-getallowedwifilist-f.md#getallowedwifilist) |
| [getAllowedWifiList](arkts-mdm-wifimanager-getallowedwifilist-f.md#getallowedwifilist) |
| [getDisallowedWifiList](arkts-mdm-wifimanager-getdisallowedwifilist-f.md#getdisallowedwifilist) |
| [getDisallowedWifiList](arkts-mdm-wifimanager-getdisallowedwifilist-f.md#getdisallowedwifilist) |
| [isWifiActiveSync](arkts-mdm-wifimanager-iswifiactivesync-f.md#iswifiactivesync) |
| [removeAllowedWifiList](arkts-mdm-wifimanager-removeallowedwifilist-f.md#removeallowedwifilist) |
| [removeDisallowedWifiList](arkts-mdm-wifimanager-removedisallowedwifilist-f.md#removedisallowedwifilist) |
| [setWifiProfileSync](arkts-mdm-wifimanager-setwifiprofilesync-f.md#setwifiprofilesync) |
| [turnOffWifi](arkts-mdm-wifimanager-turnoffwifi-f.md#turnoffwifi) |
| [turnOnWifi](arkts-mdm-wifimanager-turnonwifi-f.md#turnonwifi) |

<!--Del-->
### 函数（系统接口）

| 名称 |
| --- |
| [isWifiActive](arkts-mdm-wifimanager-iswifiactive-f-sys.md#iswifiactive系统接口) |
| [isWifiActive](arkts-mdm-wifimanager-iswifiactive-f-sys.md#iswifiactive系统接口) |
| [isWifiDisabled](arkts-mdm-wifimanager-iswifidisabled-f-sys.md#iswifidisabled系统接口) |
| [setWifiDisabled](arkts-mdm-wifimanager-setwifidisabled-f-sys.md#setwifidisabled系统接口) |
| [setWifiProfile](arkts-mdm-wifimanager-setwifiprofile-f-sys.md#setwifiprofile系统接口) |
| [setWifiProfile](arkts-mdm-wifimanager-setwifiprofile-f-sys.md#setwifiprofile系统接口) |
<!--DelEnd-->

### 接口

| 名称 |
| --- |
| [IpProfile](arkts-mdm-wifimanager-ipprofile-i.md) |
| [WifiAccessInfo](arkts-mdm-wifimanager-wifiaccessinfo-i.md) |
| [WifiEapProfile](arkts-mdm-wifimanager-wifieapprofile-i.md) |
| [WifiProfile](arkts-mdm-wifimanager-wifiprofile-i.md) |

### 枚举

| 名称 |
| --- |
| [EapMethod](arkts-mdm-wifimanager-eapmethod-e.md) |
| [IpType](arkts-mdm-wifimanager-iptype-e.md) |
| [Phase2Method](arkts-mdm-wifimanager-phase2method-e.md) |
| [WifiSecurityType](arkts-mdm-wifimanager-wifisecuritytype-e.md) |
