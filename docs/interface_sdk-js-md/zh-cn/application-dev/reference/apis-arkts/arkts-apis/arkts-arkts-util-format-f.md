# format

## 导入模块

```TypeScript
import { util } from 'kits/@kit.ArkTS';
```

## format

```TypeScript
function format(format: string, ...args: Object[]): string
```

使用样式化字符串将输入内容按特定格式输出，适用于日志输出、用户界面文本格式化等场景。

**起始版本：** 9

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [format](#format) | string | 是 |
| [args](../../apis-arkdata/arkts-apis/arkts-arkdata-relationalstore-sqlinfo-i.md) | Object[] | 是 |

**返回值：**

| 类型 |
| --- |
| string |
