# initSession

## initSession

```TypeScript
function initSession(keyAlias: string, options: HuksOptions, callback: AsyncCallback<HuksSessionHandle>): void
```

initSession操作密钥接口。使用callback异步回调。

huks.initSession、huks.updateSession、huks.finishSession为三段式接口，需要一起使用。

> **说明：**
> 
> 初始化[HuksKeySecurityLevel](arkts-universalkeystore-huks-hukskeysecuritylevel-e.md#HuksKeySecurityLevel)中定义的SE安全级别密钥会话需要ohos.permission.ACCESS_SE_KEY权限。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-huks-function initSession(keyAlias: string, options: HuksOptions, callback: AsyncCallback<HuksSessionHandle>): void--><!--Device-huks-function initSession(keyAlias: string, options: HuksOptions, callback: AsyncCallback<HuksSessionHandle>): void-End-->

**系统能力：** SystemCapability.Security.Huks.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| keyAlias | string | 是 |
| options | [HuksOptions](arkts-universalkeystore-huks-huksoptions-i.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[HuksSessionHandle](arkts-universalkeystore-huks-hukssessionhandle-i.md)&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [12000023](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-universal-keystore-kit/errorcode-huks.md#12000023-ukey-pin码未认证) |
| [801](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#801-该设备不支持此api) |
| [12000021](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-universal-keystore-kit/errorcode-huks.md#12000021-ukey-pin码被锁定) |
| [12000020](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-universal-keystore-kit/errorcode-huks.md#12000020-依赖的模块报错) |
| [12000018](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-universal-keystore-kit/errorcode-huks.md#12000018-输入参数非法) |
| [201](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#201-权限校验失败) |
| [12000026](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-universal-keystore-kit/errorcode-huks.md#12000026-安全元件故障) |
| [12000024](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-universal-keystore-kit/errorcode-huks.md#12000024-设备或资源繁忙) |
| [401](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-contacts-kit/errorcode-contacts.md#401-打开联系人头像文件失败) |
| [12000006](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-universal-keystore-kit/errorcode-huks.md#12000006-算法库操作失败) |
| [12000005](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-universal-keystore-kit/errorcode-huks.md#12000005-进程通信错误) |
| [12000004](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-universal-keystore-kit/errorcode-huks.md#12000004-文件错误) |
| [12000003](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-universal-keystore-kit/errorcode-huks.md#12000003-无效的密钥算法参数) |
| [12000002](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-universal-keystore-kit/errorcode-huks.md#12000002-缺少密钥算法参数) |
| [12000001](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-universal-keystore-kit/errorcode-huks.md#12000001-该子功能不支持特性) |
| [12000014](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-universal-keystore-kit/errorcode-huks.md#12000014-内存不足) |
| [12000012](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-universal-keystore-kit/errorcode-huks.md#12000012-外部错误) |
| [12000011](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-universal-keystore-kit/errorcode-huks.md#12000011-目标对象不存在) |
| [12000010](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-universal-keystore-kit/errorcode-huks.md#12000010-密钥操作会话数已达上限) |


## initSession

```TypeScript
function initSession(keyAlias: string, options: HuksOptions): Promise<HuksSessionHandle>
```

initSession操作密钥接口。使用Promise异步回调。

huks.initSession、huks.updateSession、huks.finishSession为三段式接口，需要一起使用。

> **说明：**
> 
> 初始化[HuksKeySecurityLevel](arkts-universalkeystore-huks-hukskeysecuritylevel-e.md#HuksKeySecurityLevel)中定义的SE安全级别密钥会话需要ohos.permission.ACCESS_SE_KEY权限。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-huks-function initSession(keyAlias: string, options: HuksOptions): Promise<HuksSessionHandle>--><!--Device-huks-function initSession(keyAlias: string, options: HuksOptions): Promise<HuksSessionHandle>-End-->

**系统能力：** SystemCapability.Security.Huks.Extension

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| keyAlias | string | 是 |
| options | [HuksOptions](arkts-universalkeystore-huks-huksoptions-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;[HuksSessionHandle](arkts-universalkeystore-huks-hukssessionhandle-i.md)&gt; |

**错误码：**

| 错误码ID |
| --- |
| [12000023](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-universal-keystore-kit/errorcode-huks.md#12000023-ukey-pin码未认证) |
| [801](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#801-该设备不支持此api) |
| [12000021](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-universal-keystore-kit/errorcode-huks.md#12000021-ukey-pin码被锁定) |
| [12000020](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-universal-keystore-kit/errorcode-huks.md#12000020-依赖的模块报错) |
| [12000018](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-universal-keystore-kit/errorcode-huks.md#12000018-输入参数非法) |
| [201](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#201-权限校验失败) |
| [12000026](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-universal-keystore-kit/errorcode-huks.md#12000026-安全元件故障) |
| [12000024](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-universal-keystore-kit/errorcode-huks.md#12000024-设备或资源繁忙) |
| [401](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-contacts-kit/errorcode-contacts.md#401-打开联系人头像文件失败) |
| [12000006](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-universal-keystore-kit/errorcode-huks.md#12000006-算法库操作失败) |
| [12000005](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-universal-keystore-kit/errorcode-huks.md#12000005-进程通信错误) |
| [12000004](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-universal-keystore-kit/errorcode-huks.md#12000004-文件错误) |
| [12000003](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-universal-keystore-kit/errorcode-huks.md#12000003-无效的密钥算法参数) |
| [12000002](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-universal-keystore-kit/errorcode-huks.md#12000002-缺少密钥算法参数) |
| [12000001](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-universal-keystore-kit/errorcode-huks.md#12000001-该子功能不支持特性) |
| [12000014](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-universal-keystore-kit/errorcode-huks.md#12000014-内存不足) |
| [12000012](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-universal-keystore-kit/errorcode-huks.md#12000012-外部错误) |
| [12000011](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-universal-keystore-kit/errorcode-huks.md#12000011-目标对象不存在) |
| [12000010](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-universal-keystore-kit/errorcode-huks.md#12000010-密钥操作会话数已达上限) |
