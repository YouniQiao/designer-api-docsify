# getTrafficStatsByIface (System API)

## Modules to Import

```TypeScript
import { statistics } from 'statistics';
```

## getTrafficStatsByIface

```TypeScript
function getTrafficStatsByIface(ifaceInfo: IfaceInfo, callback: AsyncCallback<NetStatsInfo>): void
```

Get the traffic usage details of the network interface in the specified time period.

**Since:** 23

**Required permissions:** ohos.permission.GET_NETWORK_STATS

<!--Device-statistics-function getTrafficStatsByIface(ifaceInfo: IfaceInfo, callback: AsyncCallback<NetStatsInfo>): void--><!--Device-statistics-function getTrafficStatsByIface(ifaceInfo: IfaceInfo, callback: AsyncCallback<NetStatsInfo>): void-End-->

**System capability:** SystemCapability.Communication.NetManager.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| ifaceInfo | [IfaceInfo](arkts-network-statistics-ifaceinfo-i-sys.md) | Yes | Detailed query content. See [IfaceInfo](arkts-network-statistics-ifaceinfo-i-sys.md#ifaceinfo-system-api). |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[NetStatsInfo](arkts-network-statistics-netstatsinfo-i.md)&gt; | Yes | Returns the [NetStatsInfo](arkts-network-statistics-netstatsinfo-i.md#netstatsinfo) object; |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. |
| [2100001](../errorcode-net-connection.md#2100001-invalid-parameter-value) | Invalid parameter value. |
| [2100002](../errorcode-net-connection.md#2100002-service-connection-failure) | Failed to connect to the service. |
| [2100003](../errorcode-net-connection.md#2100003-system-internal-error) | System internal error. |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. |
| [2103017](../errorcode-net-statistics.md#2103017-failed-to-read-the-database) | Failed to read the database. |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Non-system applications use system APIs. |

**Examples**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { statistics } from '@kit.NetworkKit';

let iFaceInfo: statistics.IfaceInfo | null = null;
if (iFaceInfo) {
  statistics.getTrafficStatsByIface(iFaceInfo as statistics.IfaceInfo, (error: BusinessError, statsInfo: statistics.NetStatsInfo) => {
    console.error(JSON.stringify(error));
    console.info(
      "getTrafficStatsByIface bytes of received = " +
      JSON.stringify(statsInfo.rxBytes)
    );
    console.info(
      "getTrafficStatsByIface bytes of sent = " +
      JSON.stringify(statsInfo.txBytes)
    );
    console.info(
      "getTrafficStatsByIface packets of received = " +
      JSON.stringify(statsInfo.rxPackets)
    );
    console.info(
      "getTrafficStatsByIface packets of sent = " +
      JSON.stringify(statsInfo.txPackets)
    );
  });
}
```


## getTrafficStatsByIface

```TypeScript
function getTrafficStatsByIface(ifaceInfo: IfaceInfo): Promise<NetStatsInfo>
```

Get the traffic usage details of the network interface in the specified time period.

**Since:** 23

**Required permissions:** ohos.permission.GET_NETWORK_STATS

<!--Device-statistics-function getTrafficStatsByIface(ifaceInfo: IfaceInfo): Promise<NetStatsInfo>--><!--Device-statistics-function getTrafficStatsByIface(ifaceInfo: IfaceInfo): Promise<NetStatsInfo>-End-->

**System capability:** SystemCapability.Communication.NetManager.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| ifaceInfo | [IfaceInfo](arkts-network-statistics-ifaceinfo-i-sys.md) | Yes | Detailed query content. See [IfaceInfo](arkts-network-statistics-ifaceinfo-i-sys.md#ifaceinfo-system-api). |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;[NetStatsInfo](arkts-network-statistics-netstatsinfo-i.md)&gt; | The promise returned by the function. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. |
| [2100001](../errorcode-net-connection.md#2100001-invalid-parameter-value) | Invalid parameter value. |
| [2100002](../errorcode-net-connection.md#2100002-service-connection-failure) | Failed to connect to the service. |
| [2100003](../errorcode-net-connection.md#2100003-system-internal-error) | System internal error. |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. |
| [2103017](../errorcode-net-statistics.md#2103017-failed-to-read-the-database) | Failed to read the database. |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Non-system applications use system APIs. |

**Examples**

```TypeScript
import { statistics } from '@kit.NetworkKit';

let iFaceInfo: statistics.IfaceInfo | null = null;
if (iFaceInfo) {
  statistics.getTrafficStatsByIface(iFaceInfo as statistics.IfaceInfo).then((statsInfo: statistics.NetStatsInfo) => {
    console.info(
      "getTrafficStatsByIface bytes of received = " +
      JSON.stringify(statsInfo.rxBytes)
    );
    console.info(
      "getTrafficStatsByIface bytes of sent = " +
      JSON.stringify(statsInfo.txBytes)
    );
    console.info(
      "getTrafficStatsByIface packets of received = " +
      JSON.stringify(statsInfo.rxPackets)
    );
    console.info(
      "getTrafficStatsByIface packets of sent = " +
      JSON.stringify(statsInfo.txPackets)
    );
  });
}
```

