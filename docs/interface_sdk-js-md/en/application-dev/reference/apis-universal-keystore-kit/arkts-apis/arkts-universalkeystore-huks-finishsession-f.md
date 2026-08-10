# finishSession

## Modules to Import

```TypeScript
import { huks } from 'kits/@kit.UniversalKeystoreKit';
```

## finishSession

```TypeScript
function finishSession(handle: number, options: HuksOptions, callback: AsyncCallback<HuksReturnResult>): void
```

finishSession操作密钥接口。使用callback异步回调。

huks.initSession、huks.updateSession、huks.finishSession为三段式接口，需要一起使用。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-huks-function finishSession(handle: number, options: HuksOptions, callback: AsyncCallback<HuksReturnResult>): void--><!--Device-huks-function finishSession(handle: number, options: HuksOptions, callback: AsyncCallback<HuksReturnResult>): void-End-->

**System capability:** SystemCapability.Security.Huks.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| handle | number | Yes | finishSession操作的uint64类型的handle值。 |
| options | [HuksOptions](arkts-universalkeystore-huks-huksoptions-i.md) | Yes | finishSession的参数集合。 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;HuksReturnResult&gt; | Yes | 回调函数。当密钥操作finish成功时，err为undefined，data为获取到的HuksReturnResult；否 则为错误对象。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 12000023 | the UKey PIN not authenticated<br>**Applicable version:** 22 and later |
| 801 | api is not supported |
| 12000021 | the UKey PIN is locked<br>**Applicable version:** 22 and later |
| 12000020 | the provider operation failed<br>**Applicable version:** 22 and later |
| 12000018 | the group id specified by the access group tag is invalid<br>**Applicable version:** 23 and later |
| 12000017 | The key with the same alias already exists<br>**Applicable version:** 20 and later |
| 12000026 | the secure element is not available<br>**Applicable version:** 26.0.0 and later |
| 12000024 | the provider or UKey is busy<br>**Applicable version:** 22 and later |
| 12000007 | this credential is already invalidated permanently |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 12000006 | error occurred in crypto engine |
| 12000005 | IPC communication failed |
| 12000004 | operating file failed |
| 12000003 | algorithm param is invalid |
| 12000002 | algorithm param is missing |
| 12000001 | algorithm mode is not supported |
| 12000014 | memory is insufficient |
| 12000012 | Device environment or input parameter abnormal |
| 12000011 | queried entity does not exist |
| 12000009 | auth token is already timeout |
| 12000008 | verify auth token failed |


## finishSession

```TypeScript
function finishSession(
    handle: number,
    options: HuksOptions,
    token: Uint8Array,
    callback: AsyncCallback<HuksReturnResult>
  ): void
```

Finishes the key operation. This API uses an asynchronous callback to return the result.huks.initSession, huks.updateSession, and huks.finishSession must be used together.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-huks-function finishSession(    handle: number,    options: HuksOptions,    token: Uint8Array,    callback: AsyncCallback<HuksReturnResult>  ): void--><!--Device-huks-function finishSession(    handle: number,    options: HuksOptions,    token: Uint8Array,    callback: AsyncCallback<HuksReturnResult>  ): void-End-->

**System capability:** SystemCapability.Security.Huks.Extension

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| handle | number | Yes | Handle for the finishSession operation. &lt;br&gt;取值限定为整数。 |
| options | [HuksOptions](arkts-universalkeystore-huks-huksoptions-i.md) | Yes | Parameter set used for the **finishSession** operation. |
| token | Uint8Array | Yes | Authentication token for [refined key access control](../../../security/UniversalKeystoreKit/huks-identity-authentication-overview.md#refined-key-access-control) . |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;HuksReturnResult&gt; | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined**, and **data** is the obtained **HuksReturnResult**. Otherwise, **err** is an error object. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 801 | api is not supported |
| 12000018 | the group id specified by the access group tag is invalid<br>**Applicable version:** 23 and later |
| 12000017 | The key with the same alias already exists<br>**Applicable version:** 20 and later |
| 12000026 | the secure element is not available<br>**Applicable version:** 26.0.0 and later |
| 12000007 | this credential is already invalidated permanently |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 12000006 | error occurred in crypto engine |
| 12000005 | IPC communication failed |
| 12000004 | operating file failed |
| 12000003 | algorithm param is invalid |
| 12000002 | algorithm param is missing |
| 12000001 | algorithm mode is not supported |
| 12000014 | memory is insufficient |
| 12000012 | Device environment or input parameter abnormal |
| 12000011 | queried entity does not exist |
| 12000009 | auth token is already timeout |
| 12000008 | verify auth token failed |


## finishSession

```TypeScript
function finishSession(handle: number, options: HuksOptions, token?: Uint8Array): Promise<HuksReturnResult>
```

finishSession操作密钥接口。使用Promise异步回调。

huks.initSession、huks.updateSession、huks.finishSession为三段式接口，需要一起使用。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-huks-function finishSession(handle: number, options: HuksOptions, token?: Uint8Array): Promise<HuksReturnResult>--><!--Device-huks-function finishSession(handle: number, options: HuksOptions, token?: Uint8Array): Promise<HuksReturnResult>-End-->

**System capability:** SystemCapability.Security.Huks.Extension

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| handle | number | Yes | finishSession操作的uint64类型的handle值。 |
| options | [HuksOptions](arkts-universalkeystore-huks-huksoptions-i.md) | Yes | finishSession操作的参数集合。 |
| token | Uint8Array | No | 密钥 [二次认证密钥访问控制](../../../security/UniversalKeystoreKit/huks-identity-authentication-overview.md#二次认证密钥访问控制)的用户鉴权证 明(AuthToken)，不填表示不进行二次认证密钥访问控制。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;HuksReturnResult&gt; | Promise对象，返回调用接口的结果。当调用成功时，HuksReturnResult的outData成员为对应操作返回的数据。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 12000023 | the UKey PIN not authenticated<br>**Applicable version:** 22 and later |
| 801 | api is not supported |
| 12000021 | the UKey PIN is locked<br>**Applicable version:** 22 and later |
| 12000020 | the provider operation failed<br>**Applicable version:** 22 and later |
| 12000018 | the group id specified by the access group tag is invalid<br>**Applicable version:** 23 and later |
| 12000017 | The key with the same alias already exists<br>**Applicable version:** 20 and later |
| 12000026 | the secure element is not available<br>**Applicable version:** 26.0.0 and later |
| 12000024 | the provider or UKey is busy<br>**Applicable version:** 22 and later |
| 12000007 | this credential is already invalidated permanently |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 12000006 | error occurred in crypto engine |
| 12000005 | IPC communication failed |
| 12000004 | operating file failed |
| 12000003 | algorithm param is invalid |
| 12000002 | algorithm param is missing |
| 12000001 | algorithm mode is not supported |
| 12000014 | memory is insufficient |
| 12000012 | Device environment or input parameter abnormal |
| 12000011 | queried entity does not exist |
| 12000009 | auth token is already timeout |
| 12000008 | verify auth token failed |

