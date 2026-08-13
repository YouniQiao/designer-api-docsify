# getKeyItemProperties

## getKeyItemProperties

```TypeScript
function getKeyItemProperties(
    keyAlias: string,
    options: HuksOptions,
    callback: AsyncCallback<HuksReturnResult>
  ): void
```

Obtains key properties. This API uses an asynchronous callback to return the result. > **说明：** > > 获取[HuksKeySecurityLevel](arkts-universalkeystore-huks-hukskeysecuritylevel-e.md#HuksKeySecurityLevel)中定义的SE安全级别密钥属性需要ohos.permission.ACCESS_SE_KEY权限。

**起始版本：** 9

**废弃版本：** -1

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-huks-function getKeyItemProperties(    keyAlias: string,    options: HuksOptions,    callback: AsyncCallback<HuksReturnResult>  ): void--><!--Device-huks-function getKeyItemProperties(    keyAlias: string,    options: HuksOptions,    callback: AsyncCallback<HuksReturnResult>  ): void-End-->

**系统能力：** 
- API版本12+：SystemCapability.Security.Huks.Core
- API版本9-11：SystemCapability.Security.Huks.Extension

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| keyAlias | string | 是 |
| options | [HuksOptions](arkts-universalkeystore-huks-huksoptions-i.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[HuksReturnResult](arkts-universalkeystore-huks-huksreturnresult-i.md)&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [12000018](../errorcode-huks.md#12000018-输入参数非法) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [12000026](../errorcode-huks.md#12000026-安全元件故障) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [12000006](../errorcode-huks.md#12000006-算法库操作失败) |
| [12000005](../errorcode-huks.md#12000005-进程通信错误) |
| [12000004](../errorcode-huks.md#12000004-文件错误) |
| [12000003](../errorcode-huks.md#12000003-无效的密钥算法参数) |
| [12000002](../errorcode-huks.md#12000002-缺少密钥算法参数) |
| [12000001](../errorcode-huks.md#12000001-该子功能不支持特性) |
| [12000014](../errorcode-huks.md#12000014-内存不足) |
| [12000012](../errorcode-huks.md#12000012-外部错误) |
| [12000011](../errorcode-huks.md#12000011-目标对象不存在) |

## 示例

```TypeScript
import { huks } from '@kit.UniversalKeystoreKit';

/* 此处options选择emptyOptions来传空 */
let keyAlias = 'keyAlias';
let emptyOptions: huks.HuksOptions = {
  properties: []
};

/* 获取密钥属性 */
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

获取密钥属性。使用Promise异步回调。 > **说明：** > > 获取[HuksKeySecurityLevel](arkts-universalkeystore-huks-hukskeysecuritylevel-e.md#HuksKeySecurityLevel)中定义的SE安全级别密钥属性需要ohos.permission.ACCESS_SE_KEY权限。

**起始版本：** 9

**废弃版本：** -1

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-huks-function getKeyItemProperties(keyAlias: string, options: HuksOptions): Promise<HuksReturnResult>--><!--Device-huks-function getKeyItemProperties(keyAlias: string, options: HuksOptions): Promise<HuksReturnResult>-End-->

**系统能力：** SystemCapability.Security.Huks.Extension

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| keyAlias | string | 是 |
| options | [HuksOptions](arkts-universalkeystore-huks-huksoptions-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;[HuksReturnResult](arkts-universalkeystore-huks-huksreturnresult-i.md)&gt; |

**错误码：**

| 错误码ID |
| --- |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [12000018](../errorcode-huks.md#12000018-输入参数非法) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [12000026](../errorcode-huks.md#12000026-安全元件故障) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [12000006](../errorcode-huks.md#12000006-算法库操作失败) |
| [12000005](../errorcode-huks.md#12000005-进程通信错误) |
| [12000004](../errorcode-huks.md#12000004-文件错误) |
| [12000003](../errorcode-huks.md#12000003-无效的密钥算法参数) |
| [12000002](../errorcode-huks.md#12000002-缺少密钥算法参数) |
| [12000001](../errorcode-huks.md#12000001-该子功能不支持特性) |
| [12000014](../errorcode-huks.md#12000014-内存不足) |
| [12000012](../errorcode-huks.md#12000012-外部错误) |
| [12000011](../errorcode-huks.md#12000011-目标对象不存在) |

## 示例

```TypeScript
import { huks } from '@kit.UniversalKeystoreKit';

/* 此处options选择emptyOptions来传空 */
let keyAlias = 'keyAlias';
let emptyOptions: huks.HuksOptions = {
  properties: []
};

/* 获取密钥属性 */
huks.getKeyItemProperties(keyAlias, emptyOptions)
  .then((data) => {
    console.info(`promise: getKeyItemProperties success, data = ${JSON.stringify(data)}`);
  });
```
