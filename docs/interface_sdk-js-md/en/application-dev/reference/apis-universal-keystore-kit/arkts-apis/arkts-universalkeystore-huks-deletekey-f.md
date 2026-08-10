# deleteKey

## Modules to Import

```TypeScript
import { huks } from 'kits/@kit.UniversalKeystoreKit';
```

## deleteKey

```TypeScript
function deleteKey(keyAlias: string, options: HuksOptions, callback: AsyncCallback<HuksResult>): void
```

删除密钥。使用callback异步回调。

> **说明：**
> 
> 从API version 8开始支持，从API version 9开始废弃，建议使用
> [huks.deleteKeyItem&lt;sup&gt;9+&lt;/sup&gt;](arkts-universalkeystore-huks-deletekeyitem-f.md#deletekeyitem)
> 替代。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Deprecated since:** 9

**Substitutes:** [huks.deleteKeyItem](arkts-universalkeystore-huks-deletekeyitem-f.md#deletekeyitem)(keyAlias:

<!--Device-huks-function deleteKey(keyAlias: string, options: HuksOptions, callback: AsyncCallback<HuksResult>): void--><!--Device-huks-function deleteKey(keyAlias: string, options: HuksOptions, callback: AsyncCallback<HuksResult>): void-End-->

**System capability:** SystemCapability.Security.Huks.Extension

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| keyAlias | string | Yes | 密钥别名，应为生成key时传入的别名。 |
| options | [HuksOptions](arkts-universalkeystore-huks-huksoptions-i.md) | Yes | 用于删除时指定密钥的属性TAG。 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;HuksResult&gt; | Yes | 回调函数。当删除密钥成功时，err为undefined，data为获取到的HuksResult；否则为错误对象。 |

## Examples

```TypeScript
import { huks } from '@kit.UniversalKeystoreKit';

/* Set options to emptyOptions. */
let keyAlias = 'keyAlias';
let emptyOptions: huks.HuksOptions = {
  properties: []
};
huks.deleteKey(keyAlias, emptyOptions, (err, data) => {
});
```


## deleteKey

```TypeScript
function deleteKey(keyAlias: string, options: HuksOptions): Promise<HuksResult>
```

删除密钥。使用Promise异步回调。

> **说明：**
> 
> 从API version 8开始支持，从API version 9开始废弃，建议使用
> [huks.deleteKeyItem&lt;sup&gt;9+&lt;/sup&gt;](arkts-universalkeystore-huks-deletekeyitem-f.md#deletekeyitem)替代。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Deprecated since:** 9

**Substitutes:** [huks.deleteKeyItem](arkts-universalkeystore-huks-deletekeyitem-f.md#deletekeyitem)(keyAlias:

<!--Device-huks-function deleteKey(keyAlias: string, options: HuksOptions): Promise<HuksResult>--><!--Device-huks-function deleteKey(keyAlias: string, options: HuksOptions): Promise<HuksResult>-End-->

**System capability:** SystemCapability.Security.Huks.Extension

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| keyAlias | string | Yes | 密钥别名，应为生成key时传入的别名。 |
| options | [HuksOptions](arkts-universalkeystore-huks-huksoptions-i.md) | Yes | 用于删除时指定密钥的属性TAG。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;HuksResult&gt; | Promise对象，返回HuksResult。 |

## Examples

```TypeScript
import { huks } from '@kit.UniversalKeystoreKit';
import { BusinessError } from "@kit.BasicServicesKit"

/* Set options to emptyOptions. */
let keyAlias = 'keyAlias';
let emptyOptions: huks.HuksOptions = {
  properties: []
};
let result = huks.deleteKey(keyAlias, emptyOptions).then((data) => {
  console.info('delete key success');
}).catch((err: BusinessError) => {
  console.error("Failed to delete the key. Error code: " + err.code + " Error message: " + err.message);
});
```

