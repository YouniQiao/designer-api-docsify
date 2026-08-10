# ChangeNotification

数据变更时通知的对象，包括插入的数据、更新的数据、删除的数据和设备ID。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-distributedKVStore-interface ChangeNotification--><!--Device-distributedKVStore-interface ChangeNotification-End-->

**System capability:** SystemCapability.DistributedDataManager.KVStore.Core

## Modules to Import

```TypeScript
import { distributedKVStore } from 'kits/@kit.ArkData';
```

## deleteEntries

```TypeScript
deleteEntries: Entry[]
```

数据删除记录。

**Type:** [Entry](../../apis-arkui/arkts-apis/arkts-arkui-customcomponent-entry-i.md)[]

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ChangeNotification-deleteEntries: Entry[]--><!--Device-ChangeNotification-deleteEntries: Entry[]-End-->

**System capability:** SystemCapability.DistributedDataManager.KVStore.Core

## deviceId

```TypeScript
deviceId: string
```

设备ID，此处为设备UUID。

**Type:** string

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ChangeNotification-deviceId: string--><!--Device-ChangeNotification-deviceId: string-End-->

**System capability:** SystemCapability.DistributedDataManager.KVStore.Core

## insertEntries

```TypeScript
insertEntries: Entry[]
```

数据添加记录。

**Type:** [Entry](../../apis-arkui/arkts-apis/arkts-arkui-customcomponent-entry-i.md)[]

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ChangeNotification-insertEntries: Entry[]--><!--Device-ChangeNotification-insertEntries: Entry[]-End-->

**System capability:** SystemCapability.DistributedDataManager.KVStore.Core

## updateEntries

```TypeScript
updateEntries: Entry[]
```

数据更新记录。

**Type:** [Entry](../../apis-arkui/arkts-apis/arkts-arkui-customcomponent-entry-i.md)[]

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ChangeNotification-updateEntries: Entry[]--><!--Device-ChangeNotification-updateEntries: Entry[]-End-->

**System capability:** SystemCapability.DistributedDataManager.KVStore.Core

