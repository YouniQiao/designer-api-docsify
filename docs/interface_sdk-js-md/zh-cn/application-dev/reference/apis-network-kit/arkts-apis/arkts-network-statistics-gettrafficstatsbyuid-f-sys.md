# getTrafficStatsByUid（系统接口）

## 导入模块

```TypeScript
import { statistics } from 'kits/@kit.NetworkKit';
```

## getTrafficStatsByUid

```TypeScript
function getTrafficStatsByUid(uidInfo: UidInfo, callback: AsyncCallback<NetStatsInfo>): void
```

Get the traffic usage details of the specified time period of the application.

**起始版本：** 10

**ArkTS模式：** ArkTS-Dyn起始版本为10；ArkTS-Sta起始版本为23。

**需要权限：** ohos.permission.GET_NETWORK_STATS

<!--Device-statistics-function getTrafficStatsByUid(uidInfo: UidInfo, callback: AsyncCallback<NetStatsInfo>): void--><!--Device-statistics-function getTrafficStatsByUid(uidInfo: UidInfo, callback: AsyncCallback<NetStatsInfo>): void-End-->

**系统能力：** SystemCapability.Communication.NetManager.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| uidInfo | [UidInfo](arkts-network-statistics-uidinfo-i-sys.md) | 是 | Detailed query content. See {@link UidInfo}. |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;NetStatsInfo&gt; | 是 | Returns the {@link NetStatsInfo} object; |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. |
| 2100001 | Invalid parameter value. |
| 2100002 | Failed to connect to the service. |
| 2100003 | System internal error. |
| 201 | Permission denied. |
| 2103017 | Failed to read the database. |
| 202 | Non-system applications use system APIs. |

## 示例

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { statistics } from '@kit.NetworkKit';

let uidInfo: statistics.UidInfo = {
  uid: 20010037,
  ifaceInfo: {
    iface: '',
    startTime: 1,
    endTime: 3,
  }
}

statistics.getTrafficStatsByUid(
  uidInfo,
  (error: BusinessError, statsInfo: statistics.NetStatsInfo) => {
    console.error(JSON.stringify(error));
    console.info(
      "getTrafficStatsByUid bytes of received = " +
      JSON.stringify(statsInfo.rxBytes)
    );
    console.info(
      "getTrafficStatsByUid bytes of sent = " +
      JSON.stringify(statsInfo.txBytes)
    );
    console.info(
      "getTrafficStatsByUid packets of received = " +
      JSON.stringify(statsInfo.rxPackets)
    );
    console.info(
      "getTrafficStatsByUid packets of sent = " +
      JSON.stringify(statsInfo.txPackets)
    );
  }
);
```


## getTrafficStatsByUid

```TypeScript
function getTrafficStatsByUid(uidInfo: UidInfo): Promise<NetStatsInfo>
```

Get the traffic usage details of the specified time period of the application.

**起始版本：** 10

**ArkTS模式：** ArkTS-Dyn起始版本为10；ArkTS-Sta起始版本为23。

**需要权限：** ohos.permission.GET_NETWORK_STATS

<!--Device-statistics-function getTrafficStatsByUid(uidInfo: UidInfo): Promise<NetStatsInfo>--><!--Device-statistics-function getTrafficStatsByUid(uidInfo: UidInfo): Promise<NetStatsInfo>-End-->

**系统能力：** SystemCapability.Communication.NetManager.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| uidInfo | [UidInfo](arkts-network-statistics-uidinfo-i-sys.md) | 是 | Detailed query content. See {@link UidInfo}. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;NetStatsInfo&gt; | The promise returned by the function. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. |
| 2100001 | Invalid parameter value. |
| 2100002 | Failed to connect to the service. |
| 2100003 | System internal error. |
| 201 | Permission denied. |
| 2103017 | Failed to read the database. |
| 202 | Non-system applications use system APIs. |

## 示例

```TypeScript
import { statistics } from '@kit.NetworkKit';

let uidInfo: statistics.UidInfo = {
  uid: 20010037,
  ifaceInfo: {
    iface: '',
    startTime: 1,
    endTime: 3,
  }
}

statistics.getTrafficStatsByUid(uidInfo).then((statsInfo: statistics.NetStatsInfo) => {
  console.info("getTrafficStatsByUid bytes of received = " + JSON.stringify(statsInfo.rxBytes));
  console.info("getTrafficStatsByUid bytes of sent = " + JSON.stringify(statsInfo.txBytes));
  console.info("getTrafficStatsByUid packets of received = " + JSON.stringify(statsInfo.rxPackets));
  console.info("getTrafficStatsByUid packets of sent = " + JSON.stringify(statsInfo.txPackets));
})
```

