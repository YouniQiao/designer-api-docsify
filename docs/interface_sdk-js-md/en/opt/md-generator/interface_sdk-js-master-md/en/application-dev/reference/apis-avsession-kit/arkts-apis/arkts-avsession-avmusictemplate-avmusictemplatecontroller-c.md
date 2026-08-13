# AVMusicTemplateController

The definition of the AVMusicTemplateController.

**Since:** 23

**Deprecated since:** -1

<!--Device-avMusicTemplate-class AVMusicTemplateController--><!--Device-avMusicTemplate-class AVMusicTemplateController-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVMusicTemplate

## Modules to Import

```TypeScript
import { avMusicTemplate } from '@kit.AVSessionKit';
```

## clearSearchHistory

```TypeScript
clearSearchHistory(): Promise<OperResult>
```

Clear search history.

**Since:** 23

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-AVMusicTemplateController-clearSearchHistory(): Promise<OperResult>--><!--Device-AVMusicTemplateController-clearSearchHistory(): Promise<OperResult>-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[OperResult](arkts-avsession-avmusictemplate-operresult-i.md)&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [35000006](../errorcode-avmusictemplate.md#35000006-template-controller-does-not-exist) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [35000005](../errorcode-avmusictemplate.md#35000005-audio-template-does-not-exist) |
| [35000003](../errorcode-avmusictemplate.md#35000003-template-listener-not-registered) |

## destroy

```TypeScript
destroy(): Promise<void>
```

Destroy the controller.

**Since:** 23

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-AVMusicTemplateController-destroy(): Promise<void>--><!--Device-AVMusicTemplateController-destroy(): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../errorcode-universal.md#801-api-not-supported) |

## downloadMediaEntity

```TypeScript
downloadMediaEntity(controlType: DownloadControlType, mediaEntity: MediaEntity): Promise<OperResult>
```

Download media entity.

**Since:** 23

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-AVMusicTemplateController-downloadMediaEntity(controlType: DownloadControlType, mediaEntity: MediaEntity): Promise<OperResult>--><!--Device-AVMusicTemplateController-downloadMediaEntity(controlType: DownloadControlType, mediaEntity: MediaEntity): Promise<OperResult>-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| controlType | [DownloadControlType](arkts-avsession-avmusictemplate-downloadcontroltype-t.md) | Yes |
| mediaEntity | [MediaEntity](arkts-avsession-avmusictemplate-mediaentity-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[OperResult](arkts-avsession-avmusictemplate-operresult-i.md)&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [35000006](../errorcode-avmusictemplate.md#35000006-template-controller-does-not-exist) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [35000005](../errorcode-avmusictemplate.md#35000005-audio-template-does-not-exist) |
| [35000003](../errorcode-avmusictemplate.md#35000003-template-listener-not-registered) |

## executeAction

```TypeScript
executeAction(actionType: string, params: string): Promise<string>
```

Execute action.

**Since:** 23

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-AVMusicTemplateController-executeAction(actionType: string, params: string): Promise<string>--><!--Device-AVMusicTemplateController-executeAction(actionType: string, params: string): Promise<string>-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| actionType | string | Yes |
| params | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;string & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [35000006](../errorcode-avmusictemplate.md#35000006-template-controller-does-not-exist) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [35000005](../errorcode-avmusictemplate.md#35000005-audio-template-does-not-exist) |
| [35000003](../errorcode-avmusictemplate.md#35000003-template-listener-not-registered) |

## favoriteMediaEntity

```TypeScript
favoriteMediaEntity(actionType: MediaFavoriteType, mediaEntity: MediaEntity): Promise<OperResult>
```

Favorite media entity.

**Since:** 23

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-AVMusicTemplateController-favoriteMediaEntity(actionType: MediaFavoriteType, mediaEntity: MediaEntity): Promise<OperResult>--><!--Device-AVMusicTemplateController-favoriteMediaEntity(actionType: MediaFavoriteType, mediaEntity: MediaEntity): Promise<OperResult>-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| actionType | [MediaFavoriteType](arkts-avsession-avmusictemplate-mediafavoritetype-t.md) | Yes |
| mediaEntity | [MediaEntity](arkts-avsession-avmusictemplate-mediaentity-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[OperResult](arkts-avsession-avmusictemplate-operresult-i.md)&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [35000006](../errorcode-avmusictemplate.md#35000006-template-controller-does-not-exist) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [35000005](../errorcode-avmusictemplate.md#35000005-audio-template-does-not-exist) |
| [35000003](../errorcode-avmusictemplate.md#35000003-template-listener-not-registered) |

## handleMemberPurchase

```TypeScript
handleMemberPurchase(info: MemberPurchaseInfo): Promise<DialogInfo>
```

Handle member purchase.

**Since:** 23

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-AVMusicTemplateController-handleMemberPurchase(info: MemberPurchaseInfo): Promise<DialogInfo>--><!--Device-AVMusicTemplateController-handleMemberPurchase(info: MemberPurchaseInfo): Promise<DialogInfo>-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| info | [MemberPurchaseInfo](arkts-avsession-avmusictemplate-memberpurchaseinfo-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[DialogInfo](arkts-avsession-avmusictemplate-dialoginfo-i.md)&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [35000006](../errorcode-avmusictemplate.md#35000006-template-controller-does-not-exist) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [35000005](../errorcode-avmusictemplate.md#35000005-audio-template-does-not-exist) |
| [35000003](../errorcode-avmusictemplate.md#35000003-template-listener-not-registered) |

## login

```TypeScript
login(controlType: LoginType, id?: string): Promise<QrCodeInfo[]>
```

Login.

**Since:** 23

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-AVMusicTemplateController-login(controlType: LoginType, id?: string): Promise<QrCodeInfo[]>--><!--Device-AVMusicTemplateController-login(controlType: LoginType, id?: string): Promise<QrCodeInfo[]>-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| controlType | [LoginType](arkts-avsession-avmusictemplate-logintype-t.md) | Yes |
| id | string | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[QrCodeInfo](arkts-avsession-avmusictemplate-qrcodeinfo-i.md)[]&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [35000006](../errorcode-avmusictemplate.md#35000006-template-controller-does-not-exist) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [35000005](../errorcode-avmusictemplate.md#35000005-audio-template-does-not-exist) |
| [35000003](../errorcode-avmusictemplate.md#35000003-template-listener-not-registered) |

## offCurrentSingleChange

```TypeScript
offCurrentSingleChange(callback?: Callback<Single>): void
```

Unregister report current single callback.

**Since:** 23

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-AVMusicTemplateController-offCurrentSingleChange(callback?: Callback<Single>): void--><!--Device-AVMusicTemplateController-offCurrentSingleChange(callback?: Callback<Single>): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;Single&gt; | No |

**Error codes:**

| Error Code ID |
| --- |
| [35000006](../errorcode-avmusictemplate.md#35000006-template-controller-does-not-exist) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| 35000012 |

## offCustomElementsChange

```TypeScript
offCustomElementsChange(callback?: ReportCustomElementsChangeEvent): void
```

Unregister report custom elements change callback.

**Since:** 23

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-AVMusicTemplateController-offCustomElementsChange(callback?: ReportCustomElementsChangeEvent): void--><!--Device-AVMusicTemplateController-offCustomElementsChange(callback?: ReportCustomElementsChangeEvent): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [ReportCustomElementsChangeEvent](arkts-avsession-avmusictemplate-reportcustomelementschangeevent-t.md) | No |

**Error codes:**

| Error Code ID |
| --- |
| [35000006](../errorcode-avmusictemplate.md#35000006-template-controller-does-not-exist) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| 35000012 |

## offDialogCommandChange

```TypeScript
offDialogCommandChange(callback?: ReportDialogCommandEvent): void
```

Unregister report dialog command callback.

**Since:** 23

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-AVMusicTemplateController-offDialogCommandChange(callback?: ReportDialogCommandEvent): void--><!--Device-AVMusicTemplateController-offDialogCommandChange(callback?: ReportDialogCommandEvent): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [ReportDialogCommandEvent](arkts-avsession-avmusictemplate-reportdialogcommandevent-t.md) | No |

**Error codes:**

| Error Code ID |
| --- |
| [35000006](../errorcode-avmusictemplate.md#35000006-template-controller-does-not-exist) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| 35000012 |

## offDownloadMediaEntityStatusChange

```TypeScript
offDownloadMediaEntityStatusChange(callback?: Callback<MediaEntity>): void
```

Unregister report download media entity status callback.

**Since:** 23

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-AVMusicTemplateController-offDownloadMediaEntityStatusChange(callback?: Callback<MediaEntity>): void--><!--Device-AVMusicTemplateController-offDownloadMediaEntityStatusChange(callback?: Callback<MediaEntity>): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[MediaEntity](arkts-avsession-avmusictemplate-mediaentity-i.md)&gt; | No |

**Error codes:**

| Error Code ID |
| --- |
| [35000006](../errorcode-avmusictemplate.md#35000006-template-controller-does-not-exist) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| 35000012 |

## offExtensionAbilityChange

```TypeScript
offExtensionAbilityChange(callback?: ReportExecuteAbilityEvent): void
```

Unregister report extension ability callback.

**Since:** 23

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-AVMusicTemplateController-offExtensionAbilityChange(callback?: ReportExecuteAbilityEvent): void--><!--Device-AVMusicTemplateController-offExtensionAbilityChange(callback?: ReportExecuteAbilityEvent): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [ReportExecuteAbilityEvent](arkts-avsession-avmusictemplate-reportexecuteabilityevent-t.md) | No |

**Error codes:**

| Error Code ID |
| --- |
| [35000006](../errorcode-avmusictemplate.md#35000006-template-controller-does-not-exist) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| 35000012 |

## offMediaEntitiesChange

```TypeScript
offMediaEntitiesChange(callback?: Callback<MediaEntity[]>): void
```

Unregister report media entities change callback.

**Since:** 23

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-AVMusicTemplateController-offMediaEntitiesChange(callback?: Callback<MediaEntity[]>): void--><!--Device-AVMusicTemplateController-offMediaEntitiesChange(callback?: Callback<MediaEntity[]>): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[MediaEntity](arkts-avsession-avmusictemplate-mediaentity-i.md)[]&gt; | No |

**Error codes:**

| Error Code ID |
| --- |
| [35000006](../errorcode-avmusictemplate.md#35000006-template-controller-does-not-exist) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| 35000012 |

## offPlaylistChange

```TypeScript
offPlaylistChange(callback?: Callback<PageMediaEntity>): void
```

Unregister report playlist callback.

**Since:** 23

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-AVMusicTemplateController-offPlaylistChange(callback?: Callback<PageMediaEntity>): void--><!--Device-AVMusicTemplateController-offPlaylistChange(callback?: Callback<PageMediaEntity>): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[PageMediaEntity](arkts-avsession-avmusictemplate-pagemediaentity-i.md)&gt; | No |

**Error codes:**

| Error Code ID |
| --- |
| [35000006](../errorcode-avmusictemplate.md#35000006-template-controller-does-not-exist) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| 35000012 |

## offReportExecuteAction

```TypeScript
offReportExecuteAction(callback?: ReportExecuteActionEvent): void
```

Unregister report execute action callback.

**Since:** 23

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-AVMusicTemplateController-offReportExecuteAction(callback?: ReportExecuteActionEvent): void--><!--Device-AVMusicTemplateController-offReportExecuteAction(callback?: ReportExecuteActionEvent): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [ReportExecuteActionEvent](arkts-avsession-avmusictemplate-reportexecuteactionevent-t.md) | No |

**Error codes:**

| Error Code ID |
| --- |
| [35000006](../errorcode-avmusictemplate.md#35000006-template-controller-does-not-exist) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| 35000012 |

## offSettingsChange

```TypeScript
offSettingsChange(callback?: Callback<SettingItem[]>): void
```

Unregister report settings callback.

**Since:** 23

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-AVMusicTemplateController-offSettingsChange(callback?: Callback<SettingItem[]>): void--><!--Device-AVMusicTemplateController-offSettingsChange(callback?: Callback<SettingItem[]>): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[SettingItem](arkts-avsession-avmusictemplate-settingitem-i.md)[]&gt; | No |

**Error codes:**

| Error Code ID |
| --- |
| [35000006](../errorcode-avmusictemplate.md#35000006-template-controller-does-not-exist) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| 35000012 |

## offTabContentChange

```TypeScript
offTabContentChange(callback?: ReportTabContentEvent): void
```

Unregister report tab content callback.

**Since:** 23

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-AVMusicTemplateController-offTabContentChange(callback?: ReportTabContentEvent): void--><!--Device-AVMusicTemplateController-offTabContentChange(callback?: ReportTabContentEvent): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [ReportTabContentEvent](arkts-avsession-avmusictemplate-reporttabcontentevent-t.md) | No |

**Error codes:**

| Error Code ID |
| --- |
| [35000006](../errorcode-avmusictemplate.md#35000006-template-controller-does-not-exist) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| 35000012 |

## offUserInfoChange

```TypeScript
offUserInfoChange(callback?: Callback<UserInfo>): void
```

Unregister report user info callback.

**Since:** 23

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-AVMusicTemplateController-offUserInfoChange(callback?: Callback<UserInfo>): void--><!--Device-AVMusicTemplateController-offUserInfoChange(callback?: Callback<UserInfo>): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;UserInfo&gt; | No |

**Error codes:**

| Error Code ID |
| --- |
| [35000006](../errorcode-avmusictemplate.md#35000006-template-controller-does-not-exist) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| 35000012 |

## onCurrentSingleChange

```TypeScript
onCurrentSingleChange(callback: Callback<Single>): void
```

Register report current single callback.

**Since:** 23

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-AVMusicTemplateController-onCurrentSingleChange(callback: Callback<Single>): void--><!--Device-AVMusicTemplateController-onCurrentSingleChange(callback: Callback<Single>): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;Single&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [35000006](../errorcode-avmusictemplate.md#35000006-template-controller-does-not-exist) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| 35000012 |

## onCustomElementsChange

```TypeScript
onCustomElementsChange(callback: ReportCustomElementsChangeEvent): void
```

Register report custom elements change callback.

**Since:** 23

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-AVMusicTemplateController-onCustomElementsChange(callback: ReportCustomElementsChangeEvent): void--><!--Device-AVMusicTemplateController-onCustomElementsChange(callback: ReportCustomElementsChangeEvent): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [ReportCustomElementsChangeEvent](arkts-avsession-avmusictemplate-reportcustomelementschangeevent-t.md) | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [35000006](../errorcode-avmusictemplate.md#35000006-template-controller-does-not-exist) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| 35000012 |

## onDialogCommandChange

```TypeScript
onDialogCommandChange(callback: ReportDialogCommandEvent): void
```

Register report dialog command callback.

**Since:** 23

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-AVMusicTemplateController-onDialogCommandChange(callback: ReportDialogCommandEvent): void--><!--Device-AVMusicTemplateController-onDialogCommandChange(callback: ReportDialogCommandEvent): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [ReportDialogCommandEvent](arkts-avsession-avmusictemplate-reportdialogcommandevent-t.md) | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [35000006](../errorcode-avmusictemplate.md#35000006-template-controller-does-not-exist) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| 35000012 |

## onDownloadMediaEntityStatusChange

```TypeScript
onDownloadMediaEntityStatusChange(callback: Callback<MediaEntity>): void
```

Register report download media entity status callback.

**Since:** 23

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-AVMusicTemplateController-onDownloadMediaEntityStatusChange(callback: Callback<MediaEntity>): void--><!--Device-AVMusicTemplateController-onDownloadMediaEntityStatusChange(callback: Callback<MediaEntity>): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[MediaEntity](arkts-avsession-avmusictemplate-mediaentity-i.md)&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [35000006](../errorcode-avmusictemplate.md#35000006-template-controller-does-not-exist) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| 35000012 |

## onExtensionAbilityChange

```TypeScript
onExtensionAbilityChange(callback: ReportExecuteAbilityEvent): void
```

Register report extension ability callback.

**Since:** 23

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-AVMusicTemplateController-onExtensionAbilityChange(callback: ReportExecuteAbilityEvent): void--><!--Device-AVMusicTemplateController-onExtensionAbilityChange(callback: ReportExecuteAbilityEvent): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [ReportExecuteAbilityEvent](arkts-avsession-avmusictemplate-reportexecuteabilityevent-t.md) | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [35000006](../errorcode-avmusictemplate.md#35000006-template-controller-does-not-exist) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| 35000012 |

## onMediaEntitiesChange

```TypeScript
onMediaEntitiesChange(callback: Callback<MediaEntity[]>): void
```

Register report media entities change callback.

**Since:** 23

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-AVMusicTemplateController-onMediaEntitiesChange(callback: Callback<MediaEntity[]>): void--><!--Device-AVMusicTemplateController-onMediaEntitiesChange(callback: Callback<MediaEntity[]>): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[MediaEntity](arkts-avsession-avmusictemplate-mediaentity-i.md)[]&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [35000006](../errorcode-avmusictemplate.md#35000006-template-controller-does-not-exist) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| 35000012 |

## onPlaylistChange

```TypeScript
onPlaylistChange(callback: Callback<PageMediaEntity>): void
```

Register report playlist callback.

**Since:** 23

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-AVMusicTemplateController-onPlaylistChange(callback: Callback<PageMediaEntity>): void--><!--Device-AVMusicTemplateController-onPlaylistChange(callback: Callback<PageMediaEntity>): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[PageMediaEntity](arkts-avsession-avmusictemplate-pagemediaentity-i.md)&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [35000006](../errorcode-avmusictemplate.md#35000006-template-controller-does-not-exist) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| 35000012 |

## onReportExecuteAction

```TypeScript
onReportExecuteAction(callback: ReportExecuteActionEvent): void
```

Register report execute action callback.

**Since:** 23

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-AVMusicTemplateController-onReportExecuteAction(callback: ReportExecuteActionEvent): void--><!--Device-AVMusicTemplateController-onReportExecuteAction(callback: ReportExecuteActionEvent): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [ReportExecuteActionEvent](arkts-avsession-avmusictemplate-reportexecuteactionevent-t.md) | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [35000006](../errorcode-avmusictemplate.md#35000006-template-controller-does-not-exist) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| 35000012 |

## onSettingsChange

```TypeScript
onSettingsChange(callback: Callback<SettingItem[]>): void
```

Register report settings callback.

**Since:** 23

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-AVMusicTemplateController-onSettingsChange(callback: Callback<SettingItem[]>): void--><!--Device-AVMusicTemplateController-onSettingsChange(callback: Callback<SettingItem[]>): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[SettingItem](arkts-avsession-avmusictemplate-settingitem-i.md)[]&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [35000006](../errorcode-avmusictemplate.md#35000006-template-controller-does-not-exist) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| 35000012 |

## onTabContentChange

```TypeScript
onTabContentChange(callback: ReportTabContentEvent): void
```

Register report tab content callback.

**Since:** 23

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-AVMusicTemplateController-onTabContentChange(callback: ReportTabContentEvent): void--><!--Device-AVMusicTemplateController-onTabContentChange(callback: ReportTabContentEvent): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [ReportTabContentEvent](arkts-avsession-avmusictemplate-reporttabcontentevent-t.md) | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [35000006](../errorcode-avmusictemplate.md#35000006-template-controller-does-not-exist) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| 35000012 |

## onUserInfoChange

```TypeScript
onUserInfoChange(callback: Callback<UserInfo>): void
```

Register report user info callback.

**Since:** 23

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-AVMusicTemplateController-onUserInfoChange(callback: Callback<UserInfo>): void--><!--Device-AVMusicTemplateController-onUserInfoChange(callback: Callback<UserInfo>): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;UserInfo&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [35000006](../errorcode-avmusictemplate.md#35000006-template-controller-does-not-exist) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| 35000012 |

## playForSearch

```TypeScript
playForSearch(command: SearchPlayInfoType, args: SearchPlayInfo): Promise<OperResult>
```

Play for search.

**Since:** 23

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-AVMusicTemplateController-playForSearch(command: SearchPlayInfoType, args: SearchPlayInfo): Promise<OperResult>--><!--Device-AVMusicTemplateController-playForSearch(command: SearchPlayInfoType, args: SearchPlayInfo): Promise<OperResult>-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| command | [SearchPlayInfoType](arkts-avsession-avmusictemplate-searchplayinfotype-e.md) | Yes |
| [args](../../apis-arkdata/arkts-apis/arkts-arkdata-relationalstore-sqlinfo-i.md) | [SearchPlayInfo](arkts-avsession-avmusictemplate-searchplayinfo-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[OperResult](arkts-avsession-avmusictemplate-operresult-i.md)&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [35000006](../errorcode-avmusictemplate.md#35000006-template-controller-does-not-exist) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [35000005](../errorcode-avmusictemplate.md#35000005-audio-template-does-not-exist) |
| [35000003](../errorcode-avmusictemplate.md#35000003-template-listener-not-registered) |

## playMediaEntity

```TypeScript
playMediaEntity(mediaEntity: MediaEntity): Promise<void>
```

Play media entity.

**Since:** 23

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-AVMusicTemplateController-playMediaEntity(mediaEntity: MediaEntity): Promise<void>--><!--Device-AVMusicTemplateController-playMediaEntity(mediaEntity: MediaEntity): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| mediaEntity | [MediaEntity](arkts-avsession-avmusictemplate-mediaentity-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [35000006](../errorcode-avmusictemplate.md#35000006-template-controller-does-not-exist) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [35000005](../errorcode-avmusictemplate.md#35000005-audio-template-does-not-exist) |
| [35000003](../errorcode-avmusictemplate.md#35000003-template-listener-not-registered) |

## queryCompilation

```TypeScript
queryCompilation(compilationId: string, pageIndex: number): Promise<PageMediaEntity>
```

Query compilation.

**Since:** 23

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-AVMusicTemplateController-queryCompilation(compilationId: string, pageIndex: int): Promise<PageMediaEntity>--><!--Device-AVMusicTemplateController-queryCompilation(compilationId: string, pageIndex: int): Promise<PageMediaEntity>-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| compilationId | string | Yes |
| pageIndex | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[PageMediaEntity](arkts-avsession-avmusictemplate-pagemediaentity-i.md)&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [35000006](../errorcode-avmusictemplate.md#35000006-template-controller-does-not-exist) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [35000005](../errorcode-avmusictemplate.md#35000005-audio-template-does-not-exist) |
| [35000003](../errorcode-avmusictemplate.md#35000003-template-listener-not-registered) |

## queryCompilationByKeyword

```TypeScript
queryCompilationByKeyword(keyword: string): Promise<Compilation[]>
```

Query compilation by keyword.

**Since:** 23

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-AVMusicTemplateController-queryCompilationByKeyword(keyword: string): Promise<Compilation[]>--><!--Device-AVMusicTemplateController-queryCompilationByKeyword(keyword: string): Promise<Compilation[]>-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| keyword | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[Compilation](arkts-avsession-avmusictemplate-compilation-i.md)[]&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [35000006](../errorcode-avmusictemplate.md#35000006-template-controller-does-not-exist) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [35000005](../errorcode-avmusictemplate.md#35000005-audio-template-does-not-exist) |
| [35000003](../errorcode-avmusictemplate.md#35000003-template-listener-not-registered) |

## queryCurrentSingle

```TypeScript
queryCurrentSingle(): Promise<Single>
```

Query current single.

**Since:** 23

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-AVMusicTemplateController-queryCurrentSingle(): Promise<Single>--><!--Device-AVMusicTemplateController-queryCurrentSingle(): Promise<Single>-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;Single & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [35000006](../errorcode-avmusictemplate.md#35000006-template-controller-does-not-exist) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [35000005](../errorcode-avmusictemplate.md#35000005-audio-template-does-not-exist) |
| [35000003](../errorcode-avmusictemplate.md#35000003-template-listener-not-registered) |

## queryCustomContent

```TypeScript
queryCustomContent(queryType: CustomType[]): Promise<CustomElement>
```

Query custom content.

**Since:** 23

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-AVMusicTemplateController-queryCustomContent(queryType: CustomType[]): Promise<CustomElement>--><!--Device-AVMusicTemplateController-queryCustomContent(queryType: CustomType[]): Promise<CustomElement>-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [queryType](../../apis-ability-kit/arkts-apis/arkts-ability-insightintent-queryentityparam-i.md) | [CustomType](arkts-avsession-avmusictemplate-customtype-t.md)[] | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[CustomElement](arkts-avsession-avmusictemplate-customelement-i.md)&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [35000006](../errorcode-avmusictemplate.md#35000006-template-controller-does-not-exist) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [35000005](../errorcode-avmusictemplate.md#35000005-audio-template-does-not-exist) |
| [35000003](../errorcode-avmusictemplate.md#35000003-template-listener-not-registered) |

## queryHotWords

```TypeScript
queryHotWords(): Promise<string[]>
```

Query hot words.

**Since:** 23

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-AVMusicTemplateController-queryHotWords(): Promise<string[]>--><!--Device-AVMusicTemplateController-queryHotWords(): Promise<string[]>-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;string[] & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [35000006](../errorcode-avmusictemplate.md#35000006-template-controller-does-not-exist) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [35000005](../errorcode-avmusictemplate.md#35000005-audio-template-does-not-exist) |
| [35000003](../errorcode-avmusictemplate.md#35000003-template-listener-not-registered) |

## queryMainTabs

```TypeScript
queryMainTabs(): Promise<MediaTab[]>
```

Query main tabs.

**Since:** 23

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-AVMusicTemplateController-queryMainTabs(): Promise<MediaTab[]>--><!--Device-AVMusicTemplateController-queryMainTabs(): Promise<MediaTab[]>-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[MediaTab](arkts-avsession-avmusictemplate-mediatab-i.md)[]&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [35000006](../errorcode-avmusictemplate.md#35000006-template-controller-does-not-exist) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [35000005](../errorcode-avmusictemplate.md#35000005-audio-template-does-not-exist) |
| [35000003](../errorcode-avmusictemplate.md#35000003-template-listener-not-registered) |

## queryMediaEntity

```TypeScript
queryMediaEntity(params: QueryMediaEntityParam): Promise<PageMediaEntity>
```

Query media entity.

**Since:** 23

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-AVMusicTemplateController-queryMediaEntity(params: QueryMediaEntityParam): Promise<PageMediaEntity>--><!--Device-AVMusicTemplateController-queryMediaEntity(params: QueryMediaEntityParam): Promise<PageMediaEntity>-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| params | [QueryMediaEntityParam](arkts-avsession-avmusictemplate-querymediaentityparam-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[PageMediaEntity](arkts-avsession-avmusictemplate-pagemediaentity-i.md)&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [35000006](../errorcode-avmusictemplate.md#35000006-template-controller-does-not-exist) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [35000005](../errorcode-avmusictemplate.md#35000005-audio-template-does-not-exist) |
| [35000003](../errorcode-avmusictemplate.md#35000003-template-listener-not-registered) |

## queryMediaEntityByKeyword

```TypeScript
queryMediaEntityByKeyword(keyword: string, searchType: EntityType, pageIndex: number): Promise<PageMediaEntity>
```

Query media entity by keyword.

**Since:** 23

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-AVMusicTemplateController-queryMediaEntityByKeyword(keyword: string, searchType: EntityType, pageIndex: int): Promise<PageMediaEntity>--><!--Device-AVMusicTemplateController-queryMediaEntityByKeyword(keyword: string, searchType: EntityType, pageIndex: int): Promise<PageMediaEntity>-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| keyword | string | Yes |
| searchType | [EntityType](arkts-avsession-avmusictemplate-entitytype-e.md) | Yes |
| pageIndex | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[PageMediaEntity](arkts-avsession-avmusictemplate-pagemediaentity-i.md)&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [35000006](../errorcode-avmusictemplate.md#35000006-template-controller-does-not-exist) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [35000005](../errorcode-avmusictemplate.md#35000005-audio-template-does-not-exist) |
| [35000003](../errorcode-avmusictemplate.md#35000003-template-listener-not-registered) |

## queryMediaTabContent

```TypeScript
queryMediaTabContent(tabId: string): Promise<MediaTabContent>
```

Query media tab content.

**Since:** 23

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-AVMusicTemplateController-queryMediaTabContent(tabId: string): Promise<MediaTabContent>--><!--Device-AVMusicTemplateController-queryMediaTabContent(tabId: string): Promise<MediaTabContent>-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| tabId | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[MediaTabContent](arkts-avsession-avmusictemplate-mediatabcontent-i.md)&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [35000006](../errorcode-avmusictemplate.md#35000006-template-controller-does-not-exist) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [35000005](../errorcode-avmusictemplate.md#35000005-audio-template-does-not-exist) |
| [35000003](../errorcode-avmusictemplate.md#35000003-template-listener-not-registered) |

## queryMemberPurchase

```TypeScript
queryMemberPurchase(memberPurchaseType: MemberPurchaseType): Promise<MemberPurchaseInfo[]>
```

Query member purchase.

**Since:** 23

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-AVMusicTemplateController-queryMemberPurchase(memberPurchaseType: MemberPurchaseType): Promise<MemberPurchaseInfo[]>--><!--Device-AVMusicTemplateController-queryMemberPurchase(memberPurchaseType: MemberPurchaseType): Promise<MemberPurchaseInfo[]>-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [memberPurchaseType](arkts-avsession-avmusictemplate-memberpurchaseinfo-i.md) | [MemberPurchaseType](arkts-avsession-avmusictemplate-memberpurchasetype-e.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[MemberPurchaseInfo](arkts-avsession-avmusictemplate-memberpurchaseinfo-i.md)[]&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [35000006](../errorcode-avmusictemplate.md#35000006-template-controller-does-not-exist) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [35000005](../errorcode-avmusictemplate.md#35000005-audio-template-does-not-exist) |
| [35000003](../errorcode-avmusictemplate.md#35000003-template-listener-not-registered) |

## queryPlaylist

```TypeScript
queryPlaylist(pageIndex: number, sort: Sort): Promise<PageMediaEntity>
```

Query playlist.

**Since:** 23

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-AVMusicTemplateController-queryPlaylist(pageIndex: int, sort: Sort): Promise<PageMediaEntity>--><!--Device-AVMusicTemplateController-queryPlaylist(pageIndex: int, sort: Sort): Promise<PageMediaEntity>-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| pageIndex | number | Yes |
| sort | [Sort](arkts-avsession-avmusictemplate-sort-e.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[PageMediaEntity](arkts-avsession-avmusictemplate-pagemediaentity-i.md)&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [35000006](../errorcode-avmusictemplate.md#35000006-template-controller-does-not-exist) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [35000005](../errorcode-avmusictemplate.md#35000005-audio-template-does-not-exist) |
| [35000003](../errorcode-avmusictemplate.md#35000003-template-listener-not-registered) |

## queryRecommendMediaEntityList

```TypeScript
queryRecommendMediaEntityList(): Promise<MediaEntity[]>
```

Query recommend media entity list.

**Since:** 23

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-AVMusicTemplateController-queryRecommendMediaEntityList(): Promise<MediaEntity[]>--><!--Device-AVMusicTemplateController-queryRecommendMediaEntityList(): Promise<MediaEntity[]>-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[MediaEntity](arkts-avsession-avmusictemplate-mediaentity-i.md)[]&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [35000006](../errorcode-avmusictemplate.md#35000006-template-controller-does-not-exist) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [35000005](../errorcode-avmusictemplate.md#35000005-audio-template-does-not-exist) |
| [35000003](../errorcode-avmusictemplate.md#35000003-template-listener-not-registered) |

## querySearchHistory

```TypeScript
querySearchHistory(): Promise<string[]>
```

Query search history.

**Since:** 23

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-AVMusicTemplateController-querySearchHistory(): Promise<string[]>--><!--Device-AVMusicTemplateController-querySearchHistory(): Promise<string[]>-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;string[] & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [35000006](../errorcode-avmusictemplate.md#35000006-template-controller-does-not-exist) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [35000005](../errorcode-avmusictemplate.md#35000005-audio-template-does-not-exist) |
| [35000003](../errorcode-avmusictemplate.md#35000003-template-listener-not-registered) |

## reportProblemAndAdvice

```TypeScript
reportProblemAndAdvice(advice: string): Promise<OperResult>
```

Report problem and advice.

**Since:** 23

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-AVMusicTemplateController-reportProblemAndAdvice(advice: string): Promise<OperResult>--><!--Device-AVMusicTemplateController-reportProblemAndAdvice(advice: string): Promise<OperResult>-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| advice | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[OperResult](arkts-avsession-avmusictemplate-operresult-i.md)&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [35000006](../errorcode-avmusictemplate.md#35000006-template-controller-does-not-exist) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [35000005](../errorcode-avmusictemplate.md#35000005-audio-template-does-not-exist) |
| [35000003](../errorcode-avmusictemplate.md#35000003-template-listener-not-registered) |

## requestDialogInfo

```TypeScript
requestDialogInfo(actionType: DialogActionType, actionInfo?: DialogActionInfo): Promise<DialogInfo>
```

Request dialog info.

**Since:** 23

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-AVMusicTemplateController-requestDialogInfo(actionType: DialogActionType, actionInfo?: DialogActionInfo): Promise<DialogInfo>--><!--Device-AVMusicTemplateController-requestDialogInfo(actionType: DialogActionType, actionInfo?: DialogActionInfo): Promise<DialogInfo>-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| actionType | [DialogActionType](arkts-avsession-avmusictemplate-dialogactiontype-t.md) | Yes |
| actionInfo | [DialogActionInfo](arkts-avsession-avmusictemplate-dialogactioninfo-i.md) | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[DialogInfo](arkts-avsession-avmusictemplate-dialoginfo-i.md)&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [35000006](../errorcode-avmusictemplate.md#35000006-template-controller-does-not-exist) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [35000005](../errorcode-avmusictemplate.md#35000005-audio-template-does-not-exist) |
| [35000003](../errorcode-avmusictemplate.md#35000003-template-listener-not-registered) |

## sendCustomCommand

```TypeScript
sendCustomCommand(command: string, args: string): Promise<OperResult>
```

Send custom commands to AVMusicTemplate

**Since:** 26.1.0

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-AVMusicTemplateController-sendCustomCommand(command: string, args: string): Promise<OperResult>--><!--Device-AVMusicTemplateController-sendCustomCommand(command: string, args: string): Promise<OperResult>-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| command | string | Yes |
| [args](../../apis-arkdata/arkts-apis/arkts-arkdata-relationalstore-sqlinfo-i.md) | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[OperResult](arkts-avsession-avmusictemplate-operresult-i.md)&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [35000006](../errorcode-avmusictemplate.md#35000006-template-controller-does-not-exist) |
| [35000005](../errorcode-avmusictemplate.md#35000005-audio-template-does-not-exist) |
| [35000003](../errorcode-avmusictemplate.md#35000003-template-listener-not-registered) |

## updateSettings

```TypeScript
updateSettings(settingItem: SettingItem): Promise<SettingItem>
```

Report settings change.

**Since:** 23

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-AVMusicTemplateController-updateSettings(settingItem: SettingItem): Promise<SettingItem>--><!--Device-AVMusicTemplateController-updateSettings(settingItem: SettingItem): Promise<SettingItem>-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| settingItem | [SettingItem](arkts-avsession-avmusictemplate-settingitem-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[SettingItem](arkts-avsession-avmusictemplate-settingitem-i.md)&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [35000006](../errorcode-avmusictemplate.md#35000006-template-controller-does-not-exist) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [35000005](../errorcode-avmusictemplate.md#35000005-audio-template-does-not-exist) |
| [35000003](../errorcode-avmusictemplate.md#35000003-template-listener-not-registered) |

## isDestroy

```TypeScript
isDestroy: boolean
```

Mark the controller is or not destroy.

**Type:** boolean

**Since:** 23

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-AVMusicTemplateController-isDestroy: boolean--><!--Device-AVMusicTemplateController-isDestroy: boolean-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVMusicTemplate

## sessionId

```TypeScript
sessionId: string
```

Unique id of the AVMusicTemplateController.

**Type:** string

**Since:** 23

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-AVMusicTemplateController-sessionId: string--><!--Device-AVMusicTemplateController-sessionId: string-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVMusicTemplate
