# on

## on('operationSubmitMetadata')

```TypeScript
function on(type: 'operationSubmitMetadata', bundleName: string, callback: Callback<int>): void
```

订阅系统获取编码内容的事件。应用注册回调，事件发生时通过回调通知应用。调用on()方法订阅事件后，必须在不再需要监听事件时调用off()方法取消订阅，释放监听资源。

**起始版本：** 18

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为18。

**原子化服务API：** 从API版本18开始，该接口支持在原子化服务API中使用。

<!--Device-metadataBinding-function on(type: 'operationSubmitMetadata', bundleName: string, callback: Callback<int>): void--><!--Device-metadataBinding-function on(type: 'operationSubmitMetadata', bundleName: string, callback: Callback<int>): void-End-->

**系统能力：** SystemCapability.MultimodalAwareness.MetadataBinding

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | 'operationSubmitMetadata' | 是 | 事件类型，type为'operationSubmitMetadata'，表示系统应用获取编码内容。 |
| bundleName | string | 是 | 应用包名，用于标识注册订阅事件的第三方应用。在事件发生时，系统将通过此包名识别并通知对应的注册应用。需确保传入的包名为有效的应用包名。 |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;int&gt; | 是 | 回调函数，用于返回事件编码。当事件值为1时表示截图事件。注意：回调函数应快速执行，避免阻塞UI线程。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [32100001](../../apis-multimodalawareness-kit/errorcode-metadataBinding.md#32100001-文件创建失败) | Internal handling failed. |
| [32100004](../../apis-multimodalawareness-kit/errorcode-metadataBinding.md#32100004-订阅失败) | Subscribe Failed. Possible causes: &lt;br&gt;1. Abnormal system capability. &lt;br&gt;2. IPC communication abnormality. &lt;br&gt;3. Algorithm loading exception. |

## 示例

```TypeScript
import { metadataBinding } from '@kit.MultimodalAwarenessKit';

let bundleName: string = '';
try {
  metadataBinding.on('operationSubmitMetadata', bundleName, (event: number) => {
    if (event == 1) {
      console.info("The screenshot request is intercepted and the app link is obtained");
    }
  });
} catch (error) {
  console.error("register screenshot event error");
}
```

