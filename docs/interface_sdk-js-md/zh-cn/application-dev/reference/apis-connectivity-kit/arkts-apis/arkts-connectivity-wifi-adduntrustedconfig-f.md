# addUntrustedConfig

## 导入模块

```TypeScript
import { wifi } from 'kits/@kit.ConnectivityKit';
```

## addUntrustedConfig

```TypeScript
function addUntrustedConfig(config: WifiDeviceConfig): Promise<boolean>
```

添加不可信网络配置，使用Promise异步回调。<p>该方法一次添加一个配置。添加该配置后，设备将决定是否连接到热点。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [addCandidateConfig](arkts-connectivity-wifimanager-addcandidateconfig-f.md)

**需要权限：** ohos.permission.SET_WIFI_INFO

**系统能力：** SystemCapability.Communication.WiFi.STA

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| config | [WifiDeviceConfig](arkts-connectivity-wifi-wifideviceconfig-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;boolean & gt; |


## addUntrustedConfig

```TypeScript
function addUntrustedConfig(config: WifiDeviceConfig, callback: AsyncCallback<boolean>): void
```

添加不可信网络配置，使用callback异步回调。<p>该方法一次添加一个配置。添加该配置后，设备将决定是否连接到热点。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [addCandidateConfig](arkts-connectivity-wifimanager-addcandidateconfig-f.md)

**需要权限：** ohos.permission.SET_WIFI_INFO

**系统能力：** SystemCapability.Communication.WiFi.STA

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| config | [WifiDeviceConfig](arkts-connectivity-wifi-wifideviceconfig-i.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;boolean&gt; | 是 |
