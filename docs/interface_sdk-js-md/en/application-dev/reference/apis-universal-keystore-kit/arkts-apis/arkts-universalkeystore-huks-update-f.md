# update

## Modules to Import

```TypeScript
import { huks } from 'kits/@kit.UniversalKeystoreKit';
```

## update

```TypeScript
function update(handle: number, token?: Uint8Array, options: HuksOptions, callback: AsyncCallback<HuksResult>): void
```

update操作密钥接口。使用callback异步回调。

huks.init、huks.update、huks.finish为三段式接口，需要一起使用。

> **说明：**
> 
> 从API version 8开始支持，从API version 9开始废弃，建议使用
> [huks.updateSession&lt;sup&gt;9+&lt;/sup&gt;](arkts-universalkeystore-huks-updatesession-f.md#updatesession)
> 替代。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Deprecated since:** 9

**Substitutes:** [huks.updateSession](arkts-universalkeystore-huks-updatesession-f.md#updatesession)(

<!--Device-huks-function update(handle: number, token?: Uint8Array, options: HuksOptions, callback: AsyncCallback<HuksResult>): void--><!--Device-huks-function update(handle: number, token?: Uint8Array, options: HuksOptions, callback: AsyncCallback<HuksResult>): void-End-->

**System capability:** SystemCapability.Security.Huks.Extension

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| handle | number | Yes | Update操作的uint64类型的handle值。 |
| token | Uint8Array | No | Update操作的token。 |
| options | [HuksOptions](arkts-universalkeystore-huks-huksoptions-i.md) | Yes | Update操作的参数集合。 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;HuksResult&gt; | Yes | 回调函数。当密钥操作update成功时，err为undefined，data为获取到的HuksResult；否则为错误对象。 |


## update

```TypeScript
function update(handle: number, token?: Uint8Array, options: HuksOptions): Promise<HuksResult>
```

update操作密钥接口。使用Promise异步回调。

huks.init、huks.update、huks.finish为三段式接口，需要一起使用。

> **说明：**
> 
> 从API version 8开始支持，从API version 9开始废弃，建议使用
> [huks.updateSession&lt;sup&gt;9+&lt;/sup&gt;](arkts-universalkeystore-huks-updatesession-f.md#updatesession)
> 替代。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Deprecated since:** 9

**Substitutes:** [huks.updateSession](arkts-universalkeystore-huks-updatesession-f.md#updatesession)(handle:

<!--Device-huks-function update(handle: number, token?: Uint8Array, options: HuksOptions): Promise<HuksResult>--><!--Device-huks-function update(handle: number, token?: Uint8Array, options: HuksOptions): Promise<HuksResult>-End-->

**System capability:** SystemCapability.Security.Huks.Extension

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| handle | number | Yes | Update操作的uint64类型的handle值。 |
| token | Uint8Array | No | Update操作的token。 |
| options | [HuksOptions](arkts-universalkeystore-huks-huksoptions-i.md) | Yes | Update操作的参数集合。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;HuksResult&gt; | Promise对象，返回HuksResult。 |

