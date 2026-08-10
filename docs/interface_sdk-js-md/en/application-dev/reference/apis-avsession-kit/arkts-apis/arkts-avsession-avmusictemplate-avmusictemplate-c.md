# AVMusicTemplate

调用[avMusicTemplate.createAVMusicTemplate](arkts-avsession-avmusictemplate-createavmusictemplate-f.md#createavmusictemplate)获取实例后，可获取其ID，启动音频模板界面，并配置数据获取方法。随后，同步数据给模板控制方，以完成后续操作。

> **说明：**
> 
> - 本模块仅适用于API version 23及以上版本的Car设备。

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-avMusicTemplate-class AVMusicTemplate--><!--Device-avMusicTemplate-class AVMusicTemplate-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVMusicTemplate

## Modules to Import

```TypeScript
import { avMusicTemplate } from 'kits/@kit.AVSessionKit';
```

## destroy

```TypeScript
destroy(): Promise<void>
```

销毁音频模板实例。使用Promise异步回调。

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AVMusicTemplate-destroy(): Promise<void>--><!--Device-AVMusicTemplate-destroy(): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise对象，无返回结果。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 801 | Capability not supported.function destroy can not work correctly due to limited device capabilities. |

## offClearSearchHistory

```TypeScript
offClearSearchHistory(callback?: ClearSearchHistoryEvent): void
```

注销清除搜索历史的监听。

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AVMusicTemplate-offClearSearchHistory(callback?: ClearSearchHistoryEvent): void--><!--Device-AVMusicTemplate-offClearSearchHistory(callback?: ClearSearchHistoryEvent): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [ClearSearchHistoryEvent](arkts-avsession-avmusictemplate-clearsearchhistoryevent-t.md) | No | 清除搜索历史的事件。不填该参数则注销该类型对应的所有回调。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 801 | Capability not supported.function offClearSearchHistory can not work correctly due to limited device capabilities. |
| 35000005 | AVMusicTemplate does not exist. |
| 35000012 | AVMusicTemplate error. |

## offDownloadMediaEntity

```TypeScript
offDownloadMediaEntity(callback?: DownloadMediaEntityEvent): void
```

注销下载媒体实体事件的监听。

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AVMusicTemplate-offDownloadMediaEntity(callback?: DownloadMediaEntityEvent): void--><!--Device-AVMusicTemplate-offDownloadMediaEntity(callback?: DownloadMediaEntityEvent): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [DownloadMediaEntityEvent](arkts-avsession-avmusictemplate-downloadmediaentityevent-t.md) | No | 下载媒体实体的事件。不填该参数则注销该类型对应的所有回调。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 801 | Capability not supported.function offDownloadMediaEntity can not work correctly due to limited device capabilities. |
| 35000005 | AVMusicTemplate does not exist. |
| 35000012 | AVMusicTemplate error. |

## offExecuteAction

```TypeScript
offExecuteAction(callback?: ExecuteActionEvent): void
```

注销执行操作事件的监听。

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AVMusicTemplate-offExecuteAction(callback?: ExecuteActionEvent): void--><!--Device-AVMusicTemplate-offExecuteAction(callback?: ExecuteActionEvent): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [ExecuteActionEvent](arkts-avsession-avmusictemplate-executeactionevent-t.md) | No | 执行操作的事件。不填该参数则注销该类型对应的所有回调。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 801 | Capability not supported.function offExecuteAction can not work correctly due to limited device capabilities. |
| 35000005 | AVMusicTemplate does not exist. |
| 35000012 | AVMusicTemplate error. |

## offFavoriteMediaEntity

```TypeScript
offFavoriteMediaEntity(callback?: FavoriteMediaEntityEvent): void
```

注销收藏媒体实体事件的监听。

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AVMusicTemplate-offFavoriteMediaEntity(callback?: FavoriteMediaEntityEvent): void--><!--Device-AVMusicTemplate-offFavoriteMediaEntity(callback?: FavoriteMediaEntityEvent): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [FavoriteMediaEntityEvent](arkts-avsession-avmusictemplate-favoritemediaentityevent-t.md) | No | 收藏媒体实体的事件。不填该参数则注销该类型对应的所有回调。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 801 | Capability not supported.function offFavoriteMediaEntity can not work correctly due to limited device capabilities. |
| 35000005 | AVMusicTemplate does not exist. |
| 35000012 | AVMusicTemplate error. |

## offHandleMemberPurchase

```TypeScript
offHandleMemberPurchase(callback?: HandleMemberPurchaseEvent): void
```

注销处理购买会员事件的监听。

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AVMusicTemplate-offHandleMemberPurchase(callback?: HandleMemberPurchaseEvent): void--><!--Device-AVMusicTemplate-offHandleMemberPurchase(callback?: HandleMemberPurchaseEvent): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [HandleMemberPurchaseEvent](arkts-avsession-avmusictemplate-handlememberpurchaseevent-t.md) | No | 处理购买会员的事件。不填该参数则注销该类型对应的所有回调。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 801 | Capability not supported.function offHandleMemberPurchase can not work correctly due to limited device capabilities. |
| 35000005 | AVMusicTemplate does not exist. |
| 35000012 | AVMusicTemplate error. |

## offLogin

```TypeScript
offLogin(callback?: LoginEvent): void
```

注销登录事件的监听。

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AVMusicTemplate-offLogin(callback?: LoginEvent): void--><!--Device-AVMusicTemplate-offLogin(callback?: LoginEvent): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [LoginEvent](arkts-avsession-avmusictemplate-loginevent-t.md) | No | 登录事件。不填该参数则注销该类型对应的所有回调。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 801 | Capability not supported.function offLogin can not work correctly due to limited device capabilities. |
| 35000005 | AVMusicTemplate does not exist. |
| 35000012 | AVMusicTemplate error. |

## offPlayForSearch

```TypeScript
offPlayForSearch(callback?: PlayForSearchEvent): void
```

注销搜播事件的监听。

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AVMusicTemplate-offPlayForSearch(callback?: PlayForSearchEvent): void--><!--Device-AVMusicTemplate-offPlayForSearch(callback?: PlayForSearchEvent): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [PlayForSearchEvent](arkts-avsession-avmusictemplate-playforsearchevent-t.md) | No | 搜播的事件。不填该参数则注销该类型对应的所有回调。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 801 | Capability not supported.function offPlayForSearch can not work correctly due to limited device capabilities. |
| 35000005 | AVMusicTemplate does not exist. |
| 35000012 | AVMusicTemplate error. |

## offPlayMediaEntity

```TypeScript
offPlayMediaEntity(callback?: PlayMediaEntityEvent): void
```

注销播放媒体实体事件的监听。

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AVMusicTemplate-offPlayMediaEntity(callback?: PlayMediaEntityEvent): void--><!--Device-AVMusicTemplate-offPlayMediaEntity(callback?: PlayMediaEntityEvent): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [PlayMediaEntityEvent](arkts-avsession-avmusictemplate-playmediaentityevent-t.md) | No | 播放媒体实体的事件。不填该参数则注销该类型对应的所有回调。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 801 | Capability not supported.function offPlayMediaEntity can not work correctly due to limited device capabilities. |
| 35000005 | AVMusicTemplate does not exist. |
| 35000012 | AVMusicTemplate error. |

## offProblemAndAdvice

```TypeScript
offProblemAndAdvice(callback?: ProblemAndAdviceEvent): void
```

注销问题与建议事件的监听。

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AVMusicTemplate-offProblemAndAdvice(callback?: ProblemAndAdviceEvent): void--><!--Device-AVMusicTemplate-offProblemAndAdvice(callback?: ProblemAndAdviceEvent): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [ProblemAndAdviceEvent](arkts-avsession-avmusictemplate-problemandadviceevent-t.md) | No | 处理问题与建议的回调。不填该参数则注销该类型对应的所有回调。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 801 | Capability not supported.function offProblemAndAdvice can not work correctly due to limited device capabilities. |
| 35000005 | AVMusicTemplate does not exist. |
| 35000012 | AVMusicTemplate error. |

## offQueryCompilation

```TypeScript
offQueryCompilation(callback?: QueryCompilationEvent): void
```

注销查询合集的监听。

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AVMusicTemplate-offQueryCompilation(callback?: QueryCompilationEvent): void--><!--Device-AVMusicTemplate-offQueryCompilation(callback?: QueryCompilationEvent): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [QueryCompilationEvent](arkts-avsession-avmusictemplate-querycompilationevent-t.md) | No | 查询合集的事件。不填该参数则注销该类型对应的所有回调。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 801 | Capability not supported.function offQueryCompilation can not work correctly due to limited device capabilities. |
| 35000005 | AVMusicTemplate does not exist. |
| 35000012 | AVMusicTemplate error. |

## offQueryCompilationByKeyword

```TypeScript
offQueryCompilationByKeyword(callback?: QueryCompilationByKeywordEvent): void
```

注销按关键字查询合集的监听。

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AVMusicTemplate-offQueryCompilationByKeyword(callback?: QueryCompilationByKeywordEvent): void--><!--Device-AVMusicTemplate-offQueryCompilationByKeyword(callback?: QueryCompilationByKeywordEvent): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [QueryCompilationByKeywordEvent](arkts-avsession-avmusictemplate-querycompilationbykeywordevent-t.md) | No | 按关键字查询合集的事件。不填该参数则注销该类型对应的所有回调。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 801 | Capability not supported.function offQueryCompilationByKeyword can not work correctly due to limited device capabilities. |
| 35000005 | AVMusicTemplate does not exist. |
| 35000012 | AVMusicTemplate error. |

## offQueryCurrentSingle

```TypeScript
offQueryCurrentSingle(callback?: QueryCurrentSingleEvent): void
```

注销查询当前单曲的监听。

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AVMusicTemplate-offQueryCurrentSingle(callback?: QueryCurrentSingleEvent): void--><!--Device-AVMusicTemplate-offQueryCurrentSingle(callback?: QueryCurrentSingleEvent): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [QueryCurrentSingleEvent](arkts-avsession-avmusictemplate-querycurrentsingleevent-t.md) | No | 查询当前单曲的事件。不填该参数则注销该类型对应的所有回调。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 801 | Capability not supported.function offQueryCurrentSingle can not work correctly due to limited device capabilities. |
| 35000005 | AVMusicTemplate does not exist. |
| 35000012 | AVMusicTemplate error. |

## offQueryCustomContent

```TypeScript
offQueryCustomContent(callback?: QueryCustomContentEvent): void
```

注销查询自定义内容事件的监听。

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AVMusicTemplate-offQueryCustomContent(callback?: QueryCustomContentEvent): void--><!--Device-AVMusicTemplate-offQueryCustomContent(callback?: QueryCustomContentEvent): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [QueryCustomContentEvent](arkts-avsession-avmusictemplate-querycustomcontentevent-t.md) | No | 查询自定义内容的事件。不填该参数则注销该类型对应的所有回调。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 801 | Capability not supported.function offQueryCustomContent can not work correctly due to limited device capabilities. |
| 35000005 | AVMusicTemplate does not exist. |
| 35000012 | AVMusicTemplate error. |

## offQueryHotWords

```TypeScript
offQueryHotWords(callback?: QueryHotWordsEvent): void
```

注销查询热词的监听。

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AVMusicTemplate-offQueryHotWords(callback?: QueryHotWordsEvent): void--><!--Device-AVMusicTemplate-offQueryHotWords(callback?: QueryHotWordsEvent): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [QueryHotWordsEvent](arkts-avsession-avmusictemplate-queryhotwordsevent-t.md) | No | 查询热词的事件。不填该参数则注销该类型对应的所有回调。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 801 | Capability not supported.function offQueryHotWords can not work correctly due to limited device capabilities. |
| 35000005 | AVMusicTemplate does not exist. |
| 35000012 | AVMusicTemplate error. |

## offQueryMainTabs

```TypeScript
offQueryMainTabs(callback?: QueryMainTabsEvent): void
```

注销查询主标签事件监听。

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AVMusicTemplate-offQueryMainTabs(callback?: QueryMainTabsEvent): void--><!--Device-AVMusicTemplate-offQueryMainTabs(callback?: QueryMainTabsEvent): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [QueryMainTabsEvent](arkts-avsession-avmusictemplate-querymaintabsevent-t.md) | No | 查询主标签事件。不填该参数则注销该类型对应的所有回调。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 801 | Capability not supported.function offQueryMainTabs can not work correctly due to limited device capabilities. |
| 35000005 | AVMusicTemplate does not exist. |
| 35000012 | AVMusicTemplate error. |

## offQueryMediaEntity

```TypeScript
offQueryMediaEntity(callback?: QueryMediaEntityEvent): void
```

注销查询媒体实体监听。

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AVMusicTemplate-offQueryMediaEntity(callback?: QueryMediaEntityEvent): void--><!--Device-AVMusicTemplate-offQueryMediaEntity(callback?: QueryMediaEntityEvent): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [QueryMediaEntityEvent](arkts-avsession-avmusictemplate-querymediaentityevent-t.md) | No | 查询媒体实体的事件。不填该参数则注销该类型对应的所有回调。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 801 | Capability not supported.function offQueryMediaEntity can not work correctly due to limited device capabilities. |
| 35000005 | AVMusicTemplate does not exist. |
| 35000012 | AVMusicTemplate error. |

## offQueryMediaEntityByKeyword

```TypeScript
offQueryMediaEntityByKeyword(callback?: QueryMediaEntityByKeywordEvent): void
```

注销按关键字查询媒体实体的监听。

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AVMusicTemplate-offQueryMediaEntityByKeyword(callback?: QueryMediaEntityByKeywordEvent): void--><!--Device-AVMusicTemplate-offQueryMediaEntityByKeyword(callback?: QueryMediaEntityByKeywordEvent): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [QueryMediaEntityByKeywordEvent](arkts-avsession-avmusictemplate-querymediaentitybykeywordevent-t.md) | No | 按关键字查询媒体实体的事件。不填该参数则注销该类型对应的所有回调。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 801 | Capability not supported.function offQueryMediaEntityByKeyword can not work correctly due to limited device capabilities. |
| 35000005 | AVMusicTemplate does not exist. |
| 35000012 | AVMusicTemplate error. |

## offQueryMediaTabContent

```TypeScript
offQueryMediaTabContent(callback?: QueryMediaTabContentEvent): void
```

取消查询媒体标签内容监听。

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AVMusicTemplate-offQueryMediaTabContent(callback?: QueryMediaTabContentEvent): void--><!--Device-AVMusicTemplate-offQueryMediaTabContent(callback?: QueryMediaTabContentEvent): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [QueryMediaTabContentEvent](arkts-avsession-avmusictemplate-querymediatabcontentevent-t.md) | No | 查询媒体标签页内容的事件。不填该参数则注销该类型对应的所有回调。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 801 | Capability not supported.function offQueryMediaTabContent can not work correctly due to limited device capabilities. |
| 35000005 | AVMusicTemplate does not exist. |
| 35000012 | AVMusicTemplate error. |

## offQueryMemberPurchase

```TypeScript
offQueryMemberPurchase(callback?: QueryMemberPurchaseEvent): void
```

注销查询购买会员事件的监听。

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AVMusicTemplate-offQueryMemberPurchase(callback?: QueryMemberPurchaseEvent): void--><!--Device-AVMusicTemplate-offQueryMemberPurchase(callback?: QueryMemberPurchaseEvent): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [QueryMemberPurchaseEvent](arkts-avsession-avmusictemplate-querymemberpurchaseevent-t.md) | No | 查询购买会员的事件。不填该参数则注销该类型对应的所有回调。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 801 | Capability not supported.function offQueryMemberPurchase can not work correctly due to limited device capabilities. |
| 35000005 | AVMusicTemplate does not exist. |
| 35000012 | AVMusicTemplate error. |

## offQueryPlaylist

```TypeScript
offQueryPlaylist(callback?: QueryPlaylistEvent): void
```

注销查询播放列表的监听。

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AVMusicTemplate-offQueryPlaylist(callback?: QueryPlaylistEvent): void--><!--Device-AVMusicTemplate-offQueryPlaylist(callback?: QueryPlaylistEvent): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [QueryPlaylistEvent](arkts-avsession-avmusictemplate-queryplaylistevent-t.md) | No | 查询播放列表的事件。不填该参数则注销该类型对应的所有回调。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 801 | Capability not supported.function offQueryPlaylist can not work correctly due to limited device capabilities. |
| 35000005 | AVMusicTemplate does not exist. |
| 35000012 | AVMusicTemplate error. |

## offQueryRecommendMediaEntityList

```TypeScript
offQueryRecommendMediaEntityList(callback?: QueryRecommendMediaEntityListEvent): void
```

注销查询推荐媒体列表的监听。

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AVMusicTemplate-offQueryRecommendMediaEntityList(callback?: QueryRecommendMediaEntityListEvent): void--><!--Device-AVMusicTemplate-offQueryRecommendMediaEntityList(callback?: QueryRecommendMediaEntityListEvent): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [QueryRecommendMediaEntityListEvent](arkts-avsession-avmusictemplate-queryrecommendmediaentitylistevent-t.md) | No | 查询推荐媒体列表的事件。不填该参数则注销该类型对应的所有回调。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 801 | Capability not supported.function offQueryRecommendMediaEntityList can not work correctly due to limited device capabilities. |
| 35000005 | AVMusicTemplate does not exist. |
| 35000012 | AVMusicTemplate error. |

## offQuerySearchHistory

```TypeScript
offQuerySearchHistory(callback?: QuerySearchHistoryEvent): void
```

注销查询搜索历史的监听。

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AVMusicTemplate-offQuerySearchHistory(callback?: QuerySearchHistoryEvent): void--><!--Device-AVMusicTemplate-offQuerySearchHistory(callback?: QuerySearchHistoryEvent): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [QuerySearchHistoryEvent](arkts-avsession-avmusictemplate-querysearchhistoryevent-t.md) | No | 查询搜索历史的事件。不填该参数则注销该类型对应的所有回调。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 801 | Capability not supported.function offQuerySearchHistory can not work correctly due to limited device capabilities. |
| 35000005 | AVMusicTemplate does not exist. |
| 35000012 | AVMusicTemplate error. |

## offRequestDialogInfo

```TypeScript
offRequestDialogInfo(callback?: RequestDialogInfoEvent): void
```

注销请求对话框信息的监听。

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AVMusicTemplate-offRequestDialogInfo(callback?: RequestDialogInfoEvent): void--><!--Device-AVMusicTemplate-offRequestDialogInfo(callback?: RequestDialogInfoEvent): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [RequestDialogInfoEvent](arkts-avsession-avmusictemplate-requestdialoginfoevent-t.md) | No | 请求对话框信息的事件。不填该参数则注销该类型对应的所有回调。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 801 | Capability not supported.function offRequestDialogInfo can not work correctly due to limited device capabilities. |
| 35000005 | AVMusicTemplate does not exist. |
| 35000012 | AVMusicTemplate error. |

## offSettingsChange

```TypeScript
offSettingsChange(callback?: SettingsChangeEvent): void
```

注销设置改变事件的监听。

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AVMusicTemplate-offSettingsChange(callback?: SettingsChangeEvent): void--><!--Device-AVMusicTemplate-offSettingsChange(callback?: SettingsChangeEvent): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [SettingsChangeEvent](arkts-avsession-avmusictemplate-settingschangeevent-t.md) | No | 设置改变的事件。不填该参数则注销该类型对应的所有回调。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 801 | Capability not supported.function offSettingsChange can not work correctly due to limited device capabilities. |
| 35000005 | AVMusicTemplate does not exist. |
| 35000012 | AVMusicTemplate error. |

## onClearSearchHistory

```TypeScript
onClearSearchHistory(callback: ClearSearchHistoryEvent): void
```

注册清除搜索历史的监听。使用callback异步回调。

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AVMusicTemplate-onClearSearchHistory(callback: ClearSearchHistoryEvent): void--><!--Device-AVMusicTemplate-onClearSearchHistory(callback: ClearSearchHistoryEvent): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [ClearSearchHistoryEvent](arkts-avsession-avmusictemplate-clearsearchhistoryevent-t.md) | Yes | 回调函数，返回清除搜索历史的事件。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 801 | Capability not supported.function onClearSearchHistory can not work correctly due to limited device capabilities. |
| 35000005 | AVMusicTemplate does not exist. |
| 35000012 | AVMusicTemplate error. |

## onDownloadMediaEntity

```TypeScript
onDownloadMediaEntity(callback: DownloadMediaEntityEvent): void
```

注册下载媒体实体事件的监听。使用callback异步回调。

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AVMusicTemplate-onDownloadMediaEntity(callback: DownloadMediaEntityEvent): void--><!--Device-AVMusicTemplate-onDownloadMediaEntity(callback: DownloadMediaEntityEvent): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [DownloadMediaEntityEvent](arkts-avsession-avmusictemplate-downloadmediaentityevent-t.md) | Yes | 回调函数，返回下载媒体实体的事件。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 801 | Capability not supported.function onDownloadMediaEntity can not work correctly due to limited device capabilities. |
| 35000005 | AVMusicTemplate does not exist. |
| 35000012 | AVMusicTemplate error. |

## onExecuteAction

```TypeScript
onExecuteAction(callback: ExecuteActionEvent): void
```

注册执行操作事件的监听。使用callback异步回调。

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AVMusicTemplate-onExecuteAction(callback: ExecuteActionEvent): void--><!--Device-AVMusicTemplate-onExecuteAction(callback: ExecuteActionEvent): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [ExecuteActionEvent](arkts-avsession-avmusictemplate-executeactionevent-t.md) | Yes | 回调函数，返回执行操作的事件。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 801 | Capability not supported.function onExecuteAction can not work correctly due to limited device capabilities. |
| 35000005 | AVMusicTemplate does not exist. |
| 35000012 | AVMusicTemplate error. |

## onFavoriteMediaEntity

```TypeScript
onFavoriteMediaEntity(callback: FavoriteMediaEntityEvent): void
```

注册收藏媒体实体事件的监听。使用callback异步回调。

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AVMusicTemplate-onFavoriteMediaEntity(callback: FavoriteMediaEntityEvent): void--><!--Device-AVMusicTemplate-onFavoriteMediaEntity(callback: FavoriteMediaEntityEvent): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [FavoriteMediaEntityEvent](arkts-avsession-avmusictemplate-favoritemediaentityevent-t.md) | Yes | 回调函数，返回收藏媒体实体的事件。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 801 | Capability not supported.function onFavoriteMediaEntity can not work correctly due to limited device capabilities. |
| 35000005 | AVMusicTemplate does not exist. |
| 35000012 | AVMusicTemplate error. |

## onHandleMemberPurchase

```TypeScript
onHandleMemberPurchase(callback: HandleMemberPurchaseEvent): void
```

注册处理购买会员事件的监听。使用callback异步回调。

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AVMusicTemplate-onHandleMemberPurchase(callback: HandleMemberPurchaseEvent): void--><!--Device-AVMusicTemplate-onHandleMemberPurchase(callback: HandleMemberPurchaseEvent): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [HandleMemberPurchaseEvent](arkts-avsession-avmusictemplate-handlememberpurchaseevent-t.md) | Yes | 回调函数，返回处理购买会员的事件。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 801 | Capability not supported.function onHandleMemberPurchase can not work correctly due to limited device capabilities. |
| 35000005 | AVMusicTemplate does not exist. |
| 35000012 | AVMusicTemplate error. |

## onLogin

```TypeScript
onLogin(callback: LoginEvent): void
```

注册登录事件的监听。使用callback异步回调。

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AVMusicTemplate-onLogin(callback: LoginEvent): void--><!--Device-AVMusicTemplate-onLogin(callback: LoginEvent): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [LoginEvent](arkts-avsession-avmusictemplate-loginevent-t.md) | Yes | 回调函数，返回登录事件。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 801 | Capability not supported.function onLogin can not work correctly due to limited device capabilities. |
| 35000005 | AVMusicTemplate does not exist. |
| 35000012 | AVMusicTemplate error. |

## onPlayForSearch

```TypeScript
onPlayForSearch(callback: PlayForSearchEvent): void
```

注册搜播事件的监听。使用callback异步回调。

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AVMusicTemplate-onPlayForSearch(callback: PlayForSearchEvent): void--><!--Device-AVMusicTemplate-onPlayForSearch(callback: PlayForSearchEvent): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [PlayForSearchEvent](arkts-avsession-avmusictemplate-playforsearchevent-t.md) | Yes | 回调函数，返回搜播的事件。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 801 | Capability not supported.function onPlayForSearch can not work correctly due to limited device capabilities. |
| 35000005 | AVMusicTemplate does not exist. |
| 35000012 | AVMusicTemplate error. |

## onPlayMediaEntity

```TypeScript
onPlayMediaEntity(callback: PlayMediaEntityEvent): void
```

注册播放媒体实体事件的监听。使用callback异步回调。

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AVMusicTemplate-onPlayMediaEntity(callback: PlayMediaEntityEvent): void--><!--Device-AVMusicTemplate-onPlayMediaEntity(callback: PlayMediaEntityEvent): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [PlayMediaEntityEvent](arkts-avsession-avmusictemplate-playmediaentityevent-t.md) | Yes | 回调函数，返回播放媒体实体的事件。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 801 | Capability not supported.function onPlayMediaEntity can not work correctly due to limited device capabilities. |
| 35000005 | AVMusicTemplate does not exist. |
| 35000012 | AVMusicTemplate error. |

## onProblemAndAdvice

```TypeScript
onProblemAndAdvice(callback: ProblemAndAdviceEvent): void
```

注册问题与建议事件的监听。使用callback异步回调。

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AVMusicTemplate-onProblemAndAdvice(callback: ProblemAndAdviceEvent): void--><!--Device-AVMusicTemplate-onProblemAndAdvice(callback: ProblemAndAdviceEvent): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [ProblemAndAdviceEvent](arkts-avsession-avmusictemplate-problemandadviceevent-t.md) | Yes | 回调函数，返回问题与建议的事件。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 801 | Capability not supported.function onProblemAndAdvice can not work correctly due to limited device capabilities. |
| 35000005 | AVMusicTemplate does not exist. |
| 35000012 | AVMusicTemplate error. |

## onQueryCompilation

```TypeScript
onQueryCompilation(callback: QueryCompilationEvent): void
```

注册查询合集的监听。使用callback异步回调。

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AVMusicTemplate-onQueryCompilation(callback: QueryCompilationEvent): void--><!--Device-AVMusicTemplate-onQueryCompilation(callback: QueryCompilationEvent): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [QueryCompilationEvent](arkts-avsession-avmusictemplate-querycompilationevent-t.md) | Yes | 回调函数，返回查询合集的事件。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 801 | Capability not supported.function onQueryCompilation can not work correctly due to limited device capabilities. |
| 35000005 | AVMusicTemplate does not exist. |
| 35000012 | AVMusicTemplate error. |

## onQueryCompilationByKeyword

```TypeScript
onQueryCompilationByKeyword(callback: QueryCompilationByKeywordEvent): void
```

注册按关键字查询合集的监听。使用callback异步回调。

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AVMusicTemplate-onQueryCompilationByKeyword(callback: QueryCompilationByKeywordEvent): void--><!--Device-AVMusicTemplate-onQueryCompilationByKeyword(callback: QueryCompilationByKeywordEvent): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [QueryCompilationByKeywordEvent](arkts-avsession-avmusictemplate-querycompilationbykeywordevent-t.md) | Yes | 回调函数，返回按关键字查询合集的事件。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 801 | Capability not supported.function onQueryCompilationByKeyword can not work correctly due to limited device capabilities. |
| 35000005 | AVMusicTemplate does not exist. |
| 35000012 | AVMusicTemplate error. |

## onQueryCurrentSingle

```TypeScript
onQueryCurrentSingle(callback: QueryCurrentSingleEvent): void
```

注册查询当前单曲的监听。使用callback异步回调。

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AVMusicTemplate-onQueryCurrentSingle(callback: QueryCurrentSingleEvent): void--><!--Device-AVMusicTemplate-onQueryCurrentSingle(callback: QueryCurrentSingleEvent): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [QueryCurrentSingleEvent](arkts-avsession-avmusictemplate-querycurrentsingleevent-t.md) | Yes | 回调函数，返回查询当前单曲的事件。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 801 | Capability not supported.function onQueryCurrentSingle can not work correctly due to limited device capabilities. |
| 35000005 | AVMusicTemplate does not exist. |
| 35000012 | AVMusicTemplate error. |

## onQueryCustomContent

```TypeScript
onQueryCustomContent(callback: QueryCustomContentEvent): void
```

注册查询自定义内容事件的监听。使用callback异步回调。

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AVMusicTemplate-onQueryCustomContent(callback: QueryCustomContentEvent): void--><!--Device-AVMusicTemplate-onQueryCustomContent(callback: QueryCustomContentEvent): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [QueryCustomContentEvent](arkts-avsession-avmusictemplate-querycustomcontentevent-t.md) | Yes | 回调函数，返回查询自定义内容的事件。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 801 | Capability not supported.function onQueryCustomContent can not work correctly due to limited device capabilities. |
| 35000005 | AVMusicTemplate does not exist. |
| 35000012 | AVMusicTemplate error. |

## onQueryHotWords

```TypeScript
onQueryHotWords(callback: QueryHotWordsEvent): void
```

注册查询热词的监听。使用callback异步回调。

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AVMusicTemplate-onQueryHotWords(callback: QueryHotWordsEvent): void--><!--Device-AVMusicTemplate-onQueryHotWords(callback: QueryHotWordsEvent): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [QueryHotWordsEvent](arkts-avsession-avmusictemplate-queryhotwordsevent-t.md) | Yes | 回调函数，返回查询热词的事件。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 801 | Capability not supported.function onQueryHotWords can not work correctly due to limited device capabilities. |
| 35000005 | AVMusicTemplate does not exist. |
| 35000012 | AVMusicTemplate error. |

## onQueryMainTabs

```TypeScript
onQueryMainTabs(callback: QueryMainTabsEvent): void
```

注册查询主标签的事件监听。使用callback异步回调。

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AVMusicTemplate-onQueryMainTabs(callback: QueryMainTabsEvent): void--><!--Device-AVMusicTemplate-onQueryMainTabs(callback: QueryMainTabsEvent): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [QueryMainTabsEvent](arkts-avsession-avmusictemplate-querymaintabsevent-t.md) | Yes | 回调函数，返回查询主标签事件。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 801 | Capability not supported.function onQueryMainTabs can not work correctly due to limited device capabilities. |
| 35000005 | AVMusicTemplate does not exist. |
| 35000012 | AVMusicTemplate error. |

## onQueryMediaEntity

```TypeScript
onQueryMediaEntity(callback: QueryMediaEntityEvent): void
```

注册查询媒体实体监听。使用callback异步回调。

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AVMusicTemplate-onQueryMediaEntity(callback: QueryMediaEntityEvent): void--><!--Device-AVMusicTemplate-onQueryMediaEntity(callback: QueryMediaEntityEvent): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [QueryMediaEntityEvent](arkts-avsession-avmusictemplate-querymediaentityevent-t.md) | Yes | 回调函数，返回查询媒体实体的事件。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 801 | Capability not supported.function onQueryMediaEntity can not work correctly due to limited device capabilities. |
| 35000005 | AVMusicTemplate does not exist. |
| 35000012 | AVMusicTemplate error. |

## onQueryMediaEntityByKeyword

```TypeScript
onQueryMediaEntityByKeyword(callback: QueryMediaEntityByKeywordEvent): void
```

注册按关键字查询媒体实体的监听。使用callback异步回调。

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AVMusicTemplate-onQueryMediaEntityByKeyword(callback: QueryMediaEntityByKeywordEvent): void--><!--Device-AVMusicTemplate-onQueryMediaEntityByKeyword(callback: QueryMediaEntityByKeywordEvent): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [QueryMediaEntityByKeywordEvent](arkts-avsession-avmusictemplate-querymediaentitybykeywordevent-t.md) | Yes | 回调函数，返回按关键字查询媒体实体的事件。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 801 | Capability not supported.function onQueryMediaEntityByKeyword can not work correctly due to limited device capabilities. |
| 35000005 | AVMusicTemplate does not exist. |
| 35000012 | AVMusicTemplate error. |

## onQueryMediaTabContent

```TypeScript
onQueryMediaTabContent(callback: QueryMediaTabContentEvent): void
```

注册查询媒体标签内容事件监听。使用callback异步回调。

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AVMusicTemplate-onQueryMediaTabContent(callback: QueryMediaTabContentEvent): void--><!--Device-AVMusicTemplate-onQueryMediaTabContent(callback: QueryMediaTabContentEvent): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [QueryMediaTabContentEvent](arkts-avsession-avmusictemplate-querymediatabcontentevent-t.md) | Yes | 回调函数，返回查询媒体标签页内容的事件。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 801 | Capability not supported.function onQueryMediaTabContent can not work correctly due to limited device capabilities. |
| 35000005 | AVMusicTemplate does not exist. |
| 35000012 | AVMusicTemplate error. |

## onQueryMemberPurchase

```TypeScript
onQueryMemberPurchase(callback: QueryMemberPurchaseEvent): void
```

注册查询购买会员事件的监听。使用callback异步回调。

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AVMusicTemplate-onQueryMemberPurchase(callback: QueryMemberPurchaseEvent): void--><!--Device-AVMusicTemplate-onQueryMemberPurchase(callback: QueryMemberPurchaseEvent): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [QueryMemberPurchaseEvent](arkts-avsession-avmusictemplate-querymemberpurchaseevent-t.md) | Yes | 回调函数，返回查询购买会员的事件。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 801 | Capability not supported.function onQueryMemberPurchase can not work correctly due to limited device capabilities. |
| 35000005 | AVMusicTemplate does not exist. |
| 35000012 | AVMusicTemplate error. |

## onQueryPlaylist

```TypeScript
onQueryPlaylist(callback: QueryPlaylistEvent): void
```

注册查询播放列表的监听。使用callback异步回调。

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AVMusicTemplate-onQueryPlaylist(callback: QueryPlaylistEvent): void--><!--Device-AVMusicTemplate-onQueryPlaylist(callback: QueryPlaylistEvent): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [QueryPlaylistEvent](arkts-avsession-avmusictemplate-queryplaylistevent-t.md) | Yes | 回调函数，返回查询播放列表的事件。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 801 | Capability not supported.function onQueryPlaylist can not work correctly due to limited device capabilities. |
| 35000005 | AVMusicTemplate does not exist. |
| 35000012 | AVMusicTemplate error. |

## onQueryRecommendMediaEntityList

```TypeScript
onQueryRecommendMediaEntityList(callback: QueryRecommendMediaEntityListEvent): void
```

注册查询推荐媒体列表的监听。使用callback异步回调。

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AVMusicTemplate-onQueryRecommendMediaEntityList(callback: QueryRecommendMediaEntityListEvent): void--><!--Device-AVMusicTemplate-onQueryRecommendMediaEntityList(callback: QueryRecommendMediaEntityListEvent): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [QueryRecommendMediaEntityListEvent](arkts-avsession-avmusictemplate-queryrecommendmediaentitylistevent-t.md) | Yes | 回调函数，返回查询推荐媒体列表的事件。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 801 | Capability not supported.function onQueryRecommendMediaEntityList can not work correctly due to limited device capabilities. |
| 35000005 | AVMusicTemplate does not exist. |
| 35000012 | AVMusicTemplate error. |

## onQuerySearchHistory

```TypeScript
onQuerySearchHistory(callback: QuerySearchHistoryEvent): void
```

注册查询搜索历史的监听。使用callback异步回调。

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AVMusicTemplate-onQuerySearchHistory(callback: QuerySearchHistoryEvent): void--><!--Device-AVMusicTemplate-onQuerySearchHistory(callback: QuerySearchHistoryEvent): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [QuerySearchHistoryEvent](arkts-avsession-avmusictemplate-querysearchhistoryevent-t.md) | Yes | 回调函数，返回查询搜索历史的事件。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 801 | Capability not supported.function onQuerySearchHistory can not work correctly due to limited device capabilities. |
| 35000005 | AVMusicTemplate does not exist. |
| 35000012 | AVMusicTemplate error. |

## onRequestDialogInfo

```TypeScript
onRequestDialogInfo(callback: RequestDialogInfoEvent): void
```

注册请求对话框信息的监听。使用callback异步回调。

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AVMusicTemplate-onRequestDialogInfo(callback: RequestDialogInfoEvent): void--><!--Device-AVMusicTemplate-onRequestDialogInfo(callback: RequestDialogInfoEvent): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [RequestDialogInfoEvent](arkts-avsession-avmusictemplate-requestdialoginfoevent-t.md) | Yes | 回调函数，返回请求对话框信息的事件。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 801 | Capability not supported.function onRequestDialogInfo can not work correctly due to limited device capabilities. |
| 35000005 | AVMusicTemplate does not exist. |
| 35000012 | AVMusicTemplate error. |

## onSettingsChange

```TypeScript
onSettingsChange(callback: SettingsChangeEvent): void
```

注册设置改变事件的监听。使用callback异步回调。

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AVMusicTemplate-onSettingsChange(callback: SettingsChangeEvent): void--><!--Device-AVMusicTemplate-onSettingsChange(callback: SettingsChangeEvent): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [SettingsChangeEvent](arkts-avsession-avmusictemplate-settingschangeevent-t.md) | Yes | 回调函数，返回设置改变的事件。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 801 | Capability not supported.function onSettingsChange can not work correctly due to limited device capabilities. |
| 35000005 | AVMusicTemplate does not exist. |
| 35000012 | AVMusicTemplate error. |

## reportExecuteAction

```TypeScript
reportExecuteAction(actionType: string, params: string): Promise<void>
```

向音频模板控制方同步执行操作信息。使用Promise异步回调。

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AVMusicTemplate-reportExecuteAction(actionType: string, params: string): Promise<void>--><!--Device-AVMusicTemplate-reportExecuteAction(actionType: string, params: string): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| actionType | string | Yes | 行为类型。 |
| params | string | Yes | 行为信息。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise对象，无返回结果。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 801 | Capability not supported.function reportExecuteAction can not work correctly due to limited device capabilities. |
| 35000005 | AVMusicTemplate does not exist. |
| 35000011 | Thr data write error, data is invalid. |

## setCurrentSingle

```TypeScript
setCurrentSingle(single: Single): Promise<void>
```

向音频模板控制方同步当前单曲。使用Promise异步回调。

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AVMusicTemplate-setCurrentSingle(single: Single): Promise<void>--><!--Device-AVMusicTemplate-setCurrentSingle(single: Single): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| single | [Single](arkts-avsession-avmusictemplate-single-i.md) | Yes | 当前单曲。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise对象，无返回结果。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 801 | Capability not supported.function setCurrentSingle can not work correctly due to limited device capabilities. |
| 35000005 | AVMusicTemplate does not exist. |
| 35000011 | Thr data write error, data is invalid. |

## setCustomElements

```TypeScript
setCustomElements(actionType: ActionType, customType: CustomType,
      customElement: CustomElement): Promise<void>
```

上报自定义数据变更信息至媒体中心

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AVMusicTemplate-setCustomElements(actionType: ActionType, customType: CustomType,      customElement: CustomElement): Promise<void>--><!--Device-AVMusicTemplate-setCustomElements(actionType: ActionType, customType: CustomType,      customElement: CustomElement): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| actionType | [ActionType](arkts-avsession-avmusictemplate-actiontype-t.md) | Yes | 操作类型 |
| customType | [CustomType](arkts-avsession-avmusictemplate-customtype-t.md) | Yes | 自定义数据的类型 |
| customElement | [CustomElement](arkts-avsession-avmusictemplate-customelement-i.md) | Yes | 自定义数据 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | 通过promise'返回上报自定义数据的结果 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 801 | Capability not supported.function setCustomElements can not work correctly due to limited device capabilities. |
| 35000005 | AVMusicTemplate does not exist. |
| 35000011 | Thr data write error, data is invalid. |

## setDialogCommand

```TypeScript
setDialogCommand(type: DialogControlType, dialogInfo: DialogInfo): Promise<void>
```

向音频模板控制方同步对话框命令。使用Promise异步回调。

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AVMusicTemplate-setDialogCommand(type: DialogControlType, dialogInfo: DialogInfo): Promise<void>--><!--Device-AVMusicTemplate-setDialogCommand(type: DialogControlType, dialogInfo: DialogInfo): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | [DialogControlType](arkts-avsession-avmusictemplate-dialogcontroltype-t.md) | Yes | 对话框控制类型。 |
| dialogInfo | [DialogInfo](arkts-avsession-avmusictemplate-dialoginfo-i.md) | Yes | 对话框信息。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise对象，无返回结果。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 801 | Capability not supported.function setDialogCommand can not work correctly due to limited device capabilities. |
| 35000005 | AVMusicTemplate does not exist. |
| 35000011 | Thr data write error, data is invalid. |

## setDownloadMediaEntityStatus

```TypeScript
setDownloadMediaEntityStatus(single: MediaEntity): Promise<void>
```

向音频模板控制方同步单曲下载状态信息。使用Promise异步回调。

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AVMusicTemplate-setDownloadMediaEntityStatus(single: MediaEntity): Promise<void>--><!--Device-AVMusicTemplate-setDownloadMediaEntityStatus(single: MediaEntity): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| single | [MediaEntity](arkts-avsession-avmusictemplate-mediaentity-i.md) | Yes | 单曲。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise对象，无返回结果。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 801 | Capability not supported.function setDownloadMediaEntityStatus can not work correctly due to limited device capabilities. |
| 35000005 | AVMusicTemplate does not exist. |
| 35000011 | Thr data write error, data is invalid. |

## setExtensionAbility

```TypeScript
setExtensionAbility(want: WantAgent): Promise<void>
```

向音频模板控制方同步用于被拉起的Ability。使用Promise异步回调。

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AVMusicTemplate-setExtensionAbility(want: WantAgent): Promise<void>--><!--Device-AVMusicTemplate-setExtensionAbility(want: WantAgent): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| want | [WantAgent](../../apis-ability-kit/arkts-apis/arkts-ability-wantagent-t.md) | Yes | 能力信息。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise对象，无返回结果。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 801 | capability not supported. |
| 35000005 | AVMusicTemplate does not exist. |
| 35000011 | Thr data write error, data is invalid. |

## setMediaEntities

```TypeScript
setMediaEntities(entities: MediaEntity[]): Promise<void>
```

向音频模板控制方同步媒体资源变更信息。使用Promise异步回调。

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AVMusicTemplate-setMediaEntities(entities: MediaEntity[]): Promise<void>--><!--Device-AVMusicTemplate-setMediaEntities(entities: MediaEntity[]): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| entities | [MediaEntity](arkts-avsession-avmusictemplate-mediaentity-i.md)[] | Yes | 媒体实体的数组。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise对象，无返回结果。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 801 | Capability not supported.function setMediaEntities can not work correctly due to limited device capabilities. |
| 35000005 | AVMusicTemplate does not exist. |
| 35000011 | Thr data write error, data is invalid. |

## setPlaylist

```TypeScript
setPlaylist(playlist: PageMediaEntity): Promise<void>
```

向音频模板控制方同步播放列表。使用Promise异步回调。

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AVMusicTemplate-setPlaylist(playlist: PageMediaEntity): Promise<void>--><!--Device-AVMusicTemplate-setPlaylist(playlist: PageMediaEntity): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| playlist | [PageMediaEntity](arkts-avsession-avmusictemplate-pagemediaentity-i.md) | Yes | 分页媒体实体。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise对象，无返回结果。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 801 | Capability not supported.function setPlaylist can not work correctly due to limited device capabilities. |
| 35000005 | AVMusicTemplate does not exist. |
| 35000011 | Thr data write error, data is invalid. |

## setSettings

```TypeScript
setSettings(settingItems: SettingItem[]): Promise<void>
```

向音频模板控制方同步设置信息。使用Promise异步回调。

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AVMusicTemplate-setSettings(settingItems: SettingItem[]): Promise<void>--><!--Device-AVMusicTemplate-setSettings(settingItems: SettingItem[]): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| settingItems | [SettingItem](arkts-avsession-avmusictemplate-settingitem-i.md)[] | Yes | 设置项数组。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise对象，无返回结果。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 801 | Capability not supported.function setSettings can not work correctly due to limited device capabilities. |
| 35000005 | AVMusicTemplate does not exist. |
| 35000011 | Thr data write error, data is invalid. |

## setTabContent

```TypeScript
setTabContent(tabId: string, tabContent: MediaTabContent): Promise<void>
```

向音频模板控制方同步标签页内容信息。使用Promise异步回调。

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AVMusicTemplate-setTabContent(tabId: string, tabContent: MediaTabContent): Promise<void>--><!--Device-AVMusicTemplate-setTabContent(tabId: string, tabContent: MediaTabContent): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| tabId | string | Yes | 标签的ID。 |
| tabContent | [MediaTabContent](arkts-avsession-avmusictemplate-mediatabcontent-i.md) | Yes | 媒体标签页内容。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise对象，无返回结果。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 801 | Capability not supported.function setTabContent can not work correctly due to limited device capabilities. |
| 35000005 | AVMusicTemplate does not exist. |
| 35000011 | Thr data write error, data is invalid. |

## setUserInfo

```TypeScript
setUserInfo(userInfo: UserInfo): Promise<void>
```

向音频模板控制方同步用户信息。使用Promise异步回调。

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AVMusicTemplate-setUserInfo(userInfo: UserInfo): Promise<void>--><!--Device-AVMusicTemplate-setUserInfo(userInfo: UserInfo): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| userInfo | [UserInfo](../../apis-arkdata/arkts-apis/arkts-arkdata-distributeddata-userinfo-i.md) | Yes | 用户信息。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise对象，无返回结果。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 801 | Capability not supported.function setUserInfo can not work correctly due to limited device capabilities. |
| 35000005 | AVMusicTemplate does not exist. |
| 35000011 | Thr data write error, data is invalid. |

## startTemplate

```TypeScript
startTemplate(): Promise<OperResult>
```

启动音频模板界面。使用Promise异步回调。

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AVMusicTemplate-startTemplate(): Promise<OperResult>--><!--Device-AVMusicTemplate-startTemplate(): Promise<OperResult>-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;OperResult&gt; | Promise对象，返回启动音频模板界面的操作结果。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 801 | capability not supported. |

## sessionId

```TypeScript
sessionId: string
```

音频模板唯一的标识。

**Type:** string

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AVMusicTemplate-sessionId: string--><!--Device-AVMusicTemplate-sessionId: string-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVMusicTemplate

## sessionTag

```TypeScript
sessionTag: string
```

音频模板标签。

**Type:** string

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AVMusicTemplate-sessionTag: string--><!--Device-AVMusicTemplate-sessionTag: string-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVMusicTemplate

