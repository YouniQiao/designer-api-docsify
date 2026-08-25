# @ohos.multimodalAwareness.metadataBinding(记忆链接)

本模块提供记忆链接能力调用，用于向图片加入和解析元数据信息，实现信息传递，包括编码内容传递、订阅事件和取消订阅事件。记忆链接允许系统应用获取第三方应用的编码内容， <br>支持实时事件监听和回调机制，适用于需要在图片中存储和传递元数据的场景，可用于防伪、版权保护等场景，为开发者提供灵活的信息嵌入和解析机制。

**起始版本：** 18

**ArkTS模式：** ArkTS-Dyn起始版本为18；ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.MultimodalAwareness.MetadataBinding

## 导入模块

```TypeScript
import { metadataBinding } from '@kit.MultimodalAwarenessKit';
```

## 汇总

### 函数

| 名称 |
| --- |
| [off(记忆链接)](arkts-multimodalawareness-metadatabinding-off-f.md#offoperationsubmitmetadata) |
| [offOperationSubmitMetadata(记忆链接)](arkts-multimodalawareness-metadatabinding-offoperationsubmitmetadata-f.md) |
| [on(记忆链接)](arkts-multimodalawareness-metadatabinding-on-f.md#onoperationsubmitmetadata) |
| [onOperationSubmitMetadata(记忆链接)](arkts-multimodalawareness-metadatabinding-onoperationsubmitmetadata-f.md) |
| [submitMetadata(记忆链接)](arkts-multimodalawareness-metadatabinding-submitmetadata-f.md) |

<!--Del-->
### 函数（系统接口）

| 名称 |
| --- |
| [decodeImage(记忆链接)](arkts-multimodalawareness-metadatabinding-decodeimage-f-sys.md) |
| [encodeImage(记忆链接)](arkts-multimodalawareness-metadatabinding-encodeimage-f-sys.md) |
| [notifyMetadataBindingEvent(记忆链接)](arkts-multimodalawareness-metadatabinding-notifymetadatabindingevent-f-sys.md) |
<!--DelEnd-->
