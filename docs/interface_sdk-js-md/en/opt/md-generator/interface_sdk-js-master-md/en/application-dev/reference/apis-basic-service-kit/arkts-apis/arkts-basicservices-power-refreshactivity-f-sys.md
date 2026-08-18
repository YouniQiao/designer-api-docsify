# refreshActivity (System API)

## Modules to Import

```TypeScript
```

## refreshActivity

```TypeScript
function refreshActivity(reason: string): void
```

Refreshes the device activity status (for example, resetting the screen-off time). This API takes effect only when the device is active. For details about the device activity status, see [power.isActive](arkts-basicservices-power-isactive-f.md#isactive).

**Since:** 23

**Required permissions:** ohos.permission.REFRESH_USER_ACTION

<!--Device-power-function refreshActivity(reason: string): void--><!--Device-power-function refreshActivity(reason: string): void-End-->

**System capability:** SystemCapability.PowerManager.PowerManager.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| reason | string | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [4900201](../../apis-basic-services-kit/errorcode-power.md#4900201-frequent-status-refreshes) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [4900101](../../apis-basic-services-kit/errorcode-power.md#4900101-service-connection-failure) |

**Examples**

```TypeScript
try {
    power.refreshActivity('refreshActivity_test');
} catch(err) {
    console.error('refreshActivity failed, err: ' + err);
}
```
