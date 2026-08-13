# onAVMusicTemplateDestroy（系统接口）

## onAVMusicTemplateDestroy

```TypeScript
function onAVMusicTemplateDestroy(callback: Callback<AVMusicTemplateDescriptor>): void
```

注册音频模板销毁监听。使用callback异步回调。

**起始版本：** 23

**废弃版本：** -1

**需要权限：** ohos.permission.MANAGE_MEDIA_RESOURCES

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-avMusicTemplate-function onAVMusicTemplateDestroy(callback: Callback<AVMusicTemplateDescriptor>): void--><!--Device-avMusicTemplate-function onAVMusicTemplateDestroy(callback: Callback<AVMusicTemplateDescriptor>): void-End-->

**系统能力：** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[AVMusicTemplateDescriptor](arkts-avsession-avmusictemplate-avmusictemplatedescriptor-i-sys.md)&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
