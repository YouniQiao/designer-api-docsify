# getP2pLocalDevice

## 导入模块

```TypeScript
import { wifiManager } from 'kits/@kit.ConnectivityKit';
```

## getP2pLocalDevice

```TypeScript
function getP2pLocalDevice(): Promise<WifiP2pDevice>
```

获取本设备的信息。 如果未获取ohos.permission.GET_WIFI_LOCAL_MAC权限，返回的WifiP2pDevice中的DeviceAddress将设置为"00:00:00:00:00:00"。

**起始版本：** 11

**需要权限：** ohos.permission.GET_WIFI_INFO

**系统能力：** SystemCapability.Communication.WiFi.P2P

**返回值：**

| 类型 |
| --- |
| Promise & lt;WifiP2pDevice & gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [2801000](../errorcode-wifi.md#2801000-p2p模块异常) |


## getP2pLocalDevice

```TypeScript
function getP2pLocalDevice(callback: AsyncCallback<WifiP2pDevice>): void
```

获取本设备的信息。 如果未获取ohos.permission.GET_WIFI_LOCAL_MAC权限，返回的WifiP2pDevice中的DeviceAddress将设置为"00:00:00:00:00:00"。

**起始版本：** 11

**需要权限：** ohos.permission.GET_WIFI_INFO

**系统能力：** SystemCapability.Communication.WiFi.P2P

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;WifiP2pDevice&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [2801000](../errorcode-wifi.md#2801000-p2p模块异常) |
| [2801001](../errorcode-wifi.md#2801001-p2p功能未打开) |
