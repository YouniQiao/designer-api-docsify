# @ohos.multimodalAwareness.metadataBinding

The **metadataBinding** module provides metadata binding–specific functions such as metadata transfer, event subscription, and event unsubscription.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-unnamed-declare namespace metadataBinding--><!--Device-unnamed-declare namespace metadataBinding-End-->

**System capability:** SystemCapability.MultimodalAwareness.MetadataBinding

## Modules to Import

```TypeScript
import { metadataBinding } from '@kit.MultimodalAwarenessKit';
```

## Summary

### Functions

| Name | Description |
| --- | --- |
| [offOperationSubmitMetadata](arkts-multimodalawareness-metadatabinding-offoperationsubmitmetadata-f.md#offOperationSubmitMetadata) | Unsubscribes from system events that are used to obtain the encoded metadata. |
| off_operationSubmitMetadata | Unsubscribes from system events that are used to obtain the encoded metadata. The respective callback will be unregistered. |
| [onOperationSubmitMetadata](arkts-multimodalawareness-metadatabinding-onoperationsubmitmetadata-f.md#onOperationSubmitMetadata) | Subscribes to a system event to obtain the encoded metadata. |
| on_operationSubmitMetadata | Subscribes to a system event to obtain the encoded metadata. The application needs to register a callback to return the encoded metadata when the registered system event occurs. |
| [submitMetadata](arkts-multimodalawareness-metadatabinding-submitmetadata-f.md#submitMetadata) | Transfers the metadata to be encoded to the MSDP. The MSDP determines whether to transfer the metadata to the system application or service that calls the encoding API. |

<!--Del-->
### Functions（系统接口）

| Name | Description |
| --- | --- |
| [decodeImage](arkts-multimodalawareness-metadatabinding-decodeimage-f-sys.md#decodeImage) | Decodes the information carried in the image. This API uses a promise to return the result. |
| [encodeImage](arkts-multimodalawareness-metadatabinding-encodeimage-f-sys.md#encodeImage) | Encodes metadata into an image. This API uses a promise to return the result. |
| [notifyMetadataBindingEvent](arkts-multimodalawareness-metadatabinding-notifymetadatabindingevent-f-sys.md#notifyMetadataBindingEvent) | Transfers metadata to the application or service that calls the encoding API. This API uses a promise to return the result. |
<!--DelEnd-->

