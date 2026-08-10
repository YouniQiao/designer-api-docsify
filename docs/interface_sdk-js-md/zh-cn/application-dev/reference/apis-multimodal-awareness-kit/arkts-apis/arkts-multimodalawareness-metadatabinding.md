# @ohos.multimodalAwareness.metadataBinding

The **metadataBinding** module provides metadata binding–specific functions such as metadata transfer, event subscription, and event unsubscription.

**起始版本：** 18

**ArkTS模式：** ArkTS-Dyn起始版本为18；ArkTS-Sta起始版本为23。

<!--Device-unnamed-declare namespace metadataBinding--><!--Device-unnamed-declare namespace metadataBinding-End-->

**系统能力：** SystemCapability.MultimodalAwareness.MetadataBinding

## 导入模块

```TypeScript
import { metadataBinding } from 'kits/@kit.MultimodalAwarenessKit';
```

## 汇总

### 函数

| 名称 | 说明 |
| --- | --- |
| [off](arkts-multimodalawareness-metadatabinding-off-f.md#off) | Unsubscribes from system events that are used to obtain the encoded metadata. The respective callback will be unregistered. |
| [offOperationSubmitMetadata](arkts-multimodalawareness-metadatabinding-offoperationsubmitmetadata-f.md#offoperationsubmitmetadata) | Unsubscribes from system events that are used to obtain the encoded metadata. |
| [on](arkts-multimodalawareness-metadatabinding-on-f.md#on) | Subscribes to a system event to obtain the encoded metadata. The application needs to register a callback to return the encoded metadata when the registered system event occurs. |
| [onOperationSubmitMetadata](arkts-multimodalawareness-metadatabinding-onoperationsubmitmetadata-f.md#onoperationsubmitmetadata) | Subscribes to a system event to obtain the encoded metadata. |
| [submitMetadata](arkts-multimodalawareness-metadatabinding-submitmetadata-f.md#submitmetadata) | Transfers the metadata to be encoded to the MSDP. The MSDP determines whether to transfer the metadata to the system application or service that calls the encoding API. |

<!--Del-->
### 函数（系统接口）

| 名称 | 说明 |
| --- | --- |
| [decodeImage](arkts-multimodalawareness-metadatabinding-decodeimage-f-sys.md#decodeimage) | Decodes the information carried in the image. This API uses a promise to return the result. |
| [encodeImage](arkts-multimodalawareness-metadatabinding-encodeimage-f-sys.md#encodeimage) | Encodes metadata into an image. This API uses a promise to return the result. |
| [notifyMetadataBindingEvent](arkts-multimodalawareness-metadatabinding-notifymetadatabindingevent-f-sys.md#notifymetadatabindingevent) | Transfers metadata to the application or service that calls the encoding API. This API uses a promise to return the result. |
<!--DelEnd-->

