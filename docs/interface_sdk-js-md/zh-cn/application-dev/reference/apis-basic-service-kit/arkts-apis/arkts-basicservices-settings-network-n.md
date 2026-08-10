# network

Provides methods for setting network information, including the data roaming status, HTTP proxy configurations,and preferred networks.

**起始版本：** 7

**ArkTS模式：** ArkTS-Dyn起始版本为7；ArkTS-Sta起始版本为23。

<!--Device-settings-namespace network--><!--Device-settings-namespace network-End-->

**系统能力：** SystemCapability.Applications.Settings.Core

## 导入模块

```TypeScript
import { settings } from 'kits/@kit.BasicServicesKit';
```

## 汇总

### 常量

| 名称 | 说明 |
| --- | --- |
| [DATA_ROAMING_STATUS](arkts-basicservices-network-con.md#data_roaming_status) | Specifies whether data roaming is enabled.  &lt;p&gt;If the value is {@code true}, data roaming is enabled. If the value is {@code false},data roaming is disabled. |
| [HTTP_PROXY_CFG](arkts-basicservices-network-con.md#http_proxy_cfg) | Indicates the host name and port number of the global HTTP proxy.The host name and port number are separated by a colon (:). |
| [NETWORK_PREFERENCE_USAGE](arkts-basicservices-network-con.md#network_preference_usage) | Indicates the user preferences of the network to use. |

