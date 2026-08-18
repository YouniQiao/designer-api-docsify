# onOperationSubmitMetadata

## Modules to Import

```TypeScript
```

## onOperationSubmitMetadata

```TypeScript
function onOperationSubmitMetadata(bundleName: string, callback: Callback<number>): void
```

Subscribes to a system event to obtain the encoded metadata.

**Since:** 23

<!--Device-metadataBinding-function onOperationSubmitMetadata(bundleName: string, callback: Callback<int>): void--><!--Device-metadataBinding-function onOperationSubmitMetadata(bundleName: string, callback: Callback<int>): void-End-->

**System capability:** SystemCapability.MultimodalAwareness.MetadataBinding

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| bundleName | string | Yes |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;number&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [32100001](../../apis-multimodalawareness-kit/errorcode-metadataBinding.md#32100001-file-creation-failed) |
| [32100004](../../apis-multimodalawareness-kit/errorcode-metadataBinding.md#32100004-subscription-failed) |
