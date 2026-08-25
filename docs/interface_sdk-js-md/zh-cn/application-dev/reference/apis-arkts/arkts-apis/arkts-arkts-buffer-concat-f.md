# concat

## 导入模块

```TypeScript
import { buffer } from 'kits/@kit.ArkTS';
```

## concat

```TypeScript
function concat(list: Buffer[] | Uint8Array[], totalLength?: number): Buffer
```

将数组中的内容复制（默认复制全部内容，或复制指定字节长度）到新的Buffer对象中并返回。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| list | Buffer[] \| Uint8Array[] | 是 |
| [totalLength](../../apis-arkui/arkts-components/arkts-arkui-computedbarattribute-i.md) | number | 否 |

**返回值：**

| 类型 |
| --- |
| Buffer |

**错误码：**

| 错误码ID |
| --- |
| [10200001](../errorcode-utils.md#10200001-参数范围越界错误) |
