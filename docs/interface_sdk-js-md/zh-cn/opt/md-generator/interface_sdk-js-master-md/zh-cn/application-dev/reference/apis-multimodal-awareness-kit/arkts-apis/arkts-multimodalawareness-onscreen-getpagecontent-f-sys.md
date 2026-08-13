# getPageContent（系统接口）

## getPageContent

```TypeScript
function getPageContent(options?: ContentOptions): Promise<PageContent>
```

在需要抓取内容的窗口在桌面上时，调用该接口以获取屏上内容。

**起始版本：** 23

**废弃版本：** -1

**需要权限：** ohos.permission.GET_SCREEN_CONTENT

<!--Device-onScreen-function getPageContent(options?: ContentOptions): Promise<PageContent>--><!--Device-onScreen-function getPageContent(options?: ContentOptions): Promise<PageContent>-End-->

**系统能力：** SystemCapability.MultimodalAwareness.OnScreenAwareness

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| options | [ContentOptions](arkts-multimodalawareness-onscreen-contentoptions-i-sys.md) | 否 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;[PageContent](arkts-multimodalawareness-onscreen-pagecontent-i-sys.md)&gt; |

**错误码：**

| 错误码ID |
| --- |
| [34000006](../../apis-multimodalawareness-kit/errorcode-onScreen.md#34000006-请求超时) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [34000004](../../apis-multimodalawareness-kit/errorcode-onScreen.md#34000004-页面未准备就绪) |
| [34000002](../../apis-multimodalawareness-kit/errorcode-onScreen.md#34000002-应用或页面不支持) |
| [34000003](../../apis-multimodalawareness-kit/errorcode-onScreen.md#34000003-窗口id无效) |
| [34000001](../../apis-multimodalawareness-kit/errorcode-onScreen.md#34000001-服务异常) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
