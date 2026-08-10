# DistributedField (System API)

用于谓词查询条件的特殊字段。请使用枚举名称而非枚举值。

**Since:** 24

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 24.

<!--Device-relationalStore-enum DistributedField--><!--Device-relationalStore-enum DistributedField-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

**System API:** This is a system API.

## ORIGIN

```TypeScript
ORIGIN = '#_origin'
```

用于查找或更新时指定数据来源的字段名。

**Since:** 24

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DistributedField-ORIGIN = '#_origin'--><!--Device-DistributedField-ORIGIN = '#_origin'-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

**System API:** This is a system API.

## ORIGIN_ORIDEVICE

```TypeScript
ORIGIN_ORIDEVICE = '#_ori_device'
```

用于查找或更新时指定数据产生者的设备id，该值传入若为空，则表示本地设备；若不为空，则表示其他组网设备。

**Since:** 24

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DistributedField-ORIGIN_ORIDEVICE = '#_ori_device'--><!--Device-DistributedField-ORIGIN_ORIDEVICE = '#_ori_device'-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

**System API:** This is a system API.

## CURSOR_FIELD

```TypeScript
CURSOR_FIELD = '#_cursor'
```

用于cursor查找的字段名。

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DistributedField-CURSOR_FIELD = '#_cursor'--><!--Device-DistributedField-CURSOR_FIELD = '#_cursor'-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

**System API:** This is a system API.

## DELETED_FLAG_FIELD

```TypeScript
DELETED_FLAG_FIELD = '#_deleted_flag'
```

用于cursor查找的结果集返回时填充的字段。true表示对端删除的数据，同步到本端。false表示对端写入或更新的数据，同步到本端；或者本端写入或更新的数据。

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DistributedField-DELETED_FLAG_FIELD = '#_deleted_flag'--><!--Device-DistributedField-DELETED_FLAG_FIELD = '#_deleted_flag'-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

**System API:** This is a system API.

