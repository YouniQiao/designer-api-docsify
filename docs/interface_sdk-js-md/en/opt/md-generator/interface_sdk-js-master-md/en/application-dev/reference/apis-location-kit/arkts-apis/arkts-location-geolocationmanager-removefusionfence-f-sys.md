# removeFusionFence (System API)

## Modules to Import

```TypeScript
```

## removeFusionFence

```TypeScript
function removeFusionFence(identifier: string): Promise<void>
```

Remove a fusion fence.

**Since:** 26.1.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-geoLocationManager-function removeFusionFence(identifier: string): Promise<void>--><!--Device-geoLocationManager-function removeFusionFence(identifier: string): Promise<void>-End-->

**System capability:** SystemCapability.Location.Location.Geofence

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| identifier | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [3301602](../errorcode-geoLocationManager.md#3301602-failed-to-delete-a-geofence-due-to-an-incorrect-id) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [3301000](../errorcode-geoLocationManager.md#3301000-location-service-unavailable) |
