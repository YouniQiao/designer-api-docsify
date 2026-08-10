# SymKey

对称密钥，是[Key](arkts-cryptoarchitecture-cryptoframework-key-i.md)的子类，在对称加解密时需要将其对象传入  
[Cipher](arkts-cryptoarchitecture-cryptoframework-cipher-i.md)实例的  
[init()](arkts-cryptoarchitecture-cryptoframework-cipher-i.md#init)方法使用。

&lt;br&gt;对称密钥通过对称密钥生成器[SymKeyGenerator](arkts-cryptoarchitecture-cryptoframework-symkeygenerator-i.md)来生成。

**Inheritance/Implementation:** SymKey extends [Key](arkts-cryptoarchitecture-cryptoframework-key-i.md)

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-cryptoFramework-interface SymKey extends Key--><!--Device-cryptoFramework-interface SymKey extends Key-End-->

**System capability:** 
- API version 12 and later: SystemCapability.Security.CryptoFramework.Key.SymKey
- API version 9 to 11: SystemCapability.Security.CryptoFramework

## Modules to Import

```TypeScript
import { cryptoFramework } from 'kits/@kit.CryptoArchitectureKit';
```

## clearMem

```TypeScript
clearMem(): void
```

同步方法，将系统底层内存中的密钥数据清零。建议在不再使用对称密钥实例时调用此函数，避免密钥数据在内存中存留过久。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-SymKey-clearMem(): void--><!--Device-SymKey-clearMem(): void-End-->

**System capability:** 
- API version 12 and later: SystemCapability.Security.CryptoFramework.Key.SymKey
- API version 9 to 11: SystemCapability.Security.CryptoFramework

## Examples

```TypeScript
import { cryptoFramework } from '@kit.CryptoArchitectureKit';

async function testGenerateAesKeyFun() {
  let symKeyGenerator = cryptoFramework.createSymKeyGenerator('AES256');
  let key = await symKeyGenerator.generateSymKey();
  let encodedKey = key.getEncoded();
  console.info('key blob: '+ encodedKey.data);
  key.clearMem();
  encodedKey = key.getEncoded();
  console.info('key blob: ' + encodedKey.data);
}
```

