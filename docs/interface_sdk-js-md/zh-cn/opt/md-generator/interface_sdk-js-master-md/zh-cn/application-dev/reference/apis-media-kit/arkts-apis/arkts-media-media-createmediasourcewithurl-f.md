# createMediaSourceWithUrl

## createMediaSourceWithUrl

```TypeScript
function createMediaSourceWithUrl(url: string, headers?: Record<string, string>): MediaSource
```

创建流媒体预下载媒体来源实例方法。

**起始版本：** 12

**原子化服务API：** 从API版本13开始，该接口支持在原子化服务API中使用。

<!--Device-media-function createMediaSourceWithUrl(url: string, headers?: Record<string, string>): MediaSource--><!--Device-media-function createMediaSourceWithUrl(url: string, headers?: Record<string, string>): MediaSource-End-->

**系统能力：** SystemCapability.Multimedia.Media.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| url | string | 是 |
| headers | Record & lt;string, string & gt; | 否 |

**返回值：**

| 类型 |
| --- |
| [MediaSource](arkts-media-multimedia-media-mediasource-i.md) |

**错误码：**

| 错误码ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-contacts-kit/errorcode-contacts.md#401-打开联系人头像文件失败) |
| [5400101](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-media-kit/errorcode-media.md#5400101-内存分配失败) |
