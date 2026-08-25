# getHash

## 导入模块

```TypeScript
import { util } from 'kits/@kit.ArkTS';
```

## getHash

```TypeScript
function getHash(object: object): number
```

获取对象的哈希值。 如果尚未获取过哈希值，则生成一个随机哈希值，保存到对象的 **hash** 字段中并返回。如果已经获取过哈希值，则返回保存在 **hash** 字段中的哈希值（同一对象返回相同的值）。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| object | object | 是 |

**返回值：**

| 类型 |
| --- |
| number |
