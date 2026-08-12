# off

## off('operationSubmitMetadata')

```TypeScript
function off(type: 'operationSubmitMetadata', bundleName: string, callback?: Callback<int>): void
```

取消订阅系统获取编码内容的事件。

**起始版本：** 18

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为18。

**原子化服务API：** 从API版本18开始，该接口支持在原子化服务API中使用。

<!--Device-metadataBinding-function off(type: 'operationSubmitMetadata', bundleName: string, callback?: Callback<int>): void--><!--Device-metadataBinding-function off(type: 'operationSubmitMetadata', bundleName: string, callback?: Callback<int>): void-End-->

**系统能力：** SystemCapability.MultimodalAwareness.MetadataBinding

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | 'operationSubmitMetadata' | 是 | 事件类型，type为'operationSubmitMetadata'，表示系统应用获取编码内容。 |
| bundleName | string | 是 | 应用包名，标识注册应用的包名，需与订阅时传入的包名一致。 |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;int&gt; | 否 | 回调函数，返回编码结果。需要取消监听的回调函数，需与订阅时传入的回调函数一致。建议在订阅时保存回调函数引用，在取消订阅时使用同一引用。若不填，则取消当前监 听该事件的所有回调函数。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [32100001](../../../../../../../../gitee_tmp/docs/stamaster/zh-cn/application-dev/reference/apis-multimodalawareness-kit/errorcode-metadataBinding.md#32100001-文件创建失败) | Internal handling failed. |
| [32100005](../../../../../../../../gitee_tmp/docs/stamaster/zh-cn/application-dev/reference/apis-multimodalawareness-kit/errorcode-metadataBinding.md#32100005-取消订阅失败) | Unsubscribe Failed. Possible causes: &lt;br&gt; 1. Abnormal system capability. &lt;br&gt; 2. IPC communication abnormality. |

## 示例

```TypeScript
import { metadataBinding } from '@kit.MultimodalAwarenessKit';

let bundleName: string = '';
try {
  metadataBinding.off('operationSubmitMetadata', bundleName, (event: number) => {
  });
} catch (error) {
  console.error("unsubscript screenshot event" + error);
}
```

