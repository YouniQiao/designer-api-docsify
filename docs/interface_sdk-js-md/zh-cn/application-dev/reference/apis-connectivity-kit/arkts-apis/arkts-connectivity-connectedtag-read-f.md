# read

## 导入模块

```TypeScript
import { connectedTag } from 'kits/@kit.ConnectivityKit';
```

## read

```TypeScript
function read(): Promise<number[]>
```

读取有源标签内容。使用Promise异步回调。

**起始版本：** 9

**需要权限：** ohos.permission.NFC_TAG

**系统能力：** SystemCapability.Communication.ConnectedTag

**返回值：**

| 类型 |
| --- |
| Promise & lt;number[] & gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [3200101](../errorcode-nfc.md#3200101-有源nfc标签状态异常) |


## read

```TypeScript
function read(callback: AsyncCallback<number[]>): void
```

读取有源标签内容，使用AsyncCallback方式作为异步方法。

**起始版本：** 9

**需要权限：** ohos.permission.NFC_TAG

**系统能力：** SystemCapability.Communication.ConnectedTag

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;number[]&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [3200101](../errorcode-nfc.md#3200101-有源nfc标签状态异常) |
