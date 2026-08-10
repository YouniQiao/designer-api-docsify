# createMac

## Modules to Import

```TypeScript
import { cryptoFramework } from 'kits/@kit.CryptoArchitectureKit';
```

## createMac

```TypeScript
function createMac(algName: string): Mac
```

创建消息认证码实例。

&lt;br&gt;支持的规格详见[HMAC消息认证码算法规格](../../../security/CryptoArchitectureKit/crypto-compute-mac-overview.md)。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-cryptoFramework-function createMac(algName: string): Mac--><!--Device-cryptoFramework-function createMac(algName: string): Mac-End-->

**System capability:** 
- API version 12 and later: SystemCapability.Security.CryptoFramework.Mac
- API version 9 to 11: SystemCapability.Security.CryptoFramework

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| algName | string | Yes | 指定摘要算法，支持算法请参考 [HMAC消息认证码算法规格](../../../security/CryptoArchitectureKit/crypto-compute-mac-overview.md)。 |

**Return value:**

| Type | Description |
| --- | --- |
| [Mac](arkts-cryptoarchitecture-cryptoframework-mac-i.md) | 返回对应算法的Mac实例。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | 非法入参。可能的原因： &lt;br&gt;1. 必填参数未指定； &lt;br&gt;2. 参数类型不正确； &lt;br&gt;3. 参数验证失败。 |
| 17620001 | 内存操作失败。 |

## Examples

```TypeScript
import { cryptoFramework } from '@kit.CryptoArchitectureKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  // Set algName based on the algorithm supported.
  let mac = cryptoFramework.createMac('SHA256');
} catch (error) {
  let e: BusinessError = error as BusinessError;
  console.error(`sync failed: errCode: ${e.code}, errMsg: ${e.message}`);
}
```


## createMac

```TypeScript
function createMac(macSpec: MacSpec): Mac
```

创建消息认证码实例。

&lt;br&gt;支持的规格详见[MAC消息认证码算法规格](../../../security/CryptoArchitectureKit/crypto-compute-mac-overview.md)。

**Since:** 18

**ArkTS mode:** ArkTS-Dyn since version 18; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-cryptoFramework-function createMac(macSpec: MacSpec): Mac--><!--Device-cryptoFramework-function createMac(macSpec: MacSpec): Mac-End-->

**System capability:** SystemCapability.Security.CryptoFramework.Mac

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| macSpec | [MacSpec](arkts-cryptoarchitecture-cryptoframework-macspec-i.md) | Yes | 根据消息认证码的不同算法，指定入参参数，支持算法请参考 [MAC消息认证码算法规格](../../../security/CryptoArchitectureKit/crypto-compute-mac-overview.md)。 |

**Return value:**

| Type | Description |
| --- | --- |
| [Mac](arkts-cryptoarchitecture-cryptoframework-mac-i.md) | 返回对应算法的Mac实例。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | 非法入参。可能的原因： &lt;br&gt;1. 必填参数未指定； &lt;br&gt;2. 参数类型不正确； &lt;br&gt;3. 参数验证失败。 |
| 17630001 | 密码操作错误。 |
| 17620001 | 内存操作失败。 |
| 17620002 | 获取Native对象失败或参数转换失败。 |

## Examples

```TypeScript
import { cryptoFramework } from '@kit.CryptoArchitectureKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  // Set algName based on the algorithm supported.
  let spec: cryptoFramework.HmacSpec = {
    algName: 'HMAC',
    mdName: 'SHA256',
  };
  let mac = cryptoFramework.createMac(spec);
} catch (error) {
  let e: BusinessError = error as BusinessError;
  console.error(`sync failed: errCode: ${error.code}, errMsg: ${error.message}`);
}
```

