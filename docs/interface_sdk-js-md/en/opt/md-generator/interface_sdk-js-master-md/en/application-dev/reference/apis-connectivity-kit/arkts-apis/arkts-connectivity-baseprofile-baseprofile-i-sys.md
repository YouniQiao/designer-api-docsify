# BaseProfile

Base interface of profile.

**Since:** 23

**Deprecated since:** -1

<!--Device-baseProfile-export interface BaseProfile--><!--Device-baseProfile-export interface BaseProfile-End-->

**System capability:** SystemCapability.Communication.Bluetooth.Core

## Modules to Import

```TypeScript
import { baseProfile } from '@kit.ConnectivityKit';
```

## getConnectionStrategy

```TypeScript
getConnectionStrategy(deviceId: string, callback: AsyncCallback<ConnectionStrategy>): void
```

Get connection strategy of this profile.

**Since:** 23

**Deprecated since:** -1

**Required permissions:** ohos.permission.ACCESS_BLUETOOTH and ohos.permission.MANAGE_BLUETOOTH

**Model restriction:** This API can be used only in the stage model.

<!--Device-BaseProfile-getConnectionStrategy(deviceId: string, callback: AsyncCallback<ConnectionStrategy>): void--><!--Device-BaseProfile-getConnectionStrategy(deviceId: string, callback: AsyncCallback<ConnectionStrategy>): void-End-->

**System capability:** SystemCapability.Communication.Bluetooth.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| deviceId | string | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[ConnectionStrategy](arkts-connectivity-baseprofile-connectionstrategy-e-sys.md)&gt; | Yes |

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

## getConnectionStrategy

```TypeScript
getConnectionStrategy(deviceId: string): Promise<ConnectionStrategy>
```

Get connection strategy of this profile.

**Since:** 23

**Deprecated since:** -1

**Required permissions:** ohos.permission.ACCESS_BLUETOOTH and ohos.permission.MANAGE_BLUETOOTH

**Model restriction:** This API can be used only in the stage model.

<!--Device-BaseProfile-getConnectionStrategy(deviceId: string): Promise<ConnectionStrategy>--><!--Device-BaseProfile-getConnectionStrategy(deviceId: string): Promise<ConnectionStrategy>-End-->

**System capability:** SystemCapability.Communication.Bluetooth.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| deviceId | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[ConnectionStrategy](arkts-connectivity-baseprofile-connectionstrategy-e-sys.md)&gt; |

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

## setConnectionStrategy

```TypeScript
setConnectionStrategy(deviceId: string, strategy: ConnectionStrategy): Promise<void>
```

Set connection strategy of this profile.

**Since:** 23

**Deprecated since:** -1

**Required permissions:** ohos.permission.ACCESS_BLUETOOTH and ohos.permission.MANAGE_BLUETOOTH

**Model restriction:** This API can be used only in the stage model.

<!--Device-BaseProfile-setConnectionStrategy(deviceId: string, strategy: ConnectionStrategy): Promise<void>--><!--Device-BaseProfile-setConnectionStrategy(deviceId: string, strategy: ConnectionStrategy): Promise<void>-End-->

**System capability:** SystemCapability.Communication.Bluetooth.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| deviceId | string | Yes |
| strategy | [ConnectionStrategy](arkts-connectivity-baseprofile-connectionstrategy-e-sys.md) | Yes |

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

## setConnectionStrategy

```TypeScript
setConnectionStrategy(deviceId: string, strategy: ConnectionStrategy, callback: AsyncCallback<void>): void
```

Set connection strategy of this profile.

**Since:** 23

**Deprecated since:** -1

**Required permissions:** ohos.permission.ACCESS_BLUETOOTH and ohos.permission.MANAGE_BLUETOOTH

**Model restriction:** This API can be used only in the stage model.

<!--Device-BaseProfile-setConnectionStrategy(deviceId: string, strategy: ConnectionStrategy, callback: AsyncCallback<void>): void--><!--Device-BaseProfile-setConnectionStrategy(deviceId: string, strategy: ConnectionStrategy, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Communication.Bluetooth.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| deviceId | string | Yes |
| strategy | [ConnectionStrategy](arkts-connectivity-baseprofile-connectionstrategy-e-sys.md) | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

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
