# submitMetadata

## submitMetadata

```TypeScript
function submitMetadata(metadata: string): void
```

第三方应用将需要编码的内容传递给接口服务，接口服务将内容传递给调用编码接口的系统应用或服务。

**起始版本：** 18

**原子化服务API：** 从API版本18开始，该接口支持在原子化服务API中使用。

<!--Device-metadataBinding-function submitMetadata(metadata: string): void--><!--Device-metadataBinding-function submitMetadata(metadata: string): void-End-->

**系统能力：** SystemCapability.MultimodalAwareness.MetadataBinding

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| metadata | string | 是 |

**错误码：**

| 错误码ID |
| --- |
| [32100001](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-multimodalawareness-kit/errorcode-metadataBinding.md#32100001-文件创建失败) |

## 示例

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { metadataBinding } from '@kit.MultimodalAwarenessKit';

let metadata: string = "";
try {
  metadataBinding.submitMetadata(metadata);
} catch (error) {
  const err: BusinessError = error as BusinessError;
  console.error(`Failed to submit metadata. Code: ${err.code}, message: ${err.message}`);
}
```
