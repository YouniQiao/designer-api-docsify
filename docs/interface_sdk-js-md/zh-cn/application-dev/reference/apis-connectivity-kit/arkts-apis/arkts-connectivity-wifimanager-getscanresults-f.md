# getScanResults

## 导入模块

```TypeScript
import { wifiManager } from 'kits/@kit.ConnectivityKit';
```

## getScanResults

```TypeScript
function getScanResults(): Promise<Array<WifiScanInfo>>
```

获取扫描结果，使用Promise异步回调。

**起始版本：** 9

**废弃版本：** 10

**替代接口：** [getScanInfoList](arkts-connectivity-wifimanager-getscaninfolist-f.md)

**需要权限：** ohos.permission.GET_WIFI_INFO and (ohos.permission.GET_WIFI_PEERS_MAC or (ohos.permission.LOCATION and ohos.permission.APPROXIMATELY_LOCATION))

**系统能力：** SystemCapability.Communication.WiFi.STA

**返回值：**

| 类型 |
| --- |
| Promise & lt;Array & lt;WifiScanInfo & gt; & gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [2501000](../errorcode-wifi.md#2501000-sta内部异常) |


## getScanResults

```TypeScript
function getScanResults(callback: AsyncCallback<Array<WifiScanInfo>>): void
```

获取扫描结果，使用callback异步回调。

**起始版本：** 9

**废弃版本：** 10

**替代接口：** [getScanInfoList](arkts-connectivity-wifimanager-getscaninfolist-f.md)

**需要权限：** ohos.permission.GET_WIFI_INFO and (ohos.permission.GET_WIFI_PEERS_MAC or (ohos.permission.LOCATION and ohos.permission.APPROXIMATELY_LOCATION))

**系统能力：** SystemCapability.Communication.WiFi.STA

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;WifiScanInfo&gt;&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [2501000](../errorcode-wifi.md#2501000-sta内部异常) |
