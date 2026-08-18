# createHash

## 导入模块

```TypeScript
```

## createHash

```TypeScript
function createHash(algorithm: string): HashStream
```

创建并返回 HashStream 对象，该对象可用于使用给定的 algorithm 生成哈希摘要。

**起始版本：** 23

<!--Device-hash-function createHash(algorithm: string): HashStream--><!--Device-hash-function createHash(algorithm: string): HashStream-End-->

**系统能力：** SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [algorithm](../../apis-device-certificate-kit/arkts-apis/arkts-devicecertificate-cert-certchainvalidator-i.md) | string | 是 |

**返回值：**

| 类型 |
| --- |
| [HashStream](arkts-corefile-hash-hashstream-c.md) |

**错误码：**

| 错误码ID |
| --- |
| 13900020 |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| 13900042 |

**示例**

```TypeScript
// pages/xxx.ets
import { fileIo } from '@kit.CoreFileKit';

function hashFileWithStream() {
  const filePath = pathDir + "/test.txt";
  // 创建文件可读流
  const rs = fileIo.createReadStream(filePath);
  // 创建哈希流
  const hs = hash.createHash('sha256');
  rs.on('data', (emitData) => {
    const data = emitData?.data;
    hs.update(new Uint8Array(data?.split('').map((x: string) => x.charCodeAt(0))).buffer);
  });
  rs.on('close', async () => {
    const hashResult = hs.digest();
    const fileHash = await hash.hash(filePath, 'sha256');
    console.info(`Succeeded in calculating file hash. hashResult: ${hashResult}, fileHash: ${fileHash}`);
  });
}
```
