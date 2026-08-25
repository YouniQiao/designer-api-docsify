# submitMetadata

## 导入模块

```TypeScript
import { metadataBinding } from 'kits/@kit.MultimodalAwarenessKit';
```

## submitMetadata

```TypeScript
function submitMetadata(metadata: string): void
```

第三方应用将需要编码的内容传递给接口服务，接口服务将内容传递给调用编码接口的系统应用或服务。本接口由第三方应用调用，供系统应用订阅获取数据。 系统应用需先通过on('operationSubmitMetadata')方法订阅事件，才能接收到编码内容。

**起始版本：** 18

**原子化服务API：** 从API版本18开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.MultimodalAwareness.MetadataBinding

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| metadata | string | 是 |

**错误码：**

| 错误码ID |
| --- |
| [32100001](../errorcode-metadataBinding.md#32100001-文件创建失败) |
