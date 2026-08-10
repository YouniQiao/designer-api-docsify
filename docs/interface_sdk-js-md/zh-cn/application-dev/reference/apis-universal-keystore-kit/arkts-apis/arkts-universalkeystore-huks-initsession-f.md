# initSession

## 导入模块

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

**起始版本：** 9

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为9。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-huks-function initSession(keyAlias: string, options: HuksOptions, callback: AsyncCallback<HuksSessionHandle>): void--><!--Device-huks-function initSession(keyAlias: string, options: HuksOptions, callback: AsyncCallback<HuksSessionHandle>): void-End-->

**系统能力：** SystemCapability.Security.Huks.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| keyAlias | string | 是 | initSession操作密钥的别名。 |
| options | [HuksOptions](arkts-universalkeystore-huks-huksoptions-i.md) | 是 | initSession操作的参数集合。 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;HuksSessionHandle&gt; | 是 | 回调函数。当密钥操作init成功时，err为undefined，data为获取到的HuksSessionHandle；否 则为错误对象。HuksSessionHandle的handle返回initSession生成的handle。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 12000023 | the UKey PIN not authenticated<br>**适用版本：** 22+ |
| 801 | api is not supported |
| 12000021 | the UKey PIN is locked<br>**适用版本：** 22+ |
| 12000020 | the provider operation failed<br>**适用版本：** 22+ |
| 12000018 | the input parameter is invalid. Possible causes: 1. the aead length is invalid. 2. the group id specified by the access group tag is invalid.<br>**适用版本：** 22+ |
| 201 | The application permissions are insufficient, possibly because the ohos.permission.ACCESS_SE_KEY permission is missing.<br>**适用版本：** 26.0.0+ |
| 12000026 | the secure element is not available<br>**适用版本：** 26.0.0+ |
| 12000024 | the provider or UKey is busy<br>**适用版本：** 22+ |
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

**起始版本：** 9

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为9。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-huks-function initSession(keyAlias: string, options: HuksOptions): Promise<HuksSessionHandle>--><!--Device-huks-function initSession(keyAlias: string, options: HuksOptions): Promise<HuksSessionHandle>-End-->

**系统能力：** SystemCapability.Security.Huks.Extension

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| keyAlias | string | 是 | initSession操作密钥的别名。 |
| options | [HuksOptions](arkts-universalkeystore-huks-huksoptions-i.md) | 是 | initSession参数集合。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;HuksSessionHandle&gt; | Promise对象，返回HuksSessionHandle。HuksSessionHandle的handle返回initSession生成的 handle。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 12000023 | the UKey PIN not authenticated<br>**适用版本：** 22+ |
| 801 | api is not supported |
| 12000021 | the UKey PIN is locked<br>**适用版本：** 22+ |
| 12000020 | the provider operation failed<br>**适用版本：** 22+ |
| 12000018 | the input parameter is invalid. Possible causes: 1. the aead length is invalid. 2. the group id specified by the access group tag is invalid.<br>**适用版本：** 22+ |
| 201 | The application permissions are insufficient, possibly because the ohos.permission.ACCESS_SE_KEY permission is missing.<br>**适用版本：** 26.0.0+ |
| 12000026 | the secure element is not available<br>**适用版本：** 26.0.0+ |
| 12000024 | the provider or UKey is busy<br>**适用版本：** 22+ |
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

