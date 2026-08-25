# @ohos.file.PhotoPickerComponent(PhotoPickerComponent)

You can embed the **PhotoPickerComponent** in your application's layout to let users pick images or videos without
 requiring extra permissions. Once the users have made their selection, your application gets read-only access to the
 chosen images or videos.
 Note that **PhotoPickerComponent** does not support nesting. Additionally, prevent overlaying components with the
 **overlay** attribute or of higher levels on top it, as this will prevent it from receiving gesture events.
 Once embedded, users can directly select images or videos within the **PhotoPickerComponent**.
 > **NOTE**
 >
 > - This component does not support [same-layer rendering](../../../web/web-same-layer.md).
 ###### Attributes
 The universal attributes are supported.


## Modules to Import

```TypeScript
import { PhotoPickerComponent, PickerController, PickerOptions, DataType, BaseItemInfo, ItemInfo, PhotoBrowserInfo, AnimatorParams, MaxSelected, ItemType, ClickType, PickerOrientation, SelectMode, PickerColorMode, ReminderMode, MaxCountType, PhotoBrowserRange, PhotoBrowserUIElement, ItemsDeletedCallback, ExceedMaxSelectedCallback, CurrentAlbumDeletedCallback, videoPlayStateChangedCallback, MovingPhotoBadgeStateChangedCallback, UpdatablePickerConfigs, SingleLineConfig, BadgeConfig, PreselectedInfo, SaveMode, BadgeType, VideoPlayerState, ItemDisplayRatio, ScrollStopAtStartCallback, ItemClickedNotifyCallback, ScrollStopAtEndCallback, PhotoBrowserChangeStartCallback, PinchGridSwitchedCallback, ErrorCallback, ClickResult, PickerError } from 'kits/@kit.MediaLibraryKit';
```

## Summary

### Classes

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [AnimatorParams(PhotoPickerComponent)](arkts-medialibrary-file-photopickercomponent-animatorparams-c.md) |
| [BadgeConfig(PhotoPickerComponent)](arkts-medialibrary-file-photopickercomponent-badgeconfig-c.md) |
| [BaseItemInfo(PhotoPickerComponent)](arkts-medialibrary-file-photopickercomponent-baseiteminfo-c.md) |
| [ClickResult(PhotoPickerComponent)](arkts-medialibrary-file-photopickercomponent-clickresult-c.md) |
| [CompletedResult(PhotoPickerComponent)](arkts-medialibrary-file-photopickercomponent-completedresult-c.md) |
| [ItemInfo(PhotoPickerComponent)](arkts-medialibrary-file-photopickercomponent-iteminfo-c.md) |
| [MaxSelected(PhotoPickerComponent)](arkts-medialibrary-file-photopickercomponent-maxselected-c.md) |
| [PhotoBrowserInfo(PhotoPickerComponent)](arkts-medialibrary-file-photopickercomponent-photobrowserinfo-c.md) |
| [PickerController(PhotoPickerComponent)](arkts-medialibrary-file-photopickercomponent-pickercontroller-c.md) |
| [PickerError(PhotoPickerComponent)](arkts-medialibrary-file-photopickercomponent-pickererror-c.md) |
| [PickerOptions(PhotoPickerComponent)](arkts-medialibrary-file-photopickercomponent-pickeroptions-c.md) |
| [PreselectedInfo(PhotoPickerComponent)](arkts-medialibrary-file-photopickercomponent-preselectedinfo-c.md) |
| [RecoveryResult(PhotoPickerComponent)](arkts-medialibrary-file-photopickercomponent-recoveryresult-c.md) |
| [SingleLineConfig(PhotoPickerComponent)](arkts-medialibrary-file-photopickercomponent-singlelineconfig-c.md) |
| [UnselectableItemInfo(PhotoPickerComponent)](arkts-medialibrary-file-photopickercomponent-unselectableiteminfo-c.md) |
| [UpdatablePickerConfigs(PhotoPickerComponent)](arkts-medialibrary-file-photopickercomponent-updatablepickerconfigs-c.md) |

### Structs

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [PhotoPickerComponent(PhotoPickerComponent)](arkts-medialibrary-file-photopickercomponent-photopickercomponent-s.md) |

### Enums

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [BadgeType(PhotoPickerComponent)](arkts-medialibrary-file-photopickercomponent-badgetype-e.md) |
| [ClickType(PhotoPickerComponent)](arkts-medialibrary-file-photopickercomponent-clicktype-e.md) |
| [DataType(PhotoPickerComponent)](arkts-medialibrary-file-photopickercomponent-datatype-e.md) |
| [ItemDisplayRatio(PhotoPickerComponent)](arkts-medialibrary-file-photopickercomponent-itemdisplayratio-e.md) |
| [ItemType(PhotoPickerComponent)](arkts-medialibrary-file-photopickercomponent-itemtype-e.md) |
| [MaxCountType(PhotoPickerComponent)](arkts-medialibrary-file-photopickercomponent-maxcounttype-e.md) |
| [PhotoBrowserRange(PhotoPickerComponent)](arkts-medialibrary-file-photopickercomponent-photobrowserrange-e.md) |
| [PhotoBrowserUIElement(PhotoPickerComponent)](arkts-medialibrary-file-photopickercomponent-photobrowseruielement-e.md) |
| [PickerColorMode(PhotoPickerComponent)](arkts-medialibrary-file-photopickercomponent-pickercolormode-e.md) |
| [PickerOrientation(PhotoPickerComponent)](arkts-medialibrary-file-photopickercomponent-pickerorientation-e.md) |
| [ReminderMode(PhotoPickerComponent)](arkts-medialibrary-file-photopickercomponent-remindermode-e.md) |
| [SaveMode(PhotoPickerComponent)](arkts-medialibrary-file-photopickercomponent-savemode-e.md) |
| [SelectMode(PhotoPickerComponent)](arkts-medialibrary-file-photopickercomponent-selectmode-e.md) |
| [VideoPlayerState(PhotoPickerComponent)](arkts-medialibrary-file-photopickercomponent-videoplayerstate-e.md) |

### Types

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [CurrentAlbumDeletedCallback(PhotoPickerComponent)](arkts-medialibrary-currentalbumdeletedcallback-t.md) |
| [ErrorCallback(PhotoPickerComponent)](arkts-medialibrary-errorcallback-t.md) |
| [ExceedMaxSelectedCallback(PhotoPickerComponent)](arkts-medialibrary-exceedmaxselectedcallback-t.md) |
| [ItemClickedNotifyCallback(PhotoPickerComponent)](arkts-medialibrary-itemclickednotifycallback-t.md) |
| [ItemsDeletedCallback(PhotoPickerComponent)](arkts-medialibrary-itemsdeletedcallback-t.md) |
| [MovingPhotoBadgeStateChangedCallback(PhotoPickerComponent)](arkts-medialibrary-movingphotobadgestatechangedcallback-t.md) |
| [PhotoBrowserChangeStartCallback(PhotoPickerComponent)](arkts-medialibrary-photobrowserchangestartcallback-t.md) |
| [PhotoBrowserZoomCallback(PhotoPickerComponent)](arkts-medialibrary-photobrowserzoomcallback-t.md) |
| [PickerRecoveryCallback(PhotoPickerComponent)](arkts-medialibrary-pickerrecoverycallback-t.md) |
| [PinchGridSwitchedCallback(PhotoPickerComponent)](arkts-medialibrary-pinchgridswitchedcallback-t.md) |
| [ScrollStopAtEndCallback(PhotoPickerComponent)](arkts-medialibrary-scrollstopatendcallback-t.md) |
| [ScrollStopAtStartCallback(PhotoPickerComponent)](arkts-medialibrary-scrollstopatstartcallback-t.md) |
| [UnselectableItemClickedCallback(PhotoPickerComponent)](arkts-medialibrary-unselectableitemclickedcallback-t.md) |
| [videoPlayStateChangedCallback(PhotoPickerComponent)](arkts-medialibrary-videoplaystatechangedcallback-t.md) |
