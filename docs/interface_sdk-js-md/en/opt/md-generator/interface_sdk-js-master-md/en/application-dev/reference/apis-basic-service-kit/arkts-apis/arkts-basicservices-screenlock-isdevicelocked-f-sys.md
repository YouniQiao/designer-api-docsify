# isDeviceLocked (System API)

## Modules to Import

```TypeScript
```

## isDeviceLocked

```TypeScript
function isDeviceLocked(userId: number): boolean
```

Check whether the device is currently locked and the screenlock requires an identity to authenticate and unlock.

**Since:** 23

<!--Device-screenLock-function isDeviceLocked(userId: int): boolean--><!--Device-screenLock-function isDeviceLocked(userId: int): boolean-End-->

**System capability:** SystemCapability.MiscServices.ScreenLock

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| userId | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

**Error codes:**

| Error Code ID |
| --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [13200002](../../apis-basic-services-kit/errorcode-screenlock.md#13200002-screen-lock-management-service-is-abnormal) |
| 13200004 |
