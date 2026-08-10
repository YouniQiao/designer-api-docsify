# unwrapKeyItem

## Modules to Import

```TypeScript
import { huks } from 'kits/@kit.UniversalKeystoreKit';
```

## unwrapKeyItem

```TypeScript
function unwrapKeyItem(keyAlias: string, params: HuksOptions, wrappedKey: Uint8Array): Promise<HuksReturnResult>
```

加密导入密钥。使用Promise异步回调。

> **说明：**
> 
> 加密导入[HuksKeySecurityLevel](arkts-universalkeystore-huks-hukskeysecuritylevel-e.md)中定义的SE安全级别密钥需要ohos.permission.ACCESS_SE_KEY权限。

&lt;!--Del--&gt;该功能暂不支持。&lt;!--DelEnd--&gt;

**Since:** 20

**ArkTS mode:** ArkTS-Dyn only, since version 20.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-huks-function unwrapKeyItem(keyAlias: string, params: HuksOptions, wrappedKey: Uint8Array): Promise<HuksReturnResult>--><!--Device-huks-function unwrapKeyItem(keyAlias: string, params: HuksOptions, wrappedKey: Uint8Array): Promise<HuksReturnResult>-End-->

**System capability:** SystemCapability.Security.Huks.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| keyAlias | string | Yes | 密钥别名，指定导入密钥的密钥别名。 |
| params | [HuksOptions](arkts-universalkeystore-huks-huksoptions-i.md) | Yes | 用于指定导入密钥时的加密类型。 |
| wrappedKey | Uint8Array | Yes | 加密导出密钥的密文。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;HuksReturnResult&gt; | Promise对象，返回调用接口的结果。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 801 | api is not supported |
| 12000005 | IPC communication failed |
| 12000004 | operating file failed |
| 12000018 | the input parameter is invalid |
| 12000015 | Failed to obtain the security information via UserIAM |
| 201 | The application permissions are insufficient, possibly because the ohos.permission.ACCESS_SE_KEY permission is missing.<br>**Applicable version:** 26.0.0 and later |
| 12000014 | memory is insufficient |
| 12000012 | Device environment or input parameter abnormal |
| 12000026 | the secure element is not available<br>**Applicable version:** 26.0.0 and later |

