# MacSpec

消息认证码参数，计算HMAC或CMAC时，需要构建子类对象并作为输入参数。

> **说明：**
> 
> algName是必选参数，表示消息认证码算法。

**Since:** 18

**ArkTS mode:** ArkTS-Dyn since version 18; ArkTS-Sta since version 23.

<!--Device-cryptoFramework-interface MacSpec--><!--Device-cryptoFramework-interface MacSpec-End-->

**System capability:** SystemCapability.Security.CryptoFramework.Mac

## Modules to Import

```TypeScript
import { cryptoFramework } from 'kits/@kit.CryptoArchitectureKit';
```

## algName

```TypeScript
algName: string
```

消息认证码算法名。

**Type:** string

**Since:** 18

**ArkTS mode:** ArkTS-Dyn since version 18; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-MacSpec-algName: string--><!--Device-MacSpec-algName: string-End-->

**System capability:** SystemCapability.Security.CryptoFramework.Mac

