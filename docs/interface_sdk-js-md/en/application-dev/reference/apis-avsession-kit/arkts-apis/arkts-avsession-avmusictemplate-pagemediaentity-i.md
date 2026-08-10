# PageMediaEntity

标签页媒体的定义。继承自[OperResult](arkts-avsession-avmusictemplate-operresult-i.md)。

**Inheritance/Implementation:** PageMediaEntity extends [OperResult](arkts-avsession-avmusictemplate-operresult-i.md)

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-avMusicTemplate-interface PageMediaEntity extends OperResult--><!--Device-avMusicTemplate-interface PageMediaEntity extends OperResult-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVMusicTemplate

## Modules to Import

```TypeScript
import { avMusicTemplate } from 'kits/@kit.AVSessionKit';
```

## elements

```TypeScript
elements: MediaEntity[]
```

查询数据内容（根据类型传递相应的结构数据）。

**Type:** [MediaEntity](arkts-avsession-avmusictemplate-mediaentity-i.md)[]

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PageMediaEntity-elements: MediaEntity[]--><!--Device-PageMediaEntity-elements: MediaEntity[]-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVMusicTemplate

## episodeRange

```TypeScript
episodeRange?: EpisodeRange
```

剧集区间。

**Type:** [EpisodeRange](arkts-avsession-avmusictemplate-episoderange-i.md)

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PageMediaEntity-episodeRange?: EpisodeRange--><!--Device-PageMediaEntity-episodeRange?: EpisodeRange-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVMusicTemplate

## hasMoreData

```TypeScript
hasMoreData: boolean
```

是否有下一页。true表示有，false表示没有。无默认值。

**Type:** boolean

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PageMediaEntity-hasMoreData: boolean--><!--Device-PageMediaEntity-hasMoreData: boolean-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVMusicTemplate

## memberMediaType

```TypeScript
memberMediaType: EntityType
```

媒体资源类型。

**Type:** [EntityType](arkts-avsession-avmusictemplate-entitytype-e.md)

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PageMediaEntity-memberMediaType: EntityType--><!--Device-PageMediaEntity-memberMediaType: EntityType-End-->

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

<!--Device-PageMediaEntity-pageIndex: int--><!--Device-PageMediaEntity-pageIndex: int-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVMusicTemplate

## pageSize

```TypeScript
pageSize: int
```

页面的大小。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PageMediaEntity-pageSize: int--><!--Device-PageMediaEntity-pageSize: int-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVMusicTemplate

## sort

```TypeScript
sort?: Sort
```

数据排序。

**Type:** [Sort](arkts-avsession-avmusictemplate-sort-e.md)

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PageMediaEntity-sort?: Sort--><!--Device-PageMediaEntity-sort?: Sort-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVMusicTemplate

## totalSize

```TypeScript
totalSize: int
```

数据总大小。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PageMediaEntity-totalSize: int--><!--Device-PageMediaEntity-totalSize: int-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVMusicTemplate

