# transcode

## 导入模块

```TypeScript
import { buffer } from 'kits/@kit.ArkTS';
```

## transcode

```TypeScript
function transcode(source: Buffer | Uint8Array, fromEnc: string, toEnc: string): Buffer
```

将Buffer或Uint8Array对象从一种字符编码重新编码为另一种。适用于需要在不同编码格式之间转换已有Buffer数据的场景。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| source | Buffer \| Uint8Array | 是 |
| fromEnc | string | 是 |
| toEnc | string | 是 |

**返回值：**

| 类型 |
| --- |
| Buffer |
