# compare

## 导入模块

```TypeScript
import { buffer } from 'kits/@kit.ArkTS';
```

## compare

```TypeScript
function compare(buf1: Buffer | Uint8Array, buf2: Buffer | Uint8Array): -1 | 0 | 1
```

返回两个Buffer或Uint8Array对象的比较结果，通常用于对Buffer或Uint8Array对象数组进行排序。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| buf1 | Buffer \| Uint8Array | 是 |
| buf2 | Buffer \| Uint8Array | 是 |

**返回值：**

| 类型 |
| --- |
| -1 \| 0 \| 1 |
