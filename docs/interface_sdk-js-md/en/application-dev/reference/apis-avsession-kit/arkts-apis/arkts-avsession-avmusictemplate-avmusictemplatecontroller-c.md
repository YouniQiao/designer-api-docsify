# AVMusicTemplateController

音频模板控制器，可以获得音频模板控制器唯一的标识，用于与接入音频模板的媒体应用数据交互。

> **说明：**
> 
> - 本模块仅适用于API version 23及以上版本的Car设备。

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-avMusicTemplate-class AVMusicTemplateController--><!--Device-avMusicTemplate-class AVMusicTemplateController-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVMusicTemplate

## Modules to Import

```TypeScript
import { avMusicTemplate } from 'kits/@kit.AVSessionKit';
```

## clearSearchHistory

```TypeScript
clearSearchHistory(): Promise<OperResult>
```

清除搜索历史。使用Promise异步回调。

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AVMusicTemplateController-clearSearchHistory(): Promise<OperResult>--><!--Device-AVMusicTemplateController-clearSearchHistory(): Promise<OperResult>-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;OperResult&gt; | Promise对象，返回清除搜索历史的操作结果。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 35000006 | AVMusicTemplateController does not exist. |
| 801 | capability not supported. |
| 35000005 | AVMusicTemplate does not exist. |
| 35000003 | Template listener not registered. |

## destroy

```TypeScript
destroy(): Promise<void>
```

销毁音频模板控制器。使用Promise异步回调。

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AVMusicTemplateController-destroy(): Promise<void>--><!--Device-AVMusicTemplateController-destroy(): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise对象，无返回结果。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 801 | capability not supported. |

## downloadMediaEntity

```TypeScript
downloadMediaEntity(controlType: DownloadControlType, mediaEntity: MediaEntity): Promise<OperResult>
```

下载媒体实体。使用Promise异步回调。

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AVMusicTemplateController-downloadMediaEntity(controlType: DownloadControlType, mediaEntity: MediaEntity): Promise<OperResult>--><!--Device-AVMusicTemplateController-downloadMediaEntity(controlType: DownloadControlType, mediaEntity: MediaEntity): Promise<OperResult>-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| controlType | [DownloadControlType](arkts-avsession-avmusictemplate-downloadcontroltype-t.md) | Yes | 下载的控制类型。 |
| mediaEntity | [MediaEntity](arkts-avsession-avmusictemplate-mediaentity-i.md) | Yes | 媒体实体。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;OperResult&gt; | Promise对象，返回下载媒体实体的操作结果。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 35000006 | AVMusicTemplateController does not exist. |
| 801 | capability not supported. |
| 35000005 | AVMusicTemplate does not exist. |
| 35000003 | Template listener not registered. |

## executeAction

```TypeScript
executeAction(actionType: string, params: string): Promise<string>
```

执行动作。使用Promise异步回调。

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AVMusicTemplateController-executeAction(actionType: string, params: string): Promise<string>--><!--Device-AVMusicTemplateController-executeAction(actionType: string, params: string): Promise<string>-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| actionType | string | Yes | 动作类型。 |
| params | string | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;string&gt; | Promise对象，返回执行动作的结果。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 35000006 | AVMusicTemplateController does not exist. |
| 801 | capability not supported. |
| 35000005 | AVMusicTemplate does not exist. |
| 35000003 | Template listener not registered. |

## favoriteMediaEntity

```TypeScript
favoriteMediaEntity(actionType: MediaFavoriteType, mediaEntity: MediaEntity): Promise<OperResult>
```

收藏媒体。使用Promise异步回调。

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AVMusicTemplateController-favoriteMediaEntity(actionType: MediaFavoriteType, mediaEntity: MediaEntity): Promise<OperResult>--><!--Device-AVMusicTemplateController-favoriteMediaEntity(actionType: MediaFavoriteType, mediaEntity: MediaEntity): Promise<OperResult>-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| actionType | [MediaFavoriteType](arkts-avsession-avmusictemplate-mediafavoritetype-t.md) | Yes | 媒体收藏的类型。 |
| mediaEntity | [MediaEntity](arkts-avsession-avmusictemplate-mediaentity-i.md) | Yes | 媒体实体。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;OperResult&gt; | Promise对象，返回收藏媒体的操作结果。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 35000006 | AVMusicTemplateController does not exist. |
| 801 | capability not supported. |
| 35000005 | AVMusicTemplate does not exist. |
| 35000003 | Template listener not registered. |

## handleMemberPurchase

```TypeScript
handleMemberPurchase(info: MemberPurchaseInfo): Promise<DialogInfo>
```

处理购买会员情况。使用Promise异步回调。

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AVMusicTemplateController-handleMemberPurchase(info: MemberPurchaseInfo): Promise<DialogInfo>--><!--Device-AVMusicTemplateController-handleMemberPurchase(info: MemberPurchaseInfo): Promise<DialogInfo>-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| info | [MemberPurchaseInfo](arkts-avsession-avmusictemplate-memberpurchaseinfo-i.md) | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;DialogInfo&gt; | Promise对象，返回对话框信息。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 35000006 | AVMusicTemplateController does not exist. |
| 801 | capability not supported. |
| 35000005 | AVMusicTemplate does not exist. |
| 35000003 | Template listener not registered. |

## login

```TypeScript
login(controlType: LoginType, id?: string): Promise<QrCodeInfo[]>
```

登录。使用Promise异步回调。

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AVMusicTemplateController-login(controlType: LoginType, id?: string): Promise<QrCodeInfo[]>--><!--Device-AVMusicTemplateController-login(controlType: LoginType, id?: string): Promise<QrCodeInfo[]>-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| controlType | [LoginType](arkts-avsession-avmusictemplate-logintype-t.md) | Yes | 登录类型。 |
| id | string | No |  |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;QrCodeInfo[]&gt; | Promise对象，返回二维码信息的数组。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 35000006 | AVMusicTemplateController does not exist. |
| 801 | capability not supported. |
| 35000005 | AVMusicTemplate does not exist. |
| 35000003 | Template listener not registered. |

## offCurrentSingleChange

```TypeScript
offCurrentSingleChange(callback?: Callback<Single>): void
```

注销当前单曲改变的回调。使用callback异步回调。

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AVMusicTemplateController-offCurrentSingleChange(callback?: Callback<Single>): void--><!--Device-AVMusicTemplateController-offCurrentSingleChange(callback?: Callback<Single>): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;Single&gt; | No | 回调函数，返回当前单曲的信息。不填该参数则注销该类型对应的所有回调。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 35000006 | AVMusicTemplateController does not exist. |
| 801 | capability not supported. |
| 35000012 | AVMusicTemplate error. |

## offCustomElementsChange

```TypeScript
offCustomElementsChange(callback?: ReportCustomElementsChangeEvent): void
```

注销上报自定义元素改变的回调。

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AVMusicTemplateController-offCustomElementsChange(callback?: ReportCustomElementsChangeEvent): void--><!--Device-AVMusicTemplateController-offCustomElementsChange(callback?: ReportCustomElementsChangeEvent): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [ReportCustomElementsChangeEvent](arkts-avsession-avmusictemplate-reportcustomelementschangeevent-t.md) | No | 上报自定义元素改变事件。不填该参数则注销该类型对应的所有回调。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 35000006 | AVMusicTemplateController does not exist. |
| 801 | capability not supported. |
| 35000012 | AVMusicTemplate error. |

## offDialogCommandChange

```TypeScript
offDialogCommandChange(callback?: ReportDialogCommandEvent): void
```

注销对话框命令改变的回调。

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AVMusicTemplateController-offDialogCommandChange(callback?: ReportDialogCommandEvent): void--><!--Device-AVMusicTemplateController-offDialogCommandChange(callback?: ReportDialogCommandEvent): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [ReportDialogCommandEvent](arkts-avsession-avmusictemplate-reportdialogcommandevent-t.md) | No | 上报对话框命令事件。不填该参数则注销该类型对应的所有回调。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 35000006 | AVMusicTemplateController does not exist. |
| 801 | capability not supported. |
| 35000012 | AVMusicTemplate error. |

## offDownloadMediaEntityStatusChange

```TypeScript
offDownloadMediaEntityStatusChange(callback?: Callback<MediaEntity>): void
```

注销上报下载媒体状态改变的回调。使用callback异步回调。

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AVMusicTemplateController-offDownloadMediaEntityStatusChange(callback?: Callback<MediaEntity>): void--><!--Device-AVMusicTemplateController-offDownloadMediaEntityStatusChange(callback?: Callback<MediaEntity>): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;MediaEntity&gt; | No | 回调函数，返回媒体实体信息。不填该参数则注销该类型对应的所有回调。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 35000006 | AVMusicTemplateController does not exist. |
| 801 | capability not supported. |
| 35000012 | AVMusicTemplate error. |

## offExtensionAbilityChange

```TypeScript
offExtensionAbilityChange(callback?: ReportExecuteAbilityEvent): void
```

注销回调，用于停止监听拉起指定媒体应用的请求。

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AVMusicTemplateController-offExtensionAbilityChange(callback?: ReportExecuteAbilityEvent): void--><!--Device-AVMusicTemplateController-offExtensionAbilityChange(callback?: ReportExecuteAbilityEvent): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [ReportExecuteAbilityEvent](arkts-avsession-avmusictemplate-reportexecuteabilityevent-t.md) | No | 通知音频模板控制方拉起指定的媒体应用界面的事件回调。不填该参数则注销该类型对应的所有回调。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 35000006 | AVMusicTemplateController does not exist. |
| 801 | capability not supported. |
| 35000012 | AVMusicTemplate error. |

## offMediaEntitiesChange

```TypeScript
offMediaEntitiesChange(callback?: Callback<MediaEntity[]>): void
```

注销媒体实体改变的回调。使用callback异步回调。

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AVMusicTemplateController-offMediaEntitiesChange(callback?: Callback<MediaEntity[]>): void--><!--Device-AVMusicTemplateController-offMediaEntitiesChange(callback?: Callback<MediaEntity[]>): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;MediaEntity[]&gt; | No | 回调函数，返回媒体实体数组。不填该参数则注销该类型对应的所有回调。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 35000006 | AVMusicTemplateController does not exist. |
| 801 | capability not supported. |
| 35000012 | AVMusicTemplate error. |

## offPlaylistChange

```TypeScript
offPlaylistChange(callback?: Callback<PageMediaEntity>): void
```

注销上报播放列表改变的回调。使用callback异步回调。

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AVMusicTemplateController-offPlaylistChange(callback?: Callback<PageMediaEntity>): void--><!--Device-AVMusicTemplateController-offPlaylistChange(callback?: Callback<PageMediaEntity>): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;PageMediaEntity&gt; | No | 回调函数，返回标签页媒体实体信息。不填该参数则注销该类型对应的所有回调。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 35000006 | AVMusicTemplateController does not exist. |
| 801 | capability not supported. |
| 35000012 | AVMusicTemplate error. |

## offReportExecuteAction

```TypeScript
offReportExecuteAction(callback?: ReportExecuteActionEvent): void
```

注销上报执行动作的回调。

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AVMusicTemplateController-offReportExecuteAction(callback?: ReportExecuteActionEvent): void--><!--Device-AVMusicTemplateController-offReportExecuteAction(callback?: ReportExecuteActionEvent): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [ReportExecuteActionEvent](arkts-avsession-avmusictemplate-reportexecuteactionevent-t.md) | No | 上报执行动作的事件。不填该参数则注销该类型对应的所有回调。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 35000006 | AVMusicTemplateController does not exist. |
| 801 | capability not supported. |
| 35000012 | AVMusicTemplate error. |

## offSettingsChange

```TypeScript
offSettingsChange(callback?: Callback<SettingItem[]>): void
```

注销上报设置改变的回调。使用callback异步回调。

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AVMusicTemplateController-offSettingsChange(callback?: Callback<SettingItem[]>): void--><!--Device-AVMusicTemplateController-offSettingsChange(callback?: Callback<SettingItem[]>): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;SettingItem[]&gt; | No | 回调函数，用于接收并处理设置项数组。不填该参数则注销该类型对应的所有回调。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 35000006 | AVMusicTemplateController does not exist. |
| 801 | capability not supported. |
| 35000012 | AVMusicTemplate error. |

## offTabContentChange

```TypeScript
offTabContentChange(callback?: ReportTabContentEvent): void
```

注销标签页内容改变的回调。

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AVMusicTemplateController-offTabContentChange(callback?: ReportTabContentEvent): void--><!--Device-AVMusicTemplateController-offTabContentChange(callback?: ReportTabContentEvent): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [ReportTabContentEvent](arkts-avsession-avmusictemplate-reporttabcontentevent-t.md) | No | 上报标签页内容事件。不填该参数则注销该类型对应的所有回调。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 35000006 | AVMusicTemplateController does not exist. |
| 801 | capability not supported. |
| 35000012 | AVMusicTemplate error. |

## offUserInfoChange

```TypeScript
offUserInfoChange(callback?: Callback<UserInfo>): void
```

注销用户信息改变的回调。使用callback异步回调。

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AVMusicTemplateController-offUserInfoChange(callback?: Callback<UserInfo>): void--><!--Device-AVMusicTemplateController-offUserInfoChange(callback?: Callback<UserInfo>): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;UserInfo&gt; | No | 回调函数，返回用户信息。不填该参数则注销该类型对应的所有回调。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 35000006 | AVMusicTemplateController does not exist. |
| 801 | capability not supported. |
| 35000012 | AVMusicTemplate error. |

## onCurrentSingleChange

```TypeScript
onCurrentSingleChange(callback: Callback<Single>): void
```

注册当前单曲改变的回调。使用callback异步回调。

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AVMusicTemplateController-onCurrentSingleChange(callback: Callback<Single>): void--><!--Device-AVMusicTemplateController-onCurrentSingleChange(callback: Callback<Single>): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;Single&gt; | Yes | 回调函数，返回当前单曲的信息。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 35000006 | AVMusicTemplateController does not exist. |
| 801 | capability not supported. |
| 35000012 | AVMusicTemplate error. |

## onCustomElementsChange

```TypeScript
onCustomElementsChange(callback: ReportCustomElementsChangeEvent): void
```

注册上报自定义元素改变的回调。使用callback异步回调。

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AVMusicTemplateController-onCustomElementsChange(callback: ReportCustomElementsChangeEvent): void--><!--Device-AVMusicTemplateController-onCustomElementsChange(callback: ReportCustomElementsChangeEvent): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [ReportCustomElementsChangeEvent](arkts-avsession-avmusictemplate-reportcustomelementschangeevent-t.md) | Yes | 回调函数，上报自定义元素改变事件。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 35000006 | AVMusicTemplateController does not exist. |
| 801 | capability not supported. |
| 35000012 | AVMusicTemplate error. |

## onDialogCommandChange

```TypeScript
onDialogCommandChange(callback: ReportDialogCommandEvent): void
```

注册对话框命令改变的回调。使用callback异步回调。

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AVMusicTemplateController-onDialogCommandChange(callback: ReportDialogCommandEvent): void--><!--Device-AVMusicTemplateController-onDialogCommandChange(callback: ReportDialogCommandEvent): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [ReportDialogCommandEvent](arkts-avsession-avmusictemplate-reportdialogcommandevent-t.md) | Yes | 回调函数，上报对话框命令事件。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 35000006 | AVMusicTemplateController does not exist. |
| 801 | capability not supported. |
| 35000012 | AVMusicTemplate error. |

## onDownloadMediaEntityStatusChange

```TypeScript
onDownloadMediaEntityStatusChange(callback: Callback<MediaEntity>): void
```

注册上报下载媒体状态改变的回调。使用callback异步回调。

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AVMusicTemplateController-onDownloadMediaEntityStatusChange(callback: Callback<MediaEntity>): void--><!--Device-AVMusicTemplateController-onDownloadMediaEntityStatusChange(callback: Callback<MediaEntity>): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;MediaEntity&gt; | Yes | 回调函数，返回媒体实体信息。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 35000006 | AVMusicTemplateController does not exist. |
| 801 | capability not supported. |
| 35000012 | AVMusicTemplate error. |

## onExtensionAbilityChange

```TypeScript
onExtensionAbilityChange(callback: ReportExecuteAbilityEvent): void
```

注册回调，当需要拉起指定媒体应用界面时触发。使用callback异步回调。

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AVMusicTemplateController-onExtensionAbilityChange(callback: ReportExecuteAbilityEvent): void--><!--Device-AVMusicTemplateController-onExtensionAbilityChange(callback: ReportExecuteAbilityEvent): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [ReportExecuteAbilityEvent](arkts-avsession-avmusictemplate-reportexecuteabilityevent-t.md) | Yes | 回调函数，通知音频模板控制方拉起指定三方应用界面的事件，包含应用包名和界面名称等信息。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 35000006 | AVMusicTemplateController does not exist. |
| 801 | capability not supported. |
| 35000012 | AVMusicTemplate error. |

## onMediaEntitiesChange

```TypeScript
onMediaEntitiesChange(callback: Callback<MediaEntity[]>): void
```

注册媒体实体改变的回调。使用callback异步回调。

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AVMusicTemplateController-onMediaEntitiesChange(callback: Callback<MediaEntity[]>): void--><!--Device-AVMusicTemplateController-onMediaEntitiesChange(callback: Callback<MediaEntity[]>): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;MediaEntity[]&gt; | Yes | 回调函数，返回媒体实体数组。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 35000006 | AVMusicTemplateController does not exist. |
| 801 | capability not supported. |
| 35000012 | AVMusicTemplate error. |

## onPlaylistChange

```TypeScript
onPlaylistChange(callback: Callback<PageMediaEntity>): void
```

注册上报播放列表改变的回调。使用callback异步回调。

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AVMusicTemplateController-onPlaylistChange(callback: Callback<PageMediaEntity>): void--><!--Device-AVMusicTemplateController-onPlaylistChange(callback: Callback<PageMediaEntity>): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;PageMediaEntity&gt; | Yes | 回调函数，返回标签页媒体实体信息。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 35000006 | AVMusicTemplateController does not exist. |
| 801 | capability not supported. |
| 35000012 | AVMusicTemplate error. |

## onReportExecuteAction

```TypeScript
onReportExecuteAction(callback: ReportExecuteActionEvent): void
```

注册上报执行动作的回调。使用callback异步回调。

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AVMusicTemplateController-onReportExecuteAction(callback: ReportExecuteActionEvent): void--><!--Device-AVMusicTemplateController-onReportExecuteAction(callback: ReportExecuteActionEvent): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [ReportExecuteActionEvent](arkts-avsession-avmusictemplate-reportexecuteactionevent-t.md) | Yes | 回调函数，上报对应按钮动作的事件。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 35000006 | AVMusicTemplateController does not exist. |
| 801 | capability not supported. |
| 35000012 | AVMusicTemplate error. |

## onSettingsChange

```TypeScript
onSettingsChange(callback: Callback<SettingItem[]>): void
```

注册上报设置改变的回调。使用callback异步回调。

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AVMusicTemplateController-onSettingsChange(callback: Callback<SettingItem[]>): void--><!--Device-AVMusicTemplateController-onSettingsChange(callback: Callback<SettingItem[]>): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;SettingItem[]&gt; | Yes | 回调函数，返回设置项数组。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 35000006 | AVMusicTemplateController does not exist. |
| 801 | capability not supported. |
| 35000012 | AVMusicTemplate error. |

## onTabContentChange

```TypeScript
onTabContentChange(callback: ReportTabContentEvent): void
```

注册标签页内容改变的回调。使用callback异步回调。

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AVMusicTemplateController-onTabContentChange(callback: ReportTabContentEvent): void--><!--Device-AVMusicTemplateController-onTabContentChange(callback: ReportTabContentEvent): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [ReportTabContentEvent](arkts-avsession-avmusictemplate-reporttabcontentevent-t.md) | Yes | 回调函数，上报标签页内容事件。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 35000006 | AVMusicTemplateController does not exist. |
| 801 | capability not supported. |
| 35000012 | AVMusicTemplate error. |

## onUserInfoChange

```TypeScript
onUserInfoChange(callback: Callback<UserInfo>): void
```

注册用户信息改变的回调。使用callback异步回调。

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AVMusicTemplateController-onUserInfoChange(callback: Callback<UserInfo>): void--><!--Device-AVMusicTemplateController-onUserInfoChange(callback: Callback<UserInfo>): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;UserInfo&gt; | Yes | 回调函数，参数为用户信息。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 35000006 | AVMusicTemplateController does not exist. |
| 801 | capability not supported. |
| 35000012 | AVMusicTemplate error. |

## playForSearch

```TypeScript
playForSearch(command: SearchPlayInfoType, args: SearchPlayInfo): Promise<OperResult>
```

搜播，支持音视频，示例仅以音频为例。使用Promise异步回调。

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AVMusicTemplateController-playForSearch(command: SearchPlayInfoType, args: SearchPlayInfo): Promise<OperResult>--><!--Device-AVMusicTemplateController-playForSearch(command: SearchPlayInfoType, args: SearchPlayInfo): Promise<OperResult>-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| command | [SearchPlayInfoType](arkts-avsession-avmusictemplate-searchplayinfotype-e.md) | Yes |  |
| args | [SearchPlayInfo](arkts-avsession-avmusictemplate-searchplayinfo-i.md) | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;OperResult&gt; | Promise对象，返回操作结果。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 35000006 | AVMusicTemplateController does not exist. |
| 801 | capability not supported. |
| 35000005 | AVMusicTemplate does not exist. |
| 35000003 | Template listener not registered. |

## playMediaEntity

```TypeScript
playMediaEntity(mediaEntity: MediaEntity): Promise<void>
```

播放媒体。使用Promise异步回调。

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AVMusicTemplateController-playMediaEntity(mediaEntity: MediaEntity): Promise<void>--><!--Device-AVMusicTemplateController-playMediaEntity(mediaEntity: MediaEntity): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| mediaEntity | [MediaEntity](arkts-avsession-avmusictemplate-mediaentity-i.md) | Yes | 包含标题、作者等元数据的媒体实体对象。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise对象，无返回结果。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 35000006 | AVMusicTemplateController does not exist. |
| 801 | capability not supported. |
| 35000005 | AVMusicTemplate does not exist. |
| 35000003 | Template listener not registered. |

## queryCompilation

ArkTS-Dyn:
```TypeScript
queryCompilation(compilationId: string, pageIndex: number): Promise<PageMediaEntity>
```

ArkTS-Sta:
```TypeScript
queryCompilation(compilationId: string, pageIndex: int): Promise<PageMediaEntity>
```

查询合集。使用Promise异步回调。

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AVMusicTemplateController-queryCompilation(compilationId: string, pageIndex: int): Promise<PageMediaEntity>--><!--Device-AVMusicTemplateController-queryCompilation(compilationId: string, pageIndex: int): Promise<PageMediaEntity>-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| compilationId | string | Yes | 合集的ID。 |
| pageIndex | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | 页索引。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;PageMediaEntity&gt; | Promise对象，返回查询的合集的分页对象。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 35000006 | AVMusicTemplateController does not exist. |
| 801 | capability not supported. |
| 35000005 | AVMusicTemplate does not exist. |
| 35000003 | Template listener not registered. |

## queryCompilationByKeyword

```TypeScript
queryCompilationByKeyword(keyword: string): Promise<Compilation[]>
```

按关键字查询合集。使用Promise异步回调。

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AVMusicTemplateController-queryCompilationByKeyword(keyword: string): Promise<Compilation[]>--><!--Device-AVMusicTemplateController-queryCompilationByKeyword(keyword: string): Promise<Compilation[]>-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| keyword | string | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;Compilation[]&gt; | Promise对象，返回合集数组。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 35000006 | AVMusicTemplateController does not exist. |
| 801 | capability not supported. |
| 35000005 | AVMusicTemplate does not exist. |
| 35000003 | Template listener not registered. |

## queryCurrentSingle

```TypeScript
queryCurrentSingle(): Promise<Single>
```

查询当前单曲。使用Promise异步回调。

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AVMusicTemplateController-queryCurrentSingle(): Promise<Single>--><!--Device-AVMusicTemplateController-queryCurrentSingle(): Promise<Single>-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;Single&gt; | Promise对象，返回当前单曲。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 35000006 | AVMusicTemplateController does not exist. |
| 801 | capability not supported. |
| 35000005 | AVMusicTemplate does not exist. |
| 35000003 | Template listener not registered. |

## queryCustomContent

```TypeScript
queryCustomContent(queryType: CustomType[]): Promise<CustomElement>
```

查询自定义内容。使用Promise异步回调。

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AVMusicTemplateController-queryCustomContent(queryType: CustomType[]): Promise<CustomElement>--><!--Device-AVMusicTemplateController-queryCustomContent(queryType: CustomType[]): Promise<CustomElement>-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| queryType | [CustomType](arkts-avsession-avmusictemplate-customtype-t.md)[] | Yes | 自定义类型数组。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;CustomElement&gt; | Promise对象，返回查询的自定义元素。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 35000006 | AVMusicTemplateController does not exist. |
| 801 | capability not supported. |
| 35000005 | AVMusicTemplate does not exist. |
| 35000003 | Template listener not registered. |

## queryHotWords

```TypeScript
queryHotWords(): Promise<string[]>
```

查询热词。使用Promise异步回调。

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AVMusicTemplateController-queryHotWords(): Promise<string[]>--><!--Device-AVMusicTemplateController-queryHotWords(): Promise<string[]>-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;string[]&gt; | Promise对象，返回热词数组。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 35000006 | AVMusicTemplateController does not exist. |
| 801 | capability not supported. |
| 35000005 | AVMusicTemplate does not exist. |
| 35000003 | Template listener not registered. |

## queryMainTabs

```TypeScript
queryMainTabs(): Promise<MediaTab[]>
```

查询主标签。使用Promise异步回调。

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AVMusicTemplateController-queryMainTabs(): Promise<MediaTab[]>--><!--Device-AVMusicTemplateController-queryMainTabs(): Promise<MediaTab[]>-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;MediaTab[]&gt; | Promise对象，返回查询的主标签页数组。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 35000006 | AVMusicTemplateController does not exist. |
| 801 | capability not supported. |
| 35000005 | AVMusicTemplate does not exist. |
| 35000003 | Template listener not registered. |

## queryMediaEntity

```TypeScript
queryMediaEntity(params: QueryMediaEntityParam): Promise<PageMediaEntity>
```

查询媒体实体。使用Promise异步回调。

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AVMusicTemplateController-queryMediaEntity(params: QueryMediaEntityParam): Promise<PageMediaEntity>--><!--Device-AVMusicTemplateController-queryMediaEntity(params: QueryMediaEntityParam): Promise<PageMediaEntity>-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| params | [QueryMediaEntityParam](arkts-avsession-avmusictemplate-querymediaentityparam-i.md) | Yes | 查询媒体实体参数。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;PageMediaEntity&gt; | Promise对象，返回查询的媒体实体分页对象。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 35000006 | AVMusicTemplateController does not exist. |
| 801 | capability not supported. |
| 35000005 | AVMusicTemplate does not exist. |
| 35000003 | Template listener not registered. |

## queryMediaEntityByKeyword

ArkTS-Dyn:
```TypeScript
queryMediaEntityByKeyword(keyword: string, searchType: EntityType, pageIndex: number): Promise<PageMediaEntity>
```

ArkTS-Sta:
```TypeScript
queryMediaEntityByKeyword(keyword: string, searchType: EntityType, pageIndex: int): Promise<PageMediaEntity>
```

按关键字查询媒体实体。使用Promise异步回调。

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AVMusicTemplateController-queryMediaEntityByKeyword(keyword: string, searchType: EntityType, pageIndex: int): Promise<PageMediaEntity>--><!--Device-AVMusicTemplateController-queryMediaEntityByKeyword(keyword: string, searchType: EntityType, pageIndex: int): Promise<PageMediaEntity>-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| keyword | string | Yes |  |
| searchType | [EntityType](arkts-avsession-avmusictemplate-entitytype-e.md) | Yes | 媒体资源类型。 |
| pageIndex | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | 页索引。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;PageMediaEntity&gt; | Promise对象，返回与该关键字相关的媒体实体分页对象。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 35000006 | AVMusicTemplateController does not exist. |
| 801 | capability not supported. |
| 35000005 | AVMusicTemplate does not exist. |
| 35000003 | Template listener not registered. |

## queryMediaTabContent

```TypeScript
queryMediaTabContent(tabId: string): Promise<MediaTabContent>
```

查询媒体标签内容。使用Promise异步回调。

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AVMusicTemplateController-queryMediaTabContent(tabId: string): Promise<MediaTabContent>--><!--Device-AVMusicTemplateController-queryMediaTabContent(tabId: string): Promise<MediaTabContent>-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| tabId | string | Yes | 标签页ID。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;MediaTabContent&gt; | Promise对象，返回媒体标签页内容。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 35000006 | AVMusicTemplateController does not exist. |
| 801 | capability not supported. |
| 35000005 | AVMusicTemplate does not exist. |
| 35000003 | Template listener not registered. |

## queryMemberPurchase

```TypeScript
queryMemberPurchase(memberPurchaseType: MemberPurchaseType): Promise<MemberPurchaseInfo[]>
```

查询购买会员的情况。使用Promise异步回调。

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AVMusicTemplateController-queryMemberPurchase(memberPurchaseType: MemberPurchaseType): Promise<MemberPurchaseInfo[]>--><!--Device-AVMusicTemplateController-queryMemberPurchase(memberPurchaseType: MemberPurchaseType): Promise<MemberPurchaseInfo[]>-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| memberPurchaseType | [MemberPurchaseType](arkts-avsession-avmusictemplate-memberpurchasetype-e.md) | Yes | 会员购买类型。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;MemberPurchaseInfo[]&gt; | Promise对象，返回购买会员信息的数组。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 35000006 | AVMusicTemplateController does not exist. |
| 801 | capability not supported. |
| 35000005 | AVMusicTemplate does not exist. |
| 35000003 | Template listener not registered. |

## queryPlaylist

ArkTS-Dyn:
```TypeScript
queryPlaylist(pageIndex: number, sort: Sort): Promise<PageMediaEntity>
```

ArkTS-Sta:
```TypeScript
queryPlaylist(pageIndex: int, sort: Sort): Promise<PageMediaEntity>
```

查询播放列表。使用Promise异步回调。

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AVMusicTemplateController-queryPlaylist(pageIndex: int, sort: Sort): Promise<PageMediaEntity>--><!--Device-AVMusicTemplateController-queryPlaylist(pageIndex: int, sort: Sort): Promise<PageMediaEntity>-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| pageIndex | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | 页索引。 |
| sort | [Sort](arkts-avsession-avmusictemplate-sort-e.md) | Yes | 查询到的播放列表数据的排序类型。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;PageMediaEntity&gt; | Promise对象，返回查询的播放列表的分页对象。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 35000006 | AVMusicTemplateController does not exist. |
| 801 | capability not supported. |
| 35000005 | AVMusicTemplate does not exist. |
| 35000003 | Template listener not registered. |

## queryRecommendMediaEntityList

```TypeScript
queryRecommendMediaEntityList(): Promise<MediaEntity[]>
```

查询推荐的媒体实体列表。使用Promise异步回调。

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AVMusicTemplateController-queryRecommendMediaEntityList(): Promise<MediaEntity[]>--><!--Device-AVMusicTemplateController-queryRecommendMediaEntityList(): Promise<MediaEntity[]>-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;MediaEntity[]&gt; | Promise对象，返回推荐的媒体实体数组。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 35000006 | AVMusicTemplateController does not exist. |
| 801 | capability not supported. |
| 35000005 | AVMusicTemplate does not exist. |
| 35000003 | Template listener not registered. |

## querySearchHistory

```TypeScript
querySearchHistory(): Promise<string[]>
```

查询搜索历史。使用Promise异步回调。

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AVMusicTemplateController-querySearchHistory(): Promise<string[]>--><!--Device-AVMusicTemplateController-querySearchHistory(): Promise<string[]>-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;string[]&gt; | Promise对象，返回历史搜索词数组。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 35000006 | AVMusicTemplateController does not exist. |
| 801 | capability not supported. |
| 35000005 | AVMusicTemplate does not exist. |
| 35000003 | Template listener not registered. |

## reportProblemAndAdvice

```TypeScript
reportProblemAndAdvice(advice: string): Promise<OperResult>
```

报告问题和建议。使用Promise异步回调。

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AVMusicTemplateController-reportProblemAndAdvice(advice: string): Promise<OperResult>--><!--Device-AVMusicTemplateController-reportProblemAndAdvice(advice: string): Promise<OperResult>-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| advice | string | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;OperResult&gt; | Promise对象，返回报告问题和建议的操作结果。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 35000006 | AVMusicTemplateController does not exist. |
| 801 | capability not supported. |
| 35000005 | AVMusicTemplate does not exist. |
| 35000003 | Template listener not registered. |

## requestDialogInfo

```TypeScript
requestDialogInfo(actionType: DialogActionType, actionInfo?: DialogActionInfo): Promise<DialogInfo>
```

请求对话框信息。使用Promise异步回调。

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AVMusicTemplateController-requestDialogInfo(actionType: DialogActionType, actionInfo?: DialogActionInfo): Promise<DialogInfo>--><!--Device-AVMusicTemplateController-requestDialogInfo(actionType: DialogActionType, actionInfo?: DialogActionInfo): Promise<DialogInfo>-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| actionType | [DialogActionType](arkts-avsession-avmusictemplate-dialogactiontype-t.md) | Yes | 对话框操作类型。 |
| actionInfo | [DialogActionInfo](arkts-avsession-avmusictemplate-dialogactioninfo-i.md) | No | 对话框操作的信息。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;DialogInfo&gt; | Promise对象，返回对话框信息。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 35000006 | AVMusicTemplateController does not exist. |
| 801 | capability not supported. |
| 35000005 | AVMusicTemplate does not exist. |
| 35000003 | Template listener not registered. |

## updateSettings

```TypeScript
updateSettings(settingItem: SettingItem): Promise<SettingItem>
```

更新设置信息。使用Promise异步回调。

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AVMusicTemplateController-updateSettings(settingItem: SettingItem): Promise<SettingItem>--><!--Device-AVMusicTemplateController-updateSettings(settingItem: SettingItem): Promise<SettingItem>-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| settingItem | [SettingItem](arkts-avsession-avmusictemplate-settingitem-i.md) | Yes | 待更新的设置项。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;SettingItem&gt; | Promise对象，返回更新后的设置项。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 35000006 | AVMusicTemplateController does not exist. |
| 801 | capability not supported. |
| 35000005 | AVMusicTemplate does not exist. |
| 35000003 | Template listener not registered. |

## isDestroy

```TypeScript
isDestroy: boolean
```

音频模板控制器是否销毁。true表示已经销毁，false表示没有销毁。无默认值。

**Type:** boolean

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AVMusicTemplateController-isDestroy: boolean--><!--Device-AVMusicTemplateController-isDestroy: boolean-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVMusicTemplate

## sessionId

```TypeScript
sessionId: string
```

音频模板控制器唯一的标识。

**Type:** string

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AVMusicTemplateController-sessionId: string--><!--Device-AVMusicTemplateController-sessionId: string-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVMusicTemplate

