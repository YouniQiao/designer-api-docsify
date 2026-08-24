# @ohos.multimedia.avMusicTemplate

This module provides the capability to media enhancement@namespace avMusicTemplate

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-declare namespace avMusicTemplate--><!--Device-unnamed-declare namespace avMusicTemplate-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVMusicTemplate

## Modules to Import

```TypeScript
import { avMusicTemplate } from '@kit.AVSessionKit';
```

## Summary

### Functions

| Name | Description |
| --- | --- |
| [createAVMusicTemplate](arkts-avsession-avmusictemplate-createavmusictemplate-f.md) | Create an AVMusicTemplate instance. |

<!--Del-->
### Functions(System API)

| Name | Description |
| --- | --- |
| [createAVMusicTemplateController](arkts-avsession-avmusictemplate-createavmusictemplatecontroller-f-sys.md) | Create AVMusicTemplate controller instance. |
| [getAllAVMusicTemplateDescriptors](arkts-avsession-avmusictemplate-getallavmusictemplatedescriptors-f-sys.md) | Get all AVMusicTemplate descriptors. |
| [offAVMusicTemplateCreate](arkts-avsession-avmusictemplate-offavmusictemplatecreate-f-sys.md) | UnRegister session create event |
| [offAVMusicTemplateDestroy](arkts-avsession-avmusictemplate-offavmusictemplatedestroy-f-sys.md) | UnRegister session destroy event |
| [onAVMusicTemplateCreate](arkts-avsession-avmusictemplate-onavmusictemplatecreate-f-sys.md) | Register session create event |
| [onAVMusicTemplateDestroy](arkts-avsession-avmusictemplate-onavmusictemplatedestroy-f-sys.md) | Register session destroy event |
<!--DelEnd-->

### Classes

| Name | Description |
| --- | --- |
| [AVMusicTemplate](arkts-avsession-avmusictemplate-avmusictemplate-c.md) | AVMusicTemplate interface |
| [AVMusicTemplateController](arkts-avsession-avmusictemplate-avmusictemplatecontroller-c.md) | The definition of the AVMusicTemplateController. |

### Interfaces

| Name | Description |
| --- | --- |
| [Album](arkts-avsession-avmusictemplate-album-i.md) | The definition of Album.@extends MediaEntity @interface Album |
| [Banner](arkts-avsession-avmusictemplate-banner-i.md) | The definition of Banner.@extends MediaEntity @interface Banner |
| [Compilation](arkts-avsession-avmusictemplate-compilation-i.md) | The definition of compilation.@extends OperResult @interface Compilation |
| [CustomElement](arkts-avsession-avmusictemplate-customelement-i.md) | Custom elements of mine page.@extends OperResult @interface CustomElement |
| [DialogActionInfo](arkts-avsession-avmusictemplate-dialogactioninfo-i.md) | The definition of dialog action result.@interface DialogActionInfo |
| [DialogButtonInfo](arkts-avsession-avmusictemplate-dialogbuttoninfo-i.md) | The definition of dialog button information.@interface DialogButtonInfo |
| [DialogInfo](arkts-avsession-avmusictemplate-dialoginfo-i.md) | The definition of dialog information.@interface DialogInfo |
| [EpisodeRange](arkts-avsession-avmusictemplate-episoderange-i.md) | The definition of EpisodeRange.@interface EpisodeRange |
| [FavoriteData](arkts-avsession-avmusictemplate-favoritedata-i.md) | The definition of Favorite/Subscribe.@interface FavoriteData |
| [MediaElement](arkts-avsession-avmusictemplate-mediaelement-i.md) | The definition of Singer/Radio/Banner.@extends MediaEntity @interface MediaElement |
| [MediaEntity](arkts-avsession-avmusictemplate-mediaentity-i.md) | The definition of MediaEntity.@interface MediaEntity |
| [MediaTab](arkts-avsession-avmusictemplate-mediatab-i.md) | The definition of the tab page.@interface MediaTab |
| [MediaTabContent](arkts-avsession-avmusictemplate-mediatabcontent-i.md) | The definition of the tab page content.@extends OperResult @interface MediaTabContent |
| [MemberPurchaseInfo](arkts-avsession-avmusictemplate-memberpurchaseinfo-i.md) | The definition of member purchase information.@interface MemberPurchaseInfo |
| [OperResult](arkts-avsession-avmusictemplate-operresult-i.md) | The definition of the operate result.@interface OperResult |
| [PageMediaEntity](arkts-avsession-avmusictemplate-pagemediaentity-i.md) | The definition of pagination object.@extends OperResult @interface PageMediaEntity |
| [PlayInfo](arkts-avsession-avmusictemplate-playinfo-i.md) | The definition of play information.@interface PlayInfo |
| [QrCodeInfo](arkts-avsession-avmusictemplate-qrcodeinfo-i.md) | The definition of QR code Information.@interface QrCodeInfo |
| [QueryMediaEntityParam](arkts-avsession-avmusictemplate-querymediaentityparam-i.md) | The definition of QueryMediaEntityParam.@interface QueryMediaEntityParam |
| [Ranking](arkts-avsession-avmusictemplate-ranking-i.md) | The definition of Ranking.@extends MediaEntity @interface Ranking |
| [SearchPlayInfo](arkts-avsession-avmusictemplate-searchplayinfo-i.md) | The definition of SearchPlayInfo.@interface SearchPlayInfo |
| [SearchPlayMusicInfo](arkts-avsession-avmusictemplate-searchplaymusicinfo-i.md) | The definition of SearchPlayMusicInfo.@interface SearchPlayMusicInfo |
| [SearchPlayMusicItem](arkts-avsession-avmusictemplate-searchplaymusicitem-i.md) | The definition of SearchPlayMusicItem.@interface SearchPlayMusicItem |
| [SearchPlayVideoInfo](arkts-avsession-avmusictemplate-searchplayvideoinfo-i.md) | The definition of SearchPlayVideoInfo.@interface SearchPlayVideoInfo |
| [SettingContent](arkts-avsession-avmusictemplate-settingcontent-i.md) | The definition of setting content@interface SettingContent |
| [SettingItem](arkts-avsession-avmusictemplate-settingitem-i.md) | The definition of setting Information.@interface SettingItem |
| [Single](arkts-avsession-avmusictemplate-single-i.md) | The definition of Single song.@extends MediaEntity @interface Single |
| [UserInfo](arkts-avsession-avmusictemplate-userinfo-i.md) | The definition of User information.@interface UserInfo |

<!--Del-->
### Interfaces(System API)

| Name | Description |
| --- | --- |
| [AVMusicTemplateDescriptor](arkts-avsession-avmusictemplate-avmusictemplatedescriptor-i-sys.md) | Description of the AVMusicTemplate. |
<!--DelEnd-->

### Enums

| Name | Description |
| --- | --- |
| [AVMusicTemplateErrorCode](arkts-avsession-avmusictemplate-avmusictemplateerrorcode-e.md) | Enumeration ErrorCode types, returns in BusinessError.code.@enum { int } |
| [AVMusicTemplateType](arkts-avsession-avmusictemplate-avmusictemplatetype-e.md) | Enumeration of AVMusicTemplate type.@enum { string } |
| [ButtonType](arkts-avsession-avmusictemplate-buttontype-e.md) | Enumeration of button type.@enum { int } |
| [DialogType](arkts-avsession-avmusictemplate-dialogtype-e.md) | Enumeration of dialog type.@enum { int } |
| [DownloadStatus](arkts-avsession-avmusictemplate-downloadstatus-e.md) | Enumeration of DownloadStatus.@enum { int } |
| [EntityType](arkts-avsession-avmusictemplate-entitytype-e.md) | Enumeration of media resource type.@enum { int } |
| [MemberPurchaseType](arkts-avsession-avmusictemplate-memberpurchasetype-e.md) | Enumeration of MemberPurchaseType.@enum { string } |
| [PlaybackState](arkts-avsession-avmusictemplate-playbackstate-e.md) | Enumeration of play state.@enum { int } |
| [SearchPlayInfoType](arkts-avsession-avmusictemplate-searchplayinfotype-e.md) | Enumeration of SearchPlayInfoType.@enum { string } |
| [SettingType](arkts-avsession-avmusictemplate-settingtype-e.md) | Enumeration of setting type.@enum { int } |
| [Sort](arkts-avsession-avmusictemplate-sort-e.md) | Enumeration of Sort type.@enum { int } |

### Types

| Name | Description |
| --- | --- |
| [ActionType](arkts-avsession-avmusictemplate-actiontype-t.md) | Action type add & remove. |
| [ClearSearchHistoryEvent](arkts-avsession-avmusictemplate-clearsearchhistoryevent-t.md) | The clear search history event. |
| [CustomCommandEvent](arkts-avsession-avmusictemplate-customcommandevent-t.md) | The custom command event. |
| [CustomType](arkts-avsession-avmusictemplate-customtype-t.md) | Custom tab type USER_INFO & TAB, COMPILATION, SETTINGS. |
| [DialogActionType](arkts-avsession-avmusictemplate-dialogactiontype-t.md) | Dialog action type open & close, refresh. |
| [DialogControlType](arkts-avsession-avmusictemplate-dialogcontroltype-t.md) | Dialog control type open & close, refresh, toast. |
| [DownloadControlType](arkts-avsession-avmusictemplate-downloadcontroltype-t.md) | Download control type startDownload & deleteDownload, resumeDownload, pauseDownload. |
| [DownloadMediaEntityEvent](arkts-avsession-avmusictemplate-downloadmediaentityevent-t.md) | The download media entity event. |
| [ExecuteActionEvent](arkts-avsession-avmusictemplate-executeactionevent-t.md) | The execute action event. |
| [FavoriteMediaEntityEvent](arkts-avsession-avmusictemplate-favoritemediaentityevent-t.md) | The favorite media entity event. |
| [HandleMemberPurchaseEvent](arkts-avsession-avmusictemplate-handlememberpurchaseevent-t.md) | The handle member purchase event. |
| [LoginEvent](arkts-avsession-avmusictemplate-loginevent-t.md) | The login event. |
| [LoginType](arkts-avsession-avmusictemplate-logintype-t.md) | Login type queryLoginInfo & refreshLoginInfo, logout. |
| [MediaFavoriteType](arkts-avsession-avmusictemplate-mediafavoritetype-t.md) | Media favorite type addFavorite & removeFavorite. |
| [NoParamAsyncCallback](arkts-avsession-avmusictemplate-noparamasynccallback-t.md) | Defines the basic callback. |
| [PlayForSearchEvent](arkts-avsession-avmusictemplate-playforsearchevent-t.md) | The play for search event. |
| [PlayMediaEntityEvent](arkts-avsession-avmusictemplate-playmediaentityevent-t.md) | The play media entity event. |
| [ProblemAndAdviceEvent](arkts-avsession-avmusictemplate-problemandadviceevent-t.md) | The problem and advice event. |
| [QueryCompilationByKeywordEvent](arkts-avsession-avmusictemplate-querycompilationbykeywordevent-t.md) | The query compilation by keyword event. |
| [QueryCompilationEvent](arkts-avsession-avmusictemplate-querycompilationevent-t.md) | The query compilation event. |
| [QueryCurrentSingleEvent](arkts-avsession-avmusictemplate-querycurrentsingleevent-t.md) | The query current single event. |
| [QueryCustomContentEvent](arkts-avsession-avmusictemplate-querycustomcontentevent-t.md) | The query custom content event. |
| [QueryHotWordsEvent](arkts-avsession-avmusictemplate-queryhotwordsevent-t.md) | The query hot words event. |
| [QueryMainTabsEvent](arkts-avsession-avmusictemplate-querymaintabsevent-t.md) | The query main tabs event. |
| [QueryMediaEntityByKeywordEvent](arkts-avsession-avmusictemplate-querymediaentitybykeywordevent-t.md) | The query media entity by keyword event. |
| [QueryMediaEntityEvent](arkts-avsession-avmusictemplate-querymediaentityevent-t.md) | The query media entity event. |
| [QueryMediaTabContentEvent](arkts-avsession-avmusictemplate-querymediatabcontentevent-t.md) | The query media tab content event. |
| [QueryMemberPurchaseEvent](arkts-avsession-avmusictemplate-querymemberpurchaseevent-t.md) | The query member purchase event. |
| [QueryPlaylistEvent](arkts-avsession-avmusictemplate-queryplaylistevent-t.md) | The query play list event. |
| [QueryRecommendMediaEntityListEvent](arkts-avsession-avmusictemplate-queryrecommendmediaentitylistevent-t.md) | The query recommend media entity list event. |
| [QuerySearchHistoryEvent](arkts-avsession-avmusictemplate-querysearchhistoryevent-t.md) | The query search history event. |
| [ReportCustomElementsChangeEvent](arkts-avsession-avmusictemplate-reportcustomelementschangeevent-t.md) | The report custom elements change event. |
| [ReportDialogCommandEvent](arkts-avsession-avmusictemplate-reportdialogcommandevent-t.md) | The report dialog command event. |
| [ReportExecuteAbilityEvent](arkts-avsession-avmusictemplate-reportexecuteabilityevent-t.md) | The report extension ability event. |
| [ReportExecuteActionEvent](arkts-avsession-avmusictemplate-reportexecuteactionevent-t.md) | The report execute action event. |
| [ReportTabContentEvent](arkts-avsession-avmusictemplate-reporttabcontentevent-t.md) | The report tab content event. |
| [RequestDialogInfoEvent](arkts-avsession-avmusictemplate-requestdialoginfoevent-t.md) | The request dialog info event. |
| [SettingsChangeEvent](arkts-avsession-avmusictemplate-settingschangeevent-t.md) | The settings change event. |

