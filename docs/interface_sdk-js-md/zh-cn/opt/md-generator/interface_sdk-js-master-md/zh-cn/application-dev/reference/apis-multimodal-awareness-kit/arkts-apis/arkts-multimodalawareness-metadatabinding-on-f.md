# on

## on('operationSubmitMetadata')

```TypeScript
function on(type: 'operationSubmitMetadata', bundleName: string, callback: Callback<number>): void
```

订阅系统获取编码内容的事件。应用注册回调，事件发生时通过回调通知应用。调用on()方法订阅事件后，必须在不再需要监听事件时调用off()方法取消订阅，释放监听资源。

**起始版本：** 18

**原子化服务API：** 从API版本18开始，该接口支持在原子化服务API中使用。

<!--Device-metadataBinding-function on(type: 'operationSubmitMetadata', bundleName: string, callback: Callback<int>): void--><!--Device-metadataBinding-function on(type: 'operationSubmitMetadata', bundleName: string, callback: Callback<int>): void-End-->

**系统能力：** SystemCapability.MultimodalAwareness.MetadataBinding

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'operationSubmitMetadata' | 是 |
| bundleName | string | 是 |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;number&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [32100001](../../apis-multimodalawareness-kit/errorcode-metadataBinding.md#32100001-文件创建失败) |
| [32100004](../../apis-multimodalawareness-kit/errorcode-metadataBinding.md#32100004-订阅失败) |

## 示例

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { metadataBinding } from '@kit.MultimodalAwarenessKit';

let bundleName: string = '';
try {
  metadataBinding.on('operationSubmitMetadata', bundleName, (event: number) => {
    if (event == 1) {
      console.info("The screenshot request is received and the app link is obtained");
    }
  });
} catch (error) {
  const err = error as BusinessError;
  console.error(`Failed to register operationSubmitMetadata event. Code: ${err.code}, message: ${err.message}`);
}
```
