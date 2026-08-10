# HuksReturnResult

调用接口返回的result。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

<!--Device-huks-export interface HuksReturnResult--><!--Device-huks-export interface HuksReturnResult-End-->

**System capability:** SystemCapability.Security.Huks.Core

## Modules to Import

```TypeScript
import { huks } from 'kits/@kit.UniversalKeystoreKit';
```

## certChains

```TypeScript
certChains?: Array<string>
```

表示证书链数据。默认为undefined。

**Type:** Array&lt;string&gt;

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-HuksReturnResult-certChains?: Array<string>--><!--Device-HuksReturnResult-certChains?: Array<string>-End-->

**System capability:** SystemCapability.Security.Huks.Core

## outData

```TypeScript
outData?: Uint8Array
```

表示  
[initSession](arkts-universalkeystore-huks-initsession-f.md#initsession)操作之后获取到的challenge信息。默认为undefined。

**Type:** Uint8Array

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-HuksReturnResult-outData?: Uint8Array--><!--Device-HuksReturnResult-outData?: Uint8Array-End-->

**System capability:** SystemCapability.Security.Huks.Core

## properties

```TypeScript
properties?: Array<HuksParam>
```

表示  
[initSession](arkts-universalkeystore-huks-initsession-f.md#initsession)操作之后获取到的challenge信息。默认为undefined。

**Type:** Array&lt;HuksParam&gt;

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-HuksReturnResult-properties?: Array<HuksParam>--><!--Device-HuksReturnResult-properties?: Array<HuksParam>-End-->

**System capability:** SystemCapability.Security.Huks.Core

## sharedSecret

```TypeScript
sharedSecret?: Uint8Array
```

定义共享密钥。

**Type:** Uint8Array

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-HuksReturnResult-sharedSecret?: Uint8Array--><!--Device-HuksReturnResult-sharedSecret?: Uint8Array-End-->

**System capability:** SystemCapability.Security.Huks.Core

