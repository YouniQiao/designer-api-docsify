# generateRandomUUID

## Modules to Import

```TypeScript
import { util } from 'kits/@kit.ArkTS';
```

## generateRandomUUID

```TypeScript
function generateRandomUUID(entropyCache?: boolean): string
```

使用加密安全的随机数生成器生成随机的RFC 4122版本4 UUID。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-util-function generateRandomUUID(entropyCache?: boolean): string--><!--Device-util-function generateRandomUUID(entropyCache?: boolean): string-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| entropyCache | boolean | No | 是否使用缓存生成UUID。默认值：true。 |

**Return value:**

| Type | Description |
| --- | --- |
| string | 返回表示此UUID的字符串。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | 参数错误。可能的原因：1.参数类型不正确。 |

