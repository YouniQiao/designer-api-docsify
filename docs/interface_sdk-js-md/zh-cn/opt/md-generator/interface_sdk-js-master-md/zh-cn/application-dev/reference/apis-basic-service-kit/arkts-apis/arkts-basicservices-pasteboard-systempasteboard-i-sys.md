# SystemPasteboard

系统剪贴板对象。 在调用SystemPasteboard的接口前，需要先通过[getSystemPasteboard](arkts-basicservices-pasteboard-getsystempasteboard-f.md#getSystemPasteboard)获取系统剪贴板。

**起始版本：** 23

**废弃版本：** -1

<!--Device-pasteboard-interface SystemPasteboard--><!--Device-pasteboard-interface SystemPasteboard-End-->

**系统能力：** SystemCapability.MiscServices.Pasteboard

## removeAppShareOptions

```TypeScript
removeAppShareOptions(): void
```

删除应用全局的可粘贴的范围。适用于应用需要取消之前设置的粘贴范围限制，恢复剪贴板数据默认粘贴范围的场景。 - 与setAppShareOptions()方法（应用设置本应用剪贴板数据的可粘贴范围）配合使用。 - 删除的是通过setAppShareOptions()设置的分享范围。 - 必须在已设置分享范围的情况下才能调用。

**起始版本：** 23

**废弃版本：** -1

**需要权限：** 
- API版本14+：ohos.permission.MANAGE_PASTEBOARD_APP_SHARE_OPTION

<!--Device-SystemPasteboard-removeAppShareOptions(): void--><!--Device-SystemPasteboard-removeAppShareOptions(): void-End-->

**系统能力：** SystemCapability.MiscServices.Pasteboard

**系统接口：** 此接口为系统接口。

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

## 示例

```TypeScript
const systemPasteboard: pasteboard.SystemPasteboard = pasteboard.getSystemPasteboard();
try {
  systemPasteboard.removeAppShareOptions();
  console.info('Remove app share options success.');
} catch (error) {
  console.error(`Remove app share options failed, errorCode: ${error.code}, errorMessage: ${error.message}.`);
}
```

## setAppShareOptions

```TypeScript
setAppShareOptions(shareOptions: ShareOption): void
```

应用设置本应用剪贴板数据的可粘贴范围。适用于应用需要全局限制本应用产生的剪贴板数据的粘贴范围，如金融类应用需要保护用户敏感信息的场景。 - 与removeAppShareOptions()方法（删除应用全局的可粘贴的范围）配合使用。 - 需要删除已设置的分享范围时，调用removeAppShareOptions()。 - 在何处设置就在何处删除，确保分享范围设置和删除的一致性。

**起始版本：** 23

**废弃版本：** -1

**需要权限：** 
- API版本14+：ohos.permission.MANAGE_PASTEBOARD_APP_SHARE_OPTION

<!--Device-SystemPasteboard-setAppShareOptions(shareOptions: ShareOption): void--><!--Device-SystemPasteboard-setAppShareOptions(shareOptions: ShareOption): void-End-->

**系统能力：** SystemCapability.MiscServices.Pasteboard

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [shareOptions](../../apis-arkdata/arkts-apis/arkts-arkdata-unifieddatachannel-unifieddataproperties-c.md) | [ShareOption](arkts-basicservices-pasteboard-shareoption-e.md) | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [12900006](../../apis-basic-services-kit/errorcode-pasteboard.md#12900006-设置已存在) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

## 示例

```TypeScript
const systemPasteboard: pasteboard.SystemPasteboard = pasteboard.getSystemPasteboard();
try {
  systemPasteboard.setAppShareOptions(pasteboard.ShareOption.INAPP);
  console.info('Set app share options success.');
} catch (error) {
  console.error(`Set app share options failed, errorCode: ${error.code}, errorMessage: ${error.message}.`);
}
```
