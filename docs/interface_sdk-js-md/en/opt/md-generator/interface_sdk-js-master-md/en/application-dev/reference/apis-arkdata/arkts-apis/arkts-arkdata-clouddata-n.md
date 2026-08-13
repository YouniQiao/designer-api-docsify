# cloudData

The **cloudData** module provides APIs for implementing device-cloud synergy and device-cloud sharing, and setting the device-cloud sync strategy. Device-cloud synergy enables sync of the structured data (in RDB stores) between devices and the cloud. The cloud serves as a data hub to implement data backup in the cloud and data consistency between the devices with the same account. This module also provides the capability of setting the device-cloud sync strategy.

**Since:** 23

**Deprecated since:** -1

<!--Device-unnamed-declare namespace cloudData--><!--Device-unnamed-declare namespace cloudData-End-->

**System capability:** SystemCapability.DistributedDataManager.CloudSync.Config

## Modules to Import

```TypeScript
import { cloudData } from '@kit.ArkData';
```

## Summary

### Namespaces

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [sharing](arkts-arkdata-clouddata-sharing-n.md) |

### Functions

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [setCloudStrategy](arkts-arkdata-clouddata-setcloudstrategy-f.md#setCloudStrategy) |
| [onAutoSyncTrigger](arkts-arkdata-clouddata-onautosynctrigger-f.md#onAutoSyncTrigger) |
| [offAutoSyncTrigger](arkts-arkdata-clouddata-offautosynctrigger-f.md#offAutoSyncTrigger) |

<!--Del-->
### Classes（系统接口）

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [Config](arkts-arkdata-clouddata-config-c-sys.md) |
<!--DelEnd-->

### Interfaces

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [AutoSyncTriggerInfo](arkts-arkdata-clouddata-autosynctriggerinfo-i.md) |

<!--Del-->
### Interfaces（系统接口）

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [ExtraData](arkts-arkdata-clouddata-extradata-i-sys.md) |
| [StatisticInfo](arkts-arkdata-clouddata-statisticinfo-i-sys.md) |
| [SyncInfo](arkts-arkdata-clouddata-syncinfo-i-sys.md) |
| [DBSwitchInfo](arkts-arkdata-clouddata-dbswitchinfo-i-sys.md) |
| [SwitchConfig](arkts-arkdata-clouddata-switchconfig-i-sys.md) |
| [DBActionInfo](arkts-arkdata-clouddata-dbactioninfo-i-sys.md) |
| [ClearConfig](arkts-arkdata-clouddata-clearconfig-i-sys.md) |
| [BundleInfo](arkts-arkdata-clouddata-bundleinfo-i-sys.md) |
<!--DelEnd-->

### Enums

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [StrategyType](arkts-arkdata-clouddata-strategytype-e.md) |
| [NetWorkStrategy](arkts-arkdata-clouddata-networkstrategy-e.md) |
| [AutoSyncTriggerMode](arkts-arkdata-clouddata-autosynctriggermode-e.md) |

<!--Del-->
### Enums（系统接口）

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [ClearAction](arkts-arkdata-clouddata-clearaction-e-sys.md) |
| [SyncStatus](arkts-arkdata-clouddata-syncstatus-e-sys.md) |
<!--DelEnd-->

<!--Del-->
### Constants（系统接口）

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [DATA_CHANGE_EVENT_ID](arkts-arkdata-clouddata-con-sys.md#DATA_CHANGE_EVENT_ID) |
<!--DelEnd-->
