# AVMusicTemplate

AVMusicTemplate interface

**Since:** 23

<!--Device-avMusicTemplate-class AVMusicTemplate--><!--Device-avMusicTemplate-class AVMusicTemplate-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVMusicTemplate

## Modules to Import

```TypeScript
import { avMusicTemplate } from '@kit.AVSessionKit';
```

## destroy

```TypeScript
destroy(): Promise<void>
```

Destroy the AVMusicTemplate instance.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-AVMusicTemplate-destroy(): Promise<void>--><!--Device-AVMusicTemplate-destroy(): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#801-ad-request-failure) |

## offClearSearchHistory

```TypeScript
offClearSearchHistory(callback?: ClearSearchHistoryEvent): void
```

Unregister clear search history callback.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-AVMusicTemplate-offClearSearchHistory(callback?: ClearSearchHistoryEvent): void--><!--Device-AVMusicTemplate-offClearSearchHistory(callback?: ClearSearchHistoryEvent): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [ClearSearchHistoryEvent](arkts-avsession-avmusictemplate-clearsearchhistoryevent-t.md) | No |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#801-ad-request-failure) |
| [35000005](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-avsession-kit/errorcode-avmusictemplate.md#35000005-audio-template-does-not-exist) |
| 35000012 |

## offCustomCommand

```TypeScript
offCustomCommand(callback?: CustomCommandEvent): void
```

Unregister custom command callback.

**Since:** 26.1.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-AVMusicTemplate-offCustomCommand(callback?: CustomCommandEvent): void--><!--Device-AVMusicTemplate-offCustomCommand(callback?: CustomCommandEvent): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [CustomCommandEvent](arkts-avsession-avmusictemplate-customcommandevent-t.md) | No |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#801-ad-request-failure) |
| [35000005](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-avsession-kit/errorcode-avmusictemplate.md#35000005-audio-template-does-not-exist) |
| 35000012 |

## offDownloadMediaEntity

```TypeScript
offDownloadMediaEntity(callback?: DownloadMediaEntityEvent): void
```

Unregister download media entity callback.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-AVMusicTemplate-offDownloadMediaEntity(callback?: DownloadMediaEntityEvent): void--><!--Device-AVMusicTemplate-offDownloadMediaEntity(callback?: DownloadMediaEntityEvent): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [DownloadMediaEntityEvent](arkts-avsession-avmusictemplate-downloadmediaentityevent-t.md) | No |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#801-ad-request-failure) |
| [35000005](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-avsession-kit/errorcode-avmusictemplate.md#35000005-audio-template-does-not-exist) |
| 35000012 |

## offExecuteAction

```TypeScript
offExecuteAction(callback?: ExecuteActionEvent): void
```

Unregister execute action callback.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-AVMusicTemplate-offExecuteAction(callback?: ExecuteActionEvent): void--><!--Device-AVMusicTemplate-offExecuteAction(callback?: ExecuteActionEvent): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [ExecuteActionEvent](arkts-avsession-avmusictemplate-executeactionevent-t.md) | No |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#801-ad-request-failure) |
| [35000005](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-avsession-kit/errorcode-avmusictemplate.md#35000005-audio-template-does-not-exist) |
| 35000012 |

## offFavoriteMediaEntity

```TypeScript
offFavoriteMediaEntity(callback?: FavoriteMediaEntityEvent): void
```

Unregister favorite media entity callback.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-AVMusicTemplate-offFavoriteMediaEntity(callback?: FavoriteMediaEntityEvent): void--><!--Device-AVMusicTemplate-offFavoriteMediaEntity(callback?: FavoriteMediaEntityEvent): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [FavoriteMediaEntityEvent](arkts-avsession-avmusictemplate-favoritemediaentityevent-t.md) | No |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#801-ad-request-failure) |
| [35000005](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-avsession-kit/errorcode-avmusictemplate.md#35000005-audio-template-does-not-exist) |
| 35000012 |

## offHandleMemberPurchase

```TypeScript
offHandleMemberPurchase(callback?: HandleMemberPurchaseEvent): void
```

Unregister handle member purchase callback.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-AVMusicTemplate-offHandleMemberPurchase(callback?: HandleMemberPurchaseEvent): void--><!--Device-AVMusicTemplate-offHandleMemberPurchase(callback?: HandleMemberPurchaseEvent): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [HandleMemberPurchaseEvent](arkts-avsession-avmusictemplate-handlememberpurchaseevent-t.md) | No |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#801-ad-request-failure) |
| [35000005](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-avsession-kit/errorcode-avmusictemplate.md#35000005-audio-template-does-not-exist) |
| 35000012 |

## offLogin

```TypeScript
offLogin(callback?: LoginEvent): void
```

Unregister login callback.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-AVMusicTemplate-offLogin(callback?: LoginEvent): void--><!--Device-AVMusicTemplate-offLogin(callback?: LoginEvent): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [LoginEvent](arkts-avsession-avmusictemplate-loginevent-t.md) | No |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#801-ad-request-failure) |
| [35000005](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-avsession-kit/errorcode-avmusictemplate.md#35000005-audio-template-does-not-exist) |
| 35000012 |

## offPlayForSearch

```TypeScript
offPlayForSearch(callback?: PlayForSearchEvent): void
```

Unregister play for search callback.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-AVMusicTemplate-offPlayForSearch(callback?: PlayForSearchEvent): void--><!--Device-AVMusicTemplate-offPlayForSearch(callback?: PlayForSearchEvent): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [PlayForSearchEvent](arkts-avsession-avmusictemplate-playforsearchevent-t.md) | No |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#801-ad-request-failure) |
| [35000005](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-avsession-kit/errorcode-avmusictemplate.md#35000005-audio-template-does-not-exist) |
| 35000012 |

## offPlayMediaEntity

```TypeScript
offPlayMediaEntity(callback?: PlayMediaEntityEvent): void
```

Unregister play media entity callback.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-AVMusicTemplate-offPlayMediaEntity(callback?: PlayMediaEntityEvent): void--><!--Device-AVMusicTemplate-offPlayMediaEntity(callback?: PlayMediaEntityEvent): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [PlayMediaEntityEvent](arkts-avsession-avmusictemplate-playmediaentityevent-t.md) | No |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#801-ad-request-failure) |
| [35000005](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-avsession-kit/errorcode-avmusictemplate.md#35000005-audio-template-does-not-exist) |
| 35000012 |

## offProblemAndAdvice

```TypeScript
offProblemAndAdvice(callback?: ProblemAndAdviceEvent): void
```

Unregister problem and advice callback.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-AVMusicTemplate-offProblemAndAdvice(callback?: ProblemAndAdviceEvent): void--><!--Device-AVMusicTemplate-offProblemAndAdvice(callback?: ProblemAndAdviceEvent): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [ProblemAndAdviceEvent](arkts-avsession-avmusictemplate-problemandadviceevent-t.md) | No |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#801-ad-request-failure) |
| [35000005](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-avsession-kit/errorcode-avmusictemplate.md#35000005-audio-template-does-not-exist) |
| 35000012 |

## offQueryCompilation

```TypeScript
offQueryCompilation(callback?: QueryCompilationEvent): void
```

Unregister query compilation callback.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-AVMusicTemplate-offQueryCompilation(callback?: QueryCompilationEvent): void--><!--Device-AVMusicTemplate-offQueryCompilation(callback?: QueryCompilationEvent): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [QueryCompilationEvent](arkts-avsession-avmusictemplate-querycompilationevent-t.md) | No |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#801-ad-request-failure) |
| [35000005](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-avsession-kit/errorcode-avmusictemplate.md#35000005-audio-template-does-not-exist) |
| 35000012 |

## offQueryCompilationByKeyword

```TypeScript
offQueryCompilationByKeyword(callback?: QueryCompilationByKeywordEvent): void
```

Unregister query compilation by keyword callback.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-AVMusicTemplate-offQueryCompilationByKeyword(callback?: QueryCompilationByKeywordEvent): void--><!--Device-AVMusicTemplate-offQueryCompilationByKeyword(callback?: QueryCompilationByKeywordEvent): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [QueryCompilationByKeywordEvent](arkts-avsession-avmusictemplate-querycompilationbykeywordevent-t.md) | No |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#801-ad-request-failure) |
| [35000005](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-avsession-kit/errorcode-avmusictemplate.md#35000005-audio-template-does-not-exist) |
| 35000012 |

## offQueryCurrentSingle

```TypeScript
offQueryCurrentSingle(callback?: QueryCurrentSingleEvent): void
```

Unregister query current single callback.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-AVMusicTemplate-offQueryCurrentSingle(callback?: QueryCurrentSingleEvent): void--><!--Device-AVMusicTemplate-offQueryCurrentSingle(callback?: QueryCurrentSingleEvent): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [QueryCurrentSingleEvent](arkts-avsession-avmusictemplate-querycurrentsingleevent-t.md) | No |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#801-ad-request-failure) |
| [35000005](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-avsession-kit/errorcode-avmusictemplate.md#35000005-audio-template-does-not-exist) |
| 35000012 |

## offQueryCustomContent

```TypeScript
offQueryCustomContent(callback?: QueryCustomContentEvent): void
```

Unregister query custom content callback.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-AVMusicTemplate-offQueryCustomContent(callback?: QueryCustomContentEvent): void--><!--Device-AVMusicTemplate-offQueryCustomContent(callback?: QueryCustomContentEvent): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [QueryCustomContentEvent](arkts-avsession-avmusictemplate-querycustomcontentevent-t.md) | No |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#801-ad-request-failure) |
| [35000005](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-avsession-kit/errorcode-avmusictemplate.md#35000005-audio-template-does-not-exist) |
| 35000012 |

## offQueryHotWords

```TypeScript
offQueryHotWords(callback?: QueryHotWordsEvent): void
```

Unregister query hot words callback.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-AVMusicTemplate-offQueryHotWords(callback?: QueryHotWordsEvent): void--><!--Device-AVMusicTemplate-offQueryHotWords(callback?: QueryHotWordsEvent): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [QueryHotWordsEvent](arkts-avsession-avmusictemplate-queryhotwordsevent-t.md) | No |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#801-ad-request-failure) |
| [35000005](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-avsession-kit/errorcode-avmusictemplate.md#35000005-audio-template-does-not-exist) |
| 35000012 |

## offQueryMainTabs

```TypeScript
offQueryMainTabs(callback?: QueryMainTabsEvent): void
```

Unregister query main tabs callback.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-AVMusicTemplate-offQueryMainTabs(callback?: QueryMainTabsEvent): void--><!--Device-AVMusicTemplate-offQueryMainTabs(callback?: QueryMainTabsEvent): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [QueryMainTabsEvent](arkts-avsession-avmusictemplate-querymaintabsevent-t.md) | No |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#801-ad-request-failure) |
| [35000005](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-avsession-kit/errorcode-avmusictemplate.md#35000005-audio-template-does-not-exist) |
| 35000012 |

## offQueryMediaEntity

```TypeScript
offQueryMediaEntity(callback?: QueryMediaEntityEvent): void
```

Unregister query media entity callback.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-AVMusicTemplate-offQueryMediaEntity(callback?: QueryMediaEntityEvent): void--><!--Device-AVMusicTemplate-offQueryMediaEntity(callback?: QueryMediaEntityEvent): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [QueryMediaEntityEvent](arkts-avsession-avmusictemplate-querymediaentityevent-t.md) | No |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#801-ad-request-failure) |
| [35000005](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-avsession-kit/errorcode-avmusictemplate.md#35000005-audio-template-does-not-exist) |
| 35000012 |

## offQueryMediaEntityByKeyword

```TypeScript
offQueryMediaEntityByKeyword(callback?: QueryMediaEntityByKeywordEvent): void
```

Unregister query media entity by keyword callback.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-AVMusicTemplate-offQueryMediaEntityByKeyword(callback?: QueryMediaEntityByKeywordEvent): void--><!--Device-AVMusicTemplate-offQueryMediaEntityByKeyword(callback?: QueryMediaEntityByKeywordEvent): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [QueryMediaEntityByKeywordEvent](arkts-avsession-avmusictemplate-querymediaentitybykeywordevent-t.md) | No |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#801-ad-request-failure) |
| [35000005](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-avsession-kit/errorcode-avmusictemplate.md#35000005-audio-template-does-not-exist) |
| 35000012 |

## offQueryMediaTabContent

```TypeScript
offQueryMediaTabContent(callback?: QueryMediaTabContentEvent): void
```

Unregister query media tab content callback.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-AVMusicTemplate-offQueryMediaTabContent(callback?: QueryMediaTabContentEvent): void--><!--Device-AVMusicTemplate-offQueryMediaTabContent(callback?: QueryMediaTabContentEvent): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [QueryMediaTabContentEvent](arkts-avsession-avmusictemplate-querymediatabcontentevent-t.md) | No |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#801-ad-request-failure) |
| [35000005](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-avsession-kit/errorcode-avmusictemplate.md#35000005-audio-template-does-not-exist) |
| 35000012 |

## offQueryMemberPurchase

```TypeScript
offQueryMemberPurchase(callback?: QueryMemberPurchaseEvent): void
```

Unregister query member purchase callback.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-AVMusicTemplate-offQueryMemberPurchase(callback?: QueryMemberPurchaseEvent): void--><!--Device-AVMusicTemplate-offQueryMemberPurchase(callback?: QueryMemberPurchaseEvent): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [QueryMemberPurchaseEvent](arkts-avsession-avmusictemplate-querymemberpurchaseevent-t.md) | No |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#801-ad-request-failure) |
| [35000005](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-avsession-kit/errorcode-avmusictemplate.md#35000005-audio-template-does-not-exist) |
| 35000012 |

## offQueryPlaylist

```TypeScript
offQueryPlaylist(callback?: QueryPlaylistEvent): void
```

Unregister query playlist callback.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-AVMusicTemplate-offQueryPlaylist(callback?: QueryPlaylistEvent): void--><!--Device-AVMusicTemplate-offQueryPlaylist(callback?: QueryPlaylistEvent): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [QueryPlaylistEvent](arkts-avsession-avmusictemplate-queryplaylistevent-t.md) | No |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#801-ad-request-failure) |
| [35000005](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-avsession-kit/errorcode-avmusictemplate.md#35000005-audio-template-does-not-exist) |
| 35000012 |

## offQueryRecommendMediaEntityList

```TypeScript
offQueryRecommendMediaEntityList(callback?: QueryRecommendMediaEntityListEvent): void
```

Unregister query recommend media entity list callback.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-AVMusicTemplate-offQueryRecommendMediaEntityList(callback?: QueryRecommendMediaEntityListEvent): void--><!--Device-AVMusicTemplate-offQueryRecommendMediaEntityList(callback?: QueryRecommendMediaEntityListEvent): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [QueryRecommendMediaEntityListEvent](arkts-avsession-avmusictemplate-queryrecommendmediaentitylistevent-t.md) | No |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#801-ad-request-failure) |
| [35000005](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-avsession-kit/errorcode-avmusictemplate.md#35000005-audio-template-does-not-exist) |
| 35000012 |

## offQuerySearchHistory

```TypeScript
offQuerySearchHistory(callback?: QuerySearchHistoryEvent): void
```

Unregister query search history callback.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-AVMusicTemplate-offQuerySearchHistory(callback?: QuerySearchHistoryEvent): void--><!--Device-AVMusicTemplate-offQuerySearchHistory(callback?: QuerySearchHistoryEvent): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [QuerySearchHistoryEvent](arkts-avsession-avmusictemplate-querysearchhistoryevent-t.md) | No |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#801-ad-request-failure) |
| [35000005](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-avsession-kit/errorcode-avmusictemplate.md#35000005-audio-template-does-not-exist) |
| 35000012 |

## offRequestDialogInfo

```TypeScript
offRequestDialogInfo(callback?: RequestDialogInfoEvent): void
```

Unregister request dialog info callback.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-AVMusicTemplate-offRequestDialogInfo(callback?: RequestDialogInfoEvent): void--><!--Device-AVMusicTemplate-offRequestDialogInfo(callback?: RequestDialogInfoEvent): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [RequestDialogInfoEvent](arkts-avsession-avmusictemplate-requestdialoginfoevent-t.md) | No |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#801-ad-request-failure) |
| [35000005](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-avsession-kit/errorcode-avmusictemplate.md#35000005-audio-template-does-not-exist) |
| 35000012 |

## offSettingsChange

```TypeScript
offSettingsChange(callback?: SettingsChangeEvent): void
```

Unregister settings change callback.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-AVMusicTemplate-offSettingsChange(callback?: SettingsChangeEvent): void--><!--Device-AVMusicTemplate-offSettingsChange(callback?: SettingsChangeEvent): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [SettingsChangeEvent](arkts-avsession-avmusictemplate-settingschangeevent-t.md) | No |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#801-ad-request-failure) |
| [35000005](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-avsession-kit/errorcode-avmusictemplate.md#35000005-audio-template-does-not-exist) |
| 35000012 |

## onClearSearchHistory

```TypeScript
onClearSearchHistory(callback: ClearSearchHistoryEvent): void
```

Register clear search history callback.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-AVMusicTemplate-onClearSearchHistory(callback: ClearSearchHistoryEvent): void--><!--Device-AVMusicTemplate-onClearSearchHistory(callback: ClearSearchHistoryEvent): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [ClearSearchHistoryEvent](arkts-avsession-avmusictemplate-clearsearchhistoryevent-t.md) | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#801-ad-request-failure) |
| [35000005](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-avsession-kit/errorcode-avmusictemplate.md#35000005-audio-template-does-not-exist) |
| 35000012 |

## onCustomCommand

```TypeScript
onCustomCommand(callback: CustomCommandEvent): void
```

Register custom command callback.

**Since:** 26.1.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-AVMusicTemplate-onCustomCommand(callback: CustomCommandEvent): void--><!--Device-AVMusicTemplate-onCustomCommand(callback: CustomCommandEvent): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [CustomCommandEvent](arkts-avsession-avmusictemplate-customcommandevent-t.md) | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#801-ad-request-failure) |
| [35000005](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-avsession-kit/errorcode-avmusictemplate.md#35000005-audio-template-does-not-exist) |
| 35000012 |

## onDownloadMediaEntity

```TypeScript
onDownloadMediaEntity(callback: DownloadMediaEntityEvent): void
```

Register download media entity callback.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-AVMusicTemplate-onDownloadMediaEntity(callback: DownloadMediaEntityEvent): void--><!--Device-AVMusicTemplate-onDownloadMediaEntity(callback: DownloadMediaEntityEvent): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [DownloadMediaEntityEvent](arkts-avsession-avmusictemplate-downloadmediaentityevent-t.md) | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#801-ad-request-failure) |
| [35000005](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-avsession-kit/errorcode-avmusictemplate.md#35000005-audio-template-does-not-exist) |
| 35000012 |

## onExecuteAction

```TypeScript
onExecuteAction(callback: ExecuteActionEvent): void
```

Register execute action callback.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-AVMusicTemplate-onExecuteAction(callback: ExecuteActionEvent): void--><!--Device-AVMusicTemplate-onExecuteAction(callback: ExecuteActionEvent): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [ExecuteActionEvent](arkts-avsession-avmusictemplate-executeactionevent-t.md) | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#801-ad-request-failure) |
| [35000005](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-avsession-kit/errorcode-avmusictemplate.md#35000005-audio-template-does-not-exist) |
| 35000012 |

## onFavoriteMediaEntity

```TypeScript
onFavoriteMediaEntity(callback: FavoriteMediaEntityEvent): void
```

Register favorite media entity callback.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-AVMusicTemplate-onFavoriteMediaEntity(callback: FavoriteMediaEntityEvent): void--><!--Device-AVMusicTemplate-onFavoriteMediaEntity(callback: FavoriteMediaEntityEvent): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [FavoriteMediaEntityEvent](arkts-avsession-avmusictemplate-favoritemediaentityevent-t.md) | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#801-ad-request-failure) |
| [35000005](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-avsession-kit/errorcode-avmusictemplate.md#35000005-audio-template-does-not-exist) |
| 35000012 |

## onHandleMemberPurchase

```TypeScript
onHandleMemberPurchase(callback: HandleMemberPurchaseEvent): void
```

Register handle member purchase callback.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-AVMusicTemplate-onHandleMemberPurchase(callback: HandleMemberPurchaseEvent): void--><!--Device-AVMusicTemplate-onHandleMemberPurchase(callback: HandleMemberPurchaseEvent): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [HandleMemberPurchaseEvent](arkts-avsession-avmusictemplate-handlememberpurchaseevent-t.md) | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#801-ad-request-failure) |
| [35000005](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-avsession-kit/errorcode-avmusictemplate.md#35000005-audio-template-does-not-exist) |
| 35000012 |

## onLogin

```TypeScript
onLogin(callback: LoginEvent): void
```

Register login callback.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-AVMusicTemplate-onLogin(callback: LoginEvent): void--><!--Device-AVMusicTemplate-onLogin(callback: LoginEvent): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [LoginEvent](arkts-avsession-avmusictemplate-loginevent-t.md) | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#801-ad-request-failure) |
| [35000005](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-avsession-kit/errorcode-avmusictemplate.md#35000005-audio-template-does-not-exist) |
| 35000012 |

## onPlayForSearch

```TypeScript
onPlayForSearch(callback: PlayForSearchEvent): void
```

Register play for search callback.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-AVMusicTemplate-onPlayForSearch(callback: PlayForSearchEvent): void--><!--Device-AVMusicTemplate-onPlayForSearch(callback: PlayForSearchEvent): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [PlayForSearchEvent](arkts-avsession-avmusictemplate-playforsearchevent-t.md) | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#801-ad-request-failure) |
| [35000005](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-avsession-kit/errorcode-avmusictemplate.md#35000005-audio-template-does-not-exist) |
| 35000012 |

## onPlayMediaEntity

```TypeScript
onPlayMediaEntity(callback: PlayMediaEntityEvent): void
```

Register play media entity callback.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-AVMusicTemplate-onPlayMediaEntity(callback: PlayMediaEntityEvent): void--><!--Device-AVMusicTemplate-onPlayMediaEntity(callback: PlayMediaEntityEvent): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [PlayMediaEntityEvent](arkts-avsession-avmusictemplate-playmediaentityevent-t.md) | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#801-ad-request-failure) |
| [35000005](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-avsession-kit/errorcode-avmusictemplate.md#35000005-audio-template-does-not-exist) |
| 35000012 |

## onProblemAndAdvice

```TypeScript
onProblemAndAdvice(callback: ProblemAndAdviceEvent): void
```

Register problem and advice callback.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-AVMusicTemplate-onProblemAndAdvice(callback: ProblemAndAdviceEvent): void--><!--Device-AVMusicTemplate-onProblemAndAdvice(callback: ProblemAndAdviceEvent): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [ProblemAndAdviceEvent](arkts-avsession-avmusictemplate-problemandadviceevent-t.md) | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#801-ad-request-failure) |
| [35000005](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-avsession-kit/errorcode-avmusictemplate.md#35000005-audio-template-does-not-exist) |
| 35000012 |

## onQueryCompilation

```TypeScript
onQueryCompilation(callback: QueryCompilationEvent): void
```

Register query compilation callback.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-AVMusicTemplate-onQueryCompilation(callback: QueryCompilationEvent): void--><!--Device-AVMusicTemplate-onQueryCompilation(callback: QueryCompilationEvent): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [QueryCompilationEvent](arkts-avsession-avmusictemplate-querycompilationevent-t.md) | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#801-ad-request-failure) |
| [35000005](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-avsession-kit/errorcode-avmusictemplate.md#35000005-audio-template-does-not-exist) |
| 35000012 |

## onQueryCompilationByKeyword

```TypeScript
onQueryCompilationByKeyword(callback: QueryCompilationByKeywordEvent): void
```

Register query compilation by keyword callback.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-AVMusicTemplate-onQueryCompilationByKeyword(callback: QueryCompilationByKeywordEvent): void--><!--Device-AVMusicTemplate-onQueryCompilationByKeyword(callback: QueryCompilationByKeywordEvent): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [QueryCompilationByKeywordEvent](arkts-avsession-avmusictemplate-querycompilationbykeywordevent-t.md) | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#801-ad-request-failure) |
| [35000005](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-avsession-kit/errorcode-avmusictemplate.md#35000005-audio-template-does-not-exist) |
| 35000012 |

## onQueryCurrentSingle

```TypeScript
onQueryCurrentSingle(callback: QueryCurrentSingleEvent): void
```

Register query current single callback.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-AVMusicTemplate-onQueryCurrentSingle(callback: QueryCurrentSingleEvent): void--><!--Device-AVMusicTemplate-onQueryCurrentSingle(callback: QueryCurrentSingleEvent): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [QueryCurrentSingleEvent](arkts-avsession-avmusictemplate-querycurrentsingleevent-t.md) | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#801-ad-request-failure) |
| [35000005](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-avsession-kit/errorcode-avmusictemplate.md#35000005-audio-template-does-not-exist) |
| 35000012 |

## onQueryCustomContent

```TypeScript
onQueryCustomContent(callback: QueryCustomContentEvent): void
```

Register query custom content callback.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-AVMusicTemplate-onQueryCustomContent(callback: QueryCustomContentEvent): void--><!--Device-AVMusicTemplate-onQueryCustomContent(callback: QueryCustomContentEvent): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [QueryCustomContentEvent](arkts-avsession-avmusictemplate-querycustomcontentevent-t.md) | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#801-ad-request-failure) |
| [35000005](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-avsession-kit/errorcode-avmusictemplate.md#35000005-audio-template-does-not-exist) |
| 35000012 |

## onQueryHotWords

```TypeScript
onQueryHotWords(callback: QueryHotWordsEvent): void
```

Register query hot words callback.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-AVMusicTemplate-onQueryHotWords(callback: QueryHotWordsEvent): void--><!--Device-AVMusicTemplate-onQueryHotWords(callback: QueryHotWordsEvent): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [QueryHotWordsEvent](arkts-avsession-avmusictemplate-queryhotwordsevent-t.md) | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#801-ad-request-failure) |
| [35000005](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-avsession-kit/errorcode-avmusictemplate.md#35000005-audio-template-does-not-exist) |
| 35000012 |

## onQueryMainTabs

```TypeScript
onQueryMainTabs(callback: QueryMainTabsEvent): void
```

Register query main tabs callback.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-AVMusicTemplate-onQueryMainTabs(callback: QueryMainTabsEvent): void--><!--Device-AVMusicTemplate-onQueryMainTabs(callback: QueryMainTabsEvent): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [QueryMainTabsEvent](arkts-avsession-avmusictemplate-querymaintabsevent-t.md) | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#801-ad-request-failure) |
| [35000005](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-avsession-kit/errorcode-avmusictemplate.md#35000005-audio-template-does-not-exist) |
| 35000012 |

## onQueryMediaEntity

```TypeScript
onQueryMediaEntity(callback: QueryMediaEntityEvent): void
```

Register query media entity callback.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-AVMusicTemplate-onQueryMediaEntity(callback: QueryMediaEntityEvent): void--><!--Device-AVMusicTemplate-onQueryMediaEntity(callback: QueryMediaEntityEvent): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [QueryMediaEntityEvent](arkts-avsession-avmusictemplate-querymediaentityevent-t.md) | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#801-ad-request-failure) |
| [35000005](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-avsession-kit/errorcode-avmusictemplate.md#35000005-audio-template-does-not-exist) |
| 35000012 |

## onQueryMediaEntityByKeyword

```TypeScript
onQueryMediaEntityByKeyword(callback: QueryMediaEntityByKeywordEvent): void
```

Register query media entity by keyword callback.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-AVMusicTemplate-onQueryMediaEntityByKeyword(callback: QueryMediaEntityByKeywordEvent): void--><!--Device-AVMusicTemplate-onQueryMediaEntityByKeyword(callback: QueryMediaEntityByKeywordEvent): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [QueryMediaEntityByKeywordEvent](arkts-avsession-avmusictemplate-querymediaentitybykeywordevent-t.md) | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#801-ad-request-failure) |
| [35000005](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-avsession-kit/errorcode-avmusictemplate.md#35000005-audio-template-does-not-exist) |
| 35000012 |

## onQueryMediaTabContent

```TypeScript
onQueryMediaTabContent(callback: QueryMediaTabContentEvent): void
```

Register query media tab content callback.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-AVMusicTemplate-onQueryMediaTabContent(callback: QueryMediaTabContentEvent): void--><!--Device-AVMusicTemplate-onQueryMediaTabContent(callback: QueryMediaTabContentEvent): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [QueryMediaTabContentEvent](arkts-avsession-avmusictemplate-querymediatabcontentevent-t.md) | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#801-ad-request-failure) |
| [35000005](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-avsession-kit/errorcode-avmusictemplate.md#35000005-audio-template-does-not-exist) |
| 35000012 |

## onQueryMemberPurchase

```TypeScript
onQueryMemberPurchase(callback: QueryMemberPurchaseEvent): void
```

Register query member purchase callback.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-AVMusicTemplate-onQueryMemberPurchase(callback: QueryMemberPurchaseEvent): void--><!--Device-AVMusicTemplate-onQueryMemberPurchase(callback: QueryMemberPurchaseEvent): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [QueryMemberPurchaseEvent](arkts-avsession-avmusictemplate-querymemberpurchaseevent-t.md) | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#801-ad-request-failure) |
| [35000005](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-avsession-kit/errorcode-avmusictemplate.md#35000005-audio-template-does-not-exist) |
| 35000012 |

## onQueryPlaylist

```TypeScript
onQueryPlaylist(callback: QueryPlaylistEvent): void
```

Register query playlist callback.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-AVMusicTemplate-onQueryPlaylist(callback: QueryPlaylistEvent): void--><!--Device-AVMusicTemplate-onQueryPlaylist(callback: QueryPlaylistEvent): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [QueryPlaylistEvent](arkts-avsession-avmusictemplate-queryplaylistevent-t.md) | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#801-ad-request-failure) |
| [35000005](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-avsession-kit/errorcode-avmusictemplate.md#35000005-audio-template-does-not-exist) |
| 35000012 |

## onQueryRecommendMediaEntityList

```TypeScript
onQueryRecommendMediaEntityList(callback: QueryRecommendMediaEntityListEvent): void
```

Register query recommend media entity list callback.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-AVMusicTemplate-onQueryRecommendMediaEntityList(callback: QueryRecommendMediaEntityListEvent): void--><!--Device-AVMusicTemplate-onQueryRecommendMediaEntityList(callback: QueryRecommendMediaEntityListEvent): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [QueryRecommendMediaEntityListEvent](arkts-avsession-avmusictemplate-queryrecommendmediaentitylistevent-t.md) | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#801-ad-request-failure) |
| [35000005](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-avsession-kit/errorcode-avmusictemplate.md#35000005-audio-template-does-not-exist) |
| 35000012 |

## onQuerySearchHistory

```TypeScript
onQuerySearchHistory(callback: QuerySearchHistoryEvent): void
```

Register query search history callback.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-AVMusicTemplate-onQuerySearchHistory(callback: QuerySearchHistoryEvent): void--><!--Device-AVMusicTemplate-onQuerySearchHistory(callback: QuerySearchHistoryEvent): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [QuerySearchHistoryEvent](arkts-avsession-avmusictemplate-querysearchhistoryevent-t.md) | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#801-ad-request-failure) |
| [35000005](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-avsession-kit/errorcode-avmusictemplate.md#35000005-audio-template-does-not-exist) |
| 35000012 |

## onRequestDialogInfo

```TypeScript
onRequestDialogInfo(callback: RequestDialogInfoEvent): void
```

Register request dialog info callback.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-AVMusicTemplate-onRequestDialogInfo(callback: RequestDialogInfoEvent): void--><!--Device-AVMusicTemplate-onRequestDialogInfo(callback: RequestDialogInfoEvent): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [RequestDialogInfoEvent](arkts-avsession-avmusictemplate-requestdialoginfoevent-t.md) | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#801-ad-request-failure) |
| [35000005](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-avsession-kit/errorcode-avmusictemplate.md#35000005-audio-template-does-not-exist) |
| 35000012 |

## onSettingsChange

```TypeScript
onSettingsChange(callback: SettingsChangeEvent): void
```

Register settings change callback.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-AVMusicTemplate-onSettingsChange(callback: SettingsChangeEvent): void--><!--Device-AVMusicTemplate-onSettingsChange(callback: SettingsChangeEvent): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [SettingsChangeEvent](arkts-avsession-avmusictemplate-settingschangeevent-t.md) | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#801-ad-request-failure) |
| [35000005](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-avsession-kit/errorcode-avmusictemplate.md#35000005-audio-template-does-not-exist) |
| 35000012 |

## reportExecuteAction

```TypeScript
reportExecuteAction(actionType: string, params: string): Promise<void>
```

Report execute action information to MediaUI.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-AVMusicTemplate-reportExecuteAction(actionType: string, params: string): Promise<void>--><!--Device-AVMusicTemplate-reportExecuteAction(actionType: string, params: string): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| actionType | string | Yes |
| params | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#801-ad-request-failure) |
| [35000005](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-avsession-kit/errorcode-avmusictemplate.md#35000005-audio-template-does-not-exist) |
| 35000011 |

## setCurrentSingle

```TypeScript
setCurrentSingle(single: Single): Promise<void>
```

Report current single song to MediaUI.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-AVMusicTemplate-setCurrentSingle(single: Single): Promise<void>--><!--Device-AVMusicTemplate-setCurrentSingle(single: Single): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| single | [Single](arkts-avsession-avmusictemplate-single-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#801-ad-request-failure) |
| [35000005](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-avsession-kit/errorcode-avmusictemplate.md#35000005-audio-template-does-not-exist) |
| 35000011 |

## setCustomElements

```TypeScript
setCustomElements(actionType: ActionType, customType: CustomType,
      customElement: CustomElement): Promise<void>
```

Report custom elements change information to MediaUI.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-AVMusicTemplate-setCustomElements(actionType: ActionType, customType: CustomType,      customElement: CustomElement): Promise<void>--><!--Device-AVMusicTemplate-setCustomElements(actionType: ActionType, customType: CustomType,      customElement: CustomElement): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| actionType | [ActionType](arkts-avsession-avmusictemplate-actiontype-t.md) | Yes |
| customType | [CustomType](arkts-avsession-avmusictemplate-customtype-t.md) | Yes |
| customElement | [CustomElement](arkts-avsession-avmusictemplate-customelement-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#801-ad-request-failure) |
| [35000005](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-avsession-kit/errorcode-avmusictemplate.md#35000005-audio-template-does-not-exist) |
| 35000011 |

## setDialogCommand

```TypeScript
setDialogCommand(type: DialogControlType, dialogInfo: DialogInfo): Promise<void>
```

Report dialog command to MediaUI.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-AVMusicTemplate-setDialogCommand(type: DialogControlType, dialogInfo: DialogInfo): Promise<void>--><!--Device-AVMusicTemplate-setDialogCommand(type: DialogControlType, dialogInfo: DialogInfo): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | [DialogControlType](arkts-avsession-avmusictemplate-dialogcontroltype-t.md) | Yes |
| dialogInfo | [DialogInfo](arkts-avsession-avmusictemplate-dialoginfo-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#801-ad-request-failure) |
| [35000005](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-avsession-kit/errorcode-avmusictemplate.md#35000005-audio-template-does-not-exist) |
| 35000011 |

## setDownloadMediaEntityStatus

```TypeScript
setDownloadMediaEntityStatus(single: MediaEntity): Promise<void>
```

Report single download status information to MediaUI.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-AVMusicTemplate-setDownloadMediaEntityStatus(single: MediaEntity): Promise<void>--><!--Device-AVMusicTemplate-setDownloadMediaEntityStatus(single: MediaEntity): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| single | [MediaEntity](arkts-avsession-avmusictemplate-mediaentity-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#801-ad-request-failure) |
| [35000005](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-avsession-kit/errorcode-avmusictemplate.md#35000005-audio-template-does-not-exist) |
| 35000011 |

## setExtensionAbility

```TypeScript
setExtensionAbility(want: WantAgent): Promise<void>
```

Report execute extension ability to MediaUI.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-AVMusicTemplate-setExtensionAbility(want: WantAgent): Promise<void>--><!--Device-AVMusicTemplate-setExtensionAbility(want: WantAgent): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| want | [WantAgent](../../apis-ability-kit/arkts-apis/arkts-ability-wantagent-t.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#801-ad-request-failure) |
| [35000005](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-avsession-kit/errorcode-avmusictemplate.md#35000005-audio-template-does-not-exist) |
| 35000011 |

## setMediaEntities

```TypeScript
setMediaEntities(entities: MediaEntity[]): Promise<void>
```

Report media resource change information to MediaUI.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-AVMusicTemplate-setMediaEntities(entities: MediaEntity[]): Promise<void>--><!--Device-AVMusicTemplate-setMediaEntities(entities: MediaEntity[]): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| entities | [MediaEntity](arkts-avsession-avmusictemplate-mediaentity-i.md)[] | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#801-ad-request-failure) |
| [35000005](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-avsession-kit/errorcode-avmusictemplate.md#35000005-audio-template-does-not-exist) |
| 35000011 |

## setPlaylist

```TypeScript
setPlaylist(playlist: PageMediaEntity): Promise<void>
```

Report play list information to MediaUI.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-AVMusicTemplate-setPlaylist(playlist: PageMediaEntity): Promise<void>--><!--Device-AVMusicTemplate-setPlaylist(playlist: PageMediaEntity): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| playlist | [PageMediaEntity](arkts-avsession-avmusictemplate-pagemediaentity-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#801-ad-request-failure) |
| [35000005](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-avsession-kit/errorcode-avmusictemplate.md#35000005-audio-template-does-not-exist) |
| 35000011 |

## setSettings

```TypeScript
setSettings(settingItems: SettingItem[]): Promise<void>
```

Report settings information to MediaUI.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-AVMusicTemplate-setSettings(settingItems: SettingItem[]): Promise<void>--><!--Device-AVMusicTemplate-setSettings(settingItems: SettingItem[]): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| settingItems | [SettingItem](arkts-avsession-avmusictemplate-settingitem-i.md)[] | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#801-ad-request-failure) |
| [35000005](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-avsession-kit/errorcode-avmusictemplate.md#35000005-audio-template-does-not-exist) |
| 35000011 |

## setTabContent

```TypeScript
setTabContent(tabId: string, tabContent: MediaTabContent): Promise<void>
```

Report tab page content information to MediaUI.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-AVMusicTemplate-setTabContent(tabId: string, tabContent: MediaTabContent): Promise<void>--><!--Device-AVMusicTemplate-setTabContent(tabId: string, tabContent: MediaTabContent): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| tabId | string | Yes |
| tabContent | [MediaTabContent](arkts-avsession-avmusictemplate-mediatabcontent-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#801-ad-request-failure) |
| [35000005](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-avsession-kit/errorcode-avmusictemplate.md#35000005-audio-template-does-not-exist) |
| 35000011 |

## setUserInfo

```TypeScript
setUserInfo(userInfo: UserInfo): Promise<void>
```

Report user infomation to MediaUI.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-AVMusicTemplate-setUserInfo(userInfo: UserInfo): Promise<void>--><!--Device-AVMusicTemplate-setUserInfo(userInfo: UserInfo): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| userInfo | [UserInfo](../../apis-arkdata/arkts-apis/arkts-arkdata-distributeddata-userinfo-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#801-ad-request-failure) |
| [35000005](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-avsession-kit/errorcode-avmusictemplate.md#35000005-audio-template-does-not-exist) |
| 35000011 |

## startTemplate

```TypeScript
startTemplate(): Promise<OperResult>
```

Start media center template interface.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-AVMusicTemplate-startTemplate(): Promise<OperResult>--><!--Device-AVMusicTemplate-startTemplate(): Promise<OperResult>-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[OperResult](arkts-avsession-avmusictemplate-operresult-i.md)&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#801-ad-request-failure) |

## sessionId

```TypeScript
sessionId: string
```

Unique AVMusicTemplate descriptor.

**Type:** string

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-AVMusicTemplate-sessionId: string--><!--Device-AVMusicTemplate-sessionId: string-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVMusicTemplate

## sessionTag

```TypeScript
sessionTag: string
```

AVMusicTemplate tag.

**Type:** string

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-AVMusicTemplate-sessionTag: string--><!--Device-AVMusicTemplate-sessionTag: string-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVMusicTemplate
