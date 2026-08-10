# getKeyItemProperties

## Modules to Import

```TypeScript
import { huks } from 'kits/@kit.UniversalKeystoreKit';
```

## getKeyItemProperties

```TypeScript
function getKeyItemProperties(
    keyAlias: string,
    options: HuksOptions,
    callback: AsyncCallback<HuksReturnResult>
  ): void
```

Obtains key properties. This API uses an asynchronous callback to return the result.

> **说明：**
> 
> 获取[HuksKeySecurityLevel](arkts-universalkeystore-huks-hukskeysecuritylevel-e.md)中定义的SE安全级别密钥属性需要ohos.permission.ACCESS_SE_KEY权限。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-huks-function getKeyItemProperties(    keyAlias: string,    options: HuksOptions,    callback: AsyncCallback<HuksReturnResult>  ): void--><!--Device-huks-function getKeyItemProperties(    keyAlias: string,    options: HuksOptions,    callback: AsyncCallback<HuksReturnResult>  ): void-End-->

**System capability:** 
- API version 12 and later: SystemCapability.Security.Huks.Core
- API version 9 to 11: SystemCapability.Security.Huks.Extension

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| keyAlias | string | Yes | Key alias, which must be the same as the alias used when the key was generated. |
| options | [HuksOptions](arkts-universalkeystore-huks-huksoptions-i.md) | Yes | Empty object (leave this parameter empty). |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;HuksReturnResult&gt; | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined**, and **data** is the obtained **HuksReturnResult**. Otherwise, **err** is an error object. **properties** of **HuksReturnResult** are the parameters required for generating a key. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 801 | api is not supported |
| 12000018 | the group id specified by the access group tag is invalid<br>**Applicable version:** 23 and later |
| 201 | The application permissions are insufficient, possibly because the ohos.permission.ACCESS_SE_KEY permission is missing.<br>**Applicable version:** 26.0.0 and later |
| 12000026 | the secure element is not available<br>**Applicable version:** 26.0.0 and later |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 12000006 | error occurred in crypto engine |
| 12000005 | IPC communication failed |
| 12000004 | operating file failed |
| 12000003 | algorithm param is invalid<br>**Applicable version:** 9 - 11 |
| 12000002 | algorithm param is missing<br>**Applicable version:** 9 - 11 |
| 12000001 | algorithm mode is not supported |
| 12000014 | memory is insufficient |
| 12000012 | Device environment or input parameter abnormal |
| 12000011 | queried entity does not exist |

## Examples

```TypeScript
import { huks } from '@kit.UniversalKeystoreKit';

/* Set options to emptyOptions. */
let keyAlias = 'keyAlias';
let emptyOptions: huks.HuksOptions = {
  properties: []
};

huks.getKeyItemProperties(keyAlias, emptyOptions, (error, data) => {
  if (error) {
    console.error(`callback: getKeyItemProperties failed`);
  } else {
    console.info(`callback: getKeyItemProperties success, data = ${JSON.stringify(data)}`);
  }
});
```


## getKeyItemProperties

```TypeScript
function getKeyItemProperties(keyAlias: string, options: HuksOptions): Promise<HuksReturnResult>
```

获取密钥属性。使用Promise异步回调。

> **说明：**
> 
> 获取[HuksKeySecurityLevel](arkts-universalkeystore-huks-hukskeysecuritylevel-e.md)中定义的SE安全级别密钥属性需要ohos.permission.ACCESS_SE_KEY权限。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-huks-function getKeyItemProperties(keyAlias: string, options: HuksOptions): Promise<HuksReturnResult>--><!--Device-huks-function getKeyItemProperties(keyAlias: string, options: HuksOptions): Promise<HuksReturnResult>-End-->

**System capability:** SystemCapability.Security.Huks.Extension

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| keyAlias | string | Yes | 密钥别名，应与所用密钥生成时使用的别名相同。 |
| options | [HuksOptions](arkts-universalkeystore-huks-huksoptions-i.md) | Yes | 空对象（此处传空即可）。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;HuksReturnResult&gt; | Promise对象，返回调用接口的结果。当调用成功时，HuksReturnResult的properties成员为获取的密钥属性信息。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 801 | api is not supported |
| 12000018 | the group id specified by the access group tag is invalid<br>**Applicable version:** 23 and later |
| 201 | The application permissions are insufficient, possibly because the ohos.permission.ACCESS_SE_KEY permission is missing.<br>**Applicable version:** 26.0.0 and later |
| 12000026 | the secure element is not available<br>**Applicable version:** 26.0.0 and later |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 12000006 | error occurred in crypto engine |
| 12000005 | IPC communication failed |
| 12000004 | operating file failed |
| 12000003 | algorithm param is invalid<br>**Applicable version:** 9 - 11 |
| 12000002 | algorithm param is missing<br>**Applicable version:** 9 - 11 |
| 12000001 | algorithm mode is not supported |
| 12000014 | memory is insufficient |
| 12000012 | Device environment or input parameter abnormal |
| 12000011 | queried entity does not exist |

## Examples

```TypeScript
import { huks } from '@kit.UniversalKeystoreKit';

/* Set options to emptyOptions. */
let keyAlias = 'keyAlias';
let emptyOptions: huks.HuksOptions = {
  properties: []
};

huks.getKeyItemProperties(keyAlias, emptyOptions)
  .then((data) => {
    console.info(`promise: getKeyItemProperties success, data = ${JSON.stringify(data)}`);
  });
```

