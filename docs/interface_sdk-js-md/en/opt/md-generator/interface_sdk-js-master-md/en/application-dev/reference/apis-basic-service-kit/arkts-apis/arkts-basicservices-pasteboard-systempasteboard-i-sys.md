# SystemPasteboard

Provides **SystemPasteboard** APIs. Before calling any **SystemPasteboard** API, you must obtain a **SystemPasteboard** object using [getSystemPasteboard](arkts-basicservices-pasteboard-getsystempasteboard-f.md#getsystempasteboard).

**Since:** 23

<!--Device-pasteboard-interface SystemPasteboard--><!--Device-pasteboard-interface SystemPasteboard-End-->

**System capability:** SystemCapability.MiscServices.Pasteboard

## Modules to Import

```TypeScript
```

## removeAppShareOptions

```TypeScript
removeAppShareOptions(): void
```

Deletes the global pasteable range of the application.

**Since:** 23

**Required permissions:** 
- API version 14+: ohos.permission.MANAGE_PASTEBOARD_APP_SHARE_OPTION

<!--Device-SystemPasteboard-removeAppShareOptions(): void--><!--Device-SystemPasteboard-removeAppShareOptions(): void-End-->

**System capability:** SystemCapability.MiscServices.Pasteboard

**System API:** This is a system API.

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

**Examples**

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

Sets pasteable range of PasteData for application.

**Since:** 23

**Required permissions:** 
- API version 14+: ohos.permission.MANAGE_PASTEBOARD_APP_SHARE_OPTION

<!--Device-SystemPasteboard-setAppShareOptions(shareOptions: ShareOption): void--><!--Device-SystemPasteboard-setAppShareOptions(shareOptions: ShareOption): void-End-->

**System capability:** SystemCapability.MiscServices.Pasteboard

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [shareOptions](../../apis-arkdata/arkts-apis/arkts-arkdata-unifieddatachannel-unifieddataproperties-c.md) | [ShareOption](arkts-basicservices-pasteboard-shareoption-e.md) | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [12900006](../../apis-basic-services-kit/errorcode-pasteboard.md#12900006-settings-already-exists) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

**Examples**

```TypeScript
const systemPasteboard: pasteboard.SystemPasteboard = pasteboard.getSystemPasteboard();
try {
  systemPasteboard.setAppShareOptions(pasteboard.ShareOption.INAPP);
  console.info('Set app share options success.');
} catch (error) {
  console.error(`Set app share options failed, errorCode: ${error.code}, errorMessage: ${error.message}.`);
}
```
