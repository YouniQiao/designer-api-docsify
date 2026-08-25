# @ohos.net.statistics(流量管理)

流量管理模块提供获取设备网络流量数据的能力。该模块支持从多个维度查询数据包的流量使用情况，例如：  
- 支持获取指定网卡的上/下行流量数据； - 支持获取所有网卡的总流量数据，便于查看设备整体网络使用情况； - 支持根据应用uid获取指定应用的流量数据，帮助开发者监控应用的网络资源消耗； - 支持获取指定socket的流量统计，为细粒度的网络性能分析提供数据基础； - 支持获取应用在指定时间段内的历史流量使用情况，便于分析应用的长期网络使用趋势。

> **说明：**&gt;
> 本模块首批接口从 API version 10 开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

**起始版本：** 10

**ArkTS模式：** ArkTS-Dyn起始版本为10；ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Communication.NetManager.Core

## 导入模块

```TypeScript
import { statistics } from '@kit.NetworkKit';
```

## 汇总

### 函数

| 名称 |
| --- |
| [getAllRxBytes(流量管理)](arkts-network-statistics-getallrxbytes-f.md) |
| [getAllRxBytes(流量管理)](arkts-network-statistics-getallrxbytes-f.md) |
| [getAllTxBytes(流量管理)](arkts-network-statistics-getalltxbytes-f.md) |
| [getAllTxBytes(流量管理)](arkts-network-statistics-getalltxbytes-f.md) |
| [getCellularRxBytes(流量管理)](arkts-network-statistics-getcellularrxbytes-f.md) |
| [getCellularRxBytes(流量管理)](arkts-network-statistics-getcellularrxbytes-f.md) |
| [getCellularTxBytes(流量管理)](arkts-network-statistics-getcellulartxbytes-f.md) |
| [getCellularTxBytes(流量管理)](arkts-network-statistics-getcellulartxbytes-f.md) |
| [getIfaceRxBytes(流量管理)](arkts-network-statistics-getifacerxbytes-f.md) |
| [getIfaceRxBytes(流量管理)](arkts-network-statistics-getifacerxbytes-f.md) |
| [getIfaceTxBytes(流量管理)](arkts-network-statistics-getifacetxbytes-f.md) |
| [getIfaceTxBytes(流量管理)](arkts-network-statistics-getifacetxbytes-f.md) |
| [getSelfTrafficStats(流量管理)](arkts-network-statistics-getselftrafficstats-f.md) |
| [getSockfdRxBytes(流量管理)](arkts-network-statistics-getsockfdrxbytes-f.md) |
| [getSockfdRxBytes(流量管理)](arkts-network-statistics-getsockfdrxbytes-f.md) |
| [getSockfdTxBytes(流量管理)](arkts-network-statistics-getsockfdtxbytes-f.md) |
| [getSockfdTxBytes(流量管理)](arkts-network-statistics-getsockfdtxbytes-f.md) |
| [getUidRxBytes(流量管理)](arkts-network-statistics-getuidrxbytes-f.md) |
| [getUidRxBytes(流量管理)](arkts-network-statistics-getuidrxbytes-f.md) |
| [getUidTxBytes(流量管理)](arkts-network-statistics-getuidtxbytes-f.md) |
| [getUidTxBytes(流量管理)](arkts-network-statistics-getuidtxbytes-f.md) |

<!--Del-->
### 函数（系统接口）

| 名称 |
| --- |
| [getMonthTrafficStats(流量管理)](arkts-network-statistics-getmonthtrafficstats-f-sys.md) |
| [getTrafficPlanInfo(流量管理)](arkts-network-statistics-gettrafficplaninfo-f-sys.md) |
| [getTrafficStatsByIface(流量管理)](arkts-network-statistics-gettrafficstatsbyiface-f-sys.md) |
| [getTrafficStatsByIface(流量管理)](arkts-network-statistics-gettrafficstatsbyiface-f-sys.md) | 获取指定网卡历史流量信息，使用 Promise 异步回调。  \| 参数名 \| 类型 \| 必填 \| 说明 \| \| --------- \| ------------------------- \| ---- \| --------------------------------------------------- \| \| ifaceInfo \| [IfaceInfo](arkts-network-statistics-ifaceinfo-i-sys.md) \| 是 \| 指定查询的网卡信息，参见[IfaceInfo](arkts-network-statistics-ifaceinfo-i-sys.md)。 \|
| [getTrafficStatsByNetwork(流量管理)](arkts-network-statistics-gettrafficstatsbynetwork-f-sys.md) |
| [getTrafficStatsByUid(流量管理)](arkts-network-statistics-gettrafficstatsbyuid-f-sys.md) |
| [getTrafficStatsByUid(流量管理)](arkts-network-statistics-gettrafficstatsbyuid-f-sys.md) |
| [getTrafficStatsByUidNetwork(流量管理)](arkts-network-statistics-gettrafficstatsbyuidnetwork-f-sys.md) |
| [off(流量管理)](arkts-network-statistics-off-f-sys.md#offnetstatschange) |
| [offNetStatsChange(流量管理)](arkts-network-statistics-offnetstatschange-f-sys.md) |
| [on(流量管理)](arkts-network-statistics-on-f-sys.md#onnetstatschange) |
| [onNetStatsChange(流量管理)](arkts-network-statistics-onnetstatschange-f-sys.md) |
| [setCalibrationTraffic(流量管理)](arkts-network-statistics-setcalibrationtraffic-f-sys.md) |
| [setTrafficPlanInfo(流量管理)](arkts-network-statistics-settrafficplaninfo-f-sys.md) |
| [updateIfacesStats(流量管理)](arkts-network-statistics-updateifacesstats-f-sys.md) |
| [updateStatsData(流量管理)](arkts-network-statistics-updatestatsdata-f-sys.md) |
<!--DelEnd-->

### 接口

| 名称 |
| --- |
| [NetStatsInfo(流量管理)](arkts-network-statistics-netstatsinfo-i.md) |
| [NetworkInfo(流量管理)](arkts-network-statistics-networkinfo-i.md) |

<!--Del-->
### 接口（系统接口）

| 名称 |
| --- |
| [IfaceInfo(流量管理)](arkts-network-statistics-ifaceinfo-i-sys.md) |
| [NetStatsChangeInfo(流量管理)](arkts-network-statistics-netstatschangeinfo-i-sys.md) |
| [NetStatsInfoSequenceItem(流量管理)](arkts-network-statistics-netstatsinfosequenceitem-i-sys.md) |
| [UidInfo(流量管理)](arkts-network-statistics-uidinfo-i-sys.md) |
<!--DelEnd-->

<!--Del-->
### 枚举（系统接口）

| 名称 |
| --- |
| [TrafficPlanParam(流量管理)](arkts-network-statistics-trafficplanparam-e-sys.md) |
<!--DelEnd-->

### 类型

| 名称 |
| --- |
| [NetBearType(流量管理)](arkts-network-statistics-netbeartype-t.md) |

<!--Del-->
### 类型（系统接口）

| 名称 |
| --- |
| [NetStatsInfoSequence(流量管理)](arkts-network-statistics-netstatsinfosequence-t-sys.md) |
| [UidNetStatsInfo(流量管理)](arkts-network-statistics-uidnetstatsinfo-t-sys.md) |
<!--DelEnd-->
