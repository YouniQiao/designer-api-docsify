# getInstance

## 导入模块

```TypeScript
```

## getInstance

```TypeScript
export function getInstance(locale?:string): IndexUtil
```

创建并返回IndexUtil对象。

**起始版本：** 23

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-i18n-export function getInstance(locale?:string): IndexUtil--><!--Device-i18n-export function getInstance(locale?:string): IndexUtil-End-->

**系统能力：** SystemCapability.Global.I18n

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| locale | string | 否 |

**返回值：**

| 类型 |
| --- |
| [IndexUtil](arkts-localization-i18n-indexutil-c.md) |

**示例**

```TypeScript
import { i18n } from '@kit.LocalizationKit';

let indexUtil: i18n.IndexUtil = i18n.getInstance('zh-CN');
```
