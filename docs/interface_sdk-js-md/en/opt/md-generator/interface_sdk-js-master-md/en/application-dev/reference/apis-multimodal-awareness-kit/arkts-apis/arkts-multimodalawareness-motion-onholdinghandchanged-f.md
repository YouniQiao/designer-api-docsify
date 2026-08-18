# onHoldingHandChanged

## Modules to Import

```TypeScript
```

## onHoldingHandChanged

```TypeScript
function onHoldingHandChanged(callback: Callback<HoldingHandStatus>): void
```

Subscribe to detect the holding hand changed event.

**Since:** 23

**Required permissions:** ohos.permission.DETECT_GESTURE

<!--Device-motion-function onHoldingHandChanged(callback: Callback<HoldingHandStatus>): void--><!--Device-motion-function onHoldingHandChanged(callback: Callback<HoldingHandStatus>): void-End-->

**System capability:** SystemCapability.MultimodalAwareness.Motion

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[HoldingHandStatus](arkts-multimodalawareness-motion-holdinghandstatus-e.md)&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [31500001](../../apis-multimodalawareness-kit/errorcode-motion.md#31500001-service-exception) |
| [31500002](../../apis-multimodalawareness-kit/errorcode-motion.md#31500002-subscription-failed) |
| [201](../../errorcode-universal.md#201-permission-denied) |
