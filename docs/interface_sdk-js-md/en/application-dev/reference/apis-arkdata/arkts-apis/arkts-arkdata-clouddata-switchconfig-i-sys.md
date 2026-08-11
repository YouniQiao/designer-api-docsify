# SwitchConfig (System API)

Defines the switch configuration of a device-cloud synergy database.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-cloudData-interface SwitchConfig--><!--Device-cloudData-interface SwitchConfig-End-->

**System capability:** SystemCapability.DistributedDataManager.CloudSync.Config

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { cloudData } from 'kits/@kit.ArkData';
```

## dbInfo

```TypeScript
dbInfo: Record<string, DBSwitchInfo>
```

Switch configuration information of a database. The key is the database name, and the value is the configuration information of the database.

**Type:** [Record](../../apis-default/arkts-apis/arkts-record-t.md)&lt;string, DBSwitchInfo&gt;

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-SwitchConfig-dbInfo: Record<string, DBSwitchInfo>--><!--Device-SwitchConfig-dbInfo: Record<string, DBSwitchInfo>-End-->

**System capability:** SystemCapability.DistributedDataManager.CloudSync.Config

**System API:** This is a system API.

