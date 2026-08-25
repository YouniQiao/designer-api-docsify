# writeNdefTag

## 导入模块

```TypeScript
import { connectedTag } from 'kits/@kit.ConnectivityKit';
```

## writeNdefTag

```TypeScript
function writeNdefTag(data: string): Promise<void>
```

写入内容到有源标签。使用Promise异步回调。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [write](arkts-connectivity-connectedtag-write-f.md)

**需要权限：** ohos.permission.NFC_TAG

**系统能力：** SystemCapability.Communication.ConnectedTag

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| data | string | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |


## writeNdefTag

```TypeScript
function writeNdefTag(data: string, callback: AsyncCallback<void>): void
```

写入内容到有源标签，使用AsyncCallback方式作为异步方法。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [write](arkts-connectivity-connectedtag-write-f.md)

**需要权限：** ohos.permission.NFC_TAG

**系统能力：** SystemCapability.Communication.ConnectedTag

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| data | string | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |
