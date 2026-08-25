# UidNetStatsInfo（系统接口）

```TypeScript
export type UidNetStatsInfo = Record<int, NetStatsInfo>
```

[NetStatsInfo](arkts-network-statistics-netstatsinfo-i.md) for every UID. Key is UID. [NetStatsInfo](arkts-network-statistics-netstatsinfo-i.md) for every UID. Key is UID.

**起始版本：** 12

**ArkTS模式：** ArkTS-Dyn起始版本为12；ArkTS-Sta起始版本为23。

**系统能力：** 
- SystemCapability.Communication.NetManager.Core {
- SystemCapability.Communication.NetManager.Core

**系统接口：** 此接口为系统接口。

**属性类型：** ArkTS-Dyn: Record&lt;number, [NetStatsInfo](arkts-network-statistics-netstatsinfo-i.md)&gt;  <br>ArkTS-Sta：Record&lt;int, [NetStatsInfo](arkts-network-statistics-netstatsinfo-i.md)&gt;
