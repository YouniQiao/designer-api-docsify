# offOperationSubmitMetadata

## 导入模块

```TypeScript
import { metadataBinding } from '@kit.MultimodalAwarenessKit';
```

## offOperationSubmitMetadata

```TypeScript
function offOperationSubmitMetadata(bundleName: string, callback?: Callback<int>): void
```

取消订阅系统获取编码内容的事件。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.MultimodalAwareness.MetadataBinding

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| bundleName | string | 是 |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;int&gt; | 否 |

**错误码：**

| 错误码ID |
| --- |
| [32100001](../errorcode-metadataBinding.md#32100001-文件创建失败) |
| [32100005](../errorcode-metadataBinding.md#32100005-取消订阅失败) |

**示例**

```TypeScript
import { metadataBinding } from '@kit.MultimodalAwarenessKit';
import { BusinessError } from '@kit.BasicServicesKit';

let bundleName: string = '';
try {
  metadataBinding.offOperationSubmitMetadata(bundleName, (event: int)=>{});
} catch (error) {
  console.error("Unsubscribe screenshot event" + error);
}
```
