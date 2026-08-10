# getSdkVersion

## Modules to Import

```TypeScript
import { huks } from 'kits/@kit.UniversalKeystoreKit';
```

## getSdkVersion

```TypeScript
function getSdkVersion(options: HuksOptions): string
```

获取当前系统sdk版本。

> **说明：**
> 
> 从API version 8开始支持，从API version 11开始废弃。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Deprecated since:** 11

<!--Device-huks-function getSdkVersion(options: HuksOptions): string--><!--Device-huks-function getSdkVersion(options: HuksOptions): string-End-->

**System capability:** SystemCapability.Security.Huks.Extension

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [HuksOptions](arkts-universalkeystore-huks-huksoptions-i.md) | Yes | 空对象（此处传空即可）。 |

**Return value:**

| Type | Description |
| --- | --- |
| string | 返回sdk版本。 |

## Examples

```TypeScript
import { huks } from '@kit.UniversalKeystoreKit';

/* Set options to emptyOptions. */
let emptyOptions: huks.HuksOptions = {
  properties: []
};
let result = huks.getSdkVersion(emptyOptions);
```

