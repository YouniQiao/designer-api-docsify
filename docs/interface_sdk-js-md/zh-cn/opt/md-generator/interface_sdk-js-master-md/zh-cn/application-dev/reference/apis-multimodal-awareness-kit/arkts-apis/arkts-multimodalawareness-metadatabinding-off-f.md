# off

## off('operationSubmitMetadata')

```TypeScript
function off(type: 'operationSubmitMetadata', bundleName: string, callback?: Callback<number>): void
```

取消订阅系统获取编码内容的事件。

**起始版本：** 18

**原子化服务API：** 从API版本18开始，该接口支持在原子化服务API中使用。

<!--Device-metadataBinding-function off(type: 'operationSubmitMetadata', bundleName: string, callback?: Callback<int>): void--><!--Device-metadataBinding-function off(type: 'operationSubmitMetadata', bundleName: string, callback?: Callback<int>): void-End-->

**系统能力：** SystemCapability.MultimodalAwareness.MetadataBinding

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'operationSubmitMetadata' | 是 |
| bundleName | string | 是 |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;number&gt; | 否 |

**错误码：**

| 错误码ID |
| --- |
| [32100001](../../apis-multimodalawareness-kit/errorcode-metadataBinding.md#32100001-文件创建失败) |
| [32100005](../../apis-multimodalawareness-kit/errorcode-metadataBinding.md#32100005-取消订阅失败) |

## 示例

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { metadataBinding } from '@kit.MultimodalAwarenessKit';

let bundleName: string = '';
try {
  metadataBinding.off('operationSubmitMetadata', bundleName);
} catch (error) {
 const err = error as BusinessError;
 console.error(`Failed to unsubscribe operationSubmitMetadata event. Code: ${err.code}, message: ${err.message}`);
}
```
