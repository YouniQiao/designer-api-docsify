# LoginEvent

```TypeScript
type LoginEvent = (controlType: LoginType, id?: string) => Promise<QrCodeInfo[]>
```

登录事件。使用Promise异步回调。

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-avMusicTemplate-type LoginEvent = (controlType: LoginType, id?: string) => Promise<QrCodeInfo[]>--><!--Device-avMusicTemplate-type LoginEvent = (controlType: LoginType, id?: string) => Promise<QrCodeInfo[]>-End-->

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

