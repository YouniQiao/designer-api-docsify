# QueryMediaEntityParam

查询媒体实例参数的定义。

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-avMusicTemplate-interface QueryMediaEntityParam--><!--Device-avMusicTemplate-interface QueryMediaEntityParam-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVMusicTemplate

## Modules to Import

```TypeScript
import { avMusicTemplate } from 'kits/@kit.AVSessionKit';
```

## entityId

```TypeScript
entityId: string
```

媒体实例的ID。

**Type:** string

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-QueryMediaEntityParam-entityId: string--><!--Device-QueryMediaEntityParam-entityId: string-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVMusicTemplate

## episodeRange

```TypeScript
episodeRange?: EpisodeRange
```

要查询的剧集区间。

**Type:** [EpisodeRange](arkts-avsession-avmusictemplate-episoderange-i.md)

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-QueryMediaEntityParam-episodeRange?: EpisodeRange--><!--Device-QueryMediaEntityParam-episodeRange?: EpisodeRange-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVMusicTemplate

## pageIndex

```TypeScript
pageIndex: int
```

分页查询页码。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-QueryMediaEntityParam-pageIndex: int--><!--Device-QueryMediaEntityParam-pageIndex: int-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVMusicTemplate

## sort

```TypeScript
sort?: Sort
```

查询到的列表数据排序。

**Type:** [Sort](arkts-avsession-avmusictemplate-sort-e.md)

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-QueryMediaEntityParam-sort?: Sort--><!--Device-QueryMediaEntityParam-sort?: Sort-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVMusicTemplate

## subEntityType

```TypeScript
subEntityType?: EntityType
```

子节点的媒体资源类型。

**Type:** [EntityType](arkts-avsession-avmusictemplate-entitytype-e.md)

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-QueryMediaEntityParam-subEntityType?: EntityType--><!--Device-QueryMediaEntityParam-subEntityType?: EntityType-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVMusicTemplate

## type

```TypeScript
type: EntityType
```

媒体资源类型。

**Type:** [EntityType](arkts-avsession-avmusictemplate-entitytype-e.md)

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-QueryMediaEntityParam-type: EntityType--><!--Device-QueryMediaEntityParam-type: EntityType-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVMusicTemplate

