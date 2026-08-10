# initSession

## Modules to Import

```TypeScript
import { huks } from 'kits/@kit.UniversalKeystoreKit';
```

## initSession

```TypeScript
function initSession(keyAlias: string, options: HuksOptions, callback: AsyncCallback<HuksSessionHandle>): void
```

initSession操作密钥接口。使用callback异步回调。

huks.initSession、huks.updateSession、huks.finishSession为三段式接口，需要一起使用。

> **说明：**
> 
> 初始化[HuksKeySecurityLevel](arkts-universalkeystore-huks-hukskeysecuritylevel-e.md)中定义的SE安全级别密钥会话需要ohos.permission.ACCESS_SE_KEY权限。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-huks-function initSession(keyAlias: string, options: HuksOptions, callback: AsyncCallback<HuksSessionHandle>): void--><!--Device-huks-function initSession(keyAlias: string, options: HuksOptions, callback: AsyncCallback<HuksSessionHandle>): void-End-->

**System capability:** SystemCapability.Security.Huks.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| keyAlias | string | Yes | initSession操作密钥的别名。 |
| options | [HuksOptions](arkts-universalkeystore-huks-huksoptions-i.md) | Yes | initSession操作的参数集合。 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;HuksSessionHandle&gt; | Yes | 回调函数。当密钥操作init成功时，err为undefined，data为获取到的HuksSessionHandle；否 则为错误对象。HuksSessionHandle的handle返回initSession生成的handle。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 12000023 | the UKey PIN not authenticated<br>**Applicable version:** 22 and later |
| 801 | api is not supported |
| 12000021 | the UKey PIN is locked<br>**Applicable version:** 22 and later |
| 12000020 | the provider operation failed<br>**Applicable version:** 22 and later |
| 12000018 | the input parameter is invalid. Possible causes: 1. the aead length is invalid. 2. the group id specified by the access group tag is invalid.<br>**Applicable version:** 22 and later |
| 201 | The application permissions are insufficient, possibly because the ohos.permission.ACCESS_SE_KEY permission is missing.<br>**Applicable version:** 26.0.0 and later |
| 12000026 | the secure element is not available<br>**Applicable version:** 26.0.0 and later |
| 12000024 | the provider or UKey is busy<br>**Applicable version:** 22 and later |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 12000006 | error occurred in crypto engine or UKey driver |
| 12000005 | IPC communication failed |
| 12000004 | operating file failed |
| 12000003 | algorithm param is invalid |
| 12000002 | algorithm param is missing |
| 12000001 | algorithm mode is not supported |
| 12000014 | memory is insufficient |
| 12000012 | Device environment or input parameter abnormal |
| 12000011 | queried entity does not exist |
| 12000010 | the number of sessions has reached limit |


## initSession

```TypeScript
function initSession(keyAlias: string, options: HuksOptions): Promise<HuksSessionHandle>
```

initSession操作密钥接口。使用Promise异步回调。

huks.initSession、huks.updateSession、huks.finishSession为三段式接口，需要一起使用。

> **说明：**
> 
> 初始化[HuksKeySecurityLevel](arkts-universalkeystore-huks-hukskeysecuritylevel-e.md)中定义的SE安全级别密钥会话需要ohos.permission.ACCESS_SE_KEY权限。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-huks-function initSession(keyAlias: string, options: HuksOptions): Promise<HuksSessionHandle>--><!--Device-huks-function initSession(keyAlias: string, options: HuksOptions): Promise<HuksSessionHandle>-End-->

**System capability:** SystemCapability.Security.Huks.Extension

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| keyAlias | string | Yes | initSession操作密钥的别名。 |
| options | [HuksOptions](arkts-universalkeystore-huks-huksoptions-i.md) | Yes | initSession参数集合。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;HuksSessionHandle&gt; | Promise对象，返回HuksSessionHandle。HuksSessionHandle的handle返回initSession生成的 handle。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 12000023 | the UKey PIN not authenticated<br>**Applicable version:** 22 and later |
| 801 | api is not supported |
| 12000021 | the UKey PIN is locked<br>**Applicable version:** 22 and later |
| 12000020 | the provider operation failed<br>**Applicable version:** 22 and later |
| 12000018 | the input parameter is invalid. Possible causes: 1. the aead length is invalid. 2. the group id specified by the access group tag is invalid.<br>**Applicable version:** 22 and later |
| 201 | The application permissions are insufficient, possibly because the ohos.permission.ACCESS_SE_KEY permission is missing.<br>**Applicable version:** 26.0.0 and later |
| 12000026 | the secure element is not available<br>**Applicable version:** 26.0.0 and later |
| 12000024 | the provider or UKey is busy<br>**Applicable version:** 22 and later |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 12000006 | error occurred in crypto engine or UKey driver |
| 12000005 | IPC communication failed |
| 12000004 | operating file failed |
| 12000003 | algorithm param is invalid |
| 12000002 | algorithm param is missing |
| 12000001 | algorithm mode is not supported |
| 12000014 | memory is insufficient |
| 12000012 | Device environment or input parameter abnormal |
| 12000011 | queried entity does not exist |
| 12000010 | the number of sessions has reached limit |

