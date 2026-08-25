# getCurrentGroup

## 导入模块

```TypeScript
import { wifi } from 'kits/@kit.ConnectivityKit';
```

## getCurrentGroup

```TypeScript
function getCurrentGroup(): Promise<WifiP2pGroupInfo>
```

获取当前群组信息。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [getCurrentGroup](arkts-connectivity-wifimanager-getcurrentgroup-f.md)

**需要权限：** ohos.permission.GET_WIFI_INFO and ohos.permission.LOCATION

**系统能力：** SystemCapability.Communication.WiFi.P2P

**返回值：**

| 类型 |
| --- |
| Promise & lt;WifiP2pGroupInfo & gt; |


## getCurrentGroup

```TypeScript
function getCurrentGroup(callback: AsyncCallback<WifiP2pGroupInfo>): void
```

获取当前群组信息。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [getCurrentGroup](arkts-connectivity-wifimanager-getcurrentgroup-f.md)

**需要权限：** ohos.permission.GET_WIFI_INFO and ohos.permission.LOCATION

**系统能力：** SystemCapability.Communication.WiFi.P2P

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;WifiP2pGroupInfo&gt; | 是 |
