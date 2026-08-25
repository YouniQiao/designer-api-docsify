# getPageContent（系统接口）

## 导入模块

```TypeScript
import { onScreen } from 'kits/@kit.MultimodalAwarenessKit';
```

## getPageContent

```TypeScript
function getPageContent(options?: ContentOptions): Promise<PageContent>
```

在需要抓取内容的窗口在桌面上时，调用该接口以获取屏上内容。

**起始版本：** 20

**需要权限：** ohos.permission.GET_SCREEN_CONTENT

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
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [34000001](../errorcode-carAwareness.md#34000001-服务异常) |
| [34000002](../errorcode-carAwareness.md#34000002-指定能力不支持) |
| [34000003](../errorcode-onScreen.md#34000003-窗口id无效) |
| [34000004](../errorcode-onScreen.md#34000004-页面未准备就绪) |
| [34000006](../errorcode-onScreen.md#34000006-请求超时) |
