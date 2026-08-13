# LoginEvent

```TypeScript
type LoginEvent = (controlType: LoginType, id?: string) => Promise<QrCodeInfo[]>
```

The login event.

**Since:** 23

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-avMusicTemplate-type LoginEvent = (controlType: LoginType, id?: string) => Promise<QrCodeInfo[]>--><!--Device-avMusicTemplate-type LoginEvent = (controlType: LoginType, id?: string) => Promise<QrCodeInfo[]>-End-->

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
