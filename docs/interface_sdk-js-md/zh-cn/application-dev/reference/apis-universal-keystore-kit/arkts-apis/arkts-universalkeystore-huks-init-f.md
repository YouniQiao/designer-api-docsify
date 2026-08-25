# init

## 导入模块

```TypeScript
import { huks } from '@kit.UniversalKeystoreKit';
```

## init

```TypeScript
function init(keyAlias: string, options: HuksOptions, callback: AsyncCallback<HuksHandle>): void
```

init操作密钥接口。使用callback异步回调。huks.init、huks.update、huks.finish为三段式接口，需要一起使用。

> **说明：**&gt;
> 从API version 8开始支持，从API version 9开始废弃，建议使用
> [huks.initSession&lt;sup&gt;9+&lt;/sup&gt;](arkts-universalkeystore-huks-initsession-f.md)替代。

**起始版本：** 8

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为8。

**废弃版本：** 9

**替代接口：** [initSession](arkts-universalkeystore-huks-initsession-f.md)(keyAlias: string, options: HuksOptions)

**系统能力：** SystemCapability.Security.Huks.Extension

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| keyAlias | string | 是 |
| options | [HuksOptions](arkts-universalkeystore-huks-huksoptions-i.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[HuksHandle](arkts-universalkeystore-huks-hukshandle-i.md)&gt; | 是 |


## init

```TypeScript
function init(keyAlias: string, options: HuksOptions): Promise<HuksHandle>
```

init操作密钥接口。使用Promise异步回调。huks.init、huks.update、huks.finish为三段式接口，需要一起使用。

> **说明：**&gt;
> 从API version 8开始支持，从API version 9开始废弃，建议使用
> [huks.initSession&lt;sup&gt;9+&lt;/sup&gt;](arkts-universalkeystore-huks-initsession-f.md)替代。

**起始版本：** 8

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为8。

**废弃版本：** 9

**替代接口：** [initSession](arkts-universalkeystore-huks-initsession-f.md)(keyAlias: string, options: HuksOptions)

**系统能力：** SystemCapability.Security.Huks.Extension

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| keyAlias | string | 是 |
| options | [HuksOptions](arkts-universalkeystore-huks-huksoptions-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;[HuksHandle](arkts-universalkeystore-huks-hukshandle-i.md)&gt; |
