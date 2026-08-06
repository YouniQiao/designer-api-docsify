# LoginEvent

```TypeScript
type LoginEvent = (controlType: LoginType, id?: string) => Promise<QrCodeInfo[]>
```

The login event.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-avMusicTemplate-type LoginEvent = (controlType: LoginType, id?: string) => Promise<QrCodeInfo[]>--><!--Device-avMusicTemplate-type LoginEvent = (controlType: LoginType, id?: string) => Promise<QrCodeInfo[]>-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| controlType | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | control type  |
| id | string | No | id  |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;QrCodeInfo[]&gt; | (QrCodeInfo[]) returned through promise  |

