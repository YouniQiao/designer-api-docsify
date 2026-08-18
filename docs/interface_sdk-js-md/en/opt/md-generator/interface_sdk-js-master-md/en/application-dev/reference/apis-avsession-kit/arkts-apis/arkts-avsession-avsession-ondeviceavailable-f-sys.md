# onDeviceAvailable (System API)

## Modules to Import

```TypeScript
```

## onDeviceAvailable

```TypeScript
function onDeviceAvailable(callback: Callback<OutputDeviceInfo>): void
```

Register device discovery callback

**Since:** 23

<!--Device-avSession-function onDeviceAvailable(callback: Callback<OutputDeviceInfo>): void--><!--Device-avSession-function onDeviceAvailable(callback: Callback<OutputDeviceInfo>): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVCast

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[OutputDeviceInfo](arkts-avsession-avsession-outputdeviceinfo-i.md)&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
