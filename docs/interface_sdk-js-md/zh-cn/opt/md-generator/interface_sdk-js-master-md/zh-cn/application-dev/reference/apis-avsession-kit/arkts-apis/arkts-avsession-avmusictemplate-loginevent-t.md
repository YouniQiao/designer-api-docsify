# LoginEvent

```TypeScript
type LoginEvent = (controlType: LoginType, id?: string) => Promise<QrCodeInfo[]>
```

登录事件。使用Promise异步回调。

**起始版本：** 23

**废弃版本：** -1

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-avMusicTemplate-type LoginEvent = (controlType: LoginType, id?: string) => Promise<QrCodeInfo[]>--><!--Device-avMusicTemplate-type LoginEvent = (controlType: LoginType, id?: string) => Promise<QrCodeInfo[]>-End-->

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
