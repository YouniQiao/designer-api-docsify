# readNdefTag

## 导入模块

```TypeScript
import { connectedTag } from 'kits/@kit.ConnectivityKit';
```

## readNdefTag

```TypeScript
function readNdefTag(): Promise<string>
```

读取有源标签内容。使用Promise异步回调。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [read](arkts-connectivity-connectedtag-read-f.md)

**需要权限：** ohos.permission.NFC_TAG

**系统能力：** SystemCapability.Communication.ConnectedTag

**返回值：**

| 类型 |
| --- |
| Promise & lt;string & gt; |


## readNdefTag

```TypeScript
function readNdefTag(callback: AsyncCallback<string>): void
```

读取有源标签内容，使用AsyncCallback方式作为异步方法。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [read](arkts-connectivity-connectedtag-read-f.md)

**需要权限：** ohos.permission.NFC_TAG

**系统能力：** SystemCapability.Communication.ConnectedTag

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;string&gt; | 是 |
