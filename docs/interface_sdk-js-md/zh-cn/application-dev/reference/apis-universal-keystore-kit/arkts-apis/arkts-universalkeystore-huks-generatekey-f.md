# generateKey

## 导入模块

```TypeScript
import { huks } from 'kits/@kit.UniversalKeystoreKit';
```

## generateKey

```TypeScript
function generateKey(keyAlias: string, options: HuksOptions, callback: AsyncCallback<HuksResult>): void
```

生成密钥。使用callback异步回调。

> **说明：**&gt;
> 从API version 8开始支持，从API version 9开始废弃，建议使用
> [huks.generateKeyItem&lt;sup&gt;9+&lt;/sup&gt;](arkts-universalkeystore-huks-generatekeyitem-f.md)
> 替代。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [generateKeyItem](arkts-universalkeystore-huks-generatekeyitem-f.md)(keyAlias: string, options: HuksOptions, callback: AsyncCallback&lt;void&gt;)

**系统能力：** SystemCapability.Security.Huks.Extension

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| keyAlias | string | 是 |
| options | [HuksOptions](arkts-universalkeystore-huks-huksoptions-i.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[HuksResult](arkts-universalkeystore-huks-huksresult-i.md)&gt; | 是 |


## generateKey

```TypeScript
function generateKey(keyAlias: string, options: HuksOptions): Promise<HuksResult>
```

生成密钥。使用Promise异步回调。

> **说明：**&gt;
> 从API version 8开始支持，从API version 9开始废弃，建议使用
> [huks.generateKeyItem&lt;sup&gt;9+&lt;/sup&gt;](arkts-universalkeystore-huks-generatekeyitem-f.md)替代。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [generateKeyItem](arkts-universalkeystore-huks-generatekeyitem-f.md)(keyAlias: string, options: HuksOptions)

**系统能力：** SystemCapability.Security.Huks.Extension

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| keyAlias | string | 是 |
| options | [HuksOptions](arkts-universalkeystore-huks-huksoptions-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;[HuksResult](arkts-universalkeystore-huks-huksresult-i.md)&gt; |
