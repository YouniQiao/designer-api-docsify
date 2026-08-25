# @ohos.enterprise.wifiManager(Wi-Fi管理)

本模块提供企业设备Wi-Fi管理能力，包括查询Wi-Fi开启状态、配置Wi-Fi连接、管理Wi-Fi名单等。  
**使用场景**：  
- 企业设备批量配置Wi-Fi连接，简化设备初始化流程  
- 控制设备可连接的Wi-Fi网络，实现网络访问合规管理  
- 管理企业设备的Wi-Fi开关，统一网络策略  
**功能收益**：  
- 提高企业网络管理效率，减少IT运维成本  
- 确保设备仅连接安全的Wi-Fi网络，降低安全风险  
- 实现网络策略统一管控，满足企业合规要求

> **说明：**&gt;
> 本模块接口仅对设备管理应用开放，且调用接口前需激活设备管理应用，具体请参考[MDM Kit开发指南](../../../mdm/mdm-kit-guide.md)。&gt;
> 全局通用限制类策略由restrictions统一提供，若要全局禁用Wi-Fi，请参考
> [@ohos.enterprise.restrictions（限制类策略）](arkts-enterprise-restrictions.md)。

**起始版本：** 12

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

## 导入模块

```TypeScript
import { wifiManager } from 'kits/@kit.MDMKit';
```

## 汇总

### 函数

| 名称 |
| --- |
| [addAllowedWifiList(Wi-Fi管理)](arkts-mdm-wifimanager-addallowedwifilist-f.md) |
| [addDisallowedWifiList(Wi-Fi管理)](arkts-mdm-wifimanager-adddisallowedwifilist-f.md) |
| [getAllowedWifiList(Wi-Fi管理)](arkts-mdm-wifimanager-getallowedwifilist-f.md) |
| [getAllowedWifiList(Wi-Fi管理)](arkts-mdm-wifimanager-getallowedwifilist-f.md) |
| [getDisallowedWifiList(Wi-Fi管理)](arkts-mdm-wifimanager-getdisallowedwifilist-f.md) |
| [getDisallowedWifiList(Wi-Fi管理)](arkts-mdm-wifimanager-getdisallowedwifilist-f.md) |
| [isWifiActiveSync(Wi-Fi管理)](arkts-mdm-wifimanager-iswifiactivesync-f.md) |
| [removeAllowedWifiList(Wi-Fi管理)](arkts-mdm-wifimanager-removeallowedwifilist-f.md) |
| [removeDisallowedWifiList(Wi-Fi管理)](arkts-mdm-wifimanager-removedisallowedwifilist-f.md) |
| [setWifiProfileSync(Wi-Fi管理)](arkts-mdm-wifimanager-setwifiprofilesync-f.md) |
| [turnOffWifi(Wi-Fi管理)](arkts-mdm-wifimanager-turnoffwifi-f.md) |
| [turnOnWifi(Wi-Fi管理)](arkts-mdm-wifimanager-turnonwifi-f.md) |

<!--Del-->
### 函数（系统接口）

| 名称 |
| --- |
| [isWifiActive(Wi-Fi管理)](arkts-mdm-wifimanager-iswifiactive-f-sys.md) |
| [isWifiActive(Wi-Fi管理)](arkts-mdm-wifimanager-iswifiactive-f-sys.md) |
| [isWifiDisabled(Wi-Fi管理)](arkts-mdm-wifimanager-iswifidisabled-f-sys.md) |
| [setWifiDisabled(Wi-Fi管理)](arkts-mdm-wifimanager-setwifidisabled-f-sys.md) |
| [setWifiProfile(Wi-Fi管理)](arkts-mdm-wifimanager-setwifiprofile-f-sys.md) |
| [setWifiProfile(Wi-Fi管理)](arkts-mdm-wifimanager-setwifiprofile-f-sys.md) |
<!--DelEnd-->

### 接口

| 名称 |
| --- |
| [IpProfile(Wi-Fi管理)](arkts-mdm-wifimanager-ipprofile-i.md) |
| [WifiAccessInfo(Wi-Fi管理)](arkts-mdm-wifimanager-wifiaccessinfo-i.md) |
| [WifiEapProfile(Wi-Fi管理)](arkts-mdm-wifimanager-wifieapprofile-i.md) |
| [WifiProfile(Wi-Fi管理)](arkts-mdm-wifimanager-wifiprofile-i.md) |

### 枚举

| 名称 |
| --- |
| [EapMethod(Wi-Fi管理)](arkts-mdm-wifimanager-eapmethod-e.md) |
| [IpType(Wi-Fi管理)](arkts-mdm-wifimanager-iptype-e.md) |
| [Phase2Method(Wi-Fi管理)](arkts-mdm-wifimanager-phase2method-e.md) |
| [WifiSecurityType(Wi-Fi管理)](arkts-mdm-wifimanager-wifisecuritytype-e.md) |
