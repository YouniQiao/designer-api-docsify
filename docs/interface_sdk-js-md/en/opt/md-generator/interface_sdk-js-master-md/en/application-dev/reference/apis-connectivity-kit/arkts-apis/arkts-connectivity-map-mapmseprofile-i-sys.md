# MapMseProfile

Manager MAP MSE profile.

**Inheritance/Implementation:** MapMseProfile extends [BaseProfile](arkts-connectivity-map-baseprofile-t.md#BaseProfile)

**Since:** 26.0.0

**Deprecated since:** -1

<!--Device-map-interface MapMseProfile--><!--Device-map-interface MapMseProfile-End-->

**System capability:** SystemCapability.Communication.Bluetooth.Core

## Modules to Import

```TypeScript
import { map } from '@kit.ConnectivityKit';
```

## disconnect

```TypeScript
disconnect(deviceId: string): void
```

Disconnect the map connection with the remote device.

**Since:** 26.0.0

**Deprecated since:** -1

**Required permissions:** ohos.permission.ACCESS_BLUETOOTH

<!--Device-MapMseProfile-disconnect(deviceId: string): void--><!--Device-MapMseProfile-disconnect(deviceId: string): void-End-->

**System capability:** SystemCapability.Communication.Bluetooth.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| deviceId | string | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| 2900004 |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| 2900001 |
| 2900003 |
| 2900099 |

## getMessageAccessAuthorization

```TypeScript
getMessageAccessAuthorization(deviceId: string): Promise<AccessAuthorization>
```

Get the message access authorization.

**Since:** 26.0.0

**Deprecated since:** -1

**Required permissions:** ohos.permission.ACCESS_BLUETOOTH and ohos.permission.MANAGE_BLUETOOTH

<!--Device-MapMseProfile-getMessageAccessAuthorization(deviceId: string): Promise<AccessAuthorization>--><!--Device-MapMseProfile-getMessageAccessAuthorization(deviceId: string): Promise<AccessAuthorization>-End-->

**System capability:** SystemCapability.Communication.Bluetooth.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| deviceId | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;AccessAuthorization & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| 2900004 |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| 2900001 |
| 2900003 |
| 2900099 |

## setMessageAccessAuthorization

```TypeScript
setMessageAccessAuthorization(deviceId: string, authorization: AccessAuthorization): Promise<void>
```

Set the message access authorization.

**Since:** 26.0.0

**Deprecated since:** -1

**Required permissions:** ohos.permission.ACCESS_BLUETOOTH and ohos.permission.MANAGE_BLUETOOTH

<!--Device-MapMseProfile-setMessageAccessAuthorization(deviceId: string, authorization: AccessAuthorization): Promise<void>--><!--Device-MapMseProfile-setMessageAccessAuthorization(deviceId: string, authorization: AccessAuthorization): Promise<void>-End-->

**System capability:** SystemCapability.Communication.Bluetooth.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| deviceId | string | Yes |
| authorization | [AccessAuthorization](arkts-connectivity-constant-accessauthorization-e-sys.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| 2900004 |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| 2900001 |
| 2900003 |
| 2900099 |
