# parse

## 导入模块

```TypeScript
import { ArkTSUtils } from 'kits/@kit.ArkTS';
```

## parse

```TypeScript
function parse(text: string, reviver?: Transformer, options?: ParseOptions): ISendable | null
```

用于解析JSON字符串生成ISendable数据或null。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| text | string | 是 |
| reviver | [Transformer](arkts-arkts-ason-transformer-t.md) | 否 |
| options | [ParseOptions](arkts-arkts-json-parseoptions-i.md) | 否 |

**返回值：**

| 类型 |
| --- |
| ISendable \| null |
