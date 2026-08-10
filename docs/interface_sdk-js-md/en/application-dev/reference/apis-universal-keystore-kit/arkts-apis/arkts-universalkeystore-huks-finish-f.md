# finish

## Modules to Import

```TypeScript
import { huks } from 'kits/@kit.UniversalKeystoreKit';
```

## finish

```TypeScript
function finish(handle: number, options: HuksOptions, callback: AsyncCallback<HuksResult>): void
```

finish操作密钥接口。使用callback异步回调。

huks.init、huks.update、huks.finish为三段式接口，需要一起使用。

> **说明：**
> 
> 从API version 8开始支持，从API version 9开始废弃，建议使用
> [huks.finishSession&lt;sup&gt;9+&lt;/sup&gt;](arkts-universalkeystore-huks-finishsession-f.md#finishsession)
> 替代。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Deprecated since:** 9

**Substitutes:** [huks.finishSession](arkts-universalkeystore-huks-finishsession-f.md#finishsession)(handle:

<!--Device-huks-function finish(handle: number, options: HuksOptions, callback: AsyncCallback<HuksResult>): void--><!--Device-huks-function finish(handle: number, options: HuksOptions, callback: AsyncCallback<HuksResult>): void-End-->

**System capability:** SystemCapability.Security.Huks.Extension

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| handle | number | Yes | Finish操作的uint64类型的handle值。 |
| options | [HuksOptions](arkts-universalkeystore-huks-huksoptions-i.md) | Yes | Finish的参数集合。 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;HuksResult&gt; | Yes | 回调函数。当密钥操作finish成功时，err为undefined，data为获取到的HuksResult；否则为错误对象。 |


## finish

```TypeScript
function finish(handle: number, options: HuksOptions): Promise<HuksResult>
```

finish操作密钥接口。使用Promise异步回调。

huks.init、huks.update、huks.finish为三段式接口，需要一起使用。

> **说明：**
> 
> 从API version 8开始支持，从API version 9开始废弃，建议使用
> [huks.finishSession&lt;sup&gt;9+&lt;/sup&gt;](arkts-universalkeystore-huks-finishsession-f.md#finishsession)
> 替代。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Deprecated since:** 9

**Substitutes:** [huks.finishSession](arkts-universalkeystore-huks-finishsession-f.md#finishsession)(

<!--Device-huks-function finish(handle: number, options: HuksOptions): Promise<HuksResult>--><!--Device-huks-function finish(handle: number, options: HuksOptions): Promise<HuksResult>-End-->

**System capability:** SystemCapability.Security.Huks.Extension

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| handle | number | Yes | Finish操作的uint64类型的handle值。 |
| options | [HuksOptions](arkts-universalkeystore-huks-huksoptions-i.md) | Yes | Finish操作的参数集合。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;HuksResult&gt; | Promise对象，返回HuksResult。 |

