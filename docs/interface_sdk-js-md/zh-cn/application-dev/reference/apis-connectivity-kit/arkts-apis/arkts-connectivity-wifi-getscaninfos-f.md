# getScanInfos

## 导入模块

```TypeScript
import { wifi } from 'kits/@kit.ConnectivityKit';
```

## getScanInfos

```TypeScript
function getScanInfos(): Promise<Array<WifiScanInfo>>
```

获取扫描结果，使用Promise异步回调。

**起始版本：** 6

**废弃版本：** 9

**替代接口：** [getScanInfoList](arkts-connectivity-wifimanager-getscaninfolist-f.md)

**需要权限：** ohos.permission.GET_WIFI_INFO and (ohos.permission.GET_WIFI_PEERS_MAC or ohos.permission.LOCATION)

**系统能力：** SystemCapability.Communication.WiFi.STA

**返回值：**

| 类型 |
| --- |
| Promise & lt;Array & lt;WifiScanInfo & gt; & gt; |


## getScanInfos

```TypeScript
function getScanInfos(callback: AsyncCallback<Array<WifiScanInfo>>): void
```

获取扫描结果，使用callback异步回调。

**起始版本：** 6

**废弃版本：** 9

**替代接口：** [getScanInfoList](arkts-connectivity-wifimanager-getscaninfolist-f.md)

**需要权限：** ohos.permission.GET_WIFI_INFO and (ohos.permission.GET_WIFI_PEERS_MAC or ohos.permission.LOCATION)

**系统能力：** SystemCapability.Communication.WiFi.STA

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;WifiScanInfo&gt;&gt; | 是 |
