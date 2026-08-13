# offStreamChange (System API)

## Modules to Import

```TypeScript
import { wifiManager } from '@kit.ConnectivityKit';
```

## offStreamChange

```TypeScript
function offStreamChange(callback?: Callback<number>): void
```

Unsubscribe Wi-Fi stream change events. All callback functions will be deregistered If there is no specific callback parameter.

**Since:** 23

**Deprecated since:** -1

**Required permissions:** ohos.permission.MANAGE_WIFI_CONNECTION

<!--Device-wifiManager-function offStreamChange(callback?: Callback<int>): void--><!--Device-wifiManager-function offStreamChange(callback?: Callback<int>): void-End-->

**System capability:** SystemCapability.Communication.WiFi.STA

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;number&gt; | No |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [2501000](../errorcode-wifi.md#2501000-sta-internal-error) |
