# cloudData(端云服务)

端云服务提供端云协同和端云共享能力。 端云协同提供结构化数据（RDB Store，关系型数据库）端云同步的能力。即：云作为数据的中心节点，通过与云空间的数据同步，实现数据云备份、同账号设备间的数据一致性。 端云共享是在端云协同能力基础上，实现跨账号的数据共享。其中，端云共享资源标识是指：对于应用发起共享的每一条数据记录，该条数据在进行端云同步时会生成唯一的共享资源标识（字符串类型的值），此标识作为该条数据记录共享时的识别标识。 端云共享参与者是指：共享发起者根据好友列表选中的参与当前数据共享的所有人员。 端云共享邀请码是指：共享发起后，在共享的服务端会生成当前共享操作的邀请码，并将该邀请码附加到当前共享邀请中，通过推送消息推送到被邀请者的设备端，被邀请者可以通过该邀请码进行邀请的确认。

**起始版本：** 10

**系统能力：** SystemCapability.DistributedDataManager.CloudSync.Config

## 导入模块

```TypeScript
import { cloudData } from 'kits/@kit.ArkData';
```

## 汇总

### 命名空间

| 名称 |
| --- |
| [sharing(端云服务)](arkts-arkdata-clouddata-sharing-n.md) |

### 函数

| 名称 |
| --- |
| [setCloudStrategy(端云服务)](arkts-arkdata-clouddata-setcloudstrategy-f.md) |
| [onAutoSyncTrigger(端云服务)](arkts-arkdata-clouddata-onautosynctrigger-f.md) |
| [offAutoSyncTrigger(端云服务)](arkts-arkdata-clouddata-offautosynctrigger-f.md) |

<!--Del-->
### 类（系统接口）

| 名称 |
| --- |
| [Config(端云服务)](arkts-arkdata-clouddata-config-c-sys.md) |
<!--DelEnd-->

### 接口

| 名称 |
| --- |
| [AutoSyncTriggerInfo(端云服务)](arkts-arkdata-clouddata-autosynctriggerinfo-i.md) |

<!--Del-->
### 接口（系统接口）

| 名称 |
| --- |
| [ExtraData(端云服务)](arkts-arkdata-clouddata-extradata-i-sys.md) |
| [StatisticInfo(端云服务)](arkts-arkdata-clouddata-statisticinfo-i-sys.md) |
| [SyncInfo(端云服务)](arkts-arkdata-clouddata-syncinfo-i-sys.md) |
| [DBSwitchInfo(端云服务)](arkts-arkdata-clouddata-dbswitchinfo-i-sys.md) |
| [SwitchConfig(端云服务)](arkts-arkdata-clouddata-switchconfig-i-sys.md) |
| [DBActionInfo(端云服务)](arkts-arkdata-clouddata-dbactioninfo-i-sys.md) |
| [ClearConfig(端云服务)](arkts-arkdata-clouddata-clearconfig-i-sys.md) |
| [BundleInfo(端云服务)](arkts-arkdata-clouddata-bundleinfo-i-sys.md) |
<!--DelEnd-->

### 枚举

| 名称 |
| --- |
| [StrategyType(端云服务)](arkts-arkdata-clouddata-strategytype-e.md) |
| [NetWorkStrategy(端云服务)](arkts-arkdata-clouddata-networkstrategy-e.md) |
| [AutoSyncTriggerMode(端云服务)](arkts-arkdata-clouddata-autosynctriggermode-e.md) |

<!--Del-->
### 枚举（系统接口）

| 名称 |
| --- |
| [ClearAction(端云服务)](arkts-arkdata-clouddata-clearaction-e-sys.md) |
| [SyncStatus(端云服务)](arkts-arkdata-clouddata-syncstatus-e-sys.md) |
<!--DelEnd-->

<!--Del-->
### 常量（系统接口）

| 名称 |
| --- |
| [DATA_CHANGE_EVENT_ID(端云服务)](arkts-arkdata-clouddata-con-sys.md#data_change_event_id) |
<!--DelEnd-->
