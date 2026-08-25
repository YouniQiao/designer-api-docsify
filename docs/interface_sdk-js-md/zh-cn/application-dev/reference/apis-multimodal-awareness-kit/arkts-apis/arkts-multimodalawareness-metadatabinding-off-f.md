# off

## 导入模块

```TypeScript
import { metadataBinding } from 'kits/@kit.MultimodalAwarenessKit';
```

## off('operationSubmitMetadata')

```TypeScript
function off(type: 'operationSubmitMetadata', bundleName: string, callback?: Callback<number>): void
```

取消订阅系统获取编码内容的事件。需先调用on('operationSubmitMetadata')方法订阅事件，未订阅时调用不产生效果。取消订阅后，应用将不再接收编码内容传递事件。

**起始版本：** 18

**原子化服务API：** 从API版本18开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.MultimodalAwareness.MetadataBinding

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'operationSubmitMetadata' | 是 |
| bundleName | string | 是 |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;number&gt; | 否 |

**错误码：**

| 错误码ID |
| --- |
| [32100001](../errorcode-metadataBinding.md#32100001-文件创建失败) |
| [32100005](../errorcode-metadataBinding.md#32100005-取消订阅失败) |
