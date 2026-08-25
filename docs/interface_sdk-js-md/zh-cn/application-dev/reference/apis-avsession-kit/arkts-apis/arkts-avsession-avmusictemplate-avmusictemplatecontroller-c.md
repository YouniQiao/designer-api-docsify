# AVMusicTemplateController

音频模板控制器，可以获得音频模板控制器唯一的标识，用于与接入音频模板的媒体应用数据交互。

> **说明：**&gt;
> - 本模块仅适用于API version 23及以上版本的Car设备。

**起始版本：** 23

**系统能力：** SystemCapability.Multimedia.AVSession.AVMusicTemplate

## 导入模块

```TypeScript
import { avMusicTemplate } from 'kits/@kit.AVSessionKit';
```

## clearSearchHistory

```TypeScript
clearSearchHistory(): Promise<OperResult>
```

清除搜索历史。使用Promise异步回调。

**起始版本：** 23

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**返回值：**

| 类型 |
| --- |
| Promise&lt;[OperResult](arkts-avsession-avmusictemplate-operresult-i.md)&gt; |

**错误码：**

| 错误码ID |
| --- |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [35000003](../errorcode-avmusictemplate.md#35000003-模板监听未注册) |
| [35000005](../errorcode-avmusictemplate.md#35000005-音频模板不存在) |
| [35000006](../errorcode-avmusictemplate.md#35000006-模板控制器不存在) |

## destroy

```TypeScript
destroy(): Promise<void>
```

销毁音频模板控制器。使用Promise异步回调。

**起始版本：** 23

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |

## downloadMediaEntity

```TypeScript
downloadMediaEntity(controlType: DownloadControlType, mediaEntity: MediaEntity): Promise<OperResult>
```

下载媒体实体。使用Promise异步回调。

**起始版本：** 23

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| controlType | [DownloadControlType](arkts-avsession-avmusictemplate-downloadcontroltype-t.md) | 是 |
| mediaEntity | [MediaEntity](arkts-avsession-avmusictemplate-mediaentity-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;[OperResult](arkts-avsession-avmusictemplate-operresult-i.md)&gt; |

**错误码：**

| 错误码ID |
| --- |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [35000003](../errorcode-avmusictemplate.md#35000003-模板监听未注册) |
| [35000005](../errorcode-avmusictemplate.md#35000005-音频模板不存在) |
| [35000006](../errorcode-avmusictemplate.md#35000006-模板控制器不存在) |

## executeAction

```TypeScript
executeAction(actionType: string, params: string): Promise<string>
```

执行动作。使用Promise异步回调。

**起始版本：** 23

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| actionType | string | 是 |
| params | string | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;string & gt; |

**错误码：**

| 错误码ID |
| --- |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [35000003](../errorcode-avmusictemplate.md#35000003-模板监听未注册) |
| [35000005](../errorcode-avmusictemplate.md#35000005-音频模板不存在) |
| [35000006](../errorcode-avmusictemplate.md#35000006-模板控制器不存在) |

## favoriteMediaEntity

```TypeScript
favoriteMediaEntity(actionType: MediaFavoriteType, mediaEntity: MediaEntity): Promise<OperResult>
```

收藏媒体。使用Promise异步回调。

**起始版本：** 23

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| actionType | [MediaFavoriteType](arkts-avsession-avmusictemplate-mediafavoritetype-t.md) | 是 |
| mediaEntity | [MediaEntity](arkts-avsession-avmusictemplate-mediaentity-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;[OperResult](arkts-avsession-avmusictemplate-operresult-i.md)&gt; |

**错误码：**

| 错误码ID |
| --- |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [35000003](../errorcode-avmusictemplate.md#35000003-模板监听未注册) |
| [35000005](../errorcode-avmusictemplate.md#35000005-音频模板不存在) |
| [35000006](../errorcode-avmusictemplate.md#35000006-模板控制器不存在) |

## handleMemberPurchase

```TypeScript
handleMemberPurchase(info: MemberPurchaseInfo): Promise<DialogInfo>
```

处理购买会员情况。使用Promise异步回调。

**起始版本：** 23

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| info | [MemberPurchaseInfo](arkts-avsession-avmusictemplate-memberpurchaseinfo-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;[DialogInfo](arkts-avsession-avmusictemplate-dialoginfo-i.md)&gt; |

**错误码：**

| 错误码ID |
| --- |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [35000003](../errorcode-avmusictemplate.md#35000003-模板监听未注册) |
| [35000005](../errorcode-avmusictemplate.md#35000005-音频模板不存在) |
| [35000006](../errorcode-avmusictemplate.md#35000006-模板控制器不存在) |

## login

```TypeScript
login(controlType: LoginType, id?: string): Promise<QrCodeInfo[]>
```

登录。使用Promise异步回调。

**起始版本：** 23

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| controlType | [LoginType](arkts-avsession-avmusictemplate-logintype-t.md) | 是 |
| id | string | 否 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;[QrCodeInfo](arkts-avsession-avmusictemplate-qrcodeinfo-i.md)[]&gt; |

**错误码：**

| 错误码ID |
| --- |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [35000003](../errorcode-avmusictemplate.md#35000003-模板监听未注册) |
| [35000005](../errorcode-avmusictemplate.md#35000005-音频模板不存在) |
| [35000006](../errorcode-avmusictemplate.md#35000006-模板控制器不存在) |

## offCurrentSingleChange

```TypeScript
offCurrentSingleChange(callback?: Callback<Single>): void
```

注销当前单曲改变的回调。使用callback异步回调。

**起始版本：** 23

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;Single&gt; | 否 |

**错误码：**

| 错误码ID |
| --- |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [35000006](../errorcode-avmusictemplate.md#35000006-模板控制器不存在) |
| [35000012](../errorcode-avmusictemplate.md#35000012-音频模板错误) |

## offCustomElementsChange

```TypeScript
offCustomElementsChange(callback?: ReportCustomElementsChangeEvent): void
```

注销上报自定义元素改变的回调。

**起始版本：** 23

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [ReportCustomElementsChangeEvent](arkts-avsession-avmusictemplate-reportcustomelementschangeevent-t.md) | 否 |

**错误码：**

| 错误码ID |
| --- |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [35000006](../errorcode-avmusictemplate.md#35000006-模板控制器不存在) |
| [35000012](../errorcode-avmusictemplate.md#35000012-音频模板错误) |

## offDialogCommandChange

```TypeScript
offDialogCommandChange(callback?: ReportDialogCommandEvent): void
```

注销对话框命令改变的回调。

**起始版本：** 23

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [ReportDialogCommandEvent](arkts-avsession-avmusictemplate-reportdialogcommandevent-t.md) | 否 |

**错误码：**

| 错误码ID |
| --- |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [35000006](../errorcode-avmusictemplate.md#35000006-模板控制器不存在) |
| [35000012](../errorcode-avmusictemplate.md#35000012-音频模板错误) |

## offDownloadMediaEntityStatusChange

```TypeScript
offDownloadMediaEntityStatusChange(callback?: Callback<MediaEntity>): void
```

注销上报下载媒体状态改变的回调。使用callback异步回调。

**起始版本：** 23

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[MediaEntity](arkts-avsession-avmusictemplate-mediaentity-i.md)&gt; | 否 |

**错误码：**

| 错误码ID |
| --- |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [35000006](../errorcode-avmusictemplate.md#35000006-模板控制器不存在) |
| [35000012](../errorcode-avmusictemplate.md#35000012-音频模板错误) |

## offExtensionAbilityChange

```TypeScript
offExtensionAbilityChange(callback?: ReportExecuteAbilityEvent): void
```

注销回调，用于停止监听拉起指定媒体应用的请求。

**起始版本：** 23

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [ReportExecuteAbilityEvent](arkts-avsession-avmusictemplate-reportexecuteabilityevent-t.md) | 否 |

**错误码：**

| 错误码ID |
| --- |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [35000006](../errorcode-avmusictemplate.md#35000006-模板控制器不存在) |
| [35000012](../errorcode-avmusictemplate.md#35000012-音频模板错误) |

## offMediaEntitiesChange

```TypeScript
offMediaEntitiesChange(callback?: Callback<MediaEntity[]>): void
```

注销媒体实体改变的回调。使用callback异步回调。

**起始版本：** 23

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[MediaEntity](arkts-avsession-avmusictemplate-mediaentity-i.md)[]&gt; | 否 |

**错误码：**

| 错误码ID |
| --- |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [35000006](../errorcode-avmusictemplate.md#35000006-模板控制器不存在) |
| [35000012](../errorcode-avmusictemplate.md#35000012-音频模板错误) |

## offPlaylistChange

```TypeScript
offPlaylistChange(callback?: Callback<PageMediaEntity>): void
```

注销上报播放列表改变的回调。使用callback异步回调。

**起始版本：** 23

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[PageMediaEntity](arkts-avsession-avmusictemplate-pagemediaentity-i.md)&gt; | 否 |

**错误码：**

| 错误码ID |
| --- |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [35000006](../errorcode-avmusictemplate.md#35000006-模板控制器不存在) |
| [35000012](../errorcode-avmusictemplate.md#35000012-音频模板错误) |

## offReportExecuteAction

```TypeScript
offReportExecuteAction(callback?: ReportExecuteActionEvent): void
```

注销上报执行动作的回调。

**起始版本：** 23

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [ReportExecuteActionEvent](arkts-avsession-avmusictemplate-reportexecuteactionevent-t.md) | 否 |

**错误码：**

| 错误码ID |
| --- |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [35000006](../errorcode-avmusictemplate.md#35000006-模板控制器不存在) |
| [35000012](../errorcode-avmusictemplate.md#35000012-音频模板错误) |

## offSettingsChange

```TypeScript
offSettingsChange(callback?: Callback<SettingItem[]>): void
```

注销上报设置改变的回调。使用callback异步回调。

**起始版本：** 23

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[SettingItem](arkts-avsession-avmusictemplate-settingitem-i.md)[]&gt; | 否 |

**错误码：**

| 错误码ID |
| --- |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [35000006](../errorcode-avmusictemplate.md#35000006-模板控制器不存在) |
| [35000012](../errorcode-avmusictemplate.md#35000012-音频模板错误) |

## offTabContentChange

```TypeScript
offTabContentChange(callback?: ReportTabContentEvent): void
```

注销标签页内容改变的回调。

**起始版本：** 23

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [ReportTabContentEvent](arkts-avsession-avmusictemplate-reporttabcontentevent-t.md) | 否 |

**错误码：**

| 错误码ID |
| --- |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [35000006](../errorcode-avmusictemplate.md#35000006-模板控制器不存在) |
| [35000012](../errorcode-avmusictemplate.md#35000012-音频模板错误) |

## offUserInfoChange

```TypeScript
offUserInfoChange(callback?: Callback<UserInfo>): void
```

注销用户信息改变的回调。使用callback异步回调。

**起始版本：** 23

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;UserInfo&gt; | 否 |

**错误码：**

| 错误码ID |
| --- |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [35000006](../errorcode-avmusictemplate.md#35000006-模板控制器不存在) |
| [35000012](../errorcode-avmusictemplate.md#35000012-音频模板错误) |

## onCurrentSingleChange

```TypeScript
onCurrentSingleChange(callback: Callback<Single>): void
```

注册当前单曲改变的回调。使用callback异步回调。

**起始版本：** 23

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;Single&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [35000006](../errorcode-avmusictemplate.md#35000006-模板控制器不存在) |
| [35000012](../errorcode-avmusictemplate.md#35000012-音频模板错误) |

## onCustomElementsChange

```TypeScript
onCustomElementsChange(callback: ReportCustomElementsChangeEvent): void
```

注册上报自定义元素改变的回调。使用callback异步回调。

**起始版本：** 23

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [ReportCustomElementsChangeEvent](arkts-avsession-avmusictemplate-reportcustomelementschangeevent-t.md) | 是 |

**错误码：**

| 错误码ID |
| --- |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [35000006](../errorcode-avmusictemplate.md#35000006-模板控制器不存在) |
| [35000012](../errorcode-avmusictemplate.md#35000012-音频模板错误) |

## onDialogCommandChange

```TypeScript
onDialogCommandChange(callback: ReportDialogCommandEvent): void
```

注册对话框命令改变的回调。使用callback异步回调。

**起始版本：** 23

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [ReportDialogCommandEvent](arkts-avsession-avmusictemplate-reportdialogcommandevent-t.md) | 是 |

**错误码：**

| 错误码ID |
| --- |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [35000006](../errorcode-avmusictemplate.md#35000006-模板控制器不存在) |
| [35000012](../errorcode-avmusictemplate.md#35000012-音频模板错误) |

## onDownloadMediaEntityStatusChange

```TypeScript
onDownloadMediaEntityStatusChange(callback: Callback<MediaEntity>): void
```

注册上报下载媒体状态改变的回调。使用callback异步回调。

**起始版本：** 23

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[MediaEntity](arkts-avsession-avmusictemplate-mediaentity-i.md)&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [35000006](../errorcode-avmusictemplate.md#35000006-模板控制器不存在) |
| [35000012](../errorcode-avmusictemplate.md#35000012-音频模板错误) |

## onExtensionAbilityChange

```TypeScript
onExtensionAbilityChange(callback: ReportExecuteAbilityEvent): void
```

注册回调，当需要拉起指定媒体应用界面时触发。使用callback异步回调。

**起始版本：** 23

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [ReportExecuteAbilityEvent](arkts-avsession-avmusictemplate-reportexecuteabilityevent-t.md) | 是 |

**错误码：**

| 错误码ID |
| --- |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [35000006](../errorcode-avmusictemplate.md#35000006-模板控制器不存在) |
| [35000012](../errorcode-avmusictemplate.md#35000012-音频模板错误) |

## onMediaEntitiesChange

```TypeScript
onMediaEntitiesChange(callback: Callback<MediaEntity[]>): void
```

注册媒体实体改变的回调。使用callback异步回调。

**起始版本：** 23

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[MediaEntity](arkts-avsession-avmusictemplate-mediaentity-i.md)[]&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [35000006](../errorcode-avmusictemplate.md#35000006-模板控制器不存在) |
| [35000012](../errorcode-avmusictemplate.md#35000012-音频模板错误) |

## onPlaylistChange

```TypeScript
onPlaylistChange(callback: Callback<PageMediaEntity>): void
```

注册上报播放列表改变的回调。使用callback异步回调。

**起始版本：** 23

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[PageMediaEntity](arkts-avsession-avmusictemplate-pagemediaentity-i.md)&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [35000006](../errorcode-avmusictemplate.md#35000006-模板控制器不存在) |
| [35000012](../errorcode-avmusictemplate.md#35000012-音频模板错误) |

## onReportExecuteAction

```TypeScript
onReportExecuteAction(callback: ReportExecuteActionEvent): void
```

注册上报执行动作的回调。使用callback异步回调。

**起始版本：** 23

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [ReportExecuteActionEvent](arkts-avsession-avmusictemplate-reportexecuteactionevent-t.md) | 是 |

**错误码：**

| 错误码ID |
| --- |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [35000006](../errorcode-avmusictemplate.md#35000006-模板控制器不存在) |
| [35000012](../errorcode-avmusictemplate.md#35000012-音频模板错误) |

## onSettingsChange

```TypeScript
onSettingsChange(callback: Callback<SettingItem[]>): void
```

注册上报设置改变的回调。使用callback异步回调。

**起始版本：** 23

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[SettingItem](arkts-avsession-avmusictemplate-settingitem-i.md)[]&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [35000006](../errorcode-avmusictemplate.md#35000006-模板控制器不存在) |
| [35000012](../errorcode-avmusictemplate.md#35000012-音频模板错误) |

## onTabContentChange

```TypeScript
onTabContentChange(callback: ReportTabContentEvent): void
```

注册标签页内容改变的回调。使用callback异步回调。

**起始版本：** 23

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [ReportTabContentEvent](arkts-avsession-avmusictemplate-reporttabcontentevent-t.md) | 是 |

**错误码：**

| 错误码ID |
| --- |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [35000006](../errorcode-avmusictemplate.md#35000006-模板控制器不存在) |
| [35000012](../errorcode-avmusictemplate.md#35000012-音频模板错误) |

## onUserInfoChange

```TypeScript
onUserInfoChange(callback: Callback<UserInfo>): void
```

注册用户信息改变的回调。使用callback异步回调。

**起始版本：** 23

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;UserInfo&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [35000006](../errorcode-avmusictemplate.md#35000006-模板控制器不存在) |
| [35000012](../errorcode-avmusictemplate.md#35000012-音频模板错误) |

## playForSearch

```TypeScript
playForSearch(command: SearchPlayInfoType, args: SearchPlayInfo): Promise<OperResult>
```

搜播，支持音视频，示例仅以音频为例。使用Promise异步回调。

**起始版本：** 23

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| command | [SearchPlayInfoType](arkts-avsession-avmusictemplate-searchplayinfotype-e.md) | 是 |
| [args](../../apis-arkdata/arkts-apis/arkts-arkdata-relationalstore-sqlinfo-i.md) | [SearchPlayInfo](arkts-avsession-avmusictemplate-searchplayinfo-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;[OperResult](arkts-avsession-avmusictemplate-operresult-i.md)&gt; |

**错误码：**

| 错误码ID |
| --- |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [35000003](../errorcode-avmusictemplate.md#35000003-模板监听未注册) |
| [35000005](../errorcode-avmusictemplate.md#35000005-音频模板不存在) |
| [35000006](../errorcode-avmusictemplate.md#35000006-模板控制器不存在) |

## playMediaEntity

```TypeScript
playMediaEntity(mediaEntity: MediaEntity): Promise<void>
```

播放媒体。使用Promise异步回调。

**起始版本：** 23

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| mediaEntity | [MediaEntity](arkts-avsession-avmusictemplate-mediaentity-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [35000003](../errorcode-avmusictemplate.md#35000003-模板监听未注册) |
| [35000005](../errorcode-avmusictemplate.md#35000005-音频模板不存在) |
| [35000006](../errorcode-avmusictemplate.md#35000006-模板控制器不存在) |

## queryCompilation

```TypeScript
queryCompilation(compilationId: string, pageIndex: number): Promise<PageMediaEntity>
```

查询合集。使用Promise异步回调。

**起始版本：** 23

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| compilationId | string | 是 |
| pageIndex | number | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;[PageMediaEntity](arkts-avsession-avmusictemplate-pagemediaentity-i.md)&gt; |

**错误码：**

| 错误码ID |
| --- |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [35000003](../errorcode-avmusictemplate.md#35000003-模板监听未注册) |
| [35000005](../errorcode-avmusictemplate.md#35000005-音频模板不存在) |
| [35000006](../errorcode-avmusictemplate.md#35000006-模板控制器不存在) |

## queryCompilationByKeyword

```TypeScript
queryCompilationByKeyword(keyword: string): Promise<Compilation[]>
```

按关键字查询合集。使用Promise异步回调。

**起始版本：** 23

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| keyword | string | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;[Compilation](arkts-avsession-avmusictemplate-compilation-i.md)[]&gt; |

**错误码：**

| 错误码ID |
| --- |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [35000003](../errorcode-avmusictemplate.md#35000003-模板监听未注册) |
| [35000005](../errorcode-avmusictemplate.md#35000005-音频模板不存在) |
| [35000006](../errorcode-avmusictemplate.md#35000006-模板控制器不存在) |

## queryCurrentSingle

```TypeScript
queryCurrentSingle(): Promise<Single>
```

查询当前单曲。使用Promise异步回调。

**起始版本：** 23

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**返回值：**

| 类型 |
| --- |
| Promise & lt;Single & gt; |

**错误码：**

| 错误码ID |
| --- |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [35000003](../errorcode-avmusictemplate.md#35000003-模板监听未注册) |
| [35000005](../errorcode-avmusictemplate.md#35000005-音频模板不存在) |
| [35000006](../errorcode-avmusictemplate.md#35000006-模板控制器不存在) |

## queryCustomContent

```TypeScript
queryCustomContent(queryType: CustomType[]): Promise<CustomElement>
```

查询自定义内容。使用Promise异步回调。

**起始版本：** 23

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [queryType](../../apis-ability-kit/arkts-apis/arkts-ability-insightintent-queryentityparam-i.md) | [CustomType](arkts-avsession-avmusictemplate-customtype-t.md)[] | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;[CustomElement](arkts-avsession-avmusictemplate-customelement-i.md)&gt; |

**错误码：**

| 错误码ID |
| --- |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [35000003](../errorcode-avmusictemplate.md#35000003-模板监听未注册) |
| [35000005](../errorcode-avmusictemplate.md#35000005-音频模板不存在) |
| [35000006](../errorcode-avmusictemplate.md#35000006-模板控制器不存在) |

## queryHotWords

```TypeScript
queryHotWords(): Promise<string[]>
```

查询热词。使用Promise异步回调。

**起始版本：** 23

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**返回值：**

| 类型 |
| --- |
| Promise & lt;string[] & gt; |

**错误码：**

| 错误码ID |
| --- |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [35000003](../errorcode-avmusictemplate.md#35000003-模板监听未注册) |
| [35000005](../errorcode-avmusictemplate.md#35000005-音频模板不存在) |
| [35000006](../errorcode-avmusictemplate.md#35000006-模板控制器不存在) |

## queryMainTabs

```TypeScript
queryMainTabs(): Promise<MediaTab[]>
```

查询主标签。使用Promise异步回调。

**起始版本：** 23

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**返回值：**

| 类型 |
| --- |
| Promise&lt;[MediaTab](arkts-avsession-avmusictemplate-mediatab-i.md)[]&gt; |

**错误码：**

| 错误码ID |
| --- |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [35000003](../errorcode-avmusictemplate.md#35000003-模板监听未注册) |
| [35000005](../errorcode-avmusictemplate.md#35000005-音频模板不存在) |
| [35000006](../errorcode-avmusictemplate.md#35000006-模板控制器不存在) |

## queryMediaEntity

```TypeScript
queryMediaEntity(params: QueryMediaEntityParam): Promise<PageMediaEntity>
```

查询媒体实体。使用Promise异步回调。

**起始版本：** 23

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| params | [QueryMediaEntityParam](arkts-avsession-avmusictemplate-querymediaentityparam-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;[PageMediaEntity](arkts-avsession-avmusictemplate-pagemediaentity-i.md)&gt; |

**错误码：**

| 错误码ID |
| --- |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [35000003](../errorcode-avmusictemplate.md#35000003-模板监听未注册) |
| [35000005](../errorcode-avmusictemplate.md#35000005-音频模板不存在) |
| [35000006](../errorcode-avmusictemplate.md#35000006-模板控制器不存在) |

## queryMediaEntityByKeyword

```TypeScript
queryMediaEntityByKeyword(keyword: string, searchType: EntityType, pageIndex: number): Promise<PageMediaEntity>
```

按关键字查询媒体实体。使用Promise异步回调。

**起始版本：** 23

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| keyword | string | 是 |
| searchType | [EntityType](arkts-avsession-avmusictemplate-entitytype-e.md) | 是 |
| pageIndex | number | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;[PageMediaEntity](arkts-avsession-avmusictemplate-pagemediaentity-i.md)&gt; |

**错误码：**

| 错误码ID |
| --- |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [35000003](../errorcode-avmusictemplate.md#35000003-模板监听未注册) |
| [35000005](../errorcode-avmusictemplate.md#35000005-音频模板不存在) |
| [35000006](../errorcode-avmusictemplate.md#35000006-模板控制器不存在) |

## queryMediaTabContent

```TypeScript
queryMediaTabContent(tabId: string): Promise<MediaTabContent>
```

查询媒体标签内容。使用Promise异步回调。

**起始版本：** 23

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| tabId | string | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;[MediaTabContent](arkts-avsession-avmusictemplate-mediatabcontent-i.md)&gt; |

**错误码：**

| 错误码ID |
| --- |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [35000003](../errorcode-avmusictemplate.md#35000003-模板监听未注册) |
| [35000005](../errorcode-avmusictemplate.md#35000005-音频模板不存在) |
| [35000006](../errorcode-avmusictemplate.md#35000006-模板控制器不存在) |

## queryMemberPurchase

```TypeScript
queryMemberPurchase(memberPurchaseType: MemberPurchaseType): Promise<MemberPurchaseInfo[]>
```

查询购买会员的情况。使用Promise异步回调。

**起始版本：** 23

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [memberPurchaseType](arkts-avsession-avmusictemplate-memberpurchaseinfo-i.md) | [MemberPurchaseType](arkts-avsession-avmusictemplate-memberpurchasetype-e.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;[MemberPurchaseInfo](arkts-avsession-avmusictemplate-memberpurchaseinfo-i.md)[]&gt; |

**错误码：**

| 错误码ID |
| --- |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [35000003](../errorcode-avmusictemplate.md#35000003-模板监听未注册) |
| [35000005](../errorcode-avmusictemplate.md#35000005-音频模板不存在) |
| [35000006](../errorcode-avmusictemplate.md#35000006-模板控制器不存在) |

## queryPlaylist

```TypeScript
queryPlaylist(pageIndex: number, sort: Sort): Promise<PageMediaEntity>
```

查询播放列表。使用Promise异步回调。

**起始版本：** 23

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| pageIndex | number | 是 |
| sort | [Sort](arkts-avsession-avmusictemplate-sort-e.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;[PageMediaEntity](arkts-avsession-avmusictemplate-pagemediaentity-i.md)&gt; |

**错误码：**

| 错误码ID |
| --- |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [35000003](../errorcode-avmusictemplate.md#35000003-模板监听未注册) |
| [35000005](../errorcode-avmusictemplate.md#35000005-音频模板不存在) |
| [35000006](../errorcode-avmusictemplate.md#35000006-模板控制器不存在) |

## queryRecommendMediaEntityList

```TypeScript
queryRecommendMediaEntityList(): Promise<MediaEntity[]>
```

查询推荐的媒体实体列表。使用Promise异步回调。

**起始版本：** 23

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**返回值：**

| 类型 |
| --- |
| Promise&lt;[MediaEntity](arkts-avsession-avmusictemplate-mediaentity-i.md)[]&gt; |

**错误码：**

| 错误码ID |
| --- |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [35000003](../errorcode-avmusictemplate.md#35000003-模板监听未注册) |
| [35000005](../errorcode-avmusictemplate.md#35000005-音频模板不存在) |
| [35000006](../errorcode-avmusictemplate.md#35000006-模板控制器不存在) |

## querySearchHistory

```TypeScript
querySearchHistory(): Promise<string[]>
```

查询搜索历史。使用Promise异步回调。

**起始版本：** 23

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**返回值：**

| 类型 |
| --- |
| Promise & lt;string[] & gt; |

**错误码：**

| 错误码ID |
| --- |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [35000003](../errorcode-avmusictemplate.md#35000003-模板监听未注册) |
| [35000005](../errorcode-avmusictemplate.md#35000005-音频模板不存在) |
| [35000006](../errorcode-avmusictemplate.md#35000006-模板控制器不存在) |

## reportProblemAndAdvice

```TypeScript
reportProblemAndAdvice(advice: string): Promise<OperResult>
```

报告问题和建议。使用Promise异步回调。

**起始版本：** 23

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| advice | string | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;[OperResult](arkts-avsession-avmusictemplate-operresult-i.md)&gt; |

**错误码：**

| 错误码ID |
| --- |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [35000003](../errorcode-avmusictemplate.md#35000003-模板监听未注册) |
| [35000005](../errorcode-avmusictemplate.md#35000005-音频模板不存在) |
| [35000006](../errorcode-avmusictemplate.md#35000006-模板控制器不存在) |

## requestDialogInfo

```TypeScript
requestDialogInfo(actionType: DialogActionType, actionInfo?: DialogActionInfo): Promise<DialogInfo>
```

请求对话框信息。使用Promise异步回调。

**起始版本：** 23

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| actionType | [DialogActionType](arkts-avsession-avmusictemplate-dialogactiontype-t.md) | 是 |
| actionInfo | [DialogActionInfo](arkts-avsession-avmusictemplate-dialogactioninfo-i.md) | 否 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;[DialogInfo](arkts-avsession-avmusictemplate-dialoginfo-i.md)&gt; |

**错误码：**

| 错误码ID |
| --- |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [35000003](../errorcode-avmusictemplate.md#35000003-模板监听未注册) |
| [35000005](../errorcode-avmusictemplate.md#35000005-音频模板不存在) |
| [35000006](../errorcode-avmusictemplate.md#35000006-模板控制器不存在) |

## updateSettings

```TypeScript
updateSettings(settingItem: SettingItem): Promise<SettingItem>
```

更新设置信息。使用Promise异步回调。

**起始版本：** 23

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| settingItem | [SettingItem](arkts-avsession-avmusictemplate-settingitem-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;[SettingItem](arkts-avsession-avmusictemplate-settingitem-i.md)&gt; |

**错误码：**

| 错误码ID |
| --- |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [35000003](../errorcode-avmusictemplate.md#35000003-模板监听未注册) |
| [35000005](../errorcode-avmusictemplate.md#35000005-音频模板不存在) |
| [35000006](../errorcode-avmusictemplate.md#35000006-模板控制器不存在) |

## isDestroy

```TypeScript
isDestroy: boolean
```

音频模板控制器是否销毁。true表示已经销毁，false表示没有销毁。无默认值。

**类型：** boolean

**起始版本：** 23

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Multimedia.AVSession.AVMusicTemplate

## sessionId

```TypeScript
sessionId: string
```

音频模板控制器唯一的标识。

**类型：** string

**起始版本：** 23

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Multimedia.AVSession.AVMusicTemplate
