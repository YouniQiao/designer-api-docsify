# getLinkedInfo

## 导入模块

```TypeScript
import { wifi } from 'kits/@kit.ConnectivityKit';
```

## getLinkedInfo

```TypeScript
function getLinkedInfo(): Promise<WifiLinkedInfo>
```

获取WLAN连接信息。使用Promise异步回调。

**起始版本：** 6

**废弃版本：** 9

**替代接口：** [getLinkedInfo](arkts-connectivity-wifimanager-getlinkedinfo-f.md)

**需要权限：** ohos.permission.GET_WIFI_INFO

**系统能力：** SystemCapability.Communication.WiFi.STA

**返回值：**

| 类型 |
| --- |
| Promise & lt;WifiLinkedInfo & gt; |


## getLinkedInfo

```TypeScript
function getLinkedInfo(callback: AsyncCallback<WifiLinkedInfo>): void
```

获取WLAN连接信息。使用callback异步回调。

**起始版本：** 6

**废弃版本：** 9

**替代接口：** [getLinkedInfo](arkts-connectivity-wifimanager-getlinkedinfo-f.md)

**需要权限：** ohos.permission.GET_WIFI_INFO

**系统能力：** SystemCapability.Communication.WiFi.STA

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;WifiLinkedInfo&gt; | 是 |
