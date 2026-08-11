# AVMusicTemplate

调用[avMusicTemplate.createAVMusicTemplate](arkts-avsession-avmusictemplate-createavmusictemplate-f.md#createavmusictemplate)获取实例后，可获取其ID，启动音频模板界面，并配置数据获取方法。随后，同步数据给模板控制方，以完成后续操作。

> **说明：**
> 
> - 本模块仅适用于API version 23及以上版本的Car设备。

**起始版本：** 23

<!--Device-avMusicTemplate-class AVMusicTemplate--><!--Device-avMusicTemplate-class AVMusicTemplate-End-->

**系统能力：** SystemCapability.Multimedia.AVSession.AVMusicTemplate

## destroy

```TypeScript
destroy(): Promise<void>
```

销毁音频模板实例。使用Promise异步回调。

**起始版本：** 23

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-AVMusicTemplate-destroy(): Promise<void>--><!--Device-AVMusicTemplate-destroy(): Promise<void>-End-->

**系统能力：** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**返回值：**

| 类型 |
| --- |
| Promise&lt;void&gt; |

**错误码：**

| 错误码ID |
| --- |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |

## offClearSearchHistory

```TypeScript
offClearSearchHistory(callback?: ClearSearchHistoryEvent): void
```

注销清除搜索历史的监听。

**起始版本：** 23

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-AVMusicTemplate-offClearSearchHistory(callback?: ClearSearchHistoryEvent): void--><!--Device-AVMusicTemplate-offClearSearchHistory(callback?: ClearSearchHistoryEvent): void-End-->

**系统能力：** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [ClearSearchHistoryEvent](arkts-avsession-avmusictemplate-clearsearchhistoryevent-t.md) | 否 |

**错误码：**

| 错误码ID |
| --- |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [35000005](../errorcode-avmusictemplate.md#35000005-音频模板不存在) |
| [35000012](../errorcode-avmusictemplate.md#35000012-音频模板错误) |

## offDownloadMediaEntity

```TypeScript
offDownloadMediaEntity(callback?: DownloadMediaEntityEvent): void
```

注销下载媒体实体事件的监听。

**起始版本：** 23

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-AVMusicTemplate-offDownloadMediaEntity(callback?: DownloadMediaEntityEvent): void--><!--Device-AVMusicTemplate-offDownloadMediaEntity(callback?: DownloadMediaEntityEvent): void-End-->

**系统能力：** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [DownloadMediaEntityEvent](arkts-avsession-avmusictemplate-downloadmediaentityevent-t.md) | 否 |

**错误码：**

| 错误码ID |
| --- |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [35000005](../errorcode-avmusictemplate.md#35000005-音频模板不存在) |
| [35000012](../errorcode-avmusictemplate.md#35000012-音频模板错误) |

## offExecuteAction

```TypeScript
offExecuteAction(callback?: ExecuteActionEvent): void
```

注销执行操作事件的监听。

**起始版本：** 23

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-AVMusicTemplate-offExecuteAction(callback?: ExecuteActionEvent): void--><!--Device-AVMusicTemplate-offExecuteAction(callback?: ExecuteActionEvent): void-End-->

**系统能力：** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [ExecuteActionEvent](arkts-avsession-avmusictemplate-executeactionevent-t.md) | 否 |

**错误码：**

| 错误码ID |
| --- |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [35000005](../errorcode-avmusictemplate.md#35000005-音频模板不存在) |
| [35000012](../errorcode-avmusictemplate.md#35000012-音频模板错误) |

## offFavoriteMediaEntity

```TypeScript
offFavoriteMediaEntity(callback?: FavoriteMediaEntityEvent): void
```

注销收藏媒体实体事件的监听。

**起始版本：** 23

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-AVMusicTemplate-offFavoriteMediaEntity(callback?: FavoriteMediaEntityEvent): void--><!--Device-AVMusicTemplate-offFavoriteMediaEntity(callback?: FavoriteMediaEntityEvent): void-End-->

**系统能力：** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [FavoriteMediaEntityEvent](arkts-avsession-avmusictemplate-favoritemediaentityevent-t.md) | 否 |

**错误码：**

| 错误码ID |
| --- |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [35000005](../errorcode-avmusictemplate.md#35000005-音频模板不存在) |
| [35000012](../errorcode-avmusictemplate.md#35000012-音频模板错误) |

## offHandleMemberPurchase

```TypeScript
offHandleMemberPurchase(callback?: HandleMemberPurchaseEvent): void
```

注销处理购买会员事件的监听。

**起始版本：** 23

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-AVMusicTemplate-offHandleMemberPurchase(callback?: HandleMemberPurchaseEvent): void--><!--Device-AVMusicTemplate-offHandleMemberPurchase(callback?: HandleMemberPurchaseEvent): void-End-->

**系统能力：** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [HandleMemberPurchaseEvent](arkts-avsession-avmusictemplate-handlememberpurchaseevent-t.md) | 否 |

**错误码：**

| 错误码ID |
| --- |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [35000005](../errorcode-avmusictemplate.md#35000005-音频模板不存在) |
| [35000012](../errorcode-avmusictemplate.md#35000012-音频模板错误) |

## offLogin

```TypeScript
offLogin(callback?: LoginEvent): void
```

注销登录事件的监听。

**起始版本：** 23

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-AVMusicTemplate-offLogin(callback?: LoginEvent): void--><!--Device-AVMusicTemplate-offLogin(callback?: LoginEvent): void-End-->

**系统能力：** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [LoginEvent](arkts-avsession-avmusictemplate-loginevent-t.md) | 否 |

**错误码：**

| 错误码ID |
| --- |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [35000005](../errorcode-avmusictemplate.md#35000005-音频模板不存在) |
| [35000012](../errorcode-avmusictemplate.md#35000012-音频模板错误) |

## offPlayForSearch

```TypeScript
offPlayForSearch(callback?: PlayForSearchEvent): void
```

注销搜播事件的监听。

**起始版本：** 23

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-AVMusicTemplate-offPlayForSearch(callback?: PlayForSearchEvent): void--><!--Device-AVMusicTemplate-offPlayForSearch(callback?: PlayForSearchEvent): void-End-->

**系统能力：** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [PlayForSearchEvent](arkts-avsession-avmusictemplate-playforsearchevent-t.md) | 否 |

**错误码：**

| 错误码ID |
| --- |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [35000005](../errorcode-avmusictemplate.md#35000005-音频模板不存在) |
| [35000012](../errorcode-avmusictemplate.md#35000012-音频模板错误) |

## offPlayMediaEntity

```TypeScript
offPlayMediaEntity(callback?: PlayMediaEntityEvent): void
```

注销播放媒体实体事件的监听。

**起始版本：** 23

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-AVMusicTemplate-offPlayMediaEntity(callback?: PlayMediaEntityEvent): void--><!--Device-AVMusicTemplate-offPlayMediaEntity(callback?: PlayMediaEntityEvent): void-End-->

**系统能力：** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [PlayMediaEntityEvent](arkts-avsession-avmusictemplate-playmediaentityevent-t.md) | 否 |

**错误码：**

| 错误码ID |
| --- |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [35000005](../errorcode-avmusictemplate.md#35000005-音频模板不存在) |
| [35000012](../errorcode-avmusictemplate.md#35000012-音频模板错误) |

## offProblemAndAdvice

```TypeScript
offProblemAndAdvice(callback?: ProblemAndAdviceEvent): void
```

注销问题与建议事件的监听。

**起始版本：** 23

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-AVMusicTemplate-offProblemAndAdvice(callback?: ProblemAndAdviceEvent): void--><!--Device-AVMusicTemplate-offProblemAndAdvice(callback?: ProblemAndAdviceEvent): void-End-->

**系统能力：** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [ProblemAndAdviceEvent](arkts-avsession-avmusictemplate-problemandadviceevent-t.md) | 否 |

**错误码：**

| 错误码ID |
| --- |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [35000005](../errorcode-avmusictemplate.md#35000005-音频模板不存在) |
| [35000012](../errorcode-avmusictemplate.md#35000012-音频模板错误) |

## offQueryCompilation

```TypeScript
offQueryCompilation(callback?: QueryCompilationEvent): void
```

注销查询合集的监听。

**起始版本：** 23

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-AVMusicTemplate-offQueryCompilation(callback?: QueryCompilationEvent): void--><!--Device-AVMusicTemplate-offQueryCompilation(callback?: QueryCompilationEvent): void-End-->

**系统能力：** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [QueryCompilationEvent](arkts-avsession-avmusictemplate-querycompilationevent-t.md) | 否 |

**错误码：**

| 错误码ID |
| --- |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [35000005](../errorcode-avmusictemplate.md#35000005-音频模板不存在) |
| [35000012](../errorcode-avmusictemplate.md#35000012-音频模板错误) |

## offQueryCompilationByKeyword

```TypeScript
offQueryCompilationByKeyword(callback?: QueryCompilationByKeywordEvent): void
```

注销按关键字查询合集的监听。

**起始版本：** 23

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-AVMusicTemplate-offQueryCompilationByKeyword(callback?: QueryCompilationByKeywordEvent): void--><!--Device-AVMusicTemplate-offQueryCompilationByKeyword(callback?: QueryCompilationByKeywordEvent): void-End-->

**系统能力：** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [QueryCompilationByKeywordEvent](arkts-avsession-avmusictemplate-querycompilationbykeywordevent-t.md) | 否 |

**错误码：**

| 错误码ID |
| --- |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [35000005](../errorcode-avmusictemplate.md#35000005-音频模板不存在) |
| [35000012](../errorcode-avmusictemplate.md#35000012-音频模板错误) |

## offQueryCurrentSingle

```TypeScript
offQueryCurrentSingle(callback?: QueryCurrentSingleEvent): void
```

注销查询当前单曲的监听。

**起始版本：** 23

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-AVMusicTemplate-offQueryCurrentSingle(callback?: QueryCurrentSingleEvent): void--><!--Device-AVMusicTemplate-offQueryCurrentSingle(callback?: QueryCurrentSingleEvent): void-End-->

**系统能力：** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [QueryCurrentSingleEvent](arkts-avsession-avmusictemplate-querycurrentsingleevent-t.md) | 否 |

**错误码：**

| 错误码ID |
| --- |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [35000005](../errorcode-avmusictemplate.md#35000005-音频模板不存在) |
| [35000012](../errorcode-avmusictemplate.md#35000012-音频模板错误) |

## offQueryCustomContent

```TypeScript
offQueryCustomContent(callback?: QueryCustomContentEvent): void
```

注销查询自定义内容事件的监听。

**起始版本：** 23

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-AVMusicTemplate-offQueryCustomContent(callback?: QueryCustomContentEvent): void--><!--Device-AVMusicTemplate-offQueryCustomContent(callback?: QueryCustomContentEvent): void-End-->

**系统能力：** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [QueryCustomContentEvent](arkts-avsession-avmusictemplate-querycustomcontentevent-t.md) | 否 |

**错误码：**

| 错误码ID |
| --- |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [35000005](../errorcode-avmusictemplate.md#35000005-音频模板不存在) |
| [35000012](../errorcode-avmusictemplate.md#35000012-音频模板错误) |

## offQueryHotWords

```TypeScript
offQueryHotWords(callback?: QueryHotWordsEvent): void
```

注销查询热词的监听。

**起始版本：** 23

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-AVMusicTemplate-offQueryHotWords(callback?: QueryHotWordsEvent): void--><!--Device-AVMusicTemplate-offQueryHotWords(callback?: QueryHotWordsEvent): void-End-->

**系统能力：** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [QueryHotWordsEvent](arkts-avsession-avmusictemplate-queryhotwordsevent-t.md) | 否 |

**错误码：**

| 错误码ID |
| --- |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [35000005](../errorcode-avmusictemplate.md#35000005-音频模板不存在) |
| [35000012](../errorcode-avmusictemplate.md#35000012-音频模板错误) |

## offQueryMainTabs

```TypeScript
offQueryMainTabs(callback?: QueryMainTabsEvent): void
```

注销查询主标签事件监听。

**起始版本：** 23

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-AVMusicTemplate-offQueryMainTabs(callback?: QueryMainTabsEvent): void--><!--Device-AVMusicTemplate-offQueryMainTabs(callback?: QueryMainTabsEvent): void-End-->

**系统能力：** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [QueryMainTabsEvent](arkts-avsession-avmusictemplate-querymaintabsevent-t.md) | 否 |

**错误码：**

| 错误码ID |
| --- |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [35000005](../errorcode-avmusictemplate.md#35000005-音频模板不存在) |
| [35000012](../errorcode-avmusictemplate.md#35000012-音频模板错误) |

## offQueryMediaEntity

```TypeScript
offQueryMediaEntity(callback?: QueryMediaEntityEvent): void
```

注销查询媒体实体监听。

**起始版本：** 23

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-AVMusicTemplate-offQueryMediaEntity(callback?: QueryMediaEntityEvent): void--><!--Device-AVMusicTemplate-offQueryMediaEntity(callback?: QueryMediaEntityEvent): void-End-->

**系统能力：** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [QueryMediaEntityEvent](arkts-avsession-avmusictemplate-querymediaentityevent-t.md) | 否 |

**错误码：**

| 错误码ID |
| --- |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [35000005](../errorcode-avmusictemplate.md#35000005-音频模板不存在) |
| [35000012](../errorcode-avmusictemplate.md#35000012-音频模板错误) |

## offQueryMediaEntityByKeyword

```TypeScript
offQueryMediaEntityByKeyword(callback?: QueryMediaEntityByKeywordEvent): void
```

注销按关键字查询媒体实体的监听。

**起始版本：** 23

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-AVMusicTemplate-offQueryMediaEntityByKeyword(callback?: QueryMediaEntityByKeywordEvent): void--><!--Device-AVMusicTemplate-offQueryMediaEntityByKeyword(callback?: QueryMediaEntityByKeywordEvent): void-End-->

**系统能力：** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [QueryMediaEntityByKeywordEvent](arkts-avsession-avmusictemplate-querymediaentitybykeywordevent-t.md) | 否 |

**错误码：**

| 错误码ID |
| --- |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [35000005](../errorcode-avmusictemplate.md#35000005-音频模板不存在) |
| [35000012](../errorcode-avmusictemplate.md#35000012-音频模板错误) |

## offQueryMediaTabContent

```TypeScript
offQueryMediaTabContent(callback?: QueryMediaTabContentEvent): void
```

取消查询媒体标签内容监听。

**起始版本：** 23

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-AVMusicTemplate-offQueryMediaTabContent(callback?: QueryMediaTabContentEvent): void--><!--Device-AVMusicTemplate-offQueryMediaTabContent(callback?: QueryMediaTabContentEvent): void-End-->

**系统能力：** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [QueryMediaTabContentEvent](arkts-avsession-avmusictemplate-querymediatabcontentevent-t.md) | 否 |

**错误码：**

| 错误码ID |
| --- |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [35000005](../errorcode-avmusictemplate.md#35000005-音频模板不存在) |
| [35000012](../errorcode-avmusictemplate.md#35000012-音频模板错误) |

## offQueryMemberPurchase

```TypeScript
offQueryMemberPurchase(callback?: QueryMemberPurchaseEvent): void
```

注销查询购买会员事件的监听。

**起始版本：** 23

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-AVMusicTemplate-offQueryMemberPurchase(callback?: QueryMemberPurchaseEvent): void--><!--Device-AVMusicTemplate-offQueryMemberPurchase(callback?: QueryMemberPurchaseEvent): void-End-->

**系统能力：** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [QueryMemberPurchaseEvent](arkts-avsession-avmusictemplate-querymemberpurchaseevent-t.md) | 否 |

**错误码：**

| 错误码ID |
| --- |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [35000005](../errorcode-avmusictemplate.md#35000005-音频模板不存在) |
| [35000012](../errorcode-avmusictemplate.md#35000012-音频模板错误) |

## offQueryPlaylist

```TypeScript
offQueryPlaylist(callback?: QueryPlaylistEvent): void
```

注销查询播放列表的监听。

**起始版本：** 23

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-AVMusicTemplate-offQueryPlaylist(callback?: QueryPlaylistEvent): void--><!--Device-AVMusicTemplate-offQueryPlaylist(callback?: QueryPlaylistEvent): void-End-->

**系统能力：** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [QueryPlaylistEvent](arkts-avsession-avmusictemplate-queryplaylistevent-t.md) | 否 |

**错误码：**

| 错误码ID |
| --- |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [35000005](../errorcode-avmusictemplate.md#35000005-音频模板不存在) |
| [35000012](../errorcode-avmusictemplate.md#35000012-音频模板错误) |

## offQueryRecommendMediaEntityList

```TypeScript
offQueryRecommendMediaEntityList(callback?: QueryRecommendMediaEntityListEvent): void
```

注销查询推荐媒体列表的监听。

**起始版本：** 23

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-AVMusicTemplate-offQueryRecommendMediaEntityList(callback?: QueryRecommendMediaEntityListEvent): void--><!--Device-AVMusicTemplate-offQueryRecommendMediaEntityList(callback?: QueryRecommendMediaEntityListEvent): void-End-->

**系统能力：** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [QueryRecommendMediaEntityListEvent](arkts-avsession-avmusictemplate-queryrecommendmediaentitylistevent-t.md) | 否 |

**错误码：**

| 错误码ID |
| --- |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [35000005](../errorcode-avmusictemplate.md#35000005-音频模板不存在) |
| [35000012](../errorcode-avmusictemplate.md#35000012-音频模板错误) |

## offQuerySearchHistory

```TypeScript
offQuerySearchHistory(callback?: QuerySearchHistoryEvent): void
```

注销查询搜索历史的监听。

**起始版本：** 23

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-AVMusicTemplate-offQuerySearchHistory(callback?: QuerySearchHistoryEvent): void--><!--Device-AVMusicTemplate-offQuerySearchHistory(callback?: QuerySearchHistoryEvent): void-End-->

**系统能力：** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [QuerySearchHistoryEvent](arkts-avsession-avmusictemplate-querysearchhistoryevent-t.md) | 否 |

**错误码：**

| 错误码ID |
| --- |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [35000005](../errorcode-avmusictemplate.md#35000005-音频模板不存在) |
| [35000012](../errorcode-avmusictemplate.md#35000012-音频模板错误) |

## offRequestDialogInfo

```TypeScript
offRequestDialogInfo(callback?: RequestDialogInfoEvent): void
```

注销请求对话框信息的监听。

**起始版本：** 23

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-AVMusicTemplate-offRequestDialogInfo(callback?: RequestDialogInfoEvent): void--><!--Device-AVMusicTemplate-offRequestDialogInfo(callback?: RequestDialogInfoEvent): void-End-->

**系统能力：** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [RequestDialogInfoEvent](arkts-avsession-avmusictemplate-requestdialoginfoevent-t.md) | 否 |

**错误码：**

| 错误码ID |
| --- |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [35000005](../errorcode-avmusictemplate.md#35000005-音频模板不存在) |
| [35000012](../errorcode-avmusictemplate.md#35000012-音频模板错误) |

## offSettingsChange

```TypeScript
offSettingsChange(callback?: SettingsChangeEvent): void
```

注销设置改变事件的监听。

**起始版本：** 23

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-AVMusicTemplate-offSettingsChange(callback?: SettingsChangeEvent): void--><!--Device-AVMusicTemplate-offSettingsChange(callback?: SettingsChangeEvent): void-End-->

**系统能力：** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [SettingsChangeEvent](arkts-avsession-avmusictemplate-settingschangeevent-t.md) | 否 |

**错误码：**

| 错误码ID |
| --- |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [35000005](../errorcode-avmusictemplate.md#35000005-音频模板不存在) |
| [35000012](../errorcode-avmusictemplate.md#35000012-音频模板错误) |

## onClearSearchHistory

```TypeScript
onClearSearchHistory(callback: ClearSearchHistoryEvent): void
```

注册清除搜索历史的监听。使用callback异步回调。

**起始版本：** 23

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-AVMusicTemplate-onClearSearchHistory(callback: ClearSearchHistoryEvent): void--><!--Device-AVMusicTemplate-onClearSearchHistory(callback: ClearSearchHistoryEvent): void-End-->

**系统能力：** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [ClearSearchHistoryEvent](arkts-avsession-avmusictemplate-clearsearchhistoryevent-t.md) | 是 |

**错误码：**

| 错误码ID |
| --- |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [35000005](../errorcode-avmusictemplate.md#35000005-音频模板不存在) |
| [35000012](../errorcode-avmusictemplate.md#35000012-音频模板错误) |

## onDownloadMediaEntity

```TypeScript
onDownloadMediaEntity(callback: DownloadMediaEntityEvent): void
```

注册下载媒体实体事件的监听。使用callback异步回调。

**起始版本：** 23

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-AVMusicTemplate-onDownloadMediaEntity(callback: DownloadMediaEntityEvent): void--><!--Device-AVMusicTemplate-onDownloadMediaEntity(callback: DownloadMediaEntityEvent): void-End-->

**系统能力：** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [DownloadMediaEntityEvent](arkts-avsession-avmusictemplate-downloadmediaentityevent-t.md) | 是 |

**错误码：**

| 错误码ID |
| --- |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [35000005](../errorcode-avmusictemplate.md#35000005-音频模板不存在) |
| [35000012](../errorcode-avmusictemplate.md#35000012-音频模板错误) |

## onExecuteAction

```TypeScript
onExecuteAction(callback: ExecuteActionEvent): void
```

注册执行操作事件的监听。使用callback异步回调。

**起始版本：** 23

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-AVMusicTemplate-onExecuteAction(callback: ExecuteActionEvent): void--><!--Device-AVMusicTemplate-onExecuteAction(callback: ExecuteActionEvent): void-End-->

**系统能力：** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [ExecuteActionEvent](arkts-avsession-avmusictemplate-executeactionevent-t.md) | 是 |

**错误码：**

| 错误码ID |
| --- |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [35000005](../errorcode-avmusictemplate.md#35000005-音频模板不存在) |
| [35000012](../errorcode-avmusictemplate.md#35000012-音频模板错误) |

## onFavoriteMediaEntity

```TypeScript
onFavoriteMediaEntity(callback: FavoriteMediaEntityEvent): void
```

注册收藏媒体实体事件的监听。使用callback异步回调。

**起始版本：** 23

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-AVMusicTemplate-onFavoriteMediaEntity(callback: FavoriteMediaEntityEvent): void--><!--Device-AVMusicTemplate-onFavoriteMediaEntity(callback: FavoriteMediaEntityEvent): void-End-->

**系统能力：** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [FavoriteMediaEntityEvent](arkts-avsession-avmusictemplate-favoritemediaentityevent-t.md) | 是 |

**错误码：**

| 错误码ID |
| --- |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [35000005](../errorcode-avmusictemplate.md#35000005-音频模板不存在) |
| [35000012](../errorcode-avmusictemplate.md#35000012-音频模板错误) |

## onHandleMemberPurchase

```TypeScript
onHandleMemberPurchase(callback: HandleMemberPurchaseEvent): void
```

注册处理购买会员事件的监听。使用callback异步回调。

**起始版本：** 23

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-AVMusicTemplate-onHandleMemberPurchase(callback: HandleMemberPurchaseEvent): void--><!--Device-AVMusicTemplate-onHandleMemberPurchase(callback: HandleMemberPurchaseEvent): void-End-->

**系统能力：** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [HandleMemberPurchaseEvent](arkts-avsession-avmusictemplate-handlememberpurchaseevent-t.md) | 是 |

**错误码：**

| 错误码ID |
| --- |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [35000005](../errorcode-avmusictemplate.md#35000005-音频模板不存在) |
| [35000012](../errorcode-avmusictemplate.md#35000012-音频模板错误) |

## onLogin

```TypeScript
onLogin(callback: LoginEvent): void
```

注册登录事件的监听。使用callback异步回调。

**起始版本：** 23

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-AVMusicTemplate-onLogin(callback: LoginEvent): void--><!--Device-AVMusicTemplate-onLogin(callback: LoginEvent): void-End-->

**系统能力：** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [LoginEvent](arkts-avsession-avmusictemplate-loginevent-t.md) | 是 |

**错误码：**

| 错误码ID |
| --- |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [35000005](../errorcode-avmusictemplate.md#35000005-音频模板不存在) |
| [35000012](../errorcode-avmusictemplate.md#35000012-音频模板错误) |

## onPlayForSearch

```TypeScript
onPlayForSearch(callback: PlayForSearchEvent): void
```

注册搜播事件的监听。使用callback异步回调。

**起始版本：** 23

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-AVMusicTemplate-onPlayForSearch(callback: PlayForSearchEvent): void--><!--Device-AVMusicTemplate-onPlayForSearch(callback: PlayForSearchEvent): void-End-->

**系统能力：** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [PlayForSearchEvent](arkts-avsession-avmusictemplate-playforsearchevent-t.md) | 是 |

**错误码：**

| 错误码ID |
| --- |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [35000005](../errorcode-avmusictemplate.md#35000005-音频模板不存在) |
| [35000012](../errorcode-avmusictemplate.md#35000012-音频模板错误) |

## onPlayMediaEntity

```TypeScript
onPlayMediaEntity(callback: PlayMediaEntityEvent): void
```

注册播放媒体实体事件的监听。使用callback异步回调。

**起始版本：** 23

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-AVMusicTemplate-onPlayMediaEntity(callback: PlayMediaEntityEvent): void--><!--Device-AVMusicTemplate-onPlayMediaEntity(callback: PlayMediaEntityEvent): void-End-->

**系统能力：** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [PlayMediaEntityEvent](arkts-avsession-avmusictemplate-playmediaentityevent-t.md) | 是 |

**错误码：**

| 错误码ID |
| --- |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [35000005](../errorcode-avmusictemplate.md#35000005-音频模板不存在) |
| [35000012](../errorcode-avmusictemplate.md#35000012-音频模板错误) |

## onProblemAndAdvice

```TypeScript
onProblemAndAdvice(callback: ProblemAndAdviceEvent): void
```

注册问题与建议事件的监听。使用callback异步回调。

**起始版本：** 23

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-AVMusicTemplate-onProblemAndAdvice(callback: ProblemAndAdviceEvent): void--><!--Device-AVMusicTemplate-onProblemAndAdvice(callback: ProblemAndAdviceEvent): void-End-->

**系统能力：** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [ProblemAndAdviceEvent](arkts-avsession-avmusictemplate-problemandadviceevent-t.md) | 是 |

**错误码：**

| 错误码ID |
| --- |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [35000005](../errorcode-avmusictemplate.md#35000005-音频模板不存在) |
| [35000012](../errorcode-avmusictemplate.md#35000012-音频模板错误) |

## onQueryCompilation

```TypeScript
onQueryCompilation(callback: QueryCompilationEvent): void
```

注册查询合集的监听。使用callback异步回调。

**起始版本：** 23

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-AVMusicTemplate-onQueryCompilation(callback: QueryCompilationEvent): void--><!--Device-AVMusicTemplate-onQueryCompilation(callback: QueryCompilationEvent): void-End-->

**系统能力：** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [QueryCompilationEvent](arkts-avsession-avmusictemplate-querycompilationevent-t.md) | 是 |

**错误码：**

| 错误码ID |
| --- |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [35000005](../errorcode-avmusictemplate.md#35000005-音频模板不存在) |
| [35000012](../errorcode-avmusictemplate.md#35000012-音频模板错误) |

## onQueryCompilationByKeyword

```TypeScript
onQueryCompilationByKeyword(callback: QueryCompilationByKeywordEvent): void
```

注册按关键字查询合集的监听。使用callback异步回调。

**起始版本：** 23

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-AVMusicTemplate-onQueryCompilationByKeyword(callback: QueryCompilationByKeywordEvent): void--><!--Device-AVMusicTemplate-onQueryCompilationByKeyword(callback: QueryCompilationByKeywordEvent): void-End-->

**系统能力：** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [QueryCompilationByKeywordEvent](arkts-avsession-avmusictemplate-querycompilationbykeywordevent-t.md) | 是 |

**错误码：**

| 错误码ID |
| --- |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [35000005](../errorcode-avmusictemplate.md#35000005-音频模板不存在) |
| [35000012](../errorcode-avmusictemplate.md#35000012-音频模板错误) |

## onQueryCurrentSingle

```TypeScript
onQueryCurrentSingle(callback: QueryCurrentSingleEvent): void
```

注册查询当前单曲的监听。使用callback异步回调。

**起始版本：** 23

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-AVMusicTemplate-onQueryCurrentSingle(callback: QueryCurrentSingleEvent): void--><!--Device-AVMusicTemplate-onQueryCurrentSingle(callback: QueryCurrentSingleEvent): void-End-->

**系统能力：** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [QueryCurrentSingleEvent](arkts-avsession-avmusictemplate-querycurrentsingleevent-t.md) | 是 |

**错误码：**

| 错误码ID |
| --- |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [35000005](../errorcode-avmusictemplate.md#35000005-音频模板不存在) |
| [35000012](../errorcode-avmusictemplate.md#35000012-音频模板错误) |

## onQueryCustomContent

```TypeScript
onQueryCustomContent(callback: QueryCustomContentEvent): void
```

注册查询自定义内容事件的监听。使用callback异步回调。

**起始版本：** 23

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-AVMusicTemplate-onQueryCustomContent(callback: QueryCustomContentEvent): void--><!--Device-AVMusicTemplate-onQueryCustomContent(callback: QueryCustomContentEvent): void-End-->

**系统能力：** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [QueryCustomContentEvent](arkts-avsession-avmusictemplate-querycustomcontentevent-t.md) | 是 |

**错误码：**

| 错误码ID |
| --- |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [35000005](../errorcode-avmusictemplate.md#35000005-音频模板不存在) |
| [35000012](../errorcode-avmusictemplate.md#35000012-音频模板错误) |

## onQueryHotWords

```TypeScript
onQueryHotWords(callback: QueryHotWordsEvent): void
```

注册查询热词的监听。使用callback异步回调。

**起始版本：** 23

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-AVMusicTemplate-onQueryHotWords(callback: QueryHotWordsEvent): void--><!--Device-AVMusicTemplate-onQueryHotWords(callback: QueryHotWordsEvent): void-End-->

**系统能力：** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [QueryHotWordsEvent](arkts-avsession-avmusictemplate-queryhotwordsevent-t.md) | 是 |

**错误码：**

| 错误码ID |
| --- |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [35000005](../errorcode-avmusictemplate.md#35000005-音频模板不存在) |
| [35000012](../errorcode-avmusictemplate.md#35000012-音频模板错误) |

## onQueryMainTabs

```TypeScript
onQueryMainTabs(callback: QueryMainTabsEvent): void
```

注册查询主标签的事件监听。使用callback异步回调。

**起始版本：** 23

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-AVMusicTemplate-onQueryMainTabs(callback: QueryMainTabsEvent): void--><!--Device-AVMusicTemplate-onQueryMainTabs(callback: QueryMainTabsEvent): void-End-->

**系统能力：** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [QueryMainTabsEvent](arkts-avsession-avmusictemplate-querymaintabsevent-t.md) | 是 |

**错误码：**

| 错误码ID |
| --- |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [35000005](../errorcode-avmusictemplate.md#35000005-音频模板不存在) |
| [35000012](../errorcode-avmusictemplate.md#35000012-音频模板错误) |

## onQueryMediaEntity

```TypeScript
onQueryMediaEntity(callback: QueryMediaEntityEvent): void
```

注册查询媒体实体监听。使用callback异步回调。

**起始版本：** 23

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-AVMusicTemplate-onQueryMediaEntity(callback: QueryMediaEntityEvent): void--><!--Device-AVMusicTemplate-onQueryMediaEntity(callback: QueryMediaEntityEvent): void-End-->

**系统能力：** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [QueryMediaEntityEvent](arkts-avsession-avmusictemplate-querymediaentityevent-t.md) | 是 |

**错误码：**

| 错误码ID |
| --- |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [35000005](../errorcode-avmusictemplate.md#35000005-音频模板不存在) |
| [35000012](../errorcode-avmusictemplate.md#35000012-音频模板错误) |

## onQueryMediaEntityByKeyword

```TypeScript
onQueryMediaEntityByKeyword(callback: QueryMediaEntityByKeywordEvent): void
```

注册按关键字查询媒体实体的监听。使用callback异步回调。

**起始版本：** 23

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-AVMusicTemplate-onQueryMediaEntityByKeyword(callback: QueryMediaEntityByKeywordEvent): void--><!--Device-AVMusicTemplate-onQueryMediaEntityByKeyword(callback: QueryMediaEntityByKeywordEvent): void-End-->

**系统能力：** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [QueryMediaEntityByKeywordEvent](arkts-avsession-avmusictemplate-querymediaentitybykeywordevent-t.md) | 是 |

**错误码：**

| 错误码ID |
| --- |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [35000005](../errorcode-avmusictemplate.md#35000005-音频模板不存在) |
| [35000012](../errorcode-avmusictemplate.md#35000012-音频模板错误) |

## onQueryMediaTabContent

```TypeScript
onQueryMediaTabContent(callback: QueryMediaTabContentEvent): void
```

注册查询媒体标签内容事件监听。使用callback异步回调。

**起始版本：** 23

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-AVMusicTemplate-onQueryMediaTabContent(callback: QueryMediaTabContentEvent): void--><!--Device-AVMusicTemplate-onQueryMediaTabContent(callback: QueryMediaTabContentEvent): void-End-->

**系统能力：** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [QueryMediaTabContentEvent](arkts-avsession-avmusictemplate-querymediatabcontentevent-t.md) | 是 |

**错误码：**

| 错误码ID |
| --- |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [35000005](../errorcode-avmusictemplate.md#35000005-音频模板不存在) |
| [35000012](../errorcode-avmusictemplate.md#35000012-音频模板错误) |

## onQueryMemberPurchase

```TypeScript
onQueryMemberPurchase(callback: QueryMemberPurchaseEvent): void
```

注册查询购买会员事件的监听。使用callback异步回调。

**起始版本：** 23

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-AVMusicTemplate-onQueryMemberPurchase(callback: QueryMemberPurchaseEvent): void--><!--Device-AVMusicTemplate-onQueryMemberPurchase(callback: QueryMemberPurchaseEvent): void-End-->

**系统能力：** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [QueryMemberPurchaseEvent](arkts-avsession-avmusictemplate-querymemberpurchaseevent-t.md) | 是 |

**错误码：**

| 错误码ID |
| --- |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [35000005](../errorcode-avmusictemplate.md#35000005-音频模板不存在) |
| [35000012](../errorcode-avmusictemplate.md#35000012-音频模板错误) |

## onQueryPlaylist

```TypeScript
onQueryPlaylist(callback: QueryPlaylistEvent): void
```

注册查询播放列表的监听。使用callback异步回调。

**起始版本：** 23

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-AVMusicTemplate-onQueryPlaylist(callback: QueryPlaylistEvent): void--><!--Device-AVMusicTemplate-onQueryPlaylist(callback: QueryPlaylistEvent): void-End-->

**系统能力：** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [QueryPlaylistEvent](arkts-avsession-avmusictemplate-queryplaylistevent-t.md) | 是 |

**错误码：**

| 错误码ID |
| --- |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [35000005](../errorcode-avmusictemplate.md#35000005-音频模板不存在) |
| [35000012](../errorcode-avmusictemplate.md#35000012-音频模板错误) |

## onQueryRecommendMediaEntityList

```TypeScript
onQueryRecommendMediaEntityList(callback: QueryRecommendMediaEntityListEvent): void
```

注册查询推荐媒体列表的监听。使用callback异步回调。

**起始版本：** 23

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-AVMusicTemplate-onQueryRecommendMediaEntityList(callback: QueryRecommendMediaEntityListEvent): void--><!--Device-AVMusicTemplate-onQueryRecommendMediaEntityList(callback: QueryRecommendMediaEntityListEvent): void-End-->

**系统能力：** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [QueryRecommendMediaEntityListEvent](arkts-avsession-avmusictemplate-queryrecommendmediaentitylistevent-t.md) | 是 |

**错误码：**

| 错误码ID |
| --- |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [35000005](../errorcode-avmusictemplate.md#35000005-音频模板不存在) |
| [35000012](../errorcode-avmusictemplate.md#35000012-音频模板错误) |

## onQuerySearchHistory

```TypeScript
onQuerySearchHistory(callback: QuerySearchHistoryEvent): void
```

注册查询搜索历史的监听。使用callback异步回调。

**起始版本：** 23

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-AVMusicTemplate-onQuerySearchHistory(callback: QuerySearchHistoryEvent): void--><!--Device-AVMusicTemplate-onQuerySearchHistory(callback: QuerySearchHistoryEvent): void-End-->

**系统能力：** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [QuerySearchHistoryEvent](arkts-avsession-avmusictemplate-querysearchhistoryevent-t.md) | 是 |

**错误码：**

| 错误码ID |
| --- |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [35000005](../errorcode-avmusictemplate.md#35000005-音频模板不存在) |
| [35000012](../errorcode-avmusictemplate.md#35000012-音频模板错误) |

## onRequestDialogInfo

```TypeScript
onRequestDialogInfo(callback: RequestDialogInfoEvent): void
```

注册请求对话框信息的监听。使用callback异步回调。

**起始版本：** 23

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-AVMusicTemplate-onRequestDialogInfo(callback: RequestDialogInfoEvent): void--><!--Device-AVMusicTemplate-onRequestDialogInfo(callback: RequestDialogInfoEvent): void-End-->

**系统能力：** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [RequestDialogInfoEvent](arkts-avsession-avmusictemplate-requestdialoginfoevent-t.md) | 是 |

**错误码：**

| 错误码ID |
| --- |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [35000005](../errorcode-avmusictemplate.md#35000005-音频模板不存在) |
| [35000012](../errorcode-avmusictemplate.md#35000012-音频模板错误) |

## onSettingsChange

```TypeScript
onSettingsChange(callback: SettingsChangeEvent): void
```

注册设置改变事件的监听。使用callback异步回调。

**起始版本：** 23

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-AVMusicTemplate-onSettingsChange(callback: SettingsChangeEvent): void--><!--Device-AVMusicTemplate-onSettingsChange(callback: SettingsChangeEvent): void-End-->

**系统能力：** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [SettingsChangeEvent](arkts-avsession-avmusictemplate-settingschangeevent-t.md) | 是 |

**错误码：**

| 错误码ID |
| --- |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [35000005](../errorcode-avmusictemplate.md#35000005-音频模板不存在) |
| [35000012](../errorcode-avmusictemplate.md#35000012-音频模板错误) |

## reportExecuteAction

```TypeScript
reportExecuteAction(actionType: string, params: string): Promise<void>
```

向音频模板控制方同步执行操作信息。使用Promise异步回调。

**起始版本：** 23

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-AVMusicTemplate-reportExecuteAction(actionType: string, params: string): Promise<void>--><!--Device-AVMusicTemplate-reportExecuteAction(actionType: string, params: string): Promise<void>-End-->

**系统能力：** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| actionType | string | 是 |
| params | string | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;void&gt; |

**错误码：**

| 错误码ID |
| --- |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [35000005](../errorcode-avmusictemplate.md#35000005-音频模板不存在) |
| [35000011](../errorcode-avmusictemplate.md#35000011-数据写入错误数据无效) |

## setCurrentSingle

```TypeScript
setCurrentSingle(single: Single): Promise<void>
```

向音频模板控制方同步当前单曲。使用Promise异步回调。

**起始版本：** 23

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-AVMusicTemplate-setCurrentSingle(single: Single): Promise<void>--><!--Device-AVMusicTemplate-setCurrentSingle(single: Single): Promise<void>-End-->

**系统能力：** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| single | [Single](arkts-avsession-avmusictemplate-single-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;void&gt; |

**错误码：**

| 错误码ID |
| --- |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [35000005](../errorcode-avmusictemplate.md#35000005-音频模板不存在) |
| [35000011](../errorcode-avmusictemplate.md#35000011-数据写入错误数据无效) |

## setCustomElements

```TypeScript
setCustomElements(actionType: ActionType, customType: CustomType,
      customElement: CustomElement): Promise<void>
```

上报自定义数据变更信息至媒体中心

**起始版本：** 23

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-AVMusicTemplate-setCustomElements(actionType: ActionType, customType: CustomType,      customElement: CustomElement): Promise<void>--><!--Device-AVMusicTemplate-setCustomElements(actionType: ActionType, customType: CustomType,      customElement: CustomElement): Promise<void>-End-->

**系统能力：** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| actionType | [ActionType](../../apis-data-protection-kit/arkts-apis/arkts-dataprotection-dlppermission-actiontype-e.md) | 是 |
| customType | [CustomType](arkts-avsession-avmusictemplate-customtype-t.md) | 是 |
| customElement | [CustomElement](arkts-avsession-avmusictemplate-customelement-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;void&gt; |

**错误码：**

| 错误码ID |
| --- |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [35000005](../errorcode-avmusictemplate.md#35000005-音频模板不存在) |
| [35000011](../errorcode-avmusictemplate.md#35000011-数据写入错误数据无效) |

## setDialogCommand

```TypeScript
setDialogCommand(type: DialogControlType, dialogInfo: DialogInfo): Promise<void>
```

向音频模板控制方同步对话框命令。使用Promise异步回调。

**起始版本：** 23

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-AVMusicTemplate-setDialogCommand(type: DialogControlType, dialogInfo: DialogInfo): Promise<void>--><!--Device-AVMusicTemplate-setDialogCommand(type: DialogControlType, dialogInfo: DialogInfo): Promise<void>-End-->

**系统能力：** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | [DialogControlType](arkts-avsession-avmusictemplate-dialogcontroltype-t.md) | 是 |
| dialogInfo | [DialogInfo](arkts-avsession-avmusictemplate-dialoginfo-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;void&gt; |

**错误码：**

| 错误码ID |
| --- |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [35000005](../errorcode-avmusictemplate.md#35000005-音频模板不存在) |
| [35000011](../errorcode-avmusictemplate.md#35000011-数据写入错误数据无效) |

## setDownloadMediaEntityStatus

```TypeScript
setDownloadMediaEntityStatus(single: MediaEntity): Promise<void>
```

向音频模板控制方同步单曲下载状态信息。使用Promise异步回调。

**起始版本：** 23

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-AVMusicTemplate-setDownloadMediaEntityStatus(single: MediaEntity): Promise<void>--><!--Device-AVMusicTemplate-setDownloadMediaEntityStatus(single: MediaEntity): Promise<void>-End-->

**系统能力：** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| single | [MediaEntity](arkts-avsession-avmusictemplate-mediaentity-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;void&gt; |

**错误码：**

| 错误码ID |
| --- |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [35000005](../errorcode-avmusictemplate.md#35000005-音频模板不存在) |
| [35000011](../errorcode-avmusictemplate.md#35000011-数据写入错误数据无效) |

## setExtensionAbility

```TypeScript
setExtensionAbility(want: WantAgent): Promise<void>
```

向音频模板控制方同步用于被拉起的Ability。使用Promise异步回调。

**起始版本：** 23

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-AVMusicTemplate-setExtensionAbility(want: WantAgent): Promise<void>--><!--Device-AVMusicTemplate-setExtensionAbility(want: WantAgent): Promise<void>-End-->

**系统能力：** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| want | [WantAgent](../../apis-ability-kit/arkts-apis/arkts-ability-wantagent-t.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;void&gt; |

**错误码：**

| 错误码ID |
| --- |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [35000005](../errorcode-avmusictemplate.md#35000005-音频模板不存在) |
| [35000011](../errorcode-avmusictemplate.md#35000011-数据写入错误数据无效) |

## setMediaEntities

```TypeScript
setMediaEntities(entities: MediaEntity[]): Promise<void>
```

向音频模板控制方同步媒体资源变更信息。使用Promise异步回调。

**起始版本：** 23

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-AVMusicTemplate-setMediaEntities(entities: MediaEntity[]): Promise<void>--><!--Device-AVMusicTemplate-setMediaEntities(entities: MediaEntity[]): Promise<void>-End-->

**系统能力：** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| entities | [MediaEntity](arkts-avsession-avmusictemplate-mediaentity-i.md)[] | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;void&gt; |

**错误码：**

| 错误码ID |
| --- |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [35000005](../errorcode-avmusictemplate.md#35000005-音频模板不存在) |
| [35000011](../errorcode-avmusictemplate.md#35000011-数据写入错误数据无效) |

## setPlaylist

```TypeScript
setPlaylist(playlist: PageMediaEntity): Promise<void>
```

向音频模板控制方同步播放列表。使用Promise异步回调。

**起始版本：** 23

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-AVMusicTemplate-setPlaylist(playlist: PageMediaEntity): Promise<void>--><!--Device-AVMusicTemplate-setPlaylist(playlist: PageMediaEntity): Promise<void>-End-->

**系统能力：** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| playlist | [PageMediaEntity](arkts-avsession-avmusictemplate-pagemediaentity-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;void&gt; |

**错误码：**

| 错误码ID |
| --- |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [35000005](../errorcode-avmusictemplate.md#35000005-音频模板不存在) |
| [35000011](../errorcode-avmusictemplate.md#35000011-数据写入错误数据无效) |

## setSettings

```TypeScript
setSettings(settingItems: SettingItem[]): Promise<void>
```

向音频模板控制方同步设置信息。使用Promise异步回调。

**起始版本：** 23

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-AVMusicTemplate-setSettings(settingItems: SettingItem[]): Promise<void>--><!--Device-AVMusicTemplate-setSettings(settingItems: SettingItem[]): Promise<void>-End-->

**系统能力：** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| settingItems | [SettingItem](arkts-avsession-avmusictemplate-settingitem-i.md)[] | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;void&gt; |

**错误码：**

| 错误码ID |
| --- |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [35000005](../errorcode-avmusictemplate.md#35000005-音频模板不存在) |
| [35000011](../errorcode-avmusictemplate.md#35000011-数据写入错误数据无效) |

## setTabContent

```TypeScript
setTabContent(tabId: string, tabContent: MediaTabContent): Promise<void>
```

向音频模板控制方同步标签页内容信息。使用Promise异步回调。

**起始版本：** 23

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-AVMusicTemplate-setTabContent(tabId: string, tabContent: MediaTabContent): Promise<void>--><!--Device-AVMusicTemplate-setTabContent(tabId: string, tabContent: MediaTabContent): Promise<void>-End-->

**系统能力：** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| tabId | string | 是 |
| tabContent | [MediaTabContent](arkts-avsession-avmusictemplate-mediatabcontent-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;void&gt; |

**错误码：**

| 错误码ID |
| --- |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [35000005](../errorcode-avmusictemplate.md#35000005-音频模板不存在) |
| [35000011](../errorcode-avmusictemplate.md#35000011-数据写入错误数据无效) |

## setUserInfo

```TypeScript
setUserInfo(userInfo: UserInfo): Promise<void>
```

向音频模板控制方同步用户信息。使用Promise异步回调。

**起始版本：** 23

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-AVMusicTemplate-setUserInfo(userInfo: UserInfo): Promise<void>--><!--Device-AVMusicTemplate-setUserInfo(userInfo: UserInfo): Promise<void>-End-->

**系统能力：** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| userInfo | [UserInfo](../../apis-arkdata/arkts-apis/arkts-arkdata-distributeddata-userinfo-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;void&gt; |

**错误码：**

| 错误码ID |
| --- |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [35000005](../errorcode-avmusictemplate.md#35000005-音频模板不存在) |
| [35000011](../errorcode-avmusictemplate.md#35000011-数据写入错误数据无效) |

## startTemplate

```TypeScript
startTemplate(): Promise<OperResult>
```

启动音频模板界面。使用Promise异步回调。

**起始版本：** 23

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-AVMusicTemplate-startTemplate(): Promise<OperResult>--><!--Device-AVMusicTemplate-startTemplate(): Promise<OperResult>-End-->

**系统能力：** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**返回值：**

| 类型 |
| --- |
| Promise&lt;OperResult&gt; |

**错误码：**

| 错误码ID |
| --- |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |

## sessionId

```TypeScript
sessionId: string
```

音频模板唯一的标识。

**类型：** string

**起始版本：** 23

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-AVMusicTemplate-sessionId: string--><!--Device-AVMusicTemplate-sessionId: string-End-->

**系统能力：** SystemCapability.Multimedia.AVSession.AVMusicTemplate

## sessionTag

```TypeScript
sessionTag: string
```

音频模板标签。

**类型：** string

**起始版本：** 23

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-AVMusicTemplate-sessionTag: string--><!--Device-AVMusicTemplate-sessionTag: string-End-->

**系统能力：** SystemCapability.Multimedia.AVSession.AVMusicTemplate
