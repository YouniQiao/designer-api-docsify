# isEncoding

## 导入模块

```TypeScript
```

## isEncoding

```TypeScript
function isEncoding(encoding: string): boolean
```

判断`encoding`是否为支持的编码格式。

**起始版本：** 23

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-buffer-function isEncoding(encoding: string): boolean--><!--Device-buffer-function isEncoding(encoding: string): boolean-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| encoding | string | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |

**示例**

```TypeScript
import { buffer } from '@kit.ArkTS';

console.info(buffer.isEncoding('utf-8').toString());
// 输出结果：true
console.info(buffer.isEncoding('hex').toString());
// 输出结果：true
console.info(buffer.isEncoding('utf/8').toString());
// 输出结果：false
console.info(buffer.isEncoding('').toString());
// 输出结果：false
```
